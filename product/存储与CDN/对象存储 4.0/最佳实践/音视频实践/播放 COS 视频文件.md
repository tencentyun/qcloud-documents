## 简介

本文介绍如何实现在 Web 浏览器播放对象存储（Cloud Object Storage，COS）存储桶的视频文件，以及实现一些进阶的视频播放场景。实践步骤以 [腾讯云点播超级播放器（TCPlayer）](https://cloud.tencent.com/document/product/266/58772) 为例。

## 实践步骤

1. 准备您的 COS 视频文件链接，您需要：
   - [创建一个存储桶](https://cloud.tencent.com/document/product/436/13309)
   - [上传对象](https://cloud.tencent.com/document/product/436/13321)
   - 在 [对象信息](https://cloud.tencent.com/document/product/436/13326) 里复制对象地址
2. 在页面中引入播放器样式文件与脚本文件：
```
<!--播放器样式文件-->
<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.min.css" rel="stylesheet"/>
<!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.v4.2.2.min.js 之前引入 hls.min.0.13.2m.js。-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/libs/hls.min.0.13.2m.js"></script>
<!--播放器脚本文件-->
<script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.v4.2.2.min.js"></script>
```
>?建议在正式使用播放器 SDK 时，自行部署以上相关静态资源，[单击下载播放器资源](https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/release.zip)。部署解压后的文件夹，不能调整文件夹里面的目录，避免资源互相引用异常。
>
3. 设置播放器容器节点
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
> 
4. 初始化播放器，并传入 COS 视频文件对象地址 URL。
```
   var player = TCPlayer('player-container-id', {}); // player-container-id 为播放器容器 ID，必须与 html 中一致
   player.src(url); // url 播放地址
```

## 进阶使用场景

### 场景1：播放公有读视频文件

存储桶公有读权限包括两种：公有读私有写、公有读写。其中，公有读私有写权限下，任何人（包括匿名访问者）都对该存储桶中的对象有读权限，但只有存储桶创建者和已被授权的账号才对该存储桶中的对象有写权限。公有读写权限下，任何人（包括匿名访问者）都对该存储桶中的对象有读权限和写权限，不推荐使用。

播放公有读权限的视频文件的步骤为：
1. 将存储桶设置为公有读，参考 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。
2. 上传视频文件后，在 [对象信息](https://cloud.tencent.com/document/product/436/13326)中，复制对象地址。
3. 结合前面的步骤流程，使用 TCPlayer 播放公有读视频文件地址，代码如下：
```
   <script>
     var tcplayer = TCPlayer("player-container-id", {})
     tcplayer.src('https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/path/test.mp4')
   </script>
```
4. 查看效果。
![](https://qcloudimg.tencent-cloud.cn/raw/2fc23e71f3675e0e98ce9a42c3a1d34c.png)

### 场景2：播放私有读视频文件

为了保障存储桶数据的安全性能，一般推荐将存储桶设为私有读写权限。此时只有该存储桶的创建者及有授权的账号才对该存储桶中的对象有读写权限，其他任何人对该存储桶中的对象都没有读写权限。

播放私有读权限的视频文件的步骤为：
1. 将存储桶设置为私有读，参考 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。
2. 由于存储桶为私有读，因此访问的对象地址需要携带上签名，有三种方式：
 - 方法一：在 [对象信息](https://cloud.tencent.com/document/product/436/13326) 中，**复制临时链接**，该临时链接携带有效期为1小时的签名参数。
![复制临时链接](https://qcloudimg.tencent-cloud.cn/raw/6760807294324f79c5e0e5d3258e597e.png)
 - 方法二：利用 [COS 签名工具](https://cloud.tencent.com/document/product/436/30442)，计算您的对象签名。
 - 方法三：利用 API 或对应 SDK，计算您的对象签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778#sdk-.E7.AD.BE.E5.90.8D.E5.AE.9E.E7.8E.B0)。
以上三种方法中，正式使用时推荐使用方法三的 SDK 签名方式，可更加方便、安全地计算您的对象签名。
3. 结合前面的步骤流程，利用 TCPlayer 播放**携带签名**的私有读视频文件地址，完整代码如下：
```
   <script>
     var tcplayer = TCPlayer("player-container-id", {})
     tcplayer.src('https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/path/test.mp4?<Authorization>')
   </script>
```
4. 查看效果。
![2](https://qcloudimg.tencent-cloud.cn/raw/2fc23e71f3675e0e98ce9a42c3a1d34c.png)

### 场景3：播放公有读 HLS 视频文件

>? **HTTP Live Streaming**（缩写是 **HLS**）是一个由苹果公司提出的基于 HTTP 的流媒体网络传输协议，它是苹果公司 QuickTime X 和 iPhone 软件系统的一部分。它的工作原理是把整个流分成一个个小的基于 HTTP 的文件来下载，每次只下载一些。当媒体流正在播放时，客户端可以选择从许多不同的备用源中以不同的速率下载同样的资源，允许流媒体会话适应不同的数据速率。在开始一个流媒体会话时，客户端会下载一个包含元数据的 extended M3U m3u8playlist 文件，用于寻找可用的媒体流。
>

对象存储（Cloud Object Storage，COS）数据处理提供了 [HLS 视频转码](https://cloud.tencent.com/document/product/436/53968#.E5.88.9B.E5.BB.BA.E9.9F.B3.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81.E4.BB.BB.E5.8A.A1) 的功能。您可以结合 COS 数据工作流转码任务，播放 HLS 视频文件。

1. 根据 [创建音视频转码任务](https://cloud.tencent.com/document/product/436/53968#.E5.88.9B.E5.BB.BA.E9.9F.B3.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81.E4.BB.BB.E5.8A.A1)，选择系统模版中的任一 HLS 转码任务，配置任务生成 HLS 视频文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ce600b583301e3e1021e36b940ceb8ee.png" style="width: 65%" />
2. 复制生成的 m3u8 文件对象地址。
![](https://qcloudimg.tencent-cloud.cn/raw/8d21f4e85c63f44bf891883040ab0e8c.png)
3. 结合前面的步骤流程，利用TCPlayer播放**公有读 HLS**视频文件地址，完整代码如下：
```
   <script>
     var tcplayer = TCPlayer("player-container-id", {})
     tcplayer.src('https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/path/test.m3u8')
   </script>
```
4. 查看效果。
![3](https://qcloudimg.tencent-cloud.cn/raw/2fc23e71f3675e0e98ce9a42c3a1d34c.png)

### 场景4：播放私有读 HLS 视频文件

在场景3的基础上，为了保证存储桶数据的安全性，我们把存储桶设置为私有读写权限，同时结合 PM3U8 API，进行私有 HLS 视频文件的播放，具体步骤如下：
1. 将存储桶设置为私有读，参考 [设置访问权限](https://cloud.tencent.com/document/product/436/13315)。
2. 由于存储桶是私有的，所以需要给每块 TS 分片设置请求签名。COS 提供了 **PM3U8** API，让您在请求 m3u8 文件时，携带上相关的参数`?ci-process=pm3u8&expires=3600`，返回的文件中的 TS 分片请求路径就能携带上对应的请求签名。
  - 普通 m3u8 文件的请求结果如下，ts 分片不带签名：
     ![image-20211105162546606](https://qcloudimg.tencent-cloud.cn/raw/3f162b76dbd37b60922ea706f50b36dd.png)
  - 利用 **PM3U8 API**，请求的结果如下，ts 分片携带签名：![image-20211105163202007](https://qcloudimg.tencent-cloud.cn/raw/78c5eda94340421c019f6d04dd499b62.png)
3. 结合前面的步骤流程，利用 TCPlayer 播放**私有读 HLS** 视频文件地址，完整代码如下：
```
   <script>
     var tcplayer = TCPlayer("player-container-id", {})
     tcplayer.src('https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/path/test.m3u8?ci-process=pm3u8&expires=3600&sign')
   </script>
```
4. 查看效果。
![4](https://qcloudimg.tencent-cloud.cn/raw/2fc23e71f3675e0e98ce9a42c3a1d34c.png)

## 体验

以上实践，我们准备了一个 [线上体验 demo](https://ci-exhibition.cloud.tencent.com/tools/video/)，欢迎体验。
