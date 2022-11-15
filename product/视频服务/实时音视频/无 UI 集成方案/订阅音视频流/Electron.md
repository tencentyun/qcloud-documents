本文档主要介绍如何订阅房间中其他用户的音视频流，也就是如何播放其他用户的音频和视频。为了方便起见，我们在接下来的文档中，会将“房间中的其他用户”统称为“远端用户”。
![](https://qcloudimg.tencent-cloud.cn/raw/692f3cddee1dc9e9dfadde81448643ad.png)

## 调用指引

[](id:step1)
### 步骤1：完成前序步骤
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/38549) 完成 SDK 的导入。

[](id:step2)
### 步骤2：设定订阅模式（非必须）
您可以通过调用 TRTCCloud 中的 **setDefaultStreamRecvMode** 接口设置订阅模式，TRTC 提供了两种订阅模式：
- 自动订阅：SDK 会自动播放远端用户的声音，无需您进行额外操作，这是 SDK 的默认行为。
- 手动订阅：SDK 不会自动拉取和播放远端用户的声音，需要您手动调用 **muteRemoteAudio(userId, false)** 来触发声音的播放。
>! 需要您注意的是，如果您不调用 setDefaultStreamRecvMode 也是没有关系的，SDK 的默认行为是自动订阅。但如果您希望设置为手动订阅，**请务必注意 setDefaultStreamRecvMode 只有在 enterRoom 之前调用才有效果。**

[](id:step3)
### 步骤3：进入 TRTC 房间
参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74635) 让当前用户进入 TRTC 房间，只有在成功进入房间之后才能订阅其他用户的音视频流。

[](id:step4)
### 步骤4：音频流的播放
您可以通过调用接口 muteRemoteAudio("denny"，true) 来静音远端用户 denny 的声音，之后也可以通过调用接口 muteRemoteAudio('denny'，false) 来解除对他的静音。

```javascript
import TRTCCloud from 'trtc-electron-sdk';
const rtcCloud = new TRTCCloud();

// Reference https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteRemoteAudio
// Mute user with id denny
rtcCloud.muteRemoteAudio('denny', true);
// Unmute user with id denny
rtcCloud.muteRemoteAudio('denny', false);
```

[](id:step5)
### 步骤5：视频流的播放

#### 1. 开始和停止播放（startRemoteView + stopRemoteView）
您可以通过调用接口 startRemoteView 来播放远端用户的视频画面，但前提是您需要传递给 SDK 一个 view 对象，用来作为承载该用户的视频画面的渲染控件。

startRemoteView 的第一个参数是远端用户的 userId，第二个参数是远端用户的流类型，第三个参数则是您需要传递的 view 对象。其中第二个参数 streamType(流类型) 有三个可选的值，分别是：
- **TRTCVideoStreamTypeBig**：用户的主路画面，一般用来传输用户摄像头的画面。
- **TRTCVideoStreamTypeSub**：用户的辅路画面，一般用来传输用户屏幕分享的画面。
- **TRTCVideoStreamTypeSmall**：用户的低清小画面，这是相对于主路画面而言的，只有当远端用户开启了“双路编码（enableEncSmallVideoStream）”之后，我们才能播放他/她的低清画面。并且同时只能在主路画面和低清小画面中二选一。

通过调用 stopRemoteView 接口，您可以停止播放某一个远端用户的视频，也可以通过 stopAllRemoteView 接口停止播放所有远端用户的视频。

```javascript
// 可参考 https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView

import TRTCCloud, { TRTCVideoStreamType } from 'trtc-electron-sdk';

const cameraView = document.querySelector('.user-dom');
const screenView = document.querySelector('.screen-dom');
const rtcCloud = new TRTCCloud();
// 播放 denny 的摄像头画面（我们称之为“主路画面”）
rtcCloud.startRemoteView('denny', cameraView, TRTCVideoStreamType.TRTCVideoStreamTypeBig);
// 播放 denny 的屏幕分享画面（我们称之为“辅路画面”）
rtcCloud.startRemoteView('denny', screenView, TRTCVideoStreamType.TRTCVideoStreamTypeSub);
// 播放 denny 的低分辨率画面（主路画面和低清画面只能二选一）
rtcCloud.startRemoteView('denny', cameraView, TRTCVideoStreamType.TRTCVideoStreamTypeSmall);
// 停止播放 denny 的摄像头画面
rtcCloud.stopRemoteView('denny', TRTCVideoStreamType.TRTCVideoStreamTypeBig);
// 停止播放所有视频画面
rtcCloud.stopAllRemoteView();
```

#### 2. 设置播放参数（setRemoteRenderParams）

通过 setRemoteRenderParams 您可以设置画面的填充模式、旋转角度和镜像模式。
- 填充模式：分为填充或者适应，两种模式下画面都能保持原始的宽高比例，区别在于有无黑边。
- 旋转角度：可以设置 0度、90度、180度 和 270度等四个旋转角度。
- 镜像模式：即画面的左右镜像模式。

