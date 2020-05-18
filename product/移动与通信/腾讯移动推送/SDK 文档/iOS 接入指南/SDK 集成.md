
## 简介
本文档提供关于 SDK 的接入以及开启推送服务的示例代码。（SDK 版本：V1.0+ 版本）
>!如果您是从信鸽平台（https:// xg.qq.com）迁移至腾讯移动推送平台，请务必：
1.实现 [注销信鸽平台推送服务接口](#zhuxiao)。
2.参考 [iOS迁移指南](https://cloud.tencent.com/document/product/548/41610)  文档，根据您 App 的集成情况，实现相应的变更，完成后返回当前文档。
3.完成下述文档的集成工作。

## SDK 组成
- doc 文件夹：腾讯移动推送 iOS SDK 开发指南。
- demo 文件夹：主要包含样例工程，腾讯移动推送 SDK（仅包含 OC demo，Swift Demo 请前往 [腾讯工蜂](https://git.code.tencent.com/tpns/XG-Demo-Swift) 进行下载）。 



## 集成步骤
1. 登录 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns)，单击左侧菜单栏【产品管理】。
2. 进入产品管理页面，单击【新增产品】。
3. 进入新增产品页面，填写产品名称、产品详情，选择产品分类，单击【确定】，即可完成产品新增。
4. 产品创建完成后，选择左侧菜单【配置管理】，在应用信息一栏中，获取应用`Access ID` 和 `SECRET KEY`。
5. 导入 SDK：
 -  **方式一：Cocoapods 导入**
通过 Cocoapods 下载地址：
``` 
 pod 'TPNS-iOS' 
```
 >?
    - 首次下载需要登录 [仓库地址](https://git.code.tencent.com/users/sign_in)，并在【账户】菜单栏中设置账号和密码，然后在 Terminal 输入对应的账号和密码。后续即可正常使用，当前 PC 不需要再次登录。
    - 由于仓库地址变更，pod 如果提示`Unable to find a specification for 'TPNS-iOS'`，需要执行以下命令，并更新仓库确认版本：
``` 
pod repo update
pod search TPNS-iOS
pod install //安装SDK 
```  

 -  **方式二：carthage 导入**
 在 Cartfile 文件中指明依赖的第三方库：
```
 github "xingePush/carthage-TPNS-iOS"
```
 
 - **方式三：手动导入**
进入腾讯移动推送控制台，单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择需要下载的 SDK 版本，单击操作栏【下载】即可。

6. 打开 demo 目录下的 SDK 文件夹，将 XGPush.h 及 libXG-SDK-Cloud.a 添加到工程，打开 XGPushStatistics 文件夹，获取 XGMTACloud.framework。
7. 在 Build Phases 下，添加以下 Framework：
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
8. 添加完成后，库的引用如下：
![](https://main.qcloudimg.com/raw/92f32ba9287713e009988ba8ee962ec8.png)
9. 在工程配置和后台模式中打开推送，如下图所示：
![](https://main.qcloudimg.com/raw/549acb8c1cf61c1d2f41de4762baf47b.png)
10. 添加编译参数 `-ObjC` 。
![](https://main.qcloudimg.com/raw/b0b74cec883f69fb0287fedc7bad4140.png)

>! 如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。

11. 调用启动腾讯移动推送的 API，并根据需要实现 `XGPushDelegate` 协议中的方法，开启推送服务。
	1. 启动腾讯移动推送服务， `AppDelegate` 示例如下：
   ```Objective-C
@interface AppDelegate () <XGPushDelegate>
@end 
/**
@param appID  通过 TPNS 管理台申请的 AccessID
@param appKey  通过 TPNS 管理台申请的 AccessKey
@param delegate 回调对象
**/
-(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{
[[XGPush defaultManager] startXGWithAppID:<#your appID#> appKey:<#your appKey#>  delegate:<#your delegate#>];
return YES;
}
   ```
	2. 在 `AppDelegate` 中，选择实现 `XGPushDelegate ` 协议中的方法：
		```objective-c
		/// 统一收到通知消息的回调
		/// @param notification 消息对象
		/// @param completionHandler 完成回调
		/// 区分消息类型说明：xg字段里的msgtype为1则代表通知消息msgtype为2则代表静默消息
		/// notification消息对象说明：有2种类型NSDictionary和UNNotification具体解析参考示例代码
		- (void)xgPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(NSUInteger))completionHandler{
		/// code
		} 
		#if __IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_10_0
		/// iOS 10 新增 API
		/// iOS 10 会走新 API, iOS 10 以前会走到老 API
		/// App 用户点击通知和用户选择通知中的行为
		/// 无论本地推送还是远程推送都会走这个回调
		- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center
      didReceiveNotificationResponse:(UNNotificationResponse *)response
               withCompletionHandler:(void (^)(void))completionHandler {
                                                         /// code
	}
	#endif
			 ```


#### 境外集群接入方法
1. 解压 SDK 文件包，将 SDK 目录下的 XGPushPrivate.h 文件添加到工程中。
2. 调用头文件中的配置 `HOST` 接口：
 - 如需接入新加坡集群则将 `HOST`设置为 `https://api.tpns.sgp.tencent.com`, `PORT`设置为0。
 - 如需接入中国香港集群则将 `HOST` 设置为`https://api.tpns.hk.tencent.com`, `PORT `设置为0。
 
**示例**
``` object-c
[[XGPush defaultManager] configureHost:@"https://api.tpns.hk.tencent.com" port:0]
```
>?配置 `HOST` 接口需要在 `startXGWithAppID` 方法之前调用。




## 调试方法
#### 开启 Debug 模式
打开 Debug 模式，即可在终端查看详细的腾讯移动推送 Debug 信息，方便定位问题。

#### 示例代码
```
//打开debug开关
[[XGPush defaultManager] setEnableDebug:YES];
```



#### 实现 `XGPushDelegate` 协议

在调试阶段，建议实现协议中的此方法，即可获取更详细的调试信息：

```objective-c
/**
 @brief 注册推送服务回调
 @param deviceToken APNs 生成的 Device Token
 @param xgToken TPNS 生成的 Token，推送消息时需要使用此值。TPNS 维护此值与 APNs 的 Device Token 的映射关系
 @param error 错误信息，若 error 为 nil 则注册推送服务成功
 */
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken xgToken:(nullable NSString *)xgToken error:(nullable NSError *)error;
```

#### 观察日志
如果 Xcode 控制台，显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[TPNS] Current device token is 9298da5605c3b242261b57****376e409f826c2caf87aa0e6112f944
[TPNS] Current TPNS token is 00c30e0aeddff1270d8****dc594606dc184  
```
>?在推送单个目标设备时请使用 XG 36位的 Token。

## 统一接收消息及点击消息回调说明

- 高于iOS 10.0 的系统版本，点击消息，此函数将被调用.
```objective-c
	- (void)xgPushUserNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler;
```
- 低于iOS 10.0 的系统版本，点击消息，此函数将被调用：
```objective-c
	- (void)xgPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(NSUInteger))completionHandler;
```
 
- 若收到的是静默消息，此函数将被调用：
```objective-c
	- (void)xgPushDidReceiveRemoteNotification:(nonnull id)notification withCompletionHandler:(nullable void (^)(NSUInteger))completionHandler;
```

>!
- 应用在前台收到消息不管点不点击消息都会走xgPushDidReceiveRemoteNotification统一接收消息回调 
- 不建议自行实现接口application:didReceiveRemoteNotification:fetchCompletionHandler ，SDK内部已处理

<span id="zhuxiao"></span>
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
>!如果未做以上配置，则在信鸽和腾讯移动推送两个平台上同时推送时，可能会出现重复消息。

## 集成建议
#### 通知服务扩展功能（必选）
为了实现抵达数据上报和富媒体消息的功能，SDK 提供了 Service Extension 接口，可供客户端调用，从而可以监听消息的到达和发送富媒体消息，强烈建议您实现此接口，接入指南请参见 [通知服务扩展的使用说明](https://cloud.tencent.com/document/product/548/36667)。
>!如果未集成此接口，则统计数据中消息`抵达数`与`点击数`一致。

<span id="QHToken"></span>
#### 获取 Token （非必选）
建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示 Token，该操作便于我们后续进行问题排查。

#### 示例代码
```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
//获取 APNs 生成的 DeviceToken
[[XGPushTokenManager defaultTokenManager] deviceTokenString];
```

![](https://main.qcloudimg.com/raw/7afeffeac5828bb42563765e10730179.png)


