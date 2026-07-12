# QUALITY_REPORT — 最新の検証結果

最終検証: 2026-07-12（余白ハブ新設・ナビ統合）

## 余白（yohaku.html）ハブ新設・グローバルナビ統合（2026-07-12）
新規: `yohaku.html`。ナビ変更: index/focus/today/colors/sky/words/privacy/security-ai/en。sitemap更新。

### 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | yohaku 抽出 → `node --check` / focus.js 再検証 | ✅ 両OK |
| タグ整合 | yohaku マークアップ開閉カウント | ✅ 全一致 |
| コンソール | yohaku / focus | ✅ エラーゼロ |
| ライブ状態 | 集中=時計23:14 / 今日=JULY 12 / 今夜の空=二十八日月 / ことば=—モンテーニュ | ✅ 各ページと一致（月＝sky.html、著者＝seed%84） |
| ナビ配線 | 全9ページ＋enが yohaku を指す / Focus・Today の旧nav項目残存なし | ✅ grep一致・残存0 |
| i18n | focus.html EN切替で 余白→Yohaku | ✅ 切替動作 |
| リンク解決 | 索引4項目の href（focus/today/sky/words） | ✅ 正 |
| モバイル | 375px横溢れ判定 | ✅ 溢れなし |
| エントランス | fail-open（.pre＋2.5sバックストップ、スタッガー付） | ✅ 5/5表示 |

### 未検証（開示）
- contact.html は独自の最小ナビ（戻るリンクのみ）のため 余白 未追加（意図的）
- 実機（iOS/Android）・スクリーンリーダー通し — 未実行

## Sky Tonight（sky.html）新設（2026-07-12）

## Sky Tonight（sky.html）新設（2026-07-12）
新規: `sky.html`。変更: `today.html`（フッターに導線）、`sitemap.xml`。

### 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| 天文計算の正確性 | Nodeハーネス: 日食3件（2017/2024/2026）・月食3件（2018/2022/2026）の既知の瞬間で離角を検定 | ✅ 全て誤差0.07°以内（月齢換算±0.006日） |
| 朔望の探索 | 次の新月が2026-08-12日食と一致するか（7/20起点） | ✅ 2時間以内で一致 |
| 日の出入り | 東京の既知値（7/12 日の入18:58・日の出4:34 / 冬至16:32）と比較 | ✅ 全て±1分 |
| 今夜の表示値 | 2026-07-12: 月齢27.3・輝面比5%・二十八日月・次の新月7/14・次の満月7/29 | ✅ ハーネスと一致 |
| 月SVGの向き | 欠けていく月が左側に光る（北半球の見え方） | ✅ スクリーンショットで目視確認 |
| inline JS 構文 | 抽出 → `node --check` | ✅ OK |
| タグ整合 | マークアップの開閉カウント | ✅ 全一致 |
| コンソール | ローカルサーバー＋ブラウザ | ✅ エラーゼロ |
| 条件分岐 | 今夜のひとこと: 月明かり少＋みずがめ座δ南活動開始(7/12)の分岐 | ✅ 正しい枝に入る |
| 流星群バッジ | 活動中/見頃/三大の判定（年またぎ含むロジック） | ✅ δ南のみ「活動中」= 正 |
| 地点切替 | 東京→那覇(19:25)→札幌(19:14)、localStorage永続化 | ✅ 実際の日没と数分以内・保存OK |
| モバイル | 375pxで横溢れ判定 | ✅ 溢れなし |
| エントランス | fail-open（.pre方式＋2.5sバックストップ）today.htmlと同実装 | ✅ 同方式を移植 |

### 未検証（開示）
- **流星群の極大日・活動期間**は国立天文台の解説に基づく年平均値（±1日前後する旨をページ内に明記）。2026年個別の予報とは未照合
- **月の和名の典拠**は歳時記・辞典類に広く見える記載。個別の文献照合は未実施（伝統名以外は「◯日月」の中立表記とし創作を回避）
- 那覇・札幌の日没は記憶値との照合（±数分）。8都市全数の公的値との照合は未実施
- 実機（iOS/Android）・スクリーンリーダー通し — 未実行



## Today ページ新設 / Focus 名言撤去（2026-07-12）
新規: `today.html`。変更: `focus.html`（名言撤去＋Today導線）、`index.html`/`colors.html`/`words.html`（ナビ）、`sitemap.xml`。

