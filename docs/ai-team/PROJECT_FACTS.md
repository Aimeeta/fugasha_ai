# PROJECT_FACTS — スタックの事実

最終更新: 2026-07-03（リポジトリ観察に基づく）

## 構成
- **種別**: ビルドなしの静的サイト。フレームワーク・パッケージマネージャ・テストランナーなし
- **LP本体**: `index.html` 単一ファイル（約2,300行、CSS/JSインライン、約130KB）
- **その他ページ**: `contact.html` / `blog/index.html` / `blog/ai-security-checkpoints/`
- **デプロイ**: GitHub Pages（`main` へのpush＝本番公開）
- **リポジトリ**: https://github.com/Aimeeta/fugasha_ai （公開URL: https://aimeeta.github.io/fugasha_ai/）

## 依存
- **JS**: Lenis 1.1.14（CDN, defer, smooth scroll）のみ。Three.js / GSAP は不採用（DECISION_LOG参照）
- **フォント**: Google Fonts — Zen Kaku Gothic New (400/500/700) / Noto Serif JP (300/400)。等幅は `--font-mono`（`ui-monospace, 'SF Mono', 'Cascadia Mono', Menlo, Consolas, 'Liberation Mono', monospace` のOS標準スタック。JetBrains Mono等のWebフォントは読み込まない）。読み込んでいないウェイトをCSSで指定しない
- **アイコン**: インラインSVG（Tabler outline由来、stroke=currentColor）。webフォントアイコンは廃止済み
- **ツールロゴ**: simpleicons CDN（`onerror` フォールバックあり）

## 実装パターン
- スクロール出現: IntersectionObserver → `.visible` クラス → CSS transition（イージングは `cubic-bezier(.16,1,.3,1)` に統一）
- canvas 2種（ヒーロー: マウス追従グラデ / CTA: 波）— 画面外・タブ非表示で rAF 停止
- 見出しの単語リビール: `splitTextIntoWords()`（対象: `.h-h1` `.ah2` `.ch2`）
- 見出しは `font-feature-settings: 'palt'` で約物詰め（本文は全角のまま）
- reduced-motion: グローバルで transition/animation を 0.01ms 化、Lenis・canvas・自動スライダー停止

## 検証手段（テストランナーがないため）
1. inline JS 抽出 → `node --check`
2. div/section/button/svg 等のタグ整合カウント
3. ローカルサーバー（`.claude/launch.json` の static-site / autoPort）でブラウザ確認（コンソールエラー・主要インタラクション）

## SEO/AEO資産
- `robots.txt`: AIクローラー（GPTBot/ClaudeBot/PerplexityBot等）個別許可の構成
- `sitemap.xml`: 手動管理（ブログ増加時はActions自動生成へ移行推奨）
- JSON-LD: ProfessionalService / WebSite / Person / FAQPage
- OGP: `ogp.jpg`（1200×630, ネイビー基調）。再生成ソースは `ogp-source.html`（Chromeヘッドレスでスクリーンショット）
- ブログOGP: `generate_ogp.py`（要 rsvg-convert 環境）
