实时音视频（TRTC）支持自定义控制本地画面和远程画面的旋转方向和填充模式。

## 自定义控制本地画面
可以通过调用 [setLocalRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalRenderParams) 设置本地渲染参数。
```javascript
import TRTCCloud, { 
  TRTCRenderParams, TRTCVideoRotation, TRTCVideoFillMode,
  TRTCVideoMirrorType
} from 'trtc-electron-sdk';
const trtcCloud = new TRTCCloud();
const param = new TRTCRenderParams(
  TRTCVideoRotation.TRTCVideoRotation90,
  TRTCVideoFillMode.TRTCVideoFillMode_Fill,
  TRTCVideoMirrorType.TRTCVideoMirrorType_Enable
);

trtcCloud.setLocalRenderParams(param);
const localUserDom = document.querySelector('local-user');
trtcCloud.startLocalPreview(localUserDom);
```

## 自定义控制远程画面画面
可以通过调用 [setRemoteRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteRenderParams) 设置远端渲染参数。
```javascript
import TRTCCloud, { 
  TRTCRenderParams, TRTCVideoRotation, TRTCVideoFillMode,
  TRTCVideoMirrorType, TRTCVideoStreamType
} from 'trtc-electron-sdk';
const trtcCloud = new TRTCCloud();
const param = new TRTCRenderParams(
  TRTCVideoRotation.TRTCVideoRotation180,
  TRTCVideoFillMode.TRTCVideoFillMode_Fill,
  TRTCVideoMirrorType.TRTCVideoMirrorType_Disable
);

const remoteUserId = 'remoteUser';
trtcCloud.setRemoteRenderParams(remoteUserId, TRTCVideoStreamType.TRTCVideoStreamTypeBig, param);
const remoteUserDom = document.querySelector('remote-user');
trtcCloud.startRemoteView(remoteUserId, remoteUserDom, TRTCVideoStreamType.TRTCVideoStreamTypeBig);
```