### 実行した検証（ローカルサーバー＋ブラウザ）
| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | today/focus を抽出 → `node --check` | ✅ 両OK |
| タグ整合 | today.html マークアップの開閉カウント | ✅ 全一致 |
| コンソール | today.html / focus.html | ✅ エラーゼロ |
| セクション描画 | DOM問い合わせ（10セクション・件数） | ✅ 今日の出来事4件/今月6+全11/雑学/物語2/人物5/問い/行動/出典6 |
| 月別データ充足 | 全12月 events≥5・people≥3・facts≥3・story≥1 | ✅ 全月充足（空にならない） |
| 空状態フォールバック | 出来事の無い日(7/2)で day filter=0 | ✅ 空ノート＋月別で埋まる設計を確認 |
| インタラクション | お気に入り/コピー/次へ/View all/雑学切替/問い保存/行動チェック | ✅ 動作＋localStorage永続化 |
| モバイル | 375px で横溢れ判定 | ✅ 溢れなし（横スクロールrailのみ内部スクロール） |
| エントランス fail-open | `.reveal` 16件が2.5sバックストップで全表示 | ✅ 16/16（本文が隠れ残らない） |
| Focus 名言撤去 | .msg-wrap/#msg 消失・タイマー/モード切替・Today導線href | ✅ 残存ゼロ・回帰なし |
| ナビ整合 | 全HTMLで Words除去・today.html配線 | ✅ grep一致 |

### 未検証（開示）
- **各歴史・雑学・人物の内容はアシスタントの知識ベース。機関URLは"参考"提示で、個別URLの実在・解決は未確認。** push＝本番のため、公開前に日付・URLのスポット確認を推奨
- スクロール連動のエントランス演出の"見た目": プレビュー環境がバックグラウンドタブとしてIO/スクロール/タイマーを抑制し、スクロール後のラスタも再描画されないため**目視スクリーンショット未取得**（DOM問い合わせ=elementFromPoint/getBoundingClientRectで内容・レイアウトは確認済み）。フォアグラウンドの実ブラウザでは標準IOで動作
- 実機（iOS/Android）・スクリーンリーダー通し・Lighthouse計測 — 未実行

## AI Daily News 自動生成パイプライン（2026-07-12）

## AI Daily News 自動生成パイプライン（2026-07-12）
新規: automation/ai-daily-news/（run.js・config.json・template.html・mock-feed.json・README.md）、
.github/workflows/ai-daily-news.yml、assets/favicons/（openai/huggingface）、blog/index.html のカード挿入マーカー。

### 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| スクリプト構文 | node --check / workflow は yaml.safe_load | ✅ OK |
| モック実行（全経路） | --mock で記事生成→カード挿入→sitemap追記→ログ | ✅ 生成物をブラウザで確認（既存ブログデザインと調和・コンソールエラーゼロ） |
| 実RSS取得 | --fetch-only で OpenAI/HF の実フィード | ✅ 1040+823件パース（RSS/Atom両対応）、72h窓で候補3件抽出 |
| 二重生成防止 | 同日再実行 | ✅ スキップ発火 |
| 注入テスト | mock-feed.json に命令文を混入 | ✅ 記事に出力されない（FEも独立確認） |
| 外部依存 | 生成記事のリソース | ✅ Google favicon依存を排し自己ホスト化（既存記事と同方式）、fetch 200確認 |
| LLM実呼び出し | — | ⚠️ **未検証**（APIキーが必要。オーナーのSecret設定後、workflow手動実行で最終確認する） |

### クロスレビュー（frontend-engineer・再現確認つき）への対応
- **C-2 replaceAllの$特殊置換でHTML破損（再現済み）**: split/joinのliteral置換に全面変更（カード挿入含む）
- **C-1 Atomのrel="self"誤選択（再現済み）**: rel="alternate"優先の選択ロジックに修正
- **E-1/O-1 スキップ日でもログだけのPRが立つ**: runs/ を .gitignore 化し、Actions artifact（90日）へ
- **O-2 PRブランチへのforce push（CLAUDE.md禁止事項）**: 除去。同名ブランチ残存時はworkflow失敗で気づく設計に
- **O-3 モック実行が本番used-urls.jsonを上書き（再現済み）**: モック時は書き込まない
- **S-1 JSON-LDの</script>脱出（理論）**: < を < へエスケープ
- **C-3 出典日付のUTC/JSTずれ**: JSTに統一 ／ **E-3** リトライ枯渇時のエラーメッセージを実因に ／ **M-1** プロンプトのプレースホルダを{{}}形式に
- **レビュー最重要指摘**: 巻き戻し手順が未コミットのマーカーを破壊する問題 → README の手順を修正（レビュアーが検証中に実際に踏んで復旧済み）
- 見送り（開示）: C-4 相対URLフィード（公式フィードは絶対URLのみ・追加時に注意としてREADME記載）/ O-6 draftモードのdedupはマージ後に効く（許容リスクとしてREADME記載）
- O-5 モデルID `claude-sonnet-5` は現行の有効なAPIモデルIDであることを確認済み

### 未検証（開示）
- LLM実呼び出し〜PR作成のエンドツーエンド（ANTHROPIC_API_KEY 設定後に Actions 手動実行で確認すること）
- スケジュール実行の初回発火（cronはGitHub側で数分遅延することがある）

