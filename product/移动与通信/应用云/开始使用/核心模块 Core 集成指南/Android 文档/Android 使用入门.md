
移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

> 如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。

## 第二步：添加配置文件

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

下表展示了 MobileLine 各种服务所对应的库

|功能|服务名称|Gradle 依赖项|
|:---|:---|:---|
|腾讯移动分析（MTA）|analytics|com.tencent.tac:tac-core:1.0.1|
|腾讯移动推送（信鸽）|messaging|com.tencent.tac:tac-messaging:1.0.1|
|腾讯崩溃服务（bugly）|crash|com.tencent.tac:tac-crash:1.0.1|
|腾讯计费（米大师）|payment|com.tencent.tac:tac-payment:1.0.1|
|移动存储（Storage）|storage|com.tencent.tac:tac-storage:1.0.1|
|登录与授权（Authorization）|authorization|com.tencent.tac:tac-authorization:1.0.1|


如果您想集成我们的各种服务，那么您只需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加对应的服务依赖即可：

例如，您只想集成 `analytics` 服务，

```
dependencies {
	// 增加这行
	compile 'com.tencent.tac:tac-core:1.0.1'
}
```

如果您想集成 `messaging` 服务：

```
dependencies {
	// 增加这两行，其中 core 是所有其他模块的基础
	compile 'com.tencent.tac:tac-core:1.0.1' 
	compile 'com.tencent.tac:tac-messaging:1.0.1'
}
```

如果您想同时集成 `messaging` 和 `crash` 服务：

```
dependencies {
	// 增加这三行，其中 core 是所有其他模块的基础
	compile 'com.tencent.tac:tac-core:1.0.1' 
	compile 'com.tencent.tac:tac-messaging:1.0.1'
	compile 'com.tencent.tac:tac-crash:1.0.1'
}
```
> 使用 payment 计费等服务时还需要额外的配置，详情请参见各自服务的快速入门。

## 第四步：参考各个服务的快速入门

一些子服务可能还有其他的集成步骤，请参考各个服务的快速入门文档。

|功能|服务名称|入门指南|
|:---|:---|:---|
|腾讯移动分析（MTA）|analytics|[Analytics 快速入门](https://cloud.tencent.com/document/product/666/14313)|
|腾讯移动推送（信鸽）|messaging|[Messaging 快速入门](https://cloud.tencent.com/document/product/666/14323)|
|腾讯崩溃服务（bugly）|crash|[Crash 快速入门](https://cloud.tencent.com/document/product/666/14309)|
|腾讯计费（米大师）|payment|[Payment 快速入门](https://cloud.tencent.com/document/product/666/14593)|
|移动存储（Storage）|storage|[Storage 快速入门](https://cloud.tencent.com/document/product/666/14327)|
|登录与授权（Authorization）|authorization|[Authorization 快速入门](https://cloud.tencent.com/document/product/666/14331)|

## 后续步骤

### 了解 MobileLine：

- 查看 [MoblieLine 应用示例](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/QCloudTACSample)

### 向您的应用添加 MobileLine 功能：

- 借助 [Analytics](https://cloud.tencent.com/document/product/666/14822) 深入分析用户行为。
- 借助 [messaging](https://cloud.tencent.com/document/product/666/14826) 向用户发送通知。
- 借助 [crash](https://cloud.tencent.com/document/product/666/14824) 确定应用崩溃的时间和原因。
- 借助 [storage](https://cloud.tencent.com/document/product/666/14828) 存储和访问用户生成的内容（如照片或视频）。
- 借助 [authorization](https://cloud.tencent.com/document/product/666/14830) 来进行用户身份验证。
- 借助 [payment](https://cloud.tencent.com/document/product/666/14832) 获取微信和手 Q 支付能力
