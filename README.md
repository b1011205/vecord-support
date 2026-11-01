# VECORD Support Site

VECORD（ヴィコード）のストア公開用サポートサイトです。

- トップ: <https://b1011205.github.io/vecord-support/>
- プライバシーポリシー: <https://b1011205.github.io/vecord-support/privacy-policy/>
- サポート: <https://b1011205.github.io/vecord-support/support/>
- OSSライセンス: <https://b1011205.github.io/vecord-support/licenses/>
- 問い合わせ: <https://b1011205.github.io/vecord-support/contact/>
- 整備記録のコツ: <https://b1011205.github.io/vecord-support/articles/>（このPRで準備、公開承認待ち）

## お問い合わせフォーム

お問い合わせフォームにはTallyを使用しています。

- フォームID: `vGvMrg`
- お問い合わせページ: `/contact/`
- Hidden fields: `source`、`app_version`、`os`、`locale`
- 通知先: VECORDサポート用Gmail（メールアドレスは公開リポジトリへ記載しない）
- 問い合わせ内容を自動的にGitHub Issueへ登録しない
- 必要な問い合わせのみ、人間が内容を確認してIssue化する
- TallyのWidget Scriptは`contact/index.html`だけで読み込む

Tallyフォーム以外にアクセス解析や広告は導入していません。

## 公開方法

GitHub Pagesの公開元は`main`ブランチの`/(root)`です。独自workflowはなく、GitHub管理のlegacy Pages/Jekyll buildが公開します。作業branchへのpush・Draft PRだけでは公開されません。公開には別途プロダクトオーナーの確認が必要です。

HTML/CSSはビルド前から完成した静的ファイルです。`_config.yml`は`docs/`（SNS草稿・計測資料）と`scripts/`等を生成物から除外します。`.nojekyll`は追加しないでください。除外を迂回して内部原稿を公開するおそれがあります。依存パッケージや追跡SDKはサイトに追加していません。

## ローカル確認

本番と同じサブパス・配信対象で確認します。Jekyll 3.10が使える環境で、出力先をリポジトリ外に指定してください。今回の検証では一時領域にJekyllをインストールしました。Ruby 4ではbase64/bigdecimalが別gemとして必要です。

```sh
jekyll build --source . --destination /private/tmp/vecord-website-build
python3 scripts/check-site.py /private/tmp/vecord-website-build
python3 scripts/preview.py --directory /private/tmp/vecord-website-build --port 8027
```

`http://127.0.0.1:8027/vecord-support/`で確認します。別ターミナルでHTTP検査:

```sh
python3 scripts/check-site.py /private/tmp/vecord-website-build --http http://127.0.0.1:8027
```

ソース直下をそのままサーバー配信すると`docs/`の除外を確認できません。公開検証には使わないでください。検証スクリプトは内部リンク・HTML構造・canonical・metadata・sitemap・非公開資料の除外を確認します。第三者サイトへのフォーム送信は行いません。

## 集客準備資料（公開対象外）

- `docs/marketing/seo-audit.md`: 現状監査・公開前確認
- `docs/marketing/search-console-setup.md`: 所有者が行う操作
- `docs/marketing/social-posts.md`: 未投稿SNS原稿3案
- `docs/marketing/measurement.md` / `kpi-tracking.csv`: 28日計測
- `docs/marketing/image-sources.md`: 公開済み画像の出典
- `docs/marketing/validation.md`: ローカル検証結果

関連: アプリrepoのIssue #15、調査Draft PR #19。未公開アイコンPR #20を現行機能として扱いません。

## 方針

- 静的HTMLとCSSで構成し、お問い合わせページだけでTally公式の外部JavaScriptを使用する
- Cookie同意バナー、アクセス解析、広告を使用しない
- 公開中VECORD 1.2.0の実装済み機能と制約だけを記載する（既存OSS一覧の更新は別作業）
- OSS一覧はVECORD本体の`docs/licenses.md`と`package-lock.json`を根拠に更新する
