## 1. SDK Information

You can update the [Mini LVB SDK](https://cloud.tencent.com/document/product/454/7873) on Tencent Cloud's official website, which has the following versions:

| Version | Feature |
| ------ | ---------------------------- |
| LVB simplified version | Supports push, LVB, and VOD |
| Independent player version | Supports LVB and VOD |
| Short video feature version | Supports short video and VOD |
| Full-featured professional version | Supports push, LVB, VOD, joint broadcasting, and short video |
| Commercial enterprise version | Motion effect sticker, eyes beautifying and face slimming, and green screen keying-out features are added on the basis of full-featured professional version |

In professional version, for example, the decompressed SDK is composed as follows:

![](//mc.qcloudimg.com/static/img/1244d459b1719650ee80b7b1ab9e0be1/image.png)


| File Name | Description | 
|---------|---------|
|  LiteAVSDK_Professional_3.0.1185.aar  | The SDK wrapped as aar, suitable for Android Studio users | 
|  LiteAVSDK_Professional_3.0.1185.zip  | The SDK wrapped as jar + so, suitable for Eclipse users. If fully wrapping the SDK into APK may increase the size of the installation package, you can upload the so files in the zip package to the server, and download them as needed to decrease the size of APK. For more information, please see [How to decrease the size of APK?](#online_so) |
| Demo | The simplified demo based on aar, including a simple demonstration of UI and main SDK features. Use Android Studio to quickly import the demo and try it out. |
| API document | Click the index.html file in the folder to view all API descriptions of this SDK |

## 2. System Requirement

SDK is supported on Android 4.0.3 (API 15) or above. However, hardware encoding can be enabled only on Android 4.3 (API 18) or above.

## 3. Development Environment

The development environment of App does not need to be consistent with that of SDK, but they must be compatible. SDK development environment is described as below:

- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_25.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21
- Android Studio (Android Studio is recommended. You can also use Eclipse+ADT)

## 4 Integration Guide (aar)

### 4.1 New project
![](//mc.qcloudimg.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

### 4.2 Copy files

Put the aar package under the libs directory of the project.

### 4.3 Project configuration
- Add the code that references aar package to build.gradle under the app directory of the project:
```
dependencies {
      compile fileTree(dir: 'libs', include: ['*.jar'])
      //Import Tencent Cloud LVB SDK aar
      compile(name: 'LiteAVSDK_Professional_3.0.1185', ext: 'aar')
  }
```

- Add flatDir to build.gradle under the project directory, and specify the local repository:
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
            //For commercial SDK, only armeabi architecture is applicable:
            // abiFilters "armeabi",
        }
    }
```

- Compile Rebuild Project.

## 5. Integration Guide (jar)

### 5.1 Library description

Decompress LiteAVSDK_Professional_3.0.1185.zip to get the libs directory, which contains a jar file and so files, as shown below:

| SO File | Description |
| ---------------------------- | ----------------------- |
| liteavsdk.jar                 | Mini LVB SDK Android core library |
| libliteavsdk.so               | Mini LVB SDK core component |
| libsaturn.so                 | Mini LVB SDK core component |
| libtraeimp-rtmp-armeabi.so   |  Acoustic component library used in joint broadcasting |
| libstlport_shared.so          | C++ stl basic library (do not replace this library, otherwise a crash may occur due to version incompatibility) |
| libijkffmpeg.so              |  ffmpeg basic library (ijk version) for VOD playback, used to solve compatibility issues about special video formats |
| libijkplayer.so               | ijkplayer open source library for VOD playback, used to solve compatibility issues about special video formats |
| libijksdl.so                 | ijkplayer open source library for VOD playback, used to solve compatibility issues about special video formats |

### 5.2 Copy files

If no jni loading path is previously specified in your project, we recommend that you put the jar package and so libraries under the /src/main/jniLibs directory, which is the default jni loading directory of Android Studio.

### 5.3 Project configuration

Add the code that references jar package and so libraries to build.gradle under the app directory of the project:

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    //Import Tencent Cloud LVB SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
}
```
## 6. Configure App Permissions

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

## 7. Verify

Call the SDK API in the project to get SDK version information and verify whether the project is correctly configured.

### 7.1 Reference SDK

Reference the class of SDK in MainActivity.java:

```
import com.tencent.rtmp.TXLiveBase;
```

### 7.2 Call API

Call the API getSDKVersioin in onCreate to get the version number:
```
String sdkver = TXLiveBase.getSDKVersionStr();
Log.d("liteavsdk", "liteav sdk version is : " + sdkver);
```

### 7.3 Compile and run the project
The demo project can be compiled successfully if all of the above steps are correctly performed. Run the project and you can find the following log information in logcat:
`08-10 19:30:36.547 19577-19577/ D/liteavsdk: liteav sdk version is : 3.0.1185`

<a name="online_so">&nbsp;</a>
## 8. Reduce APK Size

The so files are the audio/video coding and encoding library, image processing library and acoustic component that SDK relies on. They take up much of the resources in SDK. If Mini LVB SDK is not the core feature of your App, you can upload so files online to reduce the size of APK package.

### 8.1 Upload SO files
Upload the so files in SDK package to CDN and record the download URL, such as `http://xxx.com/so_files.zip`.

### 8.2 Preparation
Before playing videos or using other SDK features, you are prompted with a loading animation indicating "Loading relevant features".

### 8.3 Download SO files
During loading process, App downloads so files from `http://xxx.com/so_files.zip` and save them in the application directory, such as the files directory under App's root directory. To ensure that this process is not affected by ISP's DNS blocking, check the integrity of the so files after downloading.

### 8.4 Load SO files
When all so files are ready, call setLibraryPath of TXLiveBase to set the destination paths of downloaded files for SDK and call relevant SDK features. SDK will then load required so files in these paths and enable related features.


## 9. Print LOG

The code used to configure whether to print log from the console and set the log level in TXLiveBase is described as follows:
- **setConsoleEnabled**
Configures whether to print the output of SDK from the Android Studio console.

- **setLogLevel**
Configures whether to allow SDK to print local log. By default, SDK writes log to the **log/tencent/liteav** folder on sdcard.
To get technical support, you are recommended to enable printing and provide the log file when a problem occurs. Thank you for your support.

- **View log file**
To reduce the storage size of logs, Mini LVB SDK encrypts local log files and limits the number of logs. Therefore, the log [decompression tool](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py) is required to view the text content of logs.


```
TXLiveBase.setConsoleEnabled(true);
TXLiveBase.setLogLevel(TXLiveConstants.LOG_LEVEL_DEBUG);
```

## Troubleshooting

If the following error occurs when you compile/run the project after importing the SDK into it:

```
Caused by: android.view.InflateException: 
Binary XML file #14:Error inflating class com.tencent.rtmp.ui.TXCloudVideoView
```

Find the problem by following the steps below:

- Check whether you have placed the jar package and so libraries into the jniLibs directory.

- If you are using the full version of aar integration mode, check whether the x64 "so" libraries have been filtered out in defaultConfig of build.gradle under the project directory. This is because the acoustic component library used for joint broadcasting in the full version is not supported in mobile phones with x64 architecture.
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




