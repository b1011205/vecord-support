# VECORD Support Site

VECORD（ヴィコード）のストア公開用サポートサイトです。

- トップ: <https://b1011205.github.io/vecord-support/>
- プライバシーポリシー: <https://b1011205.github.io/vecord-support/privacy-policy/>
- サポート: <https://b1011205.github.io/vecord-support/support/>
- OSSライセンス: <https://b1011205.github.io/vecord-support/licenses/>
- 問い合わせ: <https://b1011205.github.io/vecord-support/contact/>

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

GitHubリポジトリのSettings → Pagesで、`main`ブランチの`/(root)`を公開元に設定します。ビルド工程や外部依存はありません。

## ローカル確認

リポジトリ直下で次を実行し、`http://localhost:8000/`を開きます。

```sh
python3 -m http.server 8000
```

## 方針

- 静的HTMLとCSSで構成し、お問い合わせページだけでTally公式の外部JavaScriptを使用する
- Cookie同意バナー、アクセス解析、広告を使用しない
- VECORD v1.0.0で実装済みの機能と制約だけを記載する
- OSS一覧はVECORD本体の`docs/licenses.md`と`package-lock.json`を根拠に更新する
