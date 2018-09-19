之前在 2016 Google IO 大会上，Google 大力介绍了他们的移动和 Web 应用程序开发平台 Firebase，对于中国的用户来说，最大的两个门槛可能是

* 无法连通 firebase 后台，需要翻墙。
* 很多手机中并没有内置 Google 服务，需要用户自行安装。

这两点对于我们开发者老司机来说当然 so easy，但是对于普通用户来说可就没那么容易了，这也是 firebase 在大陆没人用的重要原因。虽然如此，当时自己还是好好的体验了一把的，整体感觉上看，使用体验非常不错，感觉非常人性化，你可以在 firebase.google.com 上可以找到想要的一切，甚至包含了你暂时还没有想到的。

当然如果用户没办法使用，对于开发者来说也只能算是鸡肋了，之前也是一直期望国内的几家大厂能够提供相类似的平台，但是一直都没有，感觉有点可惜啊，自我感觉如果这个平台搞好了还是应该有很多人用的，对于快速开发有很大的好处啊。

终于，最近腾讯云推出了一个 [MobileLine 平台](https://cloud.tencent.com/document/product/666)，功能暂时没有 firebase 那么齐全，毕竟刚上线，不过体验了一下，感觉还是很不错的。目前主要包含了数据分析、消息推送、Crash 上报、支付还有存储。

### 先来看下创建应用吧：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/project/application_create.jpg)

一共分为注册应用、下载配置文件、添加 SDK、添加初始化代码 4 步，

这里提示还是很清晰的。

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/project/application_guide.jpg)

### 移动分析：

各种数据看起来还是不错的：

![](http://tacimg-1253960454.file.myqcloud.com/guides/控制台-数据概览-实时数据.png)

### Crash 上报

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/crash/crash_overview.png)

### 消息推送

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/信鸽-创建推送-android-通知栏消息.png)

### 存储

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/storage/5AGQ%60V7%241EOX6JTLQJZ3G_2.png)

### 支付

支付稍微步骤有点多，因为涉及到比较多信息的申请，这个文档写的很详细 [Payment支付流程指南](https://cloud.tencent.com/document/product/666/14879)，

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_7.png)

更多的数据和使用方式可以参考下[官网](https://cloud.tencent.com/document/product/666)，这里就不详细贴图啦。



说一下使用 MobileLine 的几点优点吧：

- 接入成本很低，很容易就可以将 MobileLine 集成到自己的应用中。
- 通过控制台可以很方便的查看 IOS/Android 应用的整体数据情况，很直观。
- 目前提供的数据分析、推送、Crash 上报和存储还是一般应用都会需要的，刚需。
- 有腾讯那么多超大用户量的 app 做保证，MobileLine 的可靠性还是应该很不错的。




总结一下，腾讯 MobileLine 对标是的 Google 提供的 firebase，整体使用上，如控制台、使用文档、终端 SDK 这几个方面做得都还不错，开发者接入后还是能提供很多方便的，不足的是目前提供的功能还太少，很多比较重要的服务还没有，比如 数据库、登录等基本功能，希望腾讯能尽快补齐吧。整体使用感觉还是不错的，有兴趣的可以自己去体验下啦。

