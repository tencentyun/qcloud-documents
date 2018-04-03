
移动开发平台（MobileLine）使用起来非常容易，只需要简单的 4 步，您便可快速接入。接入后，您即可获得我们提供的各项能力，减少您在开发应用时的重复工作，提升开发效率。

## 准备工作

为了使用移动开发平台（MobileLine）Android 版本的 SDK，您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用

在使用我们的服务前，您必须先在 [MobileLine 控制台](https://console.cloud.tencent.com/tac) 上创建项目，每个项目下可以包含多个应用，如 Android 或者 IOS 应用，当然，您也可以在同一个项目下创建多个 Android 或者 IOS 应用。

### 创建项目

首先登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac) ，然后点击【创建第一个项目】按钮来创建一个新的项目，例如，下图这里创建了一个名为 MyGreatApp 的项目：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newProject.png)


### 创建应用

创建好项目后，我们在 MyGreatApp 项目下创建应用，点击【创建 IOS 应用】或者【创建 Android 应用】按钮来创建应用，如图这里【创建 Android 应用】：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newApp.png)

填写好 **应用名称** 和 **应用包名** 后，选择下一步。到此，您便已创建好了一个 MobileLine 项目。

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/loginApp.png)

> 您可以完全按照我们控制台上的向导来集成 MobileLine SDK，控制台上默认指导您集成我们的最基本的 core 模块，这是 MobileLine 中核心的基础功能，包含了应用基本数据的上报和分析。

## 第二步：添加配置文件

创建好应用后，您可以点击红框中的【tac\_services\_configurations.zip】来下载该应用的配置文件的压缩包：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去，添加好配置文件后，继续点击【下一步】。

> 请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。


## 第三步：集成 SDK

每一个 MobileLine 服务都是一个单独的 SDK，其中 `com.tencent.tac:tac-core` 是其他所有模块的基础模块，因此您必须至少将 `analytics` 模块集成到您的 app 中，下表展示了 MobileLine 各种服务所对应的库。

|Gradle 依赖项|服务名称|功能|
|:---|:---|:---|
|com.tencent.tac:tac-core:1.0.0|	analytics|腾讯移动分析（MTA）|
|com.tencent.tac:tac-messaging:1.0.0	|messaging|腾讯移动推送（信鸽）|
|com.tencent.tac:tac-crash:1.0.0|	crash|	腾讯崩溃服务（bugly）|
|com.tencent.tac:tac-storage:1.0.0|	storage|移动存储（Storage）|
|com.tencent.tac:tac-authorization:1.0.0|authorization|授权（Authorization）|
|com.tencent.tac:tac-payment:1.0.0|	payment|腾讯计费（米大师）|

添加好配置文件并点击【下一步】后，向导如图所示：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/addRelease.png)

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

> 控制台向导上默认您只集成最基础的 `analytics` 服务。

## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。整个初始化的过程很简单，只需要您在 `Application` 的子类中调用 `TACApplication.configure(this)` 语句，然后在 `AndroidManifest.xml` 注册该 `Application` 子类即可。

在集成好 SDK 并点击【下一步】后，向导如下图所示：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/addInitCode.png)

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

最后点击【完成】，到此您已经成功接入了 MobileLine 服务。

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
