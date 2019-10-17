移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入移动存储服务。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作
* 您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。
* 其次您需要一个在后台搭建一个授权服务器，为SDK提供临时密钥，请参考 [用户访问控制](https://cloud.tencent.com/document/product/666/17922)。


## 第一步：创建项目和应用


在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

> 如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。


## 第二步：添加配置文件

>**注意：**
>如果您已经添加过配置文件，请跳过此步。

创建好应用后，您可以单击红框中的【下载配置】来下载该应用的配置文件的压缩包：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fq0pubol92j31kw093gnw.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将改文件添加进工程中**)。 添加好配置文件后，继续单击【下一步】。


![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)

>**注意：**
>请您按照图示来添加配置文件， `tac_service_configurations_unpackage.plist` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

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

在 Podfile 中添加依赖：

```
pod 'TACStorage'
```

### 配置程序需要脚本

> 如果您在其他模块中完成了此步骤，请不要重复执行。

为了简化 SDK 的接入流程，我们使用 shell 脚本，帮助您自动化的去执行一些繁琐的操作，比如 crash 自动上报，在 Info.plist 里面注册各种第三方 SDK 的回调 scheme。因而，需要您添加以下脚本来使用我们自动化的加入流程。

脚本主要包括两个：

- 在构建之前运行的脚本，该类型的脚本会修改一些程序的配置信息，比如在 Info.plist 里面增加 qqwallet 的 scheme 回调。
- 在构建之后运行的脚本，该类型的脚本在执行结束后做一些动作，比如 Crash 符号表上报。

![](https://ws1.sinaimg.cn/large/006tNc79ly1fnttw83xayj317i0ro44j.jpg)

请按照以下步骤来添加脚本：

##### 添加构建之前运行的脚本

1. 在导航栏中打开您的工程。
2. 打开 Tab `Build Phases`。
3. 单击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before
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
3. 单击 `Add a new build phase` , 并选择 `New Run Script Phase`，您可以将改脚本命名 TAC Run Before。
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

### 步骤 1 导入 MobileLine 模块
在 UIApplicationDelegate 子类中导入移动开发平台（MobileLine）模块。

Objective-C 代码示例：
~~~
#import <TACCore/TACCore.h>
~~~

Swift 代码示例：
~~~
import TACCore
~~~

### 步骤 2 配置 TACApplication 共享实例
配置一个 TACApplication 共享实例，通常是在应用的 `application:didFinishLaunchingWithOptions:` 方法中配置。

####  使用默认配置

通常对于移动开发平台（MobileLine）的项目他的配置信息都是通过读取 tac_services_configuration.plist 文件来获取的。

Objective-C 代码示例：
~~~
[TACApplication configurate];
~~~

Swift 代码示例：
~~~
TACApplication.configurate();
~~~

### 步骤三 配置 TACStorage 的使用权限

Storage SDK 需要一个后台授权服务器提供临时密钥，才能正常工作。关于如何在 SDK 里配置服务器接口，请参见  [iOS 配置授权服务器](https://cloud.tencent.com/document/product/666/17216)。

## 启动服务

移动存储服务无需启动，到此您已经成功接入了 MobileLine 移动存储服务。

## 后续步骤

您可以通过策略精确控制您数据的访问权限，可以参考 [数据安全性最佳实践](https://cloud.tencent.com/document/product/666/17921)。

### 了解 MobileLine：

- 查看 [MoblieLine 应用示例](https://ios-release-1253960454.cos.ap-shanghai.myqcloud.com/tac.zip)

### 向您的应用添加 MobileLine 功能：

- 借助 [Analytics](https://cloud.tencent.com/document/product/666/14822) 深入分析用户行为。
- 借助 [messaging](https://cloud.tencent.com/document/product/666/14826) 向用户发送通知。
- 借助 [crash](https://cloud.tencent.com/document/product/666/14824) 确定应用崩溃的时间和原因。
- 借助 [storage](https://cloud.tencent.com/document/product/666/14828) 存储和访问用户生成的内容（如照片或视频）。
- 借助 [authorization](https://cloud.tencent.com/document/product/666/14830) 来进行用户身份验证。
- 借助 [payment](https://cloud.tencent.com/document/product/666/14832) 获取微信和手 Q 支付能力
