  
## 1. 快速集成

为了方便开发者的集成使用，我们开发了一个面向开发者的 Demo，开发者可以参照该 Demo 使用 TICSDK。
[单击下载工程 Demo >>](http://dldir1.qq.com/hudongzhibo/TICSDK/Android/TICSDK_Android_Demo.zip)

### 1.1 gradle 集成
TICSDK 目前仅支持 gradle 的集成方式。

 - 在整个工程的 build.gradle 文件中，使用 jcenter 配置 repositories，如下：

 ```
allprojects {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:2.3.0'
    }
}
```

- 在主工程的 buidle.gradle 文件中，添加 dependencies。

 ```
// COS SDK模块
compile 'com.tencent.qcloud:cosxml:5.4.4'
// iLiveSDK模块
compile 'com.tencent.ilivesdk:ilivesdk:1.9.1'
// 互动教育模块
compile 'com.tencent.ticsdk:ticsdk:1.5.0'
// 白板SDK模块
compile 'com.tencent.boardsdk:boardsdk:1.5.1'
```    

- 在 defaultConfig 中配置 abiFilters 信息。
 
 ```
defaultConfig {
	...
	ndk {
		// 设置支持的so库架构，推荐用户使用ndk 15或者ndk 16
		abiFilters 'armeabi', 'armeabi-v7a'
	}
}
```	
 	
- 混淆配置
如果您的 APK 最终会经过代码混淆，请在 proguard 配置文件中加入以下代码：

 ```
-dontwarn com.tencent.**
-keep class com.tencent.**{*;}
```

## 2. 使用详解

### 2.1. TICSDK 使用流程介绍
TICSDK 使用的一般流程如下：

![](https://main.qcloudimg.com/raw/30b9189f6c8fe279750cef683e44b56f.png)

### 2.2. 控件使用

TICSDK 主要用到两个重要的 UI 控件，分别用于显示视频流信息和白板数据信息的。开发者可以直接Layout的XML文件里直接引用，或者继承添加自己业务需要的特性。如：

```xml
<com.tencent.ilivesdk.view.AVRootView
	android:id="@+id/av_root_view"
	android:layout_width="match_parent"
	android:layout_height="wrap_content" />

<com.tencent.boardsdk.board.WhiteboardView
	android:id="@+id/whiteboardview"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:layout_alignParentTop="true"
	android:visibility="invisible" />
```
开发者也可以定义自己 **AVRootView**，继承即可。

>**注意：**
>为了更好的白板体验，WhiteboardView 控件宽高比固定为 16：9 的比例显示。请开发者注意与设计师同步该信息，以及不要随意修改该比例，以免影响白板功能的正常体验。

构建出实时音视频的 AVRootView 控件的实例后，需要设置 TICSDK 至内部，如：

```java
AVRootView livingVideoView = (AVRootView) findViewById(R.id.av_root_view);
TICManager.getInstance().setAvRootView(livingVideoView);
```


### 2.3. 初始化 SDK

> 在初始化前，需确认已[开通实时音视频服务](https://cloud.tencent.com/document/product/647/17195)，并拿到 SDKAppID。

接口 | 说明
---|---
initSDK | 初始化SDK

**如果开发者 App 中用到了多进程，初始化时需要注意避免重复初始化**，如下：
  
```
if (主进程) {    
	// 仅在主线程初始化
	TICSDK.getInstance().initSDK(.., SDKAppID);
}

```


### 2.4. 登录
初始化完成之后，接着是登录：

接口 | 说明 | 主要参数
------- | ------- | -------
login | 登录 | userId 和 userSig

该方法需要传入 **userId** 和 **userSig** 两个参数。开发调试阶段，开发者可以使用腾讯云 [实时音视频控制台](https://console.cloud.tencent.com/rav)->【开发辅助】->【签名(UserSig)生成工具】生成临时的uid和userSig用于开发测试（在控制台->【功能配置】下载公私钥）

> **注意：**
> userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并传给客户端用于登录，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

登录成功之后，您就可以创建或者加入课堂了。

### 2.5. 创建课堂

创建课堂接口如下：

接口 | 说明 | 主要参数
------- | ------- | -------
createClassroom | 创建课堂 | roomID

其中参数**roomID**由业务层自行指定（必须为正整数）。

### 2.6. 加入课堂

接口 | 说明 | 主要参数
------- | ------- | -------
joinClassroom | 根据参数配置和roomID加入互动课堂中 | TICClassroomOption

该接口需要传入TICClassroomOption 加入课堂的参数配置。如：

```java
    TICClassroomOption classroomOption = new TICClassroomOption()
        .setRoomId(roomId)			// 为createClassroom中的roomId
        .controlRole("user") 		// 默认的实时音视频角色的配置“user”，开发者需要根据自身的业务需求配置实时音视频的角色。
        .privateMapKey(privateMapKey) // 进房票据
        .autoSpeaker(false)		// 此处为demo的配置，开发者需要根据自身的业务需求配置
        .autoCamera(true)   // 开发者需要根据自身的业务需求配置
        .autoMic(true)      // 开发者需要根据自身的业务需求配置
        .setClassroomIMListener(this) // 设置课堂IM消息监听
        .setClassEventListener(this); // 设置课堂事件监听

    TICManager.getInstance().joinClassroom(classroomOption, new ILiveCallBack(){...});
```

为了保证课堂内的正常逻辑和事件都能被监听到，进房时`TICClassroomOption`的这些属性都是必填参数，另外还有两个父类的参数必须填写：**controlRole** 和 **privateMapKey**。

* **controlRole**：该参数代表进房之后使用哪些音视频参数，参数具体值为客户在 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/rav) -> **画面设定** 中配置的角色名。
* **privateMapKey**：该参数相当于一个进入房间的钥匙，进房时必须填写，**privateMapKey** 需要在开发者的业务后台生成传给客户端，生成方法见 [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)。

加入课堂成功，在成功的回调处，需要更新和设置一下白板 SDK 的相关配置，如：

```java
// 配置白板参数
WhiteboardManager.getInstance().getConfig()
	.setTimePeriod(200)
	.setPaintSize(6)
	.setPaintColor(Color.BLUE)
	.setIdentifier(ILiveLoginManager.getInstance().getMyUserId());
```

### 2.7. 使用音视频

接口 | 说明
------- | ------- 
enableCamera | 打开/关闭摄像头
switchCamera | 前后摄像头切换
enableMic | 打开/关闭麦克风
enableSpeaker | 打开/关闭扬声器

### 2.8. 使用互动白板
> **说明：**使用白板前，需确认已 [开通白板服务](/document/product/680/14782)。

白板的相关操作用户直接通过白板 SDK 操作即可，TICSDK 不做任何封装。详见 [Android 白板 SDK 使用手册](/document/product/680/17889)。

### 2.9. 收发消息

使用 TICSDK 以下接口可以完成课堂中私聊和群聊消息的发送：

接口 | 说明 | 主要参数
------- | ------- | -------
sendTextMessage | 发送文本互动消息 | userId
sendCustomMessage | 发送自定义互动消息 | userId
sendMessage | 发送互动消息 |  userId

>**注意：**
>  userId 不为空时，为 C2C 消息接收者，为空时为群组消息。

课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听 `IClassroomIMListener classroomIMListener;`，一端发送 IM 消息时，另一端就可以在课堂内 IM 消息回调对应方法中得到通知：

接口 | 说明 | 主要参数
------- | ------- | -------
onRecvTextMsg | 发送文本互动消息 | type和userId
onRecvCustomMsg | 发送自定义互动消息 | type和userId
onRecvMessage | 发送互动消息 |  type和userId

> **注意：**
> **type** 为Constants.MSG_TYPE_C2C 时，为 C2C 消息接收者，为 Constants.MSG_TYPE_GROUP 为群组消息；
> **userId** 不为空时，为 C2C 消息接收者，为空时为群组消息。


### 2.10. 课堂事件监听

进入课堂的配置对象中的课堂事件监听接口的接口方法：

接口 | 说明
------- | ------- 
onLiveVideoDisconnect |  视频流异常断开。
onClassroomDestroy | 课堂解散通知。
onMemberJoin | 有人加入课堂时的通知回调。
onMemberQuit | 有人退出课堂时（主动退出或者被踢出）时的通知回调。
onRecordTimestampRequest | 录制时间同步。为了保证录制服务质量，保持多路录制内容一致性和同步性，用户需要实现该接口，并且保证各端的时间参考一致（如统一获取服务器时间），简单实现可以返回本地毫秒时间戳，如：System.currentTimeMillis()。


以上事件监听接口，开发者可以根据自己的业务需求，对回调事件进行相应的处理，比如：在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可以弹出一个提示框，提示学生课堂已经结束。

### 2.11. 结束课堂

退出课堂接口如下：

接口 | 说明 
------- | -------
quitClassroom | 退出课堂

### 2.12. 销毁课堂

退出课堂后，课堂的创建者还需要负责销毁自己创建的课堂，接口如下：

接口 | 说明 | 主要参数
------- | ------- | ------
destroyClassroom | 销毁课堂，回收课堂资源，由课堂创建者负责调用。| roomId

>** 注意：**这里的 **roomId** 对应创建课堂中的 **roomId**。

### 2.13. 登出

登出的操作如下：

接口 | 说明 
------- | -------
logout | 注销登录。


## 3. 常见问题
### 3.1. AvRootView 与 WhiteboardView 叠加时白板无法显示？

AvRootView 和 WhiteboardView 都是集成 SurfaceView 的，SurfaceView 叠加显示时会有异常。
通过 SurfaceView 的 `setZOrderMediaOverlay(true);`即可解决。

### 3.2. 如何定制视频画面展示？
关于 AVRootView 的高阶使用，请参考实时音视频中的 [定制视频画面展示](https://cloud.tencent.com/document/product/647/17433)。



