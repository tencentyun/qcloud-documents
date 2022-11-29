## 学习目标

学习本阶段教程，您将了解并掌握如何对视频进行 DRM 加密，并使用播放器播放加密后的视频 。

##  前置条件
在开始本教程之前，请您确保已满足以下前置条件。

### 开通云点播
您需要开通云点播，步骤如下：

1. 注册 [腾讯云账号](https://intl.cloud.tencent.com/document/product/378/17985)，并完成 [实名认证](https://intl.cloud.tencent.com/document/product/378/3629)。
2. 购买云点播服务，具体请参见 [计费概述](https://intl.cloud.tencent.com/document/product/266/2838)。
3. 选择 **云产品**>**视频服务**>[**云点播**](https://console.cloud.tencent.com/vod)，进入云点播控制台。

至此，您已经完成了云点播的开通步骤。 

### 申请 FairPlay 证书信息

请参考 [如何申请 FairPlay 证书信息](https://cloud.tencent.com/document/product/266/79725)。

### 提交 FairPlay 证书信息

请参考 [如何在点播控制台提交 FairPlay 证书信息](https://cloud.tencent.com/document/product/266/79728)。


## 步骤1：开启防盗链

以您账号下的默认分发域名开启 Key 防盗链为例：
>? 请避免直接对正在使用的现网域名开启防盗链，否则可能造成现网的视频无法播放。

1. 登录云点播控制台，选择【分发播放设置】>[【域名管理】](https://console.cloud.tencent.com/vod/distribute-play/domain)，单击“默认分发域名”的【设置】，单机【访问控制】，进入设置页面。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/9f6529f256a3f74f4c87f6b4c1ab293e.png" width="800" />
2. 打开【启用 Key 防盗链】，并单击【生成随机 Key】生成一个随机的 Key，本教程为`vodtestkey`，将生成好的 Key 复制下来，然后单击【确定】保存生效。防盗链 Key 可用于后续步骤中生成播放器签名。
   ![image-KEY](https://qcloudimg.tencent-cloud.cn/raw/9e92b38164843a729cf4d64af6dac402.png)

## 步骤2：对视频进行 DRM 加密

1. 登录云点播控制台，选择 **媒资管理**>[**视频管理**](https://console.cloud.tencent.com/vod/media)，勾选要处理的视频（FileId 为387702304941991610），单击 **视频处理**。

   ![image-20220426211316803](https://qcloudimg.tencent-cloud.cn/raw/3566b9d58047da7a212b8275673d461c.png)

2. 在视频处理界面：
 - **处理类型** 选择 **任务流**。
 - **任务流模板** 选择 **WidevineFairPlayPreset**。
 ![image-20220425192205432](https://qcloudimg.tencent-cloud.cn/raw/241677fe7d1626329f7be0f5643bc70e.png)

>?
>- WidevineFairPlayPreset 是预置任务流：分别使用11、13模板转自适应码流，10模板截图做封面，10模板截雪碧图。
>- 11模板自适应码流是加密类型为 `FairPlay` 的多码率输出，13模板自适应码流是加密类型为 `Widevine` 的多码率输出。

3. 单击 **确定**，等待“视频状态”栏从“处理中”变为“正常”，表示视频已处理完毕：
<img src="https://qcloudimg.tencent-cloud.cn/raw/888c67023a08461ea531afcae13023b2.png" width="" />
4. 单击视频“操作”栏下的 **管理**，进入管理页面：
 - 选择“基本信息”页签，可以看到生成的封面，以及 DRM 加密的自适应码流输出（模板 ID 为11和13）。

   ![image-20220426201159056](https://qcloudimg.tencent-cloud.cn/raw/2586f2a04f6339c91c876529f03e2523.png)

 - 选择“截图信息”页签，可以看到生成的雪碧图（模板 ID 为10）。

   ![image-20220426201309975](https://qcloudimg.tencent-cloud.cn/raw/25733f3f9e69eeb88b724d013a8464ca.png)

## 步骤3：生成播放器签名

播放器签名，用于后续查询播放信息，生成方式请参考 [播放器签名文档](https://cloud.tencent.com/document/product/266/45554) 。 本教程的播放器签名的 PayLoad 如下：

```json
{
  "appId": 1500014561,
  "fileId": "387702304941991610",
  "currentTimeStamp": 1661163373,
  "expireTimeStamp": 2648557919,
  "pcfg":"advanceDrmPreset"
}
```

本教程的 Key 为 `vodtestkey`时，生成的播放器签名（`psign`）如下：

`eyJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6MTUwMDAxNDU2MSwiZmlsZUlkIjoiMzg3NzAyMzA0OTQxOTkxNjEwIiwiY3VycmVudFRpbWVTdGFtcCI6MTY2MTE2MzM3MywiZXhwaXJlVGltZVN0YW1wIjoyNjQ4NTU3OTE5LCJwY2ZnIjoiYWR2YW5jZURybVByZXNldCJ9.rEZLhjgsoLc2htIUI_HckxvhVmdBhQyf5d-2Kku1JeA`

## 步骤4：使用播放器播放 DRM 加密视频。

### Web 端

#### 使用点播播放器播放

您只需在初始化播放器时传入必要的播放文件参数即可播放 DRM 加密视频。


#### step 1：在页面中引入文件

在适当的地方引入播放器样式文件与相关脚本文件：

```
<link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/tcplayer.min.css" rel="stylesheet"/>
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 Webrtc 视频，需要在 tcplayer.vx.x.x.min.js 之前引入 TXLivePlayer-x.x.x.min.js。-->
 <!--有些浏览器环境不支持 Webrtc，播放器会将 Webrtc 流地址自动转换为 HLS 格式地址，因此快直播场景同样需要引入hls.min.x.xx.xm.js。-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/libs/TXLivePlayer-1.2.3.min.js"></script>
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 协议的视频，需要在 tcplayer.vx.x.x.min.js 之前引入 hls.min.x.xx.xm.js。-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/libs/hls.min.1.1.5.js"></script>
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 FLV 格式的视频，需要在 tcplayer.vx.x.x.min.js 之前引入 flv.min.x.x.x.js。-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/libs/flv.min.1.6.3.js"></script>
  <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 DASH 视频，需要在 tcplayer.vx.x.x.min.js 之前引入 dash.min.x.x.x.js。-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/libs/dash.all.min.4.4.1.js"></script>
 <!--播放器脚本文件-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.4/tcplayer.v4.5.4.min.js"></script>
```

#### step 2：放置播放器容器

在需要展示播放器的页面位置加入播放器容器，代码如下：

```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playsinline>
</video>
```

> ? 容器 ID 以及宽高都可以自定义。

#### step 3：初始化代码

在页面初始化的代码中加入以下初始化脚本，传入必须的初始化参数（其中包含步骤3中生成的播放器签名`psign`），代码如下：

```
var player = TCPlayer('player-container-id', {
    appID: '1500014561', // 请传入点播账号的appID (必须)
    fileID: '387702304941991610', // 请传入需要播放的视频filID (必须)
    psign: 'eyJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6MTUwMDAxNDU2MSwiZmlsZUlkIjoiMzg3NzAyMzA0OTQxOTkxNjEwIiwiY3VycmVudFRpbWVTdGFtcCI6MTY2MTE2MzM3MywiZXhwaXJlVGltZVN0YW1wIjoyNjQ4NTU3OTE5LCJwY2ZnIjoiYWR2YW5jZURybVByZXNldCJ9.rEZLhjgsoLc2htIUI_HckxvhVmdBhQyf5d-2Kku1JeA',
    // 其他参数请在开发文档中查看 https://cloud.tencent.com/document/product/266/63004
});
```

### iOS 端

请参考 [接入指引](https://cloud.tencent.com/document/product/266/73872#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE)（通过 FileId 方式）播放 DRM 加密视频。其中，这一过程中需要使用到步骤3中生成的播放器签名`psign`。

> ? 在接入前，请您提交工单[联系我们](https://console.cloud.tencent.com/workorder/category)获取支持 DRM 功能的 SDK 。

![](https://qcloudimg.tencent-cloud.cn/raw/28a39832d9f3247c40dd37c3b3c668ae.png)

### Android 端

请参考 [接入指引](https://cloud.tencent.com/document/product/266/73865#.E6.AD.A5.E9.AA.A45.EF.BC.9A.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE) （通过 FileId 方式）播放 DRM 加密视频。其中，这一过程中需要使用到步骤3中生成的播放器签名`psign`。

> ? 在接入前，请您提交工单[联系我们](https://console.cloud.tencent.com/workorder/category)获取支持 DRM 功能的 SDK 。

![](https://qcloudimg.tencent-cloud.cn/raw/a431cfa2a3ce7b4035703c4da984ff5c.png)

## 总结

学习本教程后，您已经掌握如何对视频进行 DRM 加密，并使用播放器播放加密后的视频。

> ? 在您对接 DRM 或者华曦达的过程中的任何问题，都可以提工单[联系我们](https://console.cloud.tencent.com/workorder/category)，我们全程负责帮您解决。