```javascript
// 可参考 https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteRenderParams
// 将远端用户 denny 的主路画面设置为填充模式，并开启左右镜像模式
import TRTCCloud, { 
  TRTCRenderParams, TRTCVideoStreamType, TRTCVideoRotation,
  TRTCVideoFillMode, TRTCVideoMirrorType
} from 'trtc-electron-sdk';

const param = new TTRTCRenderParams(
  TRTCVideoRotation.TRTCVideoRotation0,
  TRTCVideoFillMode.TRTCVideoFillMode_Fill,
  TRTCVideoMirrorType.TRTCVideoMirrorType_Enable
);
const rtcCloud = new TRTCCloud();
rtcCloud.setRemoteRenderParams('denny', TRTCVideoStreamType.TRTCVideoStreamTypeBig, param);
```

[](id:step6)
### 步骤6：感知房间中远端用户的音视频状态

在 [步骤4](#step4) 和 [步骤5](#step4) 中，您可以控制对远端用户的声音和视频的播放，但是如果没有足够的信息，您并不知道：
- 当前房间里有哪些用户？
- 他们是否开启了摄像头和麦克风？

为了解决这个问题，您需要监听来自 SDK 的几个事件回调：
- **音频状态变化通知（onUserAudioAvailable）**
当远端用户开启或关闭麦克风时，您可以通过监听 onUserAudioAvailable(userId，boolean) 来感知到这个状态的变化。

- **视频状态变化通知（onUserVideoAvailable）**
当远端用户开启或者关闭摄像头画面时，您可以通过监听 onUserVideoAvailable(userId，boolean) 来感知到这个状态的变化。
当远端用户开启或关闭屏幕分享画面时，您可以通过监听 onUserSubStreamAvailable(userId，boolean) 来感知到这个状态的变化。

- **用户进出房间的通知（onRemoteUserEnter/LeaveRoom）**
当有远端用户进入当前房间时，您可以通过 onRemoteUserEnterRoom(userId) 来感知到该用户的 userId，当有远端用户离开当前方式时，您可以通过 onRemoteUserLeaveRoom(userId, reason) 来感知到该用户的 userId 以及他/她离开的原因。
>! 准确地说，onRemoteUserEnter/LeaveRoom 仅能感知角色（role）为主播（anchor）的用户的进出房间的通知，之所以这样设计，是为了避免当一个房间中观众（audience）在线人数较多时，会因为频繁有人进出房间导致房间中的所有用户被其他用户进出房间的“信令风暴“攻击到。

有了这些事件回调，您就可以掌握房间中有哪些用户，以及他们是否开启了摄像头和麦克风，参考如下的示例代码，在这段示例代码中，我们使用了 mCameraUserList、mMicrophoneUserList 以及 mUserList 分别维护了：
- 房间中的用户（准确的说是主播）是哪些人
- 其中开启摄像头的用户是哪些人
- 其中开启麦克风的用户是哪些人

```javascript
import TRTCCloud from 'trtc-electron-sdk';
let openCameraUserList = [];
let openMicUserList = [];
let roomUserList = [];

function onUserVideoAvailable(userId, available) {
  if (available === 1) {
    openCameraUserList.push(userId);
  } else {
    openCameraUserList = openCameraUserList.filter((item) => item !== userId);
  }
}

function onUserAudioAvailable(userId, available) {
  if (available === 1) {
    openMicUserList.push(userId);
  } else {
    openMicUserList = openMicUserList.filter((item) => item !== userId);
  }
}

function onRemoteUserEnterRoom(userId) {
  roomUserList.push(userId);
}

function onRemoteUserLeaveRoom(userId, reason) {
  roomUserList = roomUserList.filter((item) => item !== userId);
}

const rtcCloud = new TRTCCloud();
rtcCloud.on('onUserVideoAvailable', onUserVideoAvailable);
rtcCloud.on('onUserAudioAvailable', onUserAudioAvailable);
rtcCloud.on('onRemoteUserEnterRoom', onRemoteUserEnterRoom);
rtcCloud.on('onRemoteUserLeaveRoom', onRemoteUserLeaveRoom);
```

## 进阶指引

### 同样是“静音”，区别在哪里？
随着您的业务需求不断深入，您会发现有三种不同的“静音”，虽然他们都叫“静音”，但是技术原理却完全不同：
- **第一种：播放端停止订阅音频流**
如果您调用了 muteRemoteAudio("denny", true) 函数，代表您不希望再播放远端用户 denny 的声音，此时 SDK 会停止拉取 denny 的音频数据流。这种模式是比较节省流量了。但是当您希望再次播放 denny 的声音时，SDK 需要重新启动一次音频数据的拉取流程，所以从“静音”到“解除静音”的状态，恢复速度会比较慢。

- **第二种：将播放音量调整为零**
如果您的业务场景需要静音切换有更快地反应速度，您可以通过 setRemoteAudioVolume("denny", 0) 将远端用户 denny 的播放音量设置为零，该接口由于不涉及网络操作，因此影响速度非常快。

- **第三种：远端用户自己关闭麦克风**
本文档介绍的所有操作都是在介绍播放端的操作，这些操作所产生的效果仅对当前用户生效，比如您通过 muteRemoteAudio("denny", true)  将远端用户 denny 设置为静音，房间中的其他用户还是能听到 denny 的声音。
如果要让 denny 彻底“闭嘴”，就需要去影响 denny 的音频发布行为，我们会在下一篇文档 [发布音视频流](https://cloud.tencent.com/document/product/647/74663) 中详细介绍。
