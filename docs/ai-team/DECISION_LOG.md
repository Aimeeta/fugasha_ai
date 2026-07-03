# DECISION_LOG — 意思決定の記録

新しい決定は上に追記する。形式: 日付 / 決定 / 理由 / 決定者。

## 2026-07-03 — エージェント運用をPlaybook v2に統合
20体のエージェントに read-only / write-capable の区分とツール制限を導入。タスクごとに最小分隊のみ招集（20体同時起動禁止）。Agent Teamsは実験的機能のため使わない。`.claude/agents/` をバージョン管理下に移動（settings.local.json 等は除外のまま）。

## 2026-07-03 — OGPはネイビー基調
`ogp.jpg` はブログOGP（generate_ogp.py の ai-dx カテゴリ）と同じ配色文法のネイビー基調。ユーザー指定。再生成ソースは `ogp-source.html`。

## 2026-07-03 — Three.js / GSAP を導入しない
13専門家レビューで提案されたが、憲法（Performance > Simplicity > Novelty loses）により却下。既存の 2D canvas + IntersectionObserver + CSS transition の体系内で磨く。再提案する場合は「既存手段では不可能または著しく劣る」ことの立証が必要。

## 2026-07-03 — Tabler webフォント廃止 → インラインSVG 9種
使用9アイコンのためにwebフォント全体を配信していたため。副次効果としてサイト独自 `.ti` クラスとの衝突も解消。

## 2026-07-03 — 見出しのみ palt 適用
表示見出しに `font-feature-settings: 'palt'`。本文は読み速度優先で全角のまま。

## 2026-07-03 — ケース横スクロールのホイール奪取を削除
縦スクロールを止める悪パターンのため。ネイティブスクロール＋ドラッグ＋スナップは維持。

## 2026-07-02（前セッション） — 静けさの設計
タイプライター演出・ライブ時計・ティッカー・カスタムカーソル・磁石ボタン等を削除。Philosophyセクション新設。数字の約束を廃止（幅表示＋観察形へ）。詳細は `fugasha_handoff_brief_current.docx`。
