# ROADMAP — 優先順位つき残タスク

最終更新: 2026-07-04（英語版改善＋全体監査の波 公開時点）

## 2026-07-04 改善波 — 実装済み
~~Cases英語版 / 英文タイポ15項目 / 英語FAQPage JSON-LD / en/ogp.jpg / stream-label未定義バグ / contact Step1キーボード修理＋色統一 / 旧トークン一掃（AA達成）/ blogドロワーdialog+inert / フォントURL統一 / マーキー画面外停止 / sst rAFスロットル / docx退避~~ ✅

## 英語版 /en/ — 残り
1. **LinkedIn URL 受領次第**: /en/ フッター＋Person JSON-LD sameAs（日本語側にも）
2. フォームの実送信テスト（本番 Formspree・TEST明記で1件、source:"en" の識別確認）

## ユーザー判断待ち（新規追加分）
- **docx の git 履歴からの完全削除**: 追跡は解除済みだが履歴には残存。履歴書き換え（force push）が必要なため要判断（過去に brief/ で実施した前例あり）
- **フォント戦略の再設計**（効果最大: 転送量の85%=1.53MBがフォント）: w300廃止（index/en のデザイン変更を伴う）・Noto Serif JP 500→400 統合（-632KBの可能性）・JetBrains Mono→システムモノ置換（-21KB）。typography-specialist と要協議
- **ツールマーキーの静的グリッド化＋ロゴのセルフホスト**: simpleicons CDN 20リクエスト削減＋「ロゴスープ」脱却（design-critic 提案・デザイン変更）
- **ヒーローの減量（残り）**: チップ3本の体言止め短縮・CTAセクション cq 削除（~~h-en 削除~~ ✅ 2026-07-04 タイポ縮小波で消化）
- ~~About カウントアップの静的化＋自動送りスライダーの静的化~~ ✅ 2026-07-04 タイポ縮小波で消化
- **Vision（sst）疑似ビジュアルの再考**: 「AI」タイルはクリップアート発想（減らすor写真1枚に投資）
- **aimee-portrait の srcset/WebP化**（72px表示に600px画像 eager 読込の解消）＋ grayscale→hover の廃止（タッチ端末で到達不能）
- **LCPアンカー**（ヒーロー演出でLCPが構造的に遅延 — サブコピー1ブロック初期可視 or 演出短縮。motion-designer と要協議）
- **未使用PNG 3.5MB の整理**（category-n*.png は OGP生成素材 → assets/ogp-src/ へ移動＋generate_ogp.py のパス更新、example-security-01.png は削除候補）
- **content-visibility の実適用**（アンカージャンプ・Lenisとの相互作用検証つき）
- **CSS/JS 外部分離**: perf実測では利得は gzip 5〜23KB/ページと小さく、主目的は ja/en 二重管理の事故防止（stream-label型）。優先度は中

## 英語版 /en/ — Phase 3
- Vision 静的3段圧縮版の英語化 / 英語ブログ記事→Blog帯復活 / 相談メモ英語化→ヒーローチップ復活
- 予約システム導入時のみ CTA を "Book a call" に変更可（文言と実体の一致）

## a11y 残課題（日英共通の parity 項目・a11y-auditor 2026-07-04 監査）
1. FAQ 閉パネルが SR に露出（max-height:0 のみ）→ aria-controls＋transitionend で hidden 付与（日英両方）
2. ツールマーキーの停止手段がホバーのみ → focus-within 停止＋停止ボタン検討
3. CTA の ✦ に aria-hidden なし / .cta-manifesto の無効ARIA / nav-logo の誤アフォーダンス / ドロワーリンク後のフォーカス喪失 / nav-ham 実効22px / prefersReducedMotion の change 監視なし（すべて日英共通）

## トップ改善 Phase 1+2 — 実装済み（2026-07-03・未push）
1. ~~entry-card 3枚の chat.html?t= リンク化~~ ✅（旧「次の波」2を吸収）
2. ~~料金セクションに30分無料の1行 / FAQ 7問化（可視+JSON-LD同期）/ 禁止語「業務棚卸し」修正~~ ✅
3. ~~contact.html: head SEO一式・Tabler webフォント全廃・「一切しません」置換・ひとこと欄のメモ案内・「営業目的以外に」の意味逆転修正・フォントウェイト整合~~ ✅
4. ~~chat.html OGP・sitemap掲載・og:image:alt 3ページ~~ ✅

## ユーザー判断待ち（実装ブロッカー）
- **独自ドメイン取得**: 商用クエリ競争力の最大レバー（SEO監査）。コンテンツ投資前に決めると手戻り最小
- **計測導入**: 現状ゼロ。Cookieレス系（Plausible/GoatCounter等）＋privacy.html明記が候補。AI安全LP・施策効果判定の前提条件

