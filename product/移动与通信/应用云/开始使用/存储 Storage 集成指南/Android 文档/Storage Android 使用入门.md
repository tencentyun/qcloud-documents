在 [MobileLine Android 集成手册]() 中，我们根据控制台向导提供了最简单的方式来接入 MobileLine 的各种服务，同时您也可以不完全依赖向导来接入我们的移动存储以及其他服务。

## 准备

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建 MobileLine 项目和应用

在使用我们的服务前，您必须先在 [MobileLine 控制台](https://console.cloud.tencent.com/tac) 上创建项目，每个项目下可以包含多个应用，如 Android 或者 IOS 应用，当然，您也可以在同一个项目下创建多个 Android 或者 IOS 应用。

### 创建项目

首先登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac) ，然后点击【创建第一个项目】按钮来创建一个新的项目，例如，下图这里创建了一个名为 MyGreatApp 的项目：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newProject.png)


### 创建应用

创建好项目后，我们在 MyGreatApp 项目下创建应用，点击【创建 IOS 应用】或者【创建 Android 应用】按钮来创建应用，如图这里【创建 Android 应用】：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/newApp.png)

填写好 **应用名称** 和 **应用包名** 后，选择下一步。到此，您便已创建好了一个 MobileLine 应用，此时，您可以点击关闭向导。

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/loginApp.png)

> 如果您之前已经创建过 MobileLine 应用了，那么你可以选择使用之前的 MobileLine 应用或者创建一个新的应用。

## 第二步：添加配置文件

在您创建好的应用上点击【下载配置】来下载该应用的配置文件的压缩包：

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/mobileLine/guide/downloadConfig2.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

> 请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。

## 第三步：集成 SDK

每一个 MobileLine 服务都是一个单独的 SDK，其中 `com.tencent.tac:tac-core` 移动分析服务是其他所有模块的基础模块，`com.tencent.tac:tac-storage` 是 MobileLine 移动存储服务，因此您在使用我们的移动存储服务时必须同时添加这两个服务。

在您的应用级 build.gradle（通常是 app/build.gradle）添加移动分析和移动存储服务的依赖：

```
dependencies {
    //增加这两行
    compile 'com.tencent.tac:tac-core:1.0.0' 
    compile 'com.tencent.tac:tac-storage:1.0.0' 
}
```

## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。整个初始化的过程很简单，只需要您在 `Application` 的子类中调用 `TACApplication.configure(this)` 语句，然后在 `AndroidManifest.xml` 注册该 `Application` 子类即可。

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

> 如果该工程之前已经添加过 MobileLine 初始化代码，那么请不要重复添加。

到此您已经成功接入了 MobileLine 移动存储服务。
