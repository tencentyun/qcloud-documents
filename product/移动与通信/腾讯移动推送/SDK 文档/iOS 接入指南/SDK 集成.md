
## 简介
本文档提供关于 SDK 的接入以及开启推送服务的示例代码。（SDK 版本：V1.0+ 版本）



## SDK 组成
- doc 文件夹：腾讯移动推送 iOS SDK 开发指南。
- demo 文件夹：主要包含样例工程，腾讯移动推送 SDK。 



## 集成步骤
1. 登录 [腾讯移动推送控制台](https://console.cloud.tencent.com/tpns)，单击左侧菜单栏【产品管理】。
2. 进入产品管理页面，单击【新增产品】。
3. 进入新增产品页面，填写产品名称、产品详情，选择产品分类，单击【确定】，即可完成产品新增。
4. 产品创建完成后，选择【应用管理】>【[应用列表](https://console.cloud.tencent.com/tpns/applist)】，进入应用列表，获取产品 AppID 和 AppKey。（AppID 即 Access ID，AppKey 即 Access Key）
5. 导入 SDK：
 -  **方式一：Cocoapods 导入**
通过 Cocoapods 下载地址：
 ``` 
 pod 'TPNS-iOS' 
 ```
 - **方式二：carthage 导入**
 在 Cartfile 文件中指明依赖的第三方库：
 ```
 github "xingePush/carthage-TPNS-iOS"
 ```
 - **方式三：手动导入**
进入腾讯移动推送控制台，单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择需要下载的 SDK 版本，单击操作栏【下载】即可。
6. 打开 demo 目录下的 SDK 文件夹，将 XGPush.h及 libXG-SDK-Cloud.a 添加到工程，打开 XGPushStatistics 文件夹，获取 XGMTACloud.framework。
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
10. 添加编译参数 ```-ObjC``` 。
![](https://main.qcloudimg.com/raw/b0b74cec883f69fb0287fedc7bad4140.png)

>! 如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。

11. 调用启动腾讯移动推送的 API，并根据需要实现 ```XGPushDelegate``` 协议中的方法，开启推送服务。
	1. 启动腾讯移动推送服务， ```AppDelegate``` 示例如下：
	```objective-c
		 @interface AppDelegate () <XGPushDelegate>
		 @end

		 -(BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
				 {
						 [[XGPush defaultManager] startXGWithAppID:<#your AppID#> appKey:<#your appKey#>  delegate:<#your delegate#>];
			return YES;
				 }
	 ```
	2. 在 ```AppDelegate``` 中，选择实现 ```XGPushDelegate ``` 协议中的方法：
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
				[[XGPush defaultManager] reportXGNotificationInfo:userInfo];
				completionHandler(UIBackgroundFetchResultNewData);
		}
		// iOS 10 新增回调 API
		// App 用户点击通知
		// App 用户选择通知中的行为
		// App 用户在通知中心清除消息
		// 无论本地推送还是远程推送都会走这个回调
	#if __IPHONE_OS_VERSION_MAX_ALLOWED >= 	__IPHONE_10_0
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




## 调试方法
#### 开启 Debug 模式
打开 Debug 模式，即可在终端查看详细的腾讯移动推送 Debug 信息，方便定位问题。

#### 示例代码
```
//打开debug开关
[[XGPush defaultManager] setEnableDebug:YES];
```



#### 实现 ```XGPushDelegate``` 协议

在调试阶段，建议实现协议中的以下两个方法，即可获取更详细的调试信息：

```objective-c
/**
 @brief 监控腾讯移动推送服务地启动情况

 @param isSuccess 腾讯移动推送是否启动成功
 @param error 腾讯移动推送启动错误的信息
 */
- (void)xgPushDidFinishStart:(BOOL)isSuccess error:(nullable NSError *)error;

/**
 @brief 向腾讯移动推送服务器注册设备token的回调
 
 @param deviceToken 当前设备的token
 @param error 错误信息
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken error:(nullable NSError *)error;

```

#### 观察日志
如果 Xcode 控制台，显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[xgpush]Current device token is 80ba1c251161a397692a107f0433d7fd9eb59991583a925030f1b913625a9dab
[xgpush]Current XG token is 05da87c0ae5973bd2dfa9e08d884aada5bb2
```
>?在推送单个目标设备时请使用 XG 36位的 Token。

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


