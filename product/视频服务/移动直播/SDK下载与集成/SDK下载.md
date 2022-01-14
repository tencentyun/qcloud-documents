移动直播 SDK 提供了4种版本的 SDK，可以按照下表选择适合您的版本：


| 版本 | 功能 |
|---------|---------|
| [基础直播 Smart](#Smart) | 支持直播推流、直播播放和基础美颜（美白、磨皮等）功能。|
| [互动直播 Live](#Live) | 在 [基础直播 Smart](#Smart) 之上增加了连麦功能。|
| [全功能版 ALL](#ALL) | 在 [互动直播 Live](#Live) 之上增加了 [实时音视频 SDK](https://cloud.tencent.com/product/trtc)、[超级播放器（Player+）](https://cloud.tencent.com/product/player)和 [短视频（UGSV）](https://cloud.tencent.com/product/ugsv)等 SDK。|
| [企业版 Enterprise](#Enterprise) | 在 [全功能版 ALL](#ALL) 之上增加了高级美颜特效能力。|

>? 更多版本特性能力请参考 [功能说明](https://cloud.tencent.com/document/product/454/19075)，也可以通过 [介绍视频](#Video) 来了解选择您所需要的版本。

[](id:Smart)
## 基础直播 Smart   

基础直播版仅包含直播推流（TXLivePusher）和直播播放（TXLivePlayer）两项功能，对 App 的安装包体积增量最小，适合仅使用移动直播相关功能的客户。 

>! 基础版的直播推流只支持 RTMP 推流，不支持 RTC 推流。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px"  style="text-align:center">Github</td>
      <th width="0px" style="text-align:center">Gitee</td>
      <th width="0px" style="text-align:center">SDK 集成指引</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">安装包增量</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_smart") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Smart_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/7876">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">1.27M（arm64）</td>
   </tr>
     <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_smart") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Smart_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/7877">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M <br> so(armeabi)：4.4M <br>so(armeabi-v7a)：4.1M <br>so(arm64-v8a)：4.9M</td>
   </tr>
   <tr>
      <td style="text-align:center">微信小程序 </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_wxmini_smart") href="https://liteavsdk-1252463788.cosgz.myqcloud.com/MLVB_WXMini_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/12554">DOC</a></td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center">N/A</td>
   </tr>
</table>

>? 扫码关注公众号，了解 SDK 的版本更新以及最新的技术动态。
>![](https://main.qcloudimg.com/raw/23242df893a3ecb11779a59ed9a5629c.jpg)

[](id:Live)
## 互动直播 Live

互动直播版包含**主播开播、主播观众连麦/主播跨房 PK** 和**直播观看**三个功能模块。互动直播 Live 是在基础直播 Smart 功能上同时支持基于 RTC 协议连麦，快速实现更加灵活、更低延时、更多人数的直播互动场景。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px" style="text-align:center">SDK 集成指引</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">安装包增量</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Live_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56986">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">so（arm64）：1.6M<br>so（armv7）：1.6M</td>
   </tr>
     <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Live_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56987">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：0.8M <br> so(armeabi)：6.2M <br>so(armeabi-v7a)：6.2M <br>so(arm64-v8a)：7.4M</td>
   </tr>
   <tr>
      <td style="text-align:center">微信小程序 </td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56990">DOC</a></td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center">N/A</td>
   </tr>
</table>

[](id:ALL)
## 全功能版 ALL

全功能版集合了包含移动直播在内的多个音视频相关的核心功能，这包括 [实时音视频 SDK](https://cloud.tencent.com/product/trtc)、[超级播放器（Player+）](https://cloud.tencent.com/product/player)和 [短视频（UGSV）](https://cloud.tencent.com/product/ugsv)等，由于底层模块的高度复用，集成全功能版的体积增量要小于同时集成两个独立的 SDK，并且可以避免符号冲突（symbol duplicate）的困恼。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px"  style="text-align:center">Github</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">安装包增量</td>
      <th width="0px" style="text-align:center">安装包瘦身</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">4.08M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_professional") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M<br> so(armeabi)：6.5M<br> so(armv7)：6.1M<br>so(arm64)：7.3M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

>? 根据您具体使用的服务，使用全功能版需先购买对应产品授权，您可按需选购：
>- 使用其中的移动直播请购买  [直播推流 License（原移动直播基础版 License）](https://cloud.tencent.com/document/product/454/8008#live_pag_price)。
>- 使用其中的短视频请购买 [短视频精简版/基础版 License](https://cloud.tencent.com/document/product/584/20333#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license)。
>- 使用其中的实时音视频请购买 [实时音视频套餐包](https://cloud.tencent.com/document/product/647/37097)。

[](id:Enterprise)
## 企业版 Enterprise

企业版除了包含全功能版的所有功能以外，还集成了一套 AI 特效组件，支持大眼、瘦脸、美容和动效贴纸挂件等能力。
下载企业版 SDK 后需要解压密码和授权 License 才能运行，获取解压密码和企业版 License，需要先 [申请企业版 License](https://cloud.tencent.com/product/x-magic)，或请 [联系腾讯云商务](https://cloud.tencent.com/apply/p/h1qsz5vhvko) 进行申请。

<table>
   <tr>
      <th width="0px" style="text-align:center">所属平台</td>
      <th width="0px" style="text-align:center">ZIP 包</td>
      <th width="0px" style="text-align:center">64位支持</td>
      <th width="0px" style="text-align:center">安装包增量</td>
      <th width="0px" style="text-align:center">安装包瘦身</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_enterprise") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Enterprise_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> 6.15M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_enterprise") href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Enterprise_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> jar：2.3M；so(armeabi)：20.4M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

>! 动效贴纸、AI抠图、美妆特效和手势动作特效需通过额外的素材来使用功能。

[](id:Video)
## 介绍视频
以下视频将为您介绍4个 SDK 之间的区别和各自的特点：

<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2343-35187?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>




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
   
