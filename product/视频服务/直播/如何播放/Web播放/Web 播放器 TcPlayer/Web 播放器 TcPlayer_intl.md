## Overview

TcPlayer Lite is mainly used to play audio/video streams in mobile phone browsers and PC browsers. With this player, you can share your videos on social platforms such as WeChat Moments and Weibo without installing other Apps. This document is intended for developers with basic knowledge in JavaScript.

## Basics
The following are the basics you must learn before getting started:

- **LVB and VOD**
LVB video source is generated in real time. Once the VJ stops broadcasting, the LVB URL becomes invalid, and since the live streams are played in real time, no progress bar is displayed on the player during the playback.
VOD video source is a file on the server, which can be played at any time as long as it has not been deleted by the provider. Since the entire video file is stored on the server, a progress bar is displayed during the playback.

- **Supported Protocols**
Playing videos using the web player depends on browsers, rather than the codes in webpages. For this reason, the compatibility may be lower than we expected. The fact is that **not all mobile browsers can yield expected performance results**. Some of the mobile browsers don't even support video playback at all. The most common video source URLs used to play videos on webpages are URLs ending with "m3u8". We call them HLS (HTTP Live Streaming), a standard from Apple. At present, this format has the best compatibility with various mobile browser products thanks to Apple's influence. However, this format has a drawback: a big delay of 20-30 seconds. Even so, we don't have any other choices for mobile browsers.

 This situation looks better on PC, because PC browsers still use FLASH widgets, which supports various video source formats. Besides, the FLASH widgets for different browsers are all developed by Adobe, so they have good compatibility.
