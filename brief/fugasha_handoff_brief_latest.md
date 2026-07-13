# 風雅舎 Webサイト引き継ぎブリーフ

最新版: 2026-07-13 / 対象: fugasha_ai リポジトリ全体（2026-07-08ブリーフ以降のすべての更新）

## 1. 現在地

2026-07-08時点のブリーフ（Focus Clock全面拡張）以降、5日間で以下が加わりました。

- トップページ・英語版の a11y/レスポンシブ/SEO監査と修正
- focus.html のさらなる磨き込み（進捗リング・完了演出・統計・ショートカット拡充）
- ブログ記事4本追加（AIトレンド2本＋実務系2本）
- **Color Generator（colors.html）** 新規追加
- **ことば（words.html）** 新規追加 — 名言84件の没入型ページ
- **AI Daily News 自動生成パイプライン**（GitHub Actions）導入
- **Today（today.html）** 新規追加 — デジタル・アルマナック。words.html の名言を統合し、Focus からは名言機能を撤去
- **Sky Tonight（sky.html）** 新規追加 — 今夜の月の和名・流星群ごよみ・日の入り（外部API不使用、天文計算はNodeハーネスで検証済み）
- **余白（yohaku.html）** 新規追加 — Focus/Today/Sky/Words を集めた目次ハブ。グローバルナビを `Home / 余白 / Colors / Blog（/Contact）` に統合（EN: Yohaku）
- 余白ページの**多エージェント改修**（4体並列レビュー→統合→実装→a11y cross-review）
- Today「この日、世界では」の**空状態を廃止**し、毎日必ず実在の出来事が出るよう修正

現在の `main` は `origin/main` と一致（push済み）。ローカルにサイト関連の未コミット差分はありません（`brief/` の旧ドラフト群のみ未コミットで残存、本ブリーフ作成時点の作業とは無関係）。

公開済みコミット（前回ブリーフ以降・直近が先頭）:

```
fd1f54c Improve yohaku.html via multi-agent review; fix Today's empty-day fallback
f422f24 Add 余白 (Yohaku) hub + Sky Tonight; consolidate global nav
7e4324c Add Sky Tonight page — Japanese moon names, computed in-browser
1118fac Add Today almanac page; move quotes out of Focus into Today
20a9d2e Merge pull request #1 from Aimeeta/ai-daily/2026-07-12
0ce7b95〜13081e9 AI Daily News: 初回下書き記事・失敗表示・feed追加・temperatureパラメータ修正
293a140 Add AI Daily News automation (GitHub Actions + zero-dependency pipeline)
9646057 Add Words page (words.html): 84 quotes with mood filters and daily quote
d7198da Add Color Generator page (colors.html)
6401e75 Humanize the site: hero byline, editorial rhythm, honest copy
a085900 Polish focus.html: progress ring, completion afterglow, shortcuts, stats
9df1b1f Fix 4 high-priority issues from full-site audit
8fcccb6 / af027d0 / 8e06167 ブログ記事4本追加・幅広画面対応
f7515af / 0bb2e3d / f49493c トップページ（JA/EN）の a11y・レスポンシブ・SEO修正
```

## 2. サイト構成の現状（ページ一覧）

グローバルナビ（全ページ共通）: **Home / 余白 / Colors / Blog / Contact**（英語版は `Yohaku`）。

| ページ | 役割 | ナビ経路 |
|---|---|---|
| `index.html` / `en/index.html` | トップページ（JA/EN） | Home |
| `yohaku.html` | **余白** — 静かなページ群の目次ハブ。各項目がその日の状態をライブ表示 | Home直下のナビ |
| `focus.html` | 集中（Focus Clock）— 時計・ポモドーロ・ToDo・音楽・背景 | 余白から |
| `today.html` | 今日（Today）— 日付ヒーロー・今日の名言・歴史・雑学・問い・行動 | 余白から |
| `sky.html` | 今夜の空（Sky Tonight）— 月の和名・流星群・日の入り | 余白から |
| `words.html` | ことば（Words）— 名言84件、気分フィルタ・お気に入り | 余白から（URL直アクセスも可） |
| `colors.html` | Color Generator — 配色パレット生成ツール | Home直下のナビ |
| `blog/` | ブログ（記事8本＋AI Daily News自動投稿） | Home直下のナビ |
| `contact.html` / `chat.html` | お問い合わせ・相談メモ | Home直下のナビ |
| `security-ai.html` / `privacy.html` | セキュリティ方針・プライバシーポリシー | フッター等 |

