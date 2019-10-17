## Download SDK
You can download the [LVB SDK](https://cloud.tencent.com/document/product/454/7873) for mobile devices from Tencent Cloud's official website. Decompress the downloaded file to acquire the libs directory, which mainly includes "so" and "jar" files. Files are listed below:

| File | Description |
|---------|---------|
| txrtmpsdk.jar | SDK Java layer encapsulation |
| libtxrtmpsdk.so | SDK core components |

## Supported Platform
- Android 4.0 (API 14) systems and above

## Development Environment
The SDK development environment is described below. The App development environment does not need to be consistent with that of SDK, but they must be compatible:
- Android NDK:  android-ndk-r10e
- Android SDK Tools:  android-sdk_r21.1.2
 - minSdkVersion:  14
 - targetSdkVersion:  21
- Android Studio (while Android Studio is recommended, you can also choose to use Eclipse + ADT)

## Android Studio Environment Configuration

### 1. Create Android Project
![](//mccdn.qcloud.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 2. Copy Files
If your project doesn't have a previously specified jni loading path, we recommend that you put the files under the /src/main/jniLibs directory, which is the default jni loading directory of Android studio.**  If you have specified the jni loading path (through gradle syntax: the sourceSets syntax or android.sources syntax), please copy the SDK related files mentioned above to this directory.**
![](//mccdn.qcloud.com/static/img/a776560bd0c3c156c7271dedd58cb9ac/image.png)

### 3. Import jar Package
Find the newly created jniLibs directory in the Android Studio project. Expand the directory, and you will see txrtmpsdk.jar. Right-click on it and select "Add As Library..."
![](//mccdn.qcloud.com/static/img/86d98492636122ed9cae898b7bff1920/image.png)
Once the package is imported, you will find that the following line of script is generated automatically in build.gradle:
![](//mccdn.qcloud.com/static/img/c83f9882d434f7fd51d4ca942f159138/image.png)
		
### 4. Configure APP Permissions
Configure App permissions in AndroidManifest.xml. Generally, audio and video Apps require the following permissions:

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

### 5. Verify
Call the SDK API in the project to acquire SDK version information and verify if the project settings are correct.

**1. Reference the SDK**
Reference the class of SDK in MainActivity.java:

```
import com.tencent.rtmp.TXLivePusher;
```

**2. Call the getSDKVersion API in onCreate to acquire version number:**

```
int[] sdkver = TXLivePusher.getSDKVersion();
if (sdkver != null && sdkver.length >= 3) {
    Log.d("rtmpsdk","rtmp sdk version is:" + sdkver[0] + "." + sdkver[1] + "." + sdkver[2]);
}
```

**3. Compile/Run**
The demo project can be compiled successfully if all of the above steps are correctly performed. If you run the project, you will see the following log information in logcat:

```
07-13 20:25:05.099 26119-26119/? D/rtmpsdk: rtmp sdk version is:1.5.188
```

### 6. Troubleshoot
If the following errors occur when you compile/run the project after importing the SDK into it:

```
Caused by: android.view.InflateException: 
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

Find the problem by following the steps below
**1**. Check if you have placed the "jar" package and "so" library into the jnilib directory.
**2**.  If you're using the full version, check if the x64 "so" library has been filtered out. This is because the joint broadcasting feature in full version does not support mobile phones with x64 architecture at the moment.
```
    buildTypes {
        release {
            minifyEnabled  false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'

            ndk {
                // filter out armeabi-x64 library
                abiFilters "armeabi", "armeabi-v7a"
            }
        }
    }
```
**3**.  Look at the proguard rules and check if you have obfuscated RTMP SDK related classes too.

