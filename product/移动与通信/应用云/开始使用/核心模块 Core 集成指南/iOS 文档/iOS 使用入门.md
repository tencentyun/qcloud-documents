
## 准备工作

为了使用移动开发平台（MobileLine） iOS 版本的 SDK，您需要一个 iOS 的工程，或者下载移动开发平台（MobileLine）的 [实例工程](https://console.cloud.tencent.com/tac)。

## 集成代码库

> 无论您使用哪种代码集成方式，都请**配置程序需要脚本**。如果您选择手工集成，则需要先从：[下载地址](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip),下载 移动开发平台（MobileLine）所需要的 SDK 集合文件。并仔细阅读文件中的 Readme.md 文档。

### 通过 CocoaPods 集成（推荐）
 
如果您是设置一个新项目，则需要安装 SDK。您可能已经在创建移动开发平台（MobileLine）项目的过程中完成此步操作。

我们 **强烈建议** 使用 CocoaPods 来安装相关的库。这样可以方便您后期 **维护** 和 **即时** 收到我们的 **SDK更新**。您可以根据 [安装说明](https://guides.cocoapods.org/using/getting-started.html#getting-started) 来安装并使用 CocoaPods 。如果您不想使用 CocoaPods ，则可以按照 **手工集成** 的方式直接集成 SDK 框架。


如果您计划下载并运行某个快速入门实例，实例中会提供 Xcode 项目和 Podfile，不过您还是需要安装 Pod 并下载  tac_services_configurations.zip ([从控制台对应的 App 下载](https://console.cloud.tencent.com/tac))文件。解压后将 tac_services_configurations.plist 文件集成进项目中。 如果您希望将移动开发平台（MobileLine）库集成至自己的某个项目中，则需要为想要使用的库添加 Pod。




#### 为新项目添加移动开发平台（MobileLine） iOS 库

##### 1. 如果没有 Xcode 项目，请新建一个。
##### 2. 如果还没有 Podfile，请创建一个。

~~~
$ cd your-project directory
$ pod init
~~~

并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

> **注意：**
> 一定要添加 [CocoaPods](https://github.com/CocoaPods/Specs) 的原始源，否则会造成部分仓库找不到的问题。

##### 3. 添加您想安装的 Pod，可以按照以下方法在 Podfile 中纳入一个 Pod。

~~~
pod 'TACCore'
~~~


这会在您的 iOS 应用中添加移动开发平台（MobileLine）正常运行所需的必备库以及 Analytics for 移动开发平台（MobileLine）功能。下面列出了目前可供使用的一系列 pod 和 subspec，在针对不同功能的设置指南中也对此给出了相应的链接。

##### 4. 安装 Pod 并打开 .xcworkspace 文件以便在 Xcode 中查看该项目。

~~~
$ pod install
$ open your-project.xcworkspace
~~~

##### 5. 从移动开发平台（MobileLine）控制台中下载一个 tac_services_configurations.zip 文件并将其添加到您的应用中。


1. tac_services_configurations.zip ([从控制台对应的 App 下载](https://console.cloud.tencent.com/tac))文件
2. 解压 tac_services_configurations.zip 后将其中文件移动到您的 XCode 项目目录下面，并将其中的plist文件添加到您的工程之中（其中 tac_services_configurations_unpackage.plist 请不要添加）

![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)



##### 6. 初始化代码

最后一步是向您的应用添加初始化代码，您可能已经在将移动开发平台（MobileLine）添加到应用时完成了此步骤。如果您使用的是快速入门示例，则此步骤已替您完成了。

###### 步骤 1 在 UIApplicationDelegate 子类中导入移动开发平台（MobileLine）模块。

Objective-C 代码示例：

~~~
#import <TACCore/TACCore.h>
~~~
Swift 代码示例：

~~~
import TACCore
~~~


###### 步骤 2 配置一个 TACApplication 共享实例，通常是在应用的 `application:didFinishLaunchingWithOptions:` 方法中配置。


####### 使用默认配置

通常对于移动开发平台（MobileLine）的项目他的配置信息都是通过读取 tac_services_configurations.zip 文件来获取的。

Objective-C 代码示例：

~~~
    [TACApplication configurate];
~~~
Swift 代码示例：

~~~
	TACApplication.configurate();
~~~
####### 需要通过编程的方式自定义某些参数

通常对于移动开发平台（MobileLine）的项目他的配置信息都是通过读取 tac_services_configurations.zip 文件来获取的。但是，您可能也有需求在程序运行时，去改变一些特定的参数来改变程序的行为。为了支持您的这种需求，我们增加了修改程序配置的接口，您可以仿照如下形式来修改移动开发平台（MobileLine）的配置。

Objective-C 代码示例：

~~~
    TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
	// 自定义配置
	// opions.xxx= xxx
    //
    [TACApplication configurateWithOptions:options];
~~~
Swift 代码示例：
~~~
	let options = TACApplicationOptions.default()
	// 自定义配置
	// opions.xxx= xxx
	TACApplication.configurate(with: options);
~~~



## 配置程序需要脚本

为了极致的简化 SDK 的接入流程我们，使用 shell 脚本，帮助您自动化的去执行一些繁琐的操作，比如 crash 自动上报，在 Info.plist 里面注册各种第三方 SDK 的回调 scheme。因而，需要您添加以下脚本来使用我们自动化的加入流程。

脚本主要包括两个：
 
- 在构建之前运行的脚本，该类型的脚本会修改一些程序的配置信息，比如在 Info.plist 里面增加 qqwallet 的 scheme 回调。
- 在构建之后运行的脚本，该类型的脚本在执行结束后做一些动作，比如 Crash 符号表上报。

![](https://ws1.sinaimg.cn/large/006tNc79ly1fnttw83xayj317i0ro44j.jpg)

请按照以下步骤来添加脚本：

##### 添加构建之前运行的脚本

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before
> **注意：**
请确保该脚本在 `Build Phases` 中排序为第二。
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

需要黏贴的代码

~~~
#export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.before.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
${TAC_CORE_FRAMEWORK_PATH}/Scripts/tac.run.all.before.sh
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：
 
* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACCore`，您需要黏贴的代码实例如下：

  ~~~
  ${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.before.sh
  ~~~

* 如果您使用手工集成的方式则为 `您存储 TACCore 库的地址`，即您 TACCore framework 的引入路径，您需要黏贴的代码实例如下：

  ~~~
   export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
   [您存储 TACCore 库的地址]/TACCore.framework/Scripts/tac.run.all.before.sh
  ~~~




##### 添加构建之后运行的脚本


1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 点击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before。
> **注意：**
>  请确保该脚本在 `Build Phases` 中排序需要放到最后。
4. 根据自己集成的模块和集成方式将代码粘贴入  `Type a script...` 文本框:。

需要黏贴的代码

~~~
#export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
${TAC_CORE_FRAMEWORK_PATH}/Scripts/tac.run.all.after.sh
~~~

其中 `THIRD_FRAMEWORK_PATH` 变量的取值根据您的安装方式而不同：
 
* 如果您使用 Cocoapods 来集成的则为 `${PODS_ROOT}/TACCore`，您需要黏贴的代码实例如下：

  ~~~
  ${SRCROOT}/Pods/TACCore/Scripts/tac.run.all.after.sh
  ~~~

* 如果您使用手工集成的方式则为 `[您存储 TACCore 库的地址]`，即您 TACCore framework 的引入路径，您需要黏贴的代码实例如下：

  ~~~
  #export TAC_SCRIPTS_BASE_PATH=[自定义执行脚本查找路径，我们会在该路径下寻找所有以“tac.run.all.after.sh”命名的脚本，并执行，如果您不需要自定义不用动这里]
  [您存储 TACCore 库的地址]/TACCore.framework/Scripts/tac.run.all.after.sh
  ~~~
