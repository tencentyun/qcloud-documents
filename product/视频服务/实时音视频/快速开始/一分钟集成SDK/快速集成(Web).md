## 支持的平台

| 操作系统平台  | 浏览器/webview  | 版本要求  |  备注|
| ------------------------- | -------- | ---------------------- |------- |
| iOS          | Safari ( 只支持Safari ) | 11.1.2 | 由于苹果 Safari 仍有偶现的 bug，产品化方案建议先规避，待苹果解决后再使用<br > 因此，对于 iOS 推荐使用兼容性更好的小程序解决方案 |
| Android      | TBS （微信和手机QQ的默认Webview） | 43600                | 微信和手机QQ默认内置的浏览器内核为TBS。 [TBS 介绍](http://x5.tencent.com/) |
| Android      | Chrome | 60+               | 需要支持 H264  |
| Mac          | Chrome | 47+                |      |
| Mac          | Safari | 11+                |      |
| Windows(PC)  | Chrome | 52+                |      |
| Windows(PC)  | [QQ浏览器](https://browser.qq.com/) | 10.2 | &nbsp;     |


> 基于 TBS 内核的 webview，需满足版本 >= 43600，我们的[ 能力检测 ](/document/product/647/17251#webrtcapi.fn.detectrtc) 中有获取 TBS 版本的方法。

## 集成 TRTC Web SDK
### NPM 方案
TO-DO

### CDN 方案
- 该方案直接从腾讯 CDN 上加载 TRTC Web SDK，速度快，稳定性好。
- 您只需要在您的 Web 页面中添加如下代码即可：

```html
<script src="https://sqimg.qq.com/expert_qq/webrtc/3.0/WebRTCAPI.min.js"></script>
```

## 更新日志

#### 3.0（ 2018-09-11 ）
- 调整初始化接口 [WebRTCAPI](/document/product/647/17251#webrtcapi) 
- 弃用字段 accountType 
- 弃用字段 closeLocalMedia 默认不再推流
- 弃用字段 video 不再支持配置是否进行音视频推流 
- 弃用字段 audio 不再支持配置是否进行音视频推流
- 弃用成功和失败回调
 
#### 2.6.1（ 2018-08-16 ）
- 增加接口 getSpeakerDevices（枚举音频输出设备）
- 增加接口chooseSpeakerDevice（选择音频输出设备）

#### 2.6 （ 2018-08-10）
- 新增SoundMeter接口
- 新增日志上报的字段
- createRoom 名称改为 enterRoom 

## 常见问题

### 1. 防火墙限制
由于 WebRTC 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请联系贵司的网络管理员，将如下端口加入防火墙的安全白名单中。

| 协议      | 端口号                                   |
| ------- | ---------------------------------------- |
| TCP | 8687 |
| UDP  | 8000 、 8800 、 443 |