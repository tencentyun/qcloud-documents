## 1下载SDK


您可以在腾讯云官网下载移动端 [直播SDK](https://www.qcloud.com/document/product/454/7873)。
目前直播 SDK 有两个版本：

- 旧版 SDK： 目前版本为 2.0.5.3469
- 新版 SDK： 目前版本为 3.0.1185

如果您是刚集成直播功能或者想更新 SDK 版本，建议你使用新版 SDK。因旧版 SDK 目前不再维护，新版 SDK 在旧版 SDK 的基础上进行重构并做了许多优化，具体可以看下[版本说明](https://www.qcloud.com/document/product/454/7873)。

## 2 库说明
### 2.1 旧版本
解压压缩包后得到libs目录，里面主要包含so文件和jar文件，文件清单如下：

| 文件 | 说明 |
|---------|---------|
| txrtmpsdk.jar | 直播 SDK java层封装 |
| ugcupload.jar | UGC 上传文件到点播系统 jar 包|
| sha1utils.jar | UGC 计算上传文件的 SHA 值 jar 包|
| cos-sdk-android.1.4.3.6.jar |  对象存储 COS 相关的 jar 包|
| okio-1.6.0.jar | 网络操作 I/O 库 |
| okhttp-3.2.0.jar | 网络请求库 |
| libtxrtmpsdk.so| 直播SDK 核心组件|
| libtraeimp-rtmp-armeabi.so | 连麦功能库 |
| libstlport_shared.so  | 连麦功能库 |
| libTXSHA1.so | UGC 计算上传文件的 SHA 值 |

如果您暂时不需要短视频功能，您可以下载完整版，导入以下包即可。

| 文件 | 说明 |
|---------|---------|
| txrtmpsdk.jar | 直播 SDK java层封装 |
| ugcupload.jar | UGC 上传文件到点播系统 jar 包|
| libtraeimp-rtmp-armeabi.so | 连麦功能库 |
| libstlport_shared.so  | 连麦功能库 |
| libtxrtmpsdk.so| 直播SDK 核心组件|

如果您暂时不需要连麦以及短视频功能，您可以下载精简版，导入以下包即可。

| 文件 | 说明 |
|---------|---------|
| txrtmpsdk.jar | 直播 SDK java层封装 |
| ugcupload.jar | UGC 上传文件到点播系统 jar 包|
| libtxrtmpsdk.so| 直播SDK 核心组件|

### 2.2 新版本
| 版本类型 | 库文件 |
|---------|---------|
| 直播精简版 | LiteAVSDK_Smart.aar |
| 独立播放器版 | 版本暂时没有发布 |
| 短视频功能版 | LiteAVSDK_UGC.aar |
| 全功能专业版 | LiteAVSDK_Professional.aar |
| 商用企业版 | [需联系商务](https://www.qcloud.com/document/product/454/9020) |



## 3 支持的平台
- SDK支持Android 4.0(API 14)及以上系统

## 4 开发环境
以下是SDK的开发环境，APP开发环境不需要与SDK一致，但要保证兼容：
- Android NDK: android-ndk-r10e
- Android SDK Tools: android-sdk_r21.1.2
 - minSdkVersion: 14
 - targetSdkVersion: 21
- Android Studio（推荐您也使用Android Studio，当然您也可以使用Eclipse+ADT）

## 5 Android Studio环境配置

### 5.1 新建Android工程
![](//mccdn.qcloud.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 5.2 拷贝文件

- 旧版本
如果您的工程之前没有指定过jni的加载路径，推荐您将刚才解压的 jar 包和so 库在/src/main/jniLibs目录下，这是android studio默认的jni加载目录。

- 新版本
将 aar 包放在 libs 目录下即可



### 5.3 工程配置
- 旧版本
在工程 app 目录下的 build.gradle 中，添加引用 jar 包和 so 库的代码。

```Java
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    //导入腾讯云直播SDK jar
    compile fileTree(dir: 'src/main/jniLibs', include: ['*.jar'])
}
```

- 新版本
在工程 app 目录下的 build.gradle 中，添加引用 aar 包的代码。

```Java
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
        //导入腾讯云直播SDK jar
    compile(name: 'LiteAVSDK_Professional', ext: 'aar')
}
```
        
### 5.4 配置APP权限
在AndroidManifest.xml中配置APP的权限，音视频类APP一般需要以下权限：

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.CALL_PHONE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

### 6.验证
在工程中调用SDK接口，获取SDK版本信息，以验证工程设置是否正确。

**6.1 引用SDK**
在MainActivity.java中引用SDK的class:

```
import com.tencent.rtmp.TXLivePusher;
```

**6.2  在onCreate中调用getSDKVersion接口获取版本号：**

```
int[] sdkver = TXLivePusher.getSDKVersion();
if (sdkver != null && sdkver.length >= 3) {
    Log.d("rtmpsdk","rtmp sdk version is:" + sdkver[0] + "." + sdkver[1] + "." + sdkver[2]);
}
```

**6.3  编译运行**
如果前面各步骤都操作正确，demo工程将顺利编译通过，运行之后将在logcat中看到如下log信息：

```
08-09 14:53:26.256 21404-21404/? D/rtmpsdk: rtmp sdk version is:3.0.1185
```

### 7.问题排查
如果您将 SDK 导入到您的工程，编译运行出现类似以下错误：

```
Caused by: android.view.InflateException: 
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

可以按照以下流程来排查问题
**7.1**. 确认是否已经将 SDK 中的 jar 包和 so 库放在 jnilib 目录下.
**7.2**.  如果您使用完整版本，确认下是否将 x64 架构的 so 库过滤掉。因为完整版本中的连麦功能暂时不支持 x64 架构的手机。
```
    buildTypes {
        release {
            minifyEnabled  false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'

            ndk {
                // 需要将 armeabi-x64 架构过滤掉
                abiFilters "armeabi", "armeabi-v7a"
            }
        }
    }
```
**7.3**.  检查下混淆规则，确认是否将 SDK 相关的类也给混淆了。
**7.4**   在集成过程中，通过输出 SDK 上报的日志来排查问题
建议在 Application 中实现 ITXLiveBaseListener 接口并实现 OnLog() 方法，具体代码如下：
```Java
public class DemoApplication extends Application implements ITXLiveBaseListener {
    @Override
    public void onCreate() {
        super.onCreate();
        TXLiveBase.getInstance().listener = this;
    }

    @Override
    public void OnLog(int level, String module, String log) {
        switch (level)
        {
            case TXLiveConstants.LOG_LEVEL_ERROR:
                Log.e(module, log);
                break;
            case TXLiveConstants.LOG_LEVEL_WARN:
                Log.w(module, log);
                break;
            case TXLiveConstants.LOG_LEVEL_INFO:
                Log.i(module, log);
                break;
            case TXLiveConstants.LOG_LEVEL_DEBUG:
                Log.d(module, log);
                break;
            default:
                Log.d(module, log);
        }
    }
}
```
