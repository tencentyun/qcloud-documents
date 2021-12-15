## 适用场景
TRTC 支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（VoiceCall）统称为 [通话模式](https://cloud.tencent.com/document/product/647/32169)，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为直播模式。
直播模式下的 TRTC，支持单个房间最多10万人同时在线，具备小于300ms的连麦延迟和小于1000ms的观看延迟，以及平滑上下麦切换技术。适用低延时互动直播、十万人互动课堂、视频相亲、在线教育、远程培训、超大型会议等应用场景。

## 原理解析
TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：
- **接口机**
该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话。
- **代理机**
该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求。

在直播模式下，TRTC 引入了角色的概念，用户被分成“主播”和“观众”两种角色，“主播”会被分配到接口机上，“观众”则被分配在代理机，同一个房间的观众人数上限为10万人。
如果“观众”要上麦，需要先切换角色（switchRole）为“主播”才能发言。切换角色的过程也伴随着用户从代理机到接口机的迁移，TRTC 特有的低延时观看技术和平滑上下麦切换技术，可以让整个切换时间变得非常短暂。
![](https://main.qcloudimg.com/raw/b88a624c0bd67d5d58db331b3d64c51c.gif)

## 示例代码
您可以登录 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTC-API-Example) 获取本文档相关的示例代码。
![](https://main.qcloudimg.com/raw/959efe00790a0a2952f8837a48baec25.png)

>?如果访问 Github 较慢，您也可以直接下载 [TXLiteAVSDK_TRTC_Android_latest.zip](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_latest.zip)。

## 操作步骤
[](id:step1)
### 步骤1：集成 SDK
您可以选择以下方式将 **TRTC SDK** 集成到项目中。
#### 方式一：自动加载（aar）
TRTC SDK 已发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。
您只需用 Android Studio 打开待集成 SDK 的工程（TRTC-API-Example 已完成集成，示例代码可以供您参考），然后通过简单的步骤修改`app/build.gradle`文件，即可完成 SDK 集成：

1. 在 dependencies 中添加 TRTCSDK 的依赖。
```
dependencies {
      compile 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
}
```
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
>?目前 TRTC SDK 支持 armeabi ， armeabi-v7a 和 arm64-v8a。
>
```
 defaultConfig {
      ndk {
          abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
      }
  }
```
3. 单击 **Sync Now** 同步 SDK。
 如果您的网络连接 jcenter 没有问题，SDK 会自动下载集成到工程中。

#### 方式二：下载 ZIP 包手动集成
您可以直接下载 [ZIP 压缩包](https://cloud.tencent.com/document/product/647/32689)，并参见 [快速集成(Android)](https://cloud.tencent.com/document/product/647/32175#.E6.96.B9.E6.B3.95.E4.BA.8C.EF.BC.9A.E6.89.8B.E5.8A.A8.E4.B8.8B.E8.BD.BD.EF.BC.88aar.EF.BC.89) 将 SDK 集成到您的工程中。


[](id:step2)
### 步骤2：配置 App 权限
在`AndroidManifest.xml`文件中添加摄像头、麦克风以及网络的申请权限。

```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />

<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```


[](id:step3)
### 步骤3：初始化 SDK 实例并监听事件回调

1. 使用 [sharedInstance()](https://cloud.tencent.com/document/product/647/32267) 接口创建 `TRTCCloud` 实例。
 ```java
// 创建 trtcCloud 实例
mTRTCCloud = TRTCCloud.sharedInstance(getApplicationContext());
mTRTCCloud.setListener(new TRTCCloudListener());
```
2. 设置`setListener`属性注册事件回调，并监听相关事件和错误通知。
```java
// 错误通知监听，错误通知意味着 SDK 不能继续运行
@Override
public void onError(int errCode, String errMsg, Bundle extraInfo) {
    Log.d(TAG, "sdk callback onError");
    if (activity != null) {
        Toast.makeText(activity, "onError: " + errMsg + "[" + errCode+ "]" , Toast.LENGTH_SHORT).show();
        if (errCode == TXLiteAVCode.ERR_ROOM_ENTER_FAIL) {
            activity.exitRoom();
        }
    }
}
```

[](id:step4)
### 步骤4：组装进房参数 TRTCParams
在调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) 接口时需要填写一个关键参数 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a674b3c744a0522802d68dfd208763b59)，该参数包含的必填字段如下表所示。

| 参数名称 | 字段类型 | 补充说明 |填写示例 | 
|---------|---------|---------|---------|
| sdkAppId | 数字 | 应用 ID，您可以在 <a href="https://console.cloud.tencent.com/trtc/app">实时音视频控制台</a> 中查看 SDKAppID。|1400000123 | 
| userId | 字符串 | 只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。 |test_user_001 | 
| userSig | 字符串 | 基于 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。| eJyrVareCeYrSy1SslI... |
| roomId | 数字 | 数字类型的房间号。如果您想使用字符串形式的房间号，请使用 TRTCParams 中的 strRoomId。 | 29834 |

>!
>- TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

[](id:step5)
### 步骤5：主播端开启摄像头预览和麦克风采音
1. 主播端调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a84098740a2e69e3d1f02735861614116) 可以开启本地的摄像头预览，SDK 会向系统请求摄像头使用权限。
2. 主播端调用 [setLocalViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af36ab721c670e5871e5b21a41518b51d) 可以设定本地视频画面的显示模式：
 - Fill 模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
 - Fit 模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
3. 主播端调用 [setVideoEncoderParam()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae047d96922cb1c19135433fa7908e6ce) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/647/32236)。
4. 主播端调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9428ef48d67e19ba91272c9cf967e35e) 开启麦克风，SDK 会向系统请求麦克风使用权限。

