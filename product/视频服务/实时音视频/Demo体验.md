<style>
.markdown-text-box table th,.markdown-text-box table td{
    text-align: center;
}
.inbuttom{
    height: 30px;
    width: 150px;
    min-width: 24px;
    padding: 0 20px;
    background-color: #00a4ff;
    color: #fff;
    border: 1px solid #00a4ff;
    line-height: 30px;
    text-align: center;
    display: inline-block;
    cursor: pointer;
    outline: 0 none;
    box-sizing: border-box;
    text-decoration: none;
    font-size: 12px;
    vertical-align: middle;
    white-space: nowrap;
}
ul.rno-tabs-operation {
    border-bottom: #E5E8ED 1px solid;
    position: relative;
    padding-left: 0;
    font-size: 0;
    margin-bottom: 0;
    height: 40px;
    background-color: #F4F7FA;
}
.preview-demo-section .preview-demo-item {
    display: inline-block;
    width: 226px;
    height: 300px;
    background: #fff;
    box-shadow: 0 1px 8px 0 rgb(156 175 204 / 25%);
    border-radius: 1px;
    text-align: center;
    padding: 0 15px;
    margin: 10px 13px 10px 7px;
    vertical-align: top;
}

.preview-demo-section .preview-demo-item .demo-item-header {
    margin-top: 30px;
}
.preview-demo-section .preview-demo-item .demo-item-desc {
    font-size: 12px;
}

.preview-demo-section .preview-demo-item .demo-item-platform {
    font-size: 20px;
    font-weight: bold;
}
.preview-demo-section .preview-demo-item .demo-logo-wrapper {
    line-height: 1;
}
.preview-demo-section .preview-demo-item .demo-item-header img {
    box-shadow: none;
    width: 40px;
    height: 40px;
}
.preview-demo-section .preview-demo-item.style-qrcode .demo-item-download {
    margin-top: 15px;
}
.preview-demo-section .preview-demo-item.style-web .demo-item-download {
    margin-top: 46px;
}
.preview-demo-section .preview-demo-item.style-single-download-btn .demo-item-download {
    margin-top: 50px;
}
.preview-demo-section .preview-demo-item.style-flutter .demo-item-download {
    margin-top: 55px;
}
.preview-demo-section .preview-demo-item.style-electron .demo-item-download {
    margin-top: 46px;
}
.preview-demo-section .preview-demo-item.style-electron .demo-item-download-btn:first-child {
    margin-bottom: 10px;
}
.preview-demo-section .preview-demo-item .demo-item-download img {
    box-shadow: none;
    width: 110px;
    height: 110px;
}
.preview-demo-section .preview-demo-item .demo-item-download .demo-item-download-btn {
    background-color: #00a4ff;
    border-radius: 20px;
    color: #fff;
    font-size: 14px;
    width: 170px;
    height: 35px;
    line-height: 35px;
    margin: 0 auto;
}
.preview-demo-section .preview-demo-item.style-web .demo-item-download .demo-item-download-btn {
    color: #fff;
    background-color: #00a4ff;
    height: 24px;
    line-height: 24px;
    margin-bottom: 6px;
}
.preview-demo-section .preview-demo-item.style-electron .demo-item-download .demo-item-download-btn {
    color: #fff;
    background-color: #00a4ff;
    height: 24px;
    line-height: 24px;
    margin-bottom: 6px;
}
.preview-demo-section .preview-demo-item .demo-item-download .demo-item-download-btn:hover {
    cursor: pointer;
}
.markdown-text-box img {
        box-shadow: none;
        background:0;
}
.support-platform{
    width: 56px;
    height: 24px;
    font-family: PingFangSC-Regular;
    font-weight: 400;
    font-size: 14px;
    color: #333333;
    letter-spacing: 0;
    line-height: 24px;
}
.tab-bottom{
    width: 100%;
    height: 180px;
    background: #EDF1F5;
    display:flex;
    justify-content: center;
    align-items: center;
}
.tab-bottom .platform-icon{
    text-align:center;
}
.tab-support{
    height:24px;
    text-align:center;
    padding: 24px 0 0 0;
}
.platform-img{
    width: 18px;
    height: 18px;
    box-shadow: 0 0 0 0 #FFFFFF;
    vertical-align:-4px;
    padding:0 8px;
}
.try-icon{
    width: 16px;
    height: 16px !important;
    margin-left: 5px !important;
    vertical-align: -3px !important;
}
.tab-experience{
    width: 150px;
    height: 40px;
    background: #FFFFFF;
    box-shadow: 0 2px 4px 0 rgba(215,226,236,0.40);
    border-radius: 20px;
    border:0;
    color:#06A4FF;
    line-height:40px;
}
.tab-img {
    width: 100%;
    background-color: #F4F7FA;
    padding: 0 0 50px 0;
}
.tab-experience-button{
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    
}
.rno-tabs-operation-bd {
    padding: 50px 0 0 0;
    background-color: #F4F7FA;
}
.markdown-text-box .rno-tabs-operation {
    margin: 0;
    padding-top: 8px;
    height: 38px;
}
ul.rno-tabs-operation {
    border-bottom: #E5E8ED 1px solid;
    position: relative;
    padding-left: 0;
    font-size: 0;
    height: 58px;
    background-color: #F4F7FA;
}
.markdown-text-box .rno-tabs-operation {
    margin: 0px;
    padding-top: 0;
}
.rno-tabs-operation-item.active {
    border-bottom-color: #06A4FF;
		top: -11px;
}
.rno-tabs-operation-item {
    display: inline-block;
    text-align: center;
    position: relative;
    cursor: pointer;
    padding-bottom: 4px;
    overflow: hidden;
    vertical-align: bottom;
    margin-bottom: -1px;
    margin-right: 20px;
    border-bottom: 2px solid transparent;
    height: 31px;
    margin-top: 19px;
		top: -11px;
}
.rno-tabs-operation-item.active>a {
    color: #00a4ff;
}
</style>

