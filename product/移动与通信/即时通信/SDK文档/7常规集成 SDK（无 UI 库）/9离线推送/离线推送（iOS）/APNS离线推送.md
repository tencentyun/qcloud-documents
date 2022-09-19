## 概述

即时通信 IM 的终端用户需要随时都能够得知最新的消息，而由于移动端设备的性能与电量有限，当 App 处于后台时，为了避免维持长连接而导致的过多资源消耗，即时通信 IM 推荐您使用 Apple 提供的系统级推送通道（APNs）来进行消息通知，APNs 相比第三方推送拥有更稳定的系统级长连接，可以做到随时接受推送消息，且资源消耗大幅降低。
<dx-alert infotype="notice" title="">
- 在没有主动退出登录的情况下，应用退后台、手机锁屏、或者应用进程被用户主动杀掉三种场景下，如果想继续接收到 IM 消息提醒，可以接入即时通信 IM 离线推送。
- 如果应用主动调用 logout 退出登录，或者多端登录被踢下线，即使接入了 IM 离线推送，也收不到离线推送消息。
</dx-alert>

 [](id:配置推送)

## 配置离线推送

如想要接收 APNs 离线消息通知，需要遵从如下几个步骤：

1. [申请 APNs 证书](#ApplyForCertificate)。
2. [上传证书到 IM 控制台](#UploadCertificate)。
3. 在 App 每次登录时，向苹果获取 [deviceToken](#DeviceToken)。
4. 调用 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) 接口将其上报到 IM 后台。

[](id:ApplyForCertificate)
### 步骤1：申请 APNs 证书

####  开启 APP 远程推送

1. 登录 [苹果开发者中心](https://developer.apple.com/account/) 网站，单击**Certificates,Identifiers & Profiles**或者侧栏的**Certificates, IDS & Profiles**，进入 Certificates, IDS & Profiles 页面。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/5888bba294f17848ab8343d507ee427d.jpg" style="zoom:50%;" />

2. 单击 Identifiers 右侧的**+**。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/ba3222cc6bda236f5080e897351c36a2.png" style="zoom:50%;" />

3. 您可以参考如下步骤新建一个 AppID，或者在您原有的 AppID 上增加 `Push Notification` 的 `Service`。

   > ? 您 App 的 `Bundle ID` 不能使用通配符 `*`，否则将无法使用远程推送服务。

4. 勾选**App IDs**，单击**Continue**进行下一步。
   <img src="https://main.qcloudimg.com/raw/1e047d154a30d4dc95e3d9fa52779a37.jpg" style="zoom:50%;" />

5. 选择**App**，单击**Continue**进行下一步。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/d8c81677b1c06cad5d2b4017a17eb5ae.jpg" style="zoom:50%;" />

6. 配置 `Bundle ID` 等其他信息，单击**Continue**进行下一步。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/bc8105688bc097e5028585f4a1a57088.png" style="zoom:50%;" />

7. 勾选**Push Notifications**，开启远程推送服务。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/bcdc52d8bae2c8bfabdbe2364d1b1180.jpg" style="zoom:50%;" />

#### 生成证书

1. 选中您的 AppID，选择**Configure**。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/7f1a06b0d5e7ae4ea74106218e3169c9.jpg" style="zoom:50%;" />

2. 可以看到在**Apple Push Notification service SSL Certificates**窗口中有两个 `SSL  Certificate` ，分别用于开发环境（Development）和生产环境（Production）的远程推送证书，如下图所示：
   <img src="https://main.qcloudimg.com/raw/bd55cffb96e80b505e70db33c73e27dd.jpg" style="zoom:50%;" />

3. <span id="step3"></span>我们先选择开发环境（Development）的**Create Certificate**，系统将提示我们需要一个 Certificate Signing Request（CSR）。
   <img src="https://main.qcloudimg.com/raw/637ce37ec54ca5a4bf3006b527572da5.jpg" style="zoom:50%;" />

4. 在 Mac 上打开**钥匙串访问工具（Keychain Access）**，在菜单中选择**钥匙串访问**>**证书助理**>**从证书颁发机构请求证书**（`Keychain Access - Certificate Assistant - Request a Certificate From a Certificate Authority`）。
   <img src="https://main.qcloudimg.com/raw/6492b4df769ec5bccf90994d30e5e520.jpg" style="zoom:50%;" />

5. 输入用户电子邮件地址（您的邮箱）、常用名称（您的名称或公司名），选择**存储到磁盘**，单击继续，系统将生成一个 `*.certSigningRequest` 文件。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/258d11e7a7d79ab51a8f89560400eac6.png" style="zoom:50%;" />

6. 返回上述 [第3步骤](#step3) 中 Apple Developer 网站刚才的页面，单击**Choose File**上传生成的`*.certSigningRequest`文件。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/ac9f49f0d8afbcdfa42f13511334f00b.png" style="zoom:50%;" />

7. 单击**Continue**，即可生成推送证书。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/c19c9bbdbdd8fdfe6b4f95af08d9035c.jpg" style="zoom:50%;" />

8. 单击**Download**下载开发环境的 `Development SSL Certificate` 到本地。
   ![](https://main.qcloudimg.com/raw/9dece7f318c93e97732fe7ea7806f961.jpg)

9. 再次按照上述步骤1 - 8，将生产环境的 `Production SSL Certificate` 下载到本地。

   > ? 生产环境的证书实际是开发（Sandbox）+生产（Production）的合并证书，可以同时作为开发环境和生产环境的证书使用。

   []()

   <img src="https://qcloudimg.tencent-cloud.cn/raw/4720f74f609c9225f43ab977215ff53f.jpg" style="zoom:50%;" />

   <img src="https://qcloudimg.tencent-cloud.cn/raw/62f6ff03e36340507d66e519796258dc.jpg" style="zoom:50%;" />

   

10. 双击打开下载的开发环境和生产环境的 `SSL Certificate`，系统会将其导入钥匙串中。

11. 打开钥匙串应用，在**登录**>**我的证书**，右键分别导出刚创建的开发环境（`Apple Development IOS Push Service`）和生产环境（`Apple Push Services`）的 `P12` 文件。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/3ab45a54c9cf39beffb1fc2adf12a0e5.jpg" style="zoom:50%;" />

    > ! 保存`P12`文件时，请务必要为其设置密码。



[](id:UploadCertificate)

### 步骤2：上传证书到控制台
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击目标应用卡片，进入应用的基础配置页面。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/74c3e635896cf575de7bd9bfafa135e8.jpg" style="zoom:50%;" />
3. 单击**iOS 原生离线推送设置**右侧的**添加证书**。
4. 选择证书类型，上传 iOS 证书（p.12），设置证书密码，单击**确认**。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/c2843be158d3a7c0beaa91dda62dea88.jpg" style="zoom:50%;" />

>!
>- 上传证书名最好使用全英文（尤其不能使用括号等特殊字符）。
>- 上传证书需要设置密码，无密码收不到推送。
>- 发布 App Store 的证书需要设置为生产环境，否则无法收到推送。
>- 上传的 p12 证书必须是自己申请的真实有效的证书。

[](id:businessid)

5. 待推送证书信息生成后，记录证书的 ID。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/f0be96239237918df38977e25d982e23.jpg" style="zoom:50%;" />

[](id:DeviceToken)

### 步骤3：App 向苹果后台请求 deviceToken

您可以在您的 App 中添加如下代码，用来向苹果的后台服务器获取 deviceToken：

> ? 考虑到合规，建议您在用户同意隐私协议之后再向苹果请求 deviceToken。

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

### 步骤4：登录 IM SDK 后上传 deviceToken 到腾讯云

在 IM SDK 登录成功后，就可以调用 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a73bf19c0c019e5e27ec441bc753daa9e) 接口，将 [步骤3](#DeviceToken) 中获取的 deviceToken 上传到腾讯云后台，示例代码如下，可参考 [ TUIKitDemo](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/AppDelegate+Push.m) 接入：

```
- (void)push_registerIfLogined:(NSString *)userID
{
    NSLog(@"[PUSH] %s, %@", __func__, userID);
    BOOL supportTPNS = NO;
    if ([self respondsToSelector:@selector(supportTPNS:)]) {
        supportTPNS = [self supportTPNS:userID];
    }
    
    if (self.deviceToken) {
        V2TIMAPNSConfig *confg = [[V2TIMAPNSConfig alloc] init];
        /* 用户自己到苹果注册开发者证书，在开发者帐号中下载并生成证书(p12 文件)，将生成的 p12 文件传到腾讯证书管理控制台，控制台会自动生成一个证书 ID，将证书 ID 传入以下 busiId 参数中。*/
        //推送证书 ID
        confg.businessID = sdkBusiId;
        confg.token = self.deviceToken;
        [[V2TIMManager sharedInstance] setAPNS:confg succ:^{
             NSLog(@"%s, succ, %@", __func__, supportTPNS ? @"TPNS": @"APNS");
        } fail:^(int code, NSString *msg) {
             NSLog(@"%s, fail, %d, %@", __func__, code, msg);
        }];
    }
    // ...
}
```

>! businessID 需要与控制台分配的 [证书 ID](#businessid) 保持一致。

## 推送格式 

推送格式示例如下图所示。
<img src="//main.qcloudimg.com/raw/d23be65b4c481beb71db993045b4fec9.png" width=480 />

### 通用推送规则

对于单聊消息，APNs 推送规则如下，其中昵称是发送方用户昵称，如果未设置昵称，则只显示内容。
```
昵称:内容
```
对于群聊消息，APNs 推送规则如下，其中名称展示优先级为消息发送者的`群名片`>`昵称`，如果都没有，则不展示。
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

> ? 如果默认的推送规则不满足您的要求，IMSDK 支持自定义，详见 [自定义离线推送展示](#customdisplay) 。

### 多 App 互通

如果您需要在多个 App 之间互相接收推送消息，可以将多个 App 中的 `SDKAppID` 设置为相同值。

> ? 不同的 App 需要使用不同的推送证书，您需要为每一个 App [申请 APNs 证书](#ApplyForCertificate) 并完成 [离线推送配置](#配置推送)。

## 自定义角标
- 默认情况下，当 App 进入后台后，IMSDK 会将当前 IM 未读消息总数设置为角标。
- 如果想自定义角标，可按照如下步骤设置：
 1. App 调用 [- (void)setAPNSListener:(id<V2TIMAPNSListener>)apnsListener](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a62e1694cf9e1d65b76f90064cbcbb683) 接口设置监听。
 2. App 实现 [- (uint32_t)onSetAPPUnreadCount](https://im.sdk.qcloud.com/doc/zh-cn/protocolV2TIMAPNSListener-p.html#a164265ae900e0ddeb6d6393786a548ba) 接口，并在内部返回需要自定义的角标。
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


// 3. App 推到后台后上报自定义未读数
/** 程序进后台后，自定义 App 的未读数，如果不处理，App 未读数默认为所有会话未读数之和
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

## 自定义推送提示音

### iOS 推送提示音

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的 `iOSSound` 字段， `iOSSound` 传语音文件名。

> ? 
>
> - 离线推送声音设置（仅对 iOS 生效）， 当 iOSSound = kIOSOfflinePushNoSound，表示接收时不会播放声音。 
> - 当 iOSSound = kIOSOfflinePushDefaultSound，表示接收时播放系统声音。 
> - 如果要自定义 iOSSound，需要先把语音文件链接进 Xcode 工程，然后把语音文件名（带后缀名）设置给 iOSSound。

```
V2TIMOfflinePushInfo *pushInfo = [[V2TIMOfflinePushInfo alloc] init];
pushInfo.title = @"push title";
pushInfo.iOSSound = @"phone_ringing.mp3"; // your voice file's name
[[V2TIMManager sharedInstance] sendMessage:msg receiver:receiver groupID:groupID priority:V2TIM_PRIORITY_DEFAULT onlineUserOnly:NO offlinePushInfo:pushInfo progress:nil succ:^{

} fail:^(int code, NSString *msg) {

}];
```

### Android 推送提示音

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置 [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的 `AndroidSound` 字段， `AndroidSound` 传语音文件名。

> ? 
>
> * 离线推送声音设置（仅对 Android 生效, 仅 imsdk 6.1 及以上版本支持） 只有华为和谷歌手机支持设置铃音提示，
> * 小米铃音设置请您参照：https://dev.mi.com/console/doc/detail?pId=1278%23_3_0 
> * 如果要自定义 AndroidSound，需要先把语音文件放到 Android 工程的 raw 目录中，然后把语音文件名（不需要后缀名）设置给 AndroidSound。

```
V2TIMOfflinePushInfo *pushInfo = [[V2TIMOfflinePushInfo alloc] init];
pushInfo.title = @"push title";
pushInfo.AndroidSound = @"phone_ringing"; // your voice file's name
[[V2TIMManager sharedInstance] sendMessage:msg receiver:receiver groupID:groupID priority:V2TIM_PRIORITY_DEFAULT onlineUserOnly:NO offlinePushInfo:pushInfo progress:nil succ:^{

} fail:^(int code, NSString *msg) {

}];
```





[](id:customdisplay)

## 自定义离线推送展示

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置  [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的`title` 和 `desc`字段，其中 `title` 设置后，会在默认的推送内容上多展示 `title` 内容，`desc` 设置后，推送内容会变成 `desc` 内容。

```
V2TIMOfflinePushInfo *info = [[V2TIMOfflinePushInfo alloc] init];
info.title = @"Harvy";                        // 离线推送展示的标题。
info.desc = @"You hava a call invitation.";   // 离线推送展示的内容

// receiver 和 groupID 不能同时为空，且同时只能有一个存在
[[V2TIMManager sharedInstance] sendMessage:msg receiver:receiver groupID:groupID priority:V2TIM_PRIORITY_DEFAULT onlineUserOnly:NO offlinePushInfo:pushInfo progress:nil succ:^{

} fail:^(int code, NSString *msg) {

}];
```

<img src="https://qcloudimg.tencent-cloud.cn/raw/ba596982ee5ebaafc575ef1469ff4ff7.png" style="zoom:50%;" />

[]()

> ? 您还可以使用 APNs 的 `multable-content` 字段，结合 `NSNotification Service Extension` 来自定义显示内容。欢迎加入 QQ 群进行技术交流和反馈问题，QQ 群：**592465424**。



## 自定义离线推送点击跳转逻辑

请在调用  [sendMessage](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07Message_08.html#a3694cd507a21c7cfdf7dfafdb0959e56) 发送消息的时候设置  [offlinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/interfaceV2TIMOfflinePushInfo.html) 的`ext` 字段，当用户收到离线推送启动 APP 的时候，可以在 `AppDelegate -> didReceiveRemoteNotification` 系统回调获取到 `ext` 字段，然后根据 `ext` 字段内容跳转到指定的 UI 界面。可以参考 [TUIKitDemo](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/AppDelegate%2BPush.m) 接入。

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

如果您想关闭离线推送消息的接收，可以通过设置 [setAPNS](https://im.sdk.qcloud.com/doc/zh-cn/categoryV2TIMManager_07APNS_08.html#a6aecbdc0edaa311c3e4e0ed3e71495b1) 接口的 `config` 参数为 `nil` 来实现。该功能从5.6.1200 版本开始支持。

### 收不到推送，且后台报错 bad devicetoken。

Apple 的 deviceToken 与当前编译环境有关。如果 [登录 IMSDK 后上传 deviceToken 到腾讯云 ](#uploadDeviceToken) 所使用的证书ID 和 token 不一致，就会报错。

- 如果使用的是 Release 环境编译，则 `- application:didRegisterForRemoteNotificationsWithDeviceToken:`  回调返回的是发布环境的 token，此时 businessID 需要设置生产环境的[证书ID](#businessid)。
- 如果使用的是 Debug 环境编译，则`- application:didRegisterForRemoteNotificationsWithDeviceToken:`  回调返回的是开发环境的 token，此时 businessID 需要设置开发环境的[证书ID](#businessid)。

```
V2TIMAPNSConfig *confg = [[V2TIMAPNSConfig alloc] init];
/* 用户自己到苹果注册开发者证书，在开发者帐号中下载并生成证书(p12 文件)，将生成的 p12 文件传到腾讯证书管理控制台，控制台会自动生成一个证书 ID，将证书 ID 传入以下 busiId 参数中。*/
//推送证书 ID
confg.businessID = sdkBusiId;
confg.token = self.deviceToken;
[[V2TIMManager sharedInstance] setAPNS:confg succ:^{
     NSLog(@"%s, succ, %@", __func__, supportTPNS ? @"TPNS": @"APNS");
} fail:^(int code, NSString *msg) {
     NSLog(@"%s, fail, %d, %@", __func__, code, msg);
}];
```

### iOS 开发环境下，注册偶现不返回 deviceToken 或提示 APNs 请求 token 失败？

此问题现象是由于 APNs 服务不稳定导致的，可尝试通过以下方式解决：

1. 给手机插入 SIM 卡后使用4G网络测试。
2. 卸载重装、重启 App、关机重启后测试。
3. 打生产环境的包测试。
4. 更换其它 iOS 系统的手机测试。



## 交流与反馈

欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e2050d5b5c894c7da725f8e25c5bfe82.jpg" style="zoom:20%;" />


