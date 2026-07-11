# 辛口レビュー：単調さの解剖 — 「AIで作った感」の正体（design-critic）

このサイトは**丁寧に整えられた同じ1枚のカードを、13回コピーして縦に並べたもの**。

## 1. セクションの同質性 — レイアウトパターンは実質3種類
検証済み事実: index.html の本文13セクションのうち、9セクションが完全に同一の開始儀式（`.s-lbl`ピル → `.s-h2` serif 38px固定 → `.s-desc` 15px/max-width 480px → グリッド）。行番号: index.html:1606, 1619, 1653, 1706, 1822, 1850, 1867, 1941, 1999。

| パターン | セクション | 数 |
|---|---|---|
| A: ラベル＋見出し＋リード＋3カラムグリッド | SIGNS(1605), SERVICES(1652), WAYS OF WORKING(1705), PHILOSOPHY(1821), BLOG(1998) | 5連発 |
| B: ラベル＋見出し＋2カラムパネル | MARGIN MAP(1618), SECURITY(1849), ABOUT(1866) | 3 |
| C: それ以外 | Hero, Tools帯, Vision(sst), FAQ, CTA | 5 |

さらに: 全セクションの縦余白が単一ルール `.sec { padding: clamp(80px, 9vw, 120px) }`（:505）、セクション開始演出も全部同じ「168pxの線がscaleXで伸びる」（:506-512）。13回同じ幕開け。

## 2. カードの均質性
検証済み事実: `font-family: var(--font-mono)` は19回、`glass-card` は17回。次の8コンポーネントが事実上同じDNA:
`.h-chip-num`（:372）、`.sign-num`（:617）、`.margin-step-num`（:572）、`.sv-num`（:658）、`.case-step-k`（:685）、`.phi-num`（:975）、`.security-list span`（:1076）、`.sst-tag`（:907）。
全部「mono 10px / letter-spacing .12〜.18em / accent-ink または hint 色」。ホバーも全カード共通で `border-color: rgba(232,134,106,.24)` になるだけ（:647, :676, :613, :571 ほか6箇所以上）。カードが違う情報を運んでいるのに視覚的には全員同じ制服。

## 3. リズムの欠如
検証済み事実: `.sec-light` は `#f0e6d6`、`.sec-white` は `#f8f3ea`（:513-514）— 差がわずかで背景交互のリズムは知覚されない。ダーク面は Vision（:1740）、BLOG（:589のネイビーグラデ）、CTA（:2026）の3つだけ。
Visionのスクロールストーリーテリング（:1740-1818）はページ唯一の「事件」で良くできているが、Heroから約5セクション同じ密度が続く。緩急は「中中中中中強中中中中中強」。強が来るのが遅すぎる。
主観的推奨: フルブリード要素がヒーローcanvasとVision以外にゼロ。SERVICESとWAYS OF WORKINGの間に「余白そのものが主役のほぼ空のセクション」（大きなserif一文だけ）を。

## 4. タイポの単調さ — 全見出しが「安全な38px」に収監
検証済み事実:
- `.s-h2` は38px固定（:527）。clampすらない。`--text-2xl/3xl/4xl`（36/48/60px, :183-185）を定義しながら**60pxはどこにも登場しない**。
- 見出しサイズ実測分布: h1 34-56px(clamp) / sst-h2 44px / ch2 42px / s-h2 38px / ah2 28px / margin-note-t 24px / phi-t 21px / sv-t 20px / sign-t 19px。28〜44pxの中間帯に密集、ジャンプ率が小さい。
- footer矛盾: blogのタグラインは `clamp(28px, 4.6vw, 56px)` の大型serif（blog/index.html:150）なのに、index側の同クラス `.ft-tagline-big` は16px（index.html:1124-1128）。サイトで一番大きな文字がLPでなくブログのフッターにある。blog側はserifに `text-transform: uppercase` で品位を落としている。
- serif 300ウェイトを44px超で使う場面が無く、Noto Serif JPの美しさが一度も全開にならない。

## 5. 色の臆病さ
検証済み事実: `--accent: #e8866a` がフル彩度で塗られるのは `.btn-amber` / `.nav-cta` / `.cta-btn-amber` / プログレスバー / スライダーのみ。他は全て `rgba(232,134,106,.1)`〜`.4` の希釈形。面としてのアクセントカラーがCTAボタン以外に存在しない。
`.margin-note`（:539-544, 左罫＋8%グラデ）は良い方向の芽。あの温度をあと2箇所に。

