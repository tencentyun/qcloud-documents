
## Short Video License Integration

- After obtaining the license for basic short video SDK, you need to rename it to TXUgcSDK.licence and copy it to a specified directory in the application.
- For Android devices, copy the license to the directory context.getExternalFilesDir(null), i.e. "/sdcard/android/data/application package name/files/" directory. For example, the path for SDK demo file is /sdcard/android/data/files/TXUgcSDK.licence.
- If your license expires, log in to Tencent Cloud VOD console to obtain the latest license and replace the license in the application with it.
>Note: The license name is "TXUgcSDK.licence" and the path is "/sdcard/android/data/application package name/files/TXUgcSDK.licence".

## System Requirement
SDK is supported on Android 4.0.3 (API 15) or above. However, hardware encoding can be enabled only on Android 4.3 (API 18) or above.

## Development Environment
App development environment does not need to be consistent with that of SDK, but they must be compatible. SDK development environment is described as below:

- Android NDK: android-ndk-r12b
- Android SDK Tools: android-sdk_25.0.2
  - minSdkVersion: 15
  - targetSdkVersion: 21
- Android Studio (Android Studio is recommended, but you can also use Eclipse + ADT)

## Integration Guide (aar)

#### 1. Create Project
![](//mc.qcloudimg.com/static/img/ac2efe1a787a8c23a9250214a84fce44/image.jpg)

#### 2. Copy File
Put the aar package under the libs directory of the project.

#### 3. Configure Project
- Add the code that references aar package to build.gradle under the App directory of the project:
```
dependencies {
      compile fileTree(dir: 'libs', include: ['*.jar'])
      // Import the short video SDK aar.
      compile(name: 'LiteAVSDK_UGC_3.9.2794', ext: 'aar')
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
        }
    }
```

- Compile Rebuild Project.

## Integration Guide (jar)

#### 1. Library Description

Decompress LiteAVSDK_UGC_3.9.2794.zip to get the libs directory, which contains a jar file and so files, as shown below:

| jar file | Description |
| ---------------------------- | ----------------------- |
| liteavsdk.jar | Mini LVB SDK Android core library |


| so file | Description |
| ---------------------------- | ----------------------- |
| libliteavsdk.so | Mini LVB SDK core component |
| libtxffmpeg.so | ffmpeg basic library (ijk version) for VOD playback, which can be used to solve compatibility issues about video format |
| libtxplayer.so | ijkplayer open source library for VOD playback, which can be used to solve compatibility issues about video format |
| libtxsdl.so | ijkplayer open source library for VOD playback, which can be used to solve compatibility issues about video format |


#### 2. Copy File
If you have not specified any jni loading path for your project, you are recommended to put the jar package and so library under the **Demo\app\src\main\jniLibs** directory, which is the default jni loading directory for Android Studio.

#### 3. Configure Project

Add the code that references jar package and so library to build.gradle under the App directory of the project:

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
    //Import Tencent Cloud LVB SDK jar
    compile fileTree(dir: 'src/main/jniLibs', includes: ['*.jar'])
}
```

## Integration of Short Video Publishing
Short video publishing feature is provided in source code.

#### 1. File Description
Short video upload library. The jar files for uploading short videos can be found in the **Demo\app\libs** directory, as shown below:

| jar file | Description |
| ---------------------------- | ----------------------- |
| cos-xml-android-sdk-1.2.jar | File upload package used for uploading short videos (TXUGCPublish) to Tencent Cloud COS |
| qcloud-core-1.2.jar | File upload package used for uploading short videos (TXUGCPublish) to Tencent Cloud COS |
| okhttp-3.2.0.jar | An excellent open source HTTP component |
| okio-1.6.0.jar | An excellent open source network I/O component |
| xstream-1.4.7.jar | An excellent open source serialization component |
| fastjson-1.1.62.android.jar | An excellent open source json component |

The source code for short video upload can be found in **Demo\app\src\main\java\com\tencent\liteav\demo\videoupload** directory.

#### 2. Copy File
Copy the jar package to **Demo\app\src\main\libs** directory, which is the default jar lib loading directory for Android Studio.
Copy the source code directory **videoupload** to the source code directory of your project and modify the package name in the source code.

#### 3. Configure Project
Add the code that references jar package to build.gradle under the App directory of the project.
```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

## Configuring App Permissions

Configure App permissions in AndroidManifest.xml. Generally, video Apps require the following permissions:

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.CALL_PHONE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" />
```

## Verification

Call the SDK API in the project to get SDK version information and verify whether the project is correctly configured.

#### 1. Reference SDK
Reference the class of SDK in MainActivity.java:

```
import com.tencent.rtmp.TXLiveBase;
```

#### 2. Call API
Call the API getSDKVersioin in onCreate to get version number:
```
String sdkver = TXLiveBase.getSDKVersionStr();
Log.d("liteavsdk", "liteav sdk version is : " + sdkver);
```

#### 3. Compile and Run Project
Demo project can be compiled successfully if all of the above steps are correctly performed. Run the project and the following log information displays in logcat:
`09-26 19:30:36.547 19577-19577/ D/liteavsdk: liteav sdk version is : 3.9.2794`

## Reducing APK Size
The so files are the audio/video coding and encoding library, image processing library and acoustic component that SDK relies on. They take up much of the resources in SDK. If short video SDK is not the core feature of your App, you can upload so files online to reduce the size of APK package.

#### 1. Upload SO Files
Upload the so files in SDK package to CDN and record the download URL such as http://xxx.com/so_files.zip.

#### 2. Preparation
Before you play videos or use other SDK features, you are prompted with a loading animation indicating "Loading relevant features".

#### 3. Download SO Files
During loading process, App downloads so files from http://xxx.com/so_files.zip and save them in the application directory, such as the files directory under App's root directory. To ensure that this process is not affected by ISP's DNS blocking, check the integrity of the so files after downloading.

#### 4. Load SO Files
When all so files are ready, call setLibraryPath of TXLiveBase to set the destination paths of download for SDK and call related SDK features. SDK will then download required so files to be loaded from these paths and enable related features.

## Printing LOG
Configure whether to print log from the console and set the log level in TXLiveBase. Codes are described as follows:
- **setConsoleEnabled**
Configure whether to print the output of SDK from the Android Studio console.
- **setLogLevel**
Configure whether to allow SDK to print local log. By default, SDK writes log to the **log / tencent / liteav** folder on sdcard.
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
- Check whether you have placed the jar package and so library into the jniLibs directory.
- If you are using the full version of aar integration mode, check whether the x64 "so" library has been filtered out in defaultConfig of build.gradle under the project directory. This is because the acoustic component library used in joint broadcasting in the full version does not support mobile phones with x64 architecture.
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

