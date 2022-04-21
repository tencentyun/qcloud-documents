<style>
.markdown-text-box table th,.markdown-text-box table td{text-align: center;}
.inbuttom{height: 30px;width: 150px;min-width: 24px;padding: 0 20px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;vertical-align: middle;white-space: nowrap;}
.preview-demo-section .preview-demo-item {
    display: inline-block;
    width: 200px;
    height: 300px;
    background: #fff;
    box-shadow: 0 1px 8px 0 rgba(156,175,204,0.25);
    border-radius: 1px;
    text-align: center;
    padding: 0 15px;
    margin: 10px 10px 10px 0;
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
    margin-top: 15px;
}
.preview-demo-section .preview-demo-item.style-single-download-btn .demo-item-download {
    margin-top: 50px;
}
.preview-demo-section .preview-demo-item.style-flutter .demo-item-download {
    margin-top: 55px;
}
.preview-demo-section .preview-demo-item.style-electron .demo-item-download {
    margin-top: 25px;
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
    width: 135px;
    height: 35px;
    line-height: 35px;
    margin: 0 auto;
}
.preview-demo-section .preview-demo-item.style-web .demo-item-download .demo-item-download-btn {
    color: #fff;
    background-color: #00a4ff;
    height: 25px;
    line-height: 25px;
    border: 1px solid #dfe0df;
    margin-bottom: 10px;
}
.preview-demo-section .preview-demo-item .demo-item-download .demo-item-download-btn:hover {
    cursor: pointer;
}
</style>

<div class="preview-demo-section">
    <div class="preview-demo-item style-qrcode">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/53be7f245c4d11d3aefcb6dc53918757.svg" alt="">
            </div>
            <div class="demo-item-platform">Android</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议、KTV、语音聊天室、互动直播等
        </div>
        <div class="demo-item-download">
            <img src="https://main.qcloudimg.com/raw/8a603ced0a61983018c794df842f7029.png" data-nonescope="true">
        </div>
    </div>
    <div class="preview-demo-item style-qrcode">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/36154dc8bb7c93826dbdc6fdcec4e194.svg" alt="">
            </div>
            <div class="demo-item-platform">iOS</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议、KTV、语音聊天室、互动直播等
        </div>
        <div class="demo-item-download">
            <img src="https://qcloudimg.tencent-cloud.cn/raw/033bd1e3f459d902dbf2c23479fec4da.png" data-nonescope="true">
        </div>
    </div>
    <div class="preview-demo-item style-single-download-btn">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/7622934bfd307936181d3a57ed69706d.svg" alt="">
            </div>
            <div class="demo-item-platform">Windows</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议、<br>语音聊天室
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Win_Demo.exe');reportEvent({name: 'demo-click-native', ext1: 'windows'});">立即下载</div>
        </div>
    </div>
    <div class="preview-demo-item style-single-download-btn">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/2f867a868913c590fbb2929b8b240f45.svg" alt="">
            </div>
            <div class="demo-item-platform">Mac OS</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议、<br>语音聊天室
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Mac_Demo.tar.bz2');reportEvent({name: 'demo-click-native', ext1: 'windows'});">立即下载</div>
        </div>
    </div>
    <div class="preview-demo-item style-qrcode">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/f86154130067ff386c90306fd71dfdce.svg" alt="">
            </div>
            <div class="demo-item-platform">微信小程序</div>
        </div>
        <div class="demo-item-desc">
            语音聊天室、音视频通话、<br>多人会议
        </div>
        <div class="demo-item-download">
            <img src="https://main.qcloudimg.com/raw/4cfc59a1b60c02fc975c8b3e23169fc7.png" data-nonescope="true">
        </div>
    </div>
    <div class="preview-demo-item style-web">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/ff4dc34a1c72fdb26fc41c1268898025.svg" alt="">
            </div>
            <div class="demo-item-platform">Web</div>
        </div>
        <div class="demo-item-desc">
           单击即可体验
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html');reportEvent({name: 'demo-click-web', ext1: 'api-example'});">视频通话</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuipusher/pusher.html');reportEvent({name: 'demo-click-web', ext1: 'pusher'});">互动直播推流</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuiplayer/player.html');reportEvent({name: 'demo-click-web', ext1: 'player'});">互动直播拉流</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/component/trtccalling/demo/web/latest/index.html');reportEvent({name: 'demo-click-web', ext1: 'calling'});">1v1音视频通话</div>
        </div>
    </div>
    <div class="preview-demo-item style-flutter">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/0fae0aca728ba2ce98e66d1b9641aa56.svg" alt="">
            </div>
            <div class="demo-item-platform">Flutter</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议等
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://comm.qq.com/im_demo_download/trtc_flutter_demo.apk');reportEvent({name: 'demo-click-flutter', ext1: 'android'});">立即下载</div>
        </div>
    </div>
    <div class="preview-demo-item style-electron">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/96a6b7e86eb8d7a93f830d3686d3164c.svg" alt="">
            </div>
            <div class="demo-item-platform">Electron</div>
        </div>
        <div class="demo-item-desc">
            音视频通话、多人会议、<br>屏幕分享等
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-windows-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'windows'});">下载 Windows 版</div>
            <div class="demo-item-download-btn" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-mac-latest.zip');reportEvent({name: 'demo-click-electron', ext1: 'mac'});">下载 Mac OS 版</div>
        </div>
    </div>
