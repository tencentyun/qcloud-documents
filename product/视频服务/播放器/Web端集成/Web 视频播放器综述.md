## 简介
腾讯云针对不同的业务场景和使用场景，提供了不同的 Web 视频播放器，分别为：
- [点播超级播放器](https://cloud.tencent.com/document/product/266/14424)
- [TCPlayer Lite](https://cloud.tencent.com/document/product/881/20207)

### 点播超级播放器

点播超级播放器是基于 video.js 框架并结合腾讯云点播业务而开发的视频播放器，采用以 HTML5`<video>`为主，Flash 为辅的播放方式，在浏览器不支持 HTML5`<video>`的情况下采用 Flash 播放。播放器界面由 HTML CSS 实现，可以通过 CSS 定制界面。

该播放器只适用于使用云点播业务的 Web 点播视频播放场景，并且会持续进行功能迭代更新。 
具体介绍请参阅 [使用文档](https://cloud.tencent.com/document/product/266/14424)、[开发文档](https://cloud.tencent.com/document/product/266/14603)。

### TCPlayer Lite

独立播放器 TCPlayer Lite 实现了基本的视频播放器功能，采用 HTML5 和 Flash 相结合的播放模式，支持播放 HLS、MP4 格式的点播视频和 RTMP、HTTP-FLV、HLS 协议的直播视频，支持主要的桌面和移动端浏览器。

该播放器仅支持传入地址播放，不关联业务，适用于轻量化 Web 视频播放场景，支持点播和直播，支持通过 CSS 定制化界面。
具体介绍请参阅 [使用文档](https://cloud.tencent.com/document/product/881/20207)。

## 如何选择播放器

通过以上对各个播放器的介绍，了解每种播放器的特点以及适用场景，结合所使用的腾讯云业务，以及自身所具备的开发能力来选择合适的 Web 播放器。

如遇到播放问题，请查看 [常见问题文档](https://cloud.tencent.com/document/product/881/20219)

>? Web 播放器是集成到网页里，并运行在浏览器里的播放器，与运行在终端系统（ Android/iOS）里的播放器 SDK 不同。
