在 iOS 10 及以上的系统中，系统使用了新的消息通知框架 `UserNotifications`。而我们也在此基础上构建我们的功能。我们设置了 `[UNUserNotificationCenter currentNotificationCenter].delegate` 请不要重复设置该参数，避免冲突。如果您对 `UNUserNotificationCenterDelegate` 的回调关心，请实现 `TACMessagingDelegate` 协议，并实现对应的方法：

~~~
- (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler __IOS_AVAILABLE(10.0) __TVOS_AVAILABLE(10.0) __WATCHOS_AVAILABLE(3.0);
- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)(void))completionHandler __IOS_AVAILABLE(10.0) __WATCHOS_AVAILABLE(3.0) __TVOS_PROHIBITED;
~~~

这两个方式是 `UNUserNotificationCenterDelegate` 中对应的方法。

> **注意：**
> 在老版本中我们对该函数进行了重新，重新设计 API 后我们直接使用了系统的函数名称，方便您使用。请不要使用被标记为废弃的 API。
