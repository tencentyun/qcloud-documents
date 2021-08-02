快直播（LEB）是标准直播在超低延迟播放场景下的延伸，比传统直播协议延迟更低，为观众提供毫秒级的极致**直播观看**体验。

> ! 由于快直播使用的是 WebRTC 协议的低延迟特性，默认不支持 B 帧且音频编解码方式为 opus 编解码。为了保证快直播流可播放，当推流时带 B 帧或音频编码非 opus 编码时，云直播后台会自动发起转码去B帧并转码为 opus 编码，从而产生 [标准转码费用](https://cloud.tencent.com/document/product/267/39889)。



[](id:app)

## App 接入

iOS、Android 上的应用可以通过集成移动直播 SDK 来实现 App 端上的直播推流/播放功能。

- **App 端直播推流**：支持采集摄像头画面或者采集手机界面，通过 RTMP 协议快速推流到云直播服务上，详情请参见 [摄像头推流](https://cloud.tencent.com/document/product/454/56591) 和 [录屏推流](https://cloud.tencent.com/document/product/454/56594)。
- **App 端直播播放**：支持 WebRTC 播放协议，配合快直播服务快速打造低延迟直播体验，详情请参见 [快直播拉流](https://cloud.tencent.com/document/product/454/55880)。

>? 移动直播 SDK 借助云直播、即时通信 IM、TRTC 等服务实现了多人音视频低延迟互联互通，可以实现多人连麦的互动效果，不参与连麦的观众仍通过直播服务观看，详情请参见 [直播连麦互动](https://cloud.tencent.com/document/product/454/52751)。



[](id:web)

## Web 接入

若您有网站需要进行直播推流和播放，推荐您使用以下方式进行接入：

- **Web 端直播推流**：基于浏览器通用的 WebRTC 标准进行设计和封装，通过引入代码片段就能实现在浏览器中进行直播推流，详情请参见 [WebRTC 推流](https://cloud.tencent.com/document/product/267/56505)。
> ! WebRTC 推流时音频编码方式为 opus 编码，若使用标准直播的播放协议（RTMP、FLV、HLS）进行播放时，为保证能正常观看，云直播后台会自动发起音频转码转为 aac 编码，从而会产生音频转码费用，详情请参见[音频转码费用说明](https://cloud.tencent.com/document/product/267/39889#a_trans)。（若只使用快直播则不会发起音频转码）
- **Web 端直播播放**：推荐您选用播放器 SDK 的[TCPlayerLite](https://cloud.tencent.com/document/product/454/7503) ，支持在手机浏览器和 PC 浏览器上播放**快直播 WebRTC 协议**直播流，相比传统的直播协议延迟更低，为观众提供毫秒级的极致直播观看体验。
> ! 在不支持 WebRTC 的浏览器环境，传入播放器的 WebRTC 地址会自动进行协议转换来更好的支持媒体播放，在移动端浏览器会默认转换为 HLS，PC 端浏览器默认转换为 FLV。
