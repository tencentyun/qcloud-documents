## IM React Native SDK 0.1.9 @2022.12.05

- 新增：多媒体消息默认不再返回 URL，需通过`getMessageOnlineUrl`获取。
- 新增：媒体消息不默认不再返回 localurl，需通过 downloadMessage 下载消息成功后才会返回。
- 新增：在`advanceMessageListener`中增加`onMessageDownloadProgressCallback`，当多媒体消息下载进度更新时会触发。
- 新增：消息扩展功能，详情可见消息相关-消息扩展。
- 改进：升级底层 Native SDK 至 6.9.3557 版本。

>?本次更新对于多媒体消息及文件消息改动较大，请根据前三条，修改您现有获取并渲染此类消息的逻辑，否则无法展示。如在修改过程中有任何疑问，欢迎随时 [联系我们](https://cloud.tencent.com/online-service?from=doc_269) 咨询。

## IM React Native SDK 0.1.0 @2022.07.14
- 正式开放用户使用
>? 我们首次推出 IM React Native，将继续更新后续版本。


