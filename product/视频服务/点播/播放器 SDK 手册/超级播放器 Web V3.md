
本文档是介绍腾讯云 Web 视频点播服务的超级播放器，它可以帮助您通过灵活的接口，快速与自有 Web 应用集成，实现视频播放功能，本文档适合有一定 Javascript 语言基础的开发人员阅读。

## 能力介绍
点播超级播放器是通过 HTML5`<video>`标签以及 Flash 实现视频播放。在浏览器不支持视频播放的情况下，实现了视频播放效果的多平台统一体验，并结合云点播视频服务，提供防盗链和 DRM 加密播放等功能。

### 视频格式与平台支持

| 浏览器/格式     | MP4 | HLS | DASH |
|:----------------|:---:|:---:|:----:|
| Chrome          |  ✔  |  ✔  |  ✔   |
| Firefox         |  ✔  |  ✔  |  ✔   |
| Edge            |  ✔  |  ✔  |  ✔   |
| QQ 浏览器       |  ✔  |  ✔  |  ✔   |
| Mac Safari      |  ✔  |  ✔  |  ✔   |
| iOS Safari      |  ✔  |  ✔  |  ✖   |
| iOS 微信/QQ     |  ✔  |  ✔  |  ✖   |
| Android Chrome  |  ✔  |  ✔  |  ✔   |
| Android 微信/QQ |  ✔  |  ✔  |  ✖   |
| 手机 QQ 浏览器  |  ✔  |  ✔  |  ✖   |
| IE11/10/9/8     |  ✔  |  ✔  |  ✖   |

>?
>- 视频编码格式仅支持 H.264 编码。
>- Chrome，Firefox 包括 Windows、macOS 平台。
>- Chrome，Firefox，Edge，QQ 浏览器播放 HLS 需要加载 hls.js。
>- Chrome，Firefox，Edge，Android Chrome，Mac Safari 播放 DASH 需要加载 dash.js。
>- Android 微信、QQ 为 TBS 内核，原生支持播放 MP4、HLS。
>- IE8 采用 Flash 播放，IE9/10/11 播放 HLS 时采用 Flash 播放，需要确保浏览器支持 Flash 插件。
>- IE8 仅支持 Windows 7 系统的 IE8。

播放器兼容常见的浏览器，播放器内部会自动区分平台，并使用最优的播放方案。例如，在 IE11/10/9/8 浏览器中会使用 Flash 播放器以实现其不支持 HTML5 播放 HLS 的能力，在 Chrome 等现代浏览器中优先使用 HTML5 技术实现视频播放，而手机浏览器上会使用 HTML5 技术或者浏览器内核能力实现视频播放。

