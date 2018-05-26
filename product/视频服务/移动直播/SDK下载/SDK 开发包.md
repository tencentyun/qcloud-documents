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
[Demo](https://cloud.tencent.com/document/product/454/6555) 中展示的功能一般会领先 SDK 1 - 2 周时间，这段时间我们会用来进行 bugfix 和 系统测试工作，所以部分 Demo 中的特性如果您在 SDK 中没有找到接口，可以先联系我们获取内部版本。

<h2 id="iOS"> iOS SDK (4.7.4395) </h2>

<table style="text-align:center;vertical-align:middle;">
  <tr>
    <th width="115px">功能特性</th>
    <th width="150px">直播精简版</th>
    <th width="150px">独立播放器版</th>
    <th width="150px">短视频功能版</th>
    <th width="150px">全功能专业版</th>
    <th width="150px">商用企业版</th>
  </tr>
  <tr>
    <td>RTMP推流</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>直播播放</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>点播播放</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>基础美颜</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>直播连麦</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频录制</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频编辑</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频拼接</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频发布</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>动效贴纸</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>美瞳瘦脸</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>绿幕抠图</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>BitCode</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
  </tr>
	<tr>
    <td>IPA 增量</td>
    <td>1.43 M</td>
    <td>2.57 M</td>
    <td>2.52 M</td>
    <td>4.19 M</td>
    <td>5.98 M</td>
  </tr>
  <tr>
    <td>Pod 安装</td>
    <td><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td><a href="https://cloud.tencent.com/document/product/454/12642">COCOAPOD</a></td>
    <td>见版本说明</td>
  </tr>
  <tr>
    <td>SDK 下载</td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_livelite") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_Smart_iOS_4.7.4395.zip?_ga=1.230547544.572863791.1503542401">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_player") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_Player_iOS_4.7.4395.zip?_ga=1.172502247.572863791.1503542401">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_shortvideo") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_UGC_Rename_iOS_4.7.4395.zip?_ga=1.172502247.572863791.1503542401">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_ios_profession") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_Professional_iOS_4.7.4395.zip?_ga=1.172502247.572863791.1503542401">DOWNLOAD</a></td>
    <td>见如下说明</td>
  </tr>
</table>

- **商用版本**
  商用企业版相比于专业版，增加了基于腾讯优图实验室专利技术的人脸特效功能，下载地址为 <a onclick=MtaH5.clickStat("wiki_download_sdk_ios_enterprise_rename") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_Enterprise_Rename_iOS_4.7.4395.zip">【Enterprise(iOS).zip】</a>，此版本非免费提供，需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。使用方法见 [特效功能指引](https://cloud.tencent.com/document/product/454/9018) 。
  
- **命名冲突**
  部分版本中包含有 ffmpeg 和 ijkplayer，如果您的项目中已经包含相关开源库，推荐使用 **精简版** 或 **符号重命名版**， 符号重命名版下载地址为 <a onclick=MtaH5.clickStat("wiki_download_sdk_ios_profession_rename") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/TXLiteAVSDK_Professional_Rename_iOS_4.7.4395.zip?_ga=1.172502247.572863791.1503542401">【Rename(iOS).zip】</a> 。  
  

<h2 id="Android"> Android SDK (4.7.4395) </h2>

<table style="text-align:center;vertical-align:middle;">
  <tr>
    <th width="115px">功能特性</th>
    <th width="150px">直播精简版</th>
    <th width="150px">独立播放器版</th>
    <th width="150px">短视频功能版</th>
    <th width="150px">全功能专业版</th>
    <th width="150px">商用企业版</th>
  </tr>
  <tr>
    <td>RTMP推流</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>直播播放</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>点播播放</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>基础美颜</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>直播连麦</td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频录制</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频编辑</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频拼接</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>视频发布</td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>动效贴纸</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>美瞳瘦脸</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>绿幕抠图</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><img src="https://mc.qcloudimg.com/static/img/a9bdba876321beb3c0ad270e67d41743/image.png"/></td>
  </tr>
  <tr>
    <td>SDK 下载</td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_android_livelite") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/LiteAVSDK_Smart_Android_4.7.4395.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_android_player") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/LiteAVSDK_Player_Android_4.7.4395.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_android_shortvideo") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/LiteAVSDK_UGC_Android_4.7.4395.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_android_profession") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/LiteAVSDK_Professional_Android_4.7.4395.zip">DOWNLOAD</a></td>
    <td>见如下说明</td>
  </tr>
