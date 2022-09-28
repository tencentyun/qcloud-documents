直播 SDK 预计在2022年09月19日发布移动端10.7版本，在该版本中接口 `startPlay` 的名称将做出变更。

`startPlay` 接口在配置 SDK 播放功能时使用，代表开始播放。具体变更如下：

- 直播播放新版接口 `V2TXLivePlayer` 的开始播放接口名由 `startPlay` 变更为 `startLivePlay`，详情参见 [API-iOS-拉流](https://cloud.tencent.com/document/product/454/56044#startliveplay)、[API-Android-拉流](https://cloud.tencent.com/document/product/454/56045#startliveplay)、[API-Flutter-拉流](https://cloud.tencent.com/document/product/454/71600#startliveplay)。
- 直播播放旧版接口 `TXLivePlayer` 的开始播放接口名由 `startPlay` 变更为 `startLivePlay`，详情参见 [API-iOS-拉流](https://cloud.tencent.com/document/product/454/34762#startliveplay)、[API-Android-拉流](https://cloud.tencent.com/document/product/454/34775#startliveplay)。

>?
>- 若您在移动端10.7以下版本的 SDK 中使用该接口，将不受本次变更影响。
>- 若您在移动端10.7及其更高版本的 SDK 中使用该接口，则需关注此次变更。

若您有任何疑问，欢迎随时 [联系我们](https://cloud.tencent.com/document/product/1449/56948)。衷心感谢各位用户对腾讯视立方产品的信赖与支持！
2022-09-19
腾讯云

