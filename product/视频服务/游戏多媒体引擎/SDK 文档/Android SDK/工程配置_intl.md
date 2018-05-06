Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes project configuration for Android development so that Android developers can easily debug and access APIs for Tencent Cloud GME.

## SDK Acquisition
You can obtain the SDK as follows.

### Download the SDK. 
Click the Tencent Cloud [Game Multimedia Engine](https://cloud.tencent.com/product/tmg?idx=1).  
![](https://main.qcloudimg.com/raw/4adb8befc9875a0823d1512f28ae046d.png)

On the displayed page, click "Developer Resources". Download the SDK resource package for Android.
![](https://main.qcloudimg.com/raw/1792e4d44a0db1bf6a0f6da752a33056.png)

Decompress the downloaded SDK resource package. The following table describes the folder in the package.

|Folder Name       | Description           
| ------------- |:-------------:|
| libs     	| Development kit **libs**.     |

## OS Requirements
The SDK can be run in Android 4.0.3 (API 15) and later versions, but hardcoding is supported only in versions later than Android 4.3 (API 18).

## Preparation
### Import the SDK files.  
Copy the **mobilepb.jar**, **tmgsdk.jar**, and **wup-1.0.0-SNAPSHOT.jar** files from the development kit folder **libs** into the **libs** folder of the Android project, as shown in the following figure. (If there is no **libs** folder in the Android project, create one. If there are no **armeabi** and **armeabi-v7a** folders in the Android project, copy these two folders from the development kit folder **libs** as well.)  
![](https://main.qcloudimg.com/raw/2d35214a4bda9fdd36de0527a6bfa0e7.png)

### Configure the project.  
In the **build.gradle** file under **app** in the Android project, add the code of the referenced library.  
```
sourceSets {
        main {
            jniLibs.srcDirs = ['libs']
        }
}
```  

### Configure application permissions.  
Add the following permissions to the **AndroidManifest.xml** file of the Android project.
```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
