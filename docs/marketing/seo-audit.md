# SEO監査と公開前確認

確認日: 2026-11-02（JST）。対象: b1011205/vecord-support。開始mainとfetch後origin/mainは`b51386f8b51d201c699275148455ac03cd27709b`、clean。同名branch/worktreeなしを確認し、`feature/website-seo-growth`を専用worktreeへ作成した。アプリrepoはread-only、PR #19のDraft文書を参照。PR #19/#20はmergeしない。

## 公開安全性

GitHub REST `repos/b1011205/vecord-support/pages`で`build_type=legacy`、source=`main`/`/`、HTTPS enforced、custom404を確認。ActionsはGitHub管理の`dynamic/pages/pages-build-deployment`のみ。repo内に独自workflow、外部ホスティング設定、独自のPR deploy設定はない。作業branchへのpushとDraft PR作成はmainを更新しない。

静的HTML/CSS中心。独自Jekyllテンプレート/プラグイン/既存_config.yml/.nojekyllはなし。Pagesのlegacy公開はJekyllを通るので、今回_config.ymlを追加しdocs/scripts/README等をexcludeする。.nojekyllは置かない（置くと除外設定を迂回し内部原稿を配信する危険がある）。今回ローカルJekyll 3.10で生成・除外検査する。問い合わせのTally JSは既存contactページだけのまま。

## before → after

| 項目 | 公開前の観測 | このPRで準備した変更 |
| --- | --- | --- |
| トップHTTP/HTTPS | HTTPS GET 200、X-Robots-Tagなし | URL維持 |
| host /robots.txt | 404 | Project下robots.txtは追加しない |
| sitemap.xml | Project下404 | 公開予定8URLのXMLを追加 |
| meta robots | 通常ページはnoindexなし、404のみnoindex | 維持 |
| title/description | 既存各ページにあり、トップはブランド/サポート中心 | トップで整備記録・予定・iPhoneを明示、新3ページは固有値 |
| canonical | 既存5主要ページは正しいHTTPS Project URL | 記事一覧・2記事にも追加 |
| OGP / X Card | なし | トップ/記事一覧/2記事に追加。画像は既存app-icon、summaryカード |
| 見出し | トップH1はVECORDのみ | H1で用途、機能/使い方/記事をH2に整理 |
| App Store導線 | トップに直接リンクなし | Hero/全体Footer/記事末尾に素の日本App Store URL |
| 画像 | 既存brand画像、空altは装飾 | 公開1.2.0の3スクリーンショットをローカル配信、内容alt、サイズ指定、下部lazy |
| モバイル | レスポンシブCSSあり | 既存theme維持、可変グリッド/折り返し、ブラウザ検証 |
| 404 | 専用noindexページ、ProjectパスのCSS/戻り先 | 変更なし。深いURLでも正しいCSS |
| Support/Privacy/contact/licenses | 既存静的ページ | 本文・URL・問い合わせ処理を変更しない |
| 内部資料 | 未追加 | docs/marketingは生成物から完全除外（noindexで隠す方式ではない） |

サイト全体がインデックス済みとは確認できない。[Googleのsite:参考検索](https://www.google.com/search?q=site%3Ab1011205.github.io%2Fvecord-support%2F)は一致なしと表示。GoogleのURL検査は未実施なので未登録とは断定しない。Search Consoleはログイン前の紹介ページに到達し、プロパティ/所有権/エラー/送信状況/検索指標は未取得。所有権tokenも未取得。GSC導入は[手順書](search-console-setup.md)でPO操作待ち。

## コンテンツと出典

予定URL:
- `/vecord-support/articles/`
- `/vecord-support/articles/oil-change-record/` — オイル交換 記録/履歴/管理
- `/vecord-support/articles/car-maintenance-record/` — 車 整備記録/整備履歴 アプリ/メンテナンス記録

記事Aは記録項目・紙/メモ/アプリ・メーカーに確認する次回予定、記事Bは散在する履歴の整理・分類・費用二重計上回避・予定と実績・写真/連絡先/バックアップを扱う。具体例は架空と明記。特定の交換周期や全車に合うオイル規格を断言しない。VECORDを法定帳票の代替、整備診断、給油/燃費、写真付き整備明細OCRとして紹介しない。

参照（2026-11-02）:
- https://toyota.jp/faq/show/194.html
- https://toyota.jp/after_service/tenken/driver/maintenance/engine_oil/
- https://www.mlit.go.jp/jidosha/jidosha/tenkenseibi/tenken/t1/t1-2/
- https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=ja
- https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec?hl=ja
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=ja
- https://apps.apple.com/jp/app/vecord/id6793060453

## 公開前にPOが行うこと

- [ ] ローカルのトップと記事2本の文言・実画面整合を確認
- [ ] 写真/JSON・1台・iPhone・予定日通知の表現確認
- [ ] 検証結果とdocs除外を確認してから、別途公開判断（このPRはDraft）
- [ ] 公開後にURL200/OGP/画像/404を確認し、その後Google所有権検証とsitemap送信を判断
- [ ] SNSは公開URLが有効になってから原稿を選ぶ。本人の開発動機は本人確認後
- [ ] 計測開始日を記録し、28日単位で比較

このPR作成は公開承認、SNS投稿承認、Search Console検証承認ではない。
