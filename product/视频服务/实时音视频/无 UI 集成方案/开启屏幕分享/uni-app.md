本文档主要介绍如何使用屏幕分享，目前一个 TRTC 音视频房间只能有一路屏幕分享。

## 调用指引
### 开启屏幕分享
要开启屏幕分享，只需调用 [startScreenCapture()](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startScreenCapture) 接口即可。
通过设置 [startScreenCapture()](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startScreenCapture) 中参数 `encParams` ，您可以指定屏幕分享的编码质量。如果您指定 `encParams` 为 null，SDK 会自动使用之前设定的编码参数，我们推荐的参数设定如下：

| 参数项 | 参数名称 | 常规推荐值 |  文字教学场景 |
|---------|---------|---------|-----|
| 分辨率 | videoResolution | 1280 × 720 | 1920 × 1080 |
| 帧率 | videoFps | 10 FPS | 8 FPS |
| 最高码率 | videoBitrate| 1600 kbps | 2000 kbps |
| 分辨率自适应 | enableAdjustRes | NO | NO |

- 由于屏幕分享的内容一般不会剧烈变动，所以设置较高的 FPS 并不经济，推荐10 FPS即可。
- 如果您要分享的屏幕内容包含大量文字，可以适当提高分辨率和码率设置。
- 最高码率（videoBitrate）是指画面在剧烈变化时的最高输出码率，如果屏幕内容变化较少，实际编码码率会比较低。

```javascript
import TrtcCloud from "@/TrtcCloud/lib/index";
import { TRTCVideoStreamType, TRTCVideoResolution, TRTCVideoResolutionMode } from '@/TrtcCloud/lib/TrtcDefines';
this.trtcCloud = TrtcCloud.createInstance();

const encParams = {
  videoResolution: TRTCVideoResolution.TRTCVideoResolution_640_360,
  videoResolutionMode: TRTCVideoResolutionMode.TRTCVideoResolutionModePortrait,
  videoFps: 15,
  videoBitrate: 900,
  minVideoBitrate: 200,
  enableAdjustRes: false,
};
this.trtcCloud.startScreenCapture(TRTCVideoStreamType.TRTCVideoStreamTypeSub, encParams);  
```
