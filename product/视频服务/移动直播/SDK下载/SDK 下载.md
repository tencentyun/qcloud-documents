<h2 id="Smart">直播基础版（Smart）</h2>

直播基础版体积最小，适合仅集成移动直播相关功能的客户。

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("smart_ios_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Smart_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/7876">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">1.27M（arm64）</td>
   </tr>
     <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("smart_android_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Smart_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/7877">DOC</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M <br> so(armeabi)：4.4M <br>so(armeabi-v7a)：4.1M <br>so(arm64-v8a)：4.9M</td>
   </tr>
   <tr>
      <td style="text-align:center">微信小程序 </td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("smart_wxmini_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/MLVB_WXMini_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/MLVBSDK">Github</a></td>
      <td style="text-align:center"><a href="https://gitee.com/cloudtencent/MLVBSDK">Gitee</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/12554">DOC</a></td>
      <td style="text-align:center">N/A</td>
      <td style="text-align:center">N/A</td>
   </tr>
</table>

<h2 id="Professional">专业版（Professional）</h2>

移动直播 SDK 是隶属于腾讯视频云 LiteAV 框架下的一款终端产品，我们基于 LiteAV 框架还研发了 [实时音视频 SDK](https://cloud.tencent.com/product/trtc)、 [超级播放器 SDK](https://cloud.tencent.com/product/player) 和 [短视频 SDK](https://cloud.tencent.com/product/ugsv) 等其他终端产品。

如果您的项目中同时集成了两款以上的 LiteAV 体系的 SDK，就会出现符号冲突（symbol duplicate）的问题，这是由于 LiteAV 体系的 SDK 都使用了相同的基础模块。

要避免符号冲突问题，正确的做法是不要同时集成两个 SDK，而是集成一个具备完整功能的专业版 SDK：

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("professional_ios_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_iOS">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">4.08M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("professional_android_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Professional_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center"><a href="https://github.com/tencentyun/LiteAVProfessional_Android">Github</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center">jar：1.5M<br> so(armeabi)：6.5M<br> so(armv7)：6.1M<br>so(arm64)：7.3M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

<h2 id="Enterprise">商业版（Enterprise）</h2>

LiteAV SDK 的商业版，除了包含专业版的所有功能以外，还集成了一套 AI 特效组件，支持大眼、瘦脸、美容和动效贴纸挂件等能力，下载后需要解压密码和授权 License 才能运行，解码密码和授权 License 请联系腾讯云商务获取。

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
      <td style="text-align:center"><a onclick=MtaH5.clickStat("enterprise_ios_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Enterprise_iOS_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> 6.15M（arm64）</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
   <tr>
      <td style="text-align:center">Android</td>
      <td style="text-align:center"><a onclick=MtaH5.clickStat("enterprise_android_zip_download") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_Enterprise_Android_latest.zip">DOWNLOAD</a></td>
      <td style="text-align:center">支持</td>
      <td style="text-align:center"> jar：2.3M；so(armeabi)：20.4M</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/34400">DOC</a></td>
   </tr>
</table>

## 各版本差异对照表

![](https://main.qcloudimg.com/raw/76d9d6f854ba4cc8cf3b3c18ed230a35.png)

<table>
  <tr>
    <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
    <th width="100px" style="text-align:center"><a href="#Smart">直播基础版</a><br>LiteAV_Smart</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/584/9366">短视频版</a><br>LiteAV_UGC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/647/32689">TRTC版</a><br>LiteAV_TRTC</th>
    <th width="100px" style="text-align:center"><a href="https://cloud.tencent.com/document/product/881/20205">播放器版</a><br>LiteAV_Player</th>
    <th width="100px" style="text-align:center"><a href="#Professional">专业版</a><br>Professional</th>
    <th width="100px" style="text-align:center"><a href="#Enterprise">商业版</a><br>Enterprise</th>
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


<script>
  var _mtac = {};
  (function() {
    var mta = document.createElement("script");
    mta.src = "//pingjs.qq.com/h5/stats.js?v2.0.4";
    mta.setAttribute("name", "MTAH5");
    mta.setAttribute("sid", "500695331");
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(mta, s);
  })();
</script>