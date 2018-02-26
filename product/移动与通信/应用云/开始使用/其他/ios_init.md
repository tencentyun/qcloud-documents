# 下载配置文件

XCode 说明

1. 下载tac_services_configurations.zip
2. 解压 tac_services_configurations.zip 后将其中文件移动到您的 XCode 项目目录下面，并将其中的plist文件添加到您的工程之中（其中 tac_services_configurations_unpackage.plist 请不要添加）

![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)



# 添加 应用云SDK 

CocoaPods 说明

应用云 服务使用 CocoaPods 安装和管理依赖项。请打开终端窗口，然后导航至应用的 Xcode 项目位置。


1. 如果您没有 Podfile，请创建一个：

	~~~
	pod init
	~~~

2. 打开 Podfile 并添加
	
	~~~
	source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
	source "https://github.com/CocoaPods/Specs"
	pod 'TACCore'
	~~~

3. 保存文件并运行

	~~~
	pod install
	~~~

此操作会为您的应用创建一个 .xcworkspace 文件。在以后开发您的应用时都要使用此文件。


# 添加初始化代码


要在应用启动时连接 应用云 平台，请在 AppDelegate 主类中添加以下初始化代码。


~~~Objective-C
#import <TACCore/TACCore.h>
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
    [TACApplication configurateWithOptions:options];
    //
    return YES;
}
~~~


~~~Swift

import TACCore
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
   
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        let options = TACApplicationOptions.default()
        TACApplication.configurate(with: options);
        return true
    }
~~~

