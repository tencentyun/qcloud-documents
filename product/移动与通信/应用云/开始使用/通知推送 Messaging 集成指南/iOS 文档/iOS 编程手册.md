



## 监听 Messaging 服务回调


设置 delegate 为您已经实现 TACMessagingDelegate 的类可以监听 Messaging 服务的回调, 包括监听推送服务启动、上报消息的情况等：

Objective-C 代码示例：
~~~
[TACMessagingService defaultService].delegate = self;
~~~

Swift 代码示例：
~~~
TACMessagingService.default().delegate = self as! TACMessagingDelegate
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

## 接受与处理远程消息
如果仅仅是推送消息而不需要进行额外处理的话，那么其实不必进行消息的处理，如果通知中带有了 payload，或者需要在通知里进行应用交互的话，可以通过接受消息的回调里去完成。当客户端收到推送消息时，分为两种情况：
- APP 正在当前前台运行    

  当 APP 在前台运行时，系统在收到推送消息时会自动静音，并且直接将通知的数据传递到 APP 中。如果需要获取通知里附带数据(payload)，那么可以在接受通知回调里实现(payload 包装在 UserInfo 内)：
  ~~~
  - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler;
  ~~~

- APP 并没有开启或者在后台运行    

  在 iOS 10 以上的操作系统中，用户可以在通知上面点击一些自定义的通知时间，例如取消按钮等，从而可以在不进入 APP 的情况下进行一下快捷操作。

  对于 iOS 8.0 - 10.0的系统，可以在该回调中实现通知栏按钮点击事件
  ~~~
  // Called when your app has been activated by the user selecting an action from a local notification.
  // A nil action identifier indicates the default action.
  // You should call the completion handler as soon as you've finished handling the action.
  - (void)application:(UIApplication *)application handleActionWithIdentifier:(nullable NSString *)identifier forLocalNotification:(UILocalNotification *)notification completionHandler:(void(^)())completionHandler NS_DEPRECATED_IOS(8_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]") __TVOS_PROHIBITED;
  ~~~
  对于 iOS 10.0以上系统，在该回调中实现通知栏按钮点击事件：
  ~~~  
  // The method will be called on the delegate when the user responded to the notification by opening the application, dismissing the notification or choosing a UNNotificationAction. The delegate must be set before the application returns from application:didFinishLaunchingWithOptions:.
  - (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)(void))completionHandler __IOS_AVAILABLE(10.0) __WATCHOS_AVAILABLE(3.0) __TVOS_PROHIBITED;
  ~~~

## 推送服务是否可用
可以通过 TACMessagingService 中的状态来检测推送服务是否可用
~~~
/**
  @brief 返回信鸽推送服务的状态，启动返回 YES，未启动返回 NO。
 */
@property (nonatomic, assign, readonly) BOOL status;
~~~

## 管理程序 SpringBoard 上的角标


### 获取程序当前角标数量

Objective-C 代码示例：
~~~
NSInteger count =[[TACMessagingService defaultService] applicationBadgeNumber];
~~~

Swift 代码示例：
~~~
let count = TACMessagingService.default().applicationBadgeNumber
~~~

###  设置程序当前角标数量

Objective-C 代码示例：
~~~
NSInteger badgeNumber =  @(2);
[[TACMessagingService defaultService] setApplicationBadgeNumber:badgeNumber];
~~~

Swift 代码示例：
~~~
let badgeNumber:NSInteger = 2
TACMessagingService.default().applicationBadgeNumber = badgeNumber
~~~


## 其他功能

其他功能请参考 [TACMessagingService.h]() 中的定义。
