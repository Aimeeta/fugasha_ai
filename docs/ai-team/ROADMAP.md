# ROADMAP — 優先順位つき残タスク

最終更新: 2026-07-12（AI Daily News 自動化を追加。words/colors はpush済み）

## 2026-07-12 — AI Daily News 自動生成 — 実装済み・オーナーのSecret設定待ち
GitHub Actions（JST 7:00）でAIニュースまとめ記事を自動生成。詳細は automation/ai-daily-news/README.md と DECISION_LOG。

**オーナーがやること（これをしないと動かない・未設定の間は安全に何もしない）**:
1. GitHub → Settings → Secrets and variables → Actions → Secrets に `ANTHROPIC_API_KEY` を追加
2. 任意: Secrets `SLACK_WEBHOOK_URL`（通知先）、Variables `NEWS_MODE`（既定 draft）
3. Actions → AI Daily News → Run workflow で手動テスト → 作成されたPR（下書き）を確認してマージ
4. 数日運用して精度に納得したら Variables `NEWS_MODE=publish` で自動公開へ切替

**フォローアップ候補**:
- 情報源の追加（config.json の feedsDisabled → feeds。DeepMind / NVIDIA / GitHub / MIT TR / The Verge を用意済み。allowedLinkDomains への追加を忘れない）
- SNS・メルマガ・Slack転用（automation/data/runs/*.json の構造化データを入力に）
- AI Daily記事のOGP画像自動生成（現在はサイト共通 ogp.jpg）
- 記事が溜まってきたらブログ一覧での見せ方を再設計（通常記事が埋もれないように）

## 2026-07-12 — ことばページ（words.html）追加・push済み
名言84件の没入型ページ。企画2体＋実装＋クロスレビュー2体で完了。colors.html にも同根のa11y修正2件を波及（この分も未push）。詳細は DECISION_LOG / QUALITY_REPORT 参照。

**フォローアップ候補（低優先）**:
- 実機（iOS VoiceOver / TalkBack）での没入モード脱出確認
- noscript フォールバック（focus/colors/words 三兄弟まとめて一文）
- 名言カード画像の書き出し（PNG/SVG — オーナー了承済みの後回し項目）
- 名言の追加運用: QUOTES は**末尾追記のみ**（並べ替え・削除は共有リンクとお気に入りを壊す）。追記日に「本日のことば」が変わる点とヘルプ内件数の更新に注意


## 2026-07-12 — Color Generator（colors.html）追加・push待ち
65篇のカラーパレット生成ツールを新設。企画4体＋実装＋クロスレビュー2体で完了。詳細は DECISION_LOG / QUALITY_REPORT 参照。

**フォローアップ候補（低優先）**:
- en/ 配下への英語版 colors ページ（現状JAのみ。UI文言は日本語。英語圏向けに出すか要オーナー判断）
- a11y #9（テーマchipのradiogroup化）・FE L-1/L-2（手作り共有URL＋ロックでの稀な低コントラスト）: いずれも見送り済み。再検討する場合の記録
- 実機（iOS/Android）・実スクリーンリーダーでの通し確認（未実施）
- パレット微調整（各色HSLスライダー）は「ツールの領分を超える」として保留（LPD判断）



## 2026-07-11 — 人間味監査 — Phase 0/1/2 実装済み・push待ち / 残りは Phase 3 と素材待ち
詳細は docs/ai-team/humanity-audit-2026-07-11/00_ROADMAP.md と DECISION_LOG 参照。

**実装済み（Phase 2）**: 余白の間奏（#s-interlude）／PHILOSOPHY骨格例外化＋4つ目の未完項／.s-h2・.ch2 のジャンプ率改修／blogフィーチャード記事＋cat-tags削除 — クロスレビュー指摘4件も修正済み

**素材待ち**: MARGIN MAP / Vision への実物写真投入（**本人宿題: 手書きメモ・机の写真**が届いたら）

**Phase 3（運用が必要・優先順）**: 404ページ（運用不要・低リスク）→ マニフェスト/やらないことリスト → 記事サイドノート（Tufte式）→ now ページ（四半期更新を守れる場合のみ）→ /uses・裏側記事 → 連載/ガーデン（運用体力の確約まで着手しない）

**運用注意（虚偽化リスク・要記憶）**:
- blog featured「いちばん新しい記事」は手動 — 新記事追加時にクラスとkickerを移す（グリッド先頭のHTMLコメント参照）
- PHILOSOPHYの「4つ目を、探しています。決まったら、ここに書き足します。」は更新約束 — 長期放置しない

**フォローアップ**: en/index.html への反映判断（sign-num/phi-num・grayscaleポートレート・旧footerタグライン・38px見出し・間奏なしが残存。JA/EN意図的差異として維持するか要オーナー判断）／Vision scene01 は実話でないため一人称化しない（確定）

## 2026-07-08 — トップページUI/UX監査 — 実装済み・push待ち
6体並列監査＋実機検証の詳細はDECISION_LOG参照。高〜中優先度は実装済み（`.ph-badge`タッチ対応/フォーカストラップフォールバック/nav-drawerランドマーク/`.sst-dot`タップ領域/sitemap.xml漏れ/FAQPage inLanguage/CLAUDE.mdフォント記載修正）。

**見送り・次候補（低優先度）**:
- border-radius（10種類以上）・影の不透明度のトークン化（`--radius-sm/md/lg`等）
- Visionセクションの装飾的h2見出し3件をAI要約向けに言い換え（index.html:1816,1823,1830 / en/index.html:979,997,1009）
- FAQPage以外のJSON-LDノード（WebPage/WebSite）を日英で完全統一するか判断
- Visionセクションのスクロール距離（280vh/320vh）を短縮するか、忙しい経営者ペルソナ向けに再検討
- 日英コンタクト導線の非対称（JA=外部ページ遷移、EN=ページ内フォーム）を統一するか判断
- 日本語版`contact.html`のa11y監査（今回のスコープ外）

## 2026-07-06 — ブログ2カラムテンプレート（Mihata参考）— 実装済み・push待ち
~~2カラム化（本文672px固定＋サイドバー256px sticky）/ サイドバーCTA=chat.html・末尾CTA=contact.html / 背景白化(--paper) / 参考文献欄（favicon不使用・ドメイン名テキストのみ）/ 対象4記事同一パッチ / ai-security-checkpointsのnav-cta色統一漏れも修正~~ ✅

**次候補**: 参考文献リストの充実（各記事2〜3件が目安。今回は実在確認できたものに絞ったため記事により1〜2件）

## 2026-07-05 監査 A・B群 — 実装済み
4体監査（brand-philosopher / awwwards-judge / motion-designer / first-visit-researcher 再調査）の指摘のうち、実バグ8件（A群）と人格・コピー14件（B群）を実装・検証済み。

- ~~blogタイプライターの reduced-motion 貫通~~ ✅ 演出削除・新記事と同じ静的フッターへ統一（blog/index.html・ai-security-checkpoints/index.html）
- ~~JS無効時に本文の大半が非表示~~ ✅ noscriptフォールバックを日英とも実装（sst疑似ビジュアルの縦流し含む）
- ~~相談メモCTAがメモを持たずに遷移~~ ✅ クリック時に自動clipboard.writeText、失敗時はフォールバック表示。文言「メモをコピーして、30分相談へ →」
- ~~contact確認画面でメモの改行が潰れる~~ ✅ #cMsg に white-space:pre-line、ひとこと欄 rows 3→5（実機CDP検証で改行保持を確認）
- ~~返信約束の日英不一致（24時間 vs 1-2営業日）~~ ✅ 「1〜2営業日」に統一（meta description・confirm-note・完了画面）
- ~~en split-word stagger の13語制限~~ ✅ data-wi CSS削除、JSでtransitionDelay動的付与に一本化
- ~~チェッカー結果のSR非通知~~ ✅ #hckStatus（role="status"）を300msデバウンスで実装済み
- ~~blog-prev-cardの重い影~~ ✅ 修正済み
- ~~contact Q3「検討状況」~~ ✅ **削除**（Q1/Q2の2問に。EN "no funnel" との矛盾解消。関連コード8箇所すべて連動修正、CDP実測で#cUrgency消滅を確認）
- ~~完了画面の有人化~~ ✅「いただいた内容は、代表の Aimee がそのまま読みます」＋ブログへの1リンク
- ~~チェッカー結語の観察形化~~ ✅「その時間の使い道は、あなたが決めることです。」
- ~~chat help文5本の結び同型解消~~ ✅ ai・outを全面改稿、pubを1語調整（「一緒に」5→3回）
- ~~en console の人格一行~~ ✅ 追加（hello@fugasha.jp を含む）
- ~~EN→JA逆輸入~~ ✅ CTA csubを「急かしません。仕事につながらなくても、考えが少し整って残れば、それで十分です。」に置換
- ~~TIME/ROOM/LIFE三対句~~ ✅ **削除**（日英とも。直上のcqが同内容を既に言っており、固有化は実績裏付けなしでは検証不能な主張を増やすだけという判断）
- ~~メモの自分宛mailtoリンク~~ ✅ 追加（無送信の約束と両立する注記つき）
- ~~entry-card（t=brand）文言不一致~~ ✅「サイトや資料を整えたい」に統一（chat着地バブルと一致）
- ~~ヒーロー従ボタンに「無料」~~ ✅「無料の30分相談を申し込む」
- ~~chat「空欄のまま進めます」表記ゆれ~~ ✅「空欄のままでも進めます」に統一
- ~~/en/ フォーム下にprivacy言及~~ ✅ 追加（日本語版へのリンク・hreflang付き）
- ~~privacy.htmlに相談メモ（無送信）の言及~~ ✅ 追加

**未実装（次回以降）**: 料金カード→contactのプラン文脈接続（?plan=）— 今回スコープ外

### C. 視覚の天井（awwwards-judge: 総合7.4、SOTDを阻む最大要因は「カードの海」）
15. **SIGNS を Philosophy の罫線語彙（上罫線＋番号＋余白・カードなし)で組み直す実験** — 審査員の「最も費用対効果の高い1手」。成功したら Pricing / FAQ へ展開判断
16. svc-visual のワイヤーフレーム風装飾（svc-artboard/artbar/swatch）削除 or 罫線ベース化（sst再考と同じ波で）
17. **モーショントークン導入＋語彙統一**: 異物イージング cubic-bezier(.4,0,.2,1) 2箇所置換 / カードhover応答の3系統分裂（0s/.2s/.6s）を .2s に統一 / stagger .08s 統一 / カードduration .6s 統一 / **モバイルドロワーの無遷移（display切替）を visibility+opacity .25s に** / 死んだtransition・二重平滑化の掃除 / CTAシーケンス等間隔化
18. JA Cases の横スクロール＋ドラッグJSを EN 方式（静的3枚グリッド）へ寄せる（3枚に過剰・JS削減）/ .cases-hint 系デッドCSS削除

### D. コンテンツ戦略（brand-philosopher）
19. **次記事「AIで浮いた時間は、なぜまた作業で埋まってしまうのか」**（中心命題「効率化は入り口」の証拠記事が現状ゼロ。「余白は、怠けではない」の実践編）
20. **「風雅舎自身がAIで回る最小単位の会社＝実験台」の主張を About/FAQ に**（実績数字の裏付け待ちを迂回する最も安い実績の代替物）
21. セキュリティ記事の本文改稿（匿名実例1つ＋144本書いた人にしか言えない断言2箇所 — 現状「AI生成的に見える危険」最大の箇所）/ sst scene03 コピーの一人称化（Vision再考と同乗）/ 「哲学がこの仕事の道具である理由」の一文を Philosophy s-desc に
22. 語彙の均質化緩和（「一緒に」20回・「整理」38回 — chat help文から着手）

### C. 視覚の天井（awwwards-judge: 総合7.4、SOTDを阻む最大要因は「カードの海」）— 波②実装済み・push待ち
1. ~~SIGNS を Philosophy の罫線語彙（上罫線＋番号＋余白・カードなし）で組み直す実験~~ ✅ `.sign-item` として実装。テキスト内容は無変更、器のみ変更。日英ともスクリーンショットで確認済み。成功と判断すれば Pricing / FAQ への展開は次候補
2. ~~svc-visual のワイヤーフレーム風装飾削除~~ ✅ 日英とも削除
3. ~~モーショントークン導入＋語彙統一~~ ✅ `--ease/--dur-*/--stagger` を日英 `:root` に追加。異物イージング2箇所置換、カードhover応答を`border-color .2s`に統一、staggerを`.08s`系に統一、**モバイルドロワーをvisibility+opacity遷移化**（inert・Esc・フォーカス往復をCDPで実機検証し健在を確認）、死んだtransition（`.hck-val`等）・プログレスバーの二重平滑化を解消、CTAシーケンス等間隔化
4. ~~JA Cases を EN方式（静的3枚グリッド）へ統一~~ ✅ ドラッグJS削除

✅ ユーザー承認済み・2026-07-06 push済み（コミット 5db09e4）

### D. コンテンツ戦略（brand-philosopher）— 波③実装済み・push待ち
1. ~~次記事「AIで浮いた時間は、なぜまた作業で埋まるのか」~~ ✅ blog/why-freed-time-fills-up/ として実装。一人称の失敗談＋Philosophy「熱中は、資源である」への接続込み。blog一覧・sitemapにも反映
2. **「風雅舎自身がAIで回る最小単位の会社＝実験台」の主張を About に** — brand-copywriterが決定稿を作成したが、**ユーザー判断により見送り**（実装しない）
3. **セキュリティ記事の本文改稿**（匿名実例＋144本書いた人にしか言える断言2箇所） — brand-copywriterが決定稿を作成したが、**ユーザー判断により見送り**（実装しない）。理由: 匿名実例が完全な創作モデルであり、実話でないものを実話のように見せる形を避けたいという判断
4. 残り未着手: sst scene03 コピーの一人称化（Vision再考と同乗）/ 「哲学がこの仕事の道具である理由」の一文を Philosophy s-desc に
4. 語彙の均質化緩和（「一緒に」20回・「整理」38回 — chat help文からは着手済み。残りは全体で）

### 守るべき資産（judge 明記 — 変えないこと）
言葉の統治（幅表示・非保証注記・not client records）/ a11y実装深度（inert・コントラスト設計・無送信のコード保証）/ 控えめな人間味の体系（ソースコメント・console・「急かしません」）/ View Transition の全ページ同一クロスフェード（このままで正しい）

## 2026-07-04 改善波 — 実装済み
~~Cases英語版 / 英文タイポ15項目 / 英語FAQPage JSON-LD / en/ogp.jpg / stream-label未定義バグ / contact Step1キーボード修理＋色統一 / 旧トークン一掃（AA達成）/ blogドロワーdialog+inert / フォントURL統一 / マーキー画面外停止 / sst rAFスロットル / docx退避~~ ✅

## 英語版 /en/ — 残り
1. **LinkedIn URL 受領次第**: /en/ フッター＋Person JSON-LD sameAs（日本語側にも）
2. フォームの実送信テスト（本番 Formspree・TEST明記で1件、source:"en" の識別確認）

## ユーザー判断待ち（新規追加分）
- **docx の git 履歴からの完全削除**: 追跡は解除済みだが履歴には残存。履歴書き換え（force push）が必要なため要判断（過去に brief/ で実施した前例あり）
- ~~フォント戦略の再設計~~ ✅ 2026-07-04 消化（woff2 -300KB・CSS -60KB 実測）
- ~~ツールマーキーの静的グリッド化＋ロゴのインラインSVG化~~ ✅ 2026-07-04 消化
- **ヒーローの減量（残り）**: チップ3本の体言止め短縮・CTAセクション cq 削除（~~h-en 削除~~ ✅ 2026-07-04 タイポ縮小波で消化）
- ~~About カウントアップの静的化＋自動送りスライダーの静的化~~ ✅ 2026-07-04 タイポ縮小波で消化
- **Vision（sst）疑似ビジュアルの再考**: 「AI」タイルはクリップアート発想（減らすor写真1枚に投資）
- ~~aimee-portrait 最適化＋grayscale→hover 廃止~~ ✅ 2026-07-04 消化（144px版アバター）
- ~~LCPアンカー~~ ✅ 2026-07-04 消化（.h-subcopy 初期表示化）
- ~~未使用PNG 3.5MB の整理~~ ✅ 2026-07-04 消化（assets/ogp-src/ へ・example-security-01 削除）
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
