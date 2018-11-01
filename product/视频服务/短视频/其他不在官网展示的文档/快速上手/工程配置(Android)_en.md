## 1. System Requirement

SDK can run on Android 4.0.3 (API 15) or above. However, hardware encoding can be enabled only on Android 4.3 (API 18) or above.

## 2. Development Environment

SDK development environment is described below. The App development environment does not need to be consistent with that of SDK, but it must be compatible with:

- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_25.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21
- Android Studio (Android Studio is recommended, but you can also use Eclipse + ADT)

## 3. Integration Guide (aar)

### 3.1 New Project
![](//mc.qcloudimg.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 3.2 Copy Files

Put the aar package under the project libs directory

### 3.3 Project Configuration
- Add the code that references aar package to build.gradle under the project app directory:
```
dependencies {
      compile fileTree(dir: 'libs', include: ['*.jar'])
      // Import the short video SDK aar
      compile(name: 'LiteAVSDK_UGC_3.4.1757', ext: 'aar')
  }
```

- Add flatDir to build.gradle under the project directory, and specify the local library in it:
```
allprojects {
      repositories {
          jcenter()
          flatDir {
              dirs 'libs'
          }
      }
  }
```

- Specify ndk-compatible architecture in defaultConfig of build.gradle under the project directory:
```
   defaultConfig {
        applicationId "com.tencent.liteav.demo"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode 1
        versionName "2.0"

        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
    }
```

- Finally, compile Rebuild Project.

## 4 Integration Guide (jar)

### 4.1 Library Description

Decompress LiteAVSDK_UGC_3.4.1757.zip to get the libs directory, which mainly includes a jar file, as shown below:

| jar file                           | Description                      |
| ---------------------------- | ----------------------- |
| liteavsdk.jar                | Mini LVB SDK android core library          |


For library related to the upload of short videos, jar files and a so file for uploading short videos can be found in the **Demo\app\libs** directory, as shown below:

| jar file                           | Description                      |
| ---------------------------- | ----------------------- |
| sha1utils.jar                | JAR package that implements SHA calculation of files to be uploaded. This component is used for short video upload (TXUGCPublish) feature |
| cos-sdk-android.1.4.3.11.jar | File upload package of Tencent Cloud COS. This component is used for short video upload (TXUGCPublish) feature |
| okio-1.6.0.jar               | An excellent open source network I/O component      |
| okhttp-3.2.0.jar             | An excellent open source HTTP component          |

| so file                           | Description                      |
| ---------------------------- | ----------------------- |
| libTXSHA1.so                 | JAR package that implements SHA calculation of files to be uploaded. This component is used for short video upload (TXUGCPublish) feature |


### 4.2 Copy Files

If no jni loading path is previously specified in your project, we recommend that you put the jar package and so library under the **/src/main/jniLibs** directory, which is the default jni loading directory of android studio.

### 4.3. Project Configuration

Add the code that references jar package and so library to build.gradle under the project app directory:

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    // Import Tencent Cloud LVB SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
}
```
## 5. Configure App Permissions

Configure App permissions in AndroidManifest.xml. Generally, video Apps require the following permissions:

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

## 6. Verify

Call the SDK API in the project to get SDK version information and verify whether the project is correctly configured.

### 6.1 Reference SDK

Reference the class of SDK in MainActivity.java:

```
import com.tencent.rtmp.TXLiveBase;
```

### 6.2 Call API

Call the API getSDKVersioin in onCreate to get version number:
```
String sdkver = TXLiveBase.getSDKVersionStr();
Log.d("liteavsdk", "liteav sdk version is : " + sdkver);
```

### 6.3 Compile and Run
The demo project can be compiled successfully if all of the above steps are correctly performed. If you run the project, you can see the following log information in logcat:
`09-26 19:30:36.547 19577-19577/ D/liteavsdk: liteav sdk version is : 3.4.1757`

<a name="online_so">&nbsp;</a>

## 7. Print LOG

Configure whether to print log in the console and set the log level in TXLiveBase. Codes are described as follows:
- **setConsoleEnabled**
Configure whether to print the output of SDK in the Android Studio console.

- **setLogLevel**
Configure whether to allow SDK to print local log. By default, SDK writes log to the **log / tencent / liteav** folder on sdcard.
For technical support, you are recommended to enable the switch and provide the log file after a problem occurs. Thank you for your support.

- **View log file**
To reduce the storage volume of logs, Mini LVB SDK encrypts the log files stored locally and limits the number of logs. Therefore, you need to use the log [Decompression Tool](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) to view the text content of log.


```
TXLiveBase.setConsoleEnabled(true);
TXLiveBase.setLogLevel(TXLiveConstants.LOG_LEVEL_DEBUG);
```

## 8. Troubleshooting
### 8.1 Compilation
If the following errors occur when you compile/run the project after importing the SDK into it:

```
Caused by: android.view.InflateException: 
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

Find the problem by following the steps below:

- Check whether you have placed the jar package and so library into the jniLibs directory.

- If you are using the full version of aar integration mode, check whether the x64 "so" library has been filtered out in defaultConfig of build.gradle under the project directory. This is because the acoustic component library used by the joint broadcasting feature in full version does not support mobile phones with x64 architecture at the moment.
```
 defaultConfig {
        applicationId "com.tencent.liteav.demo"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode 1
        versionName "2.0"

        ndk {
            abiFilters "armeabi", "armeabi-v7a"
        }
  }
```

- Check the proguard rules to confirm that the SDK-related package names have been added to the non-proguard list.
```
-keep class com.tencent.** { *; }
```

### 8.2 Short Video Publishing
After a file is published, no error message or callback response is returned. The following appears when the log is printed:
```
 TaskManager: ExecutionException
```

This is because the libTXSHA1.so used for upload has not been properly integrated into the project. For more information, please see [Integration Guide](https://cloud.tencent.com/document/product/584/11631#4-.E9.9B.86.E6.88.90.E6.94.BB.E7.95.A5.EF.BC.88jar.EF.BC.89).




