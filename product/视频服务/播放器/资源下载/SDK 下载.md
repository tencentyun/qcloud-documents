<style>
    .card-container {
        width: 350px;
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
播放器 SDK 是腾讯云视立方产品家族的子产品之一，提供直播、点播场景的视频播放能力。
您可以在 [产品功能](https://cloud.tencent.com/document/product/881/61375) 中查看 SDK 支持的功能清单，在 [Demo 体验](https://cloud.tencent.com/document/product/881/20204) 中获取各端 Demo 进行功能体验，在本页面中下载各端 SDK 并获取 Demo 源码。

### Web SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
  <div class="card-container">
      <div class="card">
        <img src="https://main.qcloudimg.com/raw/7e2651085e3e3c6e32190e401a6dfd32.svg" data-nonescope="true">
        <p class="titlename">Web 播放器 SDK</p>
        <p style="color:#586376;">可用于直播播放和点播播放，适用于 PC 端浏览器和移动端浏览器。</p>
        <a onclick="reportEvent({name: 'download-click-web', ext1: 'zip'})" target="_blank" href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.5.2/release.zip">ZIP 下载</a>
        <a style="margin-left: 10px;" onclick="reportEvent({name: 'download-click-web', ext1: 'github'})" target="_blank" href="https://cloud.tencent.com/document/product/881/77877">集成指引</a>
        <a style="margin-left: 10px;" onclick="reportEvent({name: 'download-click-web', ext1: 'doc-sdk'})" target="_blank" href="https://tcplayer.vcube.tencent.com">Demo 示例</a>
      </div>
  </div>
</div>

### iOS & Android SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
                            <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
                                <p class="titlename">iOS 播放器 SDK</p>
                <p style="color:#586376;">包含点播播放和直播播放功能，提供常见组件及场景化的 Demo 源码帮助快速搭建应用。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_iOS_latest.zip">ZIP 下载</a>
                <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/881/77878">集成指引</a>
                                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/Player_iOS">Demo 源码</a>
            </div>
        </div>
			  <div class="card-container">
            <div class="card">
                                <img class="icon" src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
                                <p class="titlename">Android 播放器 SDK</p>
                <p style="color:#586376;">包含点播播放和直播播放功能，提供常见组件及场景化的 Demo 源码帮助快速搭建应用。</p>
                                <a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_Android_latest.zip">ZIP 下载</a>
                 <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/881/77881">集成指引</a>
                                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/Player_Android">Demo 源码</a>
            </div>
        </div>
</div>


### 跨平台 SDK

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
        <div class="card-container">
            <div class="card">
									<img src="https://qcloudimg.tencent-cloud.cn/raw/3b6929f89ce1113bc2005873f2338de9.png" data-nonescope="true"/>
									<p class="titlename">Flutter 播放器 SDK</p>
                <p style="color:#586376;">基于 Flutter 框架封装的播放器 SDK，让您用一套代码快速构建出能够运行于各平台的 App。</p>
								<a href="https://github.com/LiteAVSDK/Player_Flutter">ZIP 下载</a>
								<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/881/60729">集成指引</a>
                <a style="margin-left: 10px;" href="https://github.com/LiteAVSDK/Player_Flutter">GitHub</a>
            </div>
        </div>
</div>



## SDK 能力清单
