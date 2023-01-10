播放器 SDK 预计在2022年9月19日发布移动端10.7版本，在该版本中接口 `startPlay` 的名称将做出变更。

`startPlay` 接口在配置 SDK 播放功能时使用，代表开始播放。具体变更如下：

- 点播播放接口 `TXVodPlayer` 的开始播放接口名由 `startPlay` 变更为 `startVodPlay`，详情参见 [API-iOS-点播播放](https://cloud.tencent.com/document/product/881/67109#.E6.92.AD.E6.94.BE.E5.9F.BA.E7.A1.80.E6.8E.A5.E5.8F.A3)，[API-Android-点播播放](https://cloud.tencent.com/document/product/881/67113#.E6.92.AD.E6.94.BE.E5.9F.BA.E7.A1.80.E6.8E.A5.E5.8F.A3)，[API-Flutter-点播播放](https://cloud.tencent.com/document/product/881/81255)。
- 直播播放接口 `TXLivePlayer` 的开始播放接口名由 `startPlay` 变更为 `startLivePlay`*，*详情参见 [API-iOS-直播播放](https://cloud.tencent.com/document/product/881/67108#.E6.92.AD.E6.94.BE.E5.9F.BA.E7.A1.80.E6.8E.A5.E5.8F.A3)，[API-Android-直播播放](https://cloud.tencent.com/document/product/881/67111#.E6.92.AD.E6.94.BE.E5.9F.BA.E7.A1.80.E6.8E.A5.E5.8F.A3)。

>?
>- 若您在移动端10.7以下版本的 SDK 中使用该接口，将不受本次变更影响。
>- 若您在移动端10.7及其更高版本的 SDK 中使用该接口，则需关注此次变更。

若您有任何疑问，欢迎随时 [联系我们](https://cloud.tencent.com/document/product/1449/56948)。衷心感谢各位用户对腾讯视立方产品的信赖与支持！

2022-09-19

腾讯云
