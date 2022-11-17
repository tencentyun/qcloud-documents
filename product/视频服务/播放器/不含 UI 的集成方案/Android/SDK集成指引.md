本文主要介绍如何快速地将腾讯云视立方·播放器SDK集成到您的项目中，不同版本的 SDK 集成方式都通用，按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Android Studio 2.0+。
- Android 4.1（SDK API 16）及以上系统。

## 集成 SDK（aar）
您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。

### 方法一：自动加载（aar） 
播放器 SDK 已经发布到 [mavenCentral 库](https://repo1.maven.org/maven2/com/tencent/liteav/LiteAVSDK_Player/)，您可以通过在 gradle 配置 mavenCentral 库，自动下载更新 LiteAVSDK_Player。
只需要用 Android Studio 打开需要集成 SDK 的工程，然后通过简单的四个步骤修改 `build.gradle` 文件，就可以完成 SDK 集成：
![](https://qcloudimg.tencent-cloud.cn/raw/7de67c57e87f2803217b77ed308d537d.png)

1. 打开工程根目录下的 build.gradle，添加mavenCentral库。
```xml
repositories {
    mavenCentral()
}
```

2. 打开 app 下的 build.gradle，在 dependencies 中添加 LiteAVSDK_Player 的依赖。
```
dependencies {
  // 此配置默认集成 LiteAVSDK_Player 最新版本
	implementation 'com.tencent.liteav:LiteAVSDK_Player:latest.release'
  // 集成历史版，如：10.7.0.13038 版本，可通过下面方式集成
  // implementation 'com.tencent.liteav:LiteAVSDK_Player:10.7.0.13038'
}
```
3. 在 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK_Player 支持 armeabi 、 armeabi-v7a  和 arm64-v8a）。
```
defaultConfig {
	ndk {
		abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
	}
}
```
4. 单击![](https://main.qcloudimg.com/raw/d6b018054b535424bb23e42d33744d03.png) Sync Now 按钮同步 SDK，如果您的网络连接 mavenCentral 没有问题，很快 SDK 就会自动下载集成到工程里。

### 方法二：手动下载（aar）
如果您的网络连接 mavenCentral 有问题，也可以手动下载 SDK 集成到工程里：
1. 下载 [LiteAVSDK_Player](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_Android_latest.zip) ，下载完成后进行解压。
2. 将下载文件解压之后 SDK 目录下的 aar 文件拷贝到工程的 **app/libs** 目录下：
    ![](https://qcloudimg.tencent-cloud.cn/raw/ab00ad0f12a271750d6f84f7333f8cd3.png)
3. 在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
    ![](https://main.qcloudimg.com/raw/726771558714a2b4fae8dc1a59c33ffc.png) 
4. 添加 LiteAVSDK_Player 依赖，在 app/build.gradle 中，添加引用 aar 包的代码。
    ![](https://qcloudimg.tencent-cloud.cn/raw/ac9ab42dda8992d435832c605f1e6798.png)
```
implementation(name:'LiteAVSDK_Player_10.7.0.13038', ext:'aar')
```
5. 在 `app/build.gradle` 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK_Player 支持 armeabi 、armeabi-v7a 和 arm64-v8a）。
```
defaultConfig {
	ndk {
		abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
	}
}
```
6. 单击 Sync Now 按钮同步 SDK，完成 LiteAVSDK 的集成工作。

## 集成 SDK（jar）
如果您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 LiteAVSDK：

1. 下载  [LiteAVSDK_Player](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_Android_latest.zip) ，下载完成后进行解压。在 SDK 目录下找到 `LiteAVSDK_Player_xxx.zip`（其中 `xxx` 为 LiteAVSDK 的版本号），解压后得到 libs 目录，里面主要包含 jar 文件和 so 文件夹，文件清单如下：
    ![](https://qcloudimg.tencent-cloud.cn/raw/fce689e5b968323c6f75a7f3ce08b488.png)

  如果你还需要 armeabi 架构 so，复制一份 armeabi-v7a 目录，重命名为 armeabi 即可。

2. 将解压得到的 jar文件和 armeabi、armeabi-v7a、arm64-v8a 文件夹拷贝到 `app/libs` 目录下。
    ![](https://main.qcloudimg.com/raw/d9b6339cb52fb85afda42de6001be337.png)
3. 在 `app/build.gradle` 中，添加引用 jar 库的代码。
    ![](https://main.qcloudimg.com/raw/695520309d9a01b19ce2f50439a42890.png)      
```
dependencies{
	implementation fileTree(dir:'libs',include:['*.jar'])
}
```
4. 在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/6c68b846f6f7258ae4d96bc1d95d7816.png)
5. 在 `app/build.gradle` 中，添加引用 so 库的代码。
![](https://main.qcloudimg.com/raw/e0f2f39c5f53a9fd5ca084febdd4e637.png)
6. 在 `app/build.gradle` 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 支持 armeabi、armeabi-v7a 和 
```
defaultConfig {
    ndk {
        abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
    }
}
```
7. 单击 Sync Now 按钮同步 SDK，完成 LiteAVSDK 的集成工作。

## 配置 App 打包参数
![](https://main.qcloudimg.com/raw/dabfd69ee06e4d38bb3b51fc436c0ad1.png)
```
packagingOptions {
	pickFirst '**/libc++_shared.so'
	doNotStrip "*/armeabi/libYTCommon.so"
	doNotStrip "*/armeabi-v7a/libYTCommon.so"
	doNotStrip "*/x86/libYTCommon.so"
	doNotStrip "*/arm64-v8a/libYTCommon.so"
} 
```

**注意：**如果之前没有使用过9.4以及更早版本的 SDK 的 [下载缓存功能](https://cloud.tencent.com/document/product/881/20216#13.E3.80.81.E7.A6.BB.E7.BA.BF.E7.BC.93.E5.AD.98)（TXVodDownloadManager 中的相关接口），并且不需要在9.5及后续 SDK 版本播放9.4及之前缓存的下载文件，可以不需要该功能的 so 文件，达到减少安装包的体积，例如：在9.4及之前版本使用了 TXVodDownloadManager 类的 setDownloadPath 和 startDownloadUrl 函数下载了相应的缓存文件，并且应用内存储了 TXVodDownloadManager 回调的 getPlayPath 路径用于后续播放，这时候需要 libijkhlscache-master.so 播放该 getPlayPath 路径文件，否则不需要。可以在 app/build.gradle 中添加：

```xml
// 新客户集成 SDK 建议把下面的脚本加上，可以优化包体积
packagingOptions {
    exclude "lib/armeabi/libijkhlscache-master.so"
    exclude "lib/armeabi-v7a/libijkhlscache-master.so"
    exclude "lib/arm64-v8a/libijkhlscache-master.so"
}
```

## 配置 App 权限

在 AndroidManifest.xml 中配置 App 的权限，LiteAVSDK 需要以下权限：

```
<!--网络权限-->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<!--存储-->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

## 设置混淆规则
在 proguard-rules.pro 文件中，将 LiteAVSDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```

## 配置 License 授权

单击 [License 申请](https://console.cloud.tencent.com/vcube) 获取测试用 License，不配置 License 将会播放时视频失败，具体操作请参见 [测试版 License](https://cloud.tencent.com/document/product/1449/56981#test)。您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。

在您的 App 调用 SDK 相关功能之前（建议在 Application类中）进行如下设置：

```java
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licence url
        String licenceKey = ""; // 获取到的 licence key
        TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);
        TXLiveBase.setListener(new TXLiveBaseListener() {
            @Override
            public void onLicenceLoaded(int result, String reason) {
                Log.i(TAG, "onLicenceLoaded: result:" + result + ", reason:" + reason);
            }
        });
    }
}
```

## 查看方法

License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用如下方法查看 License 信息：

```java
TXLiveBase.getInstance().getLicenceInfo();
```

## 常见问题

1. 项目里面同时集成了直播 SDK/实时音视频/播放器等 LiteAVSDK 系列的多个 SDK 报符号冲突问题怎么解决？

如果集成了2个或以上产品（直播、播放器、TRTC、短视频）的 LiteAVSDK 版本，编译时会出现库冲突问题，因为有些 SDK 底层库有相同符号文件，这里建议只集成一个全功能版 SDK 可以解决，直播、播放器、TRTC、短视频这些都包含在一个 SDK 里面。具体请参见 [SDK 下载](https://vcube.cloud.tencent.com/home.html)。
