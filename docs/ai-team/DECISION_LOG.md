# DECISION_LOG — 意思決定の記録

新しい決定は上に追記する。形式: 日付 / 決定 / 理由 / 決定者。

## 2026-07-08 — focus.html 実写真背景＋YouTube入力＋音源厳選
参照サイト(mihata)は素材の出所を非公開で、ユーザーの好きな曲は**YouTube入力**で流す設計（Open-Meteo/ipapiは天気のみ）と判明。合成の抽象ポスター/仮音源が安っぽいというオーナー指摘を受け、方針転換:
- **背景を実写真に全面差し替え**: Unsplash（無料ライセンス）の風景写真12点を取得・最適化(1600×900, 各<250KB)して自前ホスト。山と森/水辺の2グループ、動画対応5点。合成ポスター11点は廃止。背景パネルに「写真: Unsplance（無料ライセンス）」のクレジット表記。可読性は既存の輝度判定＋スクリムで担保（実写真でも白/暗文字を自動選択）。
- **YouTube入力を追加**（任意・外部接続）: 音楽パネルにURL入力＋公式IFrame Player API。動画/プレイリストURLを解析し埋め込み再生。ミニプレイヤー・音量・ミュートと連動、ローカル音源選択でYT停止、URLをlocalStorageに保存（自動再生はしない）。**既定ではYouTubeに接続せず**、ユーザーがURLを入れたときだけ外部(Google)接続する旨をパネルに明記。これによりLo-fi・アニメ/ゲームOST等の実曲を合法に再生できる。
- **合成プリセットを12→7に厳選**（近い曲を整理）: Lo-fi Focus / Midnight Lo-fi / Northern Oath / Cafe Bossa / Forest Stream / Fireplace / Ambient。未使用音源5点を削除。プリセットは環境音・雰囲気の役割に限定（実曲はYouTubeで）。
- 差し替え口: 背景=`PHOTOS[].img`（実写真JPEG）、音源=`TRACKS[].src`。動画背景mp4は従来どおり`assets/backgrounds/<id>.mp4`が置かれれば有効化（現状はposter静止画で動作）。

## 2026-07-07 — focus.html 可読性バグ修正＋音源/背景ライブラリ拡張
**可読性バグ**: 写真/動画背景では常に白文字にしていたため、明るい背景（南国カフェ等・カスタムの明るい画像）で白文字が潰れて視認性が低下していた。修正: 背景の平均輝度をcanvasで測り（`luminanceOf`/`probeImageContrast`/`probeVideoContrast`）、明るい背景では `on-media-bright` を付与して暗色テキスト＋白系スクリム＋白光の影に自動切替。暗い背景は従来どおり明色テキスト。カスタム画像/動画も判定対象。
**ライブラリ拡張**（creative-director + brand-copywriter の助言を統合）:
- 音源 5→12。カテゴリ制（`cat`）で音楽パネルをグルーピング表示: Lo-fi(Focus/Rainy/Midnight/Morning) / 叙情Cinematic(Northern Oath/Ashen Hymn/Quiet Resolve — ウィッチャー/ベルセルク/アニメOSTの"気分"を、固有名詞を使わず情景語で表現) / カフェ(Jazz/Bossa) / 自然(Forest Stream/Fireplace) / 抽象(Ambient)。全てオリジナル合成・著作権フリー・60秒ループ・ボーカルなし・低ダイナミクス。
- 背景写真 5→11。自然シーンを追加(遠い山並み/渓流/静かな湖/星空と山脈/霧の谷/夕暮れの海)。写真パネルを「自然 / 情景」でサブ分類。**各ポスターは中央帯をラジアルに暗く焼き込み**、中央の時計を白文字で常に読めるようにした(輝度判定と併用)。動画カテゴリは動きが映える5シーンに絞る。
- 実写真・実動画・実曲は著作権のため非同梱。合成ポスター/合成音源で代替し、差し替え口(`TRACKS[].src`/`PHOTOS[].img`/`assets/backgrounds/<id>.mp4`)を維持。

