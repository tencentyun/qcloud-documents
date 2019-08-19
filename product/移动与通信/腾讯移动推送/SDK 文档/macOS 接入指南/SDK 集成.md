
## 操作场景
本文档提供关于  SDK 的接入以及开启推送服务的示例代码（SDK 版本：V1.0+版本）。



## SDK 组成
- doc 文件夹：腾讯移动推送 macOS SDK 开发指南。
- demo 文件夹：主要包含样例工程，腾讯移动推送 SDK。



## 集成步骤
1. 登录腾讯移动推送控制台，单击左侧菜单栏【[产品管理](https://console.cloud.tencent.com/tpns/product)】。
2. 进入产品管理页面，单击【新增产品】。
3. 进入新增产品页面，填写产品名称、产品详情，选择产品分类，单击【确定】，即可完成产品新增。
4. 产品创建完成后，选择【应用管理】>【[应用列表](https://console.cloud.tencent.com/tpns/applist)】，进入应用列表，获取产品 AppID 和 AppKey。（AppID 即 Access ID，AppKey 即 Access Key）
5. 导入 SDK：
 - **方式一：Cocoapods 导入**
通过 Cocoapods 下载地址：
``` 
pod 'TPNS-macOS' 
```
 - **方式二：手动导入**
进入控制台，单击左侧菜单栏【[SDK 下载](https://console.cloud.tencent.com/tpns/sdkdownload)】，进入下载页面，选择 macOS 平台，在其操作栏下单击【下载】，即可导入 SDK。
6. 打开 demo 目录下的 XG-Demo-macOS 文件夹，将 XG_SDK_Cloud_macOS.framework 及 XGMTACloud_macOS.framework 添加到工程。
7. 在 Build Phases 下添加以下 Framework：
```
 * XG_SDK_Cloud_macOS.framework
 * XGMTACloud_macOS.framework
 * UserNotifications.framework(10.14+)
```
8. 添加完成以后，库的引用如下：
![](https://main.qcloudimg.com/raw/481e688090a772213ce35b15be0dbd3d.png)
9. 在工程配置和后台模式中打开推送，如下图： 
![](https://main.qcloudimg.com/raw/29eea75c08411c8666136ce3e1d8954a.png)
10. 添加编译参数 ```-ObjC```。 
![](https://main.qcloudimg.com/raw/bb61982f2959bea32f43c1fd849f5e43.png)

>!如 checkTargetOtherLinkFlagForObjc 报错，是因为 build setting 中，Other link flags 未添加 -ObjC。

11. 调用启动腾讯移动推送的 API，并根据需要实现 XGPushDelegate 协议中的方法，开启推送服务
   1. 启动腾讯移动推送服务，以下是在 AppDelegate 中做演示：
		 ```objective-c
		 @interface AppDelegate () <XGPushDelegate>
		 @end

		 -(BOOL)application:(NSApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
				 {
						 [[XGPush defaultManager] startXGWithAppID:<#your AppID#> appKey:<#your appKey#>  delegate:<#your delegate#>];
			return YES;
				 }
		 ```
   2. 在 ```AppDelegate``` 中选择实现 ```XGPushDelegate ``` 协议中的方法：
	```objective-c
		/**
		 收到推送的回调
		 @param application  NSApplication 实例
		 @param userInfo 推送时指定的参数
		 @param completionHandler 完成回调
		 */
		- (void)xgPushDidReceiveRemoteNotification:(id)notification withCompletionHandler:(void (^)(NSUInteger))completionHandler {
			NSLog(@"notificaion is %@", notification);
	}
	```


## 调试方法
#### 开启 Debug 模式
打开 Debug 模式，即可在终端查看详细的腾讯移动推送 Debug 信息，方便定位问题。

#### 代码示例

```
//打开debug开关
[[XGPush defaultManager] setEnableDebug:YES];
```


#### 实现 XGPushDelegate 协议
在调试阶段，建议实现协议中的以下两个方法，从而能得到更详细的调试信息：

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
 @note 当前的token已经注册过之后，将不会再调用此方法
 */
- (void)xgPushDidRegisteredDeviceToken:(nullable NSString *)deviceToken error:(nullable NSError *)error;

```

#### 观察日志

如果 Xcode 控制台显示如下相似日志，表明客户端已经正确集成 SDK。

```javascript
[xgpush]Current device token is ***
服务器(192.168.1.1)返回正确， 注册设备Token 成功
```



>?建议您完成 SDK 集成后，在 App 的【关于】、【意见反馈】等比较不常用的 UI 中，通过手势或者其他方式显示Token，该操作便于我们后续进行问题排查。示例代码如下：
```objective-c
//获取 TPNS 生成的 Token
[[XGPushTokenManager defaultTokenManager] xgTokenString];
//获取 APNs 生成的 DeviceToken
[[XGPushTokenManager defaultTokenManager] deviceTokenString];
```