```java
//示例代码：发布本地的音视频流
mTRTCCloud.setLocalViewFillMode(TRTC_VIDEO_RENDER_MODE_FIT);
mTRTCCloud.startLocalPreview(mIsFrontCamera, localView);
//设置本地视频编码参数
TRTCCloudDef.TRTCVideoEncParam encParam = new TRTCCloudDef.TRTCVideoEncParam();
encParam.videoResolution = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_960_540;
encParam.videoFps = 15;
encParam.videoBitrate = 1200;
encParam.videoResolutionMode = TRTCCloudDef.TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT;
mTRTCCloud.setVideoEncoderParam(encParam);
mTRTCCloud.startLocalAudio();
```

[](id:step6)
### 步骤6：主播端设置美颜效果

1. 主播端调用 [getBeautyManager()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3fdfeb3204581c27bbf1c8b5598714fb) 可以获取美颜设置接口 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
2. 主播端调用 [setBeautyStyle()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a46ffe2b60f916a87345fb357110adf10) 可以设置美颜风格：
 - Smooth：光滑，效果比较明显，类似网红风格。
 - Nature：自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然。
 - Pitu ：仅 [企业版](https://cloud.tencent.com/document/product/647/32689#Enterprise) 才支持。
3. 主播端调用 [setBeautyLevel()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#a3931ccd8fa54bb846783ab4d6ca2874b) 可以设置磨皮的级别，一般设置为5即可。
4. 主播端调用 [setWhitenessLevel()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#ab08c07ce725dbb8769b61fe0c76b0e95) 可以设置美白级别，一般设置为5即可。


[](id:step7)
### 步骤7：主播端创建房间并开始推流
1. 主播端设置 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a674b3c744a0522802d68dfd208763b59) 中的字段`role`为 **`TRTCCloudDef.TRTCRoleAnchor`**，表示当前用户的角色为主播。
2. 主播端调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) 即可创建 TRTCParams 参数中字段`roomId`的值为房间号的音视频房间，并指定**`appScene`**参数：
 - TRTCCloudDef.TRTC_APP_SCENE_LIVE：视频互动直播模式，本文以该模式为例。
 - TRTCCloudDef.TRTC_APP_SCENE_VOICE_CHATROOM：语音互动直播模式。
3. 房间创建成功后，主播端开始音视频数据的编码和传输流程。同时，SDK 会回调 [onEnterRoom(result)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abf0525c3433cbd923fd1f13b42c416a2)  事件，参数`result`大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当`result`小于0时表示进房失败，具体数值为进房失败的错误码。

```java
public void enterRoom() {
    TRTCCloudDef.TRTCParams trtcParams = new TRTCCloudDef.TRTCParams();
    trtcParams.sdkAppId = sdkappid;
    trtcParams.userId = userid;
    trtcParams.roomId = 908;
    trtcParams.userSig = usersig;
    mTRTCCloud.enterRoom(trtcParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);
}

@Override
public void onEnterRoom(long result) {
    if (result > 0) {
        toastTip("进房成功，总计耗时[\(result)]ms")
    } else {
        toastTip("进房失败，错误码[\(result)]")
    }
}
```

[](id:step8)
### 步骤8：观众端进入房间观看直播
1. 观众端设置 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a674b3c744a0522802d68dfd208763b59) 中的字段`role`为**`TRTCCloudDef.TRTCRoleAudience`**，表示当前用户的角色为观众。
2. 观众端调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) 即可进入 TRTCParams 参数中`roomId`代指的音视频房间，并指定**`appScene`**参数：
 - TRTCCloudDef.TRTC_APP_SCENE_LIVE：视频互动直播模式，本文以该模式为例。
 - TRTCCloudDef.TRTC_APP_SCENE_VOICE_CHATROOM：语音互动直播模式。
