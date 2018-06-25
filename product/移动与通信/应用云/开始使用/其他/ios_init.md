# 下载配置文件

XCode 说明

1. 下载tac_services_configurations.zip
2. 解压 tac_services_configurations.zip 后将其中文件移动到您的 XCode 项目目录下面，并将其中的plist文件添加到您的工程之中（其中 tac_services_configurations_unpackage.plist 请不要添加）

![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)



# 添加 移动开发平台SDK 

CocoaPods 说明

MobileLine移动开发平台的 服务使用 CocoaPods 安装和管理依赖项。请打开终端窗口，然后导航至应用的 Xcode 项目位置。具体配置可以参考[TAC使用入门](https://cloud.tencent.com/document/product/666/14306?!preview&lang=cn)


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

4. 配置项目脚本程序

![](https://ws1.sinaimg.cn/large/006tNc79ly1fnttw83xayj317i0ro44j.jpg)

>  添加构建之前运行的脚本

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before
> **注意：**
请确保该脚本在 `Build Phases` 中排序为第二。
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

  ~~~
  ${PODS_ROOT}/TACCore/Scripts/tac.run.all.before.sh
  ~~~

##### 添加构建之后运行的脚本

按照上述步骤，再次添加构建后运行的脚本，

> **注意：**
请确保该脚本在 `Build Phases` 中排序为最后。

  ~~~
  ${PODS_ROOT}/TACCore/Scripts/tac.run.all.after.sh
  ~~~

##### 手动集成说明

SDK 可以手动下载集成：[tac.zip](https://ios-release-1253960454.file.myqcloud.com/tac.zip)

# 添加初始化代码


要在应用启动时连接 MobileLine 移动开发平台，请在 AppDelegate 主类中添加以下初始化代码。


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

