## 一、支持的平台
- SDK支持Android 2.3（API 8）及以上系统，单由于需要兼容IM SDK，请保证开发环境在Android 4.0以上

## 二、开发环境
APP的开发环境不需要与SDK的完全一致，但要保证兼容。以下是SDK的开发环境：
- JDK：jdk-8u66
- Android NDK：android-ndk-r10e
- Android SDK Tools：android-sdk_r22.6.2
	- minSdkVersion：8
	- targetSdkVersion：18
- Eclipse：Eclipse IDE for Java Developers
- ADT：ADT-22.6.2

## 三、Eclipse工程设置
下面通过一个简单的示例工程，说明如何在Eclipse工程中集成SDK。
### 1、关于Android SDK版本
APP的开发环境不需要与SDK的完全一致，但要保证兼容。如下图所示，APP工程最低支持API 8:Android 2.2(Froyo)版本：
![](//mccdn.qcloud.com/static/img/29a545171c4479c8f255c25ef0629b8e/image.png)

### 2、拷贝SDK文件
如下图所示，将《[下载SDK](http://cloud.tencent.com/doc/product/268/%E4%B8%8B%E8%BD%BDSDK%EF%BC%88Android%EF%BC%89)》中那个libs文件夹下的所有jar和so文件拷贝到工程文件夹：
- jar文件都放在libs文件夹；
- so文件都放在libs\armeabi文件夹。
![](//mccdn.qcloud.com/static/img/ba16e54bac3a2d284c81eaefe006621e/image.png)

### 3、配置APP权限
在AndroidManifest.xml中配置APP的权限，音视频通信类的APP一般需要以下权限：
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

## 四、验证
下面在HelloSDK的代码中，调用SDK的接口，获取SDK版本信息，以验证工程设置是否正确。
### 1、引用SDK
在MainActivity.java开头引用SDK的class：
`import com.tencent.av.sdk.AVContext;`

### 2、添加调用代码
在onCreate方法中添加代码：
```
@Override
protected void onCreate(Bundle savedInstanceState) {
	super.onCreate(savedInstanceState);		
	setContentView(R.layout.activity_main);
	// 打印SDK的版本信息
  Log.i("HelloSDK", "SDK Version = " + AVContext.getVersion());
}
```
### 3、编译运行
如果前面各个步骤都操作正确的话，HelloSDK工程应该可以顺利编译通过。在Debug模式下运行APP，Eclipse的LogCat窗格会打印出SDK的版本信息。
> 05-01 19:30:27.794: I/HelloSDK(18419): SDK Version = 1.8.0.230




