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
### 通过 Flutter 集成，Android 端有时通知点击回调无法触发？
建议在 Flutter 一初始化即调用 `XgFlutterPlugin().addEventHandler()` 接口设置通知回调事件，以保证 App 冷启动时回调接口设置的时效性；另外请在一次 `XgFlutterPlugin().addEventHandler()` 接口调用中添加全部需要的回调，多次调用会依次覆盖，导致前序添加的回调无效。具体可参照工程目录 `example/lib/main.dart` 文件内接口调用方式。
