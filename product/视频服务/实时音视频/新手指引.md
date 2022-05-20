<style>

.tp-grid__row.tp-grid--gutter-5n {
    margin-right: -10px;
    margin-bottom: -20px;
    margin-left: -10px;
}

.tp-grid__row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-flow: row wrap;
    -ms-flex-flow: row wrap;
    flex-flow: row wrap;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    margin-right: 0;
    margin-left: 0;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
}

.tp-grid__row.tp-grid--gutter-5n .tp-grid__col {
    margin-bottom: 20px;
    padding-right: 10px;
    padding-left: 10px;
}
.tp-grid__col--6 {
    display: block;
    -webkit-flex: 0 0 auto;
    -ms-flex: 0 0 auto;
    flex: 0 0 auto;
    width: 25%;
    -webkit-box-flex: 0;
}

.tp-grid__col {
    display: block;
    -webkit-flex: 1 1 auto;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    padding-right: 0;
    padding-left: 0;
    font-size: 14px;
    -webkit-box-flex: 1;
}

	.tpm-experience__item {
    display: flex;
    height: 100%;
    background-image: linear-gradient(0deg,#fff,#f3f5f8);
    border: 2px solid #fff;
    box-shadow: 8px 8px 20px 0 rgb(55 99 170 / 10%), -8px -8px 20px 0 #fff;
    border-radius: 4px;
    padding: 20px 28px;
    justify-content: space-between;
		}
		
	.tpm-experience__item-cnt {
    flex: 1;
    max-width: 192px;
   }

 .tpm-experience__item-hd {
    padding-top: 8px; 
  }
	
	.tpm-experience__item-title {
    font-size: 18px;
    color: #000;
    line-height: 26px;
    font-weight: 500;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: top;
}
	
	.tpm-experience__item-qr {
    width: 100px;
    height: 100px;
    background: #fff;
    border-radius: 4px;
    padding: 4px;
    margin-left: 12px;
    }


element.style {
}
.tpm-experience__item-btns {
    margin-left: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

 .tpm-btn {
    display: inline-block;
    box-sizing: border-box;
    min-width: 104px;
    height: 36px;
    padding: 0 24px;
    color: #fff;
    font-size: 14px;
    line-height: 34px;
    white-space: nowrap;
    text-align: center;
    text-decoration: none;
    vertical-align: middle;
    background-color: #0052d9;
    border: 1px solid transparent;
    outline: 0 none;
    cursor: pointer;
    box-shadow: 8px 8px 20px 0 rgb(55 99 170 / 10%);
}

.tpm-experience__item .tpm-btn {
    min-width: 120px;
    margin-bottom: 12px;
    box-shadow: 8px 8px 20px 0 rgb(55 99 170 / 10%);
    -webkit-font-smoothing: auto;
}

.tpm-btn.size-s {
    min-width: 104px;
    height: 32px;
    padding: 0 24px;
    line-height: 30px;
}

    .card-container {
        width: 293px;
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

    .scene-card-container {
        width: 450px;
        display: block;
        float: left;
        padding-left: 15px;
        padding-right: 15px;
        box-sizing: border-box;
    }

    .scene-card {
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
    }

    .image_card {
        margin-top: 10px;
        border: 1px solid #ebeef5;
        box-shadow: 0 2px 1px 0 rgb(0 0 0 / 10%);
    }
    .markdown-text-box img {
        box-shadow: none;
    }


    h3 {
        position: relative;
        top: -2px;
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


## 步骤一：了解产品 
实时音视频（TRTC） 是腾讯云提供的一套低延时、高质量的音视频通讯服务，致力于为腾讯云客户提供稳定、可靠和低成本的音视频传输能力。您可以使用该服务快速构建“视频通话”、“在线教育”、“直播连麦”、“在线会议”等对通信延时要求比较苛刻的音视频应用。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2018-24306?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 步骤二：体验产品
为了让您能够快速了解我们的产品，我们为您提供了一款已经集成了 TRTC 服务的功能演示 Demo，安装后即可体验 TRTC 的各种功能，这包括：
<div style="position: relative; box-sizing: border-box;  overflow:hidden">
    <a href="https://cloud.tencent.com/document/product/647/17021" target="view_window">
            <div class="image_card">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/aebc188e5b459c4abfa4cfecf829c88c.png"/>
            </div>
    </a>
</div>

- **视频通话**：类似微信上的通话功能，支持窗口切换，美颜以及网络信号提示等功能。
- **多人会议**：支持多个用户在同一个房间中交流互动，可用于在线会议和在线教育等场景。
- **秀场直播**：主播在线秀才艺，支持美颜、伴奏、点赞、弹幕互动和在线连麦。
- **在线合唱**：两位主播在线同唱一首歌，感受 TRTC 所提供的低延时通信能力。
- **在线 K 歌**：支持上万人同时收听，并支持语音互动、音乐伴奏和歌词同步等功能的在线音乐直播方案。


## 步骤三：功能集成
为了能让您快速地将 TRTC 功能集成到您的应用中，我们提供了两种不同的集成方案，您可以根据需要选择其中一种方案进行集成：

### 方案一：含 UI 组件集成方案
我们开发了一组标准化的 UI 组件，并提供了源代码，您可以直接将适合的 UI 组件导入到您的项目中，并在需要的时候加载他们。该集成方案的速度非常快，通常一个小时就能完成集成。

<div style="position: relative; box-sizing: border-box; padding-bottom: 10px; margin-bottom: 10px; overflow:hidden;">
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/4f6e018388bce36b0f5b7807ed76c82a.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">音视频通话</h3>
                <p style="color:#586376" ;>组件化 UI 助您快速实现一个“类微信”等视频通话场景</p>
                <a href="https://github.com/tencentyun/TUICalling">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/42044">接入文档</a>
            </div>
        </div>
    </div>
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/129edf43d9adf4df6f022dec79ba6db0.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">多人视频会议</h3>
                <p style="color:#586376" ;>组件化 UI 助您低代码快速实现会议、相亲、面试场景</p>
                <a href="https://github.com/tencentyun/TUIMeeting">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/45681">接入文档</a>
            </div>
        </div>
    </div>
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/ab32f135f2847eaf22733e9a9ad1636a.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">语音互动直播</h3>
                <p style="color:#586376;" ;>组件化 UI 助您低代码快速实现语音聊天室场景</p>
                <a href="https://github.com/tencentyun/TUIVoiceRoom">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/45753">接入文档</a>
            </div>
        </div>
    </div>
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/ab32f135f2847eaf22733e9a9ad1636a.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">视频互动直播</h3>
                <p style="color:#586376;" ;>组件化 UI 助您低代码快速实现直播、连麦、PK场景</p>
                <a href="https://github.com/tencentyun/TUILiveRoom">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/43181">接入文档</a>
            </div>
        </div>
    </div>
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/7a7b51c1536587f0fea130d375661552.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">在线 K 歌</h3>
                <p style="color:#586376;" ;>组件化 UI 助您低代码快速实现在线 KTV 场景</p>
                <a href="https://github.com/tencentyun/TUIKaraoke">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/59402">接入文档</a>
            </div>
        </div>
    </div>
    <div class="scene-card-container">
        <div class="scene-card">
            <div style="float: left; margin-top: 20px;">
                <img src="https://main.qcloudimg.com/raw/7a7b51c1536587f0fea130d375661552.png" width="160" data-nonescope="true">
            </div>
            <div style="float: left; width: 200px; margin-left: 30px; margin-top: 20px; ">
                <h3 style="color:191919;">实时合唱</h3>
                <p style="color:#586376;" ;>组件化 UI 助您低代码快速实现双人实时合唱场景</p>
                <a href="https://github.com/tencentyun/TUIChorus">GitHub 源码</a>
                <a style="margin-left: 30px;" href="https://cloud.tencent.com/document/product/647/61859">接入文档</a>
            </div>
        </div>
    </div>
</div>

### 方案二：无 UI 组件集成方案
您可以在项目中直接导入 TRTC SDK，并通过 SDK API 以构建自己期望的业务形态。该集成方案的自由度很高，不过需要您自行构建 UI 界面和交互逻辑，所以集成速度较方案一略慢。

为了让您快速了解 SDK API 的使用方案，我们为您提供了各个平台 SDK 的 API 示例源码，源码文件夹中的 Basic 目录包含了基础功能的示例代码，Advanced 目录则包含了高级功能（比如设置分辨率、背景音效、网络测速等）的示例代码。

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
    <a href="https://github.com/LiteAVSDK/TRTC_iOS/tree/main/TRTC-API-Example-OC" target="view_window">
        <div class="card-container">
            <div class="card">
                <img class="icon" src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
                <h3>iOS API 示例</h3>
                <p>演示如何使用 RTC iOS API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
    <a href="https://github.com/LiteAVSDK/TRTC_Android/tree/main/TRTC-API-Example" target="view_window">
        <div class="card-container">
            <div class="card">
                <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
                <h3>Android API 示例</h3>
                <p>演示如何使用 RTC Android API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
    <a href="https://github.com/tencentyun/TRTCSDK/tree/master/Windows/QTDemo" target="view_window">
        <div class="card-container">
            <div class="card">
                <img src="https://main.qcloudimg.com/raw/104e3aadbd4515f61c3f2f5378948cfb.svg" data-nonescope="true">
                <h3>Windows API 示例</h3>
                <p>演示如何使用 RTC Windows API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
    <a href="https://github.com/LiteAVSDK/Live_Mac/tree/main/QTDemo" target="view_window">
        <div class="card-container">
            <div class="card">
                <img src="https://main.qcloudimg.com/raw/98394fa5d669de7fb7a187565d138cdb.svg" data-nonescope="true">
                <h3>Mac OS API 示例</h3>
                <p>演示如何使用 RTC Mac OS API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
    <a href="https://github.com/LiteAVSDK/TRTC_Web/tree/main/base-react-next" target="view_window">
        <div class="card-container">
            <div class="card">
                <img src="https://main.qcloudimg.com/raw/7e2651085e3e3c6e32190e401a6dfd32.svg" data-nonescope="true">
                <h3>Web API 示例</h3>
                <p>演示如何使用 RTC Web API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
    <a href="https://github.com/LiteAVSDK/TRTC_Electron/tree/main/TRTC-API-Example" target="view_window">
        <div class="card-container">
            <div class="card">
                <img src="https://main.qcloudimg.com/raw/559e93ed3c05c3916300b04b0b09e7aa.svg" data-nonescope="true">
                <h3>Electron API 示例</h3>
                <p>演示如何使用 RTC Electron API <br>从零开始搭建音视频应用</p>
            </div>
        </div>
    </a>
</div>

