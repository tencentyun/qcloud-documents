## 适用场景

TRTC 支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（VoiceCall）统称为通话模式，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为 [直播模式](https://cloud.tencent.com/document/product/647/43771)。
通话模式下的 TRTC，支持单个房间最多300人同时在线，支持最多50人同时发言。适合1对1视频通话、300人视频会议、在线问诊、远程面试、视频客服、在线狼人杀等应用场景。

## 原理解析

TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：

-   **接口机**
    该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话，单位时长计费较高。
-   **代理机**
    该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求，单位时长计费较低。

在通话模式下，TRTC 房间中的所有用户都会被分配到接口机上，相当于每个用户都是“主播”，每个用户随时都可以发言（最高的上行并发限制为50路），因此适合在线会议等场景，但单个房间的人数限制为300人。

![](https://main.qcloudimg.com/raw/b88a624c0bd67d5d58db331b3d64c51c.gif)

## 示例代码

您可以登录 [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Electron) 获取本文档相关的示例代码。

## 操作步骤

[](id:step1)
### 步骤1：尝试跑通官网 SimpleDemo

建议您先阅读文档 [跑通 SimpleDemo(Electron)](https://cloud.tencent.com/document/product/647/38548)，并按照文档的指引，跑通我们为您提供的官方 SimpleDemo。

- 如果 SimpleDemo 能顺利运行，说明您已经掌握了在项目中安装 Electron 的方法。
- 反之，如果运行 SimpleDemo 遇到问题，您大概率遭遇了 Electron 的下载、安装问题，此时您可以参考我们总结的 [Electron常见问题收录](https://cloud.tencent.com/developer/article/1616668) ，也可以参考 Electron 官方的 [安装指引](https://www.electronjs.org/docs/tutorial/installation) 。

[](id:step2)
### 步骤2：为您的项目集成 trtc-electron-sdk

如果 [步骤1](#step1) 正常执行并且效果符合预期，说明您已经掌握了 Electron 环境的安装方法。

- 您可以在我们的官方 Demo 的基础上进行二次开发，项目的起步阶段会比较顺利。
- 您也可以执行以下指令，把 `trtc-electron-sdk` 安装到您现有的项目中：
```bash
npm install trtc-electron-sdk --save
```

[](id:step3)
### 步骤3：初始化 SDK 实例并监听事件回调

1. 创建 `trtc-electron-sdk` 实例：
```javascript
import TRTCCloud from 'trtc-electron-sdk';
let trtcCloud = new TRTCCloud();
```
2. 监听 `onError` 事件：
<dx-codeblock>
::: javascript javascript
// 错误通知是要监听的，需要捕获并通知用户
let onError = function(err) {
  console.error(err);
};
trtcCloud.on('onError',onError);
:::
</dx-codeblock>

[](id:step4)
### 步骤4： 组装进房参数 TRTCParams

在调用 [enterRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enterRoom) 接口时需要填写一个关键参数 [TRTCParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCParams.html)，该参数包含的必填字段如下表所示。

| 参数     | 类型   | 说明                                                         | 示例                   |
| :------- | :----- | :----------------------------------------------------------- | :--------------------- |
| sdkAppId | 数字   | 应用 ID，您可以在 [控制台](https://console.cloud.tencent.com/trtc/app) >【应用管理】>【应用信息】中查找到。 | 1400000123  |
| userId   | 字符串 | 只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。 | test_user_001 |
| userSig  | 字符串 | 基于 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275) 。 | eJyrVareCeYrSy1SslI... |
| roomId   | 数字   | 数字类型的房间号。如果您想使用字符串形式的房间号，请使用 TRTCParams 中的 strRoomId。 | 29834 |

<dx-codeblock>
::: javascript javascript
import {
  TRTCParams,
  TRTCRoleType 
} from "trtc-electron-sdk/liteav/trtc_define";

let param = new TRTCParams();
param.sdkAppId = 1400000123;
param.roomId = 29834;
param.userId = 'test_user_001';
param.userSig = 'eJyrVareCeYrSy1SslI...';
:::
</dx-codeblock>


>! 
>- TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

[](id:step5)
### 步骤5：创建并进入房间

1. 调用  [enterRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enterRoom)  即可加入 `TRTCParams` 参数中 `roomId` 代指的音视频房间。如果该房间不存在，SDK 会自动创建一个以字段 `roomId` 的值为房间号的新房间。
2. 请根据应用场景设置合适的  `appScene`  参数，使用错误可能会导致卡顿率或画面清晰度不达预期。
   - 视频通话，请设置为 `TRTCAppScene.TRTCAppSceneVideoCall`。
   - 语音通话，请设置为 `TRTCAppScene.TRTCAppSceneAudioCall`。
>? 关于 `TRTCAppScene` 的详细介绍，请参见 [TRTCAppScene ](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCAppScene)。
3. 进房成功后，SDK 会回调 [onEnterRoom(result)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onEnterRoom) 事件。其中，参数 `result` 大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当 `result` 小于0时表示进房失败，具体数值为进房失败的错误码。

<dx-codeblock>
::: javascript javascript
import TRTCCloud from 'trtc-electron-sdk';
import { TRTCParams, TRTCAppScene } from "trtc-electron-sdk/liteav/trtc_define";
import TRTCCloud from 'trtc-electron-sdk';
let trtcCloud = new TRTCCloud();

let onEnterRoom = function (result) {
  if (result > 0) {
    console.log(`onEnterRoom，进房成功，使用了 ${result} 秒`);
  } else {
    console.warn(`onEnterRoom: 进房失败 ${result}`);
  }
};

// 订阅进房成功事件
trtcCloud.on('onEnterRoom', onEnterRoom);

// 进房，如果房间不存在，TRTC 后台会自动创建一个新房间
let param = new TRTCParams();
param.sdkAppId = 1400000123;
param.roomId = 29834;
param.userId = 'test_user_001';
param.userSig = 'eJyrVareCeYrSy1SslI...';
trtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneVideoCall);
:::
</dx-codeblock>


[](id:step6)
### 步骤6: 订阅远端的音视频流

SDK 支持自动订阅和手动订阅两种模式，自动订阅追求秒开速度，适合于人数少的通话场景；手动订阅追求流量节约，适合人数较多的会议场景。

#### 自动订阅（推荐）

进入某个房间之后，SDK 会自动接收房间中其他用户的音频流，从而达到最佳的“秒开”效果：

1.  当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserAudioAvailable) 事件通知，SDK 会自动播放这些远端用户的声音。
2.  您可以通过 [muteRemoteAudio(userId,  true)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteRemoteAudio) 屏蔽某一个 userId 的音频数据，也可以通过 [muteAllRemoteAudio(true)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteAllRemoteAudio) 屏蔽所有远端用户的音频数据，屏蔽后 SDK 不再继续拉取对应远端用户的音频数据。
3.  当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVideoAvailable) 事件通知，但此时 SDK 未收到该如何展示视频数据的指令，因此不会自动处理视频数据。您需要通过调用 [startRemoteView(userId, view, streamType)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) 方法将远端用户的视频数据和显示 `view` 关联起来。
4.  您可以通过  [setLocalViewFillMode()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalViewFillMode)  指定视频画面的显示模式：
    -   `TRTCVideoFillMode.TRTCVideoFillMode_Fill` 模式：表示填充，画面可能会等比放大和裁剪，但不会有黑边。
    -   `TRTCVideoFillMode.TRTCVideoFillMode_Fit` 模式：表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
5.  您可以通过 [stopRemoteView(userId)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopRemoteView) 可以屏蔽某一个 userId 的视频数据，也可以通过 [stopAllRemoteView()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopAllRemoteView) 屏蔽所有远端用户的视频数据，屏蔽后 SDK 不再继续拉取对应远端用户的视频数据。

<dx-codeblock>
::: html html
<div id="video-container"></div>

<script>
  import TRTCCloud from 'trtc-electron-sdk';
  const trtcCloud = new TRTCCloud();
  const videoContainer = document.querySelector('#video-container');
  const roomId = 29834;

  /**
   * 用户是否开启摄像头视频
   * @param {number} uid - 用户标识
   * @param {boolean} available - 画面是否开启
   **/
  let onUserVideoAvailable = function (uid, available) {
    console.log(`onUserVideoAvailable: uid: ${uid}, available: ${available}`);
    if (available === 1) {
      let id = `${uid}-${roomId}-${TRTCVideoStreamType.TRTCVideoStreamTypeBig}`;
      let view = document.getElementById(id);
      if (!view) {
        view = document.createElement('div');
        view.id = id;
        videoContainer.appendChild(view);
      }
      trtcCloud.startRemoteView(uid, view);
      trtcCloud.setRemoteViewFillMode(uid, TRTCVideoFillMode.TRTCVideoFillMode_Fill);
    } else {
      let id = `${uid}-${roomId}-${TRTCVideoStreamType.TRTCVideoStreamTypeBig}`;
      let view = document.getElementById(id);
      if (view) {
        videoContainer.removeChild(view);
      }
    }
  };

  // 实例代码：根据通知订阅（或取消订阅）远端用户的视频画面
  trtcCloud.on('onUserVideoAvailable', onUserVideoAvailable);

</script>
:::
</dx-codeblock>

>? 如果您在收到 `onUserVideoAvailable()` 事件回调后没有立即调用 `startRemoteView()` 订阅视频流，SDK 将会在5s内停止接收来自远端的视频数据。

#### 手动订阅

您可以通过 [setDefaultStreamRecvMode(autoRecvAudio, autoRecvVideo)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setDefaultStreamRecvMode) 接口将 SDK 指定为手动订阅模式。在手动订阅模式下，SDK 不会自动接收房间中其他用户的音视频数据，需要您手动通过 API 函数触发。

1.  在**进房前**调用 [setDefaultStreamRecvMode(false, false)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setDefaultStreamRecvMode) 接口将 SDK 设定为手动订阅模式。
2.  当房间中有其他用户在上行音频数据时，您会收到 [onUserAudioAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserAudioAvailable) 事件通知。此时，您需要通过调用 [muteRemoteAudio(userId, false)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteRemoteAudio) 手动订阅该用户的音频数据，SDK 会在接收到该用户的音频数据后解码并播放。
3.  当房间中有其他用户在上行视频数据时，您会收到 [onUserVideoAvailable(userId, available)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVideoAvailable) 事件通知。此时，您需要通过调用 [startRemoteView(userId,  view)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) 方法手动订阅该用户的视频数据，SDK 会在接收到该用户的视频数据后解码并播放。


[](id:step7)
### 步骤7：发布本地的音视频流

1. 调用 [startLocalAudio()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalAudio) 可以开启本地的麦克风采集，并将采集到的声音编码并发送出去。
2. 调用 [startLocalPreview()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalPreview) 可以开启本地的摄像头，并将采集到的画面编码并发送出去。
3. 调用 [setLocalViewFillMode()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalViewFillMode) 可以设定本地视频画面的显示模式：
   - `TRTCVideoFillMode.TRTCVideoFillMode_Fill`：模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
   - `TRTCVideoFillMode.TRTCVideoFillMode_Fit`：模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
4. 调用 [setVideoEncoderParam()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderParam) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/647/32236)。

<dx-codeblock>
::: javascript javascript
//示例代码：发布本地的音视频流
trtcCloud.startLocalPreview(view);
trtcCloud.setLocalViewFillMode(TRTCVideoFillMode.TRTCVideoFillMode_Fill);
trtcCloud.startLocalAudio();
//设置本地视频编码参数
let encParam = new TRTCVideoEncParam();
encParam.videoResolution = TRTCVideoResolution.TRTCVideoResolution_640_360;
encParam.resMode = TRTCVideoResolutionMode.TRTCVideoResolutionModeLandscape;
encParam.videoFps = 25;
encParam.videoBitrate = 600;
encParam.enableAdjustRes = true;
trtcCloud.setVideoEncoderParam(encParam);
:::
</dx-codeblock>


>! SDK 默认会使用当前系统默认的摄像头和麦克风。您可以通过调用 [setCurrentCameraDevice()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentCameraDevice) 和 [setCurrentMicDevice()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDevice) 选择其他摄像头和麦克风。


[](id:step8)
### 步骤8：退出当前房间

调用 [exitRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#exitRoom) 方法退出房间，SDK 在退房时需要关闭和释放摄像头、麦克风等硬件设备，因此退房动作并非瞬间完成的，需收到 [onExitRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onExitRoom) 回调后才算真正完成退房操作。

<dx-codeblock>
::: javascript javascript
// 调用退房后请等待 onExitRoom 事件回调
let onExitRoom = function (reason) {
  console.log(`onExitRoom, reason: ${reason}`);
};
trtcCloud.exitRoom();
trtcCloud.on('onExitRoom', onExitRoom);
:::
</dx-codeblock>

>! 如果您的 Electron 程序中同时集成了多个音视频 SDK，请在收到 `onExitRoom` 回调后再启动其它音视频 SDK，否则可能会遇到硬件占用问题。