## 2026-07-07 — focus.html を「Focus Clock」へ全面拡張
mihata.jp/en/clock を機能参照（コード・資産は非複製）し、focus.html を集中特化アプリへ再構築。追加: 時計の秒/12・24h/サイズ/太さ/書体、フルスクリーン(F)・スペースで開始停止・Escで閉じる、ポモドーロのスキップ/各時間・長休憩までのセッション数/自動切替/自動開始/終了音4種/ブラウザ通知/本日統計(完了数・集中時間・セッション)/タイトル残時間、Web Workerで背面時の精度維持、音源5種を Lo-fi/Jazz/**Cafe Bossa**/Fireplace/Ambient に再編(cafe-bossa.m4a を合成追加、piano-ambient を廃止)、ミニプレイヤーにミュート追加・切替フェード、背景は 単色/グラデ3/写真5/動画5(placeholder mp4→poster静止画フォールバック)/カスタム/ランダム、背景follows music、下部フローティングツールバー+右パネル/モバイルはボトムシート、JA/EN i18n、日次統計の日付リセット。
- **背景素材の方針**: 実写真・実動画は著作権のため同梱せず、PILで合成した雰囲気ポスター5枚(`assets/backgrounds/*.jpg`)を写真背景として同梱。動画は完全なパイプライン(video autoplay muted loop playsinline object-fit:cover / poster / error時に静止画フォールバック / reduced-motionでposter)を実装し、`assets/backgrounds/<id>.mp4` を差し替え口として用意(未同梱のため現状はposterで動作)。差し替え口: 音源=`TRACKS[].src`、背景写真=`PHOTOS[].img`、動画=`assets/backgrounds/<id>.mp4`。
- **時計の太さ**: 太さ調整のため focus.html のみ Zen Kaku(300-700)/Noto Serif JP(200-700)を追加読込。実ウェイトへスナップし疑似ボールドは回避(憲法遵守)。
- **未実装(優先度B)**: 天気/YouTube/PWA/カレンダー/パレット自動ローテーション。スリープ防止(wake lock)のみ実装。localStorageは v2 に更新(v1のタスク・配色は移行)。

## 2026-07-07 — focus.html の音源はセルフホストの合成プレースホルダー
Music & Ambient機能（5プリセット）の音源として、YouTube等の外部サービス連携は不採用（オーナー指定）。既存楽曲の利用は著作権確認コストが高いため、**純Pythonで合成した60秒シームレスループ**（`assets/audio/*.m4a`、各530〜730KB、AAC 96kbps）をセルフホストする方式を採用。全て合成音のため権利問題なし。`focus.html` 内の `TRACKS` 配列の `src` を書き換えるだけで後から差し替え可能（生成スクリプトは使い捨て・リポジトリ外）。`preload='none'` で選択時のみ取得し、ページ読み込みには影響しない。Lo-fi/Jazz系は合成ゆえ簡素な仮素材であり、品質を上げる場合はCC0等の実音源への差し替えを推奨。

## 2026-07-06 — ブログ4記事の拡充（favicon・目次・inline CTA・本文加筆）
オーナー追加要望に基づき、前回裁定を一部上書き。interaction-designer設計・brand-copywriter執筆・frontend-engineer実装。
- **favicon裁定の見直し**: 「外部依存を増やさない」は維持しつつ、実行時にGoogle API等を叩く方式ではなく**ビルド時に一度だけ取得しセルフホスト**（`assets/favicons/`）する方式を採用。懸念の本質は「訪問者ごとの外部送信」であり「favicon画像の利用」自体ではない、という区別で両立させた。実装時、Google s2 APIが政府系3ドメインに同一の汎用フォールバック画像を返すことが判明したため、各ドメインの`/favicon.ico`を直接取得する方式に切替
- **目次**: JS自動生成（h2から動的構築）。手書き複製は将来の見出し改稿でドリフトするため不採用
- **inline CTA**: サイドバー・記事末尾に続く3つ目のCTAとして、罫線のみの最も軽い扱いで追加。3つのCTAに視覚強度の序列（サイドバー＝箱、本文中＝罫線のみ、末尾＝塗りボタン）をつけて温度差を表現
- **本文加筆**: 4記事とも1.5〜1.75倍に拡充。各記事に新しい一人称エピソードを追加。ai-security-checkpoints（前回「AI生成的に見える危険が最も高い」と判定された記事）は創作の匿名エピソードを避け、一般論の深掘りと「筆者自身の執筆前調査」という検証可能な行為のみで厚みを出した。加筆量が1.8倍上限を超えた箇所は指定通り削減
- 読了時間表示を実測文字数から再計算（4記事とも「約4分」→「約6〜7分」に更新）
- 副次判断: 新規注釈文の「言い訳として定着してしまう」という表現について、禁止語「定着」（コンサル用語）との類似を機械的に検出したが、文脈は一般用法（「暮れる」系の意味）と判断しユーザー確認の上でそのまま維持

