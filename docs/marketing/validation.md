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
| 既存Support/Privacy/contact/404 | 本文・問い合わせ処理不変。2026-11-03にヘッダーナビゲーションを全ページで統一 |
| licenses | 直接依存表は不変。v1.0.0時点の参考一覧であり、1.2.0の全OSSを網羅しないことを明記 |
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

## PR #1 最終確認（2026-11-02）

開始HEAD `a52ed3887124c27d41d0aa57f29d1463d0bd14ac`、remote PRも一致、OPEN/Draft、worktree cleanを確認して開始。

- トップのOSSカードとlicensesのdescription/冒頭に、v1.0.0時点の参考一覧であり公開中1.2.0の全依存・著作権表示・完全なライセンス本文を網羅しない旨を追記。依存表そのものは更新していない。
- read-only照合: アプリrelease/1.2.0 `c5e148c4101d1aee53b88a24dba3a084e50b3939`のpackage.json/package-lock.jsonにある直接runtime依存29件と、サイト表の名前・解決バージョンはすべて一致。アプリdocs/licenses.mdは対象1.0.0表記のまま。
- 間接依存例`@expo-google-fonts/material-symbols`のlockfile licenseは`MIT AND Apache-2.0`。サイトの直接依存表だけで全配布物を説明したと扱わない。最終Archive/native依存/完全なnoticeは未監査。不足範囲の確認を別[Issue #2](https://github.com/b1011205/vecord-support/issues/2)へ記録。違反の判定や大規模依存監査は行っていない。
- 通常/safe Jekyll build、HTML9文書/内部参照164件/正規8URL、HTTP200・内部資料404・canonical・sitemap・metadata・Python構文・git diff --checkを再実行しPASS。
- トップ/記事一覧/記事2本/Support/Privacy/licensesの7ページを320/390/1440px幅で再検査（計21条件）。横overflow/画像破損なし、トップと記事のApp Store CTAあり、ブラウザerrorログ0。390px幅のトップ/一覧/記事2本を目視。遅延画像はスクロール後の読み込みを確認。
- 実機Safariは今回も検査しておらず、NOT TESTEDを維持。

最終確認用ローカルプレビュー: http://127.0.0.1:8028/vecord-support/ 。ビルド先: `/private/tmp/vecord-website-final-review`。公開/mergeは行わず、POのローカルプレビュー最終確認待ち。

## ナビゲーション統一（2026-11-03）

- 開始HEAD `0795ffd6977c46f361339cabfc5772b6fd664f67`、branch `feature/website-seo-growth`、worktree clean。
- トップは4項目、記事・Support等は3項目、404はブランドのみだった。全9ページを「整備記録のコツ → プライバシー → サポート → OSSライセンス」の4項目・同じ順番へ統一。リンク先は各ページの階層に合わせ、現在ページのaria-currentは維持。本文・CSS・問い合わせ処理は不変。
- `scripts/check-site.py`に、404を含む全HTMLでナビゲーションのラベル・順序・リンク先が一致する回帰検査を追加。
- safe Jekyll build、HTML9文書/内部参照175件/正規sitemap8URL、ローカルHTTP200・非公開資料404、Python構文検査、git diff --check: PASS。
- ブラウザで全9ページ×320/390/1440px幅（計27条件）を再読込して4項目・同順序・横overflowなしを確認。390px幅のオイル交換記事ヘッダーを目視。初回に旧ページのブラウザキャッシュが残ったため、再読込後の表示で判定。
- 実機SafariはNOT TESTEDのまま。プレビューURLは上記8028を継続使用。この検査段階では未commit/未pushでPO確認待ちだった。

## 公開承認（2026-11-03）

POがローカルプレビューの最終確認と公開を正式承認。確認済みHEADにはナビ統一が含まれないことを報告して一旦停止した後、ナビ統一のcommit/push・再検査・Draft解除・squash merge・Pages公開まで進める追加承認を受領。公開後の検査結果とmerge SHAはPR #1へ記録する。Search Console所有権確認/サイトマップ送信、SNS投稿、App Store metadata変更、アプリRepository変更は対象外。
