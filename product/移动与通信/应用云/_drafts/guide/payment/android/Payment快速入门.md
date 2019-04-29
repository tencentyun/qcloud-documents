## 准备

- 您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。
- 其次您需要 [配置后台服务器](https://cloud.tencent.com/document/product/666/14600)。
- 最后您需要 [添加支付渠道信息](https://cloud.tencent.com/document/product/666/14599)

## 第一步：创建项目和应用（如果已做请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](replaceme)。

## 第二步：添加配置文件（如果已做请跳过）

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

> 请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了不可泄露的机密信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的机密信息泄露。

## 第三步：集成 SDK

您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 payment 服务依赖：

```
dependencies {
    // 增加这两行
    compile 'com.tencent.tac:tac-core:1.0.0'
    compile 'com.tencent.tac:tac-payment:1.0.0'
}
```

## 第四步：初始化

集成好我们提供的 SDK 后，您需要在您自己的工程中添加初始化代码，从而让 MobileLine 服务在您的应用中进行自动配置。

### 在 `Application` 子类中添加初始代码（如果已做请跳过）

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

> 如果您同时集成了我们多个服务，只需要添加一次初始化代码，请不要重复添加。

### 在 `AndroidManifest.xml` 文件中注册（如果已做请跳过）

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

> 如果您的 `Application` 子类已经在 `AndroidManifest.xml` 文件中注册，请不要重复注册。


### 启动服务

Payment 服务无需启动，到此您已经成功接入了 MobileLine 移动付费服务。