## 3. 2026-07-08〜07-11: 基盤の磨き込み（本ブリーフ期間の前半）

- **トップページ監査**: 5エージェントでの全体監査→高優先4件修正（07-10）。人間味監査5体+Phase0/1/2（07-11、構造的リズム改修）。a11y・レスポンシブ・SEOの追加修正（英語版含む）。
- **focus.html 磨き込み**（07-11）: creative-director/design-critic/interaction-designer/first-visit-researcherの4体精査→「進捗リング不在・主役階層が弱い・完了演出が貧弱・統計が埋もれる」に収束→進捗リングSVG新設・完了時の淡い放射演出（afterglow）・タイマーパネルへの静かな統計1行・ショートカット3種→10種への拡充とチートシート整備を実装。呼吸ガイド・週次グラフ・連続日数表示は憲法（Calm/Minimal・誇大回避）により不採用。
- **ブログ記事4本追加**: AIトレンド系2本（チャットボットからエージェントへ／試すから埋め込むへ）、実務系2本（AI導入前のルール／AI下書きの編集）。幅広画面でのレイアウト対応も実施。

## 4. 2026-07-12: 新ページ群の追加ラッシュ

### Color Generator（colors.html）
配色パレット生成ツール。企画4体＋実装＋クロスレビュー2体で完成。push済み。

### ことば（words.html）
名言84件（出典の確かな古典のパブリックドメイン＋風雅舎オリジナルのみ）の没入型ページ。気分フィルタ・お気に入り・書き置き・コピー/共有・没入モードを実装。企画2体＋実装＋クロスレビュー2体。**運用ルール: QUOTESは末尾追記のみ**（並べ替え・削除は共有リンク`#q=N`とお気に入りindexを破壊する）。push済み。

### AI Daily News 自動生成パイプライン
GitHub Actions（JST 7:00起動）でAI関連ニュースをまとめ記事として自動生成。n8n/microCMSは不採用とし、既存の静的サイト構成に合わせてゼロ依存の単一スクリプト＋GitHub Actionsで実装。下書き（PR）↔自動公開（`NEWS_MODE`変数）を切替可能。情報源はOpenAI News・Hugging Face Blog等の公式RSS。使用済みURLの7日間再掲防止、3件未満の日はスキップ、フィード本文はLLMへ渡すが出典URLはid引き当てで捏造防止。**現在: 実装済み・オーナーによるGitHub Secrets設定待ち**（後述「次の担当者への注意点」参照）。

### Today（today.html）— 新規・push済み
「今日と今月を、少し特別にする」デジタル・アルマナック。10セクション: 日付ヒーロー／Quote of the Day（words.htmlの84編を移設）／Today in History／This Month in History／Did You Know／The Story of This Month／Born This Month／A Question for Today／Daily Action／Sources & References。`MONTHS[1..12]`のデータ構造で全月に最小データを用意し、日別データが薄い日でも月別コンテンツで埋まる設計。**focus.htmlからは名言機能（.msg一式）を撤去**し、Todayへの控えめな導線に置換。

### Sky Tonight（sky.html）— 新規・push済み
今夜の月の和名（三日月・十三夜・立待月・居待月・寝待月・更待月など三十夜の名前）・月齢・流星群ごよみ（11群）・日の入り/日の出（8都市）を表示。**外部API不使用**、月・太陽の黄経計算（Meeus略式）と日出没計算（NOAA/Spencer近似）をブラウザ内で実行。Nodeハーネスで2017〜2026年の既知の日食・月食6件（離角誤差0.07°以内）・東京の日出没既知値（±1分）に対して検証済み。惑星の見え方はフェーズ2として見送り。

