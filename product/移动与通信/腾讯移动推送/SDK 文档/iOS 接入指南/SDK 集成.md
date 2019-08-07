
## 简介
使用的 SDK 版本：V1.0+ 版本。



## SDK 组成
- doc 文件夹：信鸽 iOS SDK 开发指南。
- demo 文件夹：主要包含样例工程，信鸽 SDK。 



## 集成步骤
1. 登录腾讯移动推送控制台，单击左侧菜单栏【[产品管理](https://console.cloud.tencent.com/tpns/product)】。
2. 进入产品管理页面，单击【新增产品】。
3. 进入新增产品页面，填写产品名称、产品详情，选择产品分类，单击【确定】，即可完成产品新增。
4. 产品创建完成后，选择【应用管理】>【[应用列表](https://console.cloud.tencent.com/tpns/applist)】，进入应用列表，获取产品 AppID 和 AppKey。（AppID 即 Access ID，AppKey 即 Access Key）
5. 然后单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择需要下载的 SDK 版本，单击操作栏【下载】即可。
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
```
8. 添加完成后，库的引用如下：
![](https://main.qcloudimg.com/raw/e61961cd6db798d0f02d4b4c1a996fa0.png)
9. 在工程配置和后台模式中打开推送，如下图所示：
![](https://main.qcloudimg.com/raw/549acb8c1cf61c1d2f41de4762baf47b.png)
10. 添加编译参数 ```-ObjC``` 。
![](https://main.qcloudimg.com/raw/b0b74cec883f69fb0287fedc7bad4140.png)

>! 如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。

11. 调用启动信鸽的 API，并根据需要实现 ```XGPushDelegate``` 协议中的方法，开启推送服务。
	1. 启动信鸽服务， ```AppDelegate``` 示例如下：
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
打开 Debug 模式，即可在终端查看详细的信鸽 Debug 信息，方便定位问题。

#### 示例代码

```
//打开debug开关
[[XGPush defaultManager] setEnableDebug:YES];
```



#### 实现 ```XGPushDelegate``` 协议

在调试阶段，建议实现协议中的以下两个方法，即可获取更详细的调试信息：

```objective-c
/**
 @brief 监控信鸽推送服务地启动情况

 @param isSuccess 信鸽推送是否启动成功
 @param error 信鸽推送启动错误的信息
 */
- (void)xgPushDidFinishStart:(BOOL)isSuccess error:(nullable NSError *)error;

/**
 @brief 向信鸽服务器注册设备token的回调
 
 @param deviceToken 当前设备的token
 @param error 错误信息
 @note 当前的token已经注册过之后，将不会再调用此方法
 */
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken error:(nullable NSError *)error;

```

#### 观察日志
如果 Xcode 控制台，显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[xgpush]Current device token is 623e4a477abce566a74c449ae32c1ca6066fbb243e7417b3fe393811b54792eb
服务器(193.112.115.248)返回正确， 注册设备Token 成功
```