</table>

- **商用版本**
  商用企业版相较于专业版，增加了基于腾讯优图实验室专利技术的人脸特效功能，下载地址为 <a onclick=MtaH5.clickStat("wiki_download_sdk_android_enterprise") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/4.7/LiteAVSDK_Enterprise_Android_4.7.4395.zip">【Enterprise(Android).zip】</a>，此版本非免费提供，需要解压密码和授权 license 才能运行，解码密码和授权 license 请联系腾讯云商务获取。使用方法见 [特效功能指引](https://cloud.tencent.com/document/product/454/9020)。

<h2 id="Windows"> Windows SDK (3.1.0) </h2>

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
    <td>RTMP播放</td>
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
    <td>具备C#（.NET）开发经验</td>
    <td>具备C++开发经验</td>
  </tr>
  <tr align="center">
    <td>开发环境</td>
    <td>记事本</td>
    <td>Visual Studio 2010</td>
    <td>Visual Studio 2015</td>
  </tr>
  <tr align="center">
    <td>版本日期</td>
    <td>2.0.1 @ 2018-02-08</td>
    <td>3.1.0 @ 2018-05-17</td>
    <td>3.1.0 @ 2018-05-17</td>
  </tr>
  <tr align="center">
    <td>下载地址</td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_activex_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/ActiveX/LiteAV_AX_SDK.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_csharp_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/CSharp/LiteAVSDK_Windows_C%23.zip">DOWNLOAD</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_windows_cplusplus_source") href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/Cpp/LiteAVSDK_Windows_C%2B%2B.zip">DOWNLOAD</a></td>
  </tr>
</table>

- **Why not Obs?**
本 SDK 目前还处于初级阶段，我们正在持续努力中，所以本 SDK 相比于 OBS 功能要少很多，唯一的优势在于低延迟，配合 TXLivePlayer 的 RTMP_ACC 超低延时播放，可以将达到 400ms 以内的延迟效果。

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

