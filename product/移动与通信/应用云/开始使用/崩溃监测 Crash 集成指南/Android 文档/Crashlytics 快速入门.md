## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件（已完成请跳过）

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 crash 服务依赖：

```
dependencies {
    // 增加这两行
    compile 'com.tencent.tac:tac-core:1.1.0'
    compile 'com.tencent.tac:tac-crash:1.1.0'
}
```

## 验证服务

为了让您测试是否正确的接入了 Crash 服务，您可以调用如下代码来主动产生 Crash ：

```
TACCrashSimulator.testJavaCrash();
```

应用 Crash 后，您可以登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac)，然后点击【异常上报】下的【异常分析】，即可查看上报到控制台的异常，如果没有上报，您可以查看 [常见问题](https://cloud.tencent.com/document/product/666/14825)

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/crash/crash_report.png)
