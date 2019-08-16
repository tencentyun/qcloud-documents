

## 操作场景
FCM 通道是谷歌推出的系统级推送通道，在国外具备谷歌 Service 框架的手机上，能够实现无需打开应用，即可收到推送消息。

## 操作步骤
### 获取密钥
进入 FireBase 官网， 注册应用信息。并将获取到的 FCM 应用推送服务器密钥和 SenderID，配置到腾讯移动推送的管理台。

### 配置内容
1. 配置 google-services.json 文件。如图所示：
![](https://main.qcloudimg.com/raw/568561b72a775058bf06750bfab38ed0.png)
2. 配置 gradle，集成谷歌 service。
  1. 在项目级的 build.gradle 文件中的 dependencies 节点中添加下面代码：
```xml
classpath 'com.google.gms:google-services:4.2.0'
```
>!如果使用低于4.2.0版本出现 `FCM Register error! java.lang.IllegalStateException: Default FirebaseApp is not initialized in this process com.qq.xg4all. Make sure to call FirebaseApp.initializeApp(Context) first.`，建议在 res/values 文件夹下的 string.xml， 加上 YOUR_GOOGLE_APP_ID。

  2. 在应用级的 build.gradle 文件中，添加依赖：
	```xml
	implementation  'com.google.firebase:firebase-messaging:17.6.0' // fcm 推送
	implementation  'com.google.firebase:firebase-messaging:17.6.0'

	 //在应用级的gradle文件的最后一行代码中新增并将google-services.json放进您应用model的根路径下
	apply plugin: 'com.google.gms.google-services'
	```
>!Google 配置 google-play-services（建议版本 17.0.0+，较低版本有可能出现无法注册 FCM 风险）。

### 启用 FCM 推送
在调用腾讯移动推送注册代码 XGPushManager.registerPush 前，添加以下代码设置：

```java
XGPushConfig.enableOtherPush(this, true);
```
注册 FCM 成功的日志如下：

```xml
 E/XG_fcm: Fcm App has initialize 
 D/XG_fcm: FirebaseAPP初始化完成
 I/XG_fcm: registerPush Token is: eK0LLz43Z_U:APA91bHjyTCuX7fZ6Ye-fAojAo_l2nphA3rRtLZN98grADOZtULysxYd51pCaL5oiqyVs0Mtbfu2mBdjoeGsSq5sjbh5mCETgl2dURRy9-yNR_ZZrn6pWcvwt7CoWTY0_Q9_mreiryuI
12-02 09:16:31.877 17260-17260/lc.com.xinge.push W/FA: Service connection failed: ConnectionResult{statusCode=SERVICE_VERSION_UPDATE_REQUIRED, resolution=null, message=null}
12-02 09:16:31.892 17260-17278/lc.com.xinge.push V/FA: Using measurement service
12-02 09:16:31.893 17260-17278/lc.com.xinge.push V/FA: Connecting to remote service
12-02 09:16:31.895 17260-17423/lc.com.xinge.push I/XINGE: [XGOtherPush] Reservert info: other push token is : eK0LLz43Z_U:APA91bHjyTCuX7fZ6Ye-fAojAo_l2nphA3rRtLZN98grADOZtULysxYd51pCaL5oiqyVs0Mtbfu2mBdjoeGsSq5sjbh5mCETgl2dURRy9-yNR_ZZrn6pWcvwt7CoWTY0_Q9_mreiryuI  other push type: fcm
```

