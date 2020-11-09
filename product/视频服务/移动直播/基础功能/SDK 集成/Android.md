本文主要介绍如何快速地将腾讯云 LiteAVSDK（Android）集成到您的项目中，按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Android Studio 2.0+。
- Android 4.1（SDK API 16）及以上系统。

## 集成 SDK（aar）
您可以选择使用 Gradle 自动加载的方式，或者手动下载 aar 再将其导入到您当前的工程项目中。

### 方法一：自动加载（aar）
LiteAVSDK 已经发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。
只需要用 Android Studio 打开需要集成 SDK 的工程，然后通过简单的三个步骤修改`app/build.gradle`文件，就可以完成 SDK 集成：
![](https://main.qcloudimg.com/raw/eb6bcb3cb1dff43f459245ed9045e685.png)

- **第一步：添加 SDK 依赖**   
  在 dependencies 中添加 LiteAVSDK 的依赖。
```
dependencies {
     implementation 'com.tencent.liteavsdk:LiteAVSDK_Smart:latest.release'
}
```
或
```
dependencies {
     implementation 'com.tencent.liteavsdk:LiteAVSDK_Smart:latest.release@aar'
}
```
- **第二步：指定 App 使用架构**
  在 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 支持 armeabi 、 armeabi-v7a  和 arm64-v8a）。
```
defaultConfig {
     ndk {
         abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
     }
}
```
- **第三步：同步 SDK**
  单击![](https://main.qcloudimg.com/raw/d6b018054b535424bb23e42d33744d03.png) Sync Now 按钮，如果您的网络连接 jcenter 没有问题，很快 SDK 就会自动下载集成到工程里。

### 方法二：手动下载（aar）
如果您的网络连接 jcenter 有问题，也可以手动下载 SDK 集成到工程里：

- **第一步：下载 LiteAVSDK**
   下载 [LiveAVSDK](https://cloud.tencent.com/document/product/454/7873) ，下载完成后进行解压。
 
- **第二步：拷贝 LiteAVSDK 到工程目录**  
  将下载文件解压之后 SDK 目录下的 aar 文件拷贝到工程的 **app/libs** 目录下：
  ![](https://main.qcloudimg.com/raw/0550edd82139cbbfaba3cc656b4fdd9e.png)
  
- **第三步：指定本地仓库路径**
  在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
  ![](https://main.qcloudimg.com/raw/726771558714a2b4fae8dc1a59c33ffc.png)
  
- **第四步：添加 LiteAVSDK 依赖**   
  在 app/build.gradle 中，添加引用 aar 包的代码。
  ![](https://main.qcloudimg.com/raw/2333ec86f332907e7bf45b6cf83ee7b3.png)
```
implementation(name:'LiteAVSDK_Smart_6.4.7265', ext:'aar')
```

- **第五步：指定 App 使用架构**
  在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 支持 armeabi 、armeabi-v7a 和 arm64-v8a）。
```
defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
        }
    }
```

- **第六步：同步 SDK**
  单击 Sync Now按钮，完成 LiteAVSDK 的集成工作。

## 集成 SDK（jar）
如果您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 LiteAVSDK：

- **第一步：下载解压 LiteAVSDK**
  下载 [LiveAVSDK](https://cloud.tencent.com/document/product/454/7873) ，下载完成后进行解压。在 SDK 目录下找到 `LiteAVSDK_Smart_xxx.zip`（其中 xxx 为 LiteAVSDK 的版本号）：

  ![](https://main.qcloudimg.com/raw/aae5879bccd31e8c082eebc24aa4ff7c.png)

  解压后得到 libs 目录，里面主要包含 jar 文件和 so 文件夹，文件清单如下：
  ![](https://main.qcloudimg.com/raw/f460962b610f2fd80f38ced46c26e5a5.png)

- **第二步：拷贝 SDK 文件到工程目录**
  将解压得到的 jar文件和 armeabi、armeabi-v7a、arm64-v8a 文件夹拷贝到 app/libs 目录下。
  ![](https://main.qcloudimg.com/raw/d9b6339cb52fb85afda42de6001be337.png)

- **第三步：引用 jar 库**
  在 app/build.gradle 中，添加引用 jar 库的代码。
![](https://main.qcloudimg.com/raw/695520309d9a01b19ce2f50439a42890.png)			
```
dependencies{
		implementation fileTree(dir:'libs',include:['*.jar'])
}
```


- **第四步：引用 so 库**
  在 app/build.gradle 中，添加引用 so 库的代码。
  ![](https://main.qcloudimg.com/raw/e0f2f39c5f53a9fd5ca084febdd4e637.png)


- **第五步：指定 App 使用架构**
  在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构(目前 LiteAVSDK 支持 armeabi 、 armeabi-v7a  和 arm64-v8a)  。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
        }
    }
```

- **第六步：同步 SDK**
  单击 Sync Now 按钮，完成 LiteAVSDK 的集成工作。

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

## 配置 App 权限
在 AndroidManifest.xml 中配置 App 的权限，LiteAVSDK 需要以下权限：

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

## 配置 License 授权

单击 [License 申请](https://console.cloud.tencent.com/live/license) 获取测试用 License，具体操作请参见 [测试版 License](https://cloud.tencent.com/document/product/454/34750#.E6.B5.8B.E8.AF.95.E7.89.88-license)。您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。

在您的 App 调用企业版 SDK 相关功能之前（建议在 Application类中）进行如下设置：

```java
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licence url
        String licenceKey = ""; // 获取到的 licence key
        TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);
    }
}
```



## 设置混淆规则
在 proguard-rules.pro 文件中，将 LiteAVSDK 相关类加入不混淆名单：

```
-keep class com.tencent.** { *; }
```
