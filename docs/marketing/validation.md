# ローカル検証記録

2026-11-02。専用branch `feature/website-seo-growth`。公開サイト・アプリrepoへの変更なし。

| 検査 | 結果 |
| --- | --- |
| Jekyll 3.10 build（safe modeも実行） | PASS、生成先は/private/tmp/vecord-website-build |
| HTML構造 | 9文書のタグ対応、lang=ja、H1各1、重複IDなし PASS |
| 内部リンク/画像/CSS参照 | 164件の参照先とページ内anchor PASS |
| 公開予定8URL | ローカルHTTP200 PASS |
| canonical | 8URLともhttps://b1011205.github.io/vecord-support/基準 PASS |
| title/description | 公開予定8ページに存在し重複なし PASS |
| OGP/X Card | トップ/記事一覧/2記事に必須値・実在画像・正しいURL PASS |
| sitemap.xml | 正規8URL、実在index.html、404/内部資料を含まない PASS |
| docs/marketing・scripts・README | Jekyll生成物に存在せず、ローカルHTTP404 PASS |
| 404 | 深い架空URLで専用404本文・HTTP404・noindex PASS |
| ブラウザ表示 | トップ/記事一覧/2記事/Support/Privacy/licensesを320・390・1440px幅で確認、bodyの横overflowなし |
| 画像 | 公開1.2.0の3枚を目視、画像欠落なし。下部画像はlazy。原本・未公開UIは変更/使用していない |
| CSS | ブラウザCSSOMで読み込み確認、モバイル折り返し・日本語フォント・余白を画面確認。App Store CTAは白文字の可読性のため既存brand-blueの単色 |
| JavaScript | トップ/記事一覧/2記事に追加scriptなし。主要7ページのブラウザerrorログ0件 |
| 既存Support/Privacy/contact/licenses/404 | origin/mainとの差分0、本文・問い合わせ処理不変 |
| App Storeリンク | 全新規導線のhrefが素の公式URLと一致。公開Lookupの返却Version1.2.0を確認 |
| git diff --check | PASS |

## 再実行

READMEのJekyll build→scripts/check-site.py→scripts/preview.py→HTTP検査を使用。サイトの新規npm依存・JS・追跡SDKはなし。ローカル検証環境だけにJekyll3.10/base64/bigdecimal等を一時インストールした。Ruby4環境では不足gemのLoadErrorが一度発生し、一時環境へ補って解消。Python構文検査のキャッシュ権限制限は、一時キャッシュ先で再実行し解消した。

## 未検証と公開前確認

- 実iPhone Safari、Androidブラウザ、VoiceOver、SNSの実際のリンクカード表示はNOT TESTED。幅を変えたブラウザ検証とは区別する。
- Search Consoleの登録/所有権/インデックス/検索指標は未取得。Googleへのsitemap送信/URL申請は未実施。
- Campaign LinkとCTAクリック計測は未導入。値を取得できたと扱わない。
- Tallyの送信と問い合わせ先メールは検証しない。従来の外部iframe/JSを変更しない。
- 公開後のHTTP/OGPキャッシュ/Googleクロールは未検証。PO公開判断後に確認する。
- Github Pagesはmainルート公開。公開前にexcludeを削除したり.nojekyllを追加しないこと。
