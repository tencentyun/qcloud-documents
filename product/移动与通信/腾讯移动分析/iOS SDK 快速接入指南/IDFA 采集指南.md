### 集成步骤
第一步，[下载标准 SDK](http://mta.qq.com/mta/ctr_index/download)；
第二步，解压下载的 SDK 包，将 libidfa.a和AdSupport.framework 链接到工程中即可，如下图：
![](//mc.qcloudimg.com/static/img/b8a7a99fa2186b796a2dce35f3c3cf4b/image.png)
### 注意事项

MTA SDK 支持采集 iOS 用户的 IDFA（identifier for advertising）信息，IDFA 是更通用、更精准的一种标记用户的方式，广泛应用于精准的广告效果统计、 App 换量、数据互换合作等跨应用数据交叉分析场景。
使用 IDFA 原则上需要集成任意一家的广告 SDK，如果您期望采集 IDFA 但是并未使用任何广告，可以采用以下方法通过 Appstore 审核： 
![](//mc.qcloudimg.com/static/img/a54bb121e7b4e66ca8aaf1c48f260f6e/image.png)
1. serve advertisements within the app 应用内广告服务，适用于应用内集成了广告的场景，如果您的情况符合，需要勾选此选项。
2. Attribute this app installation to a previously served advertisement 用于跟踪和统计广告带来的安装量，需要勾选。
3. Attribute an action taken within this app to a previously served advertisement 用于跟踪和统计广告安装后带来的用户行为，需要勾选。
4. Limit Ad Tracking setting in iOS 此项属于确认项，需要勾选。

如果您仍因为采集 IDFA 被 Appstore 审核拒绝，建议您集成任意一家广告或选用 MTA 普通版，如需同时统计 App 内的 h5 页面数据，请根据 [hybird app ios 使用说明](https://cloud.tencent.com/document/product/549/12900)进行集成。