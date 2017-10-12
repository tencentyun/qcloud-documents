## 1. Download SDK

Decompress the package, you'll see two demos, one for one-on-one communication and one for multi-people communication.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-1.png)

The multi-people communication demo project is created through Eclipse.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-2.png)

The apk package is located under the bin directory which can be used to install the demo directly.

Operation flow charts and API documents are located under the doc directory.

"jar" and "so" files needed for SDK integration are located under the libs directory.

## 2. Create Project

Currently, AV SDK is supported for Android 2.3 or above. However, since compatibility with IM SDK is required, make sure your development environment is **Android 4.0** or above.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-3.png)

## 3. SDK Integration

SDK libraries are provided in the form of jar files and dynamic link libraries (so). Place the so files under <project name>/libs/armeabi and place eup_1.9.2__allproguad_rqdp.jar, imsdk.jar, qavsdk.jar under /libs. Refresh Eclipse and they will be automatically added to project reference.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-4.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-5.png)

> Note: Uncheck **Force error when external jars contain native libraries** in the **Preferences** section of Eclipse.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-6.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-7.png)



## 4. Permission Configuration

SDK requires permissions including camera, Bluetooth headphone, sound recording, network access, SD card read/write access, incoming call monitoring and so on.

```
Manifest
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.BLUETOOTH"/>
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>
<uses-permission android:name="android.permission.BROADCAST_STICKY"/>
```

## 5. Developer Document

For more information, please see [Audio/Video Communication Development Guide](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)
