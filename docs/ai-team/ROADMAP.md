# ROADMAP — 優先順位つき残タスク

最終更新: 2026-07-03

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
- WebGL/Three.js 背景、ページ遷移演出、GSAP導入

## 運用メモ
- push＝本番公開。ユーザーの明示指示があるまでpushしない
- 実績数字（144本・50社以上）の裏付け一覧を別途保管する
