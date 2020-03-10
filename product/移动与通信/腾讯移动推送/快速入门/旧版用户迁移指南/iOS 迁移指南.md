## 版本迁移指南
如您接入的免费版2.x的版本，请参考 [SDK集成文档](https://cloud.tencent.com/document/product/548/36663) 接入。
为保障迁移后的正常使用，请您升级至 iOS V1.2.5.3 及以上版本，以下是针对从信鸽免费版本 3.x 迁移到腾讯云 TPNS iOS V1.2.5.3 及以上版本的变更说明：

## 自动集成方式
### Pod名称变更
 通过 Cocoapods 下载地址：
 `pod 'TPNS-iOS' `


### 托管仓库变更
因仓库地址变更为腾讯工蜂首次通过 pod 下载需要注册登录 [工蜂地址](https://git.code.tencent.com/users/sign_in)，并在【账户】菜单栏中设置账号和密码，然后在 Terminal 中设置腾讯工蜂的账号和密码。后续即可正常使用，当前 PC 不需要再次登录。


### 新增支持 Carthage 导入
在 Cartfile 文件中指明依赖的第三方库：
` github "xingePush/carthage-TPNS-iOS" `

## 手动导入
### SDK包下载
请前往 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns/sdkdownload) 下载 iOS SDK 压缩包、解压。

### 工程文件变更

变更前：

`XGPush.h` 、 `libXG-SDK.a`

变更后：

`XGPush.h` 、` libXG-SDK-Cloud.a`、 `XGMTACloud.framework`



### 依赖系统库变更

在 Build Phases 下，请将以下信鸽 3.x 版本系统依赖库做相应变更。

变更前：
```
 * CoreTelephony.framework
 * SystemConfiguration.framework
 * UserNotifications.framework
 * libXG-SDK.a
 * libz.tbd
 * libsqlite3.0.tbd
```
变更后：
```
* XGMTACloud.framework
* CoreTelephony.framework
* SystemConfiguration.framework
* UserNotifications.framework
* libXG-SDK-Cloud.a
* libz.tbd
* CoreData.framework
* CFNetwork.framework
* libc++.tbd
```
## 接口变更

与免费版本对比，部分 API 接口做了以下变更：

不推荐再调用 reportXGNotification* 数据统计上报接口，SDK 已内部自动处理。

变更前：
``` objective-c
 /**
     收到推送的回调
     @param application  UIApplication 实例
     @param userInfo 推送时指定的参数
     @param completionHandler 完成回调
     */
    - (void)application:(UIApplication *)application
        didReceiveRemoteNotification:(NSDictionary *)userInfo
            fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler
    {
        [[XGPush defaultManager] reportXGNotificationInfo:userInfo];
        completionHandler(UIBackgroundFetchResultNewData);
    }
    // iOS 10 新增回调 API
    // App 用户点击通知
    // App 用户选择通知中的行为
    // App 用户在通知中心清除消息
    // 无论本地推送还是远程推送都会走这个回调
#if __IPHONE_OS_VERSION_MAX_ALLOWED >=     __IPHONE_10_0
    - (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
        didReceiveNotificationResponse:(UNNotificationResponse *)response
        withCompletionHandler:(void (^)(void))completionHandler
        {
            [[XGPush defaultManager] reportXGNotificationResponse:response];
            completionHandler();
    }

    // App 在前台弹通知需要调用这个接口
    - (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
         willPresentNotification:(UNNotification *)notification
             withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler
             {
                 [[XGPush defaultManager] reportXGNotificationInfo:notification.request.content.userInfo];
                 completionHandler(UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert);
    }
    #endif
```
变更后：(如果没有自定义处理需求，则不再需要实现以下回调)
```objective-c
/**
  收到推送的回调
  @param application  UIApplication 实例
  @param userInfo 推送时指定的参数
  @param completionHandler 完成回调
  */
 - (void)application:(UIApplication *)application
             didReceiveRemoteNotification:(NSDictionary *)userInfo
                     fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler
     {
         completionHandler(UIBackgroundFetchResultNewData);
 }
 // iOS 10 新增回调 API
 // App 用户点击通知
 // App 用户选择通知中的行为
 // App 用户在通知中心清除消息
 // 无论本地推送还是远程推送都会走这个回调
#if __IPHONE_OS_VERSION_MAX_ALLOWED >=     __IPHONE_10_0
 - (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
             didReceiveNotificationResponse:(UNNotificationResponse *)response
             withCompletionHandler:(void (^)(void))completionHandler
             {
                     completionHandler();
 }

 // App 在前台弹通知需要调用这个接口
 - (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
              willPresentNotification:(UNNotification *)notification
                      withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler
                      {
                              completionHandler(UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert);
 }
 #endif
```


## 抵达数据上报集成

为了实现抵达数据上报和富媒体消息的功能，SDK 提供了 Service Extension 接口，可供客户端调用，从而可以监听消息的到达和发送富媒体消息，需要您实现此接口，接入指南请参见 [通知服务扩展的使用说明](https://cloud.tencent.com/document/product/548/36667)。

>!如果未集成此接口，则统计数据中消息『抵达数』与『点击数』一致。

## 测试

### 指定单设备推送

变更前：

免费版本使用 Device Token(长度为64位)对指定设备进行推送，获取 Device Token 代码示例:

```objective-c
//获取 APNS 生成的 Token
 [[XGPushTokenManager defaultTokenManager] deviceTokenString];
```
变更后：
腾讯云版本使用 TPNS Token(长度为36位)对指定设备进行推送，获取 TPNS Token 代码示例：

```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
```

## 注销免费服务

如果 App 的推送服务是从免费集群迁移到付费集群，在两个集群同时推送，可能会出现重复消息。因此需要调用 `TPNS SDK(1.2.5.3+)` 的接口将设备信息在免费集群中进行反注册，从而使得在两个集群同时推送时，避免出现重复消息。

#### 接口

```objective-c
// 免费集群的 accessId(支持免费 SDK V2、V3版本)
@property uint32_t freeAccessId;
```

#### 用法

- 引入头文件: `XGForFreeVersion.h` 

- 在 `startXGWithAppID:appKey:delegate:` 之前调用此接口，参考示例：

```objective-c
[XGForFreeVersion defaultForFreeVersion].freeAccessId = 2200262432;
[[XGPush defaultManager] startXGWithAppID: <#your tpns access ID#>appKey:<#your tpns access key#> delegate:<#your delegate#>];
```
