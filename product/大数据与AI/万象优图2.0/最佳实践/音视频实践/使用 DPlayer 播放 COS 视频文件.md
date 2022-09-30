## 简介

本文将介绍如何使用 [DPlayer](https://dplayer.js.org/) 并结合 [腾讯云数据万象（CI）](https://cloud.tencent.com/document/product/460/47503) 所提供的丰富的音视频能力，实现在 Web 浏览器播放 COS 视频文件。

## 集成指引

#### 步骤1：在页面中引入播放器脚本文件以及按需引入部分依赖文件
```
<!-- 播放器脚本文件 -->
<script src="https://cdn.jsdelivr.net/npm/dplayer@1.26.0/dist/DPlayer.min.js"></script>
```
>?建议在正式使用播放器时，自行部署以上相关静态资源。

#### 步骤2：设置播放器容器节点
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<div id="dplayer" style="width: 100%; height: 100%"></div>
```

#### 步骤3：获取视频文件对象地址
1. [创建一个存储桶](https://cloud.tencent.com/document/product/436/13309)
2. [上传视频文件](https://cloud.tencent.com/document/product/436/13321)
3. 获取视频文件对象地址，格式为：`https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.<视频格式>`。

>?
> - 若存在跨域问题，则需要进行存储桶跨域访问 CORS 设置，详情请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318)。
> - 若存储桶为私有读写，则对象地址需要携带签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778)。

#### 步骤4：初始化播放器，并传入 COS 视频文件对象地址 URL
```
const dp = new DPlayer({
  container: document.getElementById('dplayer'),
  video: {
  	url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4', // COS 视频对象地址
  },
});
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
const dp = new DPlayer({
  container: document.getElementById('dplayer'),
  video: {
  	url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4', // COS 视频对象地址
  },
});
```

获取示例代码：
- [播放 MP4 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/mp4.html)
- [播放 FLV 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/flv.html)
- [播放 HLS 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/m3u8.html)
- [播放 DASH 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/dash.html)

[](id:2)
### 播放 PM3U8 视频
PM3U8 是指私有的 M3U8 视频文件，COS 提供用于获取私有 M3U8 TS 资源的下载授权 API，可参见 [私有 M3U8 接口](https://cloud.tencent.com/document/product/436/73189)。
```
 const dp = new DPlayer({
   container: document.getElementById('dplayer'),
   // 关于 pm3u8 详情请查看相关文档：https://cloud.tencent.com/document/product/436/73189
   video: {
     url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8?ci-process=pm3u8&expires=3600' // 私有 ts 资源 url 下载凭证的相对有效期为3600秒
   }
 });
```
获取示例代码：
- [播放 PM3U8 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/pm3u8.html)

[](id:3)
### 设置封面图
1. 获取 COS 存储桶上的封面图对象地址。
>!通过数据万象 [智能封面](https://cloud.tencent.com/document/product/460/47508) 能力，提取最优帧生成截图作为封面，可提升内容吸引力。
2. 初始化播放器并设置封面图。
```
const dp = new DPlayer({
  container: document.getElementById('dplayer'),
  video: {
    url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4',
    pic: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.png',
  },
});
```

获取示例代码：
- [设置封面图示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/poster.html)

[](id:4)
### 播放 HLS 加密视频
为了保障视频内容安全，防止视频被非法下载和传播，数据万象提供了对 HLS 视频内容进行加密的功能，拥有相比于私有读文件更高的安全级别。加密后的视频，无法分发给无访问权限的用户观看。即使视频被下载到本地，视频本身也是被加密的，无法恶意二次分发，从而保障您的视频版权不受到非法侵犯。
操作步骤如下：
1. 参见 [播放 HLS 加密视频](https://cloud.tencent.com/document/product/436/63989) 和 [COS 音视频实践 | 给你的视频加把锁](https://mp.weixin.qq.com/s/4f-GKyAG0S-FcZ2BZCn7jA) 流程，生成加密视频。
2. 初始化播放器并传入视频对象地址。
```
 const dp = new DPlayer({
   container: document.getElementById('dplayer'),
   video: {
     url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8' // 加密视频地址
   }
 });
```


获取示例代码：
- [播放 HLS 加密视频示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/m3u8.html)

[](id:5)
### 切换多清晰度

数据万象 [自适应码流](https://cloud.tencent.com/document/product/460/58430) 功能，可以将视频文件转码并打包生成自适应码流输出文件，帮助用户在不同网络情况下快速分发视频内容，播放器能够根据当前带宽，动态选择最合适的码率播放，详情可参见 [COS 音视频实践 ｜ 数据工作流助你播放多清晰度视频](https://mp.weixin.qq.com/s/THUhur1FV_55T9zzqT2MFQ)。

操作步骤如下：
1. 通过 数据万象 [自适应码流](https://cloud.tencent.com/document/product/460/58430) 功能，生成多码率自适应的 HLS 或 DASH 目标文件。
2. 初始化播放器并传入视频对象地址。
```
const dp = new DPlayer({
  container: document.getElementById('dplayer'),
  video: {
  	url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.m3u8', //  多码率的HLS/DASH视频
  },
});
```

获取示例代码：
- [切换清晰度示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/multiDefinition.html)

[](id:6)
### 设置左上角 LOGO
播放器支持在左上角设置 LOGO。
操作步骤如下：
1. 获取 COS 存储桶上的 LOGO 图标对象地址。
2. 初始化播放器并设置 LOGO 图标。
```
const dp = new DPlayer({
	container: document.getElementById('dplayer'),
  video: {
  	url: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.mp4',
  },
	logo: 'https://<BucketName-APPID>.cos.<Region>.myqcloud.com/xxx.svg'
});
```

获取示例代码：
- [设置左上角 LOGO 示例代码](https://github.com/tencentyun/cos-demo/blob/main/cos-video/examples/web/dplayer/logo.html)

## Demo 体验

您可在线体验 COS 音视频功能，单击前往 [COS 音视频体验馆](https://cloud.tencent.com/document/product/436/77751)。
