## 版本迁移指南
如您接入的是信鸽平台的2.x的版本，请参考 [SDK集成文档](https://cloud.tencent.com/document/product/548/36663) 接入。
为保障迁移后的正常使用，请您升级至 iOS V1.2.5.3 及以上版本，以下是针对从信鸽平台的 3.x 版本迁移到腾讯移动推送 TPNS iOS V1.2.5.3 及以上版本的变更说明：

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

与信鸽版本对比，部分 API 接口做了以下变更：

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

## 消息格式变更
与信鸽版本对比，终端收到消息格式变更如下：

### 通知消息

变更前：
```
{
	aps =     {
        alert =         {
            body = "通知内容";
            subtitle = "通知副标题";
            title = "通知标题";
        };
        badge = 1;
        category = "iOS通知category";
        "mutable-content" = 1;  // 开启后，推送详情中会有「抵达」和「点击」数据上报
        sound = "自定义通知音效.mp3";
    };
    custom1 = bar; // 自定义下发的参数string/JSON
    custom2 =     {
        bang = whiz;
    };  // 自定义下发的参数string/JSON
    xg =     {
        bid = 0;
        guid = 16625039711;
        msgid = 2273893660;
        token = c0999df7375868b9742de4b35387e49332b8c43b682482a7261278f1292eda95;
        ts = 1585709566;
    };
    "xg_media_resources" = "富媒体链接如(https://img2.woyaogexing.com/2018/01/24/5248092370629ca4!400x400_big.jpg)";
}
```

变更后：
```
{
    aps =     {
        alert =         {
            body = "通知内容";
            "launch-image" = "";
            "loc-args" = "<null>";
            "loc-key" = "";
            subtitle = "通知副标题";
            "subtitle-loc-args" = "<null>";
            "subtitle-loc-key" = "";
            title = "通知标题";
            "title-loc-args" = "<null>";
            "title-loc-key" = "";
        };
        "badge_type" = "-1";  // 角标类型，-1不变，-2自动加一，也可以自定义为大于0的值
        category = "iOS通知category";
        "mutable-content" = 1;  // 开启后，推送详情中会有「抵达」和「点击」数据上报
        sound = "自定义通知音效.mp3";
        "thread-id" = "";
    };
    custom = "{\"附加参数key1\":\"附加参数value1\",\"附加参数key2\":\"附加参数value2\"}";  // 可用于应用业务逻辑处理
    xg =     {
        bid = 390178628;
        groupId = "pt:tpns_20200401";
        guid = 338502;
        msgid = 390178628;
        msgtype = 1;
        pushTime = 1585716731;
        source = 1;
        targettype = 2;
        ts = 1585716731;
        xgToken = 00c30e0aeddff1270d8816ddc594606dc184;
    };
    "xg_media_resources" = "富媒体链接如(https://img2.woyaogexing.com/2018/01/24/5248092370629ca4!400x400_big.jpg)";
}
```
### 静默消息

变更前：
```
{
	aps =     {
        content = "内容";
        "content-available" = 1;
        title = "标题";
    };
    custom1 = bar1;  // 自定义下发的参数string/JSON
    custom2 =     (
        bang,
        whizfgg
    );  // 自定义下发的参数string/JSON
    xg =     {
        bid = 0;
        guid = 16625039711;
        msgid = 2274434534;
        token = c0999df7375868b9742de4b35387e49332b8c43b682482a7261278f1292eda95;
        ts = 1585709604;
    };
}
```
变更后：
```
{
    aps =     {
        alert = "<null>";
        "badge_type" = 0;
        category = "";
        "content-available" = 1;
        sound = "";
        "thread-id" = "";
    };
    custom = "{\"附加参数key1\":\"附加参数value1\",\"附加参数key2\":\"附加参数value2\"}";  // 可用于应用业务逻辑处理
    xg =     {
        bid = 389886288;
        groupId = "pt:tpns_20200331";
        guid = 338502;
        msgid = 389886288;
        msgtype = 2;
        pushTime = 1585644263;
        source = 1;
        targettype = 2;
        ts = 1585644263;
        xgToken = 00c30e0aeddff1270d8816ddc594606dc184;
    };
}
```


## 抵达数据上报集成

为了实现抵达数据上报和富媒体消息的功能，SDK 提供了 Service Extension 接口，可供客户端调用，从而可以监听消息的到达和发送富媒体消息，需要您实现此接口，接入指南请参见 [通知服务扩展的使用说明](https://cloud.tencent.com/document/product/548/36667)。

>!如果未集成此接口，则统计数据中消息『抵达数』与『点击数』一致。

## 测试

### 指定单设备推送

变更前：

信鸽平台使用 Device Token(长度为64位)对指定设备进行推送，获取 Device Token 代码示例:

```objective-c
//获取 APNS 生成的 Token
 [[XGPushTokenManager defaultTokenManager] deviceTokenString];
```
变更后：
腾讯移动推送平台使用 TPNS Token(长度为36位)对指定设备进行推送，获取 TPNS Token 代码示例：

```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
```

## 注销信鸽平台推送服务
如果 App 的推送服务是从信鸽平台（https://xg.qq.com）迁移到腾讯移动推送平台， 需要调用 `TPNS SDK(1.2.5.3+)` 的接口将设备信息在信鸽平台中进行反注册。

#### 接口

```objective-c
// 信鸽平台的 accessId(支持信鸽 SDK V2、V3版本)
@property uint32_t freeAccessId;
```

#### 用法

- 引入头文件: `XGForFreeVersion.h` 

- 在 `startXGWithAppID:appKey:delegate:` 之前调用此接口，参考示例：

```objective-c
[XGForFreeVersion defaultForFreeVersion].freeAccessId = 2200262432;
[[XGPush defaultManager] startXGWithAppID: <#your tpns access ID#>appKey:<#your tpns access key#> delegate:<#your delegate#>];
```
>! 如果未做以上配置，则在信鸽和腾讯移动推送两个平台上同时推送时，可能会出现重复消息。
