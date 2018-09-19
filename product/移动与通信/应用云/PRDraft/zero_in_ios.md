# 零代码三步快速集成腾讯移动分析（MTA）（iOS）


先来段正式的产品介绍：

腾讯移动分析有专业的移动应用数据分析能力，为您的应用提供实时数据统计分析服务，监控版本质量、渠道状况、用户画像属性及用户细分行为，通过数据可视化展现，协助产品运营决策。

说得简单点，就是几点

1. 有很强大的实时处理能力，你只要上报了，可以实时看到新增用户，活跃用户
2. 多维度的数据分析，从用户角度，渠道，版本等多角度对数据进行汇总分析
3. 支持自定义事件模型，也就是特殊需求你自己上报，移动分析帮你统计
4. 强大的用户挖掘能力，利用腾讯的数据，来标记你的用户是男是女等等

实际上，接入腾讯移动分析非常简单，快速搞定。

## 准备工作

您首先需要一个 iOS 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。



## 第一步：创建项目和应用


在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

![应用创建](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/project/application_create.jpg)

## 第二步：添加配置文件

创建好应用后，您可以点击红框中的【下载配置】来下载该应用的配置文件的压缩包：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fq0pubol92j31kw093gnw.jpg)

解压后将 tac_services_configurations.plist 文件集成进项目中。其中有一个  tac_services_configurations_unpackage.plist 文件，请将该文件放到您工程的根目录下面(**切记不要将改文件添加进工程中**)。 添加好配置文件后，继续点击【下一步】。


![](https://ws1.sinaimg.cn/large/006tNc79gy1forbnw3ijyj31bi11wnch.jpg)

> **注意：**
>请您按照图示来添加配置文件， `tac_service_configurations_unpackage.plist`文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


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

如果您想集成我们的各种服务，那么您只需要在 Podfile 中添加对应的服务依赖即可：

```
pod 'TACCore'
```

> TACCore 中默认包含了移动分析服务

**移动分析服务无需手动启动，到此您已经成功接入了 MobileLine 移动分析服务。**


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




### 验证服务数据

#### 1. 查看服务启动情况

app 启动后，您可以从 Console 中看到服务的启动日志：

~~~
2018-04-20 15:08:51.699182+0800 TACSamples[305:16243] [Info]Analytics服务启动...
~~~


#### 2. 控制台查看数据

打开 MobileLine 的[控制台](https://console.cloud.tencent.com/tac)，在移动分析的实时数据里面，您可以看到页面访问的数据，如下图：

![](http://tacimg-1253960454.file.myqcloud.com/guides/%E6%8E%A7%E5%88%B6%E5%8F%B0-%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE.png)


## 写在最后


对于小型开发团队而言，如何快速地构建、开发出一款功能齐全的应用在市场上是至关重要的。对于现在APP的许多基础能力，例如用户使用数据统计、推送、存储、异常检测和支付服务等都得要有，作为小型开发团队而言，自己开发这些功能相当费时费力，大多数还需有后台服务器的支撑，质量也没有云服务厂商提供的好，首选当然就是选择第三方提供的服务了。

不过使用第三方服务以后，还是会存在一定的问题。对于不同的能力，移动端上面需要集成不同的 SDK 一方面学习成本较高，因为不同的 SDK 代码和接口风格肯定不一样，配置和调用方式也千差万别，了解如何集成和使用相当费时间，集成的成本主要在学习成本上了。并且对于不同的第三方 SDK 而言，开发时一般较少考虑和其它 SDK 的兼容性，有时候两个 SDK 内部使用了同一个库或者需要对某个编译选项进行修改，影响到整体的集成流程。

考虑到上面的问题以后，发现 MobilieLine 可以较好的解决这些问题。经过封装以后，对外的接口风格都是一致的，配置过程也相当简洁，降低了学习成本。
