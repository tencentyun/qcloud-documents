

1. 注册账号：开发商在用户登录阶段，调用 Bind(Wns Sdk)接口，将开发商用户账号(uid)绑定到对应的终端。具体 SDK 调用请参考 [iOS 接入指南](https://cloud.tencent.com/document/product/276/3207) 和 [Android 接入指南](https://cloud.tencent.com/document/product/276/3208) 。
2. Push 调用：开发商服务端调用 Wns OpenApi 接口，将消息推送 给 Wns 系统。具体请参考 [Push 接入指南](https://cloud.tencent.com/document/product/276/3212) 。
3. Push 推送：Wns 系统根据相应规则，将消息推送到对应终端的 Wns SDK 中。具体回调机制请参考 [iOS 接入指南](https://cloud.tencent.com/document/product/276/3207) 和 [Android 接入指南](https://cloud.tencent.com/document/product/276/3208) 。
4. 消息通知：Wns Sdk 将接收的消息数据，通知到 App 业务层处理。