### 余白（yohaku.html）— 新規・push済み・グローバルナビ統合
Focus/Today/Sky/Wordsという「静かなページ群」を一枚の目次に集約するハブ。名前は「庭」案から発展させ、既存ブランド語彙（名言「創造は、余白のあるところに訪れる」、ブログ「余白はサボりではない」等）の回収として採用。索引の各項目がその日の状態をライブ表示（集中→現在時刻／今日→日付／今夜の空→月の和名／ことば→本日の著者）。**Colorsは余白に含めない**（オーナー指示）。全ページのグローバルナビをHome/余白/Colors/Blog(/Contact)に整理し、英語版は「Yohaku」表記。

## 5. 2026-07-13: 余白の多エージェント改修＋Todayのフォールバック修正（直近作業）

### 余白ページの磨き込み（Wave方式）
CLAUDE.mdの分隊運用に従い実施。**Wave1**（design-critic／typography-specialist／first-visit-researcher／interaction-designerを並列起動・読み取り専用）→私が統合・裁定→**Wave2**（frontend-engineerが実装）→**a11y-auditorがcross-review**、という流れ。

主な指摘の収束点: 「ライブ状態が"生きている"と伝わらない」「ホバー矢印と右端のライブ値が同じ角で衝突」「項目名と状態値が同じ明朝300で階層が潰れる」。加えてinteraction-designerが**スキップリンク破損**（`#index`の飛び先idが存在せず、WCAG 2.4.1に抵触）を発見。

実装した主な変更:
- スキップリンク修復、`aria-label`削除（ライブ状態がスクリーンリーダーに届くように）
- 右端の矢印を廃止し、ホバー時にレイアウトが動かない左の指標バー（`::before`）方式へ変更
- 実際に動く時計行にだけ脈打つドットを追加（`prefers-reduced-motion`で無効化）。時計はゼロ埋め・tabular-nums・タブ非表示で更新停止・分境界に整列
- 「余白」の字間を拡大（`.08em→.18em`）してテーマ（negative space）を字間そのもので体現。リード文にpalt適用、和文ラベルの無効なuppercase指定を削除
- 状態値の書式を和文レジスタに統一（`JULY 13`→`7月13日`）
- 索引に連番01–04を追加

**cross-reviewでの発見と対応**: a11y-auditorが6変更中5合格と判定した上で、新しいホバー指標（`::before`バー＋名前色変化）が**WCAG 2.2の2.4.11 Focus Appearance（AA）未達**（状態差コントラストが約2:1で3:1基準に届かない）と指摘。私が`.entry:focus-visible`に`--accent-ink`のoutline（コントラスト6.45:1）を復活させて解消し、実機のキーボード操作（Tab）でフォーカスリングが可視化されることを確認済み。

### Today「この日、世界では」の空状態を廃止
オーナー指摘「毎日ちゃんと出来事が出るように」に対応。その日ちょうどの出来事がない日は、**今月の中から日付の近い順に実在の出来事を4件、日付つきで表示**する設計に変更（見出しも「この日、世界では」→「この頃、世界では」に自動切替）。空メッセージは完全に廃止。あわせて7月データを拡充（ライヴエイド／ヴァスコ・ダ・ガマ出航／第1回ウィンブルドン／アポロ11号打上げ／マンデラ誕生／マチュピチュ到達／体外受精児誕生／NASA設立など）し、7月は18日分に出来事が分散。全12月に日付つき出来事があるため、どの月・どの日でも空にならない設計。

## 6. 検証済み項目

- **今回セッション分**: inline JS構文チェック（`node --check`）全ファイルOK、静的マークアップのタグ開閉カウント一致。ブラウザ実機（デスクトップ1280px・モバイル375px）で横溢れなし・コンソールエラーゼロ。ライブ状態（時計・日付・月名・著者）が各ページと整合することをDOM確認。fail-open reveal（IntersectionObserver不動でも2.5秒で必ず表示）を確認。スキップリンク・フォーカスリングを実際のキーボード操作（Tab）で確認。a11y-auditorによるコントラスト実測（背景`#efe4d3`基準）: 本文9.41:1・ラベル類6.26:1・フォーカスoutline6.45:1・スキップリンク13.4:1、いずれもAA合格。
- **Sky Tonightの天文計算**: Nodeハーネスで日食3件・月食3件の既知の瞬間、東京の日出没既知値に対して誤差を計測済み（詳細は上記4節）。
- **それ以前（07-08〜07-11分）**: 各DECISION_LOG該当項目に検証記録あり。focus.htmlの進捗リング・完了演出・統計・ショートカットは実機確認済み（既存ブリーフ・QUALITY_REPORT参照）。

