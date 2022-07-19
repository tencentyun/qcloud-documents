<style>
    .card-container {
        width: 380px;
        display: block;
        float: left;
        padding-left: 15px;
        padding-right: 15px;
        box-sizing: border-box;
    }

    .card {
        border-radius: 10px;
        padding-top: 10px;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 10px;
        margin-top: 30px;
        border: 1px solid #ebeef5;
        background-color: #fff;
        overflow: hidden;
        box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
        text-align: center;
    }

    .markdown-text-box img {
        box-shadow: none;
    }


    .titlename {
                color:#191919;
        position: relative;
        top: -2px;
                font-weight: bolder;
                font-size: larger;
    }
        
        @media (max-width: 768px){
                .card-container,
                .scene-card-container{
                        width: 100%;
                }
                .scene-card > div{
                        width: 100%!important;
                        margin-left: 0!important;
                }
                img {
        box-shadow: none;
    }
        }
</style>

## 下载 SDK
实时音视频（TRTC） 是腾讯云提供的一套低延时、高质量的音视频通讯服务，致力于为腾讯云客户提供稳定、可靠和低成本的音视频传输能力。该服务由一套遍布全球的音视频传输网络和一组终端 SDK 组成，您可以在本页面下载到涵盖目前主流客户端平台和热门框架的 TRTC SDK（音视频通话 SDK）。

