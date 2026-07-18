# VECORD Support Site

VECORD（ヴィコード）のストア公開用サポートサイトです。

- トップ: <https://b1011205.github.io/vecord-support/>
- プライバシーポリシー: <https://b1011205.github.io/vecord-support/privacy-policy/>
- サポート: <https://b1011205.github.io/vecord-support/support/>
- OSSライセンス: <https://b1011205.github.io/vecord-support/licenses/>
- 問い合わせ: <https://github.com/b1011205/vecord-support/issues>

## 公開方法

GitHubリポジトリのSettings → Pagesで、`main`ブランチの`/(root)`を公開元に設定します。ビルド工程や外部依存はありません。

## ローカル確認

リポジトリ直下で次を実行し、`http://localhost:8000/`を開きます。

```sh
python3 -m http.server 8000
```

## 方針

- HTMLとCSSだけで構成する
- Cookie、アクセス解析、広告、外部JavaScriptを使用しない
- VECORD v1.0.0で実装済みの機能と制約だけを記載する
- OSS一覧はVECORD本体の`docs/licenses.md`と`package-lock.json`を根拠に更新する