## 7. 次の担当者への注意点

### すぐ対応が必要
- **AI Daily News: オーナーのSecret設定が必須**。GitHub → Settings → Secrets and variables → Actions に `ANTHROPIC_API_KEY` を追加しないと動作しない（未設定の間は安全に何もしない設計）。手動テスト→PRレビュー→`NEWS_MODE=publish`切替の順で運用開始。
- **Today: 出典のスポット確認推奨**。歴史・雑学・人物の内容はアシスタントの知識ベースで、機関URLは"参考"として提示。push＝本番のため、少なくとも当月（7月）の日付・主要事実・URLの確認が望ましい。

### 中期的なフォローアップ
- **Today**: 7月以外の月のコンテンツが7月ほどリッチでない（各月 events≥5/people≥3/facts≥3/story≥1 の最小構成）。当月が来るたびに拡充する運用を推奨。
- **Sky Tonight**: 惑星の見え方・月の出時刻はフェーズ2候補（現状未実装）。流星群データは年平均値のため、2026年個別予報との照合は任意。
- **余白**: 既知のP2として、JS無効時に索引エントリが生成されない（progressive enhancement未対応）、スキップリンクの着地がヒーロー見出しを飛ばす、ナビの英語表記に`lang`未指定、が残る。
- **「庭」シリーズ**: Seasons（七十二候）／Slow Reading（今日の一節・縦書き）／Unhurry（何もしない5分）／Life in Weeksがオーナーと合意済みの未実装候補。着手順の目安はUnhurry→Seasons→Life in Weeks→Slow Reading。実装時は余白の索引に追加する。
- **Words**: QUOTESは末尾追記のみを厳守（並べ替え・削除は共有リンクとお気に入りindexを破壊する）。

### 変わらない前提
- サイト全体の憲法（Three.js/GSAP不使用、疑似ボールド禁止、静けさ優先、push=本番でオーナー明示指示が必要 等）はCLAUDE.mdに集約。今回追加した新ページ群もすべてこの範囲内。
- Kevin MacLeod（CC BY 4.0）の音源帰属表示は削除しないこと（focus.html）。

## 8. 主要ファイル

- `yohaku.html`: 余白ハブ。静かなページ群の目次
- `today.html`: 今日のアルマナック。`MONTHS[1..12]`データ・`QUOTES`（84件）を内包
- `sky.html`: 今夜の空。天文計算（Meeus略式・NOAA近似）を内包
- `words.html`: ことば。名言84件（words.htmlが原本、today.htmlへは複製移設）
- `focus.html`: 集中ページ。名言機能は撤去済み、Todayへの導線のみ残す
- `colors.html`: Color Generatorツール
- `automation/ai-daily-news/`: AI Daily News自動生成（run.js・config.json・README.md）
- `.github/workflows/ai-daily-news.yml`: 自動生成のGitHub Actions定義
- `docs/ai-team/DECISION_LOG.md`: 本ブリーフ期間中の意思決定はすべてここに記録
- `docs/ai-team/QUALITY_REPORT.md`: 各機能の検証結果詳細
- `docs/ai-team/ROADMAP.md`: 優先順位つき残タスク（本ブリーフの「次の担当者への注意点」の詳細版）
- `brief/fugasha_handoff_brief_2026-07-13.md` / `.docx`: このブリーフの保存版。current / latest は最新参照用コピー

---

*ブリーフ作成メモ: 本書は2026-07-13時点のgit履歴・DECISION_LOG.md・QUALITY_REPORT.md・ROADMAP.mdをもとに作成。今後サイトを更新した場合は、同じ形式で保存版・current・latestを更新する（docx・md両方）。*
