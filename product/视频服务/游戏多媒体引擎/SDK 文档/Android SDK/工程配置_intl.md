Thank you for using Tencent Cloud Game Multimedia Engine (GME) SDK. This document provides project configuration that makes it easy for Android developers to debug and integrate the APIs for GME.

## SDK Preparation

You can obtain the SDK by the following way:

### Downloading SDK

Please download applicable Demo and SDK from [Downloading Instructions](https://intl.cloud.tencent.com/document/product/607/18521).

Pinpoint the SDK resource for Android on the page.

The decompressed SDK resource is composed as follows:

| File Name | Description           
| ------------- |:-------------:|
| Libs     	| SDK Libs     |

## System Requirement
The SDK is supported on Android 4.2 or above. However, hardware encoding can be enabled only on Android 4.3 (API 18) or above.

## Preparations

### Importing SDK files

Copy mobilepb.jar, tmgsdk.jar and wup-1.0.0-SNAPSHOT.jar from the SDK's libs directory to the Android project's libs directory (If there is no libs directory in the project, create one; if there is no armeabi and armeabi-v7a in it, copy them to the libs directory), as shown below:  
![](https://main.qcloudimg.com/raw/006cc0fab7b4c2f370b9b31fdbc93f90.png)

### Configuring the project

Add the code that references the library to build.gradle under the App directory of the project.  

```
sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
}
```

### Configuring App permissions

Add the following permissions in the AndroidManifest.xml file of the project:

```
  <uses-permission android:name="android.permission.RECORD_AUDIO" />
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
  <uses-permission android:name="android.permission.READ_PHONE_STATE" />
  <uses-permission android:name="android.permission.BLUETOOTH"/>
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
  <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
	```

