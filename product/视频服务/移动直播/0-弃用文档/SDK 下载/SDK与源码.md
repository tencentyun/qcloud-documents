<style>
table td { 
    height: 35px; 
    text-align:center;
    vertical-align:middle; 
}
.markdown-text-box img {
    border: 0;
    max-width: 100%;
    height: auto;
    box-sizing: content-box;
    box-shadow: 0 0 0px #ccc;
    margin: 0px 0;
}    
.markdown-text-box table td, .markdown-text-box table th {
    padding: 8px 13px;
    border: 1px solid #d9d9d9;
    word-wrap: break-word;
    text-align: center;
}    
</style>


## 特别提醒
[Demo](https://cloud.tencent.com/document/product/454/6555) 中展示的功能一般会领先 SDK 1周 - 2周时间，这段时间我们会用来进行 bugfix 和系统测试工作，所以部分 Demo 中的特性暂时在 SDK 中找不到对应的接口。

<h2 id="iOS"> iOS SDK（6.3.7088）</h2>

<table>
  <tr>
    <th width="120px" style="text-align:center">iOS SDK</th>
    <th width="220px" style="text-align:center">BitCode<br/>是否支持 BitCode<br/>（iOS 提供的体积优化方案）</th>
    <th width="220px" style="text-align:center">IPA 增量<br/>嵌入该版本后 IPA 安装包的体积增量</th>
    <th width="160px" style="text-align:center">Pod 安装<br/>基于 Pod 的 SDK 嵌入方式</th>
    <th width="160px" style="text-align:center">SDK 下载</th>
  </tr>
  <tr>
    <td style="text-align:center">直播精简版</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">1.43M</td>
    <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_livelite") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/6.3/TXLiteAVSDK_Smart_iOS_6.3.7088.zip">DOWNLOAD</a></td>
  </tr>
  <tr>
    <td style="text-align:center">全功能专业版</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">4.19M</td>
    <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_profession") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/6.3/TXLiteAVSDK_Professional_iOS_6.3.7088.zip">DOWNLOAD</a></td>
  </tr>
	<tr>
    <td style="text-align:center">商用企业版</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">5.98M</td>
    <td style="text-align:center">见版本说明</td>
    <td style="text-align:center">见下方说明</td>
  </tr>
</table>


>?**商用企业版**相比于专业版，增加了基于腾讯优图实验室专利技术的人脸特效功能。此版本非免费提供，下载地址为 [Enterprise(iOS).zip](https://liteavsdk-1252463788.cos.ap-guangzhou.myqcloud.com/6.3/TXLiteAVSDK_Enterprise_iOS_6.3.7095.zip)，下载后需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。
>商用企业版的使用方法请参考 [特效功能指引](https://cloud.tencent.com/document/product/454/9018)。

**iOS SDK功能介绍**
<table>
  <tr>
	  <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
		<th width="300px" style="text-align:center">功能简介</th>
    <th width="120px" style="text-align:center">直播精简版</th>
    <th width="120px" style="text-align:center">全功能专业版</th>
    <th width="120px" style="text-align:center">商用企业版</th>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">RTMP 推流</td>
		<td style="text-align:left">用于实现主播端的手机推流功能（美女直播）</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	 <tr>
    <td style="text-align:center">录屏推流</td>
		<td style="text-align:left">用于实现主播端的屏幕推流功能（游戏直播）</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 播放</td>
		<td style="text-align:left">用于实现 rtmp:// 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">FLV 播放</td>
		<td style="text-align:left">用于实现 HTTP+FLV 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS 播放</td>
		<td style="text-align:left">用于实现 HLS(m3u8) 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td style="text-align:center">点播播放</td>
    <td style="text-align:center">点播播放</td>
		<td style="text-align:left">用于实现视频点播回放（类似优酷）功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">美颜滤镜</td>
    <td style="text-align:center">基础美颜</td>
		<td style="text-align:left">提供自然、光滑等多种不同风格的美颜算法</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">基础滤镜</td>
		<td style="text-align:left">提供多套不同风格的滤镜算法</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">连麦互动</td>
		<td style="text-align:left">用于实现主播与观众之间的1vn视频连麦互动</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">主播 PK</td>
		<td style="text-align:left">用于实现主播与主播之间的1v1视频 PK</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:left">用于实现带美颜滤镜的拍照和视频录制功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:left">用于实现简单易用的视频裁剪和拼接功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">类“抖音”特效</td>
    <td style="text-align:left">用于实现类“抖音”的视频特效编辑功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:left">用于实现将视频上传到云端的功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">AI 特效</td>
    <td style="text-align:center">大眼瘦脸</td>
    <td style="text-align:left">基于天天P图 AI 特效实现五官实时美型功能</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">V脸隆鼻</td>
    <td style="text-align:left">基于天天P图 AI 特效实现五官实时美型功能</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">动效贴纸</td>
    <td style="text-align:left">基于人脸关键点定位的卡通贴纸</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">绿幕抠图</td>
    <td style="text-align:left">基于天天P图 AI 特效实现背景抠图能力</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
</table>

<h2 id="Android"> Android SDK（6.3.7089） </h2>

<table>
  <tr>
    <th width="200px" style="text-align:center">Android SDK</th>
    <th width="500px" style="text-align:center">SDK 下载<br/>zip 包中提供了 aar 和 jar+so 两种集成方案</th>
  </tr>
  <tr>
    <td style="text-align:center">直播精简版</td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_sdk_android_livelite") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/6.3/LiteAVSDK_Smart_Android_6.3.7089.zip">DOWNLOAD</a></td>
  </tr>
  <tr>
    <td style="text-align:center">全功能专业版</td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_sdk_android_profession") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/6.3/LiteAVSDK_Professional_Android_6.3.7089.zip">DOWNLOAD</a></td>
  </tr>
	<tr>
    <td style="text-align:center">商用企业版</td>
    <td style="text-align:center">见下方说明</td>
  </tr>
</table>

>?**商用企业版**相较于专业版，增加了基于腾讯优图实验室专利技术的人脸特效功能，此版本非免费提供，下载地址为 [Enterprise(Android).zip](http://liteavsdk-1252463788.cosgz.myqcloud.com/6.3/LiteAVSDK_Enterprise_Android_6.3.7089.zip)，下载后需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。
>商用企业版的使用方法请参考 [特效功能指引](https://cloud.tencent.com/document/product/454/9020)。

**Android SDK 功能介绍**
<table>
  <tr>
	  <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能项</th>
		<th width="300px" style="text-align:center">功能简介</th>
    <th width="120px" style="text-align:center">直播精简版</th>
    <th width="120px" style="text-align:center">全功能专业版</th>
    <th width="120px" style="text-align:center">商用企业版</th>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">RTMP 推流</td>
		<td style="text-align:left">用于实现主播端的手机推流功能（美女直播）</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
		<td style="text-align:center">✔</td>
  </tr>
	 <tr>
    <td style="text-align:center">录屏推流</td>
		<td style="text-align:left">用于实现主播端的屏幕推流功能（游戏直播）</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 播放</td>
		<td style="text-align:left">用于实现 rtmp:// 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">FLV 播放</td>
		<td style="text-align:left">用于实现 HTTP+FLV 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS 播放</td>
		<td style="text-align:left">用于实现 HLS(m3u8) 协议的直播播放功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td style="text-align:center">点播播放</td>
    <td style="text-align:center">点播播放</td>
		<td style="text-align:left">用于实现视频点播回放（类似优酷）功能</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">美颜滤镜</td>
    <td style="text-align:center">基础美颜</td>
		<td style="text-align:left">提供自然、光滑等多种不同风格的美颜算法</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">基础滤镜</td>
		<td style="text-align:left">提供多套不同风格的滤镜算法</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">连麦互动</td>
		<td style="text-align:left">用于实现主播与观众之间的1vn视频连麦互动</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">主播 PK</td>
		<td style="text-align:left">用于实现主播与主播之间的1v1视频 PK</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:left">用于实现带美颜滤镜的拍照和视频录制功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:left">用于实现简单易用的视频裁剪和拼接功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">类“抖音”特效</td>
    <td style="text-align:left">用于实现类“抖音”的视频特效编辑功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:left">用于实现将视频上传到云端的功能</td>
    <td></td>
    <td style="text-align:center">✔</td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
	  <td rowspan='4' style="text-align:center">AI 特效</td>
    <td style="text-align:center">大眼瘦脸</td>
    <td style="text-align:left">基于天天 P 图 AI 特效实现五官实时美型功能</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">V脸隆鼻</td>
    <td style="text-align:left">基于天天 P 图 AI 特效实现五官实时美型功能</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
	<tr>
    <td style="text-align:center">动效贴纸</td>
    <td style="text-align:left">基于人脸关键点定位的卡通贴纸</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
  <tr>
    <td style="text-align:center">绿幕抠图</td>
    <td style="text-align:left">基于天天 P 图 AI 特效实现背景抠图能力</td>
    <td></td>
    <td></td>
    <td style="text-align:center">✔</td>
  </tr>
</table>

<h2 id="Windows"> Windows SDK（3.2.0） </h2>

<table>
  <tr align="center">
    <th width="200px">功能特性</th>
    <th width="300px">ActiveX 插件</th>
    <th width="300px">C#（.NET）</th>
    <th width="300px">C++（DLL）</th>
  </tr>
  <tr align="center">
    <td>推流功能</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr align="center">
    <td>RTMP 播放</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr align="center">
    <td>视频通话</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr align="center">
    <td>对接要求</td>
    <td>具备网页开发经验</td>
    <td>具备 C#（.NET）开发经验</td>
    <td>具备 C++ 开发经验</td>
  </tr>
  <tr align="center">
    <td>开发环境</td>
    <td>记事本</td>
    <td>Visual Studio 2010</td>
    <td>Visual Studio 2015</td>
  </tr>
  <tr align="center">
    <td>版本日期</td>
    <td>3.0.1 @ 2018-05-21</td>
    <td>3.2.0 @ 2018-06-15</td>
    <td>3.2.1 @ 2018-06-15</td>
  </tr>
  <tr align="center">
    <td>下载地址</td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_activex_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/ActiveX/LiteAV_AX_SDK.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_csharp_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/CSharp/LiteAVSDK_Windows_C%23.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_cplusplus_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/Cpp/LiteAVSDK_Windows_C%2B%2B.zip">DOWNLOAD</a></td>
  </tr>
</table>

>?跟 OBS 的差异?
移动直播 SDK 相比于 OBS 功能较少，唯一的优势在于低延迟，配合 TXLivePlayer 的 RTMP_ACC 超低延时播放，可以将达到400ms以内的延迟效果。

<h2 id="XiaoChengXu">小程序源码（1.2.693）</h2>

<table width="850px">
  <tr align="center">
    <th width="120px">所属平台</th>
    <th width="80px">版本号</th>
    <th width="570px">说明</th>
    <th width="80px">下载链接</th>
  </tr>
  <tr align="center">
    <td>微信小程序</td>
    <td>1.2.693</td>
    <td>小程序 Demo “腾讯视频云” 的前后台源代码</a></td>
    <td><a onclick=MtaH5.clickStat("Wiki_Download_SDK_Xiaochengxu_RTCRoom") href="https://github.com/TencentVideoCloudMLVBDev/MiniProgram">wxlite</a></td>
  </tr>
</table>

 此套源码包含两个部分，**wxlite** 文件夹中的源码为小程序源码，**simpleserver** 文件夹中的源码为后台 node.js 源码，该套支持在腾讯云平台进行一键部署，使您能在5分钟时间里即拥有一个自己的调试环境，部署方法可参考 [源码调试](https://cloud.tencent.com/document/product/454/12554)。

<h2 id="PCWeb">Web（PC 端）源码（1.0.0）</h2>

| 所属平台 | 版本号 | 说明 | 下载链接 |
|---------|---------|---------|------|
| PC 浏览器 | 1.0.0| 源码实现了一个网页唤起 EXE 桌面程序，并跟小程序互通的简单 Demo，<br>可以用实现浏览器[（IE 或 Chrome）](https://cloud.tencent.com/document/product/454/17004) => TXCloudRoom.exe + 微信[（小程序）](https://cloud.tencent.com/document/product/454/16914) 的组合解决方案。 | [WebEXE](https://github.com/TencentVideoCloudMLVBDev/webexe_web.git) |

<h2 id="Server">服务端源码（1.1.0）</h2>
 
<table width="850px">
  <tr align="center">
    <th width="120px">下载项目</th>
    <th width="80px">版本号</th>
    <th width="570px">功能说明</th>
    <th width="80px">下载链接</th>
  </tr>
	<tr align="center">
    <td>计算安全签名</td>
    <td>1.1.0</td>
    <td style="vertical-align:middle; text-align:left;">用于计算 IM、LiveRoom、RTCRoom 以及 WebRTC 等方案中所需要使用的 UserSig 和 privateMapKey 签名，算法基于 ECDSA-SHA256 实现。 </a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_server_sign") href="https://github.com/TencentVideoCloudMLVBDev/sign_srv">JAVA & PHP & Node.js</a</td>
  </tr>
  <tr align="center">
    <td rowspan="2"> RoomService</td>
    <td rowspan="2">1.1.0</td>
    <td rowspan="2" style="vertical-align:middle; text-align:left;">RoomService 是 <a href="https://cloud.tencent.com/document/product/454/14606#Server">LiveRoom</a>（直播连麦）和 <a href="https://cloud.tencent.com/document/product/454/14617#Server">RTCRoom</a>（视频通话）的后台组件，源码下载后可部署于自己的业务服务器上。 </td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_server_java") href="https://github.com/TencentVideoCloudMLVBDev/roomservice_java
">JAVA</a</td>
  </tr>
	<tr align="center">
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_server_nodejs") href="https://github.com/TencentVideoCloudMLVBDev/MiniProgram/tree/master/server">Node.js</a</td>
  </tr>
<tr align="center">
    <td>示例房间列表</td>
    <td>1.1.0</td>
    <td style="vertical-align:middle; text-align:left;"> 实现了一个简单的（无鉴权的）视频房间列表，可以支持创建通话房间，关闭通话房间、心跳保活等功能，您可以参考它来实现课程列表、客服列表、会议列表等等。 </a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_server_webrtc") href="https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java">JAVA</a</td>
  </tr>
</table>

<h2 id="Xiaozhibo">小直播源码（6.3）</h2>

小直播是腾讯视频云终端产品中心打造的一款集各种功能（文字互动、弹幕消息、飘星点赞、美颜增白、动效蒙皮、连麦互动）于一体的开源 App，致力于帮您快速搭建自己的直播产品原型。您可以参考 [搭建指引](https://cloud.tencent.com/document/product/454/15187) 了解如何快速让下面的代码跑起来。

<table width="850px">
  <tr align="center">
    <th width="150px">所属平台</th>
    <th width="80px">版本号</th>
    <th width="550px">源码说明</th>
    <th width="80px">下载链接</th>
  </tr>
  <tr align="center">
    <td style="text-align:center">iOS 源码包</td>
    <td style="text-align:center">6.3</td>
    <td style="text-align:left">由 RTMP SDK 、IM SDK、COS SDK、业务逻辑层代码和界面层代码构成，源码阅读推荐参考 <a href="https://cloud.tencent.com/document/product/454/7894">iOS 代码说明</a></td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_xzb_ios_source") href="https://download-1252463788.cos.ap-shanghai.myqcloud.com/xiaozhibo/XiaoZhiBoiOSSrc_6.3.7092.zip">DOWNLOAD</a></td>
  </tr>
  <tr align="center">
    <td style="text-align:center">Android 源码包</td>
    <td style="text-align:center">6.3</td>
    <td style="text-align:left">由 RTMP SDK 、IM SDK、COS SDK、业务逻辑层代码和界面层代码构成，源码阅读推荐参考 <a href="https://cloud.tencent.com/document/product/454/7892">Android 代码说明</a></td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_xzb_android_source") href="http://download-1252463788.file.myqcloud.com/xiaozhibo/XiaoZhiBoAndroidSrc_6.3.7090.zip">DOWNLOAD</a></td>
  </tr>
  <tr align="center">
    <td style="text-align:center">PHP 源码包</td>
    <td style="text-align:center">4.4</td>
    <td style="text-align:left">为观众端提供直播间列表和回放列表</td>
    <td style="text-align:center"><a onclick=MtaH5.clickStat("wiki_download_xzb_php_source") href="https://github.com/TencentVideoCloudMLVBDev/xiaozhibo_business_svr_php">DOWNLOAD</a></td>
  </tr>
  
</table>

<script>
    var _mtac = {"senseHash":0};
    (function() {
      var mta = document.createElement("script");
      mta.src = "//pingjs.qq.com/h5/stats.js";
      mta.setAttribute("name", "MTAH5");
      mta.setAttribute("sid", "500538821");
      mta.setAttribute("cid", "500538834");
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(mta, s);
    })();
</script>
