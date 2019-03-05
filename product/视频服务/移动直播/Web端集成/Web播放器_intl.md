## Overview

Tencent Cloud Web Player is designed to solve problems about playing audio and video streams on the mobile browser and PC browser. It allows you to propagate video content on WeChat Moments, Weibo and other social platforms even though users do not install related App.

This document is suitable for developers with some knowledge of JavaScript language.


## Basics
Before interfacing, you need to know the following basics:

- **LVB and VOD**
LVB means that the video source is generated in real time, so no progress bar is displayed on the player during the LVB. In addition, once the VJ stops broadcasting, the LVB URL will become invalid.
VOD means that the video source is a file on the server, so a progress bar is displayed during the playback. In addition, the file can be played at any time as long as the provider does not deleted it.

- - **Supported protocols (mobile phone)**
Web player's video playback capability is not achieved by web page codes, but through the support of browsers. Therefore, its compatibility is not so good. In addition, you have to accept the fact that **not all mobile browsers can meet expectations**, and some even do not support video playback.

 The most common video source URL for web LVB is the one ending with m3u8, known as HLS (HTTP Live Streaming), which is a standard introduced by Apple. Due to the influence of Apple, currently mobile browsers are most compatible with this protocol, but it has an inherent problem: high delay (generally 20-30 seconds). However, we have no other choice for mobile browsers.
 
- - **Supported Protocols (PC)**
 The situation is better on the PC because PC browsers still use Flash control, which supports video sources of many formats. In addition, all Flash controls for various browsers are developed by Adobe alone, so the compatibility is very good. That is why Google disables Flash by default in the latest Chrome browser to promote WebRTC and HTML5 technologies.
![](//mc.qcloudimg.com/static/img/b0d6aaf5a6478ad7e5bda380260983b4/image.png)
## Interfacing Guide

### Step 1: Prepare pages
Introduce the initialization script to the page on which videos will be played (including PC page or HTML5 page)
```
<script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer.js" charset="utf-8"></script>;
```

> Note: **You cannot debug it by directly using a local web page</font> because Tencent Cloud Web Player cannot handle cross-domain issues in this case.**

### Step 2: Add a container to HTML page

 Add a player "container"(namely, div) to the position on the page where the player need to be displayed, and then name the container, such as id_test_video. In this way, all video screens will be rendered in this container. You can control the container size through div attributes, and the sample codes are as follows:

```
<div id="id_test_video" style="width:100%; height:auto;"></div>
```

### Step 3: Play a interfaced video
Write JavaScript codes to pull audio and video streams from a specified URL and present the video screen to the container added in Step 2.

#### 3.1 A simple playback
The following is a typical LVB URL based on the HLS (M3U8) protocol. If a VJ is in LVB, you can directly open the URL to watch the LVB through a player such as VLC.
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8      // M3U8 playback URL
```
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)

To play this video URL on the mobile browsers, you can write JavaScript codes in this way:
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8", //Replace this URL with an actual available playback URL
"autoplay" : true,      //On the Safari browser in the iOS system and most mobile browsers, video auto playback is not enabled.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" : '480',//Video display width. It is recommended to use the video resolution width
"Height" : '320'// Video display height. It is recommended to use the video resolution height
});
```

These codes can support the playback of HLS (M3U8) protocol-based LVB videos on PC and mobile browsers. However, as mentioned above, HLS (M3U8) protocol-based videos feature good compatibility (some Android mobile phones still do not support such videos), but they have high delay (about 20 seconds or more).

#### 3.2 Achieve lower delay on the PC
Can we achieve better on PC browsers? Of course. Because PC browsers support Flash, they are more powerful than mobile browsers. You can write codes in this way:
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"flv": "http://2157.liveplay.myqcloud.com/live/2157_358535a.flv", //Add an FLV URL for playback on the PC. Replace this URL with an actual available playback URL
"autoplay" : true,//On the Safari browser in the iOS system and most mobile browsers, video auto playback is not enabled.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" : '480',//Video display width. It is recommended to use the video resolution width
"height" : '320'//Video display height. It is recommended to use the video resolution height
});
```
These codes differ from the above ones in that we add an FLV playback URL. In this way, if Tencent Cloud Web Player recognizes the current browser is a PC browser, it will automatically choose the FLV linkage to achieve lower delay.

The prerequisite is that both FLV and HLS (M3U8) can be streamed. By using Tencent Cloud LVB service, you do not need worry about this because Tencent Cloud's every LVB channel supports FLV, RTMP and HLS (M3U8) playback protocols by default.

#### 3.3 What if playback failed?
Generally, playback failure is caused by the following:

- **(1). Video source errors**
For LVB URL, check whether the primary VJ has stopped push. If the status is not "in LVB", remind viewers with the floating window: "The primary VJ has left."
For VOD URL, check whether the file to be played is still on the server. For example, whether others have removed the playback URL from the VOD system.

- **(2). Debugging on the local web page**
Currently, Tencent Cloud Web Player cannot be debugged on local web page (that is, open the web page for video playback through the file://protocol) because browsers have cross-domain security restrictions. Therefore, if you put a test.html file on the Windows and then test it, definitely, video cannot be played. You need to upload the file to a server for test. Besides, a mainstream solution is that frontend engineers perform local proxy on online page via reverse proxy to achieve local debugging.

- **(3). Incompatibility of mobile phone**
Ordinary mobile phone browsers do not support FLV and RTMP URLs. Although the latest version of QQ browser supports the playback of FLV files, the popularity is not great. Therefore, you can use only HLS (M3U8) URLs.

- **(4). Cross-domain security issues**
On the PC browsers, video playback is based on the Flash control, which checks cross-domain access (Flash developers should have known that). However, this occurs only when the video URL to be played does not belong to Tencent Cloud. The solution is to add the qq.com domain name to the crossdomain.xml, the cross-domain configuration file under the root domain name of video server:
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
</cross-domain-policy>
```

