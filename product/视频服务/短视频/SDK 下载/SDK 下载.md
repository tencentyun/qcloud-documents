>?扫码关注公众号，了解 SDK 的版本更新以及最新的技术动态。
![](https://main.qcloudimg.com/raw/23242df893a3ecb11779a59ed9a5629c.jpg)

短视频 SDK 提供3种版本的 SDK，了解3个版本 SDK 的关系和对应的 License 使用请参见 [功能说明文档]()。

<h2 id="Smart">基础版（UGC）</h2>

基础版仅包含短视频采集、编辑和点播播放功能，对 App 的安装包体积增量最小，适合仅使用短视频相关功能的客户。

<table>
   <tr>
      <th>所属平台</td>
      <th>ZIP 包</td>
   </tr>
   <tr>
      <td style="text-align:center">iOS</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_smart") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Smart_iOS_latest.zip">DOWNLOAD</a></td>
   </tr>
     <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_smart") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Smart_Android_latest.zip">DOWNLOAD</a></td>
   </tr>

</table>

<h2 id="Professional">专业版（Professional）</h2>

专业版包含移动直播在内的多个音视频相关的核心功能，分别为 [实时音视频（TRTC）](https://cloud.tencent.com/product/trtc)、[超级播放器（Player+）](https://cloud.tencent.com/product/player)和 [短视频（UGSV）](https://cloud.tencent.com/product/ugsv)等，由于底层模块的高度复用，集成专业版的体积增量要小于同时集成两个独立的 SDK，并且可以避免符号冲突（symbol duplicate）的困扰。

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_professional") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">4.08M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_professional") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M<br> so(armeabi)：6.5M<br> so(armv7)：6.1M<br>so(arm64)：7.3M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

>? 根据您具体使用的服务，使用专业版需先购买对应的产品授权，您可按需选购：
>- 使用移动直播请购买  [移动直播 License](https://cloud.tencent.com/document/product/454/34750#buy)。
>- 使用短视频请购买 [短视频 License](https://cloud.tencent.com/document/product/584/20333#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license)。
>- 使用实时音视频请购买 [实时音视频套餐包](https://cloud.tencent.com/document/product/647/37097)。

<h2 id="Enterprise">企业版（Enterprise）</h2>

企业版不仅包含专业版的所有功能，还集成了一套 AI 特效组件，支持大眼、瘦脸、美容和动效贴纸挂件等能力，下载后需要解压密码和授权 License 才能运行，解码密码和授权 License 请联系 [腾讯云商务](https://cloud.tencent.com/apply/p/h1qsz5vhvko) 获取。

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_ios_enterprise") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Enterprise_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> 6.15M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("mlvb_sdk_download_android_enterprise") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Enterprise_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> jar：2.3M<br>so(armeabi)：20.4M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

>! 动效贴纸、AI 抠图、美妆特效和手势动作特效需要通过额外的素材解锁功能。

## 各版本差异对照表
<img src="https://main.qcloudimg.com/raw/744b80d1c15efaddb50ff11ffeea0f6e.png" width="1100">

<table>
  <tr>
    <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
    <th width="100px" style="text-align:center"><a href="#Smart">直播基础版</a><br>LiteAV_Smart</th>
    <th width="100px" style="text-align:center">短视频版<br>LiteAV_UGC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32689">TRTC 版</a><br>LiteAV_TRTC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/881/20205">播放器版</a><br>LiteAV_Player</th>
    <th width="100px" style="text-align:center"><a href="#Professional">专业版</a><br>Professional</th>
    <th width="100px" style="text-align:center"><a href="#Enterprise">企业版</a><br>Enterprise</th>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">摄像头推流</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
   <tr>
    <td style="text-align:center">录屏推流</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 协议</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">HTTP - FLV</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">点播播放</td>
    <td style="text-align:center">MP4 格式</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
   <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
   <tr>
    <td style="text-align:center">DRM 加密</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">美颜滤镜</td>
    <td style="text-align:center">基础美颜</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">基础滤镜</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">连麦互动</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">跨房 PK</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">视频通话</td>
    <td style="text-align:center">双人通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">视频会议</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">“抖音”特效</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td rowspan='4' style="text-align:center">AI 特效</td>
    <td style="text-align:center">大眼瘦脸</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">V 脸隆鼻</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">动效贴纸</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
  </tr>
  <tr>
    <td style="text-align:center">绿幕抠图</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003</td>
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


