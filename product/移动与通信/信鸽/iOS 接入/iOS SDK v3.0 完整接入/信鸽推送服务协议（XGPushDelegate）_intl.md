Setting a XGPush protocol proxy is to make it easy for developers to check API calls. Developers can select how to implement the protocol based on their own needs.
The protocol method is as follows:
```
/**
 How to handle iOS 10 UNUserNotification.framework

 @param center [UNUserNotificationCenter currentNotificationCenter]
 @param notification Notification object
 @param completionHandler Callback object, which must be called
 */
- (void)xgPushUserNotificationCenter:(nonnull UNUserNotificationCenter *)center willPresentNotification:(nullable UNNotification *)notification withCompletionHandler:(nonnull void (^)(UNNotificationPresentationOptions options))completionHandler __IOS_AVAILABLE(10.0);

/**
 How to handle iOS 10 UNUserNotification.framework

 @param center [UNUserNotificationCenter currentNotificationCenter]
 @param response Users' response object to the notified message
 @param completionHandler Callback object, which must be called
 */
- (void)xgPushUserNotificationCenter:(nonnull UNUserNotificationCenter *)center didReceiveNotificationResponse:(nullable UNNotificationResponse *)response withCompletionHandler:(nonnull void (^)(void))completionHandler __IOS_AVAILABLE(10.0);

/**
 @brief Monitor the enabling of XGPush

 @param isSuccess Whether XGPush is enabled successfully
 @param error Messages on failed enabling of XGPush
 */
- (void)xgPushDidFinishStart:(BOOL)isSuccess error:(nullable NSError *)error;

/**
 @brief Monitor the termination of XGPush

 @param isSuccess Whether XGPush is terminated
 @param error Messages on failed termination of XGPush
 */
- (void)xgPushDidFinishStop:(BOOL)isSuccess error:(nullable NSError *)error;

/**
 @Brief Monitor the reporting of push messages on XGPush

 @param isSuccess Whether reporting is successful
 @param error Messages on failed reporting
 */
- (void)xgPushDidReportNotification:(BOOL)isSuccess error:(nullable NSError *)error;
```