## ことばページ新規追加（2026-07-12・push済み）
新規: `words.html`（単一HTML・約990行・外部依存ゼロ）。名言84件の没入型表示ページ。
変更: focus.html（「もっとことばを →」導線＋ナビ）/ index.html・colors.html（ナビ）/ sitemap.xml / **colors.html（words監査で見つかった同根Serious 2件の波及修正）**

### 分隊（4体・波状）
企画並列2体: creative-director（コンセプト・8背景の裁定・禁じ手）/ brand-copywriter（84件・出典検証・自訳）→ 主スレッド実装 → クロスレビュー並列2体: frontend-engineer / a11y-auditor

### 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| データ整合 | node で84件の構造・カテゴリ・背景・重複を機械検証（FEが独立再実行） | ✅ エラー0・全10カテゴリ7件以上・全8背景6件以上 |
| 背景×インクのコントラスト | WCAG式（グラデ端点＋光の最濃部ブレンド） | ✅ 全テーマ fg≥8.9 / fg2≥6.3 / hint≥4.5（dusk専用--hint #454a51 で担保） |
| inline JS / タグ整合 | 抽出→node --check＋開閉カウント（words/colors/focus/index） | ✅ 全て OK |
| 全機能 | ローカルサーバー＋ブラウザ（デスクトップ/モバイル375px） | ✅ 本日のことば・次へ・にじみ遷移・背景クロスフェード・気分フィルタ（Calm選択→全件適合を確認）・言語3モード・お気に入り・書き置き・没入モード・ハッシュ復元・導線 |
| コンソール | 両ページ・全操作後 | ✅ エラーゼロ |

### クロスレビュー指摘への対応（FE 15件＋a11y 15件を統合）
- **S（words・colorsに波及）**: トーストがvisibility:hidden中SRに読まれない → SR通知を常時可視の#srLiveへ一本化（rAF非依存・同一文回避付き。プレビュー環境でrAF不発を実測し同期方式へ）/ パネル開中に notice・srLive がinert → 除外リストに追加。**両ファイル修正・ブラウザで確認**
- **高（FEがブラウザ再現したデータバグ）**: 書き置きdebounce中の「次へ」で別のことばに保存 → 入力時点のidx捕捉＋切替時フラッシュ。修正後に保存先が正しいことを実測確認
- **中**: 連打時の出フェーズタイマー未追跡（outTimer追加）/ 'use strict'が無効位置（両ファイルIIFE先頭へ）/ ?・→キーのスコープをcolorsと統一（2.1.4）/ QUOTES末尾追記のみ運用の設計コメント追記 / qPromptのlang付与範囲 / fav削除後のフォーカス喪失（panel-close等へ復帰＋通知）/ 気分選択のモード変更通知（next後に通知）
- **低**: 没入中トーストの閉じるで没入解除される / eyebrowがフィルタ外のことばに誤ラベル / Nキー未記載 / aria-haspopup=dialog付与 / フォーカストラップselector統一（textarea/select、colorsも）/ qSubをblockquote内へ（視覚順: 本文→原文→著者）/ reduced-motionのtransition-delay全体打消し / q-anim-outにfilter/transform追加 / openPanelのlastFocus上書きガード

### 見送り・未検証（開示）
- 実機（iOS VoiceOver / Android TalkBack）での没入モード脱出経路 — コード上はクリック/Esc/focusinの三重脱出だが実機未検証（a11y M-4）
- お気に入り一覧はENモードでも日本語表示（保存物は原典表示という意図的判断）
- noscriptフォールバック（三兄弟共通の別タスク候補）/ aria-labelledbyへの統一 / eyebrow英語部分のlangスパン
- 名言カード画像の書き出し（オーナー了承済みの後回し）/ 実機スワイプ

## Color Generator ページ新規追加（2026-07-12・push済み）
新規: `colors.html`（単一HTML・CSS/JSインライン・約1420行・外部依存ゼロ）。65篇のカラーパレット生成ツール。
変更: index.html / focus.html のナビに「Colors」追加、sitemap.xml に colors.html 追加。

### 分隊（6体・波状）
- 企画（並列4体）: creative-director（世界観・主役Ix）/ brand-copywriter（64名＋詩）/ visual-designer（配色システム・ムード→HSL・ロック再生成・画像抽出規則）/ lead-product-designer（IA・ワイヤー・キーボード・モバイル）
- 実装: 主スレッドが統合実装
- クロスレビュー（並列2体）: frontend-engineer（コード品質）/ a11y-auditor（アクセシビリティ）

