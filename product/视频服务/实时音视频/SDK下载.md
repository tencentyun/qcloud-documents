<h2 id="TRTC">精简版（TRTC）</h2>

精简版体积最小，适合仅集成 TRTC 实时音视频功能的客户。


| 所属平台 |  ZIP 包下载 | Github 下载 | 国内镜像 |  Demo 运行说明 | SDK 集成指引 | 64位支持 | 安装包增量 |
|:---------:| :---------:| :--------:| :--------:| :--------:| :--------:| :--------:|:--------:|
| iOS | [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_iOS_latest.zip) | [Github](https://github.com/tencentyun/TRTCSDK)|[Gitee](https://gitee.com/cloudtencent/TRTCSDK)| [DOC](https://cloud.tencent.com/document/product/647/32396)| [DOC](https://cloud.tencent.com/document/product/647/32173) |支持|1.90M（arm64）|
| Android | [AAR](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.aar)<br>[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Android_latest.zip) | [Github](https://github.com/tencentyun/TRTCSDK)|[Gitee](https://gitee.com/cloudtencent/TRTCSDK) | [DOC](https://cloud.tencent.com/document/product/647/32166)| [DOC](https://cloud.tencent.com/document/product/647/32175) |支持| jar：820K<br> so(armeabi)：5.1M<br> so(armeabi-v7a)：4.8M<br>so(arm64-v8a)：5.7M |
| Windows(C++)| [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip) | [Github](https://github.com/tencentyun/TRTCSDK)| [Gitee](https://gitee.com/cloudtencent/TRTCSDK)| [DOC](https://cloud.tencent.com/document/product/647/32397)| [DOC](https://cloud.tencent.com/document/product/647/32178) |支持| 12.7M（C++ x86）<br>15.6M（C++ x64）|
| Windows(C#)| [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip) | [Github](https://github.com/tencentyun/TRTCSDK)| [Gitee](https://gitee.com/cloudtencent/TRTCSDK) | [DOC](https://cloud.tencent.com/document/product/647/32397)| [DOC](https://cloud.tencent.com/document/product/647/32178) | - | 13.3M（C# x86）|
| Mac| [TAR](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2) | [Github](https://github.com/tencentyun/TRTCSDK) | [Gitee](https://gitee.com/cloudtencent/TRTCSDK) | [DOC](https://cloud.tencent.com/document/product/647/32396)| [DOC](https://cloud.tencent.com/document/product/647/32176) |支持| 2.05M（arm64）|
| Web |  -  | [GitHub](https://github.com/tencentyun/TRTCSDK)|  [Gitee](https://gitee.com/cloudtencent/TRTCSDK) | [DOC](https://cloud.tencent.com/document/product/647/32398)| [DOC](https://cloud.tencent.com/document/product/647/16863) | - | -|
| 微信小程序 |  - | [GitHub](https://github.com/tencentyun/TRTCSDK) |  [Gitee](https://gitee.com/cloudtencent/TRTCSDK) | [DOC](https://cloud.tencent.com/document/product/647/32399)| [DOC](https://cloud.tencent.com/document/product/647/32183) |  - | -|

>? 阅读文档 [如何缩减安装包体积](https://cloud.tencent.com/document/product/647/34400) 了解如何减少 SDK 带来的安装包体积增量。

<h2 id="Professional">专业版（Professional）</h2>

TRTC SDK 是隶属于腾讯视频云 LiteAV 框架下的一款终端产品，我们基于 LiteAV 框架还研发了 [超级播放器 SDK](https://cloud.tencent.com/product/player)、[移动直播 SDK](https://cloud.tencent.com/product/mlvb) 和 [短视频 SDK](https://cloud.tencent.com/product/ugsv) 等其他终端产品。

由于 LiteAV 体系的 SDK 都使用了相同的基础模块，如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题。

要避免符号冲突问题，正确的做法是不要同时集成两个 SDK，而是集成一个具备完整功能的专业版 SDK：

| 所属平台 |  ZIP 包下载 | Github 下载 | 64位支持 | 安装包增量 |
|:---------:| :---------:| :--------:| :--------:|:--------:|
| iOS | [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.6/TXLiteAVSDK_Professional_iOS_6.6.7460.zip) | [Github](hhttps://github.com/tencentyun/LiteAVProfessional_iOS) | 支持 | 4.08M（arm64）|  [DOC](https://cloud.tencent.com/document/product/647/34400) |
| Android | [AAR](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.6/LiteAVSDK_Professional_6.6.7458.aar)<br>[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.6/LiteAVSDK_Professional_6.6.7458.zip) | [Github](https://github.com/tencentyun/LiteAVProfessional_Android) | 支持 | jar：1.5M<br> so(armeabi)：6.5M<br> so(armeabi-v7a)：6.1M<br>so(arm64-v8a)：7.3M| [DOC](https://cloud.tencent.com/document/product/647/34400) |

>? Windows 和 Mac 版本的 SDK 暂时只有一个版本，没有做精简版、专业版和企业版的区分。


<h2 id="Enterprise">企业版（Enterprise）</h2>

LiteAVSDK 的企业版，除了包含专业版的所有功能以外，还集成了一套 AI 特效组件，支持大眼、瘦脸、美容和动效贴纸挂件等能力，下载后需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。

| 所属平台 | ZIP 包下载 | 64位支持 | 安装包增量 | 安装包瘦身|
|:---------:| :--------:| :--------:|:--------:|:--------:|
| iOS | [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.6/TXLiteAVSDK_Enterprise_iOS_6.6.7460.zip) |支持 | 6.15M（arm64）|  [DOC](https://cloud.tencent.com/document/product/647/34400) |
| Android | [ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.6/LiteAVSDK_Enterprise_6.6.7458.zip) | 支持 |  jar：2.3M；so(armeabi)：20.4M |[DOC](https://cloud.tencent.com/document/product/647/34400) |

>? Windows 和 Mac 版的 SDK 暂无 AI 特效组件，没有做精简版、专业版和企业版的区分。

## 各版本差异对照表

![](https://main.qcloudimg.com/raw/76d9d6f854ba4cc8cf3b3c18ed230a35.png)

<table>
  <tr>
	  <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
    <th width="100px" style="text-align:center">直播精简版<br>LiteAV_Smart</th>
    <th width="100px" style="text-align:center">短视频版<br>LiteAV_UGC</th>
    <th width="100px" style="text-align:center">TRTC版<br>LiteAV_TRTC</th>
		<th width="100px" style="text-align:center">播放器版<br>LiteAV_Player</th>
		<th width="100px" style="text-align:center">专业版<br>Professional</th>
		<th width="100px" style="text-align:center">企业版<br>Enterprise</th>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">摄像头推流</td>
		<td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	 <tr>
    <td style="text-align:center">录屏推流</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 协议</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">HTTP - FLV</td>
    <td style="text-align:center">✔</td>
     <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='3' style="text-align:center">点播播放</td>
    <td style="text-align:center">MP4 格式</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	 <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	 <tr>
    <td style="text-align:center">DRM 加密</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">美颜滤镜</td>
    <td style="text-align:center">基础美颜</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">基础滤镜</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">连麦互动</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">跨房 PK</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
	  <td rowspan='2' style="text-align:center">视频通话</td>
    <td style="text-align:center">双人通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">视频会议</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">“抖音”特效</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">AI 特效</td>
    <td style="text-align:center">大眼瘦脸</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">V 脸隆鼻</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">动效贴纸</td>
   <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">绿幕抠图</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">✔</td>
  </tr>
</table>