<div class="preview-demo-section" id="demo-card">
    <div class="preview-demo-item style-qrcode" style="margin-left:0">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/53be7f245c4d11d3aefcb6dc53918757.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Android</div>
        </div>
        <div class="demo-item-desc">
            音视频通话·多人会议<br>KTV 语音聊天·互动直播等
        </div>
        <div class="demo-item-download">
            <img src="https://main.qcloudimg.com/raw/8a603ced0a61983018c794df842f7029.png">
        </div>
    </div>
    <div class="preview-demo-item style-qrcode">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/36154dc8bb7c93826dbdc6fdcec4e194.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">iOS</div>
        </div>
        <div class="demo-item-desc">
            音视频通话·多人会议<br>KTV 语音聊天·互动直播等
        </div>
        <div class="demo-item-download">
            <img src="https://qcloudimg.tencent-cloud.cn/raw/6e810724c1102666fcf7cf274c8776b0.png">
        </div>
    </div>
    <div class="preview-demo-item style-single-download-btn">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/7622934bfd307936181d3a57ed69706d.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Windows</div>
        </div>
        <div class="demo-item-desc">
            音视频通话·多人会议<br>语音聊天室
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Win_Demo.exe');reportEvent({name: 'demo-click-native', ext1: 'windows'});">立即下载</div>
        </div>
    </div>
    <div class="preview-demo-item style-single-download-btn" style="margin-right:0">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/2f867a868913c590fbb2929b8b240f45.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Mac OS</div>
        </div>
        <div class="demo-item-desc">
            音视频通话·多人会议<br>语音聊天室
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Mac_Demo.tar.bz2');reportEvent({name: 'demo-click-native', ext1: 'windows'});">立即下载</div>
        </div>
    </div>
          <div class="preview-demo-item style-qrcode" style="margin-left:0">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/f86154130067ff386c90306fd71dfdce.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">小程序</div>
        </div>
        <div class="demo-item-desc">
            音视频通话·多人会议<br>语音聊天室等
        </div>
        <div class="demo-item-download">
            <img src="https://qcloudimg.tencent-cloud.cn/raw/e0ffb1aeaf0ff8761277c78597aad01f.png" data-nonescope="true">
        </div>
    </div>
    <div class="preview-demo-item style-web">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/ff4dc34a1c72fdb26fc41c1268898025.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Web</div>
        </div>
        <div class="demo-item-desc">
           单击即可体验
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/login.html');reportEvent({name: 'demo-click-web', ext1: 'api-sample'});">音视频通话</div>
						<div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/tuiroom/index.html');reportEvent({name: 'demo-click-web', ext1: 'api-sample'});">多人视频会议</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuipusher/login.html');reportEvent({name: 'demo-click-web', ext1: 'pusher'});">互动直播推流</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuiplayer/login.html');reportEvent({name: 'demo-click-web', ext1: 'player'});">互动直播拉流</div>
        </div>
    </div>
    <div class="preview-demo-item style-flutter">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/0fae0aca728ba2ce98e66d1b9641aa56.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Flutter</div>
        </div>
        <div class="demo-item-desc">
            音视频通话 多人会议等
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://comm.qq.com/im_demo_download/trtc_flutter_demo.apk');reportEvent({name: 'demo-click-flutter', ext1: 'android'});">立即下载</div>
        </div>
    </div>
    <div class="preview-demo-item style-electron" style="margin-right:0">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/96a6b7e86eb8d7a93f830d3686d3164c.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Electron</div>
        </div>
        <div class="demo-item-desc">
           单击即可体验
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/TUIRoom-Electron/TUIRoom-Electron-mac-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'mac'});">多人视频会议 Mac OS版</div>
						<div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/TUIRoom-Electron/TUIRoom-Electron-windows-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'windows'});">多人视频会议 Windows版</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-mac-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'mac'});">教育场景化 Mac OS版</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-windows-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'windows'});">教育场景化 Windows版</div>
        </div>
    </div>
