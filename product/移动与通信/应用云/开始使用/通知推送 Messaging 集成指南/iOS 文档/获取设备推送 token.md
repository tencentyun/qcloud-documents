# 获取设备推送 token


注册成功后，会返回设备 token，token 用于标识设备唯一性，同时也是 Messaging 服务维持与后台连接的唯一身份标识(APNS的token)。在 iOS SDK 中，您可以在接入 Messaging 服务时，通过重写 `AppDelegate` `application:didReceiveRemoteNotification` 方法来获取 token。

Objective-C 代码示例：
~~~
- (void) application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo
{
    [TACMessagingService defaultService].token ;
}
~~~

Swift 代码示例：
~~~
func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any]) {
        TACMessagingService.default().token;
}
~~~

> 请注意请一定要在该函数中调用绑定代码，如果您没有注册成功 APNS 则不会存在变量`[TACMessagingService defaultService].token`


> 接入 Messaging 服务请参考 [这里](https://cloud.tencent.com/document/product/666/14350)
