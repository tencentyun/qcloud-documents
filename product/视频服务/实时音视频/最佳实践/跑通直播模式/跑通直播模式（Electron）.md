## 适用场景

TRTC 支持四种不同的进房模式，其中视频通话（VideoCall）和语音通话（VoiceCall）统称为 [通话模式](https://cloud.tencent.com/document/product/647/43770)，视频互动直播（Live）和语音互动直播（VoiceChatRoom）统称为直播模式。
直播模式下的 TRTC，支持单个房间最多10万人同时在线，具备小于300ms的连麦延迟和小于1000ms的观看延迟，以及平滑上下麦切换技术。适用低延时互动直播、十万人互动课堂、视频相亲、在线教育、远程培训、超大型会议等应用场景。

## 原理解析

TRTC 云服务由两种不同类型的服务器节点组成，分别是“接口机”和“代理机”：

-   **接口机**
    该类节点都采用最优质的线路和高性能的机器，善于处理端到端的低延时连麦通话。
-   **代理机**
    该类节点都采用普通的线路和性能一般的机器，善于处理高并发的拉流观看需求。

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

创建 `trtc-electron-sdk` 实例：

```javascript
import TRTCCloud from 'trtc-electron-sdk';
let trtcCloud = new TRTCCloud();
```

监听 `onError` 事件:

```javascript
// 错误通知是要监听的，需要捕获并通知用户
let onError = function(err) {
  console.error(err);
}
trtcCloud.on('onError',onError);
```

[](id:step4)
### 步骤4： 组装进房参数 TRTCParams

在调用 [enterRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enterRoom) 接口时需要填写一个关键参数 [TRTCParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCParams.html)，该参数包含的必填字段如下表所示。

| 参数     | 类型   | 说明                                                         | 示例                   |
| :------- | :----- | :----------------------------------------------------------- | :--------------------- |
| sdkAppId | 数字   | 应用 ID，您可以在 [控制台](https://console.cloud.tencent.com/trtc/app) >【应用管理】>【应用信息】中查找到。 | 1400000123             |
| userId   | 字符串 | 只允许包含大小写英文字母（a-z、A-Z）、数字（0-9）及下划线和连词符。 | test_user_001|
| userSig  | 字符串 | 基于 userId 可以计算出 userSig，计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275) 。 | eJyrVareCeYrSy1SslI... |
| roomId   | 数字   | 数字类型的房间号。如果您想使用字符串形式的房间号，请使用 TRTCParams 中的 strRoomId。 | 29834  |

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
param.role = TRTCRoleType.TRTCRoleAnchor; // 设置角色为"主播"
:::
</dx-codeblock>

>! 
>- TRTC 同一时间不支持两个相同的 userId 进入房间，否则会相互干扰。
>- 每个端在应用场景 appScene 上必须要进行统一，否则会出现一些不可预料的问题。

[](id:step5)
### 步骤5：主播端开启摄像头预览和麦克风采音
1.  主播端调用 [startLocalPreview()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalPreview) 可以开启本地的摄像头预览，SDK 会向系统请求摄像头使用权限。
2.  主播端调用 `setLocalViewFillMode()` 可以设定本地视频画面的显示模式：
    -   `TRTCVideoFillMode.TRTCVideoFillMode_Fill`： 模式表示填充，画面可能会被等比放大和裁剪，但不会有黑边。
    -   `TRTCVideoFillMode.TRTCVideoFillMode_Fit`： 模式表示适应，画面可能会等比缩小以完全显示其内容，可能会有黑边。
3.  主播端调用 [setVideoEncoderParam()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderParam) 接口可以设定本地视频的编码参数，该参数将决定房间里其他用户观看您的画面时所感受到的 [画面质量](https://cloud.tencent.com/document/product/647/32236)。
4.  主播端调用 [startLocalAudio()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalAudio) 开启麦克风，SDK 会向系统请求麦克风使用权限。


<dx-codeblock>
::: javascript javascript
//示例代码：发布本地的音视频流
trtcCloud.startLocalPreview(view);
trtcCloud.startLocalAudio();
trtcCloud.setLocalViewFillMode(TRTCVideoFillMode.TRTCVideoFillMode_Fill);

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

[](id:step6)
### 步骤6：主播端设置美颜效果

1.  主播端可调用 [setBeautyStyle(style, beauty, white, ruddiness)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBeautyStyle) 来开启美颜效果
2.  参数说明：
    -   style： 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。
        -   `TRTCBeautyStyle.TRTCBeautyStyleSmooth`: 光滑，适用于美女秀场，效果比较明显。
        -   `TRTCBeautyStyle.TRTCBeautyStyleNature`: 自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然。
    -   beauty：美颜级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。
    -   white：美白级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。
    -   ruddiness：红润级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显，该参数 Windows 平台暂未生效。

```javascript
// 开启美颜 
trtcCloud.setBeautyStyle(TRTCBeautyStyle.TRTCBeautyStyleNature, 5, 5, 5);
```


[](id:step7)
### 步骤7：主播端创建房间并开始推流

1.  主播端设置 [TRTCParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCParams.html) 中的字段`role`为 **`TRTCRoleType.TRTCRoleAnchor`**，表示当前用户的角色为主播。
2.  主播端调用 enterRoom( )即可创建 TRTCParams 参数字段 `roomId`   的值为房间号的音视频房间，并指定 `appScene` 参数：
    -   `TRTCAppScene.TRTCAppSceneLIVE`：视频互动直播，支持平滑上下麦，切换过程无需等待，主播延时小于300ms；支持十万级别观众同时播放，播放延时低至1000ms。本文以该模式为例。
    -   `TRTCAppScene.TRTCAppSceneVoiceChatRoom`：语音互动直播，支持平滑上下麦，切换过程无需等待，主播延时小于300ms；支持十万级别观众同时播放，播放延时低至1000ms。 
    -   关于 `TRTCAppScene` 的详细介绍，请参见 [TRTCAppScene ](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCAppScene)。
3.  房间创建成功后，主播端开始音视频数据的编码和传输流程。同时，SDK 会回调 [onEnterRoom(result)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onEnterRoom) 事件，参数 `result` 大于0时表示进房成功，具体数值为加入房间所消耗的时间，单位为毫秒（ms）；当 `result` 小于0时表示进房失败，具体数值为进房失败的错误码。

<dx-codeblock>
::: javascript javascript
let onEnterRoom = function (result) {
  if (result > 0) {
    console.log(`onEnterRoom，进房成功，使用了 ${result} 秒`);
  } else {
    console.warn(`onEnterRoom: 进房失败 ${result}`);
  }
};

trtcCloud.on('onEnterRoom', onEnterRoom);

let param = new TRTCParams();
param.sdkAppId = 1400000123;
param.roomId = 29834;
param.userId = 'test_user_001';
param.userSig = 'eJyrVareCeYrSy1SslI...';
param.role = TRTCRoleType.TRTCRoleAnchor;
trtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneLIVE);
:::
</dx-codeblock>

[](id:step8)
### 步骤8：观众端进入房间观看直播

1.  观众端设置[TRTCParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCParams.html)中的字段 `role` 为 **`TRTCRoleType.TRTCRoleAudience`**，表示当前用户的角色为观众。
1.  观众端调用 `enterRoom()` 即可进入 `TRTCParams` 参数中 `roomId` 代指的音视频房间，并指定 `appScene` 参数：
    -   `TRTCAppScene.TRTCAppSceneLIVE`：视频互动直播。
    -   `TRTCAppScene.TRTCAppSceneVoiceChatRoom`：语音互动直播。
2.  观看主播的画面：
    -  如果观众端事先知道主播的 `userId`，直接在进房成功后使用主播 `userId` 调用 [startRemoteView(userId, view)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) 即可显示主播的画面。
    -  如果观众端不知道主播的 `userId`，观众端在进房成功后会收到 [onUserVideoAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVideoAvailable) 事件通知，使用回调中获取的主播 `userId` 调用 [startRemoteView(userId, view)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) 便可显示主播的画面。

<dx-codeblock>
::: html html
<div id="video-container"></div>
<script>
  const videoContainer = document.querySelector('#video-container');
  const roomId = 29834;
  // 进房回调，当进房成功时，会触发此回调
  let onEnterRoom = function(result) {
    if (result > 0) {
      console.log(`onEnterRoom，进房成功，使用了 ${result} 秒`);
    } else {
      console.warn(`onEnterRoom: 进房失败 ${result}`);
    }
  };
  // 当主播开启/关闭摄像头推流时，会触发此回调
  let onUserVideoAvailable = function(userId, available) {
    if (available === 1) {
        let id = `${userId}-${roomId}-${TRTCVideoStreamType.TRTCVideoStreamTypeBig}`;
        let view = document.getElementById(id);
        if (!view) {
          view = document.createElement('div');
          view.id = id;
          videoContainer.appendChild(view);
        }
        trtcCloud.startRemoteView(userId, view);
        trtcCloud.setRemoteViewFillMode(userId, TRTCVideoFillMode.TRTCVideoFillMode_Fill);
    } else {
        let id = `${userId}-${roomId}-${TRTCVideoStreamType.TRTCVideoStreamTypeBig}`;
        let view = document.getElementById(id);
        if (view) {
          videoContainer.removeChild(view);
        }
    }
  };

  trtcCloud.on('onEnterRoom', onEnterRoom);
  trtcCloud.on('onUserVideoAvailable', onUserVideoAvailable);

  let param = new TRTCParams();
  param.sdkAppId = 1400000123;
  param.roomId = roomId;
  param.userId = 'test_user_001';
  param.userSig = 'eJyrVareCeYrSy1SslI...';
  param.role = TRTCRoleType.TRTCRoleAudience; // 设置角色为“观众”
  trtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneLIVE);