- **一键部署**
此套源码包含两个部分，**wxlite** 文件夹中的源码为小程序源码，**simpleserver** 文件夹中的源码为后台 node.js 源码，该套支持在腾讯云平台进行一键部署，使您能在 5 分钟时间里即拥有一个自己的调试环境，部署方法可参考 [DOC](https://cloud.tencent.com/document/product/454/12554)。

<h2 id="PCWeb">Web（PC）源码（1.0.0）</h2>

| 所属平台 | 版本号 | 说明 | 下载链接 |
|---------|---------|---------|------|
| 任意浏览器 | 1.0.0| 源码实现了一个网页唤起 EXE 桌面程序，并跟小程序互通的简单Demo，<br>可以用实现 浏览器[(IE或Chrome)](https://cloud.tencent.com/document/product/454/17004) =>TXCloudRoom.exe + 微信[(小程序)](https://cloud.tencent.com/document/product/454/16914) 的组合解决方案。 | [WebEXE](https://github.com/TencentVideoCloudMLVBDev/webexe_web.git) |
| Chrome | 1.0.0| 源码实现了一个Windows版本Chrome跟小程序互通的简单Demo，<br>可以用实现 PC[(Chrome)](https://cloud.tencent.com/document/product/454/17005) + 微信[(小程序)](https://cloud.tencent.com/document/product/454/16914) 的组合解决方案。 | [WebRTC](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc) |

<h2 id="Server">服务端源码（1.1.0）</h2>
 
<table width="850px">
  <tr align="center">
    <th width="120px">下载项目</th>
    <th width="80px">版本号</th>
    <th width="570px">功能说明</th>
    <th width="80px">下载链接</th>
  </tr>
	<tr align="center">
    <td>签名计算</td>
    <td>1.1.0</td>
    <td style="vertical-align:middle; text-align:left;">用于计算 IM、LiveRoom、RTCRoom 以及 WebRTC 等方案中所需要使用的 UserSig 和 privateMapKey 签名，算法基于 ECDSA-SHA256 实现 </a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_sdk_server_sign") href="https://github.com/TencentVideoCloudMLVBDev/sign_srv">JAVA & PHP</a</td>
  </tr>
  <tr align="center">
    <td rowspan="2"> RoomService</td>
    <td rowspan="2">1.1.0</td>
    <td rowspan="2" style="vertical-align:middle; text-align:left;">RoomService 是 <a href="https://cloud.tencent.com/document/product/454/14606#Server">LiveRoom</a>（直播连麦） 和 <a href="https://cloud.tencent.com/document/product/454/14617#Server">RTCRoom</a>（视频通话） 的后台组件，源码下载后可部署于自己的业务服务器上。 </td>
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

  
<h2 id="Xiaozhibo">小直播源码（4.5.4022）</h2>

小直播是腾讯视频云终端产品中心打造的一款集各种功能（文字互动、弹幕消息、飘星点赞、美颜增白、动效蒙皮、连麦互动）于一体的开源 APP，致力于帮您快速搭建自己的直播产品原型。您可以参考 [搭建指引](https://cloud.tencent.com/document/product/454/15187) 了解如何快速让下面的代码跑起来。

<table width="850px">
  <tr align="center">
    <th width="120px">所属平台</th>
    <th width="80px">版本号</th>
    <th width="570px">说明</th>
    <th width="80px">下载链接</th>
  </tr>
  <tr align="center">
    <td>iOS 源码包</td>
    <td>4.5.4022</td>
    <td>由 RTMP SDK 、IM SDK、COS SDK、业务逻辑层代码和界面层代码构成，源码阅读推荐参考 <a href="https://cloud.tencent.com/document/product/454/7894">[DOC]</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_xzb_ios_source") href="http://download-1252463788.file.myqcloud.com/xiaozhibo/XiaoZhiBoiOSSrc_4.5.4022.zip">DOWNLOAD</a></td>
  </tr>
  <tr align="center">
    <td>Android 源码包</td>
    <td>4.5.4022</td>
    <td>由 RTMP SDK 、IM SDK、COS SDK、业务逻辑层代码和界面层代码构成，源码阅读推荐参考 <a href="https://cloud.tencent.com/document/product/454/7892">[DOC]</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_xzb_android_source") href="http://download-1252463788.file.myqcloud.com/xiaozhibo/XiaoZhiBoAndroidSrc_4.5.4022.zip">DOWNLOAD</a></td>
  </tr>
  <tr align="center">
    <td>PHP源码包</td>
    <td>4.4</td>
    <td>为观众端提供直播间列表和回放列表</td>
    <td><a onclick=MtaH5.clickStat("wiki_download_xzb_php_source") href="https://github.com/TencentVideoCloudMLVBDev/xiaozhibo_business_svr_php">DOWNLOAD</a></td>
  </tr>
  <tr align="center">
    <td>Web分享页</td>
    <td>1.1.0</td>
    <td>基于HTML5技术构建的Web分享页面，支持在常规手机浏览器和PC浏览器上观看直播，并支持与主播进行消息互动，实现原理推荐参考 <a href="https://cloud.tencent.com/document/product/454/8046">[DOC]</a></td>
    <td><a onclick=MtaH5.clickStat("wiki_download_xzb_web_source") href="https://github.com/TencentVideoCloudMLVBDev/web_share">DOWNLOAD</a></td>
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
