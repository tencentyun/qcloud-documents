# MobileLine iOS 移动分析快速入门

移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

为了使用移动开发平台（MobileLine）iOS 版本的 SDK，您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用


在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

>**注意：**
>如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。


## 第二步：添加配置文件

创建好应用后，您可以点击红框中的【下载配置】来下载该应用的配置文件的压缩包：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fq0pubol92j31kw093gnw.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将改文件添加进工程中**)。 添加好配置文件后，继续点击【下一步】。


![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)

> **注意：**
>请您按照图示来添加配置文件， `tac_service_configurations_unpackage.plist`文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK


>**注意：** 
>无论您使用哪种代码集成方式，都请**配置程序需要脚本**。
>如果您选择手工集成，则需要先下载移动开发平台（MobileLine）所需要的 [SDK 集合文件](http://ios-release-1253960454.cossh.myqcloud.com/tac.zip)，并仔细阅读文件中的 Readme.md 文档。

每一个 MobileLine 服务都是一个单独的 SDK，其中 `TACCore` 是其他所有模块的基础模块，因此您必须至少将 `analytics` 模块集成到您的 app 中，下表展示了 MobileLine 各种服务所对应的库。


以下库分别对应各种移动开发平台（MobileLine）的功能。

| 功能 | cocoapods | 服务名称 |
|:----|:-----------|:-----------|
| 腾讯移动分析（MTA） |  TACCore   |  analytics|
| 腾讯移动推送（信鸽）|  TACMessaging |  messaging  |
| 腾讯崩溃服务（bugly）|  TACCrash   |  crash      |
| 移动存储（Storage） |  TACStorage   |  storage   |
| 授权（Authorization）|  TACAuthorization   |  social  |
| 腾讯计费（米大师）|  TACPayment   |  payment  |


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

>**注意：**
> 控制台向导上默认您只集成最基础的 `analytics` 服务。


到此您已经成功接入了移动分析服务。


### 调试时验证服务是否正常

#### 开启实时上报
Analytics 服务默认采用批量上报策略，在本地缓存事件到达一定数量之后才能集中上报。如果您在调试时，希望每个事件都独立上报，从而能在控制台实时看到手机的上报事件，可以通过下面的方式开启实时上报：

Objective-C 代码示例：
~~~
TACApplicationOptions* options = [TACApplicationOptions defaultApplicationOptions];
options.analyticsOptions.strategy = TACAnalyticsStrategyInstant;
[TACApplication configurateWithOptions:options];
~~~

Swift 代码示例：

~~~
let options = TACApplicationOptions.default();
options?.analyticsOptions.strategy = TACAnalyticsStrategy.instant;
TACApplication.configurate(with: options);
~~~

> **注意：** 
> 由于每次上报都会建立网络连接，会增加手机流量，也会损耗手机电量，影响终端体验，因此建议您在 release 模式下关闭实时上报，采用默认的批量上报策略。

### 启动服务

移动分析服务无需手动启动，到此您已经成功接入了 MobileLine 移动分析服务。


### 验证服务数据

#### 1. 查看服务启动情况

app 启动后，您可以从 Console 中看到服务的启动日志：

~~~
2018-04-20 15:08:51.699182+0800 TACSamples[305:16243] [Info]Analytics服务启动...
~~~


#### 2. 控制台查看数据

打开 MobileLine 的[控制台](https://console.cloud.tencent.com/tac)，在移动分析的实时数据里面，您可以看到页面访问的数据，如下图：

![](http://tacimg-1253960454.file.myqcloud.com/guides/%E6%8E%A7%E5%88%B6%E5%8F%B0-%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE.png)



## 后续步骤

### 了解 MobileLine

- 查看 [MoblieLine 应用示例](https://ios-release-1253960454.cos.ap-shanghai.myqcloud.com/tac.zip)

### 向您的应用添加 MobileLine 功能

- 借助 [Analytics](https://cloud.tencent.com/document/product/666/14822) 深入分析用户行为。
- 借助 [messaging](https://cloud.tencent.com/document/product/666/14826) 向用户发送通知。
- 借助 [crash](https://cloud.tencent.com/document/product/666/14824) 确定应用崩溃的时间和原因。
- 借助 [storage](https://cloud.tencent.com/document/product/666/14828) 存储和访问用户生成的内容（如照片或视频）。
- 借助 [authorization](https://cloud.tencent.com/document/product/666/14830) 来进行用户身份验证。
- 借助 [payment](https://cloud.tencent.com/document/product/666/14832) 获取微信和手 Q 支付能力
