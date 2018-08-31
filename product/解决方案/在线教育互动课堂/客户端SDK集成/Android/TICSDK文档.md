## 准备工作
TICSDK 使用了互动视频服务（iLiveSDK）、云通讯服务（IMSDK）、COS 服务等腾讯云服务能力，在使用腾讯互动课堂服务时，请先阅读 [方案简介](/document/product/680/14776)，了解相关服务的基本概念和基本业务流程。
相关链接如下：

- [实时音视频](https://cloud.tencent.com/document/product/268/8424)
- [云通讯服务（IMSDK）](https://cloud.tencent.com/document/product/269/1504)
- [COS 服务](https://cloud.tencent.com/document/product/436/6225)

## 集成 SDK
TICSDK 目前仅支持 gradle 的集成方式。

1. 在整个工程的 build.gradle 文件中，使用 jcenter 配置 repositories，如下：

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
2. 在主工程的 buidle.gradle 文件中，添加 dependencies。

 ```
// COS SDK模块
compile 'com.tencent.qcloud:cosxml:5.4.4'
// iLiveSDK模块
compile 'com.tencent.ilivesdk:ilivesdk:1.9.1'
// 互动教育模块
compile 'com.tencent.ticsdk:ticsdk:1.2.1'
// 白板SDK模块
compile 'com.tencent.boardsdk:boardsdk:1.2.8'
```    

3. 在 defaultConfig 中配置 abiFilters 信息。
 
 ```
defaultConfig {
	...
	ndk {
		// 设置支持的so库架构，推荐用户使用ndk 15或者ndk 16
		abiFilters 'armeabi', 'armeabi-v7a'
	}
}
```	
 	
### 混淆配置
如果您的 APK 最终会经过代码混淆，请在 proguard 配置文件中加入以下代码：

```
-dontwarn com.tencent.**
-keep class com.tencent.**{*;}
```

## TICSDK 使用说明
工程配置完成之后，就可以进一步了解 TICSDK 的使用方法了，为了方便开发者的集成使用，我们开发了一个面向开发者的 Demo，开发者可以参照该 Demo 使用 TICSDK。
- [下载开发者 Demo](http://dldir1.qq.com/hudongzhibo/TICSDK/Android/TICSDK_Android_Demo.zip)

>**注意：**
> 开发者 Demo 的主要主要为向开发者展示 TICSDK 的基本使用方法，所以简化了很多不必要的 UI 代码，使开发者更加专注于了解 TICSDK 的使用方法。

### 主要类概览

先总体说明下 SDK 中主要类的功能：

| 类名 | 主要功能 |
|--------- | ---------|
| TICSDK | 整个 SDK 的入口类，提供了 **SDK 初始化** 和 **获取版本号** 的方法。|
| TICManager | 互动课堂管理类，互动课堂 SDK 对外主要接口类，提供了 **添加白板**、**登录/登出 SDK**、**创建/加入/销毁课堂**、**音视频操作**、**IM 操作** 等接口。|
| TICClassroomOption | 加入课堂时的课堂配置类，主要用来配置加入课堂时的角色（学生 or 老师）、是否自动开启摄像头，麦克风等，另外课堂配置对象还带有两个可选的监听接口，一个是负责监听课堂内部事件，另一个则负责监听课堂内的 IM 消息。|
| AVRootView | iLiveSDK 视频显示控件。 |
| WhiteboardView | 白板控件。|

###  控件使用

TICSDK 主要用到两个重要的 UI 控件，分别用于显示视频流信息和白板数据信息的。开发者可以直接使用或者集成，添加自己业务需要的特性。如 Demo：

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
开发者也可以定义自己 AVRootView，继承 AVRootView 即可。

>**注意：**
>为了更好的白板体验，WhiteboardView 控件宽高比固定为 16：9 的比例显示。请开发者注意与设计师同步该信息，以及不要随意修改该比例，以免影响白板功能的正常体验。

构建出实时音视频的 AVRootView 控件的实例后，需要设置 TICSDK 内部，如：

```java
AVRootView livingVideoView = (AVRootView) findViewById(R.id.av_root_view);
TICManager.getInstance().setAvRootView(livingVideoView);
```
更多关于 AVRootView 的使用，请参考实时音视频中的 [定制视频画面展示](https://cloud.tencent.com/document/product/647/17433)。

###  TICSDK 业务流程

TICSDK 使用的一般流程如下：

![业务流程](https://main.qcloudimg.com/raw/180672aff170289c95e02556eeed9ca8.png) 

其中“创建课堂”为教师角色特有流程，学生角色不需调用。

####  1. 初始化 SDK
要使用`TICSDK`，首先得进行初始化，初始化方法位于`TICSDK`单例类中：

```java
    > TICSDK.java(接口所在类，下同)
    /**
     * 教育SDK初始化
     *
     * @param context
     * @param appId       iLiveSDK appId
     * @param accountType iLiveSDK accountType
     */
    public void initSDK(Context context, int appId, int accountType);

```
初始化方法很简单，开发者在 Application 组件中的 onCreate 调用初始化接口即可。但是开发者在初始化之前必须保证已经在 [腾讯云后台](https://console.cloud.tencent.com/rav) 注册成功，并创建了应用，这样才能拿到腾讯云后台分配的 SDKAppID 和 accountType。

> 如果开发者 App 中用到了多进程，初始化时需要注意避免重复初始化，如下：
 
```
if (主进程) {    
	// 仅在主线程初始化
	TICSDK.getInstance().initSDK(this, Constants.APPID, Constants.ACCOUNTTYPE);
}
```
COS 为 [腾讯云对象存储](https://cloud.tencent.com/document/product/436/6225)，如果您的 App 中需要用到上传图片、文件到白板上展示的功能 (移动端只能上传图片)，则需要先在腾讯云对象存储开通了服务，然后再在 SDK 中将相关参数配置好，TICSDK 内部会将调用 SDK 接口上传的图片，文件上传到您配置的 COS 云存储桶中。
TICSDK 初始化 SDK 时也需要初始化 COS SDK 模块。主要构造 **CosConfig** 配置信息，通过 **WhiteboardManager** 的 **setCosConfig** 接口完成 COS 相关配置，如下：

```java
CosConfig cosConfig = new CosConfig()
	.setAppId(cosAppId) 	
	.setSecrectId(secrectId)
	.setBucket(bucket)
	.setRegion(region)
	.setSecrectKey(secrectKey)
	.setCosPath(cosPath);
WhiteboardManager.getInstance().setCosConfig(cosConfig);

```

#### 2. 登录/登出
初始化完成之后，因为涉及到 IM 消息的收发，所以还必须先登录：

```java
    > TICManager.java
    /**
     * IM登录
     *
     * @param identifier IM用户id
     * @param userSig    IM用户鉴权票据
     * @param callBack   回调
     */
    public void login(final String identifier, final String userSig, final ILiveCallBack callBack);
```
该方法需要传入 identifier 和 userSig 两个参数，identifier 为用户 ID；userSig 为腾讯云后台用来鉴权的用户签名，登录的流程如下：

![登录流程](https://main.qcloudimg.com/raw/a5be82ca74f2d33598549d0222d3ceba.png) 

该方法需要传入 uid 和 userSig 两个参数，uid 为用户 ID；userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并传给客户端用于登录，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

>**注意：**
> - 开发调试阶段， 开发者可以使用腾讯云实时音视频控制台的开发辅助工具来生成临时的 uid 和 userSig 用于开发测试。
>- 如果此用户在其他终端被踢，登录将会失败，返回错误码（ERR_IMSDK_KICKED_BY_OTHERS：6208）。为了保证用户体验，建议开发者进行登录错误码 ERR_IMSDK_KICKED_BY_OTHERS 的判断，在收到被踢错误码时，提示用户是否重新登录。
> - 如果用户保存用户票据，可能会存在过期的情况，如果用户票据过期，login 将会返回 70001 错误码，开发者可根据错误码进行票据更换。
> - 关于以上错误的详细描述，参见 [用户状态变更](https://cloud.tencent.com/document/product/269/9148#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)。


登出的操作如下：

```java
    > TICManager.java
    /**
     * 注销登录
     *
     * @param callBack 注销登录结果回调
     */
    public void logout(final ILiveCallBack callBack);
```

#### 3. 课堂管理

3.1 创建课堂

登录成功之后，就可以创建或者加入课堂了，创建课堂接口如下：

```java
    > TICManager.java
    /**
     * 根据参数创建课堂
     * @param roomId 房间ID，有业务生成和维护。
     * @param callback 回调，见@ILiveCallBack， onSuccess，创建成功；若出错，则通过onError返回。
     */
    public void createClassroom(final int roomId, final ILiveCallBack callback) {
```

3.2 加入课堂

```java
    > TICManager.java
    /**
     * 根据参数配置和课堂id加入互动课堂中
     *
     * @param option   加入课堂参数选项。见@{TICClassroomOption}
     * @param callback 回调
     */
    public void joinClassroom(@NonNull final TICClassroomOption option, final ILiveCallBack callback);
```

该接口需要传入TICClassroomOption 加入课堂的参数配置。如：

```java
    TICClassroomOption classroomOption = new TICClassroomOption()
        .setRoomId(roomId)
        .controlRole("user") 		// 默认的实时音视频角色的配置“user”，开发者需要根据自身的业务需求配置实时音视频的角色。
        .autoSpeaker(false)		// 此处为demo的配置，开发者需要根据自身的业务需求配置
        .setRole(TICClassroomOption.Role.TEACHER) // 课堂中的老师身份
        .setEnableCamera(true)   // 此处为demo的配置，开发者需要根据自身的业务需求配置
        .setEnableMic(true)      // 此处为demo的配置，开发者需要根据自身的业务需求配置
        .privateMapKey(privateMapKey) // 进房票据
        .setClassroomIMListener(this) // 设置课堂IM消息监听
        .setClassEventListener(this); // 设置课堂事件监听

    TICManager.getInstance().joinClassroom(classroomOption, new ILiveCallBack()
```

**TICClassroomOption** 加入课堂配置类继承 iLiveSDK 的。 **ILiveRoomOption**，在此基础上新增些开关和回调接口，如：加入课堂时的角色（老师或学生，一般创建课堂的人为老师，其他人应该以学生身份加入课堂），以及进入课堂时是否自动开启摄像头和麦克风（一般情况下， 老师端进入课堂默认打开摄像头和麦克风，学生端进入课堂默认关系）。
其中 **TICClassroomOption** 的 **privateMapKey(...)** 接口用于配置票据，为必填信息，进入课堂前先从自己的业务后台获取该信息，然后调用TICSDK的进入课堂接口，跳过该过程会导致进入课堂失败，详见 [privateMapKey](https://cloud.tencent.com/document/product/647/17230#privatemapkey)。

主要代码流程如下，详细代码可参见 Demo 源码：

```java
// 1.进入课堂界面单击，
public void onJoinClsssroomClick(View v){ ... }

// 2.请求获取 privatemapkey，一下代码为工程代码示例代码，无实际功能，具体开发者需要根据自身业务需要和实现构建参数；
PrivateMapKeyParams params = new PrivateMapKeyParams();
params.setIdentifier(identifier);
params.setPwd("xxxx");
params.setRoomNum(roomId);
privateMapKeyPresenter.getPrivateMapKey(params);

// 3.监听请回结果回调，获取成功后则可执行进入课堂操作，如Demo中源码
public void onGetAuthbufferSuccess(String privateMapKey) {
    Log.i(TAG, "onGetAuthbufferSuccess: privateMapKey");
    ...
    //获取成功后则将privatemapkey通过进房参数设置：
    TICClassroomOption classroomOption = new TICClassroomOption()
       ...
       .privateMapKey(privateMapKey)
      ...
   //执行进入课堂操作
}

```

开发者也可通过该参数直接控制 iLiveSDK 的进房参数设置。
加入课堂成功，在成功的回调处，需要初始化一下白板 SDK 的相关配置，如：

```java
// 配置白板参数
WhiteboardManager.getInstance().getConfig()
	.setTimePeriod(300)
	.setPaintSize(6)
	.setPaintColor(Color.BLUE)
	.setIdentifier(ILiveLoginManager.getInstance().getMyUserId());
```

3.3 退出课堂

```java
    > TICManager.java
    /**
     * 退出课堂，退出iLiveSDK的AV房间，学生角色退出群聊和白板通道群组；老师角色则解散这两个群组
     *
     * @param callback 回调
     */
    public void quitClassroom(final ILiveCallBack callback) {
```

学生退出课堂时，只是本人退出了课堂，老师调用`退出课堂`方法退出课堂时，该课堂将会被销毁。开发者应尽量保证再加入另一个课堂前，已经退出了前一个课堂。

####  4. 白板相关操作

白板的相关操作用户直接通过白板 SDK 操作即可，TICSDK 不做任何封装。详见 [Android 白板 SDK 使用手册](/document/product/680/17889)。

####  5. IM 相关操作

IM 相关的接口封装于腾讯云通信 SDK`IMSDK`，同样，TICSDK 中也只封装了一些常用接口：

```java
    > TICManager.java
    /**
     * 发送C2C文本消息
     *
     * @param identifier 消息接收者
     * @param text       发送内容
     * @param callBack   回调
     */
    public void sendC2CTextMessage(final String identifier, final String text, final ILiveCallBack callBack);

    /**
     * 发送C2C自定义消息
     *
     * @param identifier 消息接收者
     * @param data       发送的自定义的内容
     * @param callBack   回调
     */
    public void sendC2CCustomMessage(final String identifier, final byte[] data, final ILiveCallBack callBack);

    /**
     * 发送群文本消息
     *
     * @param text     发送的群组消息内容
     * @param callBack 回调
     */
    public void sendGroupTextMessage(final String text, final ILiveCallBack callBack);

    /**
     * 发送群组自定义消息
     *
     * @param data     发送的自定义的群组消息内容
     * @param callBack 回调
     */
    public void sendGroupCustomMessage(@NonNull final byte[] data, final ILiveCallBack callBack);
    
    /**
     * 发送私聊消息
     *
     * @param dstUser  消息接收者
     * @param message  消息内容
     * @param callBack 回调
     */
    public void sendC2CMessage(String dstUser, TIMMessage message, ILiveCallBack<TIMMessage> callBack);

    /**
     * 发送群聊消息
     *
     * @param message  消息内容
     * @param callBack 回调
     */
    public void sendGroupMessage(TIMMessage message, ILiveCallBack<TIMMessage> callBack);
```
课堂内成员在调用以上方法发送消息时，会触发 IM 事件，如果在加入课堂前设置了 IM 事件监听 `IClassroomIMListener classroomIMListener;`，一端发送 IM 消息时，另一端就可以在课堂内 IM 消息回调对应方法中得到通知：

```java
    > IClassroomIMListener.java
    /**
     * 收到C2C文本消息
     */
    void onRecvC2CTextMsg(String fromId, String text);

    /**
     * 收到C2C自定义消息
     */
    void onRecvC2CCustomMsg(String fromId, byte[] data);

    /**
     * 收到Group文本消息
     */
    void onRecvGroupTextMsg(String fromId, String text);

    /**
     * 收到Group自定义消息
     */
    void onRecvGroupCustomMsg(String fromId, byte[] data);
    /**
     * 所有消息回调，所有 IM 消息都可通过监听该接口获得；如果只需要处理简单的文字消息和自定义消息，只需要处理以上 4 个回调即可；
     * 如果需要收取和处理 IM 所有类型消息，如表情、图片等，则可以只监听这个回调（其它四个回调不做处理），自己完成消息的遍历和解析即可。
     * @param message
     */
    void onRecvMessage(TIMMessage message);
```

> **注意：**
> 所有消息回调，所有 IM 消息都可通过监听该接口获得；如果只需要处理简单的文字消息和自定义消息，只需要处理前 4 个回调即可；如果需要收取和处理IM所有类型消息，如表情、图片等，则可以只监听 **onRecvMessage** 这个回调（其它 4 个回调可以不做处理，因为回到到这 4 个接口的内容，也通过 **onRecvMessage** 回调了），自己完成消息的遍历和解析即可。

####  6. 音视频相关操作

这部分功能封装于腾讯云实时音视频 SDK `iLiveSDK`，TICSDK 中只封装了一些常用的接口：打开/关闭摄像头、切换摄像头、打开/关闭麦克风、打开/关闭扬声器等，具体如下：

```java
    > TICManager.java
    /**
     * 打开/关闭摄像头
     *
     * @param cameraId 要打开或者关闭的摄像头设备标识，见@ILiveConstants.FRONT_CAMERA或ILiveConstants.BACK_CAMERA;
     * @param enable   true：打开摄像头，默认开启前置摄像头；false：关闭
     * @param callback 回调
     */
    public void enableCamera(int cameraId, final boolean enable, final ILiveCallBack callback);

	/**
     * 前后摄像头切换
     *
     * @param callback 回调
     */
    public void switchCamera(@Nullable final ILiveCallBack callback);
    
    /**
     * 打开/关闭麦克风
     *
     * @param enable   enable true：打开；false：关闭
     * @param callback 回调
     */
    public void enableMic(final boolean enable, final ILiveCallBack callback);
    
    /**
     * 打开/关闭扬声器
     *
     * @param enable   enable true：打开；false：关闭
     * @param callback
     */
    public void enableSpeaker(final boolean enable, final ILiveCallBack callback);
```

课堂内成员在进行打开/关闭摄像头、麦克风操作时，会触发音视频事件，iLiveSDK 自动渲染到控件上。同时对 AVRootView 设置 setSubCreatedListener 事件监听，则会收到 onSubViewCreated 的回调。此时，开发者可以遍历 AVRootView 中的 AVVideoView，对各视频流做展示处理。

####  7. 课堂内其他事件监听

进入课堂的配置对象中的课堂事件监听接口的协议方法：

```java
    > IClassEventListener.java
    /**
     * 视频流异常退出
     * @param errCode
     * @param errMsg
     */
    void onLiveVideoDisconnect(int errCode, String errMsg);

    /**
     * 课堂解散通知
     */
    void onClassroomDestroy();
    
    /**
     * 有人加入课堂时的通知回调（需配置工单）
     * @param userList 加入课堂的成员userId列表
     */
    void onMemberJoin(List<String> userList);

    /**
     * 有人退出课堂时（主动退出或者被踢出）时的通知回调（需配置工单）
      * @param userList  退出课堂的成员userId列表
     */
    void onMemberQuit(List<String> userList);
```

以上协议方法分别代表有人加入课堂，有人退出课堂和课堂被解散的回调，开发者可以根据自己的业务需求，对回调事件进行相应的处理，比如：在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可以弹出一个提示框，提示学生课堂已经结束。


## 常见问题
#### AvRootView 与 WhiteboardView 叠加时白板无法显示？

AvRootView 和 WhiteboardView 都是集成 SurfaceView 的，SurfaceView 叠加显示时会有异常。
通过 SurfaceView 的 `setZOrderMediaOverlay(true);`即可解决。