### 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | 抽出 → `node --check` | ✅ OK |
| タグ整合 | div/button/aside/main/nav/ul/section/header 開閉カウント | ✅ 全一致 |
| パレット構造 | 65篇・hex形式・名前重複を機械検証 | ✅ 不正0・重複0 |
| コントラスト（収録65篇） | WCAG相対輝度式で全325色を計算（FEが独立再計算で裏付け） | ✅ Text/BG 7:1以上（AAA）全篇 / Primary・Accent/BG 3:1以上（例外: ブランド配色 A Quiet Press の Accent 2.11:1 のみ意図的・ヘルプ明記） |
| コントラスト（生成物・画像抽出物） | 自動補正（fixText/fixAgainst）→ ブラウザ実測 | ✅ 抽出テストで Text/BG 12.9:1・Primary/BG 3.18:1 |
| ページ地色滲み（16%）| 4テーマ×65篇でUI文字コントラスト計算 | ✅ fg 8.2:1 / fg2 6.1:1 / hint 4.55:1（最悪）→ AA担保 |
| 全機能 | ローカルサーバー＋ブラウザ（デスクトップ1280 / モバイル375） | ✅ 生成・Space・テーマ/ムードフィルタ・ロック再生成・HEX/RGB/HSL切替コピー・まとめコピー5形式・お気に入り・履歴・URL共有・6プレビュー・画像抽出・トースト |
| localStorage 無効時 | getter例外を注入して generate/fav 実行 | ✅ 例外を投げず動作継続 |
| コンソール | デスクトップ/モバイル | ✅ エラー・警告ゼロ |

### クロスレビュー指摘への対応
- FE **M-1**（inert欠落）/ a11y **#1**（閉パネル・トーストがTab順に残る=Serious）: 全パネルを初期inert化＋開閉で管理、トーストに visibility:hidden。→ ブラウザで閉パネル内フォーカス可能要素0件を確認
- FE **M-2**（blob revoke漏れ）: 前回URLを保持し次回選択時に解放
- FE **M-3**（renderSaved毎回全再構築）: dirtyフラグで保存パネル開時のみ描画。→ 生成3回で履歴DOM不変・開いた瞬間反映を確認
- a11y **#2**（focusリングが61%の色で3:1未満=Serious）: `.sw-color:focus-visible` を `--sw-ink`（輝度適応色）3pxに変更
- a11y **#3**（--hint が暗パレット滲み地で4.5未満=Serious）: `--hint` を #5f646c→#4d525a に暗色化（最悪地4.55:1を実測確認）
- a11y **#4**（単一キーC/H/S常時発火=2.1.4）: ツール領域フォーカス時のみ発火に制限。→ navリンク上でH不発火を確認
- a11y **#5**（navリンクのタップ領域）: padding付与で高さ24px以上
- a11y **#6/#7/#8/#10/#11** + FE L-6: palName/生成名に lang="en"、nav に aria-label、ロックラベル固定化、main に tabindex=-1、プレビュー切替を aria-live 通知、生成通知にテーマ/ムード追加

### 未対応（開示・低優先）
- a11y #9（テーマchipのradiogroup化）: aria-pressedトグルは「選択解除可能な単一選択」として許容範囲と判断し見送り
- FE L-1/L-2（中間輝度背景の共有リンク＋ロックで Primary/Accent が稀に3:1未満）: 手作りURLでのみ到達する極端ケース。通常操作では踏まない
- a11y #4 の残余: ツール既定フォーカス（body）では単一キーが有効。ページに文字入力欄がないため実害小と判断
- 実機（iOS Safari / Android Chrome）・実スクリーンリーダーでの通し確認は未実施（シミュレートのみ）

## 人間味監査 Phase 2（2026-07-11）
変更: index.html（間奏セクション・PHILOSOPHY再構成・タイポclamp）/ blog/index.html（featured・cat-tags削除）

| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS / タグ整合 | node --check＋開閉カウント | ✅ OK |
| 間奏・PHILOSOPHY・featured の表示 | ローカルサーバー＋ブラウザ（1280px）でスクリーンショット目視 | ✅ 間奏60px中央・4カラム＋破線の未完項・全幅featured |
| タイポ計測 | computed style（1280/900/375、リサイズ後は再読込） | ✅ s-h2 48→36→25px / ch2 60→23px / interlude 60→26.25px |
| クロスレビュー | frontend-engineer（read-only） | 指摘4件を修正: ①.phi-item-open::before の詳細度負け（線が残るバグ）②.sign-grid のタブレット2カラム巻き添え（3カラム復帰を900pxで計測確認）③375pxで間奏が「が、」の孤立行（clamp(22px,7vw,27px)で2行組を計測確認）④noscript に .phi-t/.phi-b＋filter解除を追加 |
| sectionIds / noscript / reduced-motion | コード読解＋レビュー計測 | ✅ 's-interlude' 追加済み・interlude/phi ともフォールバックあり・グローバル reduce ルールが適用 |

未検証（開示）: ブラウザペインのビューポートが断続的に幅0になる既知の不安定挙動のため、CTAセクション60px見出しとタブレット帯の**スクリーンショット**は取得できず computed style 計測で代替。Safari・実機・JS無効の実機トグルは未実施。

## 人間味監査 Phase 0/1（2026-07-11）
変更: index.html / contact.html / blog/index.html / blog/全8記事/index.html（＋docs/ai-team/humanity-audit-2026-07-11/ 新規）

| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文（index/contact/blog） | script抽出→node --check（JSON-LDはjson.loadsで別途検証） | ✅ ALL OK |
| タグ整合 | 主要タグ開閉カウント（変更11ファイル） | ✅ 不整合なし |
| 削除クラスの参照残り | grep（sign-num/phi-num/entry-kicker、@media・JS含む） | ✅ 0件 |
| 実ブラウザ表示 | ローカルサーバー＋ブラウザペイン（デスクトップ/モバイル375px）。ヒーローバイライン・兆し/余白の地図ラベル・カラーポートレート・footer・記事著者ボックス・contact顔アバターを目視 | ✅ 崩れなし・コンソールエラー0件 |
| クロスレビュー | frontend-engineer（read-only）が全変更をレビュー | 指摘5件を修正済み（noscriptへ.h-byline追加／alt重複解消／.tools-lbl serif化／#submitErr role="alert"／記事挿入文の指示語） |
| コピーの事実性 | 「外部スクリプトはひとつだけ」= script src は Lenis 1件のみで事実。「ひとりで書いています」はAIエージェント体制と矛盾するため「AIと一緒につくりました」に変更 | ✅ 裁定済み |
| hover跳ね上げ違反 | 全HTMLで `:hover`+translateY を grep | ✅ 0件（跳ね上げ非該当のアイコン微動等のみ） |

未検証（開示）: JS無効・reduced-motion はコード読解ベース（noscriptフォールバックに .h-byline を追加済みだが実機トグル未実施）／Safari・実機タッチ端末／ブラウザペインのスクリーンショットが後半フレーク（viewport幅0になる既知の不安定挙動）したため、レビュー後の footer 文言・.tools-lbl は computed style で確認（スクショなし）。

## ブログ4記事拡充（favicon・目次・inline CTA・本文加筆）
変更: blog/{margin-is-not-laziness, why-freed-time-fills-up, finding-your-first-ai-task, ai-security-checkpoints}/index.html、assets/favicons/（新規5画像）

| 項目 | 方法 | 結果 |
|---|---|---|
| node --check / タグ整合（4記事） | script全ブロック抽出・主要タグ開閉カウント | ✅ ALL OK |
| favicon 5枚 | ローカルサーバーでHTTP 200確認、目視で個別画像であることを確認（政府系3ドメインはfavicon.ico直接取得に切替） | ✅ |
| 文字数・読了時間 | node正規表現で実測、meta表示を実測値に更新 | ✅ margin 1.56x/finding 1.58x/security 1.75x/why-freed 1.50x |
| スクリーンショット | CDP Emulation.setDeviceMetricsOverride で真の375px幅を強制し再撮影（初回はheadless Chromeが375px指定でも500pxにクランプする既知の制約を発見） | ✅ 8枚、目次・inline CTA・favicon付き参考文献を目視確認 |
| TOCアンカー整合 | href/id一致を機械確認 | ✅（実クリックでのジャンプ動作は未検証） |
| 禁止語・誇大表現grep | 「定着」1件検出→文脈確認の上ユーザー承認で維持、「完璧」は反-誇大の文脈で問題なし | ✅ |

未検証（開示）: 実ブラウザでのTOCクリックジャンプ・Safari/Firefox表示・reduced-motion実機トグル。

## 新記事＋ブログ2カラムテンプレート（2026-07-06）
変更: blog/why-freed-time-fills-up/（新規）・blog/margin-is-not-laziness・blog/finding-your-first-ai-task・blog/ai-security-checkpoints（テンプレ改修）・blog/index.html・sitemap.xml

| 項目 | 方法 | 結果 |
|---|---|---|
| node --check / タグ整合（4記事） | script全ブロック抽出・主要タグ開閉カウント | ✅ ALL OK |
| JSON-LD parse | 4記事とも | ✅ |
| 参考文献URL実在確認 | curl実UAでHTTPステータス確認、全9件 | ✅ 全件200（403だった経産省PDF数件は実在確認できる代替に差し替え済み） |
| スクリーンショット | ヘッドレスChrome 1280px（2カラム）・375px（縦積み）×4記事＝8枚 | ✅ 目視確認、崩れなし |
| 1024px境界 | 1023px/1025pxの比較撮影 | ✅ 本文の押し潰れなし |
| nav-cta色統一 | grep確認 | ✅ ai-security-checkpointsの白文字残存を発見・修正、4記事とも統一 |

未検証（開示）: reduced-motion実機トグル・正確なコントラスト比計算・Tabキー実機トレース・sticky top:96pxの厳密なピクセル調整。

## 監査A・B群 実装（2026-07-05）
変更: index.html / en/index.html（noscript・split-word・チェッカーaria-live・cta-manifesto削除・entry-card文言・ヒーロー「無料」）/ chat.html（自動コピー・help文・mailtoリンク・空欄表記）/ contact.html（Q3削除・pre-line・返信約束・完了画面）/ privacy.html（相談メモ言及）/ blog/index.html・blog/ai-security-checkpoints/index.html（タイプライター削除）

