
移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](replaceme)。

> 如果您已经在 MobileLine 控制台上创建过了项目和应用，请跳过此步。

## 第二步：添加配置文件

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

> 请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。


## 第三步：集成 SDK

下表展示了 MobileLine 各种服务所对应的库。

|功能|服务名称|Gradle 依赖项|
|:---|:---|:---|
|腾讯移动分析（MTA）|analytics|com.tencent.tac:tac-core:1.0.0|
|腾讯移动推送（信鸽）|messaging|com.tencent.tac:tac-core:1.0.0<br>com.tencent.tac:tac-messaging:1.0.0|
|腾讯崩溃服务（bugly）|crash|com.tencent.tac:tac-core:1.0.0<br>com.tencent.tac:tac-crash:1.0.0|
|腾讯计费（米大师）|payment|com.tencent.tac:tac-core:1.0.0<br>com.tencent.tac:tac-payment:1.0.0|
|移动存储（Storage）|storage|com.tencent.tac:tac-core:1.0.0<br>com.tencent.tac:tac-storage:1.0.0|
|授权（Authorization）|authorization|com.tencent.tac:tac-core:1.0.0<br>com.tencent.tac:tac-authorization:1.0.0|


如果您想集成我们的各种服务，那么您只需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加对应的服务依赖即可：

例如，您只想集成 `analytics` 服务，

```
dependencies {
	// 增加这行
	compile 'com.tencent.tac:tac-core:1.0.0'
}
```

如果您想集成 `messaging` 服务：

```
dependencies {
	// 增加这两行，其中 analytics 服务是所有其他模块的基础，因此必须添加 analytics 依赖
	compile 'com.tencent.tac:tac-core:1.0.0' 
	compile 'com.tencent.tac:tac-messaging:1.0.0'
}
```

如果您想同时集成 `messaging` 和 `crash` 服务：

```
dependencies {
	// 增加这三行，其中 analytics 服务是所有其他模块的基础，因此必须添加 analytics 依赖
	compile 'com.tencent.tac:tac-core:1.0.0' 
	compile 'com.tencent.tac:tac-messaging:1.0.0'
	compile 'com.tencent.tac:tac-crash:1.0.0'
}
```
> 使用 payment 计费服务和 storage 存储服务时还需要额外的配置，详情请参见 [payment 集成指南](replaceme) 和 [storage 集成指南](replaceme)。

## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。

### 在 `Application` 子类中添加初始代码

如果您自己的应用中已经有了 `Application` 的子类，请在该类的 `onCreate()` 方法中添加配置代码，如果没有，请自行创建：

```
public class MyCustomApp extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    ...
    //增加这行
    TACApplication.configure(this);
  }
}

```
### 在 `AndroidManifest.xml` 文件中注册

在创建好 `Application` 的子类并添加好初始化代码后，您需要在工程的 `AndroidManifest.xml` 文件中注册该 `Application` 类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    <!-- 这里替换成你自己的 Application 子类 -->
    android:name="com.example.tac.MyCustomApp"
    ...>
  </application>
</manifest>
```

### 启动服务

MobileLine Android SDK 不会自动帮您启动服务，需要您自己手动启动，详情请参考各个服务快速入门的【启动服务】部分：

|功能|服务名称|入门指南|
|:---|:---|:---|
|腾讯移动分析（MTA）|analytics|[Analytics 快速入门](replaceme)|
|腾讯移动推送（信鸽）|messaging|[Messaging 快速入门](replaceme)|
|腾讯崩溃服务（bugly）|crash|[Crash 快速入门](replaceme)|
|腾讯计费（米大师）|payment|[Payment 快速入门](replaceme)|
|移动存储（Storage）|storage|[Storage 快速入门](replaceme)|
|授权（Authorization）|authorization|[Authorization 快速入门](replaceme)|

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
