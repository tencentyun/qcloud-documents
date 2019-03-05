## 准备工作

* 首先您需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的工程。
* 其次您需要一个在后台搭建一个授权服务器，为 SDK 提供临时密钥，请参考 [用户访问控制](https://cloud.tencent.com/document/product/666/17922)。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件（已完成请跳过）

在您创建好的应用上单击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.file.myqcloud.com/guides/project/downloadConfig.gif)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

![](https://main.qcloudimg.com/raw/2098031bcf22b6a32ac87066ed8a3278.jpg)

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

您需要在工程级 build.gradle 文件中添加 SDK 插件的依赖：

```
buildscript {
	...
    dependencies {
        classpath 'com.android.tools.build:gradle:3.0.1'
        // 添加这行
        classpath 'com.tencent.tac:tac-services-plugin:1.3.+'
    }
}
```

在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 Storage 服务依赖，并使用插件：

```
dependencies {
	// 增加这行
	compile 'com.tencent.tac:tac-core:1.3.+'
	compile 'com.tencent.tac:tac-storage:1.3.+'
}
...

// 在文件最后使用插件
apply plugin: 'com.tencent.tac.services'
```

## 配置使用权限

Storage SDK 需要一个后台授权服务器提供临时密钥，才能正常工作。关于如何在 SDK 里配置服务器接口，请参见 [Android 配置授权服务器](https://cloud.tencent.com/document/product/666/17199)。

>**注意：**
>请先完成配置，再调用 Storage 服务的任何功能。否则，我们的服务无法识别您的身份。



到此您已经成功接入了 MobileLine 移动存储服务。


## Proguard 配置

如果您的代码开启了混淆，为了 SDK 可以正常工作，请在 `proguard-rules.pro`文件中添加如下配置：

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

## 后续步骤

您可以通过策略精确控制您数据的访问权限，可以参考 [数据安全性最佳实践](https://cloud.tencent.com/document/product/666/17921)。