![](https://main.qcloudimg.com/raw/8333b92b361d1dab5dee377f1e5e9941.png)

## Interfacing

### Step 1: Prepare the page
Introduce the initialization script to the page on which you want to play videos (including PC or H5)
```
<script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.1.js" charset="utf-8"></script>;
```

>**Note:**
>**You can't perform debugging directly using the local pages** because TcPlayer Lite cannot handle cross-domain issues in such situations.

### Step 2: Place Container into HTML

Place a "container" in the page where you want to display the player. That is, place a div and give it a name such as: id_test_video. When this is done, all videos will be rendered in this container. You can control the container size through the div attributes. Example code is as follows:

```
<div id="id_test_video" style="width:100%; height:auto;"></div>
```

### Step 3: Prepare for Video Playback
The next step is to write the JavaScript code, which is used to pull audio/video streams from the specified URL and display the video in the container added in Step 2.

#### 3.1 A simple playback
A typical LVB URL is shown below, which is based on the HLS (m3u8) protocol. Players such as VLC can directly open this URL to view the video as long as the VJ is still broadcasting:
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8      //m3u8 playback URL
```
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)
Now, we need to play the video of this URL on mobile phone browsers, we can write the JavaScript code like this:

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8", //Replace the URL with a valid playback URL.
"autoplay" : true,      //Most mobile browsers including Safari on iOS do not support auto video playback.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//Video display width. Use the video definition width if possible.
"height" : '320'//Video display height. Use the video definition height if possible.
});
```

This code segment can be used to play LVB videos based on HLS (m3u8) protocol on PC and mobile phone browsers. However, while videos based on HLS (m3u8) protocol have good compatibility (certain Android phones still do not support them), a big delay over 20 seconds is expected on them.

#### 3.2 Achieve lower delay on PC
As PC browsers support flash, the JavaScript code is as follows:
```javascript
var player =  new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"flv": "http://2157.liveplay.myqcloud.com/live/2157_358535a.flv", //Add an FLV playback URL to play videos on PC. Replace the URL with a valid playback URL.
"autoplay" : true,      //Most mobile browsers including Safari on iOS do not support auto video playback.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//Video display width. Use the video definition width if possible.
"height" : '320'//Video display height. Use the video definition height if possible.
});
```
Compared with the previous code, we add an FLV playback URL. When the TcPlayer detects that the browser is a PC browser, it will select the FLV linkage to achieve lower delay. The condition is that both FLV and HLS (m3u8) address can stream the video. You don't have to consider this problem if you use Tencent Cloud VOD service because every VOD channel of Tencent Cloud supports three protocols: FLV, RTMP and HLS (m3u8).

#### 3.3 Why won't the videos play?
The reasons why videos cannot be played are as follows:
-  **Reason 1: Invalid Video Source**
If it's an LVB URL, be sure to check whether the VJ has stopped streaming and isn't in "Broadcasting" status. You can send a notification to viewers via a floating window: "The VJ is offline".
If it's a VOD URL, you need to check whether the file to be played is still on the server. For example, the playback URL may be deleted from the VOD system.

- **Reason 2: Local WebPage Debugging**
TcPlayer Lite does not support debugging in local web page (opening the page where video is played using `file://` protocol). This is because of cross-domain security restrictions of browsers. Simply placing a file such as `test.html` in Windows and testing video playback using the file will definitely end up in failure. You need to upload the file to a server to perform the test. Frontend engineers can achieve local testing by setting up a local proxy for the online web page through reverse proxy. This is a feasible method for local debugging.

- **Reason 3: Mobile Phone Compatibility Problem**
Common mobile browsers do not support FLV and RTMP URLs (The latest QQ Browser can play videos based on FLV protocol, but it is not widely used). You can only use HLS (m3u8) URLs.

- **Reason 4: Cross-Domain Security Problem**
PC browsers achieve video playback based on Flash widgets. Those who did Flash development before would know that **the Flash widget performs cross-domain access check**. You will encounter this problem if cross-domain policy is not deployed on the server where the video you want to play resides in. The workaround can be: Find the cross-domain configuration file `crossdomain.xml` under the root domain name of the video server and add domain name `qq.com` to it:
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
</cross-domain-policy>
```

### Step 4: Configure a Cover Image for the Player
Next, we will explain how to use "coverpic" shown in the above sample code.
**Note: The cover image may become invalid in certain mobile device playback environments because these environments are relatively more complicated compared to PC, and different browsers and App Webviews achieve H5 videos by different means. If you encounter such a situation, feel free to send feedback to our technical support (the feedback should include key information such as system and the version of your browser or App) and we will provide assistance as much as possible.**

#### 4.1 Easily Configure a Cover Image
You can pass the URL of an image to coverpic as the player's cover image. The image will be displayed in the center of the player area, with its actual resolution.

```
"coverpic" : "http://www.test.com/myimage.jpg"
```
#### 4.2 Configure Cover Image Display Style
You can also pass an object to coverpic and configure the display style ("style") and image URL ("src") for the cover image in the object.<br>

Three styles are supported:
- default: display the image in the center, with its actual resolution;
- stretch: stretch the image to fill up to entire player area. This may distort the image.
- cover: horizontally stretch the image while keeping its ratio to fill up the player area. The image may not be fully displayed in the area.

```
"coverpic" : {"style":"stretch", "src":"http://www.test.com/myimage.jpg"}
```
#### 4.3 Implementation Case

This is an online sample code segment, which uses "cover" to display the cover image. Right-click in a PC browser and select **View Page Source** to view the codes of the page:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html
```

>**Note:**
>**The configured cover image may become invalid in certain mobile devices. For more information, please see the FAQ section.**

### Step 5: Multi-Definition Support
#### 5.1 Principle
You can choose different definitions for videos on Youku.com, Tudou.com or Tencent. How do we achieve this feature?
![](//mc.qcloudimg.com/static/img/5769d1bd31db2d9ed258d0bf62be3f0f/image.png)
First, you should know that **the players cannot change a video's definition**. There is only one definition when the video source is generated, which is called **Original**. The original video has different encoding formats and encapsulation formats, and Web pages do not support all video playback formats. In VOD scenarios, the encoding format for videos must be H.264, and encapsulation format must be MP4 or FLV.

So, how is multi-definition selection implemented? This is where the Video Cloud comes into play:
- In LVB scenarios, the original video from VJ will be transcoded in real time in Tencent Cloud, then videos transcoded with different channels are distributed, such as "High Definition (HD)" and "Standard Definition (SD)". The video from each channel has its own corresponding URL:
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          //Original
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      //HD
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      //SD
```

- In VOD scenarios, once a video file is uploaded to Tencent Cloud, you can perform operations to transcode the video and generate videos of different definitions, such as "High Definition (HD)" and "Standard Definition (SD)". Note: The uploaded original video is not transcoded by Tencent Cloud and cannot be played directly.
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8         //Original, replaced with transcoded video of Ultra High Definition
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      //HD
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      //SD
```
>**Note:**
>**The uploaded original video is not transcoded by Tencent Cloud and cannot be played directly.**

#### 5.2 Code Implementation
The following code segment allows player to support multiple definitions. In other words, it displays options used to select different definitions on the player's user interface.

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"      : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8",//Replace the URL with a valid playback URL.
"m3u8_hd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
"m3u8_sd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
"autoplay"  : true,      //Most mobile browsers including Safari on iOS do not support auto video playback.
"coverpic"  : "http://www.test.com/myimage.jpg",
});
```

#### 5.3 Implementation Case
This is an online sample code segment, which uses multi-definition selection and switching features. Right-click in a PC browser and select **View Page Source** to view the code of the page:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true
```
Generally, you will see the following screen:
![](//mc.qcloudimg.com/static/img/68c513d931214e86549dd9c0426efe04/image.png)
**PC now supports video playback in multiple definitions as well as definition switching. This is not supported on mobile devices.**

### Step 6: Customize Error Messages
The default error messages may not suite your needs. For example, the error messages "network error, check your network configuration or if the playback link is correct" or "video decoding error" can be more appropriate as needed. In this case, you can customize messages in TcPlayer Lite:

#### 6.1 Code Implementation
The following code is the core code used to allow the player to support custom messages. The configured messages are mainly placed in the "wording" attribute.
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//Replace the URL with a valid playback URL.
"autoplay" : true,      //Safari browser on iOS do not support this feature.
"coverpic" : "http://www.test.com/myimage.jpg",
"wording": {
    2032: "Video request failed, check your network.",
    2048: "m3u8 file request failed, this may be caused by network error or cross-domain issue."
}
});
```

#### 6.2 Implementation Case
This is an online sample code segment, which shows playback failure and uses custom message feature. Right-click in a PC browser and select **View Page Source** to view the code of the page:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8
```

