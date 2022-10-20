## 简介
本文将介绍如何使用 [VideojsPlayer](https://videojs.com/) 并结合 [腾讯云数据万象(CI)](https://cloud.tencent.com/document/product/460/47503) 所提供的丰富的音视频能力，实现在 Web 浏览器播放 COS 视频文件。

## 集成指引

#### 步骤1：在页面中引入播放器样式文件及脚本文件
```
<!-- 播放器样式文件 -->
<link href="https://vjs.zencdn.net/7.19.2/video-js.css" rel="stylesheet" />
<!-- 播放器脚本文件 -->
<script src="https://vjs.zencdn.net/7.19.2/video.min.js"></script>
```

>?建议在正式使用播放器时，自行部署以上相关静态资源。

#### 步骤2：设置播放器容器节点
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<video
  id="my-video"
  class="video-js"
  controls
  preload="auto"
  width="100%"
  height="100%"
  data-setup="{}"
></video>
```

#### 步骤3：获取视频文件对象地址
1. [创建一个存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. [上传视频文件](https://cloud.tencent.com/document/product/436/13321)。
3. 获取视频文件对象地址，格式为`https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.<视频格式>`。

>?
> - 若存在跨域问题，则需要进行存储桶跨域访问 CORS 设置，详情请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318)。
> - 若存储桶为私有读写，则对象地址需要携带签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

#### 步骤4：在播放器容器内设置视频地址，传入 COS 视频文件对象地址 URL
```
<video
  id="my-video"
  class="video-js"
  controls
  preload="auto"
  width="100%"
  height="100%"
  data-setup="{}"
>
  <source
    src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4"
    type="video/mp4"
  />
</video>
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
<!-- MP4 -->
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4"
  type="video/mp4"
/>

<!-- HLS -->
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8"
  type="application/x-mpegURL"
/>

<!-- FLV -->
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.flv"
  type="video/x-flv"
/>

<!-- DASH -->
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mpd"
  type="application/dash+xml"
/>
```

获取示例代码：
- [播放 MP4 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/mp4.html)
- [播放 FLV 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/flv.html)
- [播放 HLS 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/m3u8.html)
- [播放 DASH 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/dash.html)

[](id:2)
### 播放 PM3U8 视频
PM3U8 是指私有的 M3U8 视频文件，COS 提供用于获取私有 M3U8 TS 资源的下载授权API，可参见 [私有 M3U8 接口](https://cloud.tencent.com/document/product/436/73189)。
```
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8?ci-process=pm3u8&expires=3600"
  type="application/x-mpegURL"
/>
```

获取示例代码：
- [播放 PM3U8 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/pm3u8.html)

[](id:3)
### 设置封面图
1. 获取 COS 存储桶上的封面图对象地址。
>!通过数据万象 [智能封面](https://cloud.tencent.com/document/product/460/47508) 能力，提取最优帧生成截图作为封面，可提升内容吸引力。
2. 初始化播放器并设置封面图。
```
<video
  id="my-video"
  class="video-js"
  controls
  preload="auto"
  width="100%"
  height="100%"
  data-setup="{}"
  poster="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/poster.png"
>
  <source
    src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4"
    type="video/mp4"
  />
</video>
```

获取示例代码：
- [设置封面图示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/poster.html)

[](id:4)
### 播放 HLS 加密视频
为了保障视频内容安全，防止视频被非法下载和传播，数据万象提供了对 HLS 视频内容进行加密的功能，拥有相比于私有读文件更高的安全级别。加密后的视频，无法分发给无访问权限的用户观看。即使视频被下载到本地，视频本身也是被加密的，无法恶意二次分发，从而保障您的视频版权不受到非法侵犯。
操作步骤如下：
1. 参见 [播放 HLS 加密视频](https://cloud.tencent.com/document/product/436/63989) 和 [COS 音视频实践 | 给你的视频加把锁](https://mp.weixin.qq.com/s/4f-GKyAG0S-FcZ2BZCn7jA) 流程，生成加密视频。
2. 初始化播放器并传入视频对象地址。
```
<source
  src="https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8"
  type="application/x-mpegURL"
/>
```

获取示例代码：
- [播放 HLS 加密视频示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/videojs/m3u8.html)

## Demo 体验
您可在线体验 COS 音视频功能，单击前往 [COS 音视频体验馆](https://cloud.tencent.com/document/product/436/77751)。

