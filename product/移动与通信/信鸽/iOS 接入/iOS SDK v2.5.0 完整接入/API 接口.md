## 开启 Debug
打开 Debug 模式以后可以在终端看到详细的信鸽 Debug 信息。方便定位问题。

#### 示例
```
//打开debug开关
XGSetting *setting = [XGSetting getInstance];
[setting enableDebug:YES];
//查看debug开关是否打开
BOOL debugEnabled = [setting isEnableDebug];
```
## 初始化信鸽
在使用信鸽之前，需要先在 UIApplicationDelegate 中的
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;
```
回调中调用信鸽的初始化方法才能正常使用信鸽。

#### 1. 接口
```
/**
初始化信鸽

@param appId 通过前台申请的应用ID
@param appKey 通过前台申请的appKey
*/
+(void)startApp:(uint32_t)appId appKey:(nonnull NSString *)appKey;
```
#### 2. 示例
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
[XGPush startApp:1234567890 appKey:@"ABCDEFGHIJKLMN"];
}
```

## 注册苹果推送服务
使用推送前，需要先向苹果注册推送服务。请参考 Demo 向苹果注册推送服务。
>**注意：**
>在 iOS 10 中也可以可以使用 iOS 10 之前的注册方法来注册推送,但是对应的,也要使用 iOS 10 之前的方法来接收推送。

#### 示例
```
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
// 详细代码参考 Demo 中 registerAPNS 的实现
[self registerAPNS];
}
```

## 注册信鸽
向苹果注册完成推送服务以后，还需要向信鸽注册推送。在 UIApplicationDelegate 的
```
- (void)application:(UIApplication *)application
didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken;
```
回调中调用信鸽的 registerDevice 方法即可完成信鸽注册。
>**注意：**
>account 是需要设置的账号，视业务需求自定义，可以是用户的名称或者 ID 等，长度为两个字节以上，不要使用“myAccount”或者"test"，"123456"这种过于简单的字符串，若不想设置账号，请传入 nil。

#### 1. 接口
```
/**
注册设备

@param deviceToken 通过appdelegate的didRegisterForRemoteNotificationsWithDeviceToken
回调的获取
@param successCallback 成功回调
@param errorCallback 失败回调
@return 获取的 deviceToken 字符串
*/
+(nullable NSString *)registerDevice:(nonnull NSData *)deviceToken
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
注册设备并且设置账号

@param deviceToken 通过appDelegate的didRegisterForRemoteNotificationsWithDeviceToken
回调的获取
@param account 需要设置的账号,长度为2个字节以上，不要使用"test","123456"这种过于简单的字符串,
若不想设置账号,请传入nil
@param successCallback 成功回调
@param errorCallback 失败回调
@return 获取的 deviceToken 字符串
*/
+(nullable NSString *)registerDevice:(nonnull NSData *)deviceToken
account:(nullable NSString *)account
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
注册设备并且设置账号, 字符串 token 版本

@param deviceToken NSString *类型的 token
@param account 需要设置的账号,若不想设置账号,请传入 nil
@param successCallback 成功回调
@param errorCallback 失败回调
@return 获取的 deviceToken 字符串
*/
+(nullable NSString *)registerDeviceStr:(nonnull NSString *)deviceToken
account:(nullable NSString *) account
successCallback:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void))errorCallback;
```

#### 2. 示例
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

## 设置/删除标签
开发者可以针对不同的用户设置标签，然后对该标签推送。对标签推送会让该标签下的所有设备都收到推送，一个设备可以设置多个标签。

#### 1. 接口
```
/**
设置 tag

@param tag 需要设置的 tag
@param successCallback 成功回调
@param errorCallback 失败回调
*/
+(void)setTag:(nonnull NSString *)tag
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;

/**
删除tag

@param tag 需要删除的 tag
@param successCallback 成功回调
@param errorCallback 失败回调
*/
+(void)delTag:(nonnull NSString *)tag
successCallback:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```
#### 2. 示例

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

## 设置/删除账号
开发者可以针对不同的用户设置账号，然后对账号推送。对账号推送会让该账号下的所有设备都收到推送。
>**注:**
>1. 一个设备只能设置一个账号，设置账号的时候前一个账号自动失效。一个账号最多绑定15台设备，超过之后会随机解绑一台设备，然后再进行注册。
>2. 老版本不带回调的接口要求设置/删除账号后再调用一次注册设备的方法，但是新版带回调的接口不需要再调用注册设备的方法。

#### 1. 接口

```
/**
设置设备的帐号. 设置账号前需要调用一次registerDevice

@param account 需要设置的账号,长度为2个字节以上，不要使用"test","123456"这种过于简单的字符串
@param successCallback 成功回调
@param errorCallback 失败回调
*/
+(void)setAccount:(nonnull NSString *)account
successCallback:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void)) errorCallback;

/**
删除已经设置的账号. 删除账号前需要调用一次registerDevice

@param successCallback 成功回调
@param errorCallback 失败回调
*/
+(void)delAccount:(nullable void(^)(void)) successCallback
errorCallback:(nullable void(^)(void)) errorCallback;
```
#### 2. 示例

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

## 注销设备
注销设备以后，可以让该设备不再接收推送。
>**注意：**
>**重新开启推送功能需要再次调用 registerAPNS 和 registerDevice 接口。**

#### 1. 接口

```
/**
注销设备，设备不再进行推送
@param successCallback 成功回调
@param errorCallback 失败回调
*/
+(void)unRegisterDevice:(nullable void (^)(void)) successCallback
errorCallback:(nullable void (^)(void)) errorCallback;
```
#### 2. 示例

```
[XGPush unRegisterDevice:^{
NSLog(@"[XGDemo] unregister success");
} errorCallback:^{
NSLog(@"[XGDemo] unregister error");
}];
```



