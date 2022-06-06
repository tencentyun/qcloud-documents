本文档主要介绍如何订阅房间中其他用户的音视频流，也就是如何播放其他用户的音频和视频。为了方便起见，我们在接下来的文档中，会将“房间中的其他用户”统称为“远端用户”。

## 调用指引

[](id:step1)
### 步骤1：完成前序步骤
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/73371) 完成 SDK 的导入和 App 权限的配置。

[](id:step2)
### 步骤2：进入 TRTC 房间
参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74638) 让当前用户进入 TRTC 房间，只有在成功进入房间之后才能订阅其他用户的音视频流。

[](id:step3)
### 步骤3：音频流的播放

```javascript
import TrtcCloud from '@/TrtcCloud/lib/index';
import { TRTCAudioQuality } from '@/TrtcCloud/lib/TrtcDefines';

this.trtcCloud = TrtcCloud.createInstance();
this.trtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualityDefault);
```

[](id:step4)
### 步骤4：视频流的播放

#### 开始和停止播放（startRemoteView + stopRemoteView）
您可以通过调用接口 startRemoteView 来播放远端用户的视频画面，但前提是您需要传递给 SDK 一个 view 对象，用来作为承载该用户的视频画面的渲染控件。

startRemoteView 的第一个参数是远端用户的 userId，第二个参数是远端用户的流类型，第三个参数则是您需要传递的 view 对象。其中第二个参数 streamType(流类型) 有三个可选的值，分别是：
- TRTCVideoStreamTypeBig：用户的主路画面，一般用来传输用户摄像头的画面。
- TRTCVideoStreamTypeSub：用户的辅路画面，一般用来传输用户屏幕分享的画面。
- TRTCVideoStreamTypeSmall：用户的低清小画面，这是相对于主路画面而言的，只有当远端用户开启了“双路编码（enableEncSmallVideoStream）”之后，我们才能播放他/她的低清画面。并且同时只能在主路画面和低清小画面中二选一。

通过调用 stopRemoteView 接口，您可以停止播放某一个远端用户的视频。

```javascript
import { TRTCVideoStreamType } from '@/TrtcCloud/lib/TrtcDefines';
// 播放 denny 的摄像头画面（我们称之为“主路画面”）
this.trtcCloud.startRemoteView(userId, TRTCVideoStreamType.TRTCVideoStreamTypeBig, viewId);
// 停止播放 denny 的摄像头画面
this.trtcCloud.stopRemoteView(remoteUserId, TRTCVideoStreamType.TRTCVideoStreamTypeBig);
```

[](id:step5)
### 步骤5：感知房间中远端用户的音视频状态

在 [步骤4](#step3) 和 [步骤5](#step4) 中，您可以控制对远端用户的声音和视频的播放，但是如果没有足够的信息，您并不知道：
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

```javascript
// 感知远端用户视频状态的变化
public void onUserVideoAvailable(String userId, boolean available) {
  // ……
}
// 感知远端用户音频状态的变化
public void onUserAudioAvailable(String userId, boolean available) {
  // ……
}
// 感知远端用户进入房间的通知
public void onRemoteUserEnterRoom(String userId) {
  // ……
}
// 感知远端用户离开房间的通知
public void onRemoteUserLeaveRoom(String userId，int reason) {
  // ……
}
```
