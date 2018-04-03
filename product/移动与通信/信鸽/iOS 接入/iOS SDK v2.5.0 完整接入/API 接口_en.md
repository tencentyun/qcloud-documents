## Enabling Debug
After you enable the Debug mode, you can see the detailed XGPush Debug information on the terminal for easy issue location.

#### Example
```
//Enable debug 
XGSetting *setting = [XGSetting getInstance];
[setting enableDebug:YES];
//Check if the debug is enabled
BOOL debugEnabled = [setting isEnableDebug];
```
## Initializing XGPush
You need to call the XGPush initialization method in the callback of 
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
in UIApplicationDelegate before using XGPush.

#### 1. APIs
```
/**
Initializing XGPush

@param appId App ID requested from the foreground
@param appKey appKey requested from the foreground
*/
+(void)startApp:(uint32_t)appId appKey:(nonnull NSString *)appKey;
```
#### 2. Example
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
[XGPush startApp:1234567890 appKey:@"ABCDEFGHIJKLMN"];
}
```

## Signing Up for Apple Push Service
You need to sign up for the Apply push service before using it. For more information on how to sign up, please see Demo.
>**Note:**
> In iOS 10, you can use the registration methods for the versions before iOS 10. However, if you use such methods, you must also use the push receiving methods for the versions before iOS 10.

#### Example
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
//For more information on the code, please see the implementation of registerAPNS in Demo
[self registerAPNS];
}
```

## Signing Up for XGPush
After you have signed up for the Apple push service, you also need to sign up for XGPush. Call the registerDevice of methodXGPush in the callback of 
```
- (void)application:(UIApplication *)application
didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken;
```
in UIApplicationDelegate to sign up for for XGPush.
>**Note:**
>account is the account that needs to be configured according to business needs. It can be the user's name or ID, etc, and its length should contain more than two bytes. Do not use simple strings such as "myAccount", "test", or "123456". If you do not want to configure an account, pass nil.

#### 1. APIs
```
/**
Register the device

@param deviceToken Obtain via the callback of didCodeForRemoteNotificationsWithDeviceToken 
of appdelegate
@param successCallback Callback successful
@param errorCallback Callback failed
@return The obtained deviceToken string 
*/
+(nullable NSString *)registerDevice:(nonnull NSData *)deviceToken
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
Register the device and configure an account

@param deviceToken Obtain via the callback of didCodeForRemoteNotificationsWithDeviceToken
of appDelegate
@param account The account to configure, containing more than 2 bytes. Do not use simple strings such as "test" and "123456".
If you do not want to configure an account, pass nil
@param successCallback Callback successful
@param errorCallback Callback failed
@return The obtained deviceToken string
*/
+(nullable NSString *)registerDevice:(nonnull NSData *)deviceToken
account:(nullable NSString *)account
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
Register the device and configure an account, string token version

@param deviceToken token of NSString *type
@param account The account to configure. If you do not want to configure an account, pass nil
@param successCallback Callback successful
@param errorCallback Callback failed
@return The obtained deviceToken string
*/
+(nullable NSString *)registerDeviceStr:(nonnull NSString *)deviceToken
account:(nullable NSString *) account
successCallback:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void))errorCallback;
```

#### 2. Example
```
- (void)application:(UIApplication *)application
didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {

NSString *deviceTokenStr = [XGPush registerDevice:deviceToken
account:nil
successCallback:^{
NSLog(@"[XGPush Demo] register push success");
} errorCallback:^{
NSLog(@"[XGPush Demo] register push error");
}];
NSLog(@"[XGPush Demo] device token is %@", deviceTokenStr);
}
```

## Configuring/Deleting tags
Developers can configure tags for different users and then push based on tags. Pushing based on tags allows all devices under a tag to receive the push. A device can be configured with multiple tags.

#### 1. APIs
```
/**
Configure a tag

@param tag The tag to configure
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)setTag:(nonnull NSString *)tag
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
Delete a tag

@param tag The tag to delete
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)delTag:(nonnull NSString *)tag
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```
#### 2. Example

```
- (void)setTag:(NSString *)tag {
[XGPush setTag:@"myTag" successCallback:^{
NSLog(@"[XGDemo] Set tag success");
} errorCallback:^{
NSLog(@"[XGDemo] Set tag error");
}];
}

- (void)delTag:(NSString *)tag {
[XGPush delTag:@"myTag" successCallback:^{
NSLog(@"[XGDemo] Del tag success");
} errorCallback:^{
NSLog(@"[XGDemo] Del tag error");
}];
}
```

## Configuring/Deleting Accounts
Developers can configure accounts for different users and push based on accounts. Pushing based on accounts allows all devices under an account to receive the push.
>**Notes:**
>1. Only one account can be configured for a device. When you configure a new account, the previous account will automatically become invalid. A maximum of 15 devices can be bound to an account. If the number of devices bound to an account exceeds 15, a random device will be unbounded. After that, the remaining devices can be registered.
> 2. Earlier version APIs without callback requires calling the registered devices after an account is configured/deleted, while new version APIs with callback does not need to do so.

#### 1. APIs

```
/**
Configure the device's account. You need to call registerDevice before configuring the account.

@param account The account to configure, containing more than 2 bytes. Do not use simple strings such as "test" and "123456"
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)setAccount:(nonnull NSString *)account
successCallback:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void)) errorCallback;

/**
Delete the configured account. You need to call registerDevice before deleting the account

@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)delAccount:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void)) errorCallback;
```
#### 2. Example

```
- (void)setAccount:(NSString *)account {
[XGPush setAccount:@"myAccount" successCallback:^{
NSLog(@"[XGDemo] Set account success");
} errorCallback:^{
NSLog(@"[XGDemo] Set account error");
}];
}

- (void)delAccount {
[XGPush delAccount:^{
NSLog(@"[XGDemo] Del account success");
} errorCallback:^{
NSLog(@"[XGDemo] Del account error");
}];
}
```

## Deregister Devices
Deregistered devices cannot receive any push.
>**Note:**
>**To re-enable push, you need to call the registerAPNS and registerDevice again.**

#### 1. APIs

```
/**
Deregister the device to stop receiving push
@param successCallback Callback successful
@param errorCallback Callback failed
*/
+(void)unRegisterDevice:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```
#### 2. Example

```
[XGPush unRegisterDevice:^{
NSLog(@"[XGDemo] unregister success");
} errorCallback:^{
NSLog(@"[XGDemo] unregister error");
}];
```




