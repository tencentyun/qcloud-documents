## 下载SDK
您可以在腾讯云官网下载移动端 [直播SDK](https://www.qcloud.com/document/product/454/7873)，解压后得到libs目录，里面主要包含so文件和jar文件，文件清单如下：

| 文件 | 说明 |
|---------|---------|
| txrtmpsdk.jar | SDK java层封装 |
| libtxrtmpsdk.so| SDK 核心组件|

## 支持的平台
- SDK支持Android 4.0(API 14)及以上系统

## 开发环境
以下是SDK的开发环境，APP开发环境不需要与SDK一致，但要保证兼容：
- Android NDK: android-ndk-r10e
- Android SDK Tools: android-sdk_r21.1.2
 - minSdkVersion: 14
 - targetSdkVersion: 21
- Android Studio（推荐您也使用Android Studio，当然您也可以使用Eclipse+ADT）

## Android Studio环境配置

### 1.新建Android工程
![](//mccdn.qcloud.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 2.拷贝文件
如果您的工程之前没有指定过jni的加载路径，我们推荐您放在/src/main/jniLibs目录下，这是android studio默认的jni加载目录。**如果您已经指定过jni的加载路径（通过gradle的语法：sourceSets语法或者android.sources语法），请将上文提到的SDK相关文件拷入到该目录下。**
![](//mccdn.qcloud.com/static/img/a776560bd0c3c156c7271dedd58cb9ac/image.png)

### 3.导入jar包
在Android Studio工程中找到刚才新建的jniLibs目录，展开目录，可以看到txrtmpsdk.jar，点击右键选择“Add As Library...”
![](//mccdn.qcloud.com/static/img/86d98492636122ed9cae898b7bff1920/image.png)
导入之后，可以看到build.gradle中自动生成以下这一行脚本：
![](//mccdn.qcloud.com/static/img/c83f9882d434f7fd51d4ca942f159138/image.png)
		
### 4.配置APP权限
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

### 5.验证
在工程中调用SDK接口，获取SDK版本信息，以验证工程设置是否正确。

**1. 引用SDK**
在MainActivity.java中引用SDK的class:

```
import com.tencent.rtmp.TXLivePusher;
```

**2. 在onCreate中调用getSDKVersion接口获取版本号：**

```
int[] sdkver = TXLivePusher.getSDKVersion();
if (sdkver != null && sdkver.length >= 3) {
    Log.d("rtmpsdk","rtmp sdk version is:" + sdkver[0] + "." + sdkver[1] + "." + sdkver[2]);
}
```

**3. 编译运行**
如果前面各步骤都操作正确，demo工程将顺利编译通过，运行之后将在logcat中看到如下log信息：

```
07-13 20:25:05.099 26119-26119/? D/rtmpsdk: rtmp sdk version is:1.5.188
```

### 6.问题排查
如果您将 SDK 导入到您的工程，编译运行出现类似以下的错误：

```
Caused by: android.view.InflateException: 
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

可以按照以下流程来排查问题
**1**. 确认是否已经将 SDK 中的 jar 包和 so 库放在 jnilib 目录下.
**2**.  如果您使用完整版本，确认下是否将 x64 架构的 so 库过滤掉。因为完整版本中的连麦功能暂时不支持 x64 架构的手机。
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
**3**.  检查下混淆规则，确认是否将 RTMP SDK 相关的类也给混淆了。
