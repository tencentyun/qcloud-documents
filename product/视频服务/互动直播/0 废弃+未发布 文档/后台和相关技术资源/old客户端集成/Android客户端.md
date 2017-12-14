## 1 下载SDK

解开压缩包，可以看到双人通话、多人通话两份Demo。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-1.png)

多人通话Demo是由Eclipse创建的工程。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-2.png)

bin目录存放apk包，可以直接安装体验demo

doc目录存放运行时流程图和API文档。

libs目录存放集成SDK所需的jar和so。

## 2 创建工程

目前SDK最低支持Android 2.2。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-3.png)

## 3 SDK集成

SDK库以jar和动态链接库(so)的形式提供。请将so放置于工程名/libs/armeabi目录下，同时将eup_1.9.2__allproguad_rqdp.jar、imsdk.jar、qavsdk.jar放置于/libs目下，刷新Eclipse会自动加入工程引用。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-4.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-5.png)

>注意：在Eclipse的Perferences中取消选中Force error when external jars contain native libraries。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-6.png)

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinAndroidkehuduanjicheng-7.png)



## 4 权限配置

SDK需要摄像头、蓝牙耳机、录音、访问网络、读写SD卡、监听来电等权限。

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

## 5 开发者文档

详情参考[音视频通信开发指南](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)