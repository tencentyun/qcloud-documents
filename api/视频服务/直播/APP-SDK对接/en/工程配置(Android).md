## Downloading SDK
You can download the mobile end [LVB SDK](https://www.qcloud.com/doc/api/258/6172) from the official website of Tencent Cloud, and get the libs directory after decompression. It contains the so file and jar file. The file list is as follows:

|File|Description|
|---------|---------|
| txrtmpsdk.jar | SDK Java layer encapsulation |
| libtxrtmpsdk.so| SDK core component|

## Supported Platform
- The SDK supports the Android 4.0(API 14) system and above

## Development Environment
The SDK development environment is provided below. The development environment of App does not need to be consistent with that of the SDK, but compatibility must e ensured:
- Android NDK:  android-ndk-r10e
- Android SDK Tools:  android-sdk_r21.1.2
 - minSdkVersion:  14
 - targetSdkVersion:  21
- Android Studio (you are also recommended to use Android Studio; certainly you can use Eclipse+ADT)

## Android Studio Environment Configuration

### 1. Creating an Android project
![](//mccdn.qcloud.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 2. Copying files
If the jni loading path is not specified before your project, you are recommended to put the files under th /src/main/jniLibs directory, which is the default jni loading directory of Android studio.** If you have specified the jni loading path (through the gradle grammar: the sourceSets grammar or android.sources grammar), please copy the SDK related files mentioned above to this directory.**
![](//mccdn.qcloud.com/static/img/a776560bd0c3c156c7271dedd58cb9ac/image.png)

### 3. Importing the jar package
Find the jniLibs directory created just now in the Android Studio project, and open the directory. You can see txrtmpsdk.jar. Right-click on it and select "Add As Library..."
![](//mccdn.qcloud.com/static/img/86d98492636122ed9cae898b7bff1920/image.png)
After importing, you will find that this line of script is generated automatically in build.gradle:
![](//mccdn.qcloud.com/static/img/c83f9882d434f7fd51d4ca942f159138/image.png)
		
### 4. Configuring App permissions
Configure App permissions in AndroidManifest.xml. Usually the audio and video Apps need the following permissions:

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

### 5. Verifying
Invoke the SDK API in the project to get the SDK version information and verify whether the project settings are correct.

**1. Quoting the SDK**
The class used to quote the SDK in MainActivity.java:

```
import com.tencent.rtmp.TXLivePusher;
```

**2. Invoke the getSDKVersion API in onCreate to get the version number:**

```
int[] sdkver = TXLivePusher.getSDKVersion();
if (sdkver != null && sdkver.length >= 3) {
    Log.d("rtmpsdk","rtmp sdk version is:" + sdkver[0] + "." + sdkver[1] + "." + sdkver[2]);
}
```

**3. Compiling for operation**
If the operations in all the above steps are correct, the demo project will be smoothly compiled. After operation, the following log information will be seen in logcat:

```
07-13 20:25:05.099 26119-26119/? D/rtmpsdk:  rtmp sdk version is:1.5.188
```
