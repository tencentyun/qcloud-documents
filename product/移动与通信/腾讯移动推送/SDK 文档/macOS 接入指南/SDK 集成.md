
## 操作场景
本文档提供关于 SDK 接入以及开启推送服务的示例代码。

## SDK 组成
- doc 文件夹：移动推送 TPNS  macOS SDK 开发指南。
- demo 文件夹：主要包含样例工程，移动推送 TPNS  SDK。

## 集成步骤
### 接入前准备
1. 登录 [移动推送 TPNS 控制台](https://console.cloud.tencent.com/tpns)，单击左侧菜单栏【产品管理】。
2. 进入产品管理页面，单击【新增产品】。
3. 进入新增产品页面，填写产品名称、产品详情，选择产品分类，单击【确定】，即可完成产品新增。
4. 产品创建完成后，选择左侧菜单【配置管理】>【基础配置】，在应用信息一栏中获取应用`AccessID` 和 `AccessKEY`。

### 导入 SDK（二选一）
- **方式一：Cocoapods 导入**
通过 Cocoapods 下载地址：
``` 
pod 'TPNS-macOS' 
```
- **方式二：手动导入**
进入控制台，单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择 macOS 平台，在其操作栏下单击【下载】即可导入。
 1. 打开 demo 目录下的 XG-Demo-macOS 文件夹，将 XG_SDK_Cloud_macOS.framework 及 XGMTACloud_macOS.framework 添加到工程。
 2. 在 Build Phases 下添加以下 Framework：
```
 * XG_SDK_Cloud_macOS.framework
     * XGMTACloud_macOS.framework
       * UserNotifications.framework(10.14+)
```
 3. 添加完成以后，`TARGETS->General->Frameworks,Libraries,and Embedded Content`选项下Embed选择Embed&Sign 如下图：
![](https://main.qcloudimg.com/raw/f6d34ba35e5cb1dd54c9c2e1767c7891.png)

### 工程配置
1. 在工程配置中打开推送，如下图： 
![](https://main.qcloudimg.com/raw/787203b758d7f4bcea593271858d0f3a.png)
2. 在 `Build Settings->Other Linker Flags`添加编译参数 `-ObjC`。 
![](https://main.qcloudimg.com/raw/bb61982f2959bea32f43c1fd849f5e43.png)

>! 如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。
>

### 接入样例
调用启动移动推送 TPNS 的 API，并根据需要实现 XGPushDelegate 协议中的方法，开启推送服务。
1. 启动移动推送 TPNS 服务，以下是在 AppDelegate 中做演示：
```objective-c
- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    /// 打开 Debug 模式，即可在终端查看详细的移动推送 TPNS Debug 信息，方便定位问题。
//    [[XGPush defaultManager] setEnableDebug:YES];
    [XGPush defaultManager].launchOptions = [[aNotification userInfo] mutableCopy];
    [[XGPush defaultManager] startXGWithAccessID:TPNS_ACCESS_ID accessKey:TPNS_ACCESS_KEY delegate:self];
}
```
2. 在 `AppDelegate`中选择实现 `XGPushDelegate ` 协议中的方法：
```objective-c
/// 注册推送服务成功回调
/// @param deviceToken APNs 生成的Device Token
/// @param xgToken TPNS 生成的 Token，推送消息时需要使用此值。TPNS 维护此值与APNs 的 Device Token的映射关系
/// @param error 错误信息，若error为nil则注册推送服务成功
- (void)xgPushDidRegisteredDeviceToken:(NSString *)deviceToken xgToken:(NSString *)xgToken error:(NSError *)error {
    if (!error) {
        NSLog(@"%s, register success, deviceToken:%@, xgToken:%@", __FUNCTION__, deviceToken, xgToken);
    } else {
        NSLog(@"%s, register failed:%@, deviceToken:%@, xgToken:%@", __FUNCTION__,error.description, deviceToken, xgToken);
    }
}

/// 统一收到通知消息的回调
/// @param notification 消息对象
/// @param completionHandler 完成回调
/// 区分消息类型说明：xg字段里的msgtype为1则代表通知消息msgtype为2则代表静默消息
/// notification消息对象说明：有2种类型NSDictionary和UNNotification具体解析参考示例代码
- (void)xgPushDidReceiveRemoteNotification:(id)notification withCompletionHandler:(void (^)(NSUInteger))completionHandler {
    NSLog(@"[TPNS Demo] receive notification: %@", notification);
}

/// 统一点击回调
/// @param response 如果iOS 10+/macOS 10.14+则为UNNotificationResponse，低于目标版本则为NSDictionary
/// 区分消息类型说明：xg字段里的msgtype为1则代表通知消息,msgtype为9则代表本地通知
- (void)xgPushDidReceiveNotificationResponse:(nonnull id)response withCompletionHandler:(nonnull void (^)(void))completionHandler {
    if ([response isKindOfClass:[UNNotificationResponse class]]) {
        NSLog(@"[TPNS Demo] click notification: %@", ((UNNotificationResponse *)response).notification.request.content.userInfo);
    } else if ([response isKindOfClass:[NSDictionary class]]) {
        NSLog(@"[TPNS Demo] click notification: %@", response);
    }
    completionHandler();
}
```

### 观察日志

如果 Xcode 控制台显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[TPNS]  Current device token is 2117b45c7e32bcdae2939f******57e420a376bdd44cf6f58613129d2065370
[TPNS]  Current TPNS token is 0304b8f5d4e*****0af06b37d8b850d95606
[TPNS]  The server responds correctly, registering device successfully
```

<span id="QHToken"></span>
## 集成建议
#### 获取 Token （非必选）
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示 Token，该操作便于我们后续进行问题排查。

#### 示例代码
```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
//获取 APNs 生成的 DeviceToken
[[XGPushTokenManager defaultTokenManager] deviceTokenString];
```