</script>
:::
</dx-codeblock>

[](id:step9)
### 步骤9：观众跟主播连麦

1.  观众端调用 [switchRole(TRTCRoleType.TRTCRoleAnchor)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#switchRole) 将角色切换为主播（`TRTCRoleType.TRTCRoleAnchor`）。
2.  观众端调用 [startLocalPreview()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalPreview) 可以开启本地的画面。
3.  观众端调用 [startLocalAudio()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalAudio) 开启麦克风采音。

<dx-codeblock>
::: javascript javascript
//示例代码：观众上麦
trtcCloud.switchRole(TRTCRoleType.TRTCRoleAnchor);
trtcCloud.startLocalAudio();
trtcCloud.startLocalPreview(frontCamera, view);

//示例代码：观众下麦
trtcCloud.switchRole(TRTCRoleType.TRTCRoleAudience);
trtcCloud.stopLocalAudio();
trtcCloud.stopLocalPreview();
:::
</dx-codeblock>


[](id:step10)
### 步骤10：主播间进行跨房连麦 PK

TRTC 中两个不同音视频房间中的主播，可以在不退出原来的直播间的场景下，通过“跨房通话”功能拉通连麦通话功能进行“跨房连麦 PK”。

1.  主播 A 调用 [connectOtherRoom()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#connectOtherRoom) 接口，接口参数目前采用 JSON 格式，需要将主播 B 的`roomId`和`userId`拼装成格式为`{"roomId": 978,"userId": "userB"}`的参数传递给接口函数。
2.  跨房成功后，主播 A 会收到 [onConnectOtherRoom(userId, errCode, errMsg)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onConnectOtherRoom) 事件回调。同时，两个直播房间里的所有用户均会收到 [onUserVideoAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVideoAvailable) 和 [onUserAudioAvailable()](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserAudioAvailable) 事件通知。
    例如，当房间“001”中的主播 A 通过`connectOtherRoom()`与房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户会收到主播 B 的`onUserVideoAvailable(B, true)`回调和`onUserAudioAvailable(B, true)`回调。 房间“002”中的用户会收到主播 A 的`onUserVideoAvailable(A,  true)` 回调和`onUserAudioAvailable(A, true)`回调。
3.  两个房间里的用户通过调用 [startRemoteView(userId, view)](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) 即可显示另一房间里主播的画面，声音会自动播放。

![主播连麦时序图](http://main.qcloudimg.com/raw/ac5b230340ebdab69998f95844fa61c1/%E4%B8%BB%E6%92%AD%E8%BF%9E%E9%BA%A6%E6%97%B6%E5%BA%8F%E5%9B%BE.png)

<dx-codeblock>
::: javascript javascript
//示例代码：跨房连麦 PK
let onConnectOtherRoom = function(userId, errCode, errMsg) {
  if(errCode === 0) {
    console.log(`成功连上主播 ${userId} 的房间`);
  } else {
    console.warn(`连接其他主播房间失败：${errMsg}`);
  }
};

const paramJson = '{"roomId": "978","userId": "userB"}';
trtcCloud.connectOtherRoom(paramJson);
trtcCloud.on('onConnectOtherRoom', onConnectOtherRoom); 
:::
</dx-codeblock>

[](id:step11)
### 步骤11：退出当前房间  

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

>! 如果您的 Electron 程序中同时集成了多个音视频 SDK，请在收到`onExitRoom`回调后再启动其它音视频 SDK，否则可能会遇到硬件占用问题。
