# MobileLine iOS 移动推送快速入门

移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入移动崩溃监测。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

为了使用移动开发平台（MobileLine）iOS 版本的 SDK，您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用


在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

> 如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。


## 第二步：添加配置文件

> 如果您已经添加过配置文件，请跳过此步。

创建好应用后，您可以点击红框中的【下载配置】来下载该应用的配置文件的压缩包：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fq0pubol92j31kw093gnw.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将改文件添加进工程中**)。 添加好配置文件后，继续点击【下一步】。


![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.plist` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。




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

添加 Podfile 依赖：

```
pod 'TACMessaging'
```



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



## 启动服务

移动推送 服务无需启动，到此您已经成功接入了 MobileLine 移动推送服务。

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