## 2026-07-06 — ブログ記事テンプレートに2カラム＋白背景＋参考文献欄（Mihata参考）
オーナー参考: https://mihata.jp/column/ai-news-2026-07-03 の2カラム構成。生HTML/CSSを直接取得・実測（WebFetchのテキスト要約ではレイアウト情報が失われるため）してから風雅舎の罫線言語へ翻訳。interaction-designerが設計、frontend-engineerが実装。対象: 既存3記事＋新記事の計4記事。
- **2カラム化**: 本文幅672px固定＋サイドバー256px sticky（top:96px）。ブレークポイントは768pxでなく1024px（波②のPhilosophy罫線化と同じ理由 — 中間幅で本文が押し潰されるのを防ぐ）。Mihataの`flex:1`をそのまま移植せず本文幅を固定した判断は「Readabilityがブランド一貫性より優先」という憲法に基づく
- **サイドバーCTA裁定**: `chat.html`（低コミット・相談メモ）に統一、記事末尾の既存`.cta-box`（`contact.html`・高コミット）はそのまま維持。ブログ読者はファネル最上流という位置づけから、視覚の強さの差でコミットメント差を表現（サイドバーはテキストリンク調、末尾は塗りボタン）
- **背景白化**: `--paper: #fdfbf7`をブログ記事の`<style>`内のみで完結。サイト全体のクリーム基調（`--bg: #f0e6d6`）は変更しない
- **参考文献欄**: favicon取得（Google `s2/favicons` API依存）は不採用、ドメイン名のみのテキスト表示に。理由: 「入力内容はどこにも送信されません」を差別化点にするブランドで、読者の閲覧興味を暗黙に外部送信する構成は一貫性を欠くと判断。件数はJSで自動算出（ハードコードによる数値ズレを回避）
- **参考文献の出典**: 実在確認済みURLのみ採用（IPA・総務省経産省・中小企業庁・NIH/PMC・Wikipedia等）。curlで403を返した経産省PDF数件は実在確認が取れる代替資料に差し替え、創作URLは一切使用していない
- 副次修正: `blog/ai-security-checkpoints/index.html`のnav-cta/cta-boxボタンが2026-07-04の色統一波で見落とされ白文字のまま残っていたのを発見・修正（他3記事と同じ`var(--fg)`に統一）

## 2026-07-06 — 波②push・波③コンテンツ戦略（新記事1本のみ採用・2件は見送り）
- **波②（SIGNS罫線化・モーション統一）をユーザー承認後にpush**（コミット 5db09e4）
- **波③はユーザーが3提案のうち1つだけ採用**:
  - ✅ 新記事「AIで浮いた時間は、なぜまた作業で埋まるのか」（blog/why-freed-time-fills-up/）— 実装・公開
  - ❌ 「風雅舎自身がAIで回る実験台」のAbout追記 — **ユーザー判断により見送り**。決定稿はbrand-copywriterが作成済み（チェンマイ拠点・3言語・一人事業という既存事実のみから書かれた1文）だが、今回は反映しない
  - ❌ セキュリティ記事の改稿（匿名実例＋144本執筆経験の断言） — **ユーザー判断により見送り**。理由: 匿名実例が完全な創作モデルであり、実話でないものを実話のように見せる形を避けたいという判断。決定稿自体は本セッションの記録に残る
- 教訓: 監査で「AI生成的に見える危険が最も高い」と判定された箇所（セキュリティ記事）の改善は、創作要素（匿名実例）を含む提案だとオーナーが慎重になる。次に改稿を提案する場合は、創作モデルではなく実際にあった相談内容の匿名化（オーナー確認込み）から作る方が通りやすい可能性がある

