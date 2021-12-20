<style>
.markdown-text-box table th,.markdown-text-box table td{text-align: center;}
.inbuttom{height: 30px;width: 150px;min-width: 24px;padding: 0 20px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;vertical-align: middle;white-space: nowrap;}
</style>

## Native Demo
<table>
<tr>
<th>iOS</th><th>Android</th><th>Windows</th><th >Mac OS</th>
</tr>
<tr>
<td><img style="width:150px;" src="https://main.qcloudimg.com/raw/a1a6fd4a9bc3ad2b5fe60e31202c8fda.png" data-nonescope="true"></td>
<td><a onclick="window.open('https://dldir1.qq.com/hudongzhibo/liteav/TRTCDemo.apk')"><button style="width:150px;height: 150px;border:none;background-image:url(https://main.qcloudimg.com/raw/8a603ced0a61983018c794df842f7029.png);background-size: cover;">
</button></a></td>
<td><a onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Win_Demo.exe')"><button style="width:150px;height: 150px;border:none;background-image:url(https://main.qcloudimg.com/raw/e80b8f4462e2904b31dcdcaabe71c484.png);background-size: cover;">
</button></a></td>
<td><a onclick="window.open('https://liteav.sdk.qcloud.com/app/install/TXLiteAVSDK_Mac_Demo.tar.bz2')"><button style="width:150px;height: 150px;border:none;background-image:url(https://main.qcloudimg.com/raw/e80b8f4462e2904b31dcdcaabe71c484.png);background-size: cover;">
</button></a></td>
</tr>
</table>


## 跨平台 Demo
<table>
<tr>
<th>微信小程序</th><th>Web</th><th>Flutter </th><th>Electron</th>
</tr>
<tr>
</div></a></td>
<td><div style="width:150px;height: 150px;background-image:url(https://main.qcloudimg.com/raw/4cfc59a1b60c02fc975c8b3e23169fc7.png);background-size: cover;">
</div>
</td>
<td>
<input type="button" value="视频通话" class="inbuttom" onclick="window.open('https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html')" /><br><br>
<input type="button" value="互动直播推流端" class="inbuttom" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuipusher/pusher.html')" /><br><br>
<input type="button" value="互动直播拉流端" class="inbuttom" onclick="window.open('https://web.sdk.qcloud.com/component/tuiliveroom/tuiplayer/player.html')" />
</td>
<td>
<a onclick="window.open('https://www.pgyer.com/TtEk')" value="Flutter_ios_版">
	<button style="width:150px;height: 83px;border:none;background-image:url(https://main.qcloudimg.com/raw/a3b7ef0199988c33850eeeb186c8d26f.png);background-size: cover;">
</button>
</a>
<br>
<a onclick="window.open('https://comm.qq.com/im_demo_download/trtc_flutter_demo.apk')" value="Flutter_android_版"> 
	<button style="width:150px;height: 83px;border:none;background-image:url(https://main.qcloudimg.com/raw/f53741b9ad7567c475841e68cc65dbc3.png);background-size: cover;">
</button>
</a></td>
<td>
<input type="button" value="Windows 版" style="height: 30px;width: 150px;min-width: 24px;padding: 0 20px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;vertical-align: middle;white-space: nowrap;"  onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/api-example/TRTC-Electron-API-Examples-windows.zip')" /><br><br>
<input type="button" value="MacOS 版" style="height: 30px;width: 150px;min-width: 24px;padding: 0 20px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;vertical-align: middle;white-space: nowrap;" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/api-example/TRTC-Electron-API-Examples-mac.zip')" /></td>
</tr>
</table>





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
::: Windows
![](https://imgcache.qq.com/operation/dianshi/other/win.836bd473a766ea962d0b40117888e99aad5db6c8.gif)
:::
::: macOS
![](https://imgcache.qq.com/operation/dianshi/other/macOS.cd7d6d7e8a7fcc388ec27e41c6952b8615ce9d34.gif)
:::
::: Web
![](https://imgcache.qq.com/operation/dianshi/other/058ffcf5-60f0-430c-96c7-e1760b93e444.fdd0f2c10a8242dadbf99108a48a59124124b437.gif)
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
互动课堂场景支持老师和学生互动连麦，最多支持50人同时连麦，平滑上下麦，切换过程无需等待，沟通时延低于300ms；低延时直播模式下，支持10万学生同时观看，观看时延低至1000ms，CDN 旁路直播下，观众人数无限制；支持屏幕共享、互动白板、录制回放等多种课堂应用功能，打造形式更加丰富的线上教学。常见业务场景有大班课、小班课、超级小班课、AI课堂、招生课、内训直播课、1V1在线教育等。
<table>
     <tr>
         <th>老师端（Electron）</th>  
         <th>学生端（Electron）</th>  
     </tr>
<tr>
<td><img src="https://imgcache.qq.com/operation/dianshi/other/Electron_teacher.76058b065f0b01ccc5d6bfd058c6b655e69a149c.gif"/></td>
<td><img src="https://imgcache.qq.com/operation/dianshi/other/Electron_stu.9e3f55291b657d94878963ad86471b331190f47c.gif"/></td>
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


