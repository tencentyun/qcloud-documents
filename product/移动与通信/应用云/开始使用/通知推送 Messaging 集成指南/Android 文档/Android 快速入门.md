## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件（已完成请跳过）

在您创建好的应用上单击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.file.myqcloud.com/guides/project/downloadConfig.gif)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

![](https://main.qcloudimg.com/raw/2098031bcf22b6a32ac87066ed8a3278.jpg)

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 APK 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


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

在应用级 build.gradle 文件（通常是 app/build.gradle）中添加 messaging 服务依赖，并使用插件：

```
dependencies {
    // 增加这两行
    compile 'com.tencent.tac:tac-core:1.3.+'
    compile 'com.tencent.tac:tac-messaging:1.3.+'
}
...

// 在文件最后使用插件
apply plugin: 'com.tencent.tac.services'
```
> `com.tencent.tac:tac-messaging` 默认引入了厂商通道推送包，如果不需要集成厂商推送，您可以改用 `com.tencent.tac:tac-messaging-lite`

到此您已成功接入了 MobileLine 移动推送服务。

## 验证服务

### 查看服务启动情况

安装并运行 App 后，SDK 会自动在 Messaging 后台进行注册，注册成功后会打印如下日志：

```
I/tacApp: TACMessagingService register success, code is 0, token is 495689dbfda473ef44de899cf45111fd83031156
```

> **注意：**
> 这里日志打印的 token 信息标识推送时的唯一 ID，您可以通过 token 信息给该设备发送通知。

如果没有打印以上日志，请查看 [常见问题](https://cloud.tencent.com/document/product/666/14825)。

### 在控制台上推送通知栏消息

打开 [MobileLine 控制台](https://console.cloud.tencent.com/tac)，选择【创建推送】下的【通知栏消息】，并填写好 **通知标题** 和 **通知内容**，然后选择单选框中的【单个设备】，然后将注册成功后打印的设备唯一标识 token 信息拷贝到编辑框中（示例这里为 495689dbfda473ef44de899cf45111fd83031156 ），然后单击【确认推送】。

![](https://tacimg-1253960454.file.myqcloud.com/guides/Messaging/console_push_notification_simple.gif)

推送通知栏消息成功后，App 在运行状态下会收到通知栏消息。

> **注意：**您也可以选择推送给所有的设备，设备收到消息可能会有一定的延时。

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

# MobileLine Messaging

-keep class com.tencent.android.tpush.** {* ;}
-keep class com.qq.taf.jce.** {*;}

# MobileLine Vendor Messaging

-keepattributes *Annotation*
-keepattributes Exceptions
-keepattributes InnerClasses
-keepattributes Signature
-keepattributes SourceFile,LineNumberTable
-keep class com.hianalytics.android.**{*;}
-keep class com.huawei.updatesdk.**{*;}
-keep class com.huawei.hms.**{*;}
-keep class com.huawei.gamebox.plugin.gameservice.**{*;}
-keep public class com.huawei.android.hms.agent.** extends android.app.Activity { public *; protected *; }
-keep interface com.huawei.android.hms.agent.common.INoProguard {*;}
-keep class * extends com.huawei.android.hms.agent.common.INoProguard {*;}
-keep class com.meizu.cloud.pushsdk.**{*;}
-keepclasseswithmembernames class com.xiaomi.**{*;}
-dontwarn com.huawei.android.hms.**
-dontwarn com.xiaomi.push.**
-dontwarn com.meizu.cloud.pushsdk.**
```


## 后续步骤

### 注册回调接口 

**注册回调接口非常重要**，您可以注册回调接口来接收推送服务在不同状态下给您的回调，具体有：

- `onRegisterResult()` ：注册 Messaging 服务后回调。
- `onUnregisterResult()` ：反注册 Messaging 服务后回调。
- `onMessageArrived()`：收到透传消息（即控制台上的应用内消息）后回调。
- `onNotificationArrived()` ：收到通知栏消息后回调。
- `onNotificationClicked()` ：单击通知栏消息后回调。
- `onNotificationDeleted()` ：删除通知栏消息后回调。
- `onBindTagResult()`：绑定标签后回调。
- `onUnbindTagResult()` ：解绑标签后回调。

如何注册回调接口，请参见 [这里](https://cloud.tencent.com/document/product/666/16848)。

### 集成厂商推送通道

**我们建议您集成厂商推送通道**，通过集成厂商官方提供的系统级推送通道，在对应厂商手机上，推送消息能够通过系统通道抵达终端，并且无需打开应用就能够收到推送，目前支持华为、小米和魅族三个厂商通道，具体集成方式请参考 [这里](https://cloud.tencent.com/document/product/666/16641)。

### 给设备推送消息

您可以通过控制台给设备推送消息(具体请参考 [这里](https://cloud.tencent.com/document/product/666/16640))，您也可以通过我们的后台接口来发送消息，具体请参考 [Rest API 使用指南](https://cloud.tencent.com/document/product/666/15584) 或者 [服务端 SDK](https://cloud.tencent.com/document/product/666/15606)。除了通过设备 token 来指定用户外，我们还支持通过标签推送消息（具体请参考 [这里](https://cloud.tencent.com/document/product/666/16637)）或者通过账户推送消息（具体请参考 [这里](https://cloud.tencent.com/document/product/666/16639)）。



