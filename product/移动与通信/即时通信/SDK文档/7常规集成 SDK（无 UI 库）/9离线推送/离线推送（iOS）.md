[](id:配置推送)

## 配置离线推送

如想要接收 APNs 离线消息通知，需要遵从如下几个步骤：

1. [申请 APNs 证书](#ApplyForCertificate)。
2. [上传证书到 IM 控制台](#UploadCertificate)。
3. 在 App 每次登录时，向苹果获取 [deviceToken](#DeviceToken)。
4. 调用 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) 接口将其上报到 IM 后台。

配置过 APNs 的 App ，当其切到后台或者被用户 Kill 之后，腾讯云就可以通过苹果的 APNs 后台对该设备进行离线消息推送，详细推送原理请参见 [Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)。
>!对于已经退出登录（主动登出或者被踢下线）的用户，不会收到任何消息通知。

[](id:ApplyForCertificate)

### 步骤1：申请 APNs 证书

申请 APNs 证书的具体操作步骤请参见 [Apple 推送证书申请](https://cloud.tencent.com/document/product/269/3898)。

[](id:UploadCertificate)

### 步骤2：上传证书到控制台

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击目标应用卡片，进入应用的基础配置页面。
3. 单击【iOS平台推送设置】右侧的【添加证书】。
4. 选择证书类型，上传 iOS 证书（p.12），设置证书密码，单击【确认】。
>!
>- 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）。
>- 上传证书需要设置密码，无密码收不到推送。
>- 发布 App Store 的证书需要设置为生产环境，否则无法收到推送。
>- 上传的 p12 证书必须是自己申请的真实有效的证书。
5. 待推送证书信息生成后，记录证书的 ID。

[](id:DeviceToken)

### 步骤3：App 向苹果后台请求 DeviceToken

您可以在您的 App 中添加如下代码，用来向苹果的后台服务器获取 DeviceToken：

```
// 向苹果后台请求 DeviceToken
- (void)registNotification
{
    if ([[[UIDevice currentDevice] systemVersion] floatValue] >= 8.0)
    {
        [[UIApplication sharedApplication] registerUserNotificationSettings:
                [UIUserNotificationSettings settingsForTypes:
                (UIUserNotificationTypeSound | UIUserNotificationTypeAlert | UIUserNotificationTypeBadge)
                categories:nil]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
    }
    else
    {
        [[UIApplication sharedApplication] registerForRemoteNotificationTypes:
                (UIUserNotificationTypeBadge | UIUserNotificationTypeSound | UIUserNotificationTypeAlert)];
    }
}
//在 AppDelegate 的回调中会返回 deviceToken，需要在登录后上报给腾讯云后台
-(void)application:(UIApplication *)app didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken
{
    //记录下 Apple 返回的 deviceToken
    _deviceToken = deviceToken;
}
```

[](id:uploadDeviceToken)

### 步骤4：登录 IM SDK 后上传 Token 到腾讯云

在 IM SDK 登录成功后，就可以调用 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) 接口，将 [步骤3](#DeviceToken) 中获取的 DeviceToken 上传到腾讯云后台，实例代码如下：

```
V2TIMAPNSConfig *confg = [[V2TIMAPNSConfig alloc] init];
// 推送证书 ID，上传推送证书（p.12）到 IM 控制台后生成
confg.businessID = businessID;
// 苹果后台请求的  deviceToken
confg.token = deviceToken;
[[V2TIMManager sharedInstance] setAPNS:confg succ:^{
     NSLog(@"-----> 设置 APNS 成功");;
} fail:^(int code, NSString *msg) {
     NSLog(@"-----> 设置 APNS 失败");
}];
```

>! businessID 需要与控制台分配的证书 ID 保持一致。

## 推送格式 

推送格式示例如下图所示。
<img src="//main.qcloudimg.com/raw/d23be65b4c481beb71db993045b4fec9.png" width=480 />


### 通用推送规则

对于单聊消息，APNs 推送规则如下，其中昵称是发送方用户昵称，如果未设置昵称，则只显示内容。
```
昵称:内容
```
对于群聊消息，APNs 推送规则如下，其中名称展示优先级为消息发送者的`群名片`>`群昵称`，如果都没有，则不展示。
```
名称(群名):内容
```

### 不同类型消息推送规则

APNs 推送内容部分由消息体中各个 `Elem` 内容组成，不同 `Elem` 的离线消息展示效果如下表所示。

| 参数        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| 文本 Elem   | 直接显示内容                                                 |
| 语音 Elem   | 显示`[语音]`                                                 |
| 文件 Elem   | 显示`[文件]`                                                 |
| 图片 Elem   | 显示`[图片]`                                                 |
| 自定义 Elem | 显示发送消息时设置的 [desc](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html#aca3d09a4807ffc6486d556c055605c41) 的字段，如果 `desc` 不设置，则不进行推送 |


### 多 App 互通

如果将多个 App 中的 `SDKAppID` 设置为相同值，则可以实现多 App 互通。不同 App 需要使用不同的推送证书，您需要为每一个 App [申请 APNs 证书](https://cloud.tencent.com/document/product/269/3898) 并完成 [离线推送配置](#配置推送)。

## 自定义角标
- 默认情况下，当 APP 进入后台后，IMSDK 会将当前 IM 未读消息总数设置为角标。
- 如果想自定义角标，可按照如下步骤设置：
 1. App 调用 `- (void)setAPNSListener:(id<V2TIMAPNSListener>)apnsListener` 接口设置监听。
 2. App 实现 `- (uint32_t)onSetAPPUnreadCount` 接口，并在内部返回需要自定义的角标。
- 如果 App 接入了离线推送，当接收到新的离线推送时，App 角标会在基准角标（默认是 IM 未读消息总数，如果自定义了角标，则以自定义角标为准）的基础上加 1 逐条递增。
```
// 1. 设置监听
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 监听推送
    [V2TIMManager.sharedInstance setAPNSListener:self];
    // 监听会话的未读数
    [[V2TIMManager sharedInstance] setConversationListener:self];
    return YES;
}

// 2. 未读数发生变化后保存未读数
- (void)onTotalUnreadMessageCountChanged:(UInt64)totalUnreadCount {
    self.unreadNumber = totalUnreadCount;
}


// 3. APP 推到后台后上报自定义未读数
/** 程序进后台后，自定义 APP 的未读数，如果不处理，APP 未读数默认为所有会话未读数之和
 *  <pre>
 *
 *   - (uint32_t)onSetAPPUnreadCount {
 *       return 100;  // 自定义未读数
 *   }
 *
 *  </pre>
 */
- (uint32_t)onSetAPPUnreadCount {
    // 1. 获取自定义的角标
    uint32_t customBadgeNumber = ...
    
    // 2. 加上 IM 的消息未读数
    customBadgeNumber += self.unreadNumber;
    
    // 3. 通过 IMSDK 上报给 IM 服务器
    return customBadgeNumber;
}
```

## 自定义 iOS 推送提示音

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的`iOSSound`字段， `iOSSound` 传语音文件名（带后缀），语音文件需要链接进 Xcode 工程。

## 自定义离线推送展示

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置  [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的`title` 和 `desc`字段，其中 `title` 设置后，会在默认的推送内容上多展示 `title` 内容，`desc` 设置后，推送内容会变成 `desc` 内容。

## 自定义离线推送点击跳转逻辑

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置  [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的`ext` 字段，当用户收到离线推送启动 APP 的时候，可以在 `AppDelegate -> didReceiveRemoteNotification` 系统回调获取到 `ext` 字段，然后根据 `ext` 字段内容跳转到指定的 UI 界面。

本文以 “denny 给 vinson 发送消息” 的场景为例。
- 发送方：denny 需在发送消息时设置推送扩展字段 `ext`：
```
// denny在发送消息时设置 offlinePushInfo，并指定 ext 字段
V2TIMMessage *msg = [[V2TIMManager sharedInstance] createTextMessage:@"文本消息"];
V2TIMOfflinePushInfo *info = [[V2TIMOfflinePushInfo alloc] init];
info.ext = @"jump to denny";
[[V2TIMManager sharedInstance] sendMessage:msg receiver:@"vinson" groupID:nil priority:V2TIM_PRIORITY_DEFAULT
onlineUserOnly:NO offlinePushInfo:info progress:^(uint32_t progress) {
} succ:^{
} fail:^(int code, NSString *msg) {
}];
```
- 接收方：vinson 的 App 虽然不在线，但可以接收到 APNS 离线推送，当 vinson 点击推送消息时会启动 App：
```
// vinson 启动 APP 后会收到以下回调
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo 
fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
    // 解析推送扩展字段 desc
    if ([userInfo[@"ext"] isEqualToString:@"jump to denny"]) {
        //跳转到和 denny 的聊天界面
    }
}
```

## 常见问题

### 普通消息为什么收不到离线推送？

首先，请检查下 App 的运行环境和证书的环境是否一致，如果不一致，收不到离线推送。
其次，检查下 App 和证书的环境是否为开发环境，如果是开发环境，向苹果申请 `deviceToken` 可能会失败，生产环境暂时没有发现这个问题，请切换到生产环境测试。

### 自定义消息为什么收不到离线推送？

自定义消息的离线推送和普通消息不太一样，自定义消息的内容我们无法解析，不能确定推送的内容，所以默认不推送，如果您有推送需求，需要您在 [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 的时候设置  [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的 `desc`字段，推送的时候会默认展示 `desc` 信息。

### 如何关闭离线推送消息的接收？

如果您想关闭离线推送消息的接收，可以通过设置 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a6aecbdc0edaa311c3e4e0ed3e71495b1) 接口的 `config` 参数为 `nil` 来实现。该功能从5.6.1200版本开始支持。