## 6. 装飾・イラスト・図版の不在
検証済み事実: index.html内の `<img>` は `aimee-portrait.jpg` 1枚のみ（:1870）、しかも `filter: grayscale(1)`（:1010）。唯一の人間の顔から色を抜いている。
Visionの「写真」はCSS図形（:762-847）。方眼紙背景（:548-555）含め、図的表現はすべて定規で引いた抽象幾何。遊び心はソースコメント（:1469-1474）・console・コナミ・`.ph-badge` 裏返し名刺（:1012-1021）に隠されているが、隠れた遊び心は初回訪問者には存在しないのと同じ。
推奨: ①ポートレートのグレースケールを外すかダブルトーンに。②MARGIN MAPの3ステップを実際の手書きメモ写真に。「書き出す」を売る人のサイトに書かれた紙が一枚も写っていないのは致命的。

## 7. blog
- blog/index.html:124-142 — 8記事すべて同一カード。フィーチャード記事なし、サムネなし、カテゴリ色分けなし。8連同型は雑誌ではなく在庫一覧。
- カテゴリタグ（:117-121）はリンクですらない飾り。
- ブランド違反: blog/index.html:130 の `.card:hover { transform: translateY(-2px) }` は BRAND_PRINCIPLES.md:22「hoverの跳ね上げ禁止」違反。index.html:369 の `.h-chip:hover`、contact.html:156 の `.check-item:hover` も同罪。
- 記事ページ（margin-is-not-laziness）: `.art-body` はh2と段落しか存在しない（:213-218）。pull quote・小さな図・区切りが皆無で6分の記事が灰色の柱。
- 角丸がページ間でバラバラ: 記事TOC 6px / cta-box 8px / sidebar-cta 10px / LPカード12/18px / contact 24px。

## 8. focus.html / chat.html — ここに「私らしさ」が既にある
focus.html はテーマ名「生成り／宵／苔／霞」（:2, :50-64）、afterglow演出（:86-89）、ことばの引用カード（:234-251）— サイトで最も人間味と固有性がある。contact.htmlも会話バブル＋アバターで性格が出ている。
問題はこの温度がLPに一滴も還流していないこと。focus.htmlの和語感覚とLPの英語monoラベルが別人。

# 直せば単調さが最も減る順 TOP 10
1. **セクション開始儀式の解体**（:1606-1999 の `.s-lbl`×9）— 9回中3回は形式を変える。PHILOSOPHYは中央寄せ大型serif一文に、ABOUTはラベル不要。
2. **「余白の間」を1つ挿入** — SERVICESとWAYS OF WORKINGの間に全幅・ほぼ空・大型serif一文（60px、遺棄されている --text-4xl を使う）。
3. **ポートレートのグレースケール解除**（:1010）＋ MARGIN MAPに実物の手書きメモ写真。
4. **ブログ一覧にフィーチャード記事**（blog/index.html:124-142）— 最新1本を全幅、タイトル clamp(28px, 4vw, 44px)。
5. **見出しスケールのジャンプ率を上げる** — `.s-h2` 38px固定 → `clamp(32px, 4vw, 48px)`、CTA `.ch2`（:1100）は --text-4xl 級へ。
6. **footerタグラインの統一と昇格**（index.html:1124 の16px vs blog:150 の56px）— index側を大型serifに、blog側の uppercase を外す。
7. **mono番号ラベルの間引き**（19→半分）— 思想系から 01/02/03 撤去。番号=手順、無番号=思想と意味を持たせる。
8. **アクセントカラーの「面」を1箇所** — BLOGセクション（:589）のネイビーグラデをサーモン系の紙色面に。
9. **hover translateY 違反の是正**（blog:130, index:369, contact:156）。
10. **focus.htmlの和語感覚をLPへ輸入** — 英語monoラベルの数個を「兆し」「余白の地図」のような日本語小見出し（serif 13px）に。

未検証の開示: すべてコード読解に基づく。実ブラウザでのレンダリング・スクロール体感・Lighthouse計測は未実施。特に3（sec-light/whiteの知覚差）と5（ジャンプ率）は目視確認のうえ適用判断すること。
