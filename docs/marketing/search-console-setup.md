# Search Console準備

確認日: 2026-11-02。https://search.google.com/search-console/ はログイン前のabout画面。プロパティ登録・所有権・インデックス・クロールエラー・検索クエリ・sitemap送信履歴は未確認。「未設定」と断定しない。

## POが行う操作

1. Googleアカウントでログインし、既存プロパティと権限を確認する。
2. 必要ならURLプレフィックス `https://b1011205.github.io/vecord-support/` を登録。github.io全体を対象にするドメインプロパティは選ばない。
3. HTMLタグ方式でGoogleが発行する実際のverification tokenを取得。意図したGoogleアカウントへ所有権を付与することをPOが確認する。今回は架空tokenやダミー確認ファイルを置いていない。
4. 別途承認された変更で、トップindex.htmlのheadへ実際の`google-site-verification`タグを正確に追加して公開。既存所有者のtokenを上書きしない。
5. 公開HTMLで確認後、POがSearch Consoleの「確認」を実行する。確認後もtokenは残す。
6. HTMLファイル方式なら、Googleが指定する正確な名前・本文・URLへ配置する。Project Siteのサブパスと要求URLが一致するか確認。ホスト直下を要求される場合に`/vecord-support/`の配置で代用しない。合わなければmeta方式を使う。
7. 本PRの公開後に`sitemap.xml`のHTTP200とXMLを確認。POがサイトマップ `https://b1011205.github.io/vecord-support/sitemap.xml` を送信する。Draft中は新記事URLの送信・登録申請を行わない。
8. トップ・記事一覧・記事2本をURL検査し、登録/最終クロール/正規URL/除外理由を控える。必要な登録リクエストはPO判断。クロールや登録、順位は保証されない。

## robotsと参考検索

robots.txtはホスト直下`https://b1011205.github.io/robots.txt`が対象。公開応答は404。`/vecord-support/robots.txt`だけで制御できたとは扱わず、今回は配置しない。robotsの404自体はクロール禁止ではない。

トップと既存主要ページにnoindexはなく、404.htmlのnoindexは維持。Googleで`site:b1011205.github.io/vecord-support/`を検索し、「一致する情報は見つかりませんでした」と表示された。検索サービス経由でも該当なし。ただしこれだけではGoogleのインデックス登録状態の証明にはならず、URL検査は未実施。

Googleログイン、所有権付与/検証、サイトマップ送信、インデックス登録申請は今回は行っていない。

参照（2026-11-02）:

- https://support.google.com/webmasters/answer/9008080?hl=ja
- https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=ja
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=ja