### Step 4: Set a cover for the player
In the above sample codes, you can see the parameter coverpic. Here, we will detail how to use it.
Note: Cover feature may be invalid in some mobile playback environments. The reasons are that playback environments on mobile devices are more complex than that on the PC, and WebViews of various browsers and Apps use different ways to achieve HTML5 video. If the feature becomes invalid, welcome to feedback to our technical support (including information on system, browser, App version and other key items), and we will try our best to support you.

#### 4.1 Set a simply cover
You can pass a picture URL to coverpic to set the picture as the player cover. The picture will be centered on the player area and displayed at its actual resolution

```
"coverpic" : "http://www.test.com/myimage.jpg"
```
#### 4.2 Set the presentation style of the cover
You can not only pass an object to coverpic, but also set the parameters style (presentation style of the cover) and src (picture URL) in the object.<br>

The parameter style supports the following values:
- "default": The picture is centered on the player area and displayed at its actual resolution.
- "stretch": The picture is stretched to cover the whole player area so that it may be distorted.
- "cover": Preferentially, the picture is stretched horizontally and uniformly to cover the whole player area. Some parts of the picture may not be displayed on the area.

```
"coverpic" : {"style":"stretch", "src":"http://www.test.com/myimage.jpg"}
```
#### 4.3 Implementation example

The below is the URL of an online exemplary player cover, which is displayed with the cover method. To view the sample codes, right click "view page source codes" on the PC browser.
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html)

Note: Cover setting may be invalid on some mobile devices. Please see FAQs for instructions