>? 如果您当前网络访问 Github 速度不理想，可以 [单击这里](https://gitee.com/liteavsdk) 访问 Gitee 中的镜像仓库。

### Web SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
  <div class="card-container">
      <div class="card">
        <img src="https://main.qcloudimg.com/raw/7e2651085e3e3c6e32190e401a6dfd32.svg" data-nonescope="true">
        <p class="titlename">TRTC Web SDK</p>
        <p style="color:#586376;">包含 TRTC 功能，无需安装 App 即可音视频通话，兼容主流的桌面和移动端浏览器。</p>
        <a onclick="reportEvent({name: 'download-click-web', ext1: 'zip'})" target="_blank" href="https://web.sdk.qcloud.com/trtc/webrtc/download/webrtc_latest.zip">ZIP 下载</a>
        <a style="margin-left: 10px;" onclick="reportEvent({name: 'download-click-web', ext1: 'github'})" target="_blank" href="https://github.com/LiteAVSDK/TRTC_Web">GitHub</a>
        <a style="margin-left: 10px;" onclick="reportEvent({name: 'download-click-web', ext1: 'doc-sdk'})" target="_blank" href="https://cloud.tencent.com/document/product/647/16863">集成指引</a>
        <a style="margin-left: 10px;" onclick="reportEvent({name: 'download-click-web', ext1: 'doc-demo'})" target="_blank" href="https://cloud.tencent.com/document/product/647/32398">运行 Demo</a>
      </div>
  </div>
</div>

### Android SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
                            <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
                                <p class="titlename">精简版（TRTC）SDK</p>
                <p style="color:#586376;">包含 TRTC 和直播播放（TXLivePlayer）两项功能，SDK 体积小巧，功能稳定。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Android">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32175">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32166">运行 Demo</a>
            </div>
        </div>
        <div class="card-container">
            <div class="card">
                                <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
                                <p class="titlename">全功能版（Professional）SDK</p>
                <p style="color:#586376;">包含 TRTC、直播、短视频、点播等多项功能，功能丰富，SDK 体积较精简版略大。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_Android_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/tencentyun/LiteAVProfessional_Android">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32175">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32166">运行 Demo</a>
            </div>
        </div>
			  <div class="card-container">
            <div class="card">
                            <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
                                <p class="titlename">模拟器 专用版 SDK</p>
                <p style="color:#586376;">支持x86、x86_64架构，适配雷电模拟器等主流模拟器和声卡，音质佳、性能卓越，功能稳定。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Android_Emulator_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Android">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32175">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32166">运行 Demo</a>
            </div>
        </div>
</div>

### iOS SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
                                <img class="icon" src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
                                <p class="titlename">精简版（TRTC）SDK</p>
                <p style="color:#586376;">包含 TRTC 和直播播放（TXLivePlayer）两项功能，SDK 体积小巧，功能稳定。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_iOS_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_iOS">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32173">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32396">运行 Demo</a>
            </div>
        </div>
        <div class="card-container">
            <div class="card">
                                <img class="icon" src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
                                <p class="titlename">全功能版（Professional）SDK</p>
                 <p style="color:#586376;">包含 TRTC、直播、短视频、点播等多项功能，功能丰富，SDK 体积较精简版略大。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/tencentyun/LiteAVProfessional_iOS">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32173">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32396">运行 Demo</a>
            </div>
        </div>
</div>

### Windows SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
                                <img src="https://main.qcloudimg.com/raw/104e3aadbd4515f61c3f2f5378948cfb.svg" data-nonescope="true">
                                <p class="titlename">Windows SDK（C++ 版）</p>
                <p style="color:#586376;">包含实时音视频（TRTC）、直播推流（TXLivePusher）、直播播放（TXLivePlayer）和点播播放（TXVodPlayer）等四项功能</p>
                          <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Windows">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/71410">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/71413">运行 Demo</a>
            </div>
        </div>
        <div class="card-container">
            <div class="card">
                                <img src="https://main.qcloudimg.com/raw/104e3aadbd4515f61c3f2f5378948cfb.svg" data-nonescope="true">
                                <p class="titlename">Windows SDK（C# 版）</p>
                <p style="color:#586376;">包含实时音视频（TRTC）、直播推流（TXLivePusher）、直播播放（TXLivePlayer）和点播播放（TXVodPlayer）等四项功能。</p>
                          <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_CSharp_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Windows">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32178">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/71425">运行 Demo</a>
            </div>
        </div>
				        <div class="card-container">
            <div class="card">
                                <img src="https://main.qcloudimg.com/raw/104e3aadbd4515f61c3f2f5378948cfb.svg" data-nonescope="true">
                                <p class="titlename">Windows SDK（ActiveX 版）</p>
                <p style="color:#586376;">基于 ActiveX 插件封装的 TRTC SDK，让您在 ActiveX 场景下快速便捷的集成实时音视频服务。</p>
                          <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_ActiveX_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Windows">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/76512">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/76514">运行 Demo</a>
            </div>
        </div>
</div>

### Mac OS SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
                                <img src="https://qcloudimg.tencent-cloud.cn/raw/4f5b5b301babc3ddf4d2867b37c30ffc.png" data-nonescope="true">
                                <p class="titlename">Mac OS SDK</p>
                <p style="color:#586376;">包含实时音视频（TRTC）、直播推流（TXLivePusher）和播放器（TXLivePlayer）和点播播放（TXVodPlayer）等四项功能。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Mac">GitHub</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32176">集成指引</a>
                                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32396">运行 Demo</a>
            </div>
        </div>
</div>

### 微信小程序 SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
								<img src="https://qcloudimg.tencent-cloud.cn/raw/af07e321883032c9796848d189a80f5e.png" data-nonescope="true"/>
								<p class="titlename">微信小程序 SDK</p>
		<p style="color:#586376;">以 live-pusher 和 live-player 两个标签封装的 TRTC SDK，体积小巧，无需安装，效果媲美 App。</p>
							<a href="https://web.sdk.qcloud.com/trtc/miniapp/download/trtc-wx.zip">ZIP 下载</a>
							<a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/Live_WXMini">GitHub</a>
							<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32183">集成指引</a>
							<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/32399">运行 Demo</a>
            </div>
        </div>
</div>

### 跨平台 SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
									<img src="https://qcloudimg.tencent-cloud.cn/raw/d6fd52f011bdbb13302b2ae261e8a756.png" data-nonescope="true"/>
								<p class="titlename">Electron SDK</p>
                <p style="color:#586376;">基于 Electron 框架封装，让您基于 Web 技术快速构建 Windows 和 Mac 平台上的应用。</p>
							<a href="https://web.sdk.qcloud.com/trtc/electron/download/TXLiteAVSDK_TRTC_Electron_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_Electron">GitHub</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/38549">集成指引</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/38548">运行 Demo</a>
            </div>
        </div>
        <div class="card-container">
            <div class="card">
									<img src="https://qcloudimg.tencent-cloud.cn/raw/3b6929f89ce1113bc2005873f2338de9.png" data-nonescope="true"/>
									<p class="titlename">Flutter SDK</p>
                <p style="color:#586376;">基于 Flutter 框架封装的 TRTC SDK，让您用一套代码快速构建出能够运行于各平台的 App。</p>
								<a href="https://pub.dev/packages/tencent_trtc_cloud/versions">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://github.com/c1avie/trtc_demo">GitHub</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/51602">集成指引</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/51601">运行 Demo</a>
            </div>
        </div>
        <div class="card-container">
            <div class="card">
                            <img src="https://qcloudimg.tencent-cloud.cn/raw/90f1ef49218b43d7042bb05b1c0a3959.png" data-nonescope="true">
                                <p class="titlename">React Native SDK</p>
                <p style="color:#586376;">基于 React Native 框架封装的 TRTC SDK，让您用一套代码快速构建移动端 App。</p>
                <a style="margin-left: 10px;" href="https://github.com/tencentyun/TRTCReactNative">GitHub</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/63791">集成指引</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/63790">运行 Demo</a>
            </div>
        </div>
				<div class="card-container">
            <div class="card">
                            <img src="https://qcloudimg.tencent-cloud.cn/raw/e9d18b164152f08bc0694c01e966daea.png" data-nonescope="true">
                                <p class="titlename">uni-app SDK</p>
                <p style="color:#586376;">基于 uni-app 插件封装的 TRTC SDK，让您快速便捷集成实时音视频服务。</p>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/TRTC_UniApp">GitHub</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/72629">运行 Demo</a>
            </div>
        </div>
</div>



## 版本对比
<table>
  <tr>
    <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能详情</th>
    <th width="100px" style="text-align:center">TRTC 精简版</th>
    <th width="100px" style="text-align:center">全功能版</th>
  </tr>
    <tr>
    <td rowspan='2' style="text-align:center">视频通话</td>
    <td style="text-align:center">双人通话</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">多人会议</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">直播连麦</td>
    <td style="text-align:center">同房连麦</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">跨房连麦</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='2' style="text-align:center">基础美颜</td>
    <td style="text-align:center">美白磨皮</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">色彩滤镜</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
    <tr>
    <td rowspan='2' style="text-align:center">直播推流</td>
    <td style="text-align:center">摄像头推流</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">录屏推流</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">直播播放</td>
    <td style="text-align:center">RTMP 协议</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">HTTP - FLV</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='3' style="text-align:center">点播播放</td>
    <td style="text-align:center">MP4 格式</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">HLS(m3u8)</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td style="text-align:center">DRM 加密</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td rowspan='4' style="text-align:center">短视频</td>
    <td style="text-align:center">录制和拍摄</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">裁剪拼接</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">“抖音”特效</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:center">视频上传</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
   <tr>
    <td rowspan='4' style="text-align:center">安装包增量</td>
    <td style="text-align:center">Android</td>
    <td style="text-align:center">armv7：3.97M<br>arm64：4.33M</td>
    <td style="text-align:center">armv7：9.15M<br>arm64：10.4M</td>
  </tr>
    <tr>
    <td style="text-align:center">iOS</td>
    <td style="text-align:center">arm64：3.15M</td>
    <td style="text-align:center">N/A</td>
  </tr>
</table>

>! Windows SDK 和 Mac OS SDK 包含实时音视频（TRTC）、直播推流（TXLivePusher）、直播播放（TXLivePlayer）和点播播放（TXVodPlayer）等四项功能，暂不支持短视频相关功能，不区分精简版和全功能版。

<script src="https://cdn-go.cn/aegis/aegis-sdk/latest/aegis.min.js"></script>
<script>
let aegis;
if(Aegis) {
    aegis = new Aegis({
        id: 'iHWefAYqlXjjlfAkpx',
        uin: document.cookie.replace(/(?:(?:^|.*;\s*)uin\s*\=\s*([^;]*).*$)|^.*$/, "$1")|| '',
        reportApiSpeed: false,
        reportAssetSpeed: false
    });
}
function reportEvent(options){ aegis && aegis.reportEvent(options); }
</script>