### 点播平台的转自适应码流服务
目前应用最广泛的自适应码流格式为 HLS 和 Dash，自适应码流视频支持：根据播放环境的带宽情况，动态选择合适的码率播放，支持商业级 DRM 等功能。而播放器仅播放视频的自适应码流格式，因此通过本播放器播放的视频需要通过云点播转码进行 [转自适应码流](https://cloud.tencent.com/document/product/266/34071)。

## 准备工作
### Step1. 开通服务
在 [腾讯云官网](https://cloud.tencent.com/) 注册腾讯云账号，然后开通云点播。
### Step2. 上传视频并转码
云点播开通之后，需要 [上传视频](https://cloud.tencent.com/document/product/266/2841#.E4.B8.8A.E4.BC.A0.E8.A7.86.E9.A2.91)，并进行 [转码处理](https://cloud.tencent.com/document/product/266/2841#.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91)。
### Step3. 获取 ID 与 APPID
1. 获取 ID（fileID）：视频上传后，通过媒资管理可以 [查看视频 ID](https://cloud.tencent.com/document/product/266/2841#.E5.BF.AB.E6.8D.B7.E6.9F.A5.E7.9C.8B.E8.A7.86.E9.A2.91.E4.BF.A1.E6.81.AF)。

2. 获取 APPID：在【腾讯云控制台】>【[账号信息](https://console.cloud.tencent.com/developer)】中查看。

### Step4. 转自适应码流，获取 playDefinition
通过 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) ，对上传的视频发起 [转自适应码流](https://cloud.tencent.com/document/product/266/34071) 任务：
API 参数中的`MediaProcessTask.AdaptiveDynamicStreamingTaskSet.Definition`建议填10，表示转 HLS 格式的自适应码流，针对常见的参数组合，云点播提供了 [预置转自适应码流模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E8.87.AA.E9.80.82.E5.BA.94.E7.A0.81.E6.B5.81.E6.A8.A1.E6.9D.BF)。


## 初始化 Web 播放器
在准备工作完成后，通过以下步骤，您就可以在网页上添加一个视频播放器。

### Step1. 在页面中引入文件
在合适的地方引入播放器样式与脚本文件：
```
 <link href="//imgcache.qq.com/open/qcloud/video/tcplayer/tcplayer.css" rel="stylesheet">
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 和 Dash 格式的视频，需要在 tcplayer.min.js 之前引入 hls.js 和 dash.js。-->
 <script src="//imgcache.qq.com/open/qcloud/video/tcplayer/libs/hls.min.0.12.4.js"></script>
 <script src="//imgcache.qq.com/open/qcloud/video/tcplayer/libs/dash.all.min.2.9.3.js"></script>
 <!--播放器脚本文件-->
 <script src="//imgcache.qq.com/open/qcloud/video/tcplayer/tcplayer.min.js"></script>
```

### Step2. 放置播放器容器
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playsinline>
</video>
```

其中：
- 播放器容器必须为`<video>`标签。
- `player-container-id`为播放器容器的 ID，可自行设置。
- 播放器容器区域的尺寸，建议通过 CSS 进行设置，它比属性设置更灵活，可以实现铺满全屏、容器自适应等效果。
- `preload`属性规定是否在页面加载后载入视频，通常为了更快的播放视频，会设置为`auto`，其他可选值：
	- `meta`：当页面加载后只载入元数据。
	- `none`：当页面加载后不载入视频，移动端由于系统限制不会自动加载视频。
- `playsinline`和`webkit-playsinline`属性是为了在标准移动端浏览器不劫持视频播放的情况下实现行内播放，此处仅作示例，请按需使用。
- 设置`x5-playsinline`属性，在 TBS 内核会使用 X5 UI 的播放器。

### Step3. 初始化代码
在页面初始化的代码中加入以下初始化脚本，传入在准备工作中获取到的 fileID 与 APPID。
```
var player = TCPlayer('player-container-id', { // player-container-id 为播放器容器ID，必须与html中一致
    fileID: '7447398157015849771', // 请传入需要播放的视频filID 必须
    appID: '1256993030', // 请传入点播账号的appID 必须
    playDefinition: '10', // 请传入播放模版，必须
  });
```

>!要播放的视频需经过腾讯云转码，原始视频无法保证在浏览器中正常播放。

## 示例页面
[示例代码](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-base.html)
## 功能使用说明
下面将对播放器的部分功能进行详细说明，包括最佳实践与注意事项。
### 播放器尺寸设置
这里介绍几种给播放器设置尺寸的方法：

* 可以给`<video>`标签设置 width 和 height 属性，width 和 height 的属性值是以像素计量的（例如 width = "100px"或width = 100），不能设置百分比。
*	可以通过 CSS 设置尺寸，支持像素和百分比等类型的值（例如：width:"100px" 或 width:"100%" ）。

>?
>- 如果不设置宽高，播放器在获取到视频的分辨率后，将会以视频的分辨率设置播放器的显示尺寸；如果浏览器的可视区域尺寸小于视频分辨率，会造成播放器区域超出浏览器的可视区域，所以不建议这样做。最佳实践为通过 CSS 设置播放器的尺寸。
>- 熟练运用 CSS 可以实现铺满全屏、容器自适应等效果。

示例：
- [CSS 设置尺寸](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-size.html)
- [铺满网页可视区域](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-size-full-viewport.html)
- [等比率自适应](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-size-adaptive.html)

### 续播功能
开启续播功能的前提，必须通过 fileID 播放。有了唯一的 fileID，播放器才能记录该视频的播放时长，即：当播放未结束时关闭页面，在同一个浏览器中再次打开播放页面，可从上次观看的时间点继续播放。通过以下参数开启续播功能：

```
var player = TCPlayer('player-container-id', {
    fileID: '', // 请传入需要播放的视频 filID 必须
    appID: '', // 请传入点播账号的 appID 必须
    playDefinition: '', // 请传入播放模版，必须
    plugins:{
        ContinuePlay: { // 开启续播功能
          // auto: true, //[可选] 是否在视频播放后自动续播
          // text:'上次播放至 ', //[可选] 提示文案
          // btnText: '恢复播放' //[可选] 按钮文案
        },
      }
  });
```
开启成功后将会看到的效果如下图：
![](https://mc.qcloudimg.com/static/img/e155be329a6fec959e1ad6b361add390/image.png)

示例：[续播](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-continue-play.html)

>!
> - 必须通过 fileID 和 appID 播放经过腾讯云转码后的视频，才能使用该功能。
> - 该功能通过 localStorage 存储播放时间点，浏览器需支持该特性。
> - 在浏览器劫持视频播放的情况下，该功能无法使用。
> - 该功能不是多端多浏览器互通的。例如，在 PC 浏览器上没看完，不能在移动端浏览器上续播或者在 PC 的另一个浏览器续播，需额外的接口，可以自行开发。

### 倍速播放
在浏览器支持的情况下播放器**默认开启倍速播放功能**。

```
var player = TCPlayer('player-container-id', {
    fileID: '', // 请传入需要播放的视频 filID 必须
    appID: '', // 请传入点播账号的 appID 必须
    playbackRates: [0.5，1，1.25，1.5，2] // 设置变速播放倍率选项，仅 HTML5 播放模式有效
  });
```

>!
> - 如果浏览器不支持倍速播放，播放器将不会显示倍速切换按钮。
> - 如需关闭该功能请参见 [开发文档](https://cloud.tencent.com/document/product/881/30824#options-.E5.8F.82.E6.95.B0.E5.88.97.E8.A1.A8)。

### 设置播放器 logo
点播超级播放器支持配置播放器 logo，可以在[【Web播放器管理】](https://console.cloud.tencent.com/vod/distribute-play/web-player)选定某个播放器配置，在【外观】这一步设置 logo 信息。设置 logo 信息后，使用该播放器配置播放视频时，将会在指定位置显示 logo。

示例：[显示 Logo](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-logo.html)

>!
> - 在控制台设置播放器配置后，大概需要等待10分钟，让所有 CDN 节点生效该配置。
> - 在浏览器劫持视频播放的情况下，设置的 logo 将无法显示。

### 图片贴片功能
点播超级播放器支持配置片头、片中暂停以及片尾显示图片贴片，并且可以添加超链接。可以在在[【Web播放器管理】](https://console.cloud.tencent.com/vod/distribute-play/web-player)选定某个播放器配置，在【贴片】这一步设置贴片信息。

- 默认的贴片显示样式为水平垂直居中显示，如果图片的尺寸大于播放器显示区域，将按播放器的宽度等比缩放图片，水平居中显示图片，图片超出播放器区域部分将无法显示。
- 可以通过 CSS 自定义贴片的显示样式。
```
.tcp-image-patch-start{} /* 片头贴片样式Class */
.tcp-image-patch-pause{} /* 片中贴片样式Class */
.tcp-image-patch-ended{} /* 片尾贴片样式Class */
```

示例：[图片贴片](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-image-patch.html)

>!
>- 贴片建议使用体积不超过50KB且尺寸不超过播放器显示区域的图片，避免因图片过大影响视频初始化速度。
>- 在控制台设置播放器配置后，大概需要等待10分钟，让所有 CDN 节点生效该配置。
>- 在浏览器劫持视频播放的情况下，设置的贴片将无法显示。

### 缩略图预览
点播超级播放器支持缩略图预览，可以通过服务端 API 生成视频的缩略图与 VTT 文件，相关文档请参见 [截图 - 雪碧图](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。


开启成功的效果如下图：
![](https://main.qcloudimg.com/raw/cf668bbf1a991c347fbeacb6555831c1.png)

示例：[缩略图预览](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-vtt-thumbnail.html)

>!
>- 该功能仅支持桌面端浏览器。
>- 在浏览器劫持视频播放的情况下，该功能无法使用。
>- 生成的缩略图越多，进度条预览越精确，而缩略图越多，图片越大，加载越慢，需要取舍平衡。

### 切换 fileID 播放
通过实例化对象的 loadVideoByID(args) 方法，可以更换视频进行播放。该方法支持的参数如下：
```
player.loadVideoByID({
  fileID: '', // 请传入需要播放的视频 filID 必须
  appID: '', // 请传入点播账号的 appID 必须
  playDefinition: '', // 请传入播放模版，必须
  t: '', // 参考 Key 防盗链说明
  us: '', // 参考 Key 防盗链说明
  sign:'', // 参考 Key 防盗链说明
  exper:'' // 参考 试看功能说明
});
```

示例：[切换 fileID 播放](http://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-change-file.html)

### 镜像功能
激活镜像功能，可以让视频画面镜像翻转，如下图所示：
![](https://main.qcloudimg.com/raw/d5886d7d550be72b608077f341299610.png)

开启右键菜单镜像选项：
```
var player = TCPlayer('player-container-id', {
  fileID: '', // 请传入需要播放的视频 filID 必须
  appID: '', // 请传入点播账号的 appID 必须
  playDefinition: '', // 请传入播放模版，必须
  plugins: {
    ContextMenu: {
      mirror: true
    }
  }
});
```

示例：[镜像功能](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-mirror.html)

>!在浏览器劫持视频播放的情况下，该功能无法使用。

### 进度条标记
通过服务端 API 对视频 [增加打点信息](https://cloud.tencent.com/document/product/266/14190)，可以在播放器中开启显示进度条标记，如下图所示：
![](https://main.qcloudimg.com/raw/70d880065adce22cb64270f4999558f8.png)

播放器开启方式：
```
var player = TCPlayer('player-container-id', {
  fileID: '', // 请传入需要播放的视频 filID 必须
  appID: '', // 请传入点播账号的 appID 必须
  playDefinition: '', // 请传入播放模版，必须
  plugins: {
    ProgressMarker: true
  }
});
```

示例：[进度条标记](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-progress-marker.html)

>!
>- 该功能仅支持桌面端浏览器。
>- 在浏览器劫持视频播放的情况下，该功能无法使用。

### Referer 防盗链
开启流程请参见 [Referer 防盗链](https://cloud.tencent.com/document/product/266/14046)。

播放器初始化需增加参数如下：
```
var player = TCPlayer('player-container-id', {
     fileID: '', // 请传入需要播放的视频filID 必须
     appID: '', // 请传入点播账号的appID 必须
     playDefinition: '', // 请传入播放模版，必须
     flash:{
         swf: '//[腾讯云隔离域名]/vod-player/[appID]/[fileID]/tcplayer/player.swf' //swf 文件地址 必须
     }
   });
```
需传入 swf URL，如果浏览器使用 Flash 播放，将会从这个地址获取 Flash 播放器。Flash 播放器发起视频请求时，请求的 Referer 会带上该 URL 或者带上页面的 URL。

>?
>- 播放器在 Flash 模式下发起视频请求的 Referer，在 IE 和 Firefox 浏览器中会带上 swf URL。
>- 您也可以将 player.swf 文件下载后，存放到您的 CDN 服务器中，swf 参数传入指向您的 CDN 服务器路径。
>- 腾讯云提供的隔离域名是每个用户独有的域名，一个 appID 对应一个域名，通常格式为：
>`[appID].vod2.myqcloud.com`。
>- 需要将播放器 swf URL 的域名添加到白名单内，开启了 Referer 防盗链的视频才能在 Flash 模式下播放。
>- 播放器的 Flash swf 文件默认存放在`imgcache.qq.com`域名下，如需部署到自己的服务器上，可自行下载并部署，[swf 文件地址](https://imgcache.qq.com/open/qcloud/video/tcplayer/player.swf)。
>- iframe 嵌入播放器页面，视频请求的 Referer 会带上 iframe src。

### 播放 DRM 内容
点播超级播放器集成了播放 [DRM](https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm) 内容的功能，支持以下几种 DRM 方案：

- 基于 Widevine 商业级加密的 DASH 方案。
- 基于 FairPlay 商业级加密的 HLS 方案。
- 基于 SimpleAES 基础级加密的 HLS 方案。

关于 DRM 的更多详情，请参见 [如何对内容做版权保护](<https://cloud.tencent.com/document/product/266/34105#.E5.95.86.E4.B8.9A.E7.BA.A7-drm>)。

#### 浏览器的支持情况
各浏览器对 DRM 的支持情况如下。

| 浏览器          | Widevine | FairPlay | SimpleAES |
|-----------------|----------|----------|-----------|
| Chrome(PC Mac)  | ✔        | ✖        | ✔         |
| Firefox(PC Mac) | ✔        | ✖        | ✔         |
| Edge            | ✖        | ✖        | ✔         |
| Mac Safari      | ✖        | ✔        | ✔         |
| iOS Safari      | ✖        | ✔        | ✔         |
| iOS Chrome      | ✖        | ✖        | ✔         |
| iOS 微信 QQ     | ✖        | ✖        | ✔         |
| Android Chrome  | ✔        | ✖        | ✔         |
| Android 微信 QQ | ✖        | ✖        | ✔         |
| IE8,9,10,11     | ✖        | ✖        | ✔         |

>! IE 浏览器采用 Flash 播放。

#### 使用方法

首先，App 需要从您的**业务后台**获取 Token，Token 的生成方式请参见 [Token 生成](<https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90>) 。如果需要播放 FairPlay 加密的内容，按照 [ASK 和 FPS 证书指引](https://cloud.tencent.com/document/product/266/34102#ask-.E5.92.8C-fps-.E8.AF.81.E4.B9.A6) 生成 FPS 证书，并将证书部署在您的服务器中，证书的下载地址 URI 记为`certificateUri`。

然后，通过 FileId + Token 方式进行播放，播放代码如下：

```
var player = TCPlayer('player-container-id', {
  appID:  '', // 请传入点播账号的 appID 必须
  fileID: '', // 请传入需要播放的视频 fileID 必须
  playDefinition: '' // 请传入播放模版，播放 DRM 内容必须
  plugins: {
    DRM: {
      token: '', // 传入您的后台服务签发的 token，播放 DRM 内容必须
      certificateUri: '', // 传入 FairPlay 证书的下载地址，播放 FairPlay 加密内容必须
    }
  }``
});
```
播放器会根据传入的 [播放模版](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF) ID 和当前浏览器的支持情况，按优先级选择合适的播放方案，DRM 方案选择优先级为：【Widevine】>【FairPlay】>【SimpleAES】，例如：
- 传入`playDefinition`为20 ，播放器依次选择 Widevine 或 FairPlay ，SimpleAES 的加密输出播放。
- 传入`playDefinition`为12 ，播放器依次选择 Widevine 或 FairPlay 的加密输出播放。
- 传入`playDefinition`为10 ，播放器将会选择未加密的 HLS 或 DASH 输出播放。

示例：[DRM 自动识别播放](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod-v3/tcplayer-vod-drm-token-auto.html)

相关指引如下：
- [播放模版说明文档](https://cloud.tencent.com/document/product/266/34101#.E6.92.AD.E6.94.BE.E6.A8.A1.E6.9D.BF)
- [Token 生成指引](https://cloud.tencent.com/document/product/266/34102#token-.E7.94.9F.E6.88.90)
- [FairPlay 证书生成指引](https://cloud.tencent.com/document/product/266/34102#ask-.E5.92.8C-fps-.E8.AF.81.E4.B9.A6)

>!
>- 商业级 DRM 内容只能在 HTTPS 协议下的页面进行播放。
>- DRM 内容目前只支持自适应码率。