| 項目 | 方法 | 結果 |
|---|---|---|
| 実装エージェント中断からの引き継ぎ | A群8項目を個別grep/読解で再検査 → noscript・aria-liveは既に実装済みと確認、他は完了 | ✅ 8/8完了 |
| node --check / タグ整合（9ページ） | script全ブロック抽出・主要タグ開閉カウント | ✅ ALL OK |
| 残存チェック | grep: cta-manifesto/urgency/24時間以内/検討状況 = 全ファイル0件 | ✅ |
| contact Q1→Q2→Step2 フロー | **CDP（Chrome DevTools Protocol）で実クリック駆動** | ✅ Q2/2ラベル・#cUrgency消滅を実測 |
| confirm画面のメモ整形 | CDPでStep3まで進めpre-line適用を実測 | ✅ 改行保持を確認 |
| chat 4問→メモ→CTA/mailto | CDPで全4問クリック駆動 | ✅ CTA文言・mailto href（相談メモ本文含む）を実測 |
| blogタイプライター削除 | reduced-motion環境でヘッドレスChromeスクリーンショット | ✅ 静的フッターに統一、演出なし |

未検証: クリップボード実書き込み成功経路（headless環境で権限プロンプト不可のため、フォールバック分岐のみ確認）/ 実機VoiceOver / 「多くの場合は当日中」の事実性（未確認のため不採用）。

## フォント統合＋残改善バッチ（2026-07-04）
| 項目 | 方法 | 結果 |
|---|---|---|
| フォント転送量 | netlog 実測（前回と同手順） | woff2 1.53MB→**1.23MB**・122→88リクエスト・CSS 207.5→147.6KB |
| ウェイト置換の網羅 | スクリプトで全ヒット数検証（40+箇所×1ヒット） | ✅ 取りこぼしゼロ |
| 残存 w300 が serif のみ / mono に 400 以外なし / JetBrains 参照ゼロ | ルール単位の機械検査 | ✅ 疑似ウェイトなし |
| 9ページの構文・タグ整合 | node --check / JSON / タグカウント | ✅ ALL OK |
| ツールグリッド・見出しw400・ブログ記事 | ヘッドレスChromeスクリーンショット目視 | ✅ 崩れなし・階層維持 |
| バッチ5項目（マーキー/a11y/画像/PNG/LCP） | 中断エージェントの成果を全項目再検査 | ✅ 完了確認 |

未検証: Windows実機（Consolasフォールバック）のトラッキング / 小級数serif見出し4箇所の1xディスプレイ確認 / 公開URLでのPageSpeed再計測。

## ディスプレイタイポ縮小（2026-07-04・オーナーFB起点）
変更: index.html / en/index.html（B-1〜B-8: h-en削除・about-catch 26px化・フッター結び文化・manifesto-k monoラベル化・カウントアップ/スライダー静的化・9px→10px・フッターコントラスト）

| 項目 | 方法 | 結果 |
|---|---|---|
| node --check / タグ整合 | 両ファイル全ブロック | ✅ |
| 残存参照 | h-en / dots / aboutMini / ab-n1,2 / 9px の grep | ✅ 全て0件 |
| computed style | 実ブラウザで about-catch 26px・ftb 16px w400・manifesto-k 11px mono 等を実測 | ✅ |
| レイアウト | ja/en × about・cta-footer × 1440/768/375 の12枚スクリーンショット目視 | ✅ 崩れなし |
| 375px 横はみ出し | scrollWidth=375 | ✅ |
| reduced-motion / タブ順 | force-prefers-reduced-motion・dots消滅確認 | ✅ |

未検証: Safari/Firefox 描画・実機タッチ。

## 英語版改善＋全体監査の波（2026-07-04・2度目のリリース）
変更: en/index.html（Cases・タイポ・FAQPage JSON-LD・OGP差替）/ en/ogp.jpg・ogp-source-en.html 新規 / index.html（stream-labelバグ・フッターENリンク・マーキーIO・sstスロットル・色置換）/ contact.html（Step1ネイティブ入力化・reduced-motion・色統一）/ blog×4・privacy（トークン統一等）/ docx×4 を private/ へ

