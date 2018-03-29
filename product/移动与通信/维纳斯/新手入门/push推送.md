
1、注册账号：开发商在用户登录阶段，调用 Bind(Wns Sdk)接口，将开发商用户账号(uid)绑定到对应的终端。具体 SDK 调用请参考 [iOS 接入指南](http://panshi.isd.com/doc/product/276/iOS%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97)和 [Android 接入指南](http://panshi.isd.com/doc/product/276/Android%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97) 。
2、Push 调用：开发商服务端调用 Wns OpenApi 接口，将消息推送 给 Wns 系统。具体请参考 [Push 接入指南](http://panshi.isd.com/doc/product/276/%E6%8E%A5%E5%85%A5Push%E6%8C%87%E5%8D%97) 。
3、Push 推送：Wns 系统根据相应的规则，将消息推送到对应终端的 Wns Sdk 中。具体的回调机制请参考 [iOS 接入指南](http://panshi.isd.com/doc/product/276/iOS%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97)和 [Android 接入指南](http://panshi.isd.com/doc/product/276/Android%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97) 。
4、消息通知：Wns Sdk 将接收的消息数据，通知到 App 业务层处理。

