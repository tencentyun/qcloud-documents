## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 适用场景

音视频通话TRTC 功能模块支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（VoiceCall）统称为通话模式，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为 [直播模式](https://cloud.tencent.com/document/product/647/35428)。
通话模式下的 TRTC，支持单个房间最多300人同时在线，支持最多50人同时发言。适合1对1视频通话、300人视频会议、在线问诊、远程面试、视频客服、在线狼人杀等应用场景。

## 原理解析
音视频通话TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：
- **接口机**
该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话，单位时长计费较高。
- **代理机**
该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求，单位时长计费较低。

在通话模式下，音视频通话TRTC 房间中的所有用户都会被分配到接口机上，相当于每个用户都是“主播”，每个用户随时都可以发言（最高的上行并发限制为50路），因此适合在线会议等场景，但单个房间的人数限制为300人。
![](https://main.qcloudimg.com/raw/b88a624c0bd67d5d58db331b3d64c51c.gif)

## 示例代码
您可以登录 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTC-API-Example) 获取本文档相关的示例代码。
![](https://main.qcloudimg.com/raw/cdef573133900a8dce22dcca5242fcfc.png)

>?如果访问 Github 较慢，您也可以直接下载 [TXLiteAVSDK_TRTC_Android_latest.zip](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_latest.zip)。

## 操作步骤
[](id:step1)
### 步骤1：集成 SDK
您可以选择以下方式将**音视频通话 TRTC SDK** 集成到项目中。
#### 方式一：自动加载（aar）
音视频通话 TRTC SDK 已发布到 jcenter 库，您可以通过配置 gradle 自动下载更新。
您只需用 Android Studio 打开待集成 SDK 的工程（[TRTC-API-Example](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTC-API-Example) 已完成集成，示例代码可以供您参考），然后通过简单的步骤修改 `app/build.gradle` 文件，即可完成 SDK 集成：

1. 在 dependencies 中添加 TRTCSDK 的依赖。
```
dependencies {
      compile 'com.tencent.liteav:LiteAVSDK_TRTC:latest.release'
}
```
2. 在 defaultConfig 中，指定 App 使用的 CPU 架构。
>?目前 TRTC SDK 支持 armeabi ， armeabi-v7a 和 arm64-v8a。
```
 defaultConfig {
      ndk {
          abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
      }
  }
```
3. 单击【Sync Now】同步 SDK。
 如果您的网络连接 jcenter 没有问题，SDK 会自动下载集成到工程中。

#### 方式二：下载 ZIP 包手动集成
您可以直接下载 [ZIP 压缩包](https://cloud.tencent.com/document/product/647/32689)，并参考 [快速集成(Android)](https://cloud.tencent.com/document/product/647/32175#.E6.96.B9.E6.B3.95.E4.BA.8C.EF.BC.9A.E6.89.8B.E5.8A.A8.E4.B8.8B.E8.BD.BD.EF.BC.88aar.EF.BC.89) 将 SDK 集成到您的工程中。


[](id:step2)
### 步骤2：配置 App 权限
在 `AndroidManifest.xml `文件中添加摄像头、麦克风以及网络的申请权限。
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
```
// 创建 trtcCloud 实例
mTRTCCloud = TRTCCloud.sharedInstance(getApplicationContext());
mTRTCCloud.setListener(new TRTCCloudListener(){
    // 回调处理
    ...
});
```
2. 设置 `setListener` 属性注册事件回调，并监听相关事件和错误通知。
```
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
| userSig | 字符串 | 基于 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/1449/58939)。| eJyrVareCeYrSy1SslI... |
| roomId | 数字 | 默认不支持字符串类型的房间号，字符串类型的房间号会影响进房速度。如果您确实需要支持字符串类型的房间号，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。 | 29834 |

>!TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。

[](id:step5)
### 步骤5：创建并进入房间
1. 调用 [enterRoom()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) 即可加入 TRTCParams 参数中 `roomId` 代指的音视频房间。如果该房间不存在，SDK 会自动创建一个以字段 `roomId` 的值为房间号的新房间。
2. 请根据应用场景设置合适的 **appScene** 参数，使用错误可能会导致卡顿率或画面清晰度不达预期。
 - 视频通话，请设置为 `TRTC_APP_SCENE_VIDEOCALL`。
 - 语音通话，请设置为 `TRTC_APP_SCENE_AUDIOCALL`。
3. 进房成功后，SDK 会回调 `onEnterRoom(result)` 事件。其中，参数 `result` 大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当 `result` 小于0时表示进房失败，具体数值为进房失败的错误码。

```
public void enterRoom() {
    TRTCCloudDef.TRTCParams trtcParams = new TRTCCloudDef.TRTCParams();
    trtcParams.sdkAppId = sdkappid;
    trtcParams.userId = userid;
    trtcParams.roomId = 908;
    trtcParams.userSig = usersig;
    mTRTCCloud.enterRoom(trtcParams, TRTC_APP_SCENE_VIDEOCALL);
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
>! 
>- 如果进房失败，SDK 同时还会回调 `onError` 事件，并返回参数 `errCode`（[错误码](https://cloud.tencent.com/document/product/1449/57189)）、`errMsg`（错误原因）以及 `extraInfo`（保留参数）。
>- 如果已在某一个房间中，则必须先调用 `exitRoom()`退出当前房间，才能进入下一个房间。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

[](id:step6)
### 步骤6：订阅远端的音视频流
SDK 支持自动订阅和手动订阅。

#### 自动订阅模式（默认）
在自动订阅模式下，进入某个房间后，SDK 会自动接收房间中其他用户的音频流，从而达到最佳的“秒开”效果：
1. 当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac474bbf919f96c0cfda87c93890d871f) 事件通知，SDK 会自动播放远端用户的声音。
2. 您可以通过 [muteRemoteAudio(userId, true)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8d8b8edf120036d4049cc3639a1ce81f) 屏蔽某一个 userId 的音频数据，也可以通过 [muteAllRemoteAudio(true)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5b63c0796404b80323ae67aafe0384ba) 屏蔽所有远端用户的音频数据，屏蔽后 SDK 不再继续拉取对应远端用户的音频数据。
3. 当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) 事件通知，但此时 SDK 未收到该如何展示视频数据的指令，因此不会自动处理视频数据。您需要通过调用 [startRemoteView(userId, view)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 方法将远端用户的视频数据和显示`view`关联起来。
4. 您可以通过 [setRemoteViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab4197bc2efb62b471b49f926bab9352f) 指定视频画面的显示模式：
 - Fill 模式：表示填充，画面可能会等比放大和裁剪，但不会有黑边。
 - Fit 模式：表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
5. 您可以通过 [stopRemoteView(userId)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8f3e86bc219090d0e8f2d5c2fab4467a) 屏蔽某一个 userId 的视频数据，也可以通过 [stopAllRemoteView()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#addaac0786ac0bd6e73a5f35c038df127) 屏蔽所有远端用户的视频数据，屏蔽后 SDK 不再继续拉取对应远端用户的视频数据。

```
@Override
public void onUserVideoAvailable(String userId, boolean available) {
    TXCloudVideoView remoteView = remoteViewDic[userId];
    if (available) {
        mTRTCCloud.startRemoteView(userId, remoteView);
        mTRTCCloud.setRemoteViewFillMode(userId, TRTC_VIDEO_RENDER_MODE_FIT);
    } else {
        mTRTCCloud.stopRemoteView(userId);
    }
}
```

>? 如果您在收到 `onUserVideoAvailable()` 事件回调后没有立即调用 `startRemoteView()` 订阅视频流，SDK 将在5s内停止接收来自远端的视频数据。

#### 手动订阅模式
您可以通过 [setDefaultStreamRecvMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b8d004665d5003ce1d9a48a9ab551b3) 接口将 SDK 指定为手动订阅模式。在手动订阅模式下，SDK 不会自动接收房间中其他用户的音视频数据，需要您手动通过 API 函数触发。

1. 在**进房前**调用 [setDefaultStreamRecvMode(false, false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b8d004665d5003ce1d9a48a9ab551b3) 接口将 SDK 设定为手动订阅模式。
2. 当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac474bbf919f96c0cfda87c93890d871f) 事件通知。此时，您需要通过调用 [muteRemoteAudio(userId, false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8d8b8edf120036d4049cc3639a1ce81f) 手动订阅该用户的音频数据，SDK 会在接收到该用户的音频数据后解码并播放。
3. 当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) 事件通知。此时，您需要通过调用 [startRemoteView(userId, remoteView)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 方法手动订阅该用户的视频数据，SDK 会在接收到该用户的视频数据后解码并播放。


[](id:step7)
### 步骤7：发布本地的音视频流
1. 调用 [startLocalAudio()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9428ef48d67e19ba91272c9cf967e35e) 可以开启本地的麦克风采集，并将采集到的声音编码并发送出去。
2. 调用 [startLocalPreview()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a84098740a2e69e3d1f02735861614116) 可以开启本地的摄像头，并将采集到的画面编码并发送出去。
3. 调用 [setLocalViewFillMode()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af36ab721c670e5871e5b21a41518b51d) 可以设定本地视频画面的显示模式：
 - Fill 模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
 - Fit 模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
4. 调用 [setVideoEncoderParam()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae047d96922cb1c19135433fa7908e6ce) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/1449/57122)。
```java
//示例代码：发布本地的音视频流
mTRTCCloud.setLocalViewFillMode(TRTC_VIDEO_RENDER_MODE_FIT);
mTRTCCloud.startLocalPreview(mIsFrontCamera, mLocalView);
mTRTCCloud.startLocalAudio();
```

[](id:step8)
### 步骤8：退出当前房间

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

