# AUDIT_REPORT — 監査結果（対応状況つき）

最終更新: 2026-07-14。凡例: ✅ 対応済み / ⬜ 未対応 / 🚫 却下（理由つき）

## 2026-07-14 全体監査（5体並列: seo-aeo / performance / a11y / first-visit / brand-copywriter。EN含む・すべて⬜未対応）

### 重大（公開ブロッカー級・複数監査が収束）
- ⬜ **blog一式が旧世代のまま取り残され**（SEO/UX/a11y/コピーの4監査が独立に指摘）:
  - ナビが旧構成 Services/About のまま＝余白/Colors/Homeへの回遊断絶（blog/index.html:177-193＋記事8本）
  - コントラストAA割れ: `.blog-eyebrow`/`.card-badge`(1.93:1)/`.card-meta`(2.52)/`.ft-link`(2.39)/`.art-badge`/focus-visible の accent 直用 → `--accent-ink` 等へ置換（WCAG 1.4.3/1.4.11）
  - kicker「いちばん新しい記事」が虚偽化（featured=07.10 < AI Daily=07.12）→「いちばん新しい、書きおろし」へ
  - 記事側モバイルドロワーに dialog/フォーカス管理なし・nav-ham 22px（一覧側は実装済み）
- ⬜ **focus.html: 背景パネルを開くと20.4MB**（フル解像度JPG18枚をサムネ直用、focus.html:1175）→ 360px WebPサムネで-98% ／ **フォントCSSが通常の2倍(297.9KB)** → Noto Serif JP を可変レンジ `200..700` 指定で -151.6KB gz
- ⬜ **contact.html（コンバージョンページ）**: 白×アンバー「必須」2.61:1 等4件 ／ ステップ遷移でフォーカス喪失・SR無通知（WCAG 2.4.3/4.1.3, setStep:585）／ main/skip-linkなし ／ scrollTo が reduced-motion 貫通(:599)
- ⬜ **season/words が静的リンク上の孤児**（リンクが yohaku.html のJS配列内のみ→AIクローラー不可視）→ yohaku索引を静的`<li>`＋JSエンハンス化（既知P2と同根・解決策も同じ）
- ⬜ **en/index.html: FAQが存在しないプラン紹介を参照**（"The monthly retainer" 等、JAの07-08 WAYS OF WORKING 再編に未追従）→ FAQ自己完結化 or Ways of working EN版
- ⬜ **信頼の手がかり（要オーナー判断）**: 費用感の記載ゼロ（chat.html自身が「費用感がわからない」を悩み例示する自己矛盾）／実在の外部照合先ゼロ（運営者情報ページ・LinkedIn）／JA側に請求・インボイスFAQなし

### 中
- ⬜ EN微修正一式: "agree the"→"agree on"×2 ／ "The aim is one"直訳臭 ／ "where a change earns the most"3連発 ／ Security/Blogリンクの lang="ja" 誤付与（3.1.2・削除）／ Yohakuリンクは逆に注記なしで日本語ページへ無警告着地
- ⬜ og:description 欠落8ページ・twitter:card 欠落9ページ・サブページ11枚JSON-LDなし・sitemap lastmod 陳腐化5件
- ⬜ 単一キーショートカットの無効化手段なし（today/words/colors、WCAG 2.1.4）
- ⬜ WORDS_AUTHORS 複製の同期リスク（yohaku.html:171 に警告コメントを）
- ⬜ 余白系ナビ: Contact不在（5ページ）・TOP/Home表記揺れ・Colorsの所属曖昧
- ⬜ focus「動画」カテゴリは必ず404（mp4不在）／ `.grad.water` が background-position 無限アニメ=常時repaint ／ wave canvas スロットルなし（120Hzで2倍速・hero光と語彙分裂）
- ⬜ 背景JPG 18枚=20MB（2560px+WebP化で-65〜75%推定）
- ⬜ today.html `#daMsg` がSR常時露出＋二重通知 ／ index BLOG帯が07.03で停止 ／「半日ワークショップ」の根拠が本体にない（JA/EN）

### 軽微（抜粋）
- ⬜ フッター `.ftl`(4.32)/`.ftc`(3.75) のα.62統一（blog/privacy/security-ai）／ security-ai 520px以下で余白リンク消失 ／ 404にBlogリンクなし ／ chat.html のみ robots 宣言なし ／ AI Daily BlogPosting に image なし ／ season.html:349 gloss一本の律・:313コメントと実装の矛盾（23:59判定）／ today:992 文言重複・:367「アクセスした」語彙 ／ sky meta「今夜空」誤読 ／ blog description 語尾均質化