3. 观看主播的画面：
 - 如果观众端事先知道主播的 userId，直接在进房成功后使用主播`userId`调用 [startRemoteView(userId, view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 即可显示主播的画面。
 - 如果观众端不知道主播的 userId，观众端在进房成功后会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) 事件通知，使用回调中获取的主播`userId`调用 [startRemoteView(userId, view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 便可显示主播的画面。

[](id:step9)
### 步骤9：观众跟主播连麦
1. 观众端调用 [switchRole(TRTCCloudDef.TRTCRoleAnchor)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a915a4b3abca0e41f057022a4587faf66) 将角色切换为主播（TRTCCloudDef.TRTCRoleAnchor）。
2. 观众端调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a84098740a2e69e3d1f02735861614116) 可以开启本地的画面。
3. 观众端调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9428ef48d67e19ba91272c9cf967e35e) 开启麦克风采音。

```java
//示例代码：观众上麦
mTrtcCloud.switchRole(TRTCCloudDef.TRTCRoleAnchor);
mTrtcCloud.startLocalAudio();
mTrtcCloud.startLocalPreview(mIsFrontCamera, localView);

//示例代码：观众下麦
mTrtcCloud.switchRole(TRTCCloudDef.TRTCRoleAudience);
mTrtcCloud.stopLocalAudio();
mTrtcCloud.stopLocalPreview();
```


[](id:step10)
### 步骤10：主播间进行跨房连麦 PK

TRTC 中两个不同音视频房间中的主播，可以在不退出原来的直播间的场景下，通过“跨房通话”功能拉通连麦通话功能进行“跨房连麦 PK”。

1. 主播 A 调用 [connectOtherRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac1ab7e4a017b99bb91d89ce1b0fac5fd) 接口，目前接口参数采用 JSON 格式，需要将主播 B 的`roomId`和`userId`拼装成格式为`{"roomId": "978","userId": "userB"}`的参数传递给接口函数。
2. 跨房成功后，主播 A 会收到 [onConnectOtherRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac9fd524ab9de446f4aaf502f80859e95)  事件回调。同时，两个直播房间里的所有用户均会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05)  和 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac474bbf919f96c0cfda87c93890d871f) 事件通知。
 例如，当房间“001”中的主播 A 通过`connectOtherRoom()`与房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户会收到主播 B 的`onUserVideoAvailable(B, true)`回调和`onUserAudioAvailable(B, true)`回调。 房间“002”中的用户会收到主播 A 的`onUserVideoAvailable(A, true)` 回调和`onUserAudioAvailable(A, true)`回调。
3. 两个房间里的用户通过调用 [startRemoteView(userId, view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 即可显示另一房间里主播的画面，声音会自动播放。

```java
//示例代码：跨房连麦 PK
mTRTCCloud.ConnectOtherRoom(String.format("{\"roomId\":%s,\"userId\":\"%s\"}", roomId, username));
```

[](id:step11)
### 步骤11：退出当前房间

调用 [exitRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a41d16a97a9cb8f16ef92f5ef5bfebee1) 方法退出房间，SDK 在退房时需要关闭和释放摄像头、麦克风等硬件设备，因此退房动作并非瞬间完成的，需收到 [onExitRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ad5ac26478033ea9c0339462c69f9c89e) 回调后才算真正完成退房操作。

```java
// 调用退房后请等待 onExitRoom 事件回调
mTRTCCloud.exitRoom()

@Override
public void onExitRoom(int reason) {
    Log.i(TAG, "onExitRoom: reason = " + reason);
}
```

>! 如果您的 App 中同时集成了多个音视频 SDK，请在收到`onExitRoom`回调后再启动其它音视频 SDK，否则可能会遇到硬件占用问题。

