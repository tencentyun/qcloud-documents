>?
>- TCPlayerLite 为旧版播放器，后续将持续维护，但不再主动做功能迭代，后续 Web 端播放器功能迭代将在 [超级播放器 TCPlayer](https://cloud.tencent.com/document/product/881/30818) 内进行。
>- 当前 [超级播放器 TCPlayer](https://cloud.tencent.com/document/product/881/30818) 已包含旧版播放器 TCPlayerLite 的全部能力，同时具备更多丰富功能。若您首次使用腾讯云 Web 播放器，建议您直接使用超级播放器 TCPlayer。若您当前仍在使用 TCPlayerLite，建议您尽早升级为超级播放器 TCPlayer，以享受更多更全面的功能及服务。TCPlayerLite 升级为 TCPlayer 方式可参见 [TCPlayerLite 升级指引](https://cloud.tencent.com/document/product/881/72744)。

## 功能介绍

腾讯云 Web 超级播放器 TCPlayerLite 是为了解决在手机浏览器和 PC 浏览器上播放音视频流的问题，它使您的视频内容可以不依赖用户安装 App，就能在朋友圈和微博等社交平台进行传播。本文档适合有一定 Javascript 语言基础的开发人员阅读。
以下视频将为您讲解腾讯云播放器 SDK 的 Web 播放器的功能特性以及对接攻略：
<div class="doc-video-mod"><iframe src="  https://cloud.tencent.com/edu/learning/quick-play/2496-42186?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 基础知识
对接前需要了解如下基础知识：

- **直播和点播**
直播视频源是实时的，一旦主播停播，直播地址就失去意义，而且由于是实时直播，所以播放器在播直播视频的时候是没有进度条的。
点播视频源是某个服务器上的文件，只要文件没有被提供方删除，就可以随时播放， 而且由于整个视频都在服务器上，所以播放器在播点播视频的时候是有进度条的。

- **协议支持**
TCPlayerLite 的视频播放能力本身不是网页代码实现的，而是靠浏览器支持，所以其兼容性不像我们想象的那么好，因此，**不是所有的手机浏览器都能有符合预期的表现**。一般用于网页直播的视频源地址是以 M3U8 结尾的地址，我们称其为 HLS (HTTP Live Streaming)，这是苹果推出的标准，目前各种手机浏览器产品对这种格式的兼容性也最好，但它有个问题：延迟比较大，一般是20s - 30s左右的延迟。

视频协议|用途|URL 地址格式|PC 浏览器|移动浏览器
-----------|-----|-------------|-------------|----------------
WebRTC|只适用直播|`webrtc://xxx.liveplay.myqcloud.com/live/xxx`|支持|支持 
HLS（M3U8）|可用于直播|`http://xxx.liveplay.myqcloud.com/xxx.m3u8`|支持|支持
HLS（M3U8）|可用于点播|`http://xxx.vod.myqcloud.com/xxx.m3u8`|支持|支持
FLV|可用于直播|`http://xxx.liveplay.myqcloud.com/xxx.flv`|支持|不支持
FLV|可用于点播|`http://xxx.vod.myqcloud.com/xxx.flv`|支持|不支持
MP4|只适用点播|`http://xxx.vod.myqcloud.com/xxx.mp4`|支持|支持

 
>!
> - 在不支持 WebRTC 的浏览器环境，传入播放器的 WebRTC 地址会自动进行协议转换来更好的支持媒体播放，默认在移动端转换为 HLS，PC 端转换为 FLV。

**功能支持**

|功能\浏览器|Chrome|Firefox|Edge|QQ 浏览器|Mac Safari|iOS Safari|iOS 微信 QQ|Android Chrome|Android 微信、QQ|手机 QQ 浏览器|IE 8,9,10,11|
|---|---|---|---|---|---|---|---|---|---|---|---|
|设置封面|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|
|多清晰度支持|&#10003;|&#10003;|&#10003;|&#10003;|×|×|×|×|×|×|&#10003;|
|定制错误提示语|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|×|×|×|×|×|&#10003;|
|快直播|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|&#10003;|×|


## 对接攻略

### Step1. 页面准备工作
在需要播放视频的页面（PC 或 H5）中引入初始化脚本。
```
<script src="https://web.sdk.qcloud.com/player/tcplayerlite/release/v2.4.5/TcPlayer-2.4.5.js" charset="utf-8"></script>;
```

建议在使用播放器 SDK 的时候自行部署资源，[单击下载播放器资源](https://web.sdk.qcloud.com/player/tcplayerlite/release/v2.4.5/TcPlayer-2.4.5.zip)。

如果您部署的地址为 `aaa.xxx.ccc`，在合适的地方引入播放器脚本文件：
```
<script src="aaa.xxx.ccc/TcPlayer-x.x.x.js"></script>
```

>! 直接用本地网页无法调试，Web 播放器无法处理该情况下的跨域问题。

### Step2. 在 HTML 中放置容器

在需要展示播放器的页面位置加入播放器容器，即放一个 div 并命名，例如 `id_test_video`，视频画面都会在容器里渲染。对于容器的大小控制，您可以使用 div 的属性进行控制，示例代码如下：

```
<div id="id_test_video" style="width:100%; height:auto;"></div>
```

### Step3. 对接视频播放
编写 Javascript 代码，作用是去指定的 URL 地址拉取音视频流，并将视频画面呈现到添加的容器内。

#### 3.1 简单播放
如下是一个 [直播格式的 URL 地址](https://cloud.tencent.com/document/product/267/32733)，使用 HLS（M3U8）协议，如果主播在直播中，则用 VLC 等播放器是可以直接打开该 URL 进行观看的：

```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8      // m3u8 播放地址
```
![](https://main.qcloudimg.com/raw/f5444cbd256ace4033e37bb1206bc90d.png)
如果要在手机浏览器上播放该 URL 的视频，则 Javascript 代码如下：
<dx-codeblock>
::: javascript javascript
var player = new TcPlayer('id_test_video', {
     "m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8", //请替换成实际可用的播放地址
     "autoplay" : true,      //iOS 下 safari 浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
     "poster" : "http://www.test.com/myimage.jpg",
     "width" :  '480',//视频的显示宽度，请尽量使用视频分辨率宽度
     "height" : '320'//视频的显示高度，请尽量使用视频分辨率高度
});
:::
</dx-codeblock>

这段代码可以支持在 PC 及手机浏览器上播放 HLS（M3U8）协议的直播视频，虽然 HLS（M3U8）协议的视频兼容性不错，但部分 Android 手机依然不支持，其延迟较高，大约20秒以上的延迟。

#### 3.2 实现更低延迟
<dx-codeblock>
::: javascript javascript
var player =  new TcPlayer('id_test_video', {
     "m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
     "flv": "http://2157.liveplay.myqcloud.com/live/2157_358535a.flv", //增加了一个 flv 的播放地址，用于PC平台的播放 请替换成实际可用的播放地址
     "autoplay" : true,      //iOS 下 safari 浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
     "poster" : "http://www.test.com/myimage.jpg",
     "width" :  '480',//视频的显示宽度，请尽量使用视频分辨率宽度
     "height" : '320'//视频的显示高度，请尽量使用视频分辨率高度
});
:::
</dx-codeblock>
这段代码中增加了 FLV 的播放地址，Web 播放器如果发现当前的浏览器是 PC 浏览器，会主动选择 FLV 链路，从而实现更低的延迟。如果对延迟有更高的要求，可以使用 WebRTC 拉流地址，基于 WebRTC 的播放系统可以实现超低延迟（500ms），前提条件是拉流地址都是可以出流的，如果您使用腾讯云的视频直播服务，则无需考虑，因为腾讯云的直播频道默认支持 WebRTC、FLV 和 HLS（M3U8）播放协议。

#### 无法播放怎么办？
如果您发现视频无法播放，可能存在如下原因：
-  **原因一：视频源有问题**
如果是直播 URL，则需要检查主播是否已经停止推流，可以用浮窗提示观众：“主播已经离开”。请参见 [直播推流](https://cloud.tencent.com/document/product/267/32732)。
如果是点播 URL，则需要检查要播放的文件是否还存在于服务器上（如播放地址是否已经从点播系统移除）。
- **原因二：本地网页调试**
目前 TCPlayerLite 不支持本地网页调试（即通过`file://`协议打开视频播放的网页），因为浏览器有跨域安全限制，所以在 Windows 系统上放置一个 test.html 文件来进行测试是无法播放的，需要将其上传到服务器上进行测试。而前端工程师可以通过反向代理的方式，对线上页面进行本地代理以实现本地调试，这是主流的本地调试方法。

- **原因三：手机兼容问题**
普通的手机浏览器只支持 HLS（M3U8) 协议的播放，不支持 FLV ，最新版本的 QQ 浏览器支持 FLV 协议的播放。

### Step4. 给播放器设置封面
设置封面涉及到 poster 属性，下面将详细介绍 poster 属性的使用方法。
>!封面功能在部分移动端播放环境下可能失效，通常是由于移动端 webview 劫持视频播放造成的，需要 webview 支持 video 叠加元素或者放开劫持视频播放。相关详细说明请参见 [常见问题](https://cloud.tencent.com/document/product/881/20219#.E6.B5.8F.E8.A7.88.E5.99.A8.E5.8A.AB.E6.8C.81.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE)。

#### 4.1 简单设置封面
poster 支持传入图片地址作为播放器的封面，在播放器区域内居中，并且以图片的实际分辨率进行显示。

```
"poster" : "http://www.test.com/myimage.jpg"
```
#### 4.2 设置封面样式
poster 支持传入一个对象，在对象中可以对封面的展现样式（style）和图片地址（src）进行设置。

style 支持的样式如下：
- default：居中并且以图片的实际分辨率进行显示。
- stretch：拉伸铺满播放器区域，图片可能会变形。
- cover：优先横向等比拉伸铺满播放器区域，图片某些部分可能无法显示在区域内。

```
"poster" : {"style":"stretch", "src":"http://www.test.com/myimage.jpg"}
```
#### 4.3 实现用例

使用 cover 方式显示封面。线上示例如下，在 PC 浏览器中右键单击**查看页面源码**即可查看页面的代码实现：
[视频封面](https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer-poster.html)
>!
>- 在某些移动端设置封面会无效，具体说明请参见 [常见问题](https://cloud.tencent.com/document/product/881/20219)。
>- 以上示例链接仅用于文档演示，请勿用于生产环境。

### Step5. 多清晰度支持
#### 5.1 原理介绍
同腾讯视频，Web 播放器支持多清晰度，如下图所示：
![](https://main.qcloudimg.com/raw/281af6b6d9b75969eed7004722b27c9b.png)
**播放器本身是没有能力去改变视频清晰度的**，视频源只有一种清晰度，称之为原画，而原画视频的编码格式和封装格式多种，Web 端无法支持播放所有的视频格式，如点播支持以 H.264 为视频编码，MP4 和 FLV 为封装格式的视频。

**多清晰度的实现依赖于视频云**：
- 对于直播，来自主播端的原始视频会在腾讯云进行实时转码，分出多路转码后的视频，每一路视频都有其对应的地址，例如“高清-HD”和“标清-SD”，地址格式如下：
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          // 原画
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      // 高清
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      // 标清
```

- 对于点播，一个视频文件上传到腾讯云后，您可以对该视频文件进行转码，产生其它几种清晰度的视频，例如“高清-HD”和“标清-SD”，地址格式如下：
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8         // 原画，用转码后的超清替换
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      // 高清
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      // 标清
```
>!上传后的原始视频是未经过腾讯云转码的，不能直接用于播放。

#### 5.2 代码实现
多清晰度支持的代码实现如下所示：
<dx-codeblock>
::: javascript javascript
var player = new TcPlayer('id_test_video', {
     "m3u8"      : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8",//请替换成实际可用的播放地址
     "m3u8_hd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
     "m3u8_sd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
     "autoplay"  : true,      //iOS 下 safari 浏览器，以及大部分移动端浏览器是不开放视频自动播放这个能力的
     "poster"  : "http://www.test.com/myimage.jpg",
});
:::
</dx-codeblock>


#### 5.3 实现用例
使用多种分辨率的设置及切换功能。线上示例如下，在 PC 浏览器中右键单击**查看页面源码**即可查看页面的代码实现：[分辨率切换](https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer-clarity.html)
正常情况将看到如下效果：
![](https://main.qcloudimg.com/raw/99c05e75f0d417df33942d18dad2f509.jpg)
>!
> - PC 端现已支持多种清晰度播放及切换的功能，移动端尚未支持。
 >- 以上示例链接仅用于文档演示，请勿用于生产环境

### Step6. 定制错误提示语
Web 播放器支持提示语定制。

#### 6.1 代码实现
如下是让播放器支持自定义提示语的核心代码，主要在 wording 属性上设置提示语。
<dx-codeblock>
::: javascript javascript
var player = new TcPlayer('id_test_video', {
     "m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//请替换成实际可用的播放地址
     "autoplay" : true,      //iOS 下 safari 浏览器是不开放这个能力的
     "poster" : "http://www.test.com/myimage.jpg",
     "wording": {
               2032: "请求视频失败，请检查网络",
               2048: "请求m3u8文件失败，可能是网络错误或者跨域问题"
     }
});
:::
</dx-codeblock>

#### 6.2 实现用例
视频播放失败，同时使用自定义提示文案的功能。线上示例如下，在 PC 浏览器中右键单击**查看页面源码**即可查看页面的代码实现：

```
https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer-error.html
```
>!以上示例链接仅用于文档演示，请勿用于生产环境。

#### 6.3 错误码表
| Code  | 提示语|说明                                       |
|-------|-----------|---------------------------------------|
| 1      | 网络错误，请检查网络配置或者播放链接是否正确。 | H5 提示的错误。       |
| 2     | 网络错误，请检查网络配置或者播放链接是否正确。 | 视频格式 Web 播放器无法解码。<br>H5 提示的错误。          |
| 3     | 视频解码错误。 |  H5 提示的错误。      |
| 4       | 当前系统环境不支持播放该视频格式。 |         H5 提示的错误。      |
| 5       | 当前系统环境不支持播放该视频格式。 |  播放器判断当前浏览器环境不支持播放传入的视频，可能是当前浏览器不支持 MSE 。 |
| 10  | 请勿在 file 协议下使用播放器，可能会导致视频无法播放。| -  |
| 11  | 使用参数有误，请检查播放器调用代码。|  - |
| 12  | 请填写视频播放地址。|  - |
| 2001 | 调用 WebRTC 接口失败 | 播放 WebRTC 时设置 sdp 失败提示的错误 |
| 2002 | 调用拉流接口失败 | 播放 WebRTC 时调用拉流接口失败提示的错误 |
| 2003 | 连接服务器失败，并且连接重试次数已超过设定值 | 播放 WebRTC 时提示的错误，可用于确定是否为停止推流状态 |

>?
>- Code 1 - 4 对应的是 H5 原生事件。
>- 由于 H5 视频播放标准的不确定性，错误提示语会不定期更新。

## 源码参考
如下是一个线上示例代码，在 PC 浏览器中右键单击**查看页面源码**即可查看页面的代码实现：[播放示例](https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer.html)
>!以上示例链接仅用于文档演示，请勿用于生产环境。

## 参数列表
播放器支持的所有参数，如下所示：

<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>默认值</th>
<th>参数说明</th>
</tr>
</thead>
<tbody><tr>
<td>webrtc</td>
<td>String</td>
<td>无</td>
<td>原画 WebRTC 播放 URL。 <br> 示例： <code>webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1</code></td>
</tr>
<tr>
<td>webrtc_hd</td>
<td>String</td>
<td>无</td>
<td>高清 WebRTC 播放 URL。 <br> 示例： <code>webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1_hd</code></td>
</tr>
<tr>
<td>webrtc_sd</td>
<td>String</td>
<td>无</td>
<td>标清 WebRTC 播放 URL。 <br> 示例： <code>webrtc://5664.liveplay.myqcloud.com/live/5664_harchar1_sd</code></td>
</tr>
<tr>
<td>m3u8</td>
<td>String</td>
<td>无</td>
<td>原画 M3U8 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535a.m3u8</code></td>
</tr>
<tr>
<td>m3u8_hd</td>
<td>String</td>
<td>无</td>
<td>高清 M3U8 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8</code></td>
</tr>
<tr>
<td>m3u8_sd</td>
<td>String</td>
<td>无</td>
<td>标清 M3U8 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8</code></td>
</tr>
<tr>
<td>flv</td>
<td>String</td>
<td>无</td>
<td>原画 FLV 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535a.flv</code></td>
</tr>
<tr>
<td>flv_hd</td>
<td>String</td>
<td>无</td>
<td>高清 FLV 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535ahd.flv</code></td>
</tr>
<tr>
<td>flv_sd</td>
<td>String</td>
<td>无</td>
<td>标清 FLV 播放 URL。  <br> 示例：<code>http://2157.liveplay.myqcloud.com/2157_358535asd.flv</code></td>
</tr>
<tr>
<td>mp4</td>
<td>String</td>
<td>无</td>
<td>原画 MP4 播放 URL。  <br> 示例：<code>http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4</code></td>
</tr>
<tr>
<td>mp4_hd</td>
<td>String</td>
<td>无</td>
<td>高清 MP4 播放 URL。  <br> 示例：<code>http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4</code></td>
</tr>
<tr>
<td>mp4_sd</td>
<td>String</td>
<td>无</td>
<td>标清 MP4 播放 URL。  <br> 示例：<code>http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4</code></td>
</tr>
<tr>
<td>width</td>
<td>Number</td>
<td>无</td>
<td><strong>必选</strong>，设置播放器宽度，单位为像素。   <br> 示例：640</td>
</tr>
<tr>
<td>height</td>
<td>Number</td>
<td>无</td>
<td><strong>必选</strong>，设置播放器高度，单位为像素。   <br> 示例：480</td>
</tr>
<tr>
<td>volume</td>
<td>Number</td>
<td>0.5</td>
<td>设置初始音量，范围：0到1 [v2.2.0+]。    <br> 示例：0.6</td>
</tr>
<tr>
<td>live</td>
<td>Boolean</td>
<td>false</td>
<td><strong>必选</strong>，设置视频是否为直播类型，将决定是否渲染时间轴等控件，以及区分点直播的处理逻辑。  <br> 示例：true</td>
</tr>
<tr>
<td>autoplay</td>
<td>Boolean</td>
<td>false</td>
<td>是否自动播放。<br>（<strong>备注：该选项只对大部分 PC 平台生效</strong>）  <br> 示例：true</td>
</tr>
<tr>
<td>poster</td>
<td>String / Object</td>
<td>无</td>
<td>预览封面，可以传入一个图片地址或者一个包含图片地址 src 和显示样式 style 的对象。style 可选属性：<ul style="margin:0"><li>default 居中1：1显示。 <br></li><li>stretch 拉伸铺满播放器区域，图片可能会变形。</li><li>cover 优先横向等比拉伸铺满播放器区域，图片某些部分可能无法显示在区域内。</ul>示例： "<code>http://www.test.com/myimage.jpg</code>" 或者<br>{"style": "cover", "src": <code>http://www.test.com/myimage.jpg</code>}  [v2.3.0+]</li></td>
</tr>
<tr>
<td>controls</td>
<td>String</td>
<td>"default"</td>
<td>default 显示默认控件，none 不显示控件，system 移动端显示系统控件。<br> （备注：如果需要在移动端使用系统全屏，就需要设置为 system。默认全屏方案是使用 Fullscreen API + 伪全屏的方式，<a href="https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer-consoles.html">在线示例</a> ）  <br> 示例："system"</td>
</tr>
<tr>
<td>systemFullscreen</td>
<td>Boolean</td>
<td>false</td>
<td>开启后，在不支持 Fullscreen API 的浏览器环境下，尝试使用浏览器提供的 webkitEnterFullScreen 方法进行全屏，如果支持，将进入系统全屏，控件为系统控件。  <br> 示例：true</td>
</tr>
<tr>
<td>h5_flv</td>
<td>Boolean</td>
<td>false</td>
<td>是否启用 flv.js 的播放 flv。启用时播放器将在支持 MSE 的浏览器下，采用 flv.js 播放 flv，然而并不是所有支持 MSE 的浏览器都可以使用 flv.js，所以播放器不会默认开启这个属性，[v2.2.0+]。   <br> 示例：true</td>
</tr>
<tr>
<td>x5_player</td>
<td>Boolean</td>
<td>false</td>
<td>是否启用 TBS 的播放 flv 或 hls 。启用时播放器将在 TBS 模式下(例如 Android 的微信、QQ 浏览器），将 flv 或 hls 播放地址直接赋给 <code>&lt;video&gt;</code> 播放。<a href="https://x5.tencent.com/tbs/product/video.html">TBS 视频能力</a> [v2.2.0+]。   <br> 示例： true</td>
</tr>
<tr>
<td>x5_type</td>
<td>String</td>
<td>无</td>
<td>通过 video 属性 “x5-video-player-type” 声明启用同层 H5 播放器，支持的值：h5-page (该属性为 TBS 内核实验性属性，非 TBS 内核不支持)，<a href="https://x5.tencent.com/docs/video.html">TBS H5 同层播放器接入规范</a>。   <br> 示例："h5-page"</td>
</tr>
<tr>
<td>x5_fullscreen</td>
<td>String</td>
<td>无</td>
<td>通过 video 属性 “x5-video-player-fullscreen” 声明视频播放时是否进入到 TBS 的全屏模式，支持的值：true (该属性为 TBS 内核实验性属性，非 TBS 内核不支持) 。   <br> 示例："true"</td>
</tr>
<tr>
<td>x5_orientation</td>
<td>Number</td>
<td>无</td>
<td>通过 video 属性 “x5-video-orientation” 声明 TBS 播放器支持的方向，可选值：<ul style="margin:0"><li>0：landscape 横屏</li><li>1：<code>portraint</code> 竖屏</li><li>2：<code>landscape &amp;verbar; portrait</code> 跟随手机自动旋转。</li></ul> (备注：该属性为 TBS 内核实验性属性，非 TBS 内核不支持) [v2.2.0+]。  <br> 示例：0</td>
</tr>
<tr>
<td>wording</td>
<td>Object</td>
<td>无</td>
<td>自定义文案。   <br> 示例：{ 2032: '请求视频失败，请检查网络'}</td>
</tr>
<tr>
<td>clarity</td>
<td>String</td>
<td>'od'</td>
<td>默认播放清晰度 [v2.2.1+]。 <br> 示例：clarity: 'od'</td>
</tr>
<tr>
<td>clarityLabel</td>
<td>Object</td>
<td>{od: '超清', hd: '高清', sd: '标清'}</td>
<td>自定义清晰度文案 [v2.2.1+]。 <br> 示例：clarityLabel: {od: '蓝光', hd: '高清', sd: '标清'}。</td>
</tr>
<tr>
<td>listener</td>
<td>Function</td>
<td>无</td>
<td>事件监听回调函数，回调函数将传入一个 JSON 格式的对象。  <br> 示例：<br> function(msg){<br>//进行事件处理 <br>}</td>
</tr>
<tr>
<td>pausePosterEnabled</td>
<td>Boolean</td>
<td>true</td>
<td>暂停时显示封面 [v2.3.0+]。</td>
</tr>
<tr>
<td>preload</td>
<td>String</td>
<td>'auto'</td>
<td>配置 video 标签的 preload 属性，只有部分浏览器生效[v2.3.0+]。</td>
</tr>
<tr>
<td>hlsConfig</td>
<td>Object</td>
<td>无</td>
<td>hls.js 初始化配置项 [v2.3.0+]。</td>
</tr>
<tr>
<td>flvConfig</td>
<td>Object</td>
<td>无</td>
<td>flv.js 初始化配置项 [v2.3.1+]。</td>
</tr>
<tr>
<td>webrtcConfig</td>
<td>Object</td>
<td>无</td>
<td>webrtc 初始化配置项 [v2.4.1+]。<br>支持通过 streamType 指定拉流类型，默认拉取音视频，可选单独拉取视频或单独拉取音频，streamType 可选属性：<li>auto：拉取视频流和音频流</li><li> video：仅拉取视频流</li><li> audio：仅拉取音频流<br> 示例：<code>webrtcConfig: { streamType: 'video' }</code></li></td>
</tr>
</tbody></table>

>! 
>- WebRTC 快直播播放地址支持两种格式，除 `webrtc://domain/AppName/StreamName?txSecret=XXX&txTime=XXX` 以外，还支持 `http://domain/AppName/StreamName.sdp?txSecret=XXX&txTime=XXX` 格式的播放地址，但是需要配置播放域名 CNAME 到 `overseas-webrtc.liveplay.myqcloud.com` 。
>- 由于 Web 浏览器目前不支持标准 WebRTC 协议携带 B 帧播放，如果原始流存在 B 帧，则后台会自动进行转码去掉 B 帧，这样会引入额外的转码延迟，并产生转码费用。建议尽量不推包含 B 帧的流，移动直播 SDK，IOS 不支持引入 B 帧，安卓如果不开启 B 帧设置，默认是没有带 B 帧。如果使用 OBS 推流，可以通过设置，关闭 B 帧。

## 实例方法列表
播放器实例支持的方法，如下所示：

| 方法             | 参数&nbsp;                    | 返回值&nbsp; &nbsp;                        | 说明                                    |  示例
|-----------------|------------------------|----------------------------- |----------------------------------------|---------------------|
|play()           | 无                     | 无                           | 开始播放视频。                             | player.play() |
|pause()          | 无                     | 无                           | 暂停播放视频。                             | player.pause() |
|togglePlay()     | 无                     | 无                           | 切换视频播放状态 。                         | player.togglePlay() |
|mute(muted)      | {Boolean} [可选]       | true,false {Boolean}         | 切换静音状态，不传参则返回当前是否静音。      | player.mute(true) |
|volume(val)      | {int} 范围：0到1 [可选]  | 范围：0到1                    | 设置音量，不传参则返回当前音量 。            | player.volume(0.3) |
|playing()        | 无                     | true,false {Boolean}         | 返回是否在播放中 。                        | player.playing() |
|duration()       | 无                     | {int}                       | 获取视频时长 。<br>（**备注：只适用于点播，需要在触发 loadedmetadata 事件后才可获取视频时长**） | player.duration() |
|currentTime(time)| {int} [可选]           | {int}                       | 设置视频播放时间点，不传参则返回当前播放时间点 。<br>（**备注：只适用于点播** ）| player.currentTime() |
|fullscreen(enter)| {Boolean} [可选]       | true,false {Boolean}         | 调用全屏接口(Fullscreen API)，不支持全屏接口时使用伪全屏模式，不传参则返回值当前是否是全屏。 <br>（**备注：移动端系统全屏没有提供 API，也无法获取系统全屏状态** ）| player.fullscreen(true) |
|buffered()       | 无                     |  0到1                        | 获取视频缓冲数据百分比。 <br>（**备注：只适用于点播**） | player.buffered()  |
|destroy()        | 无                     |  无                        | 销毁播放器实例[v2.2.1+]。 | player.destroy()  |
|switchClarity()  | {String}[必选]         |  无                        | 切换清晰度，传值 "od"、"hd"、"sd" [v2.2.1+]。 | player.switchClarity('od')  |
|load(url)        | {String}[必选]         |  无                        |  通过视频地址加载视频。<br>（**备注：该方法只能加载对应播放模式下支持的视频格式，H5 模式支持 MP4、HLS 和 FLV（HLS、FLV 取决于浏览器是否支持）** [v2.2.2+]） | player.load(`http://xxx.mp4`)  |

>!以上方法必须是`TcPlayer`的实例化对象，且需要初始化完毕才可以调用（即 load 事件触发后）。

## 进阶攻略
下面介绍播放器 SDK 的进阶使用方法。

### ES Module
TCPlayerLite 提供了 ES Module 版本，module name 为`TcPlayer`，下载地址：
```
https://web.sdk.qcloud.com/player/tcplayerlite/release/v2.4.5/TcPlayer-module-2.4.5.js
```
### 开启优先 H5 播放模式
TCPlayerLite 根据不同的播放环境，播放器会选择默认最合适的播放方案。

### 监听事件
TCPlayerLite 以 H5`<video>`的规范，对播放事件做了一定程度的转换，以实现播放事件命名的统一，`TcPlayer`对原生事件进行了捕获和透传。

- [H5 事件参考列表](https://www.w3.org/wiki/HTML/Elements/video#Media_Events)
- [统一后的事件列表](https://www.w3school.com.cn/)
```
error
timeupdate
load
loadedmetadata
loadeddata
progress
fullscreen
play
playing
pause
ended
seeking
seeked
resize
volumechange
webrtcstatupdate
webrtcwaitstart
webrtcwaitend
webrtcstop
```
>! 
>- 如果通过系统控制栏进行全屏，将无法监听到 fullscreen 事件。
>- Web 播放器的事件，依赖浏览器内置的解码器触发，Web 播放器仅透传事件。
>- Web 播放器监听不到直播停止推流的事件，需要通过额外的接口来确认推流状态，请参见 [查询流状态](https://cloud.tencent.com/document/product/267/20470)。

在非自动播放的条件下，加载视频至待播放状态，移动端和 PC 触发的事件区别。
**移动端：**
![](https://main.qcloudimg.com/raw/f0bf0532e253c6f14f8c65dc5fd3a5c2.png)

**PC：**
![](https://main.qcloudimg.com/raw/0ff02cdc2ef70b2f8917decddec3cab8.png)
>?以上是两种平台的差异，然而在移动端的各种设备和 App 之间同样存在差异。

事件监听函数返回的 msg 对象介绍：

| 名称      | 说明                                                                                    |
|-----------|---------------------------------------------------------------------------------------|
| type      | 事件类型。                                                                               |
| src       | 事件源对象，即播放器实例，HTML5 。                                               |
| ts        | 事件触发时的 UTC 时间戳。                                                                |
| timeStamp | [Event](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/timeStamp) 实例的时间戳。 |


应用案例：通过事件监听，可以进行播放失败重连，[单击访问](https://web.sdk.qcloud.com/player/tcplayerlite/tcplayer-reconnect.html) 在线案例。

## 案例展示
结合了 TcPlayer 和即时通信 IM 的腾讯云 Web 直播互动组件：[体验地址](https://web.sdk.qcloud.com/component/tweblive/demo/latest/index.html#/)。

## 更新日志
TCPlayerLite 在不断更新及完善中，下面是 TCPlayerLite 发布的主版本介绍。

<table>
<tr><th>日期</th><th>版本</th><th>更新内容</th>
</tr>
<tr>
<td>2022.07.11</td>
<td>2.4.5</td>
<td>
     <li>修复 webrtc 场景的 stopplay 方法调用时序问题。</li>
</td>
</tr>
<tr>
<td>2022.06.7</td>
<td>2.4.4</td>
<td>
     <li>新增 webrtc 降级逻辑支持支付宝环境。</li>
     <li>更新 txliveplayer 版本。</li>
</td>
</tr>
<tr>
<td>2022.05.7</td>
<td>2.4.3</td>
<td>
     <li>新增拉流开始和拉流成功事件。</li>
     <li>新增浏览器无法自动播放时触发的事件回调。</li>
     <li>新增 stop 方法，该方法会断流，包括快直播和标准直播。</li>
     <li>新增支持 amd 规范。</li>
     <li>快直播场景降级时优先判断当前环境是否支持 flv。</li>
     <li>更新 txliveplayer 版本。</li>
     <li>修复 seek 后 loading 不消失的 bug。</li>
</td>
</tr>

<tr>
<td>2022.04.20</td>
<td>2.4.2</td>
<td>
     <li>修复微信 ua 变化导致的判断逻辑错误</li>
</td>
</tr>
<tr>
<td>2021.06.25</td>
<td>2.4.1</td>
<td><li>新增支持 v1 信令的 WebRTC 的流地址。</li><li>增加 webrtcConfig 参数。</li><li>增加 WebRTC 卡顿、卡顿结束、推流结束事件。</li></td>
</tr><tr>
<td>2021.06.03</td>
<td>2.4.0</td>
<td><li>增加对快直播功能的支持。 </li><li>修复其他已知问题。</li></td>
</tr><tr>
<td>2020.07.01</td>
<td>2.3.3</td>
<td><li>修复 X5 环境下切换全屏时，事件派发异常的问题。</li><li>规避 hls 切换源时，相关事件触发时机很慢，导致封面显示异常的问题。</li></td>
</tr><tr>
<td>2019.08.20</td>
<td>2.3.2</td>
<td><li>修改默认 hls 版本为0.12.4。</li><li>修复其他已知问题。</li></td>
</tr><tr>
<td>2019.04.26</td>
<td>2.3.1</td>
<td><li>增加 fivConfig 参数。</li><li>默认加载 flv.1.5.js。</li><li>修复其他已知问题。</li></td>
</tr><tr>
<td>2019.04.19</td>
<td>2.3.0</td>
<td><li>增加部分功能参数选项。</li><li>参数 coverpic 改为 poster。</li><li>destroy 销毁 flv.js 实例。</li><li>修复其他已知问题。</li></td>
</tr><tr>
<td>2018.12.17</td>
<td>2.2.3</td>
<td><li>优化播放逻辑。</li><li>解决 iOS 微信没有播放事件触发的情况下，出现 loading 动画的问题。</li><li>修复其他已知问题。</li></td>
</tr><tr>
<td>2018.05.03</td>
<td>2.2.2</td>
<td><li>优化 loading 组件。 </li><li>优化 Flash destroy 方法。</li><li>默认使用 H5 播放。</li><li>修复已知问题。</li></td>
</tr><tr>
<td>2017.12.20</td>
<td>2.2.1</td>
<td><li>增加可配置清晰度文案功能。</li><li>设置默认清晰度。</li><li>支持切换清晰度方法。</li></td>
</tr><tr>
<td>2017.12.07</td>
<td>2.2.1</td>
<td><li>增加 systemFullscreen 参数。</li><li>增加 flashUrl 参数。</li><li>修复音量 Max 后进行静音切换的 UI 问题。 </li><li>修复 iOS 11 微信下需要单击两次才能播放的问题。</li><li>修复 safari 11 系统样式被遮挡的问题。</li><li>适配在 x5 内核会触发 seeking，但不会触发 seeked 的情况。</li><li>修复进度条拖拽到起始位置，设置 currentTime 失败的问题。 </li><li>切换清晰度保持音量不变。</li><li>修复页面宽度为0，播放器宽度判断失败问题。 </li><li>destroy 方法增加完全销毁播放器节点。</li></td>
</tr><tr>
<td>2017.06.30</td>
<td>2.2.0</td>
<td><li>增加控制播放环境判断的参数： Flash、h5_flv、x5_player。</li><li>调整播放器初始化逻辑，优化错误提示效果。</li><li>增加 flv.js 支持，在符合条件的情况下可以采用 flv.js 播放 FLV。</li><li>支持 x5-video-orientation 属性。</li><li>增加播放环境判断逻辑，可通过参数调整 H5 与 Flash 的优先级，以及是否启用 TBS 播放。</li><li>启用版本号发布方式，避免影响旧版本的使用者。</li><li>优化事件触发的时间戳，统一为标准时间。</li><li>Bug 修复。</li></td>
</tr><tr>
<td>2017.03.04</td>
<td>2.1.0</td>
<td>至2017.06.30，经历数次的迭代开发，逐步趋于稳定，目前文档的功能描述中，如果没有特殊说明，皆基于此版本。</td>
</tr><tr>
<td>2016.12.28</td>
<td>2.0.0</td>
<td>首个版本。</td>
</tr></table>