</div> 

## 视频通话场景
视频通话场景即两人或多人视频通话，支持 720P、1080P 高清画质；单个房间最多支持300人同时在线，最多支持50人同时开启摄像头。常见应用场景有1对1视频通话、300人视频会议、在线问诊、视频聊天、视频客服、视频面审、视频双录、在线理赔、视频狼人杀等。
>?作为腾讯云推出的音视频解决方案，微信小程序和其他端都能互通，您可以在微信小程序内获得媲美 iOS/Android 的绝佳体验，欢迎使用。

<dx-tabs>
::: iOS&Android
<table>
<tr>
   <th>主动呼叫</th>
   <th>被叫接听</th>
 </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/group-call.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/group-recv.gif"/></td>
</tr>
</table>
:::
::: 小程序
<table>
<tr><th>主动呼叫</th><th>被叫接听</th> </tr>
<tr>
<td><img src="https://webim-1252463788.cos.ap-shanghai.myqcloud.com/trtc-calling-doc-assets/videocall.gif"/></td>
<td><img src="https://webim-1252463788.cos.ap-shanghai.myqcloud.com/trtc-calling-doc-assets/videoaccept.gif"/></td>
</tr>
</table>
:::
::: Flutter\s(iOS/Android)
![](https://imgcache.qq.com/operation/dianshi/other/8d81a52d-ffd3-4bbd-bd09-1a1648569b2d.453825bf12c01b9fe937ca8d7291f3c44b48cced.gif)
:::
::: Windows & Mac
![](https://qcloudimg.tencent-cloud.cn/raw/0f663092120f8f8f3673bc5d8f444516.gif)
:::
::: Web
![](https://imgcache.qq.com/operation/dianshi/other/webrtc-sdk-demo.140bfaedb71e65ca221c1338281492622950ecd6.gif)
:::
</dx-tabs>

## 语音通话场景
语音通话场景即两人或多人语音通话，支持 48kHz，支持双声道；单个房间最多支持300人同时在线，最多支持50人同时开启麦克风。常见应用场景有1对1语音通话、多人语音通话、语音聊天、语音会议、语音客服、狼人杀等。
<dx-tabs>
::: iOS&Android
<table>
<tr>
   <th>主动呼叫</th>
   <th>被叫接听</th>
 </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/call.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/recv.gif"/></td>
</tr>
</table>
:::
::: 小程序
<table>
<tr><th>主动呼叫</th><th>被叫接听</th></tr>
<tr>
<td><img src="https://webim-1252463788.cos.ap-shanghai.myqcloud.com/trtc-calling-doc-assets/audiocall.gif"/></td>
<td><img src="https://webim-1252463788.cos.ap-shanghai.myqcloud.com/trtc-calling-doc-assets/audioaccept.gif"/></td>
</tr>
</table>
:::
</dx-tabs>

## 视频互动直播场景
视频互动直播场景支持主播与观众视频连麦互动；支持主播跨房间（跨直播间）PK；支持平滑上下麦，切换过程无需等待，主播延时小于300ms；单个房间可连麦人数无限制，最多支持50人同时连麦；低延时直播模式下，支持10万观众同时播放，播放延时低至1000ms；CDN 旁路直播模式下，观众数量无限制。常见应用场景有视频低延时直播、十万人互动课堂、视频直播 PK、视频相亲房、互动课堂、远程培训、大型会议等。
<dx-tabs>
::: iOS&Android
<table>
<tr>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/beauty.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/join.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/msg.gif"/></td>
<td><img width="260" height="561" src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/pk.gif"/></td>
</tr>
</table>
:::
::: Web
![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-official-website.gif)
:::
</dx-tabs>

## 语音互动直播场景
语音互动直播场景支持主播与观众语音连麦互动；支持主播跨房间（跨直播间）PK；支持平滑上下麦，切换过程无需等待，主播延时小于300ms；单个房间可连麦人数无限制，最多支持50人同时连麦；低延时直播模式下，支持10万观众同时播放，播放延时低至1000ms；CDN 旁路直播模式下，观众数量无限制。常见应用场景有语音低延时直播、语音直播连麦、语音直播 PK、语聊房、语音相亲房、K 歌房、FM 电台等。
<table>
     <tr>
         <th>主播麦位操作</th>  
         <th>观众麦位操作</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/voiceroom_pick_seat.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/voiceroom_enter_seat.gif"/></td>
</tr>
</table>


## 视频会议场景
视频会议场景支持 支持1080p高清画质与48kHz高音质，音视频时延低于300ms，畅享流畅高清的会议体验；支持屏幕分享、文件分享，让会议更高效；并结合即时通信，支持文字图片等多种形式辅助讨论，不干扰会议进程。常见的应用场景有全媒体客服、在线会议、政企业直播等。
<table>
     <tr>
         <th>进入会议</th>  
         <th>屏幕分享</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/enterroom.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/enterroom.gif"/></td>
</tr>
</table>

## 互动课堂场景
[互动课堂](https://cloud.tencent.com/document/product/647/45465) 场景支持老师和学生互动连麦，最多支持50人同时连麦，平滑上下麦，切换过程无需等待，沟通时延低于300ms；低延时直播模式下，支持10万学生同时观看，观看时延低至1000ms，CDN 旁路直播下，观众人数无限制；支持屏幕共享、互动白板、录制回放、举手、点名签到、全员禁麦等多种课堂应用功能，打造形式更加丰富的线上教学。常见业务场景有大班课、小班课、超级小班课、AI课堂、招生课、内训直播课、1V1在线教育等。
<table>
     <tr>
         <th>老师端（Electron）</th>  
         <th>学生端（Electron）</th>  
     </tr>
<tr>
<td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-teacher.gif"/></td>
<td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-student.gif"/></td>
</tr>
</table>

## 在线 K 歌（KTV 场景）
KTV 场景支持主播与观众上麦唱歌；支持平滑上下麦，切换过程无需等待，主播延时小于300ms；单个房间可连麦人数无限制，最多支持50人同时连麦；低延时直播模式下，支持10万观众同时播放，播放延时低至1000ms；CDN 旁路直播模式下，观众数量无限制。常见应用场景有语音低延时直播、语音直播连麦、语音直播 PK、语聊房、语音相亲房、K 歌房、FM 电台等。
<table>
     <tr>
         <th>房主点歌操作</th>  
         <th>观众点歌操作</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/ktv_demo_experience_owner.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/ktv_demo_experience_audience.gif"/></td>
</tr>
</table>

## 实时合唱（Chorus 场景）

Chorus 场景支持房主主唱与一名观众上麦唱歌；支持平滑上下麦，切换过程无需等待，主播延时小于100ms；低延时直播模式下，支持10万观众同时播放，播放延时低至1000ms；CDN 旁路直播模式下，观众数量无限制。常见应用场景有双人合唱、K 歌房、FM 电台等。

<table>
     <tr>
         <th style="text-align:center;width:50%">房主点歌操作</th>  
         <th style="text-align:center">副唱查看歌单操作</th>  
     </tr>
<tr>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/Chorus_Anchor.gif"/></td>
<td><img src="https://liteav.sdk.qcloud.com/doc/res/trtc/picture/zh-cn/Chorus_Chorus.gif"/></td>
</tr>
</table>

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
