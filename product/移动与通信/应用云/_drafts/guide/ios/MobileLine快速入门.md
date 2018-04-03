# MobileLine iOS 快速入门

移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

为了使用移动开发平台（MobileLine）iOS 版本的 SDK，您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用

在使用我们的服务前，您必须先在 [MobileLine 控制台](https://console.cloud.tencent.com/tac) 上创建项目，每个项目下可以包含多个应用，如 iOS 或者 Android 应用，当然，您也可以在同一个项目下创建多个 iOS 或者 Android 应用。

### 创建项目

首先登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac) ，然后点击【创建第一个项目】按钮来创建一个新的项目，如图这里创建了一个名为 MyGreatApp 的项目：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newProject.png)


### 创建应用

创建好项目后，我们在 MyGreatApp 项目下创建应用，点击【创建 iOS 应用】或者【创建 Android 应用】按钮来创建应用，如图这里【创建 iOS 应用】：

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fpzgvdnbtfj31b80aoaat.jpg)

填写好 **应用名称** 和 **应用包名** 后，选择下一步。到此，您便已创建好了一个 MobileLine 项目。

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fpzgwqc45aj31bc0fb75l.jpg)

> 您可以完全按照我们控制台上的向导来集成 MobileLine SDK，控制台上默认指导您集成我们的最基本的 TACCore 模块，这是 MobileLine 中核心的基础功能，包含了应用基本数据的上报和分析。



## 第二步：添加配置文件

创建好应用后，您可以点击红框中的【tac\_services\_configurations.zip】来下载该应用的配置文件的压缩包：

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fpzgxkxz3sj31c40pgn7m.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将改文件添加进工程中**)。 添加好配置文件后，继续点击【下一步】。

> 切记**不要**将文件 `tac_service_configurations_unpackage.plist` 添加进工程，文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。



## 第三步：集成 SDK

每一个 MobileLine 服务都是一个单独的 SDK，其中 `TACCore` 是其他所有模块的基础模块，因此您必须至少将 `analytics` 模块集成到您的 app 中，下表展示了 MobileLine 各种服务所对应的库。


以下库分别对应各种移动开发平台（MobileLine）的功能。

| cocoapods | 服务名称 | 功能 |
|:----|:-----------|:-----------|
|  TACCore   |  analytics | 分析 |
|  TACMessaging |  messaging | 推送 |
|  TACCrash   |  crash     | 异常上报 |
|  TACStorage   |  storage   | Cloud Storage |
|  TACAuthorization   |  social | 第三方登录与授权（QQ、WeChat） |
|  TACPayment   |  payment | 支付 |

添加好配置文件并点击【下一步】后，向导如图所示：

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fpzh1nijelj30x21djaky.jpg)




如果还没有 Podfile，请创建一个。

~~~
$ cd your-project directory
$ pod init
~~~

并在您的 Podfile 文件中添加移动开发平台（MobileLine）的私有源：

~~~
source "https://git.cloud.tencent.com/qcloud_u/cocopoads-repo"
source "https://github.com/CocoaPods/Specs"
~~~

如果您想集成我们的各种服务，那么您只需要在 Podfile 中添加对应的服务依赖即可：

```
pod 'TACCore'
```

如果您想集成 `messaging` 服务：

```
pod 'TACMessaging'
```

如果您想同时集成 `messaging` 和 `crash` 服务：

```
pod 'TACMessaging'
pod 'TACCrash'
```

> 控制台向导上默认您只集成最基础的 `analytics` 服务。


### 配置程序需要脚本

为了极致的简化 SDK 的接入流程，我们使用 shell 脚本，帮助您自动化的去执行一些繁琐的操作，比如 crash 自动上报，在 Info.plist 里面注册各种第三方 SDK 的回调 scheme。因而，需要您添加以下脚本来使用我们自动化的加入流程。

脚本主要包括两个：

1. 在构建之前运行的脚本，该类型的脚本会修改一些程序的配置信息，比如在 Info.plist 里面增加 qqwallet 的 scheme 回调。
2. 在构建之后运行的脚本，该类型的脚本在执行结束后做一些动作，比如 Crash 符号表上报。

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


## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。整个初始化的过程很简单。

### 步骤 1 在 UIApplicationDelegate 子类中导入移动开发平台（MobileLine）模块。

Objective-C 代码示例：

~~~
#import <TACCore/TACCore.h>
~~~
Swift 代码示例：

~~~
import TACCore
~~~


### 步骤 2 配置一个 TACApplication 共享实例，通常是在应用的 `application:didFinishLaunchingWithOptions:` 方法中配置。


######  使用默认配置

通常对于移动开发平台（MobileLine）的项目他的配置信息都是通过读取 tac_services_configuration.plist 文件来获取的。

Objective-C 代码示例：

~~~
    [TACApplication configurate];
~~~

Swift 代码示例：

~~~
	TACApplication.configurate();
~~~




###### 通过编程的方式自定义某些参数

但是，您可能也有需求在程序运行时，去改变一些特定的参数来改变程序的行为。为了支持您的这种需求，我们增加了修改程序配置的接口，您可以仿照如下形式来修改移动开发平台（MobileLine）的配置。

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


最后点击【完成】，到此您已经成功接入了 MobileLine 服务。

## 后续步骤

### 了解 MobileLine：

- 查看 [MoblieLine 应用示例](https://github.com/tencentyun/qcloud-sdk-ios-samples/tree/master/MobileLineDemo)

### 向您的应用添加 MobileLine 功能：

- 借助 [Analytics](https://cloud.tencent.com/document/product/666/14822) 深入分析用户行为。
- 借助 [messaging](https://cloud.tencent.com/document/product/666/14826) 向用户发送通知。
- 借助 [crash](https://cloud.tencent.com/document/product/666/14824) 确定应用崩溃的时间和原因。
- 借助 [storage](https://cloud.tencent.com/document/product/666/14828) 存储和访问用户生成的内容（如照片或视频）。
- 借助 [authorization](https://cloud.tencent.com/document/product/666/14830) 来进行用户身份验证。
- 借助 [payment](https://cloud.tencent.com/document/product/666/14832) 获取微信和手 Q 支付能力
