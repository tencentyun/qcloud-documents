## Enabling Debug
After you enable the Debug mode, you can see the detailed XGPush Debug information on the terminal for easy issue location.

#### Example
```
//Enable debug
[[XGPush defaultManager] setEnableDebug:YES];
//Check if the debug is enabled
BOOL debugEnabled = [[XGPush defaultManager] isEnableDebug];
```
## Enable XGPush

#### APIs

```
- (void)startXGWithAppID:(uint32_t)appID appKey:(nonnull NSString *)appKey delegate:(nullable id<XGPushDelegate>)delegate ;
```

#### Example

```
[[XGPush defaultManager] startXGWithAppID:2200262432 appKey:@"I89WTUY132GJ" delegate:<#your delegate#>];
```
## Terminating XGPush
Devices cannot receive push messages from XGPush if your terminate XGPush.

#### APIs

```
 - (void)stopXGNotification;
```

#### Example

```
[[XGPush defaultManager] stopXGNotification];
```

## Collecting Push Effects
Users' behaviors on push messages need to be reported to learn about the operational effect of each push message.

### Collecting the Arrival of Push Messages
You need to call the data reporting API in the following callback method of UIApplicationDelegate.

```
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```

#### APIs
```
- (void)reportXGNotificationInfo:(nonnull NSDictionary *)info;
```
#### Example
```
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      [[XGPush defaultManager] reportXGNotificationInfo:launchOptions];
}
```
### Collecting the Clicked Messages

- **Versions before iOS 10**
You need to call the data reporting API in the following callback method of UIApplicationDelegate.
```
- (void)application:(UIApplication *)application
    didReceiveRemoteNotification:(NSDictionary *)userInfo;
```

#### APIs
```
- (void)reportXGNotificationInfo:(nonnull NSDictionary *)info;
```
#### Example
```
- (void)application:(UIApplication *)application
    didReceiveRemoteNotification:(NSDictionary *)userInfo {
    [[XGPush defaultManager] reportXGNotificationInfo:userInfo];
}
```

- **iOS 10 or later**
The following XGPushDelegate callback method needs to be implemented, and the above reporting API needs to be called.

```
- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
    didReceiveNotificationResponse:(UNNotificationResponse *)response
    withCompletionHandler:(void(^)())completionHandler;
```
#### Example:
```
- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
    didReceiveNotificationResponse:(UNNotificationResponse *)response
    withCompletionHandler:(void(^)())completionHandler {
      [[XGPush defaultManager] reportXGNotificationInfo:response.notification.request.content.userInfo];

    completionHandler()
}
```

-  If you want to display the push messages when the application is at foreground, implement the following method and call the reporting API in it.

```
- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler
```

#### Example

```
- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler {
[[XGPush defaultManager] reportXGNotificationInfo:notification.request.content.userInfo];
    completionHandler(UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert);
}
```