| 項目 | 方法 | 結果 |
|---|---|---|
| 実装中断からの引き継ぎ | Agent1がプロセス中断 → オーケストレーターが仕様A〜F全項目を再検査・残1件（blogフォントURL）を補完 | ✅ |
| inline JS / JSON-LD（変更全ファイル） | node --check・json.loads | ✅ 全て合格 |
| Cases/タイポ/FAQPage/OGP | 決定稿スポット照合・FAQPage 8問 inLanguage:en・sips寸法1200×630 | ✅ |
| stream-label 修正 | ヘッドレスChromeスクリーンショットで装飾表示を目視 | ✅ |
| contact キーボード完走 | **Playwright実測**: Tab→Space選択→次へ→Enter、radio矢印キー、380ms自動遷移の廃止確認、コンソールエラー0 | ✅ |
| blogドロワー | dialog/aria-modal/inert/Esc/フォーカス復帰を実測 | ✅ |
| 色負債 | grep: 28,25,23 / 217,119,6 / #92400e / #5e7f96 / #4a6a80 = 全リポジトリ0件 | ✅ |
| フォントURL統一 | 全HTML走査で distinct 1種 | ✅ |
| /en/ Cases レイアウト | ヘッドレスChrome 1280px（3カラム静的グリッド）目視 | ✅ |

未検証（開示）: Formspree実送信 / VoiceOver実機 / reduced-motion実機 / 本番LCP等の実数値（PageSpeed Insights は公開後に実URL計測を推奨）。docx は git履歴に残存（ユーザー判断待ち）。

## 英語版トップ /en/（2026-07-04）
変更: en/index.html 新規（1684行・単一ファイル） / index.html（hreflang・og:locale:alternate・ナビ/ドロワーEnglishリンク・areaServed→Worldwide・FAQフォーカスリング修正） / sitemap.xml（xhtml namespace・/en/ エントリ・双方向alternate）
※実装エージェントがプロセス中断で停止したため、検証はオーケストレーターが全項目再実施

| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS / JSON-LD | node --check・json.loads | ✅ OK（@graph: WebPage+ProfessionalService+Person、WebSite再定義なし・OfferCatalog再掲なし） |
| タグ整合 | 主要15タグの開閉カウント | ✅ 全一致 |
| head | canonical自己参照・hreflang 3行の日英バイト一致・og:locale=en_US・favicon ../相対 | ✅ grep 突合 |
| コピー忠実性 | 決定稿15フレーズの逐語スポット＋a11y-auditor の全文突合 | ✅ 差異ゼロ |
| 禁止事項 | Book a call / USD / chat.html導線 / entry-card / チェッカー | ✅ 全て不検出 |
| sitemap | xmllint | ✅ 整形式 |
| 表示 | ヘッドレスChrome（1280 / 500 / iframe実測375px）全ページスクリーンショット | ✅ 崩れなし・**375pxで docScrollW=375（横はみ出しゼロ）を実測** |
| a11yクロスレビュー | a11y-auditor（コード読解＋輝度計算） | 重大1・中4・軽微8 検出 → 重大1＋中3件（FAQリング6.6:1化・成功時フォーカス・入力境界3.2:1・フッター文字）を公開前修正。残りは ROADMAP に記録 |
| lang属性 | html lang="en"＋日本語断片8箇所の lang="ja" | ✅ 監査合格 |
| ドロワー/フォーム | dialog+inert移植・label/for/aria-describedby/role="status" | ✅ 監査合格 |

未検証（開示）: Formspree実送信（source:"en" 識別は未実測 — ROADMAP Phase 2-5）/ 実機モバイル・VoiceOver / View Transition の目視 / hreflang の Search Console 認識（公開後）。

## トップ改善 Phase 1+2（2026-07-03・未push）
変更: index.html（entry-cardリンク化・無料1行・FAQ7問・JSON-LD拡張）/ contact.html（head SEO・Tabler全廃・文言3件・フォントウェイト）/ chat.html（OGP）/ sitemap.xml（chat追記・lastmod更新）

| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | `node --check`（3ファイル） | ✅ OK |
| JSON-LD | json.loads（FAQ7問・OfferCatalog・priceRange含む） | ✅ valid |
| FAQ 7問の可視/JSON-LD 逐語一致 | seo-aeo-auditor が1文字単位で照合 | ✅ 完全一致 |
| Offer×3 と料金カード表示の一致 | 名称・minPrice・説明の突合 | ✅ 一致（月額は UnitPriceSpecification） |
| sitemap.xml | xmllint --noout・全8ページ網羅 | ✅ OK |
| entry-card 導線 | 実クリックで ?t=ai/brand/ops の3トラック事前選択 | ✅ ブラウザ実測 |
| FAQ開閉・aria-expanded | 新規3問含む排他アコーディオン | ✅ 動作 |
| contact アイコン | Tabler CDN 0件・インラインSVG 5種描画 | ✅ スクリーンショット確認 |
| フォントウェイト整合 | .btn-primary 実効500・serif600読込廃止 | ✅ getComputedStyle 実測 |
| 禁止語・営業文法 | grep「棚卸」「一切しません」「営業目的以外」 | ✅ 全て0件 |
| コンソール | index / contact 遷移 | ✅ エラー・警告ゼロ |
| クロスレビュー | seo-aeo-auditor 監査 | 重大0・中1・軽微4 → 全て修正済み（軽微3・5は据置判断） |