### Step 5. Achieve multi-clarity selection
#### 5.1 Principles
For videos on Youku, Tudou and Tencent Video, popular video streaming service providers in China, you can select different clarity. How to achieve this?
![](//mc.qcloudimg.com/static/img/5769d1bd31db2d9ed258d0bf62be3f0f/image.png)

First, we need to know that **players themselves cannot modify video clarity**. When video source is generated, the video has only one kind of clarity, referred to as **original definition**.

How is multi-clarity achieved? Actually, through video cloud:
- For LVB, the original video from a VJ is transcoded in real time on Tencent Cloud to get two videos such as **HD video** and **SD video**. Each has its URL:
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          // Original definition
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      // High definition
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      // Standard definition
```

- For VOD, after uploading a video file to Tencent Cloud, you can transcode the video file to generate videos with different clarity, such as **HD video** and **SD video**.
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8           // Original definition
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      // High definition
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      // Standard definition
```

#### 5.2 Code implementation
The following codes are used to allow players to support multi-clarity selection, that is, to display the multi-clarity option on the player user interface.

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"      : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//Replace this URL with an actual available playback URL
"m3u8_hd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
"m3u8_sd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
"autoplay"  : true,      //On the Safari browser in the iOS system and most mobile browsers, video auto playback is not enabled.
"coverpic"  : "http://www.test.com/myimage.jpg",
});
```

#### 5.3 Implementation example
The below is the URL of an online exemplary player, on which you can set and switch clarity. To view the sample codes, right click "view page source codes" on the PC browser.
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true)

Normally, you can see the following effect:
![](//mc.qcloudimg.com/static/img/68c513d931214e86549dd9c0426efe04/image.png)

Currently, the playback of multi-clarity video and clarity switch are available on the PC, but not on the mobile devices.

### Step 6: Customize error messages
Tencent Cloud Web Player supports error message customization in case you are not satisfied with the default error messages such as "Network error. Check whether the network configuration or playback URL is correct" or "Video decoding error".

#### 6.1 Code implementation
The following is core codes to make the player support error message customization. Error messages are mainly set in wording attributes.
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8" : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//Replace this URL with an actual available playback URL
"autoplay" : true,      //The feature is not enabled on the Safari browser in the iOS system
"coverpic" : "http://www.test.com/myimage.jpg",
"wording": {
    2032: "Video request failed. Check the network",
    2048: "M3U8 file request failed. It may be caused by network errors or cross-domain issues"
}
});
```

#### 6.2 Implementation example
The below is the URL of an online exemplary player which uses message customization. To view the same codes, right click "view page source codes" on the PC browser.
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8)

#### 6.3 Error codes
| Code  | Message | Description                                       |
|-------|-----------|---------------------------------------|
| 1   	| Network error. Check whether the network configuration or playback URL is correct|  Error message in HTML5          |
| 2     | Video decoding error | Web Player cannot decode video in such format (error message in HTML5)            |
| 3     | Network error. Check whether the network configuration or playback URL is correct|  Error message in HTML5          |
| 4	    |Failed to get video. Check whether the playback URL is valid |         Error message in HTML5           |
| 5 | The current system environment does not support the video format |         Error message in HTML5           |
| 1001     | Network error. Check whether the network configuration or playback URL is correct|  Network disconnected (NetConnection.Connect.Closed) (error message in Flash)          |
| 1002	|Failed to get video. Check whether the playback URL is valid |  The file to be played is not found (NetStream.Play.StreamNotFound). This may because a server error occurs or the video file does not exist (error message in Flash) |
| 2032	|Failed to get video. Check whether the playback URL is valid|   Error message in Flash                 |
| 2048	| Failed to load video file and cross-domain access refused | M3U8 file request failed. It may be caused by network errors or cross-domain problems (error message in Flash) |


Error messages are updated from time to time for the black box characteristics of Flash and the uncertainty of video playback standard of HTML5.

## Source Code Reference
The below is the URL of an online exemplary player. To view the sample codes, right click "view page source codes" on the PC browser.

[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true)