## 2026-07-05 — 新視点4体監査（brand-philosopher / awwwards-judge / motion-designer / first-visit-researcher再調査）A・B群を実装
初招集2体（brand-philosopher・awwwards-judge）を含む4体に、既存ROADMAP項目を再提案禁止として現状監査を依頼。実バグ8件（A群）と人格・コピー14件（B群）を1波で実装・公開。
- **判断が分かれた2点の裁定**:
  - **contact「検討状況」質問（Q3）→ 削除**。EN "Three fields, no funnel." と日本語版のリードスコアリング語彙が構造的に矛盾していた（philosopher・researcher 2体一致の指摘）。Q1/Q2の2問に短縮、関連コード8箇所を連動修正
  - **TIME/ROOM/LIFE三対句 → 削除**（日英とも）。直上の cq が同内容を既に言っており引き伸ばしに過ぎない上、「風雅舎固有の観察に書き直す」案は実績数字の裏付けが揃っていない現状では検証不能な主張を増やすだけと判断（証拠基準に反する）
- **返信約束を「1〜2営業日」に日英統一**（旧: JA「24時間以内」vs EN「1–2 business days」の矛盾。judge・researcher 2体一致）。「多くの場合は当日中」の温度は事実未確認のため見送り
- **相談メモCTAの自動コピー化**: 「持って」と言いながら実際は何も持たず遷移していた設計バグを解消。クリック時に clipboard.writeText、失敗時フォールバック
- **blogタイプライター演出を削除**（reduced-motion を貫通する演出だった。JSのtextContent書換はCSSクランプ対象外という新事実で a11y 案件に格上げ）。新記事と同じ静的フッターに統一
- **完了画面の有人化**: 「読むのは代表の Aimee」の一文＋ブログへの1リンク。「少し、楽しみにしていてください」は削除
- **メモの mailto リンク新設**（再訪対策。「サイトには届かない」注記つきで無送信の約束と両立）
- **awwwards-judge の採点は総合7.4**（Honorable Mention級）。SOTDを阻む最大要因は「カードの海」（器の同型反復）と裁定 → 次波（波②）で SIGNS を Philosophy の罫線語彙で組み直す実験に着手予定
- **brand-philosopher が「まだ書かれていない主張」を3つ特定**: 「風雅舎自身がAIで回る最小単位の会社＝実験台」（実績裏付け待ちを迂回する最も安い実績の代替）/「安全確認そのものがAI導入の第一歩」/「効率化の問いは哲学の問い」→ 波③のコンテンツ戦略へ
- 未実装のまま次回送り: 料金カード→contactのプラン文脈接続（?plan=）

## 2026-07-04 — フォント3ウェイト統合＋残改善バッチ（typography-specialist 裁定・全採用）
- **フォント統合**（9ページ一括）: Zen Kaku w300 廃止（小級数本文9箇所を400へ — 可読性はむしろ向上）/ Noto Serif 500→400 統合（中間見出し約30箇所 — 階層は級数とアキが担う書籍的な組みへ。大見出しw300は無傷）/ JetBrains Mono→システム等幅スタック。**実測: woff2 1.53MB→1.23MB・リクエスト122→88・フォントCSS 207.5KB→147.6KB**。既存の疑似ボールド3箇所（mono w500指定）も修正。ogp-source系は生成用のため対象外
- **ツールマーキー廃止→静的グリッド**: simpleicons CDN 20リクエスト全廃、ロゴ10個をインラインSVG化（日英）
- **a11y残課題**: FAQ閉パネルに hidden＋aria-controls / ✦ aria-hidden / manifesto role=list / ドロワーリンク後のフォーカス / nav-ham 8px（日英）
- **画像**: en アバターを144px版に（600px画像の28倍オーバーサイズ解消）/ grayscale→hover演出廃止（タッチ到達不能のため常時grayscaleへ）
- **LCPアンカー**: .h-subcopy を初期表示化（日英）/ 未使用PNG 3.5MB整理（category-n* → assets/ogp-src/・generate_ogp.py パス更新・example-security-01.png 削除）

