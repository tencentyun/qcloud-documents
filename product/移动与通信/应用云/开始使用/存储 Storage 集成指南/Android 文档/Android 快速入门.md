## 准备工作

* 首先您需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的工程。
* 其次您需要一个提供临时密钥的服务，请参考我们提供的 [快速搭建临时密钥服务](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E5%BA%94%E7%94%A8%E4%BA%91/%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8/%E5%AD%98%E5%82%A8%20Storage%20%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/%E6%9C%8D%E5%8A%A1%E5%99%A8SDK/%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA%E4%B8%B4%E6%97%B6%E5%AF%86%E9%92%A5%E6%9C%8D%E5%8A%A1.md)。

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

您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 storage 服务依赖：

```
dependencies {
	// 增加这行
	compile 'com.tencent.tac:tac-core:1.1.0'
	compile 'com.tencent.tac:tac-storage:1.1.0'
}
```

## SDK 配置密钥服务

Storage SDK 需要一个有效的密钥提供者来提供密钥，关于如何在 SDK 里配置密钥服务提供者，请参见 [Android 配置密钥服务](https://cloud.tencent.com/document/product/666/15350)。

>**注意：**
>请先完成配置，再调用 Storage 服务的任何功能。否则，我们的服务无法识别您的身份。



到此您已经成功接入了 MobileLine 移动存储服务。


## Proguard配置

如果你的代码开启了混淆，为了sdk可以正常工作，请在 `proguard-rules.pro`文件中添加如下配置：

```
# MobileLine Core

-keep class com.tencent.qcloud.core.** { *;}
-keep class bolts.** { *;}
-keep class com.tencent.tac.** { *;}
-keep class com.tencent.stat.*{*;}
-keep class com.tencent.mid.*{*;}
-dontwarn okhttp3.**
-dontwarn okio.**
-dontwarn javax.annotation.**
-dontwarn org.conscrypt.**
```