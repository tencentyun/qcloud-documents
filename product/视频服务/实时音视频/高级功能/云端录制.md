商用的音视频解决方案考虑到取证、质检、审核和存档等场景，可能会有录制的需求。实时音视频服务使用 [云直播](https://cloud.tencent.com/document/product/267) 服务的能力为您提供全程的云端录制功能，录制下来的文件可以通过 [云点播](https://cloud.tencent.com/document/product/266) 平台获取。

![](https://main.qcloudimg.com/raw/9768ef2cb4f6df10be8c654c0a9c8f4d.gif)

>?
>- 云端录制功能默认关闭，启用云端录制功能需要先开通 [云直播](https://console.cloud.tencent.com/live) 和 [云点播](https://console.cloud.tencent.com/vod) 服务。
>- 如果您使用了云端录制功能，将会产生云直播服务的录制费和云点播服务的存储费，如需播放或下载录制的视频文件，还会产生云点播服务的流量费（视频加速），详细计费规则请查阅 [云端录制相关费用](https://cloud.tencent.com/document/product/647/32574#.E4.BA.91.E7.AB.AF.E5.BD.95.E5.88.B6.E7.9B.B8.E5.85.B3.E8.B4.B9.E7.94.A8) 文档。 

## 平台支持

|   iOS    | Android  |  Mac OS  | Windows  | 微信小程序 | Chrome 浏览器 |
| :------: | :------: | :------: | :------: | :--------: | :----------: |
| &#10003; | &#10003; | &#10003; | &#10003; |  &#10003;  |   &#10003;   |

## 开启云端录制

1. 确认 [云直播](https://console.cloud.tencent.com/live) 和 [云点播](https://console.cloud.tencent.com/vod) 服务均已开通。
2. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc) ，进入【应用管理】页面，确认【旁路直播】处于“可用”状态。若【旁路直播】处于“不可用”状态，可单击应用列表右侧的【功能配置】后在对应设置页面中开启。
3. 在【应用管理】页面，单击【全局云端录制配置】，开启【全局云端自动录制】，并设置录制文件的格式。
   ![](https://main.qcloudimg.com/raw/d12676d282b1890dd39cd2de743dda7d.png)
    开启全局云端自动录制后，当前腾讯云账号下所有实时音视频应用自动录制的视频格式都会保存为您配置的储存格式。

## 混合画面

实时音视频的音视频房间默认不开启混流功能，开启云端录制功能后，默认只能录制 TRTC 房间里的每一路（主路和辅路）上行的视频。如果想要录制混合后的画面，您需要使用 [云端混流转码](https://cloud.tencent.com/document/product/647/16827)，即调用 TRTCCloud 的 `setMixTranscodingConfig` 接口便可将混合画面的视频录制成一个独立的文件。

## 获取视频文件


### 方案一：控制台查找

您可以在云点播控制台的 [视频管理](https://console.cloud.tencent.com/vod/media) 界面中查找到录制下来的视频文件。我们以腾讯云官网的 [Demo](https://cloud.tencent.com/document/product/647/17021) 为例，具体操作过程如下：

1. 腾讯云官网 Demo 所属账号的云直播 bizid 为3891，您可以在 [实时音视频控制台](https://console.cloud.tencent.com/rav) > 【应用管理】>【应用信息】>【旁路直播信息】中查询到该 bizid。
2. 用 Demo 创建一个直播间，ID 为 `12345`，用户名为 `userA`，可以计算出该房间对应的直播流 ID 为 `MD5(12345_userA_main)`，即`3891_8d0261436c375bb0dea901d86d7d70e8`。具体的计算方法可以参考文档 [CDN 旁路直播](https://cloud.tencent.com/document/product/647/16826) 中关于获取直播地址的说明。
3. 退出直播间，在点播控制台的 [视频管理](https://console.cloud.tencent.com/vod/media) 界面中直接找到该文件，或用直播流 ID 进行前缀搜索找到该文件，如下图：
   ![](https://main.qcloudimg.com/raw/c3a528e622bea92da8aa1f58ca7d57cc.png)



### 方案二：REST API 查找

您可以调用云点播服务提供的 REST API [SearchMedia 接口](https://cloud.tencent.com/document/product/266/31813) 并指定其 StreamId 参数，查找录制文件。StreamId（即直播流 ID）的获取方式请参见 [CDN 旁路直播](https://cloud.tencent.com/document/product/647/16826) 中关于获取直播地址的说明。
