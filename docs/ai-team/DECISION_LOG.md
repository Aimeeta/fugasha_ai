# DECISION_LOG — 意思決定の記録

新しい決定は上に追記する。形式: 日付 / 決定 / 理由 / 決定者。

## 2026-07-13 — GSAP再提案を審査 → 却下維持。「夜明けのスクロール」を既存スタックで実装
オーナー依頼「GSAPなど使ったいい案」を2体分隊（gsap-engineer / creative-director）で検討し、実装はメイン＋frontend-engineer cross-review。

- **GSAP導入は再却下**（2026-07-03裁定の維持）: 実測で GSAP core + ScrollTrigger ≈46KB gzip は index.html 本体（≈40KB gzip）を上回る。候補5案（Vision連続化・ヒーローパララックス・SplitText行リビール・引用ブラー・sky月ドリフト）はすべて既存手段（sticky＋自前進捗 / IO＋CSS / rAF）への3〜20行差分で同等以上に実現可能で、再提案条件「既存手段では不可能または著しく劣る」の立証不成立
- **採用: 「夜明けのスクロール」**（creative-director本命。コンセプト「時間が、ページの上を通り過ぎる — UIは動かない、世界だけが動く」）: Vision(sst)の連続進捗pに、左パネルの光膜（`.sst-dawn`・opacity=p²・光のalpha上限0.14〜0.2）・月の沈み（0→56px）・朝日の昇り（44→0px）・進捗バー（scaleY=p）を連続同期。読者のスクロール速度＝夜が明ける速度。**テキスト側は従来の離散フェードを維持**（右パネル背景は不変・コントラスト影響なし）。reduced-motion時は従来の離散切替のみ（光膜は0のまま）
- 進捗バーを height駆動→transform:scaleY駆動へ変更（毎フレーム更新をコンポジタで完結させるため）
- **既存バグ修正（発見は実装検証中）**: `.sst-dot`クリックのスクロール先が `outer.offsetTop`（親sectionがposition:relativeのため常に0）基準でページ先頭付近へ飛んでいた → 文書座標（gBCR.top+scrollY）に修正＋しきい値ちょうど着地を防ぐ+1px。キーボード操作にも効く正しさの修正
- cross-review（frontend-engineer・実測込み）: 重大0・中2（デッドtransition／画面外での毎フレーム書き込み）→ いずれも修正済み（transition削除・前回p同値ガード）
- **保管（未実装・優先順）**: 案3「紙のうえの光」（ヒーロー背景canvasをマウス追従→実時刻の光へ。yohaku/sky/colors/wordsと実時間思想を統一）／案4「月が、今夜まで満ちる」（sky.htmlの月SVGを初回のみ新月→今夜へ2.5s）／案2「罫線が先に読む」（読書位置の少し先まで引かれるヘアライン。調律コスト高）。GSAP的演出の禁止リスト（タイプライター・カウントアップ・pin2箇所目・本文パララックス・bounce系・プリローダー等）は本項の前提として維持

## 2026-07-13 — 余白ページの多エージェント改修（Wave方式）
オーナー指示「余白ページの改善を複数エージェントでよしなに」。CLAUDE.mdの分隊運用に従い実施。

- **Wave1（読み取り専用レビュー・並列4体）**: design-critic / typography-specialist / first-visit-researcher / interaction-designer。P0の収束＝「ライブ状態が"生きている"と伝わらない」「ホバー矢印と右端のライブ値が同じ角で衝突」「項目名と状態値が同じ明朝300で階層が潰れる」。加えて interaction-designer が**スキップリンク破損（`#index`の飛び先id無し＝WCAG 2.4.1）**を検出（メインの見落とし）
- **統合・裁定（メイン）**: 憲法（可読性・アクセシビリティ・パフォーマンス優先／未ロードウェイト禁止／fail-open維持）に照らしP0〜P2へ整理。却下: 索引の英字ラベル化（和文の温かさを優先し和文ラベル＋字間修正を採用）、val全mono化（OS monoが漢字を持たずフォールバックで不統一化するため）
- **Wave2（実装・frontend-engineer）**: スキップリンク修復／`aria-label`削除でライブ状態を読み上げに載せる／右矢印廃止＋ホバー横ジャンプを指標バー(::before)化／状態値を従属化(--fg2)／時計行のみ脈打つドット（reduced-motion対応）／時計をtabular-nums・ゼロ埋め・タブ非表示で停止・分境界整列／タイポ（「余白」字間.18em・リードにpalt・和名/ENスケール・和文ラベルのuppercase無効削除）／状態値を和文レジスタに統一（JULY 13→7月13日）／索引連番01–04／reveal初期ちらつき対策（html.js方式・fail-open厳守）／未使用トークン削除
- **cross-review（a11y-auditor）**: 6変更中5合格。唯一 **2.4.11 Focus Appearance（WCAG2.2 AA）** 未達を検出（entryの::beforeバー＋色変化は状態差2:1で3:1未満）。→ メインが `.entry:focus-visible` に outline（--accent-ink 6.45:1）を復活させて解消・実機のキーボードフォーカスで可視化を確認
- 既知P2（今回未対応・ROADMAP記載）: JS無効時に索引が生成されない（progressive enhancement）／skip着地がh1をスキップ／ナビ英字のlang未指定

