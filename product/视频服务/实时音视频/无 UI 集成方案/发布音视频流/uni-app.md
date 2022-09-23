本文档主要介绍主播如何发布自己的音视频流，所谓“发布”，也就是打开麦克风和摄像头，让自己的声音和视频能够被房间中其他用户听到和看到的意思。

## 调用指引

[](id:step1)
### 步骤1：完成前序步骤

请参考文档 [导入 SDK 到项目中](https://cloud.tencent.com/document/product/647/73371) 完成 SDK 的导入和 App 权限的配置。

[](id:step2)
### 步骤2：打开摄像头预览
您可以调用 [**startLocalPreview**](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startLocalPreview) 接口打开摄像头预览。

如果您希望设置本地画面的渲染参数，可以通过调用 [**setLocalRenderParams**](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setLocalRenderParams) 接口来设置本地预览的渲染参数。为防止先开启预览再设置预览参数会出现画面跳动，如果您需要设置预览参数，推荐在开启预览之前调用。

```javascript
import TrtcCloud from '@/TrtcCloud/lib/index';
this.trtcCloud = TrtcCloud.createInstance();

// 设置本地画面的预览模式
const isFrontCamera = true; // front or back camera
const userId = 'denny';    // view id
this.trtcCloud.startLocalPreview(isFrontCamera, userId);
```


[](id:step3)
### 步骤3：打开麦克风采集
您可以调用 [**startLocalAudio**](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startLocalAudio) 来开启麦克风采集，该接口需要您通过 `quality` 参数确定采集模式。虽然这个参数的名字叫做 `quality`，但并不是说质量越高越高，不同的业务场景有最适合的参数选择（这个参数更准确的含义是 scene）。

```javascript
// 开启麦克风采集，并设置当前场景为：语音模式（高噪声抑制能力、强弱网络抗性）
import TrtcCloud from '@/TrtcCloud/lib/index';
import { TRTCAudioQuality } from '@/TrtcCloud/lib/TrtcDefines';
this.trtcCloud = TrtcCloud.createInstance();
this.trtcCloud.startLocalAudio(TRTCAudioQuality.TRTCAudioQualityDefault);
```


[](id:step4)
### 步骤4：进入 TRTC 房间

参考文档 [进入房间](https://cloud.tencent.com/document/product/647/74638) 让当前用户进入 TRTC 房间。一旦进入房间后，SDK 便会开始向房间中的其他用户发布自己的音频流。

>! 当然，您可以在进入房间（[enterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom)）后再启动摄像头预览和麦克风采集，不过在直播场景下，我们需要先给主播一个测试麦克风和调整美颜的时间，所以更常见的做法是先启动摄像头和麦克风再进入房间。

```javascript
import TrtcCloud from '@/TrtcCloud/lib/index';
import { TRTCAppScene, TRTCVideoStreamType, TRTCRoleType } from '@/TrtcCloud/lib/TrtcDefines';
this.trtcCloud = TrtcCloud.createInstance();

// 组装 TRTC 进房参数，请将参数中的各字段都替换成您自己的参数
// Please replace each field in TRTCParams with your own parameters
const params = {
  sdkAppId: 1400000123;  // Please replace with your own sdkAppId
  userId: "denny";       // Please replace with your own userId
  roomId: 123321;       // Please replace with your own room number 
  userSig: "xxx";       // Please replace with your own userSig
  role: TRTCRoleType.TRTCRoleAnchor;
};

// 如果您的场景是“在线直播”，请将应用场景设置为 TRTC_APP_SCENE_LIVE
// If your application scenario is a video call between several people, please use "TRTC_APP_SCENE_LIVE"
this.trtcCloud.enterRoom(params, TRTCAppScene.TRTCAppSceneVideoCall);        
```
