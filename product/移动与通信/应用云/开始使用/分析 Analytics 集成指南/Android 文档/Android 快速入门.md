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
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK（已完成请跳过）

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

在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 analytics 服务依赖，并使用插件：

```
dependencies {
    // 增加这行
    compile 'com.tencent.tac:tac-core:1.3.+'
}
...

// 在文件最后使用插件
apply plugin: 'com.tencent.tac.services'
```

到此您已经成功接入了 MobileLine 移动分析服务。

## 验证服务

### 1. 开启实时上报

Analytics 服务默认采用批量上报策略，在本地缓存事件到达一定数量之后才能集中上报。如果您在调试时，希望每个事件都独立上报，从而能在控制台实时看到手机的上报事件，可以通过下面的方式开启实时上报。

>**注意：**
>由于每次上报都会建立网络连接，会增加手机流量，也会损耗手机电量，影响终端体验，因此建议您在 release 模式下关闭实时上报，采用默认的批量上报策略。

#### 在 `Application` 子类中添加代码

如果您自己的应用中已经有了 `Application` 的子类，请重载它的 `attachBaseContext(Context)` 方法，在里面添加配置代码，如果没有，请自创建一个 `Application` 的子类。如：

```
public class MyCustomApp extends Application {
  @Override
  protected void attachBaseContext(Context base) {
		super.attachBaseContext(base);
    	// 实例化一个新的配置
		TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);
		
		// 修改其他配置
		... 

		// 设置行为统计数据上报的策略
		TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");
		analyticsOptions.strategy(TACAnalyticsStrategy.INSTANT); // 立即发送

		// 让自定义设置生效
		TACApplication.configureWithOptions(this, applicationOptions);
  }
}
```

#### 在 `AndroidManifest.xml` 文件中注册

在创建好 `Application` 的子类并添加好代码后，您需要在工程的 `AndroidManifest.xml` 文件中注册该 `Application` 类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    <!-- 这里替换成您自己的 Application 子类 -->
    android:name="com.example.tac.MyCustomApp"
    ...>
  </application>
</manifest>
```



### 2. 查看服务启动情况

app 启动后，您可以从 logcat 中 过滤 tag `tacApp` ，查看到服务启动的日志。

```
04-18 11:40:53.087 30623-30623/com.tencent.tac.sample I/tacApp: TACAnalyticsService is starting.
04-18 11:40:53.115 30623-30623/com.tencent.tac.sample I/tacApp: Analytics set app key : Aqc100008 and channel : TAC
04-18 11:40:53.134 30623-30623/com.tencent.tac.sample I/tacApp: Boot Up : com.tencent.tac.analytics.TACAnalyticsService
```

如果没有看到启动日志，您可以从 logcat 中 过滤 tag `MtaSDK`，查看是否有错误信息。

### 3. 查看上报日志

在 App 中打开一个 Activity，您可以从 logcat 中 过滤 tag `MtaSDK`，查看上报请求和返回结果的日志。如果看到 `http get response data:{"ret":0}`，说明上报成功。

```
04-18 13:48:27.698 1550-1577/com.tencent.tac.sample D/MtaSDK: [StatDispatcher(9159): SourceFile:268] - before Gzip:1159 bytes, after Gzip:655 bytes
04-18 13:48:27.749 1550-1577/com.tencent.tac.sample I/MtaSDK: [StatDispatcher(9159): SourceFile:284] - http recv response status code:200, content length:29
04-18 13:48:27.750 1550-1577/com.tencent.tac.sample I/MtaSDK: [StatDispatcher(9159): SourceFile:325] - http get response data:{"ret":0}
```

### 4. 控制台查看数据

登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac)，在移动分析的实时数据里面，您可以看到页面访问的数据，如下图：

![](http://tacimg-1253960454.file.myqcloud.com/guides/%E6%8E%A7%E5%88%B6%E5%8F%B0-%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE.png)

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
