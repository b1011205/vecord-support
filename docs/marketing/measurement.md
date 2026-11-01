# 公開後28日の効果測定

作成: 2026-11-02。POの公開承認後をD1とする。開始/終了日は未定。Draft PR作成日を公開日にはしない。

| 系統 | 指標 | 現状 |
| --- | --- | --- |
| Search Console | Google検索表示、クリック、CTR、平均掲載順位、クエリ、流入ページ | 未取得、権限/登録状況未確認 |
| App Store Connect | Impressions、Product Page Views、First Time Downloads、Search、Web Referrer、App Referrer | 今回未取得。PO共有28日値41/15/2 |
| 使用状況 | Active Devices等 | 共有値0。データ共有同意等の制限があるので実利用者0と断定しない |
| Web訪問/CTA | 訪問数、App Storeリンククリック | 今回計測基盤なし、取得できない |

Google検索クリックは全訪問数でもApp Storeリンククリックでもない。Google表示とApp Store Impressionsを合算しない。Apple CVRはAppleの指標を記録し、15/41や2/15で代用しない。

## 止まっている段階を分ける

1. 公開: 各予定URLがHTTP200か、画像/サブパスが正しいか。
2. クロール: URL検査の最終クロール日時と失敗理由。
3. 登録: インデックス状態・正規URL・除外理由。公開だけで登録済みにしない。
4. 検索表示: 0と未取得を分離。クエリ/ページ単位で28日記録。
5. 検索クリック: 表示があるのにクリックが少なければtitle/descriptionと意図を見直す。
6. App Store流入/初回DL: 同期間のASCを確認。個人別追跡や因果関係の断定はしない。

## 実在するCampaign Linkが使える場合のみ

POがASCで実際に発行した完全URLを使う。媒体管理名の候補はwebsite-home、article-oil、article-history、social-a/b/c。これは今回pt/ctとして発行していない。台帳は「媒体/掲載箇所/実URL（未取得）/発行日/公開日/観測期間/非表示理由」。

トップとFooterが同じURLなら二つのクリックを区別できない。記事やSNSごとに本物のCampaign Linkがあっても、閾値・集計仕様で少数値が表示されない場合がある。Campaign結果はクリックカウンターではない。Web Referrerも同じホスト配下の記事を必ず識別できるわけではない。

本PRのCTAは素のApp Store URL。外部リダイレクト、GA、追跡SDKを追加しない。

## 手入力シート

[kpi-tracking.csv](kpi-tracking.csv)のW1〜W4は重複しない7日、D28は28日分を画面から再取得。CTR/平均順位/CVR/uniqueを週の単純平均や合計で作らない。地域・検索タイプ・フィルタ・報告タイムゾーン・取得日を控える。未取得/非表示を0にしない。データ反映遅延にも注意。

公開前28日の比較値も権限取得後に収集。SEOは遅れて反映される場合があるので、D28にDL増がなくてもクロール/登録/表示/クリックのどこで止まるかを見て次の28日を判断する。

仮目標はASC Impressions100〜200、First Time Downloads5以上。市場平均でも予測でも達成保証でもない。Google側は基準値未取得なので数値目標を捏造せず、まず取得・登録状態を記録する。

参照（2026-11-02）:

- https://support.google.com/webmasters/answer/7576553?hl=ja
- https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links/
- https://developer.apple.com/help/app-store-connect-analytics/reference/metrics-definitions/