You can also use it to test the player. Add an URL of the video to be played to the end of the above URL. After refreshed, this video URL can be played:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true&m3u8=http://2527.vod.myqcloud.com/2527_b3907044441c11e6a46d294f954f93eb.f230.av.m3u8
```

## Parameter List
The below list details all parameters supported by the player.

| Parameter             | Type     | Default Value   | Description                                     |   Example
|-----------------|--------- |--------  |-------------------------------------------- |----------------------------|
| m3u8            | String   | None       |  Playback URL of original-definition M3U8 file                                | http://2157.liveplay.myqcloud.com/2157_358535a.m3u8 |
| m3u8_hd         | String   | None       |  Playback URL of HD M3U8 file                            | http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8 |
| m3u8_sd         | String   | None       |  Playback URL of SD M3U8 file                            | http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8 |
| flv             | String   | None       |  Playback URL of original-definition FLV file                             | http://2157.liveplay.myqcloud.com/2157_358535a.flv |
| flv_hd          | String   | None       |  Playback URL of HD FLV file                            | http://2157.liveplay.myqcloud.com/2157_358535ahd.flv |
| flv_sd          | String   | None       |  Playback URL of SD FLV file                             | http://2157.liveplay.myqcloud.com/2157_358535asd.flv |
| mp4             | String   | None       |  Playback URL of original-definition MP4 file                             | http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4 |
| mp4_hd          | String   | None       |  Playback URL of HD MP4 file                             | http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4 |
| mp4_sd          | String   | None       |  Playback URL of SD MP4 file                             | http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4 |
| rtmp            | String   | None       |  Playback URL of original-definition RTMP file                            | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88 |
| rtmp_hd         | String   | None       |  Playback URL of HD RTMP file                            | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88hd |
| rtmp_sd         | String   | None       |  Playback URL of SD RTMP file                            | rtmp://2157.liveplay.myqcloud.com/live/2157_280d88sd |
| width           | Number   | None       | This parameter is **required** and is used to set player width in pixel |   640                                        |
| height          | Number   | None       | This parameter is **required** and is used to set player height in pixel |   480                                        |
| live            | Boolean  | false    | height | This parameter is **required**, and is used to set whether video is LVB, determine whether to render timeline and other controls, and distinguish the processing logic of VOD and LVB| true                   |
| autoplay        | Boolean  | false    | This parameter is used to set whether to play video automatically<br>Note: This option takes effect only on most PC platforms |  true                                                                                  |
| coverpic        | String / Object| None |This parameter is used to preview cover. You can pass a picture URL or an object including parameters src (picture URL) and style (presentation style of picture) <br>Optional attributes of the parameter style: <br>default: The picture is centered and displayed with scale ratio being 1:1 <br>stretch: The picture is stretched to cover the whole player area so that it may be distorted <br> cover: Preferentially, the picture is stretched horizontally and uniformly to cover the whole player area. Some parts of the picture may not be displayed on the area.    |  "http://www.test.com/myimage.jpg" <br>orbr> {"style": "cover", "src": "http://www.test.com/myimage.jpg"}                                                          |
| controls        | String   |"default" | default: default controls are displayed; none: controls are not displayed; system: system controls are displayed on the mobile device        | "system"                                                           |
| x5_type         | String   | None       | This parameter is used to enable the HTML5 player at the same layer through the video attribute "x5-video-player-type". Value: h5. This is an experimental attribute of TBS kernel and is not supported by non-TBS kernel.       | "h5"                                                           |
| x5_fullscreen   | String   | None       | This parameter is used to declare whether to enter full screen mode of TBS during video playback through the video attribute "x5-video-player-fullscreen". Value: true. This is an experimental attribute of TBS kernel and is not supported by non-TBS kernel.         | "true"                                                           |
| wodring         | Object   | None       | This parameter is used to customize message    |  { 2032:  'Video request failed. Check the network'}                                                          |
| listener        | Function | None       | Callback function of event listening, to which a JSON-format object is passed     | function(msg){<br>//handle events <br>}                                                            |

## Advanced Features
The following introduces ways to use advanced features of the video player SDK

### Listening events
The video cloud player plays video by combining HTML5 `<video>` and Flash, which trigger different events during playback. Therefore, based on the standard of HTML5 `<video>`, we convert playback events of Flash to unify the naming of playback events.

[HTML5 Events List](https://www.w3.org/wiki/HTML/Elements/video#Media_Events)
[Flash Events List](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/events/NetStatusEvent.html)

Event list after unification

```
error
timeupdate
load
loadedmetadata
loadeddata
progress
fullscreen
play
playing
pause
ended
seeking
seeked
resize
volumechange
```
Note: Since Flash has black box characteristics and the video playback standard of HTML5 is achieved differently on different platforms and terminals, trigger modes and results of an event are different, which should be noted during development.<br>

Under non-auto playback, load the video to the status of to be played. At this point, for Flash on the mobile device and PC, events triggered are different.
Flash on the mobile:
![Flash on the mobile](//mc.qcloudimg.com/static/img/ddf4e9ff5998dc84b1887fba0e94d446/image.png)
Flash on the PC:
![Flash on the PC](//mc.qcloudimg.com/static/img/f49d8aa8ef678b63ac73e69f254c20bb/image.png)

Note: The above is the difference between two platforms. Besides, differences also exist between various mobile devices and mobile Apps.<br>

Use Cases:

Through event listening, you can reconnect if playback fails. [URL of online example ](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-reconnect.html)


## FAQs

- **Why is the screen stretched when the video is played in HTML5?**

    Video can not be stretched in HTML5. Check if the width/height configuration of the player container is correct.

- **Why can't I put my div over the video?**

    Different browsers use different ways to achieve `<video>` tag. For example, if you open a web page in QQ or WeChat (for Android), it is highly possible to use X5 browser kernel (QQ browser kernel) bundled with the Apps. Due to contain reasons, QQ browser team adopted the solution that video`<video>` tag must be on the top. For more information, please see [QQ Browser Document](http://x5.tencent.com/guide?id=2009)). However, through the coordination inside Tencent, recently the team is modifying this solution gradually. Therefore, the latest version of X5 browser kernel may have solved the problem when you read this document.

- **Why is the cover setting invalid?**

    The reason for this problem is same as that of the last one. The cover cannot be displayed unless the browser allows elements to override the `<video>`tag.

- **Why are videos played in full screen by default on some mobile browsers?**

	For iOS terminals, if your video achieves inline playback within an App, namely your App packages an iOS WebView control for displaying the web page, then you can customize WebView in details. Its performance can be different from that of standard Safari browser. You can set the webkit-playsinline attribute (set it to the playsinline attribute if under iOS 10) via the `<video>` tag in the HTML, and set the WebView to the allowInlineMediaPlayback. In this way, video can be played in non-full screen mode (inline playback) when you open a page in the App.

	If you open the page on the Safari browser, currently, any Safari browser on iOS below 10 cannot disable automatic full screen playback. On iOS 10, you can achieve non-full screen playback (inline playback) through the above method (set the `<video>` tag to playsinline attribute). Tencent Cloud Web Player has automatically added this attribute. Therefore, as long as the terminal supports it, non-full screen playback can be achieved.

	For Android terminals, since Android systems have various customized versions, with each using different ways to achieve the `<video>` tag due to lack of complete and unified standard, video playback consistency on the Android system is lower that on the iOS system. Based on the common solution, Tencent Cloud Web Player has automatically added the webkit-playsinline playsinline attribute. Therefore, as long as the terminal supports it, non-full screen playback can be achieved.

- **Why cannot videos be played automatically on mobile browsers?**

	To automatically play a video on the mobile Web, you can use only two ways: setting autoplay attribute of the `<video>` tag or calling the play () method provided by the `<video>` tag. However, auto video playback on the mobile Web is always prohibited. The current common solution is to manually trigger playback by users (for example, listening to the user's click event and calling the play () method). Besides, some specially customized WebViews support the autoplay attribute of the `<video>` tag or can achieve auto playback by calling other special functions. On such WebViews, auto playback can be achieved once you open a page. Tencent Cloud Web Player has set the autoplay to true, and added the autoplay attribute to the `<video>` tag. Therefore, as long as the terminal supports it, you can achieve auto playback.

- **Why does the Flash player have two playback buttons in Chrome on PC?**

	As of Chrome 42, except main Flash content, Flash is not played automatically anymore (Google purchased and open sourced WebRTC to reach certain goals) unless user click it manually.

- **Why can the LVB video be played on the PC browsers but cannot on the mobile ones?**

    To play LVB videos on the mobile browsers, the Web Player needs to check whether the LVB push URL includes the HLS (M3U8) pull URL because only HLS (M3U8) protocol is supported. If providing an FLV or RTMP URL to the Web Player, you cannot watch the video on mobile phone.
