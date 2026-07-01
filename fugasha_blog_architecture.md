# 風雅舎 ブログ URL構造・カテゴリ設計

策定日: 2026-07-01 / 対象: 今後のブログ実装全般

---

## 1. URL構造

**フラット構造・末尾スラッシュ形式**を採用します。

```
/blog/                          ← 記事一覧ページ
/blog/{スラッグ}/                ← 各記事（index.html）
/blog/category/{カテゴリ}/       ← カテゴリ別一覧（記事が増えてから追加）
```

例:
```
https://aimeeta.github.io/fugasha_ai/blog/ai-donyu-hajimekata/
```

**なぜフラットにするか**
- カテゴリをURLに含めない（`/blog/ai/slug/` のようにしない）ことで、将来の再分類やカテゴリ統廃合が起きてもURLが変わらず、被リンク・検索順位を失わない
- スラッグは日付・連番を含めない（`/blog/2026-07-slug/` のようにしない）。更新性の高い記事でも同じURLを保てる
- GitHub Pagesのプリティurl慣習に合わせ、`{slug}/index.html` 形式でディレクトリ化（末尾スラッシュでアクセス可能に）

**スラッグ命名規則**
- 英数字・ハイフンのみ、日本語は使わない（例: `ai-donyu-hajimekata`、`security-basic-sme`）
- 3〜5語程度、検索意図が読み取れる具体性を持たせる

---

## 2. カテゴリ設計

既存の4サービス軸と、差別化ポイント（セキュリティ執筆実績）を反映した**4カテゴリ**構成:

| カテゴリID | 表示名 | 想定テーマ |
| --- | --- | --- |
| `ai-dx` | AI導入・業務効率化 | AI活用の始め方、業務改善事例、ツール比較 |
| `security` | セキュリティ | 中小企業向けの実践的なセキュリティ知識（差別化の核） |
| `design-brand` | デザイン・ブランディング | LP・資料・ブランドビジュアルの考え方 |
| `work-style` | 経営・働き方 | タグライン「無駄をなくして、熱中を取り戻す」に沿った経営者向けの視点 |

**運用ルール**
- 1記事1カテゴリを基本とする（複数タグは別途 `tags` フィールドで自由に付与可）
- カテゴリはURLに出さず、記事のメタデータ（JSON-LDの `articleSection`）で管理
- カテゴリ一覧ページ（`/blog/category/{id}/`）は記事が各カテゴリ3本以上たまってから着手（今は不要）

---

## 3. ファイル構成（実装時）

```
/blog/index.html                          記事一覧
/blog/ai-donyu-hajimekata/index.html      記事1
/blog/security-basic-sme/index.html       記事2
...
```

- 単一ファイル構成の踏襲: 各記事も `index.html` 内にCSS/JSを閉じ込める現行方針を維持
- 記事本文はJSでレンダリングせず、**初期HTMLに直接書く**（ClaudeBot等はJSレンダリングしないため — 前回セッションのGEO方針を継続）

---

## 4. 構造化データ テンプレート

### 4-1. Article / BlogPosting（各記事の`<head>`に追加）

既存の `@graph` パターンを踏襲し、記事ごとに新しいJSON-LDブロックとして追加します。

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "https://aimeeta.github.io/fugasha_ai/blog/{slug}/#article",
      "headline": "記事タイトル（32文字目安）",
      "description": "記事の要約（120文字目安、冒頭40〜60語の結論と揃える）",
      "image": "https://aimeeta.github.io/fugasha_ai/blog/{slug}/ogp.jpg",
      "datePublished": "2026-MM-DD",
      "dateModified": "2026-MM-DD",
      "articleSection": "AI導入・業務効率化",
      "inLanguage": "ja",
      "author": { "@id": "https://aimeeta.github.io/fugasha_ai/#person" },
      "publisher": { "@id": "https://aimeeta.github.io/fugasha_ai/#organization" },
      "mainEntityOfPage": "https://aimeeta.github.io/fugasha_ai/blog/{slug}/"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://aimeeta.github.io/fugasha_ai/" },
        { "@type": "ListItem", "position": 2, "name": "ブログ", "item": "https://aimeeta.github.io/fugasha_ai/blog/" },
        { "@type": "ListItem", "position": 3, "name": "記事タイトル" }
      ]
    }
  ]
}
</script>
```

`author` / `publisher` は既存の `index.html` の `#person` / `#organization` エンティティをそのまま参照する（`@id` の使い回し）ため、二重定義せずに済みます。

### 4-2. FAQPage（記事内にFAQがある場合のみ）

`index.html` に今回追加したFAQPageと同じ形式。記事末尾に「よくある質問」を置く場合のみ使用し、無理に全記事へ入れない（Google側は無関係な箇所へのFAQPage濫用を評価しない）。

---

## 5. 運用フロー（次回ブログ実装時）

1. カテゴリ4本のうち、どれから書き始めるか決める（セキュリティ執筆実績があるので `security` カテゴリが差別化上おすすめ）
2. `/blog/index.html`（一覧）の雛形を作成
3. 1本目の記事を `/blog/{slug}/index.html` として作成し、上記テンプレートでJSON-LDを追加
4. `sitemap.xml` に `<url>` ノードを追記（前回セッションで用意したコメントテンプレを使用）
5. 3本たまったらカテゴリ一覧ページの実装を検討

---

## 6. 未決事項（次回相談したいこと）

- 更新頻度（週1本？月2本？）— `sitemap.xml` の自動生成移行タイミングに影響
- 記事一覧ページのデザイン（カード形式か、リスト形式か）
- OGP画像をどう生成するか（毎回手動 or テンプレートベースで自動生成）
