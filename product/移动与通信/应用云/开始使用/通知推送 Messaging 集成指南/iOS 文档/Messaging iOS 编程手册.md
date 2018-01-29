# Messageing 编程手册


## 服务启动与停止

当您集成了 Messaging 服务之后，系统将会在程序启动的时候自动启动服务。

如果您不希望在启动的时候默认启动 Messaging 服务，您可以在配置中设置关掉 (例如在AppDelegate中加入如下代码)：

~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
    options.messagingOptions.autoStart = NO;
~~~

### 手动开启服务

~~~
    [[TACMessagingService defaultService] startReceiveNotifications];
~~~

### 手动关闭服务

~~~
    [[TACMessagingService defaultService] stopReceiveNotifications];
~~~

如果您希望在特定的时候关闭服务，

## 监听 Messaging 服务回调


设置 delegate 为您已经实现 TACMessagingDelegate 的类可以监听 Messaging 服务的回调：

~~~
    [TACMessagingService defaultService].delegate = self;
~~~

~~~
@protocol TACMessagingDelegate <NSObject>
@optional


/**
 @brief 监控推送服务地启动情况
 
 @param isSuccess 推送是否启动成功
 @param error 推送启动错误的信息
 */
- (void) messagingDidFinishStart:(BOOL)isSuccess error:(nullable NSError *)error;

/**
 @brief 监控服务的终止情况
 
 @param isSuccess 推送是否终止
 @param error 推动终止错误的信息
 */
- (void) messagingDidFinishStop:(BOOL)isSuccess error:(nullable NSError *)error;


/**
 @brief 监控服务上报推送消息的情况
 
 @param isSuccess 上报是否成功
 @param error 上报失败的信息
 */
- (void) messagingDidReportNotification:(BOOL)isSuccess error:(nullable NSError *)error;


#pragma mark iOS10 以上有效

@optional

#if __IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_10_0
/**
 处理iOS 10 UNUserNotification.framework的对应的方法
 
 @param center [UNUserNotificationCenter currentNotificationCenter]
 @param notification 通知对象
 @param completionHandler 回调对象，必须调用
 */
- (void) messagingUserNotificationCenter:(nonnull UNUserNotificationCenter *)center willPresentNotification:(nullable UNNotification *)notification withCompletionHandler:(nonnull void (^)(UNNotificationPresentationOptions options))completionHandler __IOS_AVAILABLE(10.0);


/**
 处理iOS 10 UNUserNotification.framework的对应的方法
 
 @param center [UNUserNotificationCenter currentNotificationCenter]
 @param response 用户对通知消息的响应对象
 @param completionHandler 回调对象，必须调用
 */
- (void)messagingUserNotificationCenter:(nonnull UNUserNotificationCenter *)center didReceiveNotificationResponse:(nullable UNNotificationResponse *)response withCompletionHandler:(nonnull void (^)(void))completionHandler __IOS_AVAILABLE(10.0);

#endif
@end
~~~

## 管理程序 SpringBoard 上的角标


### 获取程序当前角标数量

~~~
NSInteger count =[[TACMessagingService defaultService] applicationBadgeNumber];
~~~

###  设置程序当前角标数量

~~~
NSInteger badgeNumber =  @(2);
[[TACMessagingService defaultService] setApplicationBadgeNumber:badgeNumber];
~~~




## 其他功能

其他功能请参考 TACMessagingService.h 中的定义。