#### 6.3 Error Code Reference Table
| Code | Message | Description |
|-------|-----------|---------------------------------------|
| 1 | Network error, check if your network configuration or the playback link is correct | (Error prompted by H5) |
| 2 | Network error, check if your network configuration or the playback link is correct | Web player cannot decode the video format (error prompted by H5) |
| 3 | Video decoding error | (Error prompted by H5) |
| 4 | Current system environment does not support this video format | (Error prompted by H5) |
| 5 | Current system environment does not support this video format | The player detects that the current browser environment does not support the passed video. The reason may be that the current browser does not support MSE, or Flash plug-in is not enabled |
| 10 | Do not use the player under "file" protocol, or video playback may fail |   |
| 11 | Incorrect parameter used. Check the player calling code |   |
| 12 | Enter video playback address |   |
| 13 | The LVB ended, come back later | The (NetConnection.Connect.Closed) event is triggered during a normal RTMP playback (error prompted by Flash) |
| 1001 | Network error, check if your network configuration or the playback link is correct | Network disconnected (NetConnection.Connect.Closed) (error prompted by Flash) |
| 1002 | Failed to acquire video, check if the playback link is valid | Failed to pull playback file (NetStream.Play.StreamNotFound), this may be caused by a server error or that the video file does not exist (error prompted by Flash) |
| 2032 | Failed to acquire video, check if the playback link is valid | (error prompted by Flash) |
| 2048 | Failed to load video file, cross-domain access is rejected | Failed to request m3u8 file, this may be caused by network error or cross-domain issue (error prompted by Flash) |

>**Note:**
>**Code 1-4 are original H5 events;**
>**Due to the black box feature of Flash and the uncertainty of H5 video playback standards, the error messages will be irregularly updated.**

## Source Code Reference
This is an online sample code segment. Right-click in a PC browser and select **View Page Source** to view the codes of the page:
```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true
```

