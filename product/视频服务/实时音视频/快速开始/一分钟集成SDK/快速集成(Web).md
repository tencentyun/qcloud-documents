
本文主要介绍如何快速地将腾讯云 TRTC Web SDK 集成到您的项目中。

## 支持的平台
在 Web 端实现实时音视频通话，需要浏览器完整支持 WebRTC 能力，目前已知支持 WebRTC 的浏览器如下表所示：

| 操作系统平台 | 浏览器/webview | 版本要求 | 备注                                                                                                                        |
|--------------|----------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| iOS          | Safari         | 11.1.2   | 由于苹果 Safari 仍有偶现的 bug，产品化方案建议先规避，待苹果解决后再使用，<br > 因此对于 iOS 推荐使用兼容性更好的小程序解决方案。 |
| Android      | TBS            | 43600    | 微信和手机 QQ 默认内置的浏览器内核为 [TBS](http://x5.tencent.com/)。                                                         |
| Android      | Chrome         | 60+      | 需要支持 H264 编解码。                                                                                                       |
| Mac          | Chrome         | 47+      |  -     |
| Mac          | Safari         | 11+      |    -     |
| Windows(PC)  | Chrome         | 52+      |    -     |
| Windows(PC)  | QQ 浏览器      | 10.2     | -     |

>?基于 TBS 内核的 WebView，需满足版本 ≥ 43600，Web SDK 的 [能力检测](https://cloud.tencent.com/document/product/647/17251#webrtcapi.fn.detectrtc) 中有获取 TBS 版本的方法。
> 可以在浏览器中打开 [WebRTC 能力测试](https://www.qcloudtrtc.com/webrtc-samples/abilitytest/index.html) 页面进行检测是否完整支持 WebRTC。例如公众号等浏览器环境。
> 华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器不支持 H264 编码。

## 集成 TRTC Web SDK
建议采用 CDN 方案集成。

- 该方案直接从腾讯 CDN 上加载 TRTC Web SDK，速度快，稳定性好。
- 您只需要在您的 Web 页面中添加如下代码即可：

```html
<script src="https://sqimg.qq.com/expert_qq/webrtc/3.1.0/WebRTCAPI.min.js"></script>
```

## 更新日志
#### 3.1.0（2019-04-17）
- 修复屏幕分享切换视频流失败问题
- 修复其他已知问题
 
#### 3.0.6（2019-04-08）
- 修复已知问题
  
#### 3.0（2018-09-11）
- 调整初始化接口 [WebRTCAPI](https://cloud.tencent.com/document/product/647/17251#webrtcapi)
- 弃用字段 accountType 
- 弃用字段 closeLocalMedia 默认不再推流
- 弃用字段 video 不再支持配置是否进行音视频推流 
- 弃用字段 audio 不再支持配置是否进行音视频推流
- 弃用成功和失败回调
 
#### 2.6.1（2018-08-16）
- 增加接口 getSpeakerDevices（枚举音频输出设备）
- 增加接口 chooseSpeakerDevice（选择音频输出设备）

#### 2.6 （2018-08-10）
- 新增 SoundMeter 接口
- 新增日志上报的字段
- createRoom 名称改为 enterRoom 

## 常见问题

### 防火墙限制
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请将如下域名和端口加入防火墙的安全白名单中。
域名：`qcloud.rtc.qq.com`

| 协议 | 端口号 |
|:--------|:--------|
| TCP | 8687 |
| UDP | 8000、8800、443 |
