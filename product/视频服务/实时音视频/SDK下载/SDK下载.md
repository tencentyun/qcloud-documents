TRTC 是腾讯云 LiteAV 系列产品之一，由于 LiteAV 体系的 SDK 都使用了相同的基础模块，如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题。因此我们为您提供集成了不同产品能力的**精简版（TRTC）**、**专业版（Professional）**和**企业版（Enterprise）**，您可以根据实际业务需要选择不同的版本。

以下视频将为您介绍各个版本 SDK 的功能差别：   
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2497-42188?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>
   
<h2 id="TRTC">精简版（TRTC）</h2>  
精简版仅包含 TRTC 和直播播放（TXLivePlayer）两项功能，对 App 的安装包体积增量最小，适合仅使用 TRTC 相关功能的客户。
 
<table>  
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px"  style="text-align:center">Github</td>
      <th width="0px" style="text-align:center">Gitee</td>
      <th width="0px" style="text-align:center">Demo 运行说明</td>
      <th width="0px" style="text-align:center">SDK 集成指引</td>
      <th width="0px" style="text-align:center">安装包增量</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_ios_trtc") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32396">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32173">DOC</a></td>
      <td style="text-align:center">3M（arm64）</td>
   </tr>
     <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_android_trtc") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32166">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32175">DOC</a></td>
      <td style="text-align:center">jar：546K<br> so（armeabi）：4.5M<br> so（armv7）：4.5M<br>so（arm64）：5.3M</td>
   </tr>
     <tr>
      <td style="text-align:center">Windows(C++)  </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_cplusplus_trtc") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32397">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32178">DOC</a></td>
      <td style="text-align:center">12.7M（C++ x86）<br>15.6M（C++ x64）</td>
   </tr>
     <tr>
      <td style="text-align:center">Windows(C#) </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_csharp_trtc") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32397">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32178">DOC</a></td>
      <td style="text-align:center">13.8M（C# x64）<br>13.3M（C# x86）</td>
   </tr>
     <tr>
      <td style="text-align:center">Mac</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_mac_trtc") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32396">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32176">DOC</a></td>
      <td style="text-align:center">2.05M（arm64）</td>
   </tr>
     <tr>
      <td style="text-align:center">Web</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_web_trtc") href="https://web.sdk.qcloud.com/trtc/webrtc/download/webrtc_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32398">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/16863">DOC</a></td>
      <td style="text-align:center">N/A</td>
   </tr>
   <tr>
      <td style="text-align:center">Electron  </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_electron_trtc") href="https://web.sdk.qcloud.com/trtc/electron/download/TXLiteAVSDK_TRTC_Electron_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/38548">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/38549">DOC</a></td>
      <td style="text-align:center">N/A</td>
   </tr>
   <tr>
      <td style="text-align:center">微信小程序 </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_wxmini_trtc") href="https://web.sdk.qcloud.com/trtc/miniapp/download/trtc-wx.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/TRTCSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32399">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32183">DOC</a></td>
      <td style="text-align:center">N/A</td>
</tr>
<tr>
      <td style="text-align:center">Flutter</td>
      <td style="text-align:center"><a href="https://pub.dev/packages/tencent_trtc_cloud/versions">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/c1avie/trtc_demo">Github</a></td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/51601">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/51602">DOC</a></td>
      <td style="text-align:center">N/A</td>
</tr>
<tr>
      <td style="text-align:center">React Native</td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/TRTCReactNative">Github</a></td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/63790">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/63791">DOC</a></td>
      <td style="text-align:center">N/A</td>
</tr>
</table>

>? 
> - 如需减少 SDK 带来的安装包体积增量请参考 [如何缩减安装包体积](https://cloud.tencent.com/document/product/647/34400)。
> - 扫码关注公众号，了解 SDK 的版本更新以及最新的技术动态。
> ![](https://main.qcloudimg.com/raw/d8a8c8c130ef7799feff6efbc0260ea2.jpg)


<h2 id="Professional">专业版（Professional）</h2>

专业版集合了包含 TRTC 在内的多个音视频相关的核心功能，包括 [超级播放器（Player+）](https://cloud.tencent.com/product/player)、[移动直播（MLVB）](https://cloud.tencent.com/product/mlvb) 和 [短视频（UGSV）](https://cloud.tencent.com/product/ugsv) 等，由于底层模块的高度复用，集成专业版的体积增量要小于同时集成两个独立的 SDK，并且可以避免符号冲突（symbol duplicate）的困恼。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px"  style="text-align:center">Github</td>
      <th width="0px" style="text-align:center">64位支持</td>      
      <th width="0px" style="text-align:center">Demo 运行说明</td>
      <th width="0px" style="text-align:center">SDK 集成指引</td>
      <th width="0px" style="text-align:center">安装包增量</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_ios_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32396">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32173">DOC</a></td>
      <td style="text-align:center">3.2M（arm64）</td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_android_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32166">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32175">DOC</a></td>
      <td style="text-align:center">jar：1M<br> so（armeabi）：5.7M<br> so（armv7）：5.7M<br>so（arm64）：6.8M</td>
   </tr>
</table>

>? 
>- Windows 和 Mac 版本的 SDK 暂时只有一个版本，没有做精简版、专业版和企业版的区分。
>- 由于 LiteAV 体系的 SDK 都使用了相同的基础模块，如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题，解决方法是只集成一个专业版的 LiteAVSDK。
>- 如需减少 SDK 带来的安装包体积增量请参考 [如何缩减安装包体积](https://cloud.tencent.com/document/product/647/34400)。


<h2 id="Enterprise">企业版（Enterprise）</h2>

企业版除包含专业版的所有功能以外，还集成了 AI 美颜特效组件，支持大眼、瘦脸、美容和动效贴纸、挂件等 AI 美颜特效能力。AI 美颜特效属于增值服务，由 [美颜特效 SDK](https://cloud.tencent.com/document/product/616) 收取相关费用，计费详情请参见 [美颜特效 SDK 价格总览](https://cloud.tencent.com/document/product/616/36807)。企业版下载后需要美颜特效 SDK 的解压密码和授权 License 才能运行，解码密码和授权 License 请根据 [美颜特效 SDK 购买流程](https://cloud.tencent.com/document/product/616/11235) 获取。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">Demo 运行说明</td>
      <th width="0px" style="text-align:center">SDK 集成指引</td>
      <th width="0px" style="text-align:center">安装包增量</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_ios_enterprise") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Enterprise_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32396">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32173">DOC</a></td>
      <td style="text-align:center"> 5.5M（arm64）</td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("trtc_sdk_download_android_enterprise") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Enterprise_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32166">DOC</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32175">DOC</a></td>
      <td style="text-align:center"> jar：2.2M<br>so(armeabi)：9.3M</td>
   </tr>
</table>

>?
>- Windows 和 Mac 版的 SDK 暂无 AI 美颜特效组件，没有做精简版、专业版和企业版的区分。
>- 如需减少 SDK 带来的安装包体积增量请参考 [如何缩减安装包体积](https://cloud.tencent.com/document/product/647/34400)。


## 各版本差异对照表

![](https://main.qcloudimg.com/raw/76d9d6f854ba4cc8cf3b3c18ed230a35.png)

<table>
  <tr>
    <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/7873">直播基础版</a><br>LiteAV_Smart</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/584/9366">短视频版</a><br>LiteAV_UGC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32689">TRTC版</a><br>LiteAV_TRTC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/881/20205">播放器版</a><br>LiteAV_Player</th>
    <th width="100px" style="text-align:center"><a href="#Professional">专业版</a><br>Professional</th>
    <th width="100px" style="text-align:center"><a href="#Enterprise">企业版</a><br>Enterprise</th>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">摄像头推流</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">录屏推流</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 协议</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">HTTP - FLV</td>
    <td style="text-align:center">&#10003;</td>
     <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">点播播放</td>
    <td style="text-align:center">MP4 格式</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">DRM 加密</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">美颜滤镜</td>
    <td style="text-align:center">基础美颜</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">基础滤镜</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">连麦互动</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">跨房 PK</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">视频通话</td>
    <td style="text-align:center">双人通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">视频会议</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">“抖音”特效</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='4' style="text-align:center">AI 美颜特效</td>
    <td style="text-align:center">大眼瘦脸</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">V 脸隆鼻</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">动效贴纸</td>
   <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">绿幕抠图</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
</table>


<script>
  var _mtac = {"senseHash":0};
  (function() {
    var mta = document.createElement("script");
    mta.src = "//pingjs.qq.com/h5/stats.js?v2.0.4";
    mta.setAttribute("name", "MTAH5");
    mta.setAttribute("sid", "500695331");
    mta.setAttribute("cid", "500695332");
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(mta, s);
  })();
</script>

