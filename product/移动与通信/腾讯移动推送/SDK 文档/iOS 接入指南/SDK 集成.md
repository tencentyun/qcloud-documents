## 简介
本文档提供关于 SDK 接入以及开启推送服务的示例代码（SDK 版本：V1.0+ 版本）。

>! 为了避免您的 App 被监管部门通报或下架，请您在接入 SDK 之前务必按照 [iOS 合规指南](https://cloud.tencent.com/document/product/548/57362) 在《隐私政策》中增加 TPNS 相关说明，并且在用户同意《隐私政策》后再初始化 TPNS SDK。
>

## SDK 组成
- doc 文件夹：腾讯移动推送 iOS SDK 开发指南。
- demo 文件夹：包含样例工程，腾讯移动推送 SDK（仅包含 OC demo，Swift Demo 请前往 [腾讯工蜂](https://git.code.tencent.com/tpns/XG-Demo-Swift) 进行下载）。 

## SDK 集成
### 接入前准备
1. 接入 SDK 之前，请前往移动推送 TPNS  [控制台](https://console.cloud.tencent.com/tpns) 创建产品和 iOS 应用，详细操作可参考 [创建产品和应用](https://cloud.tencent.com/document/product/548/37241)。
   ![](https://main.qcloudimg.com/raw/47d9802945ecc9d4c84a2c1f3d45d40b.png)
2. 单击【配置管理】，进入管理页面。
   ![](https://main.qcloudimg.com/raw/30da757263936244ba3967f280202ab9.png)
3. 单击【上传证书】，完成上传操作。推送证书获取详情请参考 [证书获取指引](https://cloud.tencent.com/document/product/548/36664)。
   ![](https://main.qcloudimg.com/raw/c4eaeb3f2d9c3fbb42dbb75f2c5c12dc.png)
4. 证书上传成功后，在应用信息栏中，获取应用 Access ID 和 Access KEY。

### 导入 SDK（二选一）
#### 方式一：Cocoapods 导入
通过 Cocoapods 下载地址：
``` 
pod 'TPNS-iOS', '~> 版本'  // 如果不指定版本则默认为本地 pod TPNS-iOS 最新版本
```
>?
> - 首次下载需要登录 [仓库地址](https://git.code.tencent.com/users/sign_in)，并在【账户】菜单栏中 [设置用户名和密码](https://code.tencent.com/help/productionDoc/profile#password)。设置成功后，在 Terminal 输入对应的用户名和密码，后续即可正常使用，当前 PC 不需要再次登录。
> - 由于仓库地址变更，如果 pod 提示 `Unable to find a specification for 'TPNS-iOS'`，那么需要执行以下命令，并更新仓库确认版本：
>	``` 
	pod repo update
	pod search TPNS-iOS
	pod install //安装 SDK 
``` 

#### 方式二：手动导入
1. 进入腾讯移动推送 [控制台](https://console.cloud.tencent.com/tpns)，单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择需要下载的 SDK 版本，单击操作栏中【下载】即可。
2. 打开 demo 目录下的 SDK 文件夹，将 XGPush.h 及 libXG-SDK-Cloud.a 添加到工程，打开 XGPushStatistics 文件夹，获取 XGMTACloud.framework。
3. 将 InAppMessage 文件夹导入到工程并在【Build Setting】>【Framework Search Paths】 添加查找路径（若您 SDK 版本低于1.2.8.0，则可以忽略此步骤）。
4. 在 Build Phases 下，添加以下 Framework：
 ```
 * XGInAppMessage.framework
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
5. 添加完成后，库的引用如下：
![](https://main.qcloudimg.com/raw/34383748ef77f8e5026d3cb30eb829e4.png)


### 工程配置
1. 在工程配置和后台模式中打开推送，如下图所示：
![](https://main.qcloudimg.com/raw/549acb8c1cf61c1d2f41de4762baf47b.png)
1.1 如需使用 iOS15 新增的"时效性通知功能"，请在`Capabilities`中开启`Time Sensitive Notifications`
![](https://qcloudimg.tencent-cloud.cn/raw/f07a8d6912cc85830a99358dcf66d28a.png)
2. 添加编译参数 `-ObjC` 。
![](https://main.qcloudimg.com/raw/b0b74cec883f69fb0287fedc7bad4140.png)
如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。
>! 如果您的应用服务接入点为广州，SDK 默认实现该配置，广州域名为 `tpns.tencent.com`。
>

如果您的应用服务接入点为上海、新加坡或者中国香港，请按照下文步骤完成其他服务接入点域名配置。
1. 解压 SDK 文件包，将 SDK 目录下的 XGPushPrivate.h 文件添加到工程中。
2. 在`startXGWithAccessID:accessKey:delegate:`方法之前调用头文件中的配置`域名`接口：

如需接入上海服务接入点，则将域名设置为 `tpns.sh.tencent.com`。
**示例**
``` object-c
/// @note TPNS SDK1.2.7.1+
[[XGPush defaultManager] configureClusterDomainName:@"tpns.sh.tencent.com"];
```
如需接入新加坡服务接入点，则将域名设置为 `tpns.sgp.tencent.com`。
**示例**
``` object-c
/// @note TPNS SDK1.2.7.1+
[[XGPush defaultManager] configureClusterDomainName:@"tpns.sgp.tencent.com"];
```
如需接入中国香港服务接入点，则将域名设置为 `tpns.hk.tencent.com`。
**示例**
``` object-c
/// @note TPNS SDK1.2.7.1+
[[XGPush defaultManager] configureClusterDomainName:@"tpns.hk.tencent.com"];
```
如需接入中国广州服务接入点，则将域名设置为 `tpns.tencent.com`。
**示例**
```
/// @note TPNS SDK1.2.7.1+
[[XGPush defaultManager] configureClusterDomainName:@"tpns.tencent.com"];
```



### 接入样例
调用启动腾讯移动推送的 API，并根据需要实现 `XGPushDelegate` 协议中的方法，开启推送服务。
1. 启动腾讯移动推送服务， `AppDelegate` 示例如下：

```Objective-C
@interface AppDelegate () <XGPushDelegate>
@end 
/**
@param AccessID  通过 TPNS 管理台申请的 AccessID
@param AccessKey  通过 TPNS 管理台申请的 AccessKey
@param delegate 回调对象
**/
-(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{
  [[XGPush defaultManager] startXGWithAccessID:<your AccessID> accessKey:<your AccessKey> delegate:self];
return YES;
}
```

2. 在 `AppDelegate` 中，选择实现 `XGPushDelegate ` 协议中的方法：

```objective-c
/// 统一接收消息的回调
/// @param notification 消息对象(有2种类型NSDictionary和UNNotification具体解析参考示例代码)
/// @note 此回调为前台收到通知消息及所有状态下收到静默消息的回调（消息点击需使用统一点击回调）
/// 区分消息类型说明：xg字段里的msgtype为1则代表通知消息msgtype为2则代表静默消息
- (void)xgPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(NSUInteger))completionHandler{
 /// code
} 
 /// 统一点击回调
/// @param response 如果iOS 10+/macOS 10.14+则为UNNotificationResponse，低于目标版本则为NSDictionary
- (void)xgPushDidReceiveNotificationResponse:(nonnull id)response withCompletionHandler:(nonnull void (^)(void))completionHandler {
  /// code
}
```

## 通知服务扩展插件集成
SDK 提供了 Service Extension 接口，可供客户端调用，从而可以使用以下扩展功能：
- 精准统计 APNs 通道消息抵达。
- 接收 APNs 通道图片、音视频富媒体消息。

接入步骤请参考文档 [通知服务扩展的使用说明](https://cloud.tencent.com/document/product/548/36667)。
>!如果未集成此接口，则无法统计 APNs 通道“抵达数”。


未集成通知服务扩展插件：
![](https://main.qcloudimg.com/raw/79c01ccaffca8be63341b18ad48ea9a7.png)

集成通知服务扩展插件后：
![](https://main.qcloudimg.com/raw/9930f71a63d23b2da0c86b023f8e769f.png)


## 调试方法
#### 开启 Debug 模式
打开 Debug 模式，即可在终端查看详细的腾讯移动推送 Debug 信息，方便定位问题。

#### 示例代码
```
//打开 debug 开关
[[XGPush defaultManager] setEnableDebug:YES];
```

#### 实现 `XGPushDelegate` 协议
在调试阶段建议实现协议中的此方法，即可获取更详细的调试信息：
```objective-c
/**
@brief 注册推送服务回调
@param deviceToken APNs 生成的 Device Token
@param xgToken TPNS 生成的 Token，推送消息时需要使用此值。TPNS 维护此值与 APNs 的 Device Token 的映射关系
@param error 错误信息，若 error 为 nil 则注册推送服务成功
@note TPNS SDK1.2.6.0+
*/
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken xgToken:(nullable NSString *)xgToken error:(nullable NSError *)error;

/// 注册推送服务失败回调
/// @param error 注册失败错误信息
/// @note TPNS SDK1.2.7.1+
- (void)xgPushDidFailToRegisterDeviceTokenWithError:(nullable NSError *)error {
}
```

#### 观察日志
如果 Xcode 控制台，显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[TPNS] Current device token is 9298da5605c3b242261b57****376e409f826c2caf87aa0e6112f944
[TPNS] Current TPNS token is 00c30e0aeddff1270d8****dc594606dc184  
```
>!在推送单个目标设备时请使用 TPNS 36位的 Token。

## 统一接收消息及点击消息回调说明
TPNS 及 APNs 通道统一接收消息回调，当应用在前台收到通知消息，以及所有状态（前台、后台、关闭）下收到静默消息会走此回调。
```objective-c
- (void)xgPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(NSUInteger))completionHandler;
```
>?
- 当应用在前台收到通知消息以及所有状态下收到静默消息时，会触发统一接收消息回调 xgPushDidReceiveRemoteNotification。
区分前台收到通知消息和静默消息示例代码如下：
```
NSDictionary *tpnsInfo = notificationDic[@"xg"];
NSNumber *msgType = tpnsInfo[@"msgtype"];
if (msgType.integerValue == 1) {
        /// 前台收到通知消息
    } else if (msgType.integerValue == 2) {
        /// 收到静默消息
    } else if (msgType.integerValue == 9) {
        /// 收到本地通知（TPNS本地通知）
    }
```

统一点击消息回调，此回调方法为应用所有状态（前台、后台、关闭）下的通知消息点击回调。
```objective-c
/// 统一点击回调
/// @param response 如果 iOS 10+/macOS 10.14+ 则为 UNNotificationResponse，低于目标版本则为 NSDictionary
/// @note TPNS SDK1.2.7.1+
- (void)xgPushDidReceiveNotificationResponse:(nonnull id)response withCompletionHandler:(nonnull void (^)(void))completionHandler;
```

>!
>- TPNS 统一消息回调 `xgPushDidReceiveRemoteNotification` 会处理消息接收，并自动后续调用 `application:didReceiveRemoteNotification:fetchCompletionHandler` 方法。然而，该方法也可能被其他 SDK 也进行 hook 调用。
- 如果您只集成了 TPNS 推送平台，我们不推荐再去实现系统通知回调方法，请统一在 TPNS 通知回调中进行处理。
- 如果您集成了多推送平台，并且需要在 `application:didReceiveRemoteNotification:fetchCompletionHandler` 方法处理其他推送平台的业务，请参照如下指引，避免业务重复：
 - 您需要区分平台消息，在两个消息回调方法中分别拿到消息字典后通过“xg”字段来区分是否是 TPNS 平台的消息，如果是 TPNS 的消息则在 `xgPushDidReceiveRemoteNotification` 方法进行处理，非 TPNS 消息请统一在 `application:didReceiveRemoteNotification:fetchCompletionHandler` 方法处理
 - `xgPushDidReceiveRemoteNotification` 和 `application:didReceiveRemoteNotification:fetchCompletionHandler` 如果都执行，总共只需要调用一次 `completionHandler`。如果其他 SDK 也调用 `completionHandler`，确保整体的 `completionHandler` 只调用一次。这样可以防止由于多次 `completionHandler` 而引起的 crash。




## 高级配置（可选）

<span id="QHToken"></span>
### 获取 TPNS Token 交互建议
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示 TPNS Token，控制台和 Restful API 推送需要根据 TPNS Token 进行 Token 推送，后续问题排查也需要根据 TPNS Token 进行定位。

#### 示例代码
```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
```
![](https://main.qcloudimg.com/raw/f6ff84d3a50630bb4e8a0ab6fd090798.png)

### 获取 "TPNS运行日志" 交互建议
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示"TPNS运行日志"，方便后续问题排查。

效果如下图所示：
![](https://main.qcloudimg.com/raw/8eaaba4bedf0a541ed7f077d2e374ca3.png)![](https://main.qcloudimg.com/raw/5c28586161aefb3c47c5cdb7e23ed57b.png)
#### 示例代码
```objective-c
[[XGPush defaultManager] uploadLogCompletionHandler:^(BOOL result, NSString * _Nullable errorMessage) {
NSString *title = result ? NSLocalizedString(@"report_log_info", nil) : NSLocalizedString(@"failed", nil);
if (result && errorMessage.length>0) {
UIPasteboard *pasteboard = [UIPasteboardgeneralPasteboard];
pasteboard.string = errorMessage;
}
[TPNSCommonMethodshowAlert:title message:errorMessage viewController:selfcompletion:nil];
}];

```


### 隐私协议声明建议

您可在申请 App 权限使用时，使用以下内容声明授权的用途：

<pre>
我们使用 <a href="https://cloud.tencent.com/product/tpns">腾讯云移动推送 TPNS</a> 用于实现产品信息的推送，在您授权我们“访问网络连接”和“访问网络状态”权限后，表示您同意 <a href="https://cloud.tencent.com/document/product/548/50955">腾讯 SDK 隐私协议</a>。您可以通过关闭终端设备中的通知选项来拒绝接受此 SDK 推送服务。
</pre>

其中上述声明授权的两个链接如下：
- 腾讯云移动推送 TPNS ：`https://cloud.tencent.com/product/tpns`
- 腾讯 SDK 隐私协议：`https://cloud.tencent.com/document/product/548/50955`

