To count the clicks and opened data pushed by XGPush, do the following steps.
## Counting Opened Data
To count opened data, developers need to call handleLaunching in
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
in UIApplicationDelegate.

#### APIs

```
/**
Call in didFinishLaunchingWithOptions to push feedbacks (when app is not running or when you click Start Push)

@param launchOptions Parameter userinfo in didFinishLaunchingWithOptions
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)handleLaunching:(nonnull NSDictionary *)launchOptions
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```

#### Example

```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

[XGPush handleLaunching:launchOptions successCallback:^{
NSLog(@"[XGDemo] Handle launching success");
} errorCallback:^{
NSLog(@"[XGDemo] Handle launching error");
}];
}
```
## Counting Clicks

- **Versions before iOS 10**

For versions before iOS 10, call handleReceiveNotification in
```
- (void)application:(UIApplication *)application
didReceiveRemoteNotification:(NSDictionary *)userInfo;
```
in UIApplicationDelegate.

#### APIs

```
/**
Call in didReceiveRemoteNotification to push feedbacks.(When app is running)
@param userInfo Push information of Apple apns
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)handleReceiveNotification:(nonnull NSDictionary *)userInfo
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```
#### Example

```
- (void)application:(UIApplication *)application
didReceiveRemoteNotification:(NSDictionary *)userInfo {

NSLog(@"[XGPush Demo] receive Notification");
[XGPush handleReceiveNotification:userInfo
successCallback:^{
NSLog(@"[XGDemo] Handle receive success");
} errorCallback:^{
NSLog(@"[XGDemo] Handle receive error");
}];
}
```
- **iOS 10 **

For iOS 10, call handleReceiveNotification in
```
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
withCompletionHandler:(void(^)())completionHandler;
```
in UIApplicationDelegate.

#### APIs

```
/**
Call in didReceiveRemoteNotification to push feedbacks.(When app is running)

@param userInfo Push information of Apple apns
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)handleReceiveNotification:(nonnull NSDictionary *)userInfo
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```

#### Example

```
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
withCompletionHandler:(void(^)())completionHandler {

[XGPush handleReceiveNotification:response.notification
.request.content.userInfo
successCallback:^{
NSLog(@"[XGDemo] Handle receive success");
} errorCallback:^{
NSLog(@"[XGDemo] Handle receive error");
}];

completionHandler()
}
```