### 監査で「問題なし」を確認した主な点
sitemap網羅（season含む）/ OGP画像実在 / canonical・hreflang相互一致 / FAQ可視=JSON-LD同期 / 雨音WebAudioは模範実装 / canvas停止網羅 / img属性完備 / CLS実測0（キャッシュ済条件）/ 禁止語ゼロ / Japan bridge・一人称"I"一貫

### 未検証領域（各監査共通の開示）
実機SR通し読み / 実タッチ端末 / 本番URLでのLighthouse・OGPデバッガ / 初回訪問フォントスワップCLS / WebP/AVIF実サイズ（エンコーダ未導入）

---

（以下は 2026-07-03 の13専門家レビュー＋7専門家検証の統合）

## アクセシビリティ
- ✅ スキップリンク・`<main>` ランドマーク追加
- ✅ ケース横スクロールのキーボード到達（tabindex/role/aria-label）
- ✅ ドロワーのフォーカス管理（開→閉じるボタン、閉→ハンバーガー復帰、Esc対応）
- ✅ トースト `role="status"`、シーン番号 `aria-hidden`、slider/nav の focus-visible
- ✅ FAQを実高さアニメに（240px固定上限を廃止）
- ⬜ SIGNSカード見出しの div → h3（低優先）

## パフォーマンス
- ✅ Tabler webフォント → インラインSVG 9種
- ✅ ヒーロー/CTA canvas の画面外停止
- ✅ 死んだCSS約90行削除、疑似ボールド解消（serif 600→500）
- ⬜ CSS/JS の外部ファイル分離（ブログ基盤整備と同時に）
- ⬜ Google Fonts サブセット/ウェイト実測削減

## SEO / AEO
- ✅ ogp.jpg 欠落（og:image が404）→ ネイビー基調1200×630を生成・設置
- ✅ og:locale / og:site_name / og:image寸法 / theme-color 追加
- ✅ robots.txt はAIクローラー個別許可の模範構成（対応不要と確認）
- ⬜ contact.html に og:image がない（1行追加）
- ⬜ sitemap自動生成（ブログ毎日更新の運用が始まったら）

## タイポグラフィ
- ✅ 見出しの palt 詰め
- ⬜ margin値の8px基調への丸め（Phase 3）
- ⬜ 英ラベルの letter-spacing 統一（.16〜.22em → .18em）

## ビジュアル / ブランド
- ⬜ ツールロゴのモノクロ統一（ページ内で最も彩度の高い帯。**ブランド判断待ち**）
- ⬜ 角丸のトークン化（現在9段階）
- 🚫 Three.js背景 / GSAP導入 / 新ストーリーテリングセクション（憲法により却下）

## コピー
- 現状ほぼ完成。微修正候補: ヒーロー「手段は横断しますが」→「道具はいろいろ使いますが」（任意）
- 「More you.」（フッター）と「More curiosity.」（About）の併存は変奏として維持と判定

## ブログ（2026-07-03 SEO/AEO監査より）
- ✅ 新記事2本: JSON-LD著者インライン展開・パンくず末尾item・記事別OGP・メタ完備
- ✅ blog/index.html: og:locale/og:site_name追加、ハンバーガーのbutton化＋aria-expanded
- ✅ landing #s-blog: sec-whiteクラスとダーク背景の乖離を解消
- ⬜ 既存記事 ai-security-checkpoints が旧仕様のまま（Tablerフォント・タイプライター・共通OGP流用）→ ROADMAP Phase 3-0
- ⬜ blog/ 一覧用の専用OGP画像（現状はトップと共通、許容範囲）
- 🚫 twitter:title等の個別指定（og:*フォールバックで十分と判断）

## コード品質
- ⬜ FAQ開いたままリサイズで max-height が古くなる微バグ（transitionend 後に解除で解消可・実害小）
- ⬜ scrollspy: 非マップセクション（FAQ/Blog/CTA）で直前の下線が残る（仕様として許容中）

## 法務・運用
- ⬜ **プライバシーポリシー未整備**（contact.html 公開中のため実質必須。事業者情報のヒアリングが必要）
- ⬜ 実績数字（144本・50社以上）の裏付け一覧の保管