## 2026-07-04 — ディスプレイ英文タイポの縮小（オーナー直接フィードバック起点）
オーナー「英語タイトルのフォントサイズがでかい。全体的にUI/UXを改善してほしい」→ visual-designer 裁定「大きさで語る→一箇所だけディスプレイ、他は静かな署名」。
- タグライン3回反復を1系統に: JA `.h-en`（H1直下の英文キッカー）削除 / `.about-catch` 54px大文字→26pxプルクオート（sentence case）/ フッター `.ft-tagline-big` 160px大文字→16px serif の結び文。ディスプレイスケールの家は /en/ H1 のみ
- CTA の TIME/ROOM/LIFE（48px）→ 11px mono ラベル（サイトのラベル体系に合流）
- About のカウントアップ・自動送りスライダーを静的化（「静けさの設計」との整合。ROADMAP判断待ち2件を消化）
- 9pxラベルの10px統一（トークン --text-xs: 10px への収束）/ JAフッター法的表記のコントラストをENと同値化
- 巨大フッターワードマークは「2020年代前半のトレンドで経年劣化リスク」（Timeless優先）という判定を記録

## 2026-07-04 — 英語版改善＋全体監査の波（8体分隊）
brand-copywriter / typography-specialist / design-critic / performance-auditor（監査4体・並列）→ frontend-engineer ×2（直列実装）→ 検証はオーケストレーター。
- **/en/ 改善**: Cases英語版追加（現在形の一般描写・"not client records" 明示・3枚静的グリッド）/ 英文タイポ15項目（行間2→1.7系・行長62ch制御・疑似イタリック排除・text-wrap: balance/pretty 等 — 「直すべきは書体でなくメトリクス」の裁定でフォント追加なし）/ 英語FAQPage JSON-LD / 英語版OGP `/en/ogp.jpg` 生成・差替
- **本番バグ修正**: index.html の `.stream-label`/`.sld` 未定義クラス（初期からの潜伏バグ・定義だけがリファクタで消失）
- **contact.html 修理**: Step1 を div+click → ネイティブ checkbox/radio＋fieldset/legend に（キーボードで問い合わせ完了不能だった＝憲法1-2位違反の解消）。380ms自動遷移廃止。reduced-motion全体無効化追加。白文字ボタン（2.6:1）→ネイビー文字。Tailwind残骸色（amber-600グロー・#92400e・stone系黒・未使用の--success）を全廃
- **色トークン統一**: contact/privacy/blog×3 の旧 --muted/--hint（AA未達3.1〜3.4:1）を index と同値に。blogフッター透明度・nav-cta白文字も修正。blogドロワーに dialog+inert 移植
- **パフォーマンス**: フォントCSS URL を全9ページで1本に統一（回遊時148KBのレンダーブロッキング解消）/ jsdelivr preconnect / ツールマーキーの画面外停止（IO+play-state）＋will-change削除＋focus-within停止 / sstスクロールの rAFスロットル化 / content-visibility の虚偽コメント修正（実適用はROADMAP）
- **安全**: 公開されていた引き継ぎdocx×4を private/（gitignore済）へ退避・blog/.DS_Store 追跡解除。**注意: git履歴には残存 — 完全削除は履歴書き換えが必要でユーザー判断待ち**
- 却下: ヒーロー言語キッカーの削除（design-critic提案）— researcher の「英語対応をファーストビューで明示」要件を優先し維持

