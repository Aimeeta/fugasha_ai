# AI Daily News — 毎朝のAIニュースまとめ自動生成

毎日 JST 7:00（GitHub Actions cron 22:00 UTC）に、公式RSSからAIニュースを取得し、
LLMで選定・日本語要約して、ブログ記事（静的HTML）として生成する。

## アーキテクチャ（なぜ n8n / microCMS ではないか）

このサイトはビルドなしの静的HTML + GitHub Pages（push＝公開）で、CMSは存在しない。
2026-07-03 の既決事項（blog/auto-update-brief.md）どおり外部CMS・SSGは導入せず、
**GitHub Actions（cron）+ Node標準ライブラリのみ**で完結させる。新サービス・新契約・
フロントエンド変更はゼロ。「下書き」はPull Request、「公開」はmainへのコミットで表現する。

```
GitHub Actions (JST 7:00)
  └─ automation/ai-daily-news/run.js
       1. config.json のRSSを取得（許可ドメインのみ・タイムアウト20s）
       2. 48h以内でフィルタ（不足時72hへ拡大）→ 使用済みURL(7日)除外 → 重複除去
       3. 候補3件未満 → その日はスキップ（架空の内容は生成しない）
       4. Anthropic API で選定・日本語要約（最大5件・JSONのみ・検証つき）
       5. template.html から記事HTML生成 → blog/ai-daily/YYYY-MM-DD/index.html
       6. blog/index.html にカード挿入・sitemap.xml 追記・used-urls.json 更新
       7. 実行ログを automation/data/runs/YYYY-MM-DD.json に保存
       8. Slack通知（SLACK_WEBHOOK_URL があれば）
  └─ mode=draft  → ブランチ ai-daily/YYYY-MM-DD で Pull Request 作成（人間が確認してマージ＝公開）
     mode=publish → main へ直接コミット（即公開）
```

## セットアップ（管理者が行うこと）

1. GitHub リポジトリの **Settings → Secrets and variables → Actions → Secrets** に追加:
   - `ANTHROPIC_API_KEY`（必須。未設定の間、workflowは何もせず正常終了する）
   - `SLACK_WEBHOOK_URL`（任意。結果通知先）
2. **Variables**（任意）:
   - `NEWS_MODE` — **未設定＝`publish`（自動公開・既定）**。`draft` にすると承認制（PR）に戻せる一時停止スイッチ
   - `NEWS_MODEL` — 既定は config.json の `claude-sonnet-5`
3. 手動実行: Actions → AI Daily News → Run workflow（modeを一時的に上書き可能）

## ローカルでのテスト

```bash
# APIキー・ネットワーク不要。モックデータで記事生成の全経路を確認
node automation/ai-daily-news/run.js --mock --date 2026-07-12

# RSS取得とパースだけ確認（LLMなし・書き込みなし）
node automation/ai-daily-news/run.js --fetch-only

# 本番同等（要 ANTHROPIC_API_KEY）。ファイルを書かずに結果表示
ANTHROPIC_API_KEY=sk-... node automation/ai-daily-news/run.js --dry-run
```

モック実行はローカルのファイルを実際に書き換える（記事・blog/index.html・sitemap.xml）。
**巻き戻しの注意**: `git checkout --` は未コミットの他の変更も一緒に消すため、
テスト前に必ず `git stash push -- blog/index.html sitemap.xml` 等で退避するか、
未コミット変更がない状態（`git status` で確認）でテストすること。戻すコマンド:

```bash
git checkout -- blog/index.html sitemap.xml   # ← 未コミット変更がないことを確認してから
rm -rf blog/ai-daily automation/data/runs
```

used-urls.json はモック実行では更新されない（本番の重複除去履歴を守るため）。

## 投稿条件（run.js に実装済み）

- 有益なニュースが **3件以上** ある場合のみ生成（LLM選定後も再チェック）
- 48時間で不足 → 72時間に拡大 → それでも不足なら**その日はスキップ**
- 過去**7日以内に使用したURL**は再掲載しない（automation/data/used-urls.json）
  - 注意: draftモードではPRがマージされるまで used-urls.json がmainに反映されないため、
    未マージのPRが溜まると同じURLが再選定されうる（レビューで気づける想定の許容リスク）
- 同じ発表の複数記事は1件に統合（URL正規化＋タイトル類似＋LLM指示）
- 同じ日付の記事が既にあれば生成しない（二重登録防止）
- ニュースがない日に架空の内容を生成しない

## セキュリティ / プロンプトインジェクション対策

- APIキーは GitHub Secrets のみ。フロントエンドには一切含まれない（静的サイトに秘密なし）
- 公開エンドポイントを持たない（cronはGitHub内部で完結。認証すべきURL自体が存在しない）
- 取得リンクは `allowedLinkDomains` のドメインのみ許可
- フィード本文は「信頼できない外部テキスト」としてLLMへ渡し、本文中の指示に従わないことをシステムプロンプトで固定。モックデータに注入テスト文を含めてある
- 出典URLはLLM出力を使わず、取得データからidで引き当て（捏造URL防止）。LLM出力にURLが混じれば拒否
- LLM出力はスキーマ検証（不明id・空文字・カテゴリ外は失敗扱い）。不正なら1回だけ再試行し、それでも駄目なら**記事を作らず失敗終了**
- 全テキストはHTML挿入時にエスケープ

## エラー時の動作

| 状況 | 動作 |
|---|---|
| 一部フィードの取得失敗 | 残りで続行（ログに記録） |
| 全フィード失敗 / LLM API失敗（リトライ後） / JSON不正（再試行後） | 記事を作らず**失敗終了** → Actionsの失敗通知＋Slack |
| ニュース不足 / 記事が既に存在 | **スキップ（正常終了）** → Slackに理由を通知 |
| API 429/5xx | 60秒待って1回リトライ |

## 将来の拡張（構造は対応済み）

- 情報源追加: config.json の `feedsDisabled` から `feeds` へ移動＋ `allowedLinkDomains` に追加
- SNS/メルマガ/Slack転用: `automation/data/runs/YYYY-MM-DD.json` に全ニュースの
  構造化データ（title / originalTitle / summary / whyItMatters / sourceName / sourceUrl /
  sourceType / publishedAt / retrievedAt / category）が残るので、これを入力にすればよい
- 既定は自動公開（`publish`）。承認制に戻したいときは Variables の `NEWS_MODE` を `draft` にするだけ
