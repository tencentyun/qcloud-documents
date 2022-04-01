## 操作场景
FCM 通道是谷歌推出的系统级推送通道，在国外具备谷歌 Service 框架的手机上，鉴于其较宽松的后台进程管理方式，在应用进程未被强制停止的情况下，可以收到推送消息。

## 操作步骤
### 获取密钥
FCM 推送支持两种密钥配置，以下方式二选一，推荐使用“服务器私钥”的新协议方式。
1. 服务器私钥 （推荐）
进入 [FireBase 官网](https://firebase.google.com/?hl=zh-cn)，注册应用信息。在 **Firebase 项目** > **选择具体的项目应用** > **设置** > **服务账号** > **Firebase Admin SDK**，单击**生成新的私钥**，获取到 Firebase 服务器私钥 json 文件。然后进入 [**移动推送 TPNS 控制台**](https://console.cloud.tencent.com/tpns) > **配置管理** > **基础配置** > **FCM 官方推送通道** 栏目中，选中“（推荐）服务器私钥”，单击**点击上传**，上传获取到的 json 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/3a129ce4ab18e3d31c3ba2389e9b03cf.png)
2. 旧版服务器密钥
进入 [FireBase 官网](https://firebase.google.com/?hl=zh-cn)，注册应用信息。在**Firebase 项目** > **选择具体的项目应用** > **设置** > **云消息传递** 获取到的 FCM 应用推送 **服务器密钥**，并配置到 [**移动推送 TPNS 控制台**](https://console.cloud.tencent.com/tpns) > **配置管理** > **基础配置** > **FCM 官方推送通道** 栏目中。
![](https://main.qcloudimg.com/raw/d82c9dd04fe986ffc35a57e30eefce4f.png)
### 配置内容
1. 配置 google-services.json 文件。如图所示：
![](https://main.qcloudimg.com/raw/568561b72a775058bf06750bfab38ed0.png)
2. 配置 gradle，集成谷歌 service。
  1. 在项目级的 build.gradle 文件中的 dependencies 节点中添加下面代码：
```xml
classpath 'com.google.gms:google-services:4.2.0'
```
>! 如果使用低于4.2.0版本出现 `FCM Register error! java.lang.IllegalStateException: Default FirebaseApp is not initialized in this process com.qq.xg4all. Make sure to call FirebaseApp.initializeApp(Context) first.`，建议在 res/values 文件夹下的 string.xml， 加上 YOUR_GOOGLE_APP_ID。
>
  2. 在应用级的 build.gradle 文件中，添加依赖：
	```xml
	  implementation 'com.tencent.tpns:fcm:[VERSION]-release' // FCM 推送 [VERSION] 为当前 SDK 版本号，版本号可在 Android SDK 发布动态查看
      implementation  'com.google.firebase:firebase-messaging:17.6.0'

	 //在应用级的 gradle 文件的最后一行代码中新增并将 google-services.json 放进您应用 model 的根路径下
	apply plugin: 'com.google.gms.google-services'
	```
>!
>- FCM 推送 [VERSION] 为当前 SDK 版本号，版本号可在 [Android SDK 发布动态](https://cloud.tencent.com/document/product/548/44520) 查看。
>- Google 配置 google-play-services（建议版本 17.0.0+，较低版本有可能出现无法注册 FCM 风险）。


### 启用 FCM 推送
在调用移动推送 TPNS 注册代码 XGPushManager.registerPush 前，添加以下代码设置：

```java
XGPushConfig.enableOtherPush(this, true);
```
注册 FCM 成功的日志如下：

```xml
V/TPush: [XGPushConfig] isUsedOtherPush:true
I/TPush: [OtherPush] checkDevice pushClassNamecom.tencent.android.tpush.otherpush.fcm.impl.OtherPushImpl
I/TPush: [XGPushManager] other push token is : dSJA5n4fSZ27YeDf2rFg1A:APA91bGiqSPCMZTuyup**********f1fBIahZKYkth2OoDpixDPQmEZkQ11fX06mw_1kEaW5-jFmT4YwlER4qfX66h_BIoUxOyj_tKqZSUg7oHigIKaOrDWmMQfMAqGoT8qSfg  other push type: fcm
```