## 相談メモ導線 — 実装済み（2026-07-03・未push）
1. ~~chat.html 相談メモ化（APIなし）~~ ✅ 5トラック・メモ5項目・コピー機能・a11y修正済み
2. ~~ヒーロー二段CTA＋悩みチップ3本＋ドロワー二段＋CTAサブリンク~~ ✅
3. ~~View Transition API 全8ページ~~ ✅
4. ~~a11yクロスレビュー重大2件・中3件の修正~~ ✅（フォーカスリング3:1・メモ生成時フォーカス・main・aria-labelledby・ドロワーinert）

## 相談メモ導線 — 次の波
1. **Workers + AI API への昇格**（反応を見て判断）— プロキシ設計・レート制限・ターン上限・privacy.html 更新・CTA文言を「AIに話してみる」系へ昇格。前提: ホスティング先と予算上限のユーザー決定
2. ブログ記事末尾に1行リンク `この記事の内容を、自分の仕事に置きかえて考えたい方へ。`→`chat.html?t=カテゴリ`
3. ブログ続編「生成AI社内ルールの作り方」（AI安全LPの前哨・クエリ空白をSEO監査が特定）
4. a11y軽微指摘の残り: btn-ghost/h-chip の境界線視認性（1.2:1）・copy-status の三重通知・@view-transition のオプトイン化・noscript時のヒーローチップ表示・メモ画面から自由記入へ一段だけ戻る
5. モバイル375pxでチップが3段になる件 — 文言短縮 or 2本化の検討（現状レイアウト崩れはなし）

## ヒーロー背景の格上げ（3Dの代替 — DECISION_LOG 2026-07-03参照）
1. **reduced-motion 時の静的背景フォールバック**（現状は透明のまま＝a11y案件・最優先）
2. タッチ端末（pointer: coarse）での heroBg 描画停止 or 静的1回描画
3. canvas の DPR 対応要否確認（CTA wave のRetinaジャギー疑い・実機目視）
4. その後、案A「紙のうえの光」の実装検討（creative-director 報告参照）

## Phase 2 — 完了（2026-07-03）
1. ~~プライバシーポリシー整備~~ ✅ privacy.html公開・全フッターからリンク
2. ~~ツールロゴのモノクロ統一~~ ✅ ネイビー地×クリームに統一
3. ~~Tablerアイコン全廃~~ ✅ blog側もインラインSVG化・フォントウェイト削減
4. ~~ブログ自動更新基盤の選定~~ ✅ 既存テンプレ＋Claude Code分隊方式（auto-update-brief.md）
5. ~~FAQ増強~~ ✅ 秘密保持の1問を追加（「3ステップ」は見送り継続）
6. **実績数字の裏付け** — private/evidence-numbers.md にテンプレ作成済み。**数字の記入はユーザー作業**
7. contact.html への og:image 追加（1行・未対応）

## Phase 3（余裕があれば）
0. **既存記事・ブログ一覧の現行ブランド化** — `blog/ai-security-checkpoints/` と `blog/index.html` はまだ旧仕様（Tabler webフォント・タイプライターフッター・serif 600・CTA白文字）。新記事2本（2026-07-03公開）と同じ仕様に揃える。あわせて既存記事の記事別OGP作成、`blog/ogp.jpg`（一覧用）も検討
4. FAQリサイズ微バグ（transitionend で max-height 解除）
5. Philosophy 3原則の上罫線ドロー（scaleX、reduced-motionで即時表示）— creative-coder 承認済みの唯一の新演出
6. margin の 8px 基調への丸め / 英ラベル letter-spacing 統一 / 角丸トークン化
7. SIGNSカード見出しの h3 化

## ブログ基盤と同時にやる
8. CSS/JS の外部ファイル分離（再訪キャッシュ）
9. sitemap の GitHub Actions 自動生成
10. ブログ自動更新基盤の選定（設計メモ: `blog/auto-update-brief.md`）

## Future（凍結中 — 憲法により当面やらない）
- WebGL/Three.js 背景、GSAP導入（2026-07-03 再審査で却下維持。View Transition API のみ個別解除して採用済み）
- ナビCTAの chat.html 化（AI昇格後に計測材料が揃ってから再検討）
- brand-copywriter のサービスカード導入一文4本（全面改稿時の素材として DECISION_LOG に保管）

## 運用メモ
- push＝本番公開。ユーザーの明示指示があるまでpushしない
- 実績数字（144本・50社以上）の裏付け一覧を別途保管する
