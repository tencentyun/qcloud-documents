本文主要介绍如何快速地将腾讯云 TRTC SDK(Android) 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Android Studio 2.0+。
- Android 4.1（SDK API 16）及以上系统。

## 集成 SDK（aar）

您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。

### 方法一：自动加载（aar）
TRTC SDK 已经发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。
只需要用 Android Studio 打开需要集成 SDK 的工程（本文以 [TRTC SDK Demo](https://github.com/TencentVideoCloudTRTC/TRTCSDK/tree/master/Android) 为例），然后通过简单的三个步骤修改 app/build.gradle 文件，就可以完成 SDK 集成：
![](https://main.qcloudimg.com/raw/05caa51b138e99ac32b177201c02f649.jpg)

- **第一步：添加 SDK 依赖**   
在 dependencies 中添加 TRTCSDK 的依赖。
```
dependencies {
	compile 'com.tencent.liteav:LiteAVSDK_TRTC:6.0.1688'
}
```

- **第二步：指定 App 使用架构**
在 defaultConfig 中，指定 App 使用的 cpu 架构(目前 TRTC SDK 支持 armeabi 和 armeabi-v7a)  。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```

- **第三步：同步 SDK**  
单击 Sync Now 按钮，如果您的网络连接 jcenter 没有问题，很快 SDK 就会自动下载集成到工程里。


### 方法二：手动下载（aar）
如果您的网络连接 jcenter 有问题，也可以手动下载 SDK 集成到工程里：

- **第一步：下载 TRTC SDK**  
在 Github 上可以下载到最新版本的 [TRTC SDK](https://github.com/TencentVideoCloudTRTC/TRTCSDK/tree/master/Android/app/libs)：
![](https://main.qcloudimg.com/raw/75434db66f21ed185b30528d45128cd4.png)

- **第二步：拷贝 TRTC SDK 到工程目录**  
将下载到的 aar 文件拷贝到工程的 **app/libs** 目录下：
![](https://main.qcloudimg.com/raw/bdbc00b67ae7d087769d25a31dd6beed.png)

- **第三步：指定本地仓库路径**
在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/2bd3f6fc086314f300b0c2eddafb9215.jpg)

- **第四步：添加 TRTC SDK 依赖**   
在 app/build.gradle 中，添加引用 aar 包的代码。
![](https://main.qcloudimg.com/raw/98b4806ed2484e96d47eb1ad165e900d.jpg)

- **第五步：指定 App 使用架构**
在 app/build.gradle的defaultConfig 中，指定 App 使用的 cpu 架构(目前 TRTC SDK 支持 armeabi 和 armeabi-v7a)  。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```

- **第六步：同步 SDK**  
单击 Sync Now 按钮，完成 TRTC SDK 的集成工作。


## 集成 SDK（jar）
如果您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 TRTC SDK：

- **第一步：下载解压 TRTC SDK**
在 Github 上可以 [下载](https://github.com/TencentVideoCloudTRTC/TRTCSDK/tree/master/Android) 到最新版本的 jar 压缩包，文件名一般为 LiteAV_TRTC_xxx.zip（其中 xxx 为 TRTC SDK 的版本号）：
![](https://main.qcloudimg.com/raw/8a97ef2b6a0cb2860b57b220d0684328.png)
解压后得到 libs 目录，里面主要包含 jar 文件和 so 文件夹，文件清单如下：
![](https://main.qcloudimg.com/raw/d90ef03851b93079a6863e7530ac89ca.png)

- **第二步：拷贝 SDK 文件到工程目录**
将解压得到的 jar文件和 armeabi， armeabi-v7a 文件夹拷贝到 app/libs 目录下。
![](https://main.qcloudimg.com/raw/2b093d87ebaa3650e16523f26866b16c.png)

- **第三步：引用 jar 库**
在 app/build.gradle 中，添加引用 jar 库的代码。
![](https://main.qcloudimg.com/raw/f9cbdca4a493c0bf1e12557a15974b9d.jpg)			

- **第四步：引用 so 库**
在 app/build.gradle 中，添加引用 so 库的代码。
![](https://main.qcloudimg.com/raw/10003cdc49d4856ee4feb840f24680a7.jpg)

- **第五步：指定 App 使用架构**
在 app/build.gradle的defaultConfig 中，指定 App 使用的 cpu 架构(目前 TRTC SDK 支持 armeabi 和 armeabi-v7a) 。 
```
   defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```

- **第六步：同步 SDK**  
单击 Sync Now 按钮，完成 TRTC SDK 的集成工作。


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
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

## 设置混淆规则
在 proguard-rules.pro 文件，将 TRTC SDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```

## 常见问题

### 1. TRTC SDK 是否支持 arm64
目前 TRTC SDK 由于 3A 声学处理库尚不支持 arm64 下的一些汇编指令， 所以暂时还不支持 arm64 架构，请注意指定 App 的架构配置。