## 2026-07-04 — 英語版トップ /en/ を新設（海外クライアント向け・橋渡し主軸）
5体分隊（first-visit-researcher / brand-copywriter / seo-aeo-auditor / lead-product-designer 統合 / frontend-engineer 実装 / a11y-auditor クロスレビュー）。ユーザー決定: 範囲=トップ1ページから / 読者=海外クライアント / 位置づけ=**橋渡し（Japan bridge）を主・汎用支援を従** / LinkedIn等の外部プロフィールあり（URL受領待ち）。
- **コピー方針**: 直訳でなくトランスクリエーション。H1は既存資産 "Less friction. More you." を昇格し日本語H1を補助行に（lang="ja"）。一人称は "I"（"we"は規模の偽装）。SIGNS は「三人称の観察＋引用符つき一人称告白」の二層構造。**USD静的併記は恒久不採用**（為替で嘘になる。JPY明示＋換算説明1行）
- **CTA裁定**: 予約システム不在のため "Book a call" 却下 → `Write to me →`＋ページ内3フィールドフォーム（既存 Formspree 流用・payload source:"en" で識別）。文言と実体の一致（正しさ）
- **構成**: About前倒し（海外では「誰か」が全てに先行）/ 新設 ACROSS BORDERS（Japan, in Japanese・Remote・Time zones UTC+7・3言語・Payment）/ FAQ 8問（橋渡し問をQ3に昇格）。初版で落としたもの: 業務時間チェッカー・Cases・Vision演出・ブログ帯・日本語chatへの導線
- **技術**: 双方向hreflang（x-default=日本語）/ JSON-LD は同一@idの英語軽量ノード再宣言（WebSite再定義禁止・OfferCatalog再掲禁止）/ sitemap xhtml:link / **自動リダイレクト禁止** / 日本語側 areaServed を Japan→Worldwide（FAQ「海外対応可」と整合）
- push前ゲート3点（Philosophy英文・ヒーローリード・FAQ Q3「clients are mostly small businesses in Japan」）はユーザー承認済み（2026-07-04）
- a11yクロスレビュー: 重大1（FAQフォーカスリング）・中3件を公開前修正。残課題（FAQ閉パネルのSR露出・マーキー停止手段・nav-logo誤アフォーダンス等、日本語版と共通のparity項目）は ROADMAP へ
- Phase 2 予定: 英語版 /en/ogp.jpg・Cases英語化・英語FAQPage JSON-LD・LinkedIn sameAs 差し込み

## 2026-07-03 — サービスLP新設の提案を審査 → 不採用、トップの「4つの穴」を塞ぐ方式を採用
外部提案（ChatGPT由来: 本命「AI・業務整理はじめの相談室」LP＋別案2つ）を4体分隊（first-visit-researcher / brand-copywriter / seo-aeo-auditor / lead-product-designer 統合）で審査。
- **本命LP・発信LP: 恒久不採用**。LP構成7要素中6要素がトップに既存（ヒーロー文はトップのチップと同一文言）。「トップは世界観、LPが答える」という前提が本サイトに不成立。診断入口の提案は chat.html として実装済み
- **AI安全導入LP: 条件付き凍結**（3案中唯一将来性あり）。再検討条件: ①計測基盤の存在 ②FAQ/構造化データ整備後もなお商用クエリ・AI検索引用が弱い ③対象は安全導入LPのみ ④独自ドメイン移行 or Workers+AI昇格時は優先度上昇。保管素材: H1「安心して使える範囲から、AIを始める。」、URL `services/` 慣行、Service+BreadcrumbList+固有FAQ の @graph 構成、ブログ続編候補「生成AI社内ルールの作り方」
- **代わりに実施（Phase 1+2 実装済み）**: entry-card 3枚の `chat.html?t=ai/brand/ops` リンク化 / 料金セクションに「最初の30分の相談は無料です」の1行 / FAQ 3問追加で7問打ち止め（進め方・頼める内容・個人事業主、可視＋JSON-LD同期）/ 禁止語「業務棚卸し」修正 / contact「無理な営業は一切しません」を観察形へ / ひとこと欄に相談メモ貼り付け案内 / contact の head SEO一式＋Tabler webフォント全廃（インラインSVG 5種）/ chat の OGP＋sitemap 掲載 / JSON-LD に priceRange＋hasOfferCatalog（PriceSpecification.minPrice 方式、表示価格と逐語一致）
- 「やらないこと」4連発は「営業の文法」として不採用。肯定形変換「進め方で、決めていること。」4項目（ツールは手元にあるものから / 増やす前に片づける / 続けられる大きさまで小さくして渡す / AIに入れる情報の線を最初に引く）は将来素材として本項に保管。うち1文はFAQ回答に反映済み
- 修正ついでの発見: contact「入力内容は営業目的**以外に**使用しません」の意味逆転を「営業目的**には**使用しません」に修正（正しさ）
- **ユーザー判断待ち**: 独自ドメイン取得（github.io プロジェクトパスは商用クエリで構造的に不利 — SEO監査の推論）/ 計測導入の是非（現状計測ゼロ。Cookieレス系＋privacy.html 明記が候補）

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