</div> 


## 音视频通话场景

<dx-tabs>
::: iOS&Android
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/55e49f7fbefcc17a8a9e9685d841365c.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
                 <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/232c7d2d022d0fead3da024086557e11.png" class="platform-img">小程序</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/584b9e4444422c19af20536317680ed3.svg" class="platform-img">Uni-App</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/78729" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUICalling" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: Web
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/d1ebc0f76b824d4a65a895aee4ab6931.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/584b9e4444422c19af20536317680ed3.svg" class="platform-img">Uni-App</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/78729" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUICalling" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: 小程序
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/d05db03536a2e3035f59246810f4fe41.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/584b9e4444422c19af20536317680ed3.svg" class="platform-img">Uni-App</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/78729" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUICalling" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
</dx-tabs>


## 视频互动直播场景
<dx-tabs>
::: iOS&Android
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/f4386698a3457904a88b06673aced475.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
         <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/4dcbeb0def10b73f0ce7bee9609054a4.svg" class="platform-img">H5</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/43180" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUILiveRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: Web
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/0b75ece13658346006f6bd421e55c97a.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
         <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/4dcbeb0def10b73f0ce7bee9609054a4.svg" class="platform-img">H5</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/43180" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUILiveRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
</dx-tabs>


## 语音互动直播场景
<dx-tabs>
::: iOS&Android
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/1d18841399850926793fbe5406eabcc8.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/45736" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUIVoiceRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
</dx-tabs>


## 视频会议场景
<dx-tabs>
::: iOS&Android
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/9d68584d0fba88dc740ae70e5cdc41e5.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/cf4c9ee1645ee381b7fec591223b8f75.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
                 <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/232c7d2d022d0fead3da024086557e11.png" class="platform-img">小程序</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/864f8562e1b7780e6f23e1f2987f9ff9.svg" class="platform-img">Flutter</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/71cd4ae02a39a0a8345dee11737e717a.svg" class="platform-img">Windows</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/5300d0170d592174fc94411d162a09a1.svg" class="platform-img">Mac OS</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/45666" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUIRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: Web
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/6b6bf774e10964ae3e4d4589b58a776c.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/cf4c9ee1645ee381b7fec591223b8f75.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/864f8562e1b7780e6f23e1f2987f9ff9.svg" class="platform-img">Flutter</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/71cd4ae02a39a0a8345dee11737e717a.svg" class="platform-img">Windows</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/5300d0170d592174fc94411d162a09a1.svg" class="platform-img">Mac OS</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/45666" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUIRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: 小程序
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/069c36bfdfc339583255c9ad04ddec22.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/7adfb7daedcc48ead500f1ddf6bdb237.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/584b9e4444422c19af20536317680ed3.svg" class="platform-img">Uni-App</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/45666" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUICalling" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
::: Windows & Mac & Electron
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/c5f67e544d2143dcac8a5ffc8645f944.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/cf4c9ee1645ee381b7fec591223b8f75.svg" class="platform-img">Web</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/864f8562e1b7780e6f23e1f2987f9ff9.svg" class="platform-img">Flutter</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/71cd4ae02a39a0a8345dee11737e717a.svg" class="platform-img">Windows</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/5300d0170d592174fc94411d162a09a1.svg" class="platform-img">Mac OS</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/45666" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUIRoom" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>
:::
</dx-tabs>


## 在线 K 歌场景
<dx-tabs>
::: iOS&Android
<div class="tab-img">
    <img src="https://qcloudimg.tencent-cloud.cn/raw/9d5e3e1001eee2dbcd35ddd1f9e01883.png"/>
</div>
<div class="tab-bottom">
    <div>
    <div class="platform-icon">
        <span class="support-platform">Demo 支持平台</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/901d05fdb42e3ac74f4a1521c119b320.svg" class="platform-img">Android</span>
        <span class="support-platform"><img src="https://qcloudimg.tencent-cloud.cn/raw/8aef65529388017d7f9a46a24085d15a.svg" class="platform-img">iOS</span>
    </div>
    <div class="tab-experience-button"><a href="#demo-card"><button class="tab-experience">立即体验<img src="https://qcloudimg.tencent-cloud.cn/raw/8b41f1a6d19d184c029c6e92e6a01544.svg" class="try-icon" data-nonescope="true"></button></a></div>
    <div style="text-align:center;">您可以单击 <a href="https://cloud.tencent.com/document/product/647/59401" style="color:#06A4FF;">接入指引</a> 了解如何快速集成，或单击 <a href="https://github.com/tencentyun/TUIKaraoke" style="color:#06A4FF;">源码下载</a> 到 Github 下载最新代码</div>
    </div>
</div>

:::
</dx-tabs>


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