You can also use it to test your player. Append the URL of the video to be played after the link and refresh to play the video:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true&m3u8=http%3A%2F%2F1251132611.vod2.myqcloud.com%2F4126dd3evodtransgzp1251132611%2F8a592f8b9031868222950257296%2Ff0.f240.m3u8
```

## Parameter List
Here are all parameters supported by the player as well as their detailed description.

| Parameter | Type | Default Value | Description
|-----------------|--------- |--------  |-------------------------------------------- |
| m3u8 | String | None | m3u8 playback URL (original) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535a.m3u8` |
| m3u8_hd | String | None | m3u8 playback URL (high definition) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8` |
| m3u8_sd | String | None | m3u8 playback URL (standard definition) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8` |
| flv | String | None | flv playback URL (original) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535a.flv` |
| flv_hd | String | None | flv playback URL (high definition) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535ahd.flv` |
| flv_sd | String | None | flv playback URL (standard definition) <br> Example: `http://2157.liveplay.myqcloud.com/2157_358535asd.flv` |
| mp4 | String | None | mp4 playback URL (original) <br> Example: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4` |
| mp4_hd | String | None | mp4 playback URL (high definition) <br> Example: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4` |
| mp4_sd | String | None | mp4 playback URL (standard definition) <br> Example: `http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4` |
| rtmp | String | None | rtmp playback URL (original) <br> Example: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88` |
| rtmp_hd | String | None | rtmp playback URL (high definition) <br> Example: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88hd` |
| rtmp_sd | String | None | rtmp playback URL (standard definition) <br> Example: `rtmp://2157.liveplay.myqcloud.com/live/2157_280d88sd` |
| width | Number | None | **Required parameter**, used to configure player width (in pixels) <br> Example: 640 |
| height | Number | None | **Required parameter**, used to configure player height (in pixels) <br> Example: 480 |
| volume | Number | 0.5 | Used to configure initial volume. Range: 0-1 [v2.2.0+] <br> Example: 0.6 |
| live | Boolean | false | **Required parameter**, used to configure whether the video is LVB video. This determines whether to render certain controls such as the time axis, and is used to differentiate between VOD and LVB processing logics <br> Example: true |
| autoplay | Boolean | false | Whether to enable auto-playback<br>**Note: This option is only effective for most PC platforms** <br> Example: true |
| coverpic | String/Object | None | Preview cover image. You can either pass an image address, or an object containing image address (src) and display style (style).<br> Available styles: <br>"default": image is displayed 1:1 in the center <br>"stretch": stretch the image to fill up the player area. This may distort the image <br>"cover": horizontally stretch the image while keeping its ratio to fill up the player area. The image may not be fully displayed in the area <br> Example: "`http://www.test.com/myimage.jpg`" <br>Or <br>{"style": "cover", "src": h`ttp://www.test.com/myimage.jpg`} |
| controls | String | "default" | "default": displays default controls. "none": does not display controls. "system": displays system controls on mobile devices. **Note: You need to configure this as "system" if you want to use system full screen mode on mobile devices. The default full screen solution uses Fullscreen API + pseudo-full screen [Example](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-consoles.html)**<br> Example: "system" |
| systemFullscreen| Boolean  |false     | In a browser environment that does not support the Fullscreen API, you can try to use the webkitEnterFullScreen method provided by the browser for full screen after you enable it. If Fullscreen API is supported, the system will enter full screen and system control is used <br> Example: true |
| flash | Boolean | true | Whether to prioritize flash to play videos. <br>**Note: this option is only effective on PC platforms** [v2.2.0+] <br> Example: true |
| flashUrl | String | None | You can set flash swf url <br>**Note: this option is only effective on PC platforms** [v2.2.1+] |
| h5_flv | Boolean | false | Whether to enable flv.js to play flv videos. If this is enabled, players will use flv.js to play FLV videos in browsers that support MSE. However, since not all such browsers can use flv.js, players do not enable this attribute by default. [v2.2.0+] <br> Example: true |
| x5_player | Boolean | false | Whether to enable TBS to play flv videos. If this is enabled, players will directly transmit the flv playback addresses to `<video>` to play in TBS mode (for example, WeChat on Android or QQ Browser), [TBS Video Playback](https://x5.tencent.com/tbs/product/video.html) [v2.2.0+]   <br>Example: true |
| x5_type | String | None | Enable the H5 player at the same layer through the video attribute "x5-video-player-type". Available value: H5 (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. [Standard for Docking TBS H5 Single-Layer Player](https://x5.tencent.com/tbs/guide/video.html) <br> Example: "h5" |
| x5_fullscreen   | String   | None       | Declare whether to enter TBS full screen mode when playing a video, by using the "x5-video-player-fullscreen" attribute of "video". Available value: true (this is an experimental attribute of TBS kernel, and is not supported for non-TBS kernels). <br> Example: "true" |
| x5_orientation | Number | None | Declare the orientation supported by TBS player, using the "x5-video-orientation" attribute of "video". Available values: 0 (landscape), 1: (portrait), 2: (landscape &verbar; portrait rotates with mobile phone movement). (This is an experimental attribute of TBS kernel, and is not supported by non-TBS kernels) [v2.2.0+] <br> Example: 0 |
| wording | Object | None | Custom notification <br> Example: { 2032: 'Video request failed, check your network'} |
| clarity | String | 'od' | Default playback definition [v2.2.1+] <br> Example: clarity: 'od'  |
| clarityLabel | Object | {od: 'Ultra High Definition', hd: 'High Definition', sd: 'Standard Definition'} | Custom Definition [v2.2.1+] <br> Example: clarityLabel: {od: 'Blu-ray', hd: 'High Definition', sd: 'Standard Definition'} |
| listener | Function | None | Event monitor callback function. A JSON object is passed to this function <br> Example: function(msg){<br>//Event processing <br>}  |

## List of Instance Methods
Here's a list of methods supported by player instances:

| Method | Parameter | Returned Value | Description | Example
|-----------------|------------------------|----------------------------- |----------------------------------------|---------------------|
| play() | None | None | Start video playback | player.play() |
| pause() | None | None | Pause video playback | player.pause() |
| togglePlay() | None | None | Toggle video playback status | player.togglePlay() |
| mute(muted) | {Boolean} [optional] | true,false {Boolean} | Toggle mute status. The current mute status is returned if no parameter is passed | player.mute(true) |
| volume(val) | {int} Range: 0-1 [optional] | Range: 0-1 | Configure volume. The current volume is returned if no parameter is passed | player.volume(0.3) |
| playing() | None | true,false {Boolean} | Return whether the video is being played | player.playing() |
| duration() | None | {int} | Acquire video duration <br>**Note: this is only applicable for VOD** | player.duration() |
| currentTime(time) | {int} [optional] | {int} | Configure video playback time point. The current playback time point is returned if no parameter is passed <br>**Note: this is only applicable for VOD** | player.currentTime() |
| fullscreen(enter) | {Boolean} [optional] | true,false {Boolean} | Call the full screen API (Fullscreen API). Pseudo-full screen mode is not available when the full screen API is used. The current full screen status is returned if no parameter is passed. <br>**Note: mobile devices do not provide APIs for full screen mode, and you cannot acquire their full screen status** | player.fullscreen(true) |
| buffered() | None | 0-1 | Acquire buffer data percentage for video <br>**Note: this is only applicable for VOD** | player.buffered()  |
| destroy() | None | None | Destroy player instance [v2.2.1+] | player.destroy() |
| switchClarity() | {String} [Required] | None | Switch clarity, pass values "od", "hd", "sd" [v2.2.1+] | player.switchClarity('od')  |

>**Note:**
>**The above method is only applicable to the instantiated object of TcPlayer and can only be called after initialization (i.e., after the load event is triggered).**

## Advanced Guide
Here, we'll introduce some advanced methods for using video player SDK.

### Use an Advertising SDK
TcPlayer provides a version with integrated IMA SDK. If you need to use the advertisement feature, introduce the following code into the page.

```
<!-- Google IMA SDK  -->
<script type="text/javascript" src="//imasdk.googleapis.com/js/sdkloader/ima3.js"></script>
<!-- Use the version with integrated IMA SDK -->
<script type="text/javascript" src="//restcplayer.qcloud.com/sdk/tcplayer-web-1.0.1.js"></script>
```

You can use the advertisement feature by using adTagUrl and auth parameters. Visit `https://tcplayer.qcloud.com` to apply for an account and License information, or send an email to tcplayer@tencent.com for consultation.

```
var player = new TcPlayer('id_test_video', {
  /* Advertisement-related parameter */
  "adTagUrl": "http://ad_tag_url",	//Tags of VAST, VMAP and VAPID video ads
  "auth": {
    "user_id": "your_user_id",		//Ad account ID 
    "app_id": "your_app_id",		//Application ID 
    "license": "your_license"		//Application license
  }
});
```
>**Note:**
>For TcPlayer 2.2.0 and later versions, this document is not applicable to the version with integrated IMA SDK. tcplayer-web-1.0.1 is an independent branch.

### ES Module
TcPlayer provides ES Module version, and the module name is TCPlayer. Download URL:
```
http://imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-module-2.2.1.js
```
### Prioritize H5 for Video Playback
TcPlayer combines H5 `<video>` and Flash to play videos. By default, the player chooses the more suitable one for different playback environments.

Although browser providers have already begun to give up their support for Flash widget, most browsers in China still do not support MSE, users cannot switch to H5 `<video>` playback mode when playing FLV HLS (m3u8) videos, and RTMP videos must be played using Flash mode. For this reason, TcPlayer still enables Flash playback mode first by default, and only uses H5 `<video>` to play videos if it detects that the FLASH widget is unavailable.

Using Flash mode by default is because this mode supports the most video formats, while H5 `<video>` only supports MP4 (h.264) by default (other video formats not provided by Tencent Cloud are not discussed here), and it can support HLS (m3u8) and FLV only under certain conditions.

Starting from version 2.2.0, TcPlayer allows users to configure the attribute for playback mode priority. If you prefer H5 `<video>` for playback, you can configure the "Flash" attribute as "false", so the player will enable H5 `<video>` to play videos by default, and use Flash mode if H5 `<video>` is unavailable. If Flash widget is not detected, you will see a message: "Current system environment does not support this video format".

### Listen to Event
TcPlayer combines H5 `<video>` and FLASH to play videos. But the events triggered when playing videos using these two methods are different. In this case, we convert FLASH playback events based on the standards of H5 `<video>` to achieve unified playback event names. TcPlayer captures and transparently transmits the native events triggered by these two playback methods.

[H5 Event Reference List](https://www.w3.org/wiki/HTML/Elements/video#Media_Events)
[Flash Event Reference List](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/events/NetStatusEvent.html)

Unified event list:

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
>**Note:**
>The fullscreen event cannot be listened to if the full screen mode is enabled by using the control bar.

Events specific to the Flash mode: `netStatus`

**Note: Due to the black box feature of Flash and that H5 video playback standards are realized in different ways on different platforms, events are triggered differently and can yield different results. Be careful with these differences during the development process.**

Different events triggered on mobile device and PC Flash when video is loaded to "ready to play" status while auto-playback is disabled.
**Mobile Device:**
![Mobile Device](//mc.qcloudimg.com/static/img/ddf4e9ff5998dc84b1887fba0e94d446/image.png)
**PC Flash:**
![PC Flash](//mc.qcloudimg.com/static/img/f49d8aa8ef678b63ac73e69f254c20bb/image.png)

**Note: The differences mentioned above exist between two platforms. There are also differences between different mobile devices and applications.**

Application case: By using event listening, you can implement auto reconnection when the playback fails. [Online Example](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-reconnect.html).

## Update Log
The following shows the major version of TcPlayer after continuous update and improvement, to make it easier for users to keep track of the conditions in these versions. Some of the historical bug fixes and minor versions are not listed.

| Date | Version | Update
|-----------------|--------- |-------------------------------------------- |
| 2016.12.28 | 2.0.0 | Initial version |
| 2017.3.4 | 2.1.0 | Till 2017.6.30, TcPlayer has gone through a number of iterative development processes and has gradually become stable. Feature descriptions in current documents are all based on this version, unless specified otherwise. |
| 2017.6.30       | 2.2.0    | 1. Added parameters for controlling playback environment determination: Flash, h5_flv, x5_player; <br> 2. Adjusted the initialization logic of the player and optimized the error prompt effect; <br> 3. Added support for flv.js, which can be used to play flv videos if conditions are met; <br>4. Added support for the "x5-video-orientation" attribute; <br>5. Added playback environment determination logic. You can adjust the priority of H5 and Flash with parameter, and decide whether to enable TBS playback; <br>6. Enabled version number release method to avoid affecting the usage of previous versions; <br> 7. Optimized timestamps for triggering events (unified as standard time); <br> 8. Fixed Bugs. |
| 2017.12.7 | 2.2.1 | 1. Added the systemFullscreen parameter; <br> 2. Added the flashUrl parameter; <br> 3. Fixed the UI problem when users switch to mute after the volume is set to max; <br> 4. Fixed the problem that two clicks are needed to play the video on WeChat for iOS 11; <br> 5. Fixed the problem that the Safari 11 system style is covered; <br> 6. Adapted to the condition that X5 kernel will trigger "seeking", but not "seeked"; <br> 7. Fixed the problem of currentTime configuration failure when the progress bar is dragged to the starting position; <br> 8. Added the capability of switching the clarity while keeping the volume unchanged; <br> 9. Fixed the problem that the player width cannot be determined when the page width is 0; <br> 10. Added the capability of completely terminating player node for "destroy" method. |
| 2017.12.20 | 2.2.1 | 1. Added the capability of setting the message clarity; <br> 2. Added the capability of setting the default clarity; <br> 3. Supported clarity switch methods. |
