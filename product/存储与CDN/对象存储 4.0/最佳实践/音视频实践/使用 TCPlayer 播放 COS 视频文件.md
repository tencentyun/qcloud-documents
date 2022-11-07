## 简介
本文将介绍如何使用音视频终端 SDK（腾讯云视立方）集成的 [ TCPlayer](https://cloud.tencent.com/document/product/881/30818) 并结合 [腾讯云数据万象(CI)](https://cloud.tencent.com/document/product/460/47503) 所提供的丰富的音视频能力，实现在 Web 浏览器播放 COS 视频文件。


## 集成指引
#### 步骤1：在页面中引入播放器样式文件及脚本文件
```
<!--播放器样式文件-->
<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.1/tcplayer.min.css" rel="stylesheet">
<!--播放器脚本文件-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.0/tcplayer.v4.5.0.min.js"></script>
```
>?
>- 建议在正式使用播放器 SDK 时，自行部署以上相关静态资源，[单击下载播放器资源](https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/release.zip)。
>- 部署解压后的文件夹，不能调整文件夹里面的目录，避免资源互相引用异常。

#### 步骤2：设置播放器容器节点
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。

```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playsinline>
</video>
```

>?
> - 播放器容器必须为 `<video>` 标签。
> - 示例中的 `player-container-id` 为播放器容器的 ID，可自行设置。
> - 播放器容器区域的尺寸，建议通过 CSS 进行设置，通过 CSS 设置比属性设置更灵活，可以实现例如铺满全屏、容器自适应等效果。
> - 示例中的 `preload` 属性规定是否在页面加载后载入视频，通常为了更快的播放视频，会设置为 `auto`，其他可选值：`meta`（当页面加载后只载入元数据），`none`（当页面加载后不载入视频），移动端由于系统限制不会自动加载视频。
> - `playsinline` 和 `webkit-playsinline` 这几个属性是为了在标准移动端浏览器不劫持视频播放的情况下实现行内播放，此处仅作示例，请按需使用。
> - 设置 `x5-playsinline` 属性在 TBS 内核会使用 X5 UI 的播放器。

#### 步骤3：获取视频文件对象地址
1. [创建一个存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. [上传视频文件](https://cloud.tencent.com/document/product/436/13321)。
3. 获取视频文件对象地址，格式为：`https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.<视频格式>`。

>?
> - 若存在跨域问题，则需要进行存储桶跨域访问 CORS 设置，详情请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318)。
> - 若存储桶为私有读写，则对象地址需要携带签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

#### 步骤4：初始化播放器，并传入 COS 视频文件对象地址 URL
```
var player = TCPlayer("player-container-id", {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
player.src("https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4"); // COS 视频对象地址
```

## 功能指引
[](id:1)
### 播放不同格式的视频文件
1. 获取 COS 存储桶上的视频文件对象地址。
>? 未经转码的源视频在播放时有可能出现不兼容的情况，建议您使用转码后的视频进行播放，通过数据万象 [音视频转码处理](https://cloud.tencent.com/document/product/460/47509)，获取不同格式视频文件。
2. 针对不同的视频格式，为了保证多浏览器的兼容性，需要引入对应的依赖。
 - MP4：无需引入其他依赖。
 - HLS：如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.min.js 之前引入 hls.min.js。
```
  <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.1/libs/hls.min.0.13.2m.js"></script>
```
 - FLV：如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 FLV 格式的视频，需要在 tcplayer.min.js 之前引入 flv.min.js。
```
  <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.2/libs/flv.min.1.6.2.js"></script>
```
 - DASH：DASH 视频需要加载 dash.all.min.js 文件。
```
  <script src="https://cos-video-1258344699.cos.ap-guangzhou.myqcloud.com/lib/dash.all.min.js"></script>
```
3. 初始化播放器并传入对象地址。
```
var player = TCPlayer("player-container-id", {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
player.src("https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4"); // COS 视频地址
```

获取示例代码：
- [播放 MP4 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/mp4.html)
- [播放 FLV 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/flv.html)
- [播放 HLS 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/m3u8.html)
- [播放 DASH 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/dash.html)


[](id:2)
### 播放 PM3U8 视频
PM3U8 是指私有的 M3U8 视频文件，COS 提供用于获取私有 M3U8 TS 资源的下载授权API，可参见 [私有 M3U8 接口](https://cloud.tencent.com/document/product/436/73189)。
```
var player = TCPlayer("player-container-id", {
	poster: "https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8?ci-process=pm3u8&expires=3600" // 私有 ts 资源 url 下载凭证的相对有效期为3600秒
});
```

获取示例代码：
- [播放 PM3U8 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/pm3u8.html)

[](id:3)
### 设置封面图
1. 获取 COS 存储桶上的封面图对象地址。
>!通过数据万象 [智能封面](https://cloud.tencent.com/document/product/460/47508) 能力，提取最优帧生成截图作为封面，可提升内容吸引力。
2. 设置封面图。
```
var player = TCPlayer("player-container-id", {
	poster: "https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.png"
});
```

获取示例代码：
- [设置封面图示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/poster.html)

[](id:4)
### 播放 HLS 加密视频
为了保障视频内容安全，防止视频被非法下载和传播，数据万象提供了对 HLS 视频内容进行加密的功能，拥有相比于私有读文件更高的安全级别。加密后的视频，无法分发给无访问权限的用户观看。即使视频被下载到本地，视频本身也是被加密的，无法恶意二次分发，从而保障您的视频版权不受到非法侵犯。

操作步骤如下：
1. 参见 [播放 HLS 加密视频](https://cloud.tencent.com/document/product/436/63989) 和 [COS 音视频实践 | 给你的视频加把锁](https://mp.weixin.qq.com/s/4f-GKyAG0S-FcZ2BZCn7jA) 流程，生成加密视频。
2. 初始化播放器并传入视频对象地址。
```
var player = TCPlayer("player-container-id", {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
player.src("https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8"); // hls 加密视频地址
```

获取示例代码：
- [播放 HLS 加密视频示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/m3u8.html)

[](id:5)
### 切换清晰度
数据万象 [自适应码流](https://cloud.tencent.com/document/product/460/58430) 功能，可以将视频文件转码并打包生成自适应码流输出文件，帮助用户在不同网络情况下快速分发视频内容，播放器能够根据当前带宽，动态选择最合适的码率播放，详情可参见 [COS 音视频实践 ｜ 数据工作流助你播放多清晰度视频](https://mp.weixin.qq.com/s/THUhur1FV_55T9zzqT2MFQ)。
操作步骤如下：
1. 通过 数据万象 [自适应码流](https://cloud.tencent.com/document/product/460/58430) 功能，生成多码率自适应的 HLS 或 DASH 目标文件。
2. 初始化播放器并传入视频对象地址。
```
var player = TCPlayer("player-container-id", {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
player.src("https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8"); // 多码率视频地址
```

获取示例代码：
- [切换清晰度示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/multiDefinition.html)

[](id:6)
### 设置动态水印
播放器支持为视频添加位置与速度产生变换的水印。在使用动态水印功能时，播放器对象的引用不能暴露到全局环境，否则动态水印可以轻易去除，数据万象也支持在云端对视频进行添加动态水印等操作，详情可参见 [水印模板接口](https://cloud.tencent.com/document/product/460/77715)。
```
var player = TCPlayer("player-container-id", {
    plugins:{
      DynamicWatermark: {
        speed: 0.2, // 速度
        content: "腾讯云数据万象 CI", // 文案
        opacity: 0.7 // 透明度
      }
    }
  });
```

获取示例代码：
- [设置动态水印](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/dynamicWatermark.html)

[](id:7)
### 设置贴片广告
操作步骤如下：
1. 准备视频广告封面图以及广告链接。
2. 初始化播放器，设置广告封面图和链接，并设置广告节点。
```
var PosterImage = TCPlayer.getComponent('PosterImage');
PosterImage.prototype.handleClick = function () {
	window.open('https://cloud.tencent.com/product/ci'); // 设置广告链接
};

var player = TCPlayer('player-container-id', {
	poster: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx..png', // 广告封面图
});
player.src('https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4');

var adTextNode = document.createElement('span');
adTextNode.className = 'ad-text-node';
adTextNode.innerHTML = '广告';

var adCloseIconNode = document.createElement('i');
adCloseIconNode.className = 'ad-close-icon-node';
adCloseIconNode.onclick = function (e) {
  e.stopPropagation();
  player.posterImage.hide();
};

player.posterImage.el_.appendChild(adTextNode);
player.posterImage.el_.appendChild(adCloseIconNode);
```

获取示例代码：
- [设置贴片广告示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/advertise.html)

[](id:8)
### 设置视频进度图
操作步骤如下：
1. 通过数据万象 [视频截帧](https://cloud.tencent.com/document/product/460/47505) 并生成雪碧图。
2. 获取步骤1生成的雪碧图和 VTT（雪碧图位置描述文件） 对象地址。
3. 初始化播放器，并设置视频地址和 VTT 文件。
```
var player = TCPlayer('player-container-id', {
  plugins: {
    VttThumbnail: {
      vttUrl: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.vtt' // 进度图 VTT 文件
    },
  },
});
player.src('https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4');
```

获取示例代码：
- [设置视频进度图示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/preview.html)

[](id:9)
### 设置视频字幕
操作步骤如下：
1. 通过数据万象 [语音识别](https://cloud.tencent.com/document/product/460/47492) 并生成字幕文件。
2. 获取步骤1生成的字幕 SRT 文件对象地址。
3. 初始化播放器，并设置视频地址和字幕 SRT 文件。
```
var player = TCPlayer('player-container-id', {});
player.src('https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4');
player.on('ready', function () {
  // 添加字幕文件
  var subTrack = player.addRemoteTextTrack({
    src: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.srt', // 字幕文件
    kind: 'subtitles',
    srclang: 'zh-cn',
    label: '中文',
    default: 'true',
  }, true);
});
```

获取示例代码：
- [设置视频字幕示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/subtitle.html)

[](id:10)
### 设置视频多语言字幕
操作步骤如下：
1. 通过数据万象 [语音识别](https://cloud.tencent.com/document/product/460/47492) 生成字幕文件，并同时翻译成多种语言。
2. 获取步骤1生成的多语言字幕 SRT 文件对象地址。
3. 初始化播放器，并设置视频地址和多语言字幕 SRT 文件。
```]
var player = TCPlayer('player-container-id', {});
player.src('https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4');
player.on('ready', function () {
  // 设置中文字幕
  var subTrack = player.addRemoteTextTrack({
    src: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/zh.srt', // 字幕文件
    kind: 'subtitles',
    srclang: 'zh-cn',
    label: '中文',
    default: 'true',
  }, true);
  // 设置英文字幕
  var subTrack = player.addRemoteTextTrack({
    src: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/en.srt', // 字幕文件
    kind: 'subtitles',
    srclang: 'en',
    label: '英文',
    default: 'false',
  }, true);
});
```

获取示例代码：
- [设置视频多语言字幕示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/tcplayer/multiLanguage.html)

## Demo 体验
您可在线体验 COS 音视频功能，单击前往 [COS 音视频体验馆](https://cloud.tencent.com/document/product/436/77751)。
