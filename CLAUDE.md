# 風雅舎 (fugasha_ai) — プロジェクト運用ガイド

静的サイト。LP本体は `index.html` 単一ファイル（CSS/JSインライン）。ビルドなし・GitHub Pages公開。
**push＝本番公開**。push はユーザーの明示指示があるまで行わない。

## サイトの憲法

常にこう感じられること: Premium / Timeless / Intelligent / Calm / Curious / Human / Minimal / Research-driven。
決して犠牲にしないもの: Accessibility / Performance / Readability / Maintainability。

**意思決定の優先順位**（衝突したらこの順で勝つ）:
1. 安全とデータ保護 → 2. アクセシビリティ → 3. 正しさ → 4. ユーザー理解 → 5. パフォーマンス → 6. 保守性 → 7. ブランド一貫性 → 8. 事業価値 → 9. 視覚的洗練 → 10. 新規性。
新規性がユーザビリティに勝つことはない。どの項目も改善しない演出は実装しない。

## スタックの事実（要点）

- 外部JS依存は **Lenis のみ**。Three.js / GSAP は「導入しない」判断済み（docs/ai-team/DECISION_LOG.md）
- アイコンはインラインSVG（Tabler由来）。webフォントアイコンは使わない
- フォント: Google Fonts — Zen Kaku Gothic New (400/500/700) / Noto Serif JP (300/400)。等幅は `--font-mono`（`ui-monospace, 'SF Mono', 'Cascadia Mono', Menlo, Consolas, 'Liberation Mono', monospace` のOS標準スタック。JetBrains Mono等のWebフォントは読み込まない）。**読み込んでいないウェイトをCSSで指定しない**（疑似ボールド禁止）
- スクロール演出は IntersectionObserver + CSS transition。canvasは画面外で停止させる
- 検証手段: `node --check`（inline JS抽出後）、タグ整合カウント、ローカルサーバーでのブラウザ確認
- 詳細は docs/ai-team/PROJECT_FACTS.md

## ブランドの声

- 営業感・誇大数字の禁止。数字は幅表示（30〜50%）＋仮定明記＋観察形
- コンサル用語（棚卸し・導線・定着・見える化）→ 書き手の語彙（書き出す・洗い出す・分ける・整える）
- 詳細は docs/ai-team/BRAND_PRINCIPLES.md

## エージェント運用

`.claude/agents/` に20体。**タスクごとに最小の分隊だけ招集**する。20体同時起動は禁止。

- 小タスク: 1–2体 / 中: 3–4体 / 大機能: 4–6体 / 全体監査: 波（wave）に分けて実行
- **助言系（読み取り専用）**: technical-pm, creative-director, lead-product-designer, first-visit-researcher, brand-philosopher, brand-copywriter, typography-specialist, visual-designer, interaction-designer, motion-designer, seo-aeo-auditor, design-critic, awwwards-judge
- **実装系（write可）**: frontend-engineer, project-architect, creative-coder, threejs-engineer, gsap-engineer（+ a11y-auditor / performance-auditor は検証済み問題の修正を明示依頼されたときのみwrite）
- 同一ファイルを2体が同時編集しない。並列実装はworktreeで隔離
- 実装は書いた本人以外が1体レビューする（cross-review）
- Agent Teams は実験的機能のため自動で有効化しない

### 分隊選択の目安

| タスク | 分隊 |
|---|---|
| 小さな修正 | frontend-engineer（必要なら a11y-auditor） |
| 新UIコンポーネント | lead-product-designer + interaction-designer + frontend-engineer + a11y-auditor |
| 新ページ | technical-pm + creative-director + lead-product-designer + first-visit-researcher + frontend-engineer → 後の波で copy/typography/SEO/a11y/perf |
| ヒーロー級インタラクション | creative-director + lead-product-designer + interaction-designer + creative-coder + performance-auditor + a11y-auditor |
| コピー・コンテンツ | first-visit-researcher + brand-copywriter + seo-aeo-auditor |
| リリース前レビュー | Wave1: frontend-engineer + project-architect + a11y-auditor + performance-auditor + seo-aeo-auditor → Wave2: lead-product-designer + design-critic + awwwards-judge |

## 証拠基準

すべての報告は次を区別する: 検証済み事実 / リポジトリ観察 / 計測結果 / 推論 / 主観的推奨 / 未検証の仮定。
「パフォーマンスは完璧」等の曖昧な断言は禁止。ファイル・セレクタ・行を特定して書く。
**テスト未実行のまま「問題なし」と報告しない。** 実行できなかった検証は、何を・なぜ・どう確認すればよいかを開示する。

## Git安全規則

- push禁止（明示指示があるまで）/ force push・reset --hard・clean 禁止
- 編集前に `git status` を確認し、ユーザーの未コミット変更を消さない
- シークレット・環境変数をコミットしない

## 完了の定義

要求挙動の実装 + スコープ一致 + 実行可能な検証の実施 + キーボード/reduced-motion/レスポンシブの考慮 + 変更ファイルの報告 + 未検証領域の開示。**「見た目OK」は完了条件ではない。**

## 運用ドキュメント

- docs/ai-team/PROJECT_FACTS.md — スタックの事実
- docs/ai-team/BRAND_PRINCIPLES.md — ブランド原則・声・配色・タイポ
- docs/ai-team/AUDIT_REPORT.md — 監査結果（対応状況つき）
- docs/ai-team/ROADMAP.md — 優先順位つき残タスク
- docs/ai-team/DECISION_LOG.md — 意思決定の記録（Three.js却下等）
- docs/ai-team/QUALITY_REPORT.md — 最新の検証結果

大きめのタスク完了時は DECISION_LOG / ROADMAP / QUALITY_REPORT を更新する。