## 2026-07-13 — Today「この日、世界では」を毎日必ず表示（空状態の廃止）
オーナー指摘「毎日ちゃんと出来事が出るように」に対応。

- **フォールバック設計**: その日ちょうどの出来事が無い日は、今月の中から日付の近い順に実在の出来事を4件表示（見出しを「この頃、世界では」に切替え、各項目に「○月○日」を付す＝いつの出来事か明示して誤認を防ぐ）。空メッセージ（「収録していません」）は廃止。全12月に日付つき出来事があるため、どの日でも必ず表示される
- **7月データを拡充**: ライヴエイド(13)・ヴァスコ・ダ・ガマ出航(8)・第1回ウィンブルドン(9)・マンデラ誕生(18)・アポロ11号打上げ(16)・マチュピチュ到達(24)・体外受精児誕生(25)・NASA設立(29)・スライス食パン(7)等を追加（すべて広く検証できる出来事）。7月の日別カバレッジ: 1,4,5,6,7,8,9,11,12,13,14,16,17,18,20,24,25,29
- **他月のフォールバック品質**: 各月5〜6件の日付つき出来事で「近い日」表示は成立するが、当月ほどの日別密度はない。当月が来たら随時拡充（ROADMAP）

## 2026-07-12 — 「余白（Yohaku）」ハブ新設・グローバルナビ統合
オーナー承認「YOHAKUで」に基づき、静かなページ群（Focus/Today/Sky/Words）を一枚の目次に集約。

- **名前の選定**: 「庭」案から出発し、より洗練された案として「余白」を採用。決め手は**新概念の発明ではなく既存の語彙の回収**であること — 名言「創造は、余白のあるところに訪れる」、ブログ「余白はサボりではない」、CLAUDE.mdブランド原則「温かさ、発見、余白」と一貫。言行一致がそのままブランドの証明になる。他案（離れ/窓/縁側）は却下
- **新規: `yohaku.html`** — 明るい暖色テーマの目次ページ。索引は各項目が**その日の状態を生きて表示**: 集中→ライブ時計 / 今日→JULY 12 / 今夜の空→月の和名（sky.htmlと同計算） / ことば→本日の著者（QUOTESと同順・`seed % 84`。著者配列を移植、並べ替え禁止を明記）
- **ナビ統合**: 全ページのグローバルナビを **Home / 余白 / Colors / Blog（/ Contact）** に整理。Focus/Today/Sky/Words の個別ナビ項目は 余白 に集約（＝ナビ肥大の解消）。対象: index(nav+drawer)/focus/today/colors/sky/words/privacy/security-ai。contact は最小ナビのため対象外
- **Colors は余白に含めない**（オーナー指示）— Colors はナビ独立のまま
- **英語ページ**: en/index.html のナビ・ドロワーの「Focus」を「Yohaku」に置換（オーナー指示。JAは漢字「余白」、ENはローマ字「Yohaku」で固有名詞化）
- Focus の EN 切替でも i18n で「Yohaku」表示（nav_yohaku 追加）

## 2026-07-12 — Sky Tonight（sky.html）新設 — 外部API不使用の天文計算・月の和名を主役に
オーナー指示「Sky Tonight を作る」に基づく実装。「庭」シリーズの2ページ目。

- **新規: `sky.html`** — 夜テーマ固定の単一HTML。インクは words.html の night テーマ実測値を継承（コントラスト検証済みの値を再利用）。セクション: 今夜の月（SVG描画＋和名）/ 今夜のひとこと / 月の暦（次の満月・新月）/ 流星群ごよみ（11群）/ 特集「月を、待つ」/ 三十夜の名前 / 日の入りと星の時間（8都市）/ 精度と出典
- **中核の判断: 外部API不使用。** 月齢・輝面比・朔望・日の出入りは全てブラウザ内の簡易天文計算（Jean Meeus『Astronomical Algorithms』略式: 太陽黄経＋月黄経13項＋NOAA/Spencer日出入）。**Nodeハーネスで検証済み**: 2017〜2026年の日食・月食6件の瞬間で離角誤差0.07°以内、東京の日の出入り既知値と±1分。誤差の目安（月齢±0.1日・時刻±数分）をページ内に開示
- **月の和名を主役に**（月齢の数字ではなく）: 旧暦の夜数で三十夜の名前を引く。よく知られた伝統名（三日月・十三夜・十六夜・立待月・居待月・寝待月・更待月・二十六夜等）以外は「◯日月」の中立表記とし、典拠の弱い名前を創作しない
- **惑星の見え方（宵の金星等）はフェーズ2に見送り** — 低精度軌道計算の実装コストと検証コストに対し、v1の価値貢献が小さいため
- **グローバルナビには追加しない** — 「庭」ハブ導入（提案中）までナビ改修を保留し二度手間を避ける。導線は Today フッター「今夜の空へ →」と sitemap のみ
- 星空背景は静的SVG（アニメーションなし・固定シード）。canvasループ不使用でCPU/GPUコストゼロ

