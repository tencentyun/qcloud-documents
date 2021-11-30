## Supported Platforms
- SDK supports Android 2.3 (API 8) system or above. However, since compatibility with IM SDK is required, make sure your development environment is Android 4.0 or above.

## Development Environment
The App development environment does not need to be completely consistent with that of SDK, but it must be compatible. SDK development environment is as follows:
- JDK: jdk-8u66
- Android NDK: android-ndk-r10e
- Android SDK Tools: android-sdk_r22.6.2
	- minSdkVersion: 8
	- targetSdkVersion: 18
- Eclipse: Eclipse IDE for Java Developers
- ADT: ADT-22.6.2

## Eclipse Project Configuration
Here, we use a simple project sample to show you how to integrate SDK into Eclipse project.
### 1. About Android SDK version
The App development environment does not need to be completely consistent with that of SDK, but it must be compatible. As shown in the figure below, the lowest version supported by the App project is API 8:Android 2.2(Froyo):
![](//mccdn.qcloud.com/static/img/29a545171c4479c8f255c25ef0629b8e/image.png)

### 2. Copy SDK files
As shown in the figure below, copy all "jar" and "so" files in "libs" folder (shown in "[Download SDK](http://cloud.tencent.com/doc/product/268/%E4%B8%8B%E8%BD%BDSDK%EF%BC%88Android%EF%BC%89)") to the project folder:
- "jar" files are placed in "libs" folder;
- "so" files are placed in "libs\armeabi" folder.
![](//mccdn.qcloud.com/static/img/ba16e54bac3a2d284c81eaefe006621e/image.png)

### 3. Configure App permissions
Configure App permissions in AndroidManifest.xml. Generally, audio and video communication Apps require the following permissions:
```
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
<uses-permission android:name="android.permission.BROADCAST_STICKY" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

## Verification
Next, call the SDK API in the codes of HelloSDK to obtain SDK version information and verify whether the project is correctly configured.
### 1. Reference the SDK
Reference the class of SDK at the beginning of MainActivity.java:
`import com.tencent.av.sdk.AVContext;`

### 2. Add calling code
Add code into the onCreate method:
```
@Override
protected void onCreate(Bundle savedInstanceState) {
	super.onCreate(savedInstanceState);		
	setContentView(R.layout.activity_main);
	// Print SDK version information
  Log.i("HelloSDK", "SDK Version = " + AVContext.getVersion());
}
```
### 3. Compile and run
The HelloSDK project can be successfully compiled and run if you performed the previous steps correctly. Run the App in Debug mode. SDK version information will be printed in Eclipse's LogCat panel.
> 05-01 19:30:27.794:  I/HelloSDK(18419): SDK Version = 1.8.0.230





