## 腾讯云 WEB 视频播放器介绍

腾讯云针对不同的业务场景和使用场景，提供了不同的 WEB 视频播放器，分别为：
[点播超级播放器](https://cloud.tencent.com/document/product/266/14424)
[直播播放器1.0](https://cloud.tencent.com/document/product/267/5704)
[TCPlayer Lite](https://cloud.tencent.com/document/product/267/7479)
[点播播放器1.0](https://cloud.tencent.com/document/product/267/5706)
下面将对这些播放器进行简要介绍

### 点播超级播放器
点播超级播放器是基于 video.js 框架并结合腾讯云点播业务而开发的视频播放器，采用以 HTML5 `<video>`为主 Flash 为辅的播放方式，在浏览器不支持HTML5 `<video>`的情况下采用 Flash 播放。播放器界面由 HTML CSS 实现，可以通过 CSS 定制界面。
该播放器只适用于使用腾讯云点播业务的 WEB 点播视频播放场景，并且会持续进行功能迭代更新。 
具体介绍请看[使用文档](https://cloud.tencent.com/document/product/266/14424)、[开发文档](https://cloud.tencent.com/document/product/266/14603)

### 直播播放器1.0

直播播放器1.0是结合腾讯云直播业务而开发的视频播放器，以 Flash 为主要播放模式，需要浏览器支持并启用 Flash 插件。
该播放器只适用于使用腾讯云直播业务的 WEB 直播视频播放场景。
具体介绍请看[使用文档](https://cloud.tencent.com/document/product/267/5704)

### TCPlayer Lite

独立播放器 TCPlayer Lite 实现了基本的视频播放器功能，采用 HTML5 和 Flash 相结合的播放模式，支持播放 hls、mp4 格式的点播视频和 RTMP、http-flv、hls 协议的直播视频，支持主要的桌面和移动端浏览器。
该播放器仅支持传入地址播放，不关联业务，适用于轻量化 WEB 视频播放场景，支持点播和直播，支持通过 CSS 定制化界面。
具体介绍请看[使用文档](https://cloud.tencent.com/document/product/267/7479)

### 点播播放器1.0

点播播放器1.0是结合腾讯云点播业务而开发的视频播放器，以 Flash 为主要播放模式，需要浏览器支持并启用 Flash 插件。该播放器主要面向比较老旧的浏览器，比如IE8、9、10、11等。
由于 Flash 逐步被现代浏览器禁止运行，并且　Flash 将于2020年停止开发和更新，腾讯云点播推出了以 HTML5 播放为主的点播超级播放器方案，进行替换点播播放器1.0。
点播播放器1.0具体介绍请看[使用文档](https://cloud.tencent.com/document/product/267/5706)

## 如何选择播放器

通过以上对各个播放器的介绍，了解每种播放器的特点以及适用场景，建议结合所使用的腾讯云业务，以及自身所具备的开发能力来选择合适的 WEB 播放器。
如遇到播放问题，请查看[常见问题文档](https://cloud.tencent.com/document/product/266/1303)

>**备注：**
> * WEB 播放器是集成到网页里，并运行在浏览器里的播放器，与运行在终端系统（ Android\iOS ）里的播放器 SDK 不同。
