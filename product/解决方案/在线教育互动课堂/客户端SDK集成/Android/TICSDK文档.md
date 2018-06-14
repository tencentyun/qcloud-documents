## 准备工作
TICSDK使用了互动视频服务（iLiveSDK）、云通讯服务（IMSDK）、COS服务等腾讯云服务能力，在使用腾讯互动课堂服务时，请先阅读 [方案简介](/document/product/680/14776)，了解相关服务的基本概念和基本业务流程。相关链接如下：

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
compile 'com.tencent.ilivesdk:ilivesdk:1.8.6.1.5'
// 互动教育模块
compile 'com.tencent.ticsdk:ticsdk:1.0.0'
// 白板SDK模块
compile 'com.tencent.boardsdk:boardsdk:1.2.5'
```    

3. 在 defaultConfig 中配置 abiFilters 信息。
 
 ```
defaultConfig {
	...
	ndk {
		// 设置支持的so库架构
		abiFilters 'armeabi', 'armeabi-v7a'
	}
}
```	
 	
### 混淆配置
如果您的 APK 最终会经过代码混淆，请在 proguard 配置文件中加入以下代码：

```
- dontwarn com.tencent.**
- keep class com.tencent.** {*;}
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
| TICManager | 互动课堂管理类，互动课堂 SDK 对外主要接口类，提供了 **添加白板**、**登录/登出 SDK**、**创建/加入/销毁课堂**、**音视频操作**、**IM操作** 等接口。|
| TICClassroomOption | 加入课堂时的课堂配置类，主要用来配置加入课堂时的角色（学生 or 老师）、是否自动开启摄像头，麦克风等，另外课堂配置对象还带有两个可选的代理对象，一个是复制监听课堂内部事件，另一个则负责监听课堂内的 IM 消息。|
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
初始化方法很简单，开发者在Application组件中的onCreate调用初始化接口即可。但是开发者在初始化之前必须保证已经在[腾讯云后台](https://console.cloud.tencent.com/rav)注册成功，并创建了应用，这样才能拿到腾讯云后台分配的SDKAppID和accountType。

> 如果开发者 App 中用到了多进程，初始化时需要注意避免重复初始化，如下：

```
if (主进程) {    
	// 仅在主线程初始化
	TICSDK.getInstance().initSDK(this, Constants.APPID, Constants.ACCOUNTTYPE);
}
```
COS 为[腾讯云对象存储](https://cloud.tencent.com/document/product/436/6225)，如果您的 App 中需要用到上传图片、文件到白板上展示的功能 (移动端只能上传图片)，则需要先在腾讯云对象存储开通了服务，然后再在 SDK 中将相关参数配置好，TICSDK 内部会将调用 SDK 接口上传的图片，文件上传到您配置的 COS 云存储桶中。
TICSDK 初始化 SDK 时也需要初始化 COS SDK 模。主要构造 **CosConfig** 配置信息，通过**TICManager#setCosConfig**接口完成 COS 相关配置，如下：

```java
CosConfig cosConfig = new CosConfig()
	.setAppId(cosAppId) 	
	.setSecrectId(secrectId)
	.setBucket(bucket)
	.setRegion(region)
	.setSecrectKey(secrectKey)
	.setCosPath(cosPath);
TICManager.getInstance().setCosConfig(cosConfig);

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

该方法需要传入 uid 和 userSig 两个参数，uid 为用户 ID；userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成userSig的规则来生成，并传给客户端用于登录，详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。

>**注意：**
> - 开发调试阶段， 开发者可以使用腾讯云实时音视频控制台的开发辅助工具来生成临时的uid和userSig用于开发测试.
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

该接口需要传入TICClassroomOption加入课堂的参数配置。如：

```java
    TICClassroomOption classroomOption = new TICClassroomOption()
        .setRoomId(roomId)
        .controlRole("user") 		// 默认的实时音视频角色的配置“user”，开发者需要根据自身的业务需求配置实时音视频的角色。
        .autoSpeaker(false)		// 此处为demo的配置，开发者需要根据自身的业务需求配置
        .setRole(TICClassroomOption.Role.TEACHER) // 课堂中的老师身份
        .setEnableCamera(true)   // 此处为demo的配置，开发者需要根据自身的业务需求配置
        .setEnableMic(true)      // 此处为demo的配置，开发者需要根据自身的业务需求配置
        .setClassroomIMListener(this) // 设置课堂IM消息监听
        .setClassEventListener(this); // 设置课堂事件监听

    TICManager.getInstance().joinClassroom(classroomOption, new ILiveCallBack()
```

其中，**TICClassroomOption**功能具体如下：

```java
    > TICClassroomOption.java
    /**
     * 课堂角色
     */
    public enum Role {
        /**
         * 老师
         */
        TEACHER(0),
        /**
         * 学生
         */
        STUDENT(1);
        private int value;

        Role(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }

    /**
     * 房间ID，由业务维护
     */
    private int roomId;
    /**
     * 开启摄像头
     */
    private boolean enableCamera = false;

    /**
     * 开启Mic
     */
    private boolean enableMic = false;

    /**
     * 默认开启白板
     */
    private boolean enableWhiteboard = true;

    /**
     * 课堂角色，默认是学生角色，见@Role
     */
    private Role role = Role.STUDENT;

    /**
     * 课堂白板绘制事件回调
     */
    //private IClassroomWhiteboardListener classroomWhiteboardListener;

    /**
     * 课堂文字互动消息事件回调
     */
    private IClassroomIMListener classroomIMListener;

    /**
     * 课堂音视频异常断开/IM群组解散
     */
    private IClassEventListener classEventListener;
```

**TICClassroomOption** 加入课堂配置类集成 iLiveSDK的**ILiveRoomOption**，在此基础上新增些开关和回调接口，如：加入课堂时的角色（老师或学生，一般创建课堂的人为老师，其他人应该以学生身份加入课堂），以及进入课堂时是否自动开启摄像头和麦克风（一般情况下， 老师端进入课堂默认打开摄像头和麦克风，学生端进入课堂默认关系）。
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
    public void sendC2CTextMessage(final String identifier, final String text, final ILiveCallBack callBack) {
        ILiveTextMessage message = new ILiveTextMessage(text);
        ILiveRoomManager.getInstance().sendC2CMessage(identifier, message, callBack);
    }

    /**
     * 发送C2C自定义消息
     *
     * @param identifier 消息接收者
     * @param data       发送的自定义的内容
     * @param callBack   回调
     */
    public void sendC2CCustomMessage(final String identifier, final byte[] data, final ILiveCallBack callBack) {
        ILiveCustomMessage message = new ILiveCustomMessage(data, "");
        ILiveRoomManager.getInstance().sendC2CMessage(identifier, message, callBack);
    }

    /**
     * 发送群文本消息
     *
     * @param text     发送的群组消息内容
     * @param callBack 回调
     */
    public void sendGroupTextMessage(final String text, final ILiveCallBack callBack) {
        ILiveTextMessage message = new ILiveTextMessage(text);
        ILiveRoomManager.getInstance().sendGroupMessage(message, callBack);
    }

    /**
     * 发送群组自定义消息
     *
     * @param data     发送的自定义的群组消息内容
     * @param callBack 回调
     */
    public void sendGroupCustomMessage(@NonNull final byte[] data, final ILiveCallBack callBack) {
        ILiveCustomMessage message = new ILiveCustomMessage(data, "");
        ILiveRoomManager.getInstance().sendGroupMessage(message, callBack);
    }
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
```

这 4 个接口方法，分别对应了前面 4 个消息发送的方法，对应类型的消息会在对应类型的代理方法中回调给课堂内所有成员（发消息本人除外），其他端收到后可以将消息展示在界面上。

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
```

以上协议方法分别代表有人加入课堂，有人退出课堂和课堂被解散的回调，开发者可以根据自己的业务需求，对回调事件进行相应的处理，比如：在收到课堂解散回调时（老师退出课堂即触发该回调），课堂内的学生端可以弹出一个提示框，提示学生课堂已经结束。


## 常见问题
### AvRootView 与 WhiteboardView 叠加时白板无法显示。

AvRootView 和 WhiteboardView 都是集成 SurfaceView 的，SurfaceView 叠加显示时会有异常。
通过 SurfaceView 的 `setZOrderMediaOverlay(true);`即可解决。



