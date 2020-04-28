本文主要介绍如何快速地将腾讯云 TRTC SDK(Android) 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Android Studio 3.5+。
- Android 4.1（SDK API 16）及以上系统。

## 集成 SDK（aar）

您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。

### 方法一：自动加载（aar）
TRTC SDK 已经发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。
只需要用 Android Studio 打开需要集成 SDK 的工程（本文以 [TRTCSimpleDemo](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTCSimpleDemo) 为例），然后通过简单的三个步骤修改 app/build.gradle 文件，就可以完成 SDK 集成：
![](https://main.qcloudimg.com/raw/cc46fbc16ad95c8166af4ff99647e4c6.png)

1. 在 dependencies 中添加 TRTCSDK 的依赖。
 - 若使用3.x版本的 com.android.tools.build:gradle 工具，请执行以下命令：
```
dependencies {
         implementation 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
}
```
 - 若使用2.x版本的 com.android.tools.build:gradle 工具，请执行以下命令：
```
dependencies {
         compile 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
}
```
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
       ndk {
           abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
       }
}
```
>?目前 TRTC SDK 支持 armeabi ， armeabi-v7a 和 arm64-v8a。
>
3.单击【Sync Now】，自动下载 SDK 并集成到工程里。


### 方法二：手动下载（aar）
如果您的网络连接 jcenter 有问题，您也可以手动下载 SDK 集成到工程里：

1. 下载最新版本 [TRTC SDK](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip)。
2. 将下载到的 aar 文件拷贝到工程的 **app/libs** 目录下。
3. 在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/bc3215028103fe980aedcbf011b97b02.png)
4. 在 app/build.gradle 中，添加引用 aar 包的代码。
![](https://main.qcloudimg.com/raw/a21f50100e881d53f4d502d2a1c8c5aa.png)
5.在 app/build.gradle的defaultConfig 中，指定 App 使用的 CPU 架构。
```
defaultConfig {
       ndk {
           abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
       }
}
```
>?目前 TRTC SDK 支持 armeabi ， armeabi-v7a 和 arm64-v8a。
>
6. 单击【Sync Now】，完成 TRTC SDK 的集成工作。


## 集成 SDK（jar）
如果您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 TRTC SDK：

1. [下载](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip) 最新版本的 jar 压缩包，文件路径为`SDK/LiteAVSDK_TRTC_xxx.zip` （其中 xxx 为 TRTC SDK 的版本号）。
2. 解压后得到 libs 目录，里面主要包含 jar 文件和 so 文件夹。
3. 将解压得到的 jar 文件和 armeabi， armeabi-v7a， arm64-v8a 文件夹拷贝到 app/libs 目录下。
![](https://main.qcloudimg.com/raw/5bf82ca89b3a14cca470fcedc048d7fa.png)
4. 在 app/build.gradle 中，添加引用 jar 库的代码。
![](https://main.qcloudimg.com/raw/6ffbb4b79c06555376b137c849b43bb7.png)	
5. 在 app/build.gradle 中，添加引用 so 库的代码。
```
sourceSets {
       main {
           jniLibs.srcDirs = ['libs']
       }
}
```
![](https://main.qcloudimg.com/raw/299eeb5b3e8961e816f3ce17b97b4339.png)
6. 在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构。 
```
defaultConfig {
       ndk {
           abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
       }
}
```
>?目前 TRTC SDK 支持 armeabi， armeabi-v7a 和 arm64-v8a。
>
7. 单击【Sync Now】，完成 TRTC SDK 的集成工作。


## 配置 App 权限
在 AndroidManifest.xml 中配置 App 的权限，TRTC SDK 需要以下权限：

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

## 设置混淆规则
在 proguard-rules.pro 文件，将 TRTC SDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```
## 设置 App 打包参数
在 app/build.gradle 下，添加如下信息：

```
packagingOptions {
	pickFirst '**/libc++_shared.so'
	doNotStrip "*/armeabi/libYTCommon.so"
	doNotStrip "*/armeabi-v7a/libYTCommon.so"
	doNotStrip "*/x86/libYTCommon.so"
	doNotStrip "*/arm64-v8a/libYTCommon.so"
}
```
![](https://main.qcloudimg.com/raw/e40d5c294a59d56a1f89f20960c7e4c1.png)