未検証（開示）: Formspree実送信 / Rich Results Test・validator.schema.org での機械検証（公開後に実URL推奨）/ OGP実シェア表示 / 実機モバイル。

## 相談メモ導線（2026-07-03・未push）
変更: chat.html 全面リビルド / index.html（ヒーロー・ドロワー・CTA・focus-visible・inert）/ contact.html・privacy.html・blog 4ページ（View Transition スニペットのみ）

| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | 抽出 → `node --check`（chat.html / index.html） | ✅ OK（JSON-LDも valid） |
| タグ整合 | 変更7ファイルの開閉カウント | ✅ 全一致（実装エージェント計測） |
| 外部送信ゼロ | grep（fetch/XHR/localStorage/sessionStorage）＋実機ネットワークログ | ✅ fonts.gstatic.com のみ |
| 導線一気通貫 | ヒーローチップ→`chat.html?t=ai`→4問→メモ生成→コピー/CTA | ✅ ブラウザ実測 |
| `?t=` 分岐 | ai / 不正キー（constructor 等のprototype汚染含む）/ なし | ✅ 3系統動作 |
| a11yクロスレビュー | a11y-auditor（read-only監査） | 重大2・中3・軽微7 検出 |
| 重大1: フォーカスリング 2.11:1 | outline を accent-ink（明所6.57:1）に変更、ダーク面は accent 維持 | ✅ 修正・実測 |
| 重大2: メモ生成時フォーカス喪失 | memo-title に tabindex=-1 ＋ focus() | ✅ 修正・activeElement 実測 |
| 中: main欠如 / group のaria-labelledby / Q表示のSR文 / ドロワーdialog+inert | 修正後にブラウザで属性・挙動を実測 | ✅ すべて動作 |
| コントラスト（新規要素） | WCAG式で算出（auditor） | ✅ テキスト系は全て4.5:1以上 |
| レスポンシブ | 375px/デスクトップ、横スクロールなし | ✅ スクリーンショット確認 |
| コンソール | 全遷移でエラー・警告 | ✅ ゼロ |

未検証（開示）: 実機（iOS Safari/Android）タップ・VoiceOver実機読み上げ・OS設定でのreduced-motion実挙動・実クリップボード書き込み成功経路（権限つき環境での手動確認推奨）・View Transitionのクロスフェード目視。軽微指摘の残りは ROADMAP「次の波」4に記載。

## 残タスク一括対応（2026-07-03 終盤）
- 全7ページのJSON-LD parse / タグ整合 / sitemap XML / landing JS構文: すべてOK
- Tabler参照: 全ページで0件（サイト全体からwebフォントアイコン全廃）
- ブラウザ確認: モノクロロゴのツール帯・FAQ4問・privacy.html 表示OK、コンソールエラーゼロ
- 未検証: Formspree経由の実送信（プラポリ記載内容と実フォーム項目の突合は目視のみ）、実機表示

## ブログ2記事公開（2026-07-03 後半）
- 記事2本＋OGP2枚＋一覧・sitemap・トップ更新。JSON-LD parse OK / タグ整合 OK / sitemap XML OK
- ブラウザ確認: 記事2本・一覧・トップの#s-blogを表示、コンソールエラーゼロ
- 分隊: brand-copywriter（執筆）→ 実装は主スレッド → seo-aeo-auditor（監査、指摘6件中5件を反映・1件は執筆意図により見送り）
- 未検証: 実機表示、公開URLでのOGPシェア表示（push後に確認）

## Phase 1〜OGP対応（コミット `40a34f6` 時点）

## 実行した検証
| 項目 | 方法 | 結果 |
|---|---|---|
| inline JS 構文 | 抽出 → `node --check` | ✅ OK |
| タグ整合 | div/section/button/main/svg/span/i の開閉カウント | ✅ 全一致 |
| Tabler残存参照 | grep | ✅ 0件 |
| コンソール | ローカルサーバー＋ブラウザ（デスクトップ/モバイル375px） | ✅ エラー・警告ゼロ |
| FAQ開閉 | 実クリック → maxHeight/aria-expanded/描画高さ | ✅ 動作 |
| ドロワーフォーカス | 開→close btnへ / Esc→ham復帰 | ✅ 動作 |
| スクロールスパイ | SERVICES/ABOUT で下線確認 | ✅ 動作 |
| palt | ヒーロー/CTA/SIGNS 見出しの目視 | ✅ 崩れなし |
| OGP | 1200×630 / 110KB / 書体一致 | ✅ 生成・設置 |

## 未検証（開示）
- 実機（iOS Safari / Android Chrome）での確認 — シミュレートのみ
- Lighthouse / Core Web Vitals の計測 — ツール未実行。公開URLで PageSpeed Insights 推奨
- スクリーンリーダー（VoiceOver）での通し確認 — 構造・ARIAは目視のみ
- OGPの実シェア表示 — push後に opengraph.xyz 等で実URL確認が必要
