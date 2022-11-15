本文档主要介绍主播如何发布自己的音视频流，所谓“发布”，也就是打开麦克风和摄像头，让自己的声音和视频能够被房间中其他用户听到和看到的意思。

![](https://qcloudimg.tencent-cloud.cn/raw/b887b390411aef1396bd593ccdd9eb0e.png)
## 调用指引

[](id:step1)
### 步骤1：完成前序步骤
请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/38549) 完成 SDK 的导入和配置。

[](id:step2)
### 步骤2：打开摄像头预览
您可以调用 **startLocalPreview** 接口打开摄像头预览，此时 SDK 会向系统申请摄像头的使用权限，需要用户授权通过后才会开启摄像头的采集流程。

如果您希望设置本地画面的渲染参数，可以通过调用 **setLocalRenderParams** 接口来设置本地预览的渲染参数。为防止先开启预览再设置预览参数会出现画面跳动，如果您需要设置预览参数，推荐在开启预览之前调用。

```javascript
// 设置本地画面的预览模式：开启左右镜像，设置画面为填充模式
import TRTCCloud, { 
	TRTCRenderParams, TRTCVideoRotation,
	TRTCVideoFillMode, TRTCVideoMirrorType
} from 'trtc-electron-sdk';

const param = new TRTCRenderParams(
	TRTCVideoRotation.TRTCVideoRotation0,
	TRTCVideoFillMode.TRTCVideoFillMode_Fill,
	TRTCVideoMirrorType.TRTCVideoMirrorType_Auto
);
const rtcCloud = new TRTCCloud();
rtcCloud.setLocalRenderParams(param);
const cameraVideoDom = document.querySelector('.camera-dom');
rtcCloud.startLocalPreview(cameraVideoDom);
```

[](id:step3)
### 步骤3：打开麦克风采集
您可以调用 **startLocalAudio** 来开启麦克风采集，该接口需要您通过 `quality` 参数确定采集模式。虽然这个参数的名字叫做 quality，但并不是说质量越高越高，不同的业务场景有最适合的参数选择（这个参数更准确的含义是 scene）。

- **SPEECH**
该模式下的 SDK 音频模块会专注于提炼语音信号，尽最大限度的过滤周围的环境噪音，同时该模式下的音频数据也会获得最好的差质量网络的抵抗能力，因此该模式特别适合于“视频通话”和“在线会议”等侧重于语音沟通的场景。
- **MUSIC**
该模式下的 SDK 会采用很高的音频处理带宽以及立体式模式，在最大限度地提升采集质量的同时也会将音频的 DSP 处理模块调节到最弱的级别，从而最大限度地保证音质。因此该模式适合“音乐直播”场景，尤其适合主播采用专业的声卡进行音乐直播的场景。
- **DEFAULT**
该模式下的 SDK 会启用智能识别算法来识别当前环境，并针对性地选择最佳的处理模式。不过再好的识别算法也总是有不准确的时候，如果您非常清楚自己的产品定位，更推荐您在专注语音通信的 SPEECH 和专注音乐音质的 MUSIC 之间二选一。

```javascript
import { TRTCAudioQuality } from 'trtc-electron-sdk';
// 开启麦克风采集，并设置当前场景为：语音模式（高噪声抑制能力、强弱网络抗性）
rtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualitySpeech);

// 开启麦克风采集，并设置当前场景为：音乐模式（高保真采集、低音质损失，推荐配合专业声卡使用）
rtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualityMusic);
```

[](id:step4)
### 步骤4：进入 TRTC 房间
参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74635) 让当前用户进入 TRTC 房间。一旦进入房间后，SDK 便会开始向房间中的其他用户发布自己的音频流。

>! 当然，您可以在进入房间（enterRoom）后再启动摄像头预览和麦克风采集，不过在直播场景下，我们需要先给主播一个测试麦克风和调整美颜的时间，所以更常见的做法是先启动摄像头和麦克风再进入房间。

```javascript
import { TRTCParams, TRTCRoleType, TRTCAppScene } from 'trtc-electron-sdk';

// 组装 TRTC 进房参数，请将 TRTCParams 中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
const param = new TRTCParams();
params.sdkAppId = 1400000123;  // Please replace with your own SDKAppID
params.userId = "denny";       // Please replace with your own userid  
params.roomId = 123321;        // Please replace with your own room number
params.userSig = "xxx";        // Please replace with your own userSig
params.role = TRTCRoleType.TRTCRoleAnchor;

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
rtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneLIVE);
```

