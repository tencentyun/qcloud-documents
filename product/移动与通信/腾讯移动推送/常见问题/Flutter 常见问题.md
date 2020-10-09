### 通过 Flutter 集成，iOS 端冷启动时如何获取自定义参数？

需要在 `runner->AppDelegate->didFinishLaunchingWithOptions` 方法通过以下接口获取：
```objective-c
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{
		// 消息内容获取
		NSDictionary *remoteNotification = [launchOptions objectForKey:UIApplicationLaunchOptionsRemoteNotificationKey];
		// 然后根据消息内容进行逻辑处理
}
```