## 2026-07-12 — Today ページ新設（デジタル・アルマナック）／words.html の名言を統合
オーナー指示「今日と今月を少し特別にする Today ページを追加。名言専用ページ(words.html)の内容を統合。Focus から名言セクションを削除」に基づく実装。

- **新規: `today.html`** — 単一HTML（CSS/JSインライン・ビルドなし）。既存デザインシステム（トークン/ナビ/背景/トースト）を再利用。10セクション: 日付ヒーロー / Quote of the Day / Today in History / This Month in History / Did You Know / The Story of This Month / Born This Month / A Question for Today / Daily Action / Sources & References
- **データ構造**: `MONTHS[1..12]`（events/people/facts/story）+ `SOURCES`（機関単位）+ `QUOTES`（words.htmlの84編を移設）+ `QUESTIONS`/`ACTIONS`。日替りシードは colors/words と共通（`Y*372+(M-1)*31+D`）。日別コンテンツが無い日は月別で埋め、ページが空にならない設計
- **本文はJA主体・見出し/ラベル/カテゴリはEN**（アルマナックの編集的トーン。多言語の作成量も抑制）。名言のみ英日併記
- **出典厳守**: 出典が確認できない出来事・雑学・名言は載せない。名言は出典の確かな古典（パブリックドメイン）＋風雅舎オリジナルのみ（words.htmlの方針を踏襲）。戦争・災害偏重を避け発明/文化/科学/探検を広く採用。**注意: 各出来事の内容はアシスタントの知識ベースで、機関URLは"参考"として提示。公開前に日付・URLの実確認を推奨（push＝本番のため）**
- **背景は全月ライトテーマ固定**（長スクロールの可読性・コントラストを最優先。夜系テーマは不採用）
- **エントランス演出は fail-open**: 既定で表示、JSが `.pre` を付けたときだけ隠す。IntersectionObserver＋スクロール＋2.5秒の無条件バックストップの三重で、JS/IOが動かない環境でも本文が隠れたままにならない（アクセシビリティ＞演出）
- **words.html は残置**（URL直アクセスは可）だがグローバルナビからは Today に置換。共有リンク(#q=)・お気に入りindexを壊さないため削除・リダイレクトはしない
- **ナビ**: index/focus/colors/words の "Words" を "Today" に置換、sitemap に today.html 追加（changefreq=daily）。Focus→Today の控えめな導線を新設、Today→Focus はフッターCTA

## 2026-07-12 — Focus から名言（.msg）機能を撤去
名言・歴史・雑学・日々のインスピレーションは Today に集約する方針のため。Focus はポモドーロ/時計/ToDo/音楽/背景/集中操作に専念。撤去範囲: `.msg-*` CSS・`.msg-wrap` HTML・`MESSAGES`/`pickMessage`/`msgNext`/Nキー/関連呼び出し・i18n(`kbd_quote`/`msg_more`)・ヘルプのNキー行。共有セレクタの `.pomo-task` は保持。

## 2026-07-12 — AI Daily News 自動生成パイプライン（GitHub Actions採用・n8n/microCMS不採用）
オーナー指示「毎日のAIニュースまとめ記事の自動生成・投稿」。推奨構成は n8n + microCMS だったが、「現構成でよりシンプルで安全な方法があればそちらを選択」の委任に基づき裁定:

- **不採用: n8n / microCMS / Vercel Cron** — 本サイトはCMSのない静的HTML + GitHub Pages。CMS導入はフロントエンド全面改修＋新規契約になり、2026-07-03の既決事項（blog/auto-update-brief.md「外部CMS・SSGを導入しない」）にも反する
- **採用: GitHub Actions cron（22:00 UTC = JST 7:00）+ Node標準のみの単一スクリプト** — 新サービス・新契約・依存パッケージゼロ。「下書き」= Pull Request（人間がレビューしてマージ＝公開。既決の「公開は必ず人間が確認」と一致）、「自動公開」= mainへ直接コミット。Variables `NEWS_MODE` で切替
- **情報源は最小構成から**（オーナー指示どおり）: OpenAI News RSS + Hugging Face Blog の公式2本。追加候補は config.json の feedsDisabled に用意済み
- **投稿条件**: 3件未満はスキップ（48h→72h拡大後も）。使用済みURLは7日間再掲しない。同日記事の二重生成防止。ニュースがない日に架空の内容を生成しない
- **セキュリティ**: APIキーはGitHub Secretsのみ（静的サイト側に秘密なし）。公開エンドポイント自体を持たない。許可ドメイン制。フィード本文は信頼できない入力としてLLMに渡し、出典URLはLLM出力を使わずid引き当て（捏造防止）。全テキストHTMLエスケープ
- **microCMSフィールド相当**は実行ログ（automation/data/runs/*.json）に全ニュースの構造化データとして保存 — SNS/メルマガ転用の入力にできる
- 詳細: automation/ai-daily-news/README.md

## 2026-07-12 — ことばページ（words.html）新規追加・Focusの名言機能を独立ページ化
オーナー指示で、Focusページ内の名言機能を独立した没入型ページへ。4体分隊（企画2体並列→統合実装→クロスレビュー2体）。**未push**。

- **ページ名（creative-director裁定）**: `words.html` / ナビ `Words` / タイトル「ことば | 風雅舎」。Inspiration・Mindset等は営業感・コーチング臭で却下。focus.htmlが既に「ことば」と呼んでいた連続性を採用
- **世界観**: 三兄弟の位置づけ — focus「時間の道具（する）」/ colors「散文詩のアンソロジー（つくる）」/ words「言葉の床の間（止まる）」。一日一枚、掛け軸を掛け替えるように
- **主役インタラクション**: 「墨がにじんで、澄む」— 退場.25s→blur(6px)+8pxから.9sで澄む。著者→原文→問いかけが120msずつ追従。reduced-motion時は即時
- **背景**: 写真不使用（転送量・ポップインがCalmを壊す）。CSSグラデ＋光1灯×8テーマ（dawn/noon/mist/forest/bloom/dusk/ember/night）を名言ごとに紐づけ、2層2.8sクロスフェード。夜系2テーマはインク一式切替。全テーマ×インクのコントラストを機械検証（fg≥8.9 / fg2≥6.3 / hint≥4.5、duskのみ--hint暗色化）
- **CD案「時刻6テーマ」とデータ側8テーマの衝突**: 8テーマ採用（名言ごとの細かい背景連動が優る）。時刻の光のロジックは維持
- **名言データ84件（brand-copywriter）**: 古典51件は原典章句まで特定（老子・論語・自省録・セネカ書簡・芭蕉・方丈記・徒然草・ゴッホ書簡・リルケ等）。**誤帰属の流布名言を明示的に排除**（「孔子とされるが論語に不在」等）。出典不明の言葉は使わず風雅舎オリジナル33件で構成。訳文は全て自訳。没後100年未満・現存著者は不使用
- **機能**: 本日のことば（colorsと同じ日替りシード=三兄弟で同じ暦）/ 次へ（ボタン・Space・→・N・スワイプ）/ 気分10カテゴリ / 言語3モード（英日・日・英、lang属性動的切替）/ お気に入り / 書き置き（Reflection Prompt＋メモ、localStorage）/ コピー・SNS・リンク・Web Share / 没入モード（クリック/Esc/Tabで復帰）/ ハッシュ共有 #q=N
- **Focus側**: 「ことば」ウィジェットは集中/休憩の文脈があるため維持し、著者行の下に「もっとことばを →」の導線を追加（i18n対応）。全ページのナビとsitemapにWords追加
- **クロスレビューの波及修正**: words の Serious 2件（トーストのSR通知が visibility:hidden で死ぬ / パネル開中に notice・srLive まで inert）は **colors.html にも同根で存在したため両ファイル修正**。書き置きのdebounceレース（400ms以内の「次へ」で別のことばに保存されるデータバグ・FEがブラウザ再現）も修正

## 2026-07-12 — Color Generator ページ（colors.html）新規追加
オーナー指示で、香水のネーミングのような物語性あるカラーパレット生成ページを新設。6体分隊（企画4体並列→統合実装→クロスレビュー2体）で企画から実装・検証まで完了。**未push**。

- **世界観（creative-director裁定）**: 「色は選ぶものではなく、出会うもの」。色見本帳ではなく"散文詩のアンソロジー"。着地時に日付シードで決まる「本日のパレット」を表示（全訪問者が同じ一篇に出会う）。ページ名 `colors.html` / ナビラベル `Colors` / タイトル「色 | 風雅舎」（focus.htmlの命名規則に整合）
- **主役インタラクション（1つ）**: 生成のたびページ地色が現在パレットの Background へ静かに滲む（16%のみ・reduced-motion時は即時）。憲法「1ページ1主役」を遵守
- **背景の染め方 — CD案とLPD案の衝突を裁定**: CDは「ページ全体を染める」、LPDは「カード内に留める」。**採用=中間案**: UI文字はサイトのテーマ色のまま（コントラスト保証）・ページ地は生成色を16%だけ滲ませる（世界観を確保）。滲み地でのUI文字コントラストは4テーマ×65篇で実測（fg 8.2 / fg2 6.1 / hint 4.55 が最悪）し、`--hint` を #4d525a へ暗色化して AA を担保
- **収録65篇**: brand-copywriter が香水/映画/詩/ホテル風の英語名＋1行詩を作成（商標衝突を回避）。visual-designer の5役割ルール（Background/Surface/Primary/Accent/Text）に沿って各HEXを設計し、**Text/Background 7:1（AAA）を全篇で機械検証**。1篇目はサイト自身の配色「A Quiet Press」（Accent 2.11:1 は既存サイトの実運用どおりの意図的例外・ヘルプに明記）
- **技術方針**: 憲法どおり外部ライブラリ追加ゼロ（Lenisすら不使用）。focus.htmlの設計言語（4テーマ変数・ガラスUI・notice/openPanel/closePanel/setPanelInert/フォーカストラップ/state+localStorage）を再利用。画像からの色抽出も canvas でブラウザ内完結（外部送信なし）
- **全機能**: 生成（Space）/ テーマ14・ムード10フィルタ / ロック再生成 / HEX・RGB・HSL切替 / まとめコピー5形式（HEX/CSS変数/Tailwind/JSON/Gradient）/ お気に入り・履歴（localStorage）/ URL共有 / 6プレビュー / 画像抽出 / フルキーボード操作
- クロスレビュー（frontend-engineer + a11y-auditor）の Serious/Moderate 指摘を反映済み。詳細は QUALITY_REPORT.md

## 2026-07-11 — 人間味監査 Phase 2 実装（構造的リズム改修）
Phase 0/1 に続き、オーナー指示「着手」を受けて Phase 2 を実装。frontend-engineer がクロスレビューし、指摘4件（詳細度バグ・sign-grid巻き添え・間奏の孤立行・noscript漏れ）を修正済み:
- **余白の間奏（#s-interlude）新設**: SERVICES と WAYS OF WORKING の間に、min-height 54vh・中央一文「この、なにもない場所が、余白です。」（serif、初使用の --text-4xl 60px）＋小さな一言のみのセクション。罫線リビールも持たない `.sec-quiet` で、13回同じだった幕開けの完全な例外。モバイルは clamp(22px,7vw,27px) に落として孤立行を防止
- **PHILOSOPHY の骨格例外化**: s-lbl・s-desc を廃止し中央寄せ大見出し（.phi-head）から開始。**3つ組を崩す「4つ目の未完項」**（破線ボーダー・「4つ目を、探しています。決まったら、ここに書き足します。」）を追加し4カラム化（タブレット2×2）。⚠️ 将来の更新約束なので放置しないこと（運用リスクとして記録）
- **タイポのジャンプ率**: .s-h2 38px固定→clamp(32px,4vw,48px)、.ch2 42px→clamp(38px,5vw,60px)。モバイル上書き（28/25px・26/23px）は維持
- **blogフィーチャード記事**: 最新記事を全幅・タイトル clamp(26px,3.6vw,40px)・serif kicker「いちばん新しい記事」。⚠️ 手動運用（新記事追加時にクラスとkickerを移す — グリッド先頭にHTMLコメントで運用メモ記載）。リンクでない飾りの cat-tags は削除
- **見送り**: 2-5（実物写真投入）は本人素材待ち。en/index.html は Phase 0/1/2 とも未反映（JA/EN乖離をROADMAPに記録済み）

## 2026-07-11 — 人間味監査（5エージェント）＋ Phase 0/1 実装
オーナー指摘「AIで作った感が拭えない。単調。遊び心・人間味・私らしさが欲しい」を受け、brand-philosopher / design-critic / first-visit-researcher / Webリサーチ（general-purpose）の4体で監査し、lead-product-designer が統合（報告書: docs/ai-team/humanity-audit-2026-07-11/）。診断の核心は「**例外率ゼロの反復**（同一骨格×11・3つ組×11・格言見出し×5・mono番号9系統）と**人間味の隠し要素への隔離**」。オーナー承認のもと Phase 0（バグ級）＋ Phase 1（人の可視化）を実装、frontend-engineer がクロスレビュー:
- **Phase 0**: contact送信エラー文言に hello@fugasha.jp を明記（従来はアドレス記載ゼロの行き止まり）＋ ft-mini に mailto 追加＋ #submitErr に role="alert"／hover跳ね上げ違反3箇所除去（blog card / h-chip / check-item）／footerタグライン統一（index 16px→大型serif clamp、blog側の uppercase 廃止）
- **Phase 1**: JAヒーローに顔写真バイライン（EN の hp-photo に相当。「このサイトを書いているのも、相談を受けるのも、私です」）／ポートレートの grayscale 解除（彩度.92でトーン維持）／mono英字ラベル間引き＝**「番号=手順、無番号=思想」の原則を導入**（sign-num・phi-num・entry-kicker 撤去、margin-step-num は番号のみ、sv-num は番号なしカテゴリ名）／和語ラベル `.s-lbl-ja` 新設（focus.html の語彙感覚を輸入: 兆し・余白の地図・根にある考え・小さな診断・どこから話しますか？・ふだん使っている道具）／SERVICES見出しを平叙文化（格言構文の声域分散）／SIGNSリードに「以前の私も、そうでした。」（About既存コピーと整合）／blog全8記事に著者ボックス＋「2026年7月・チェンマイの机から」スタンプ／why-freed記事の参考文献（パーキンソンの法則・ジェボンズ）を本文に接続、二重ヘッジ「仮に〜とします」の2箇所目を「測っていなかった」形に／contact Step1 アバターを「風」→顔写真に／footerに正直の一行「風雅舎は、私ひとりの事務所です。このサイトもAIと一緒につくりました——外部スクリプトは、スクロールをなめらかにするひとつだけ。」（クロスレビュー指摘により「私がひとりで書いています」から変更。AIエージェント体制で作られたリポジトリで「ひとりで書いた」は検証可能な虚偽になり得るため、正しさ優先＋AI支援業のドッグフーディングとして開示する判断）
- **却下・保留**: Vision scene01 の一人称化（オーナー確認の結果「深夜2時」は実話でないため**書かない**）／自筆署名SVG・手書きメモ写真（素材保留）／mono番号のセクション見出しへの追加（間引きと逆行）／モーション多様化（Calmに貢献中）／カーソル演出・効果音（声量不整合）／BLOGセクションのサーモン面化（ダーク3面のリズムが痩せるため Phase 2 で再評価）
- **残タスク**: Phase 2（骨格の例外2〜3箇所・余白の間奏・タイポジャンプ率・数の非対称・blogフィーチャード記事）と Phase 3（404・now・マニフェスト等）は ROADMAP 参照。**en/index.html は今回未反映**（sign-num・grayscale・旧footerが残存、JA/EN差異として要判断）

## 2026-07-11 — focus.html 磨き込み（4エージェント精査＋Aセット実装）
creative-director / design-critic / interaction-designer / first-visit-researcher の4体を並列起動しfocus.htmlを精査。指摘は「進捗リング不在／主役の階層弱い／完了演出が貧弱／統計が埋もれる／良い機能が発見されない」に収束。オーナー承認で"すぐ効く磨き込み（Aセット）"を実装:
- **進捗リング新設**: `.pomo-time`をSVGリング（r=46, C=289.03）で囲み、残り時間に応じて弧がほどける（`renderRing`をrenderTimerから毎回呼ぶ／`stroke-dashoffset`, `.3s linear`）。写真背景では`body.on-media`でトラック色を白/黒系に自動切替。
- **完了の余韻**: 集中完了時のみ`#afterglow`（z-index 1、stage z-2の下）に`.show`を付け、accent色の放射が3sで淡く明滅（`@keyframes afterglow`）。reduced-motionは既存の一括ルールで自然停止。文字は鮮明なまま。
- **静かな統計1行**: 既存`state.stats`（completed/focusSeconds、日次リセット済み）を`renderStats`でタイマーパネルに1行表示。棒グラフ・連続日数は入れない（誇大/ゲーミフィケーション回避）。init/finish/パネル開/言語切替で更新。
- **ショートカット拡充＋チートシート**: Space/F/Escのみ→ R(リセット)/S(スキップ)/1・2・3(モード)/M(音楽)/←→(曲送り)/N(次のことば)/?(ヘルプ) を追加。keydownに集約、`toggleMusic`を抽出しミニプレイヤーと共用。ヘルプ表を3→10行、`aria-keyshortcuts`付与。
- **トランジション統一**: backdrop `.35s` linear・スクリム `.9s` ease を`--ease`へ。
- **小修正**: kokeスウォッチ見本色`#d8ddc9`→実地`#e3e8d6`、`.st-clock`に`palt`、音量スライダーに数値表示、名言送りアイコンをリセット(↻)と別の「→」に。
- **見送り/別タスク**: 音楽・背景の拡充（雨/夜の虫/和の環境音/室内背景＝合法素材の調達とライセンス確認が必要）、ことばの拡充（開始フェーズのことばが1つで「N」で変わらない既存の限界）、発見性の初回導線。呼吸ガイド・週次グラフ・連続日数は憲法（Calm/Minimal、誇大回避）により不採用で合意。

## 2026-07-10 — サイト全体監査（5エージェント）＋高優先4件の修正
リリース前レビュー分隊のWave1（frontend-engineer / project-architect / a11y-auditor / performance-auditor / seo-aeo-auditor）を並列起動し、全18ページを読み取り専用で監査。矛盾する指摘は主スレッドで裏取りして裁定（frontend「モバイルでナビ全消失」はindex/en/blogにハンバーガーがあり誤検出、副次ページは"戻る"リンク型ヘッダで機能＝広範な欠陥ではないと確認）。オーナー承認により高優先4件を実装:
- **ai-security-checkpoints記事のテンプレ同期漏れ是正**: 個別OGP画像を生成・配置（セキュリティ=紫の`category-n2`下地）、og:image/JSON-LD imageを個別URL化、不足していたog:image:width/height/locale/site_nameを補完、JSON-LDのauthor/publisherを他7記事と同じname/jobTitle入りインライン形式に統一。
- **contact.htmlフォームのa11y**: 必須2項目に`required`/`aria-required`/`aria-describedby`、エラー文言に`role="alert"`、バリデーションで`aria-invalid`をトグルし最初のエラー項目へフォーカス移動（WCAG 3.3.1/3.3.2/4.1.3）。
- **focus.htmlパネルのフォーカストラップ**: openPanel/closePanelで背後のbody子要素に`inert`付与・解除（backdropは除外）、inert非対応ブラウザ向けにTabトラップのフォールバックを追加。既存のEsc・閉時フォーカス復帰と併せて実機検証。
- **focus.html背景サムネの遅延読込**: 初期化時に18枚の原寸背景JPGを読み込んでいた問題（`buildBgGrids`/`buildTrackList`が`th.style.backgroundImage=url(原寸)`を即設定、パネルは`display:none`でなく`translateX`）を修正。URLを`data-lazybg`に退避し、**そのパネルを開いたとき**に`loadLazyThumbs`で初めて読む方式に変更（IObserverはこの環境で`.open`のtransform非適用のため不採用、パネル開トリガーの方が決定的）。実機で「初期の背景画像リクエスト0件／パネル開で18件」を確認。
- 未対応の中〜低優先（トークンドリフト`--accent-ink`、skip-link横展開、記事間相互リンク、chat.htmlのrobots、sitemap lastmod同期、CTA文言統一等）はROADMAP行き。

## 2026-07-08 — トップページ（index.html / en/index.html）UI/UX監査＋修正
オーナー指示「トップページのUI/UXを改善したい、レスポンシブか確認、デバッグしてほしい」を受け、6体のエージェント（first-visit-researcher/visual-designer/interaction-designer/a11y-auditor/performance-auditor/seo-aeo-auditor）を並列起動して監査し、私自身もブラウザ実機（モバイル375px/タブレット768px/デスクトップ1024px、日英両方）で検証。確実なバグのうち高〜中優先度を実装、a11y-auditorでクロスレビュー。
- **日英の構造差異について**: 日本語版はビジネスLP（業務時間チェッカー/Margin Map/Vision演出等）、英語版は創業者プロフィール型ページで、実質的に別ページ構成であることが判明。オーナー確認の結果「現状のまま維持する」（意図的な差別化として継続）。
- **`.ph-badge`のタッチ操作対応**（index.htmlのみ）: hoverのみに依存し、タッチデバイスで裏面コンテンツ（読書家/哲学好き）が一生表示されない不具合を修正。`aria-pressed`+click/keydownハンドラを追加。
- **モバイルドロワーのフォーカストラップにフォールバック追加**（日英共通）: `inert`属性のみに依存していたため非対応ブラウザ（Safari 15.4未満等）でTabトラップが機能しない問題に、フィーチャー検出によるフォールバック（Tabキーのループ制御）を追加。
- **モバイルドロワーに`<nav>`ランドマークを追加**（日英共通）: 裸の`<a>`並びを`<nav aria-label>`でラップ。視覚崩れ防止のため`.nav-drawer-links`に元のflex/gap設定を移設。
- **`.sst-dot`のタップ領域拡張**（index.htmlのみ）: 視覚サイズ4px×20pxのみだったタップ領域を、`::before`疑似要素で24×24px相当に拡張（WCAG 2.5.8目安）。
- **`sitemap.xml`に`focus.html`を追加**: 既知の未登録問題を解消。
- **FAQPage JSON-LDに`inLanguage`を追加**（index.htmlのみ）: 英語版と構造を統一。
- **CLAUDE.mdのフォント仕様記載を実態に合わせて修正**: JetBrains Monoは実際には読み込まれておらず`--font-mono`はOS標準等幅スタックだったため、Webフォント追加ではなくドキュメント記載を訂正（パフォーマンス優先の判断）。
- **見送った項目**（優先度低、または未着手）: border-radius/影のトークン化、装飾的h2見出しの言い換え、日英FAQPage構造の完全統一（WebPage/WebSiteノード）。次回以降の課題としてROADMAPに反映予定。

## 2026-07-08 — focus.html UI微調整（ミニプレイヤー・再生コントロール・引用の可読性・ドラッグハンドル・4K画像）
オーナー指摘5点に対応。
- **ミニプレイヤー**: ツールバーとの間隔が狭く配置が窮屈だった問題を修正（bottom offset 82px→92px）。イコライザー(3本バー)を単一のパルスドットに簡素化し、`.pomo-tabs`と同じガラス言語（pill形状・blur+saturate・var(--bg2)地）に統一。
- **再生コントロール**: 開始/スキップ/リセットのテキストボタンを、タブと同系統のガラス円形アイコンボタンに変更（開始は accent 塗りで主役化）。アクセシビリティ用に aria-label を動的更新（`data-i18n-aria`属性をapplyI18nに追加）。
- **引用（ことば）の可読性**: 写真/動画背景の上で暗背景と判定されても文字色の分類が局所的に外れるケースがあり読みにくかったため、`body.on-media .msg-wrap` にガラスの受け皿（半透明パネル+blur）を追加。テキスト色は常にテーマの --fg2 系に載るため背景の明暗に関わらず可読。
- **やることリストの並べ替えハンドル**: 6点グリップの色が `var(--line)`（罫線相当・ほぼ不可視）だったため視認できなかった不具合を修正。`var(--hint)`基調＋ホバーで濃色化。またストローク描画からNotion風の塗りドット（`svgDots`ヘルパー）に変更しクッキリ表示。
- **背景画像の高解像度化**: 2560×1440→**3840×2160(4K)**で全18点を再取得、JPEG品質もq58〜74→**q75〜84**に引き上げ（1枚あたり約0.4〜1.5MB、選択時のみオンデマンド読込のため許容）。大画面での粗さを解消。
- 副次修正: `.pomo-tab[aria-pressed]`と`.pomo-btn`のon-media上書きで、ブラウザのカスケード解決が期待と異なる挙動を示したため、冗長な`color`宣言を削除し基底ルールの`color: var(--fg/--fg2)`（`.stage`スコープで既に明暗対応済み）に一本化。挙動が単純化し、写真の明暗に応じて自動的に正しい文字色になることを実機確認。

## 2026-07-08 — focus.html 実音源(KM)導入・写真高解像度化・品質磨き
オーナー指摘（曲が安っぽい／写真がズームで全体が見えない／背景の選択肢を増やす／mihata水準に近づける）に対応。design-criticを起動して品質ギャップを洗い出し、上位項目を反映。
- **音源を実素材に差し替え**: Kevin MacLeod（incompetech.com, **CC BY 4.0**）の楽曲7曲を直リンクDL→afconvertでWAV化→中間部を約107秒抽出しクロスフェードでシームレスループ化→AAC 96k(各約1.2MB)。合成の「曲」5点は廃止。プリセットは Ambient(Deep Haze/Air/Crypto)／静かな調べ(Constance/Meditation/Angel Share)／Cinematic(Anguish)／自然(Forest Stream/Fireplace=合成環境音は継続)。音楽パネルにCC BYクレジット表記。実曲/Lo-fiはYouTube入力で。
- **写真のズーム解消＋増量**: 全背景を1600→**2560×1440**で再取得（大画面で拡大されずシャープに。object-fit:coverは維持）。実写真を12→**18点**に増量（岩峰/雪の谷/山の夜明け/星降る山/霧の森/森の湖 を追加）。山と森/水辺の2群、動画対応7点。総容量約7.3MB(オンデマンド読込)。
- **品質磨き（mihata水準へ, design-critic反映）**: スクリムを一律0.34→**上下濃・中央淡のグラデ**に（写真の質感を残しつつ文字を守る）。パネル/ツールバー/ミニのガラスに`saturate()`＋多層影で質感向上。背景クロスフェードを0.6→1.2sに。時計のタイポを詰め(letter-spacing -0.01em, line-height 1.04, 秒を従属化)。emberアニメを4.5→16sで静穏化。
- 差し替え口は不変（背景=PHOTOS[].img / 音源=TRACKS[].src）。KMはCC BYのため帰属表示を維持すること。

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
