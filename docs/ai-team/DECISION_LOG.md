# DECISION_LOG — 意思決定の記録

新しい決定は上に追記する。形式: 日付 / 決定 / 理由 / 決定者。

## 2026-07-03 — 相談メモ導線を「AI APIなし」で先行導入（段階導入方式）
Mihata（mihata.jp）着想の「相談前に頭の中を整える入口」を、4体分隊（first-visit-researcher / brand-copywriter / interaction-designer / lead-product-designer 統合）でブラッシュアップ後、**AI APIを使わないスクリプト制御版から始める**方式を採用（ユーザー決定）。理由: 旧 chat.html のAPI直呼びは認証ヘッダなしで動作不能、静的サイトでのキー秘匿にはサーバレスプロキシが必要（憲法1位: 安全とデータ保護）。反応が良ければ Cloudflare Workers + API に昇格する（メモ5項目・`?t=` キー・導線文言は昇格後も維持する契約）。
- chat.html を全面リビルド: 5トラック（ai/out/ops/pub/brand）×選択3問＋自由記入→相談メモ（dl 5項目）＋コピー。**fetch/localStorage 不使用**（「どこにも送信されません」をコードで保証）。API なしの間はページ・導線に「AI」を名乗らない（正しさ）
- index.html: ヒーロー二段CTA（主`相談メモをつくってみる`→chat.html / 従`30分相談を申し込む`→contact.html）＋悩みチップ3本（`?t=`受け渡し・自動送信なし）＋ドロワー縦積み二段＋CTAセクションにサブリンク。**ナビCTAは人間導線（contact.html）のまま維持**（常時可視の導線を実行時依存に向けない裁定）
- 却下: 流れる短文（ティッカー再導入）/ ナビ二段CTA / `3分だけ`等の数字の約束 / サービスカード文言の質問化（service-entryと重複）/ Calendlyへのメモ自動受け渡し / localStorage保存
- 保管: brand-copywriter のサービスカード導入一文4本（全面改稿時の素材）

## 2026-07-03 — View Transition API を採用（「ページ遷移演出」凍結の個別解除）
依存ゼロ・漸進的強化・prefers-reduced-motion で無効化する静かなクロスフェードのみのため、Novelty ではなく Calm への投資と判断。全8ページに同一スニペット。WebGL/Three.js/GSAP の凍結は継続。

## 2026-07-03 — 3D背景の再提案を審査 → 却下維持（2D格上げ案を保管）
ユーザー要望「Three.js＋R3Fで3D背景」を、本ログの再提案条件（既存手段では不可能または著しく劣ることの立証）に基づき threejs-engineer + creative-director が審査。**両者とも導入しない判断**。
- R3F は React＋バンドラ必須で「ビルドなし単一HTML」と構成上両立しない（恒久的に対象外）
- Three.js 単体は約165KB gzip 増（サイト全体約130KBの1.3倍）で Performance > Novelty に反する。唯一の候補表現（流体ノイズ）は現2D canvasが情緒の8割を達成済みで立証不成立
- 将来実験する場合は素のWebGLシェーダ（+6KB以内・依存ゼロ・2Dフォールバック必須）一択。受け入れ基準は threejs-engineer 報告に記録済み
- 代替として保管: creative-director の2D格上げ案A「紙のうえの光」（静的グレイン＋8〜12秒周期の光、推奨）／案B「余白が生まれる」（罫線が一度だけ整列して静止）。**3Dより先**: reduced-motion時の静的背景フォールバック・タッチ端末でのheroBg描画停止・canvasのDPR確認

## 2026-07-03 — 残タスク一括対応（5項目）
1) **プライバシーポリシー公開**（privacy.html）: Formspree・Google Fonts・CDN・AIツール利用の明記、全ページのフッターからリンク。事業者情報は屋号＋hello@fugasha.jp のみ（実名非掲載の方針に整合）
2) **ブログ自動更新基盤の選定**: SSG不採用、既存テンプレ＋Claude Code分隊方式を採用（blog/auto-update-brief.md に選定理由と移行条件を記録）。公開pushは必ず人間確認
3) **ツールロゴのモノクロ統一**: ブランドカラーのタイルを廃止し全てネイビー地×クリームに（商標ガイドライン対策＋静けさ）。ブログ側の残Tablerフォントも全廃しインラインSVG化、blogページのフォントウェイト削減（serif 600/300・sans 300を除去）
4) **実績数字の裏付け一覧**: private/evidence-numbers.md（gitignore済み・ローカル専用）にテンプレ作成。数字はユーザーの記入待ち
5) **FAQ+1（秘密保持）**: 「相談内容が外部に出ないか」を追加（JSON-LD同期）。「相談後の3ステップ」は過去にユーザー自身が削除した項目と衝突するため見送り継続

## 2026-07-03 — ブログ記事2本公開・記事別OGP方式を採用
「AIに任せる最初の仕事の見つけ方」(ai-dx)・「余白は、怠けではない」(work-style) を公開。執筆は brand-copywriter、監査は seo-aeo-auditor の分隊。記事OGPは category-nX.png 背景＋Chromeヘッドレスでタイトル合成（rsvg-convert不要の代替手順）。エッセイ記事のh3なしフラット構造は執筆意図として維持。新規ページのみ現行ブランド仕様（インラインSVG・静的フッター・serif 500）とし、既存記事の刷新はROADMAPへ。

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
