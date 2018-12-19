## Overview

TC Player is mainly used to play audio/video streams in mobile phone browsers and PC browsers. With this player, you can share your videos on social platforms such as WeChat Moments and Weibo without installing the Apps.

This document is suitable for developers with a knowledge of the JavaScript language.

## Basics
It is required to learn about the following basic knowledge before docking the player:

- **LVB and VOD**
  A video source in LVB scenario is real-time. The address loses its function if the VJ stops broadcasting. Besides, since the LVB is done in real time, there is no progress bar when the player plays LVB videos.
  In VOD scenarios, video source comes from a file on the server. You can play the video whenever you like as long as the provider doesn't delete this file. Since the entire video resides on the server, a progress bar is shown when the player plays the video.

- **Supported Protocols**
  Playing videos using web player depends on browsers, rather than the codes in web pages. For this reason, the compatibility will be lower than we expected. The fact is that **not all mobile phone browsers can yield expected performance**, some of the mobile phone browsers don't even support video playback at all.

 The most common video source addresses used to play videos on web pages are addresses ending with "m3u8". We call them HLS (HTTP Live Streaming), a standard created by Apple. Currently, this format has the best compatibility with various mobile phone browser products thanks to Apple's influence. However, this format has a drawback: a big delay of 20-30 seconds. Even so, we don't have any other choices for mobile phone browsers.

 This situation looks better on PC, because PC browsers still use flash controls, which supports various video source formats. Besides, the flash controls for different browsers are all developed by Adobe itself, thus they have good compatibility. (Just a reminder for you: Google has recently disabled Flash in Chrome.)
![](https://mc.qcloudimg.com/static/img/e59d010141e8fb6b063c180cb16bae65/image.png)


## Docking

### Step 1: Page Preparation
Introduce the initialization script to the pages that need to play videos (including PC or H5).
```
<script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.0.js" charset="utf-8"></script>;
```

>Note: **You can't perform debugging directly using the local pages</font> because TC Player cannot handle cross-domain issues in such situations.**

### Step 2: Place Container into HTML

 Place a "container" in the page where you want to display the player. That is, place a div and give it a name such as:  id_test_video. When this is done, all videos will be rendered in this container. You can control the container size through the div attributes. Example codes:

```
<div id="id_test_video" style="width:100%; height:auto;"></div>
```

### Step 3: Dock with Video Playback
The next step is to write the JavaScript code, which is used to pull audio/video streams from the specified URL address and display the video in the container added in step 2.

#### 3.1 A Simple Playback
A typical LVB URL address is shown below, which is based on HLS (m3u8) protocol. Players such as VLC can directly open this URL to view the video as long as the VJ is still broadcasting:
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8      // m3u8 playback address
```
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)

Now, we need to play the video of this URL on mobile phone browsers, we can write the JavaScript code as shown below:
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8", //Replace the address with a functional playback address.
"autoplay" : true,      //Most mobile browsers including safari on iOS do not support auto video playback.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//Video display width. Use the video definition width if possible.
"height" : '320'//Video display height. Use the video definition height if possible.
});
```

This code segment can be used to play LVB videos based on HLS (m3u8) protocol on PC and mobile phone browsers. As mentioned before, videos based on HLS (m3u8) protocol have good compatibility (some Android phones still do not support them), but these videos have a big delay about over 20 seconds.

#### 3.2 Achieve Lower Delay on PC
So now we can make it better on PC as PC browsers support flash. We can write the code as shown below:
```javascript
var player =  new TcPlayer('id_test_video', {
"m3u8": "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"flv": "http://2157.liveplay.myqcloud.com/live/2157_358535a.flv", //Add an flv playback address to play videos on PC platforms. Replace this with functional playback address.
"autoplay" : true,      //Most mobile browsers including safari on iOS do not support auto video playback.
"coverpic" : "http://www.test.com/myimage.jpg",
"width" :  '480',//Video display width. Use the video definition width if possible.
"height" : '320'//Video display height. Use the video definition height if possible.
});
```
Compared with the previous code, we added an flv playback address. When the TC Player detects that the current browser is a PC browser, it will choose the flv linkage to achieve lower delay.

The condition is that both FLV and HLS (m3u8) address can stream the video. You don't have to consider this problem if you use Tencent Cloud VOD service because every VOD channel of Tencent Cloud supports three protocols: FLV, RTMP and HLS (m3u8).

#### 3.3 Cannot Play the Video?
Failing to play video is usually caused by the following reasons:

-  **(Reason 1) Invalid Video Source**
     If it's an LVB URL, you need to check if the VJ has stopped streaming and isn't in "Broadcasting" status anymore. You can send a notification to viewers via floating window: "The VJ has left".
     If it's a VOD URL, you need to check if the file to be played is still on the server. For example, if someone else has deleted the playback address from the VOD system.

-  **(Reason 2) Local Web Page Debugging**
     Currently, TC Player does not support debugging in local web page (opening the page where video is played using "file://" protocol). This is because of cross-domain security restrictions of browsers. Simply placing a file such as "test.html" in Windows and testing video playback using the file will definitely end up in failure. You need to upload the file to a server to perform the test. Of course, frontend engineers can achieve local testing by setting up a local proxy for the online web page through reverse proxy. This is a feasible method for local debugging.

-  **(Reason 3) Mobile Phone Compatibility Problem**
     Common mobile phone browsers do not support FLV and RTMP addresses (The newest QQ Browser can play videos based on FLV protocol, but this is not widely used). You can only use HLS (m3u8) addresses.

-  **(Reason 4) Cross-Domain Security Problem**
     PC browsers achieve video playback based on flash controls. Those who did flash development before would know that the flash control performs cross-domain access check. You will encounter this problem if cross-domain policy is not deployed on the server where the video you want to play resides in. Solution: Find the cross-domain configuration file "crossdomain.xml" under the root domain name of the video server and add domain name "qq.com" to it:
```xml
<cross-domain-policy>
<allow-access-from domain="*.qq.com" secure="false"/>
</cross-domain-policy>
```

### Step 4: Configure Cover Image for the Player
You should have noticed the parameter "coverpic" in the sample code above. Here, we will explain how to use this attribute in details.

Note: The cover image may become invalid in certain mobile device playback environments because these environments are relatively more complicated compared to PC, and different browsers and App Webviews achieve H5 videos by different means. If you encounter such a situation, feel free to send feedback to our technical support (the feedback should include key information such as system and the version of your browser or App) and we will provide assistance as much as possible.

#### 4.1 Easily Configure Cover Image
You can pass the address of an image to coverpic as the player's cover image. The image will be displayed in the center of the player area, with its actual resolution.

```
"coverpic" : "http://www.test.com/myimage.jpg"
```
#### 4.2 Configure Cover Image Display Style
You can also pass an object for coverpic and configure the display style (style) and image address (src) for the cover image in the object.<br>

Three styles are supported:
- "default": display the image in the center, with its actual resolution.
- "stretch": stretch the image to fill up to entire player area. This may distort the image.
- "cover": horizontally stretch the image while keeping its ratio to fill up the player area. The image may not be fully displayed in the area.

```
"coverpic" : {"style":"stretch", "src":"http://www.test.com/myimage.jpg"}
```
#### 4.3 Implementation Case

This is an online sample code segment which uses "cover" method to display the cover image. Right-click in a PC browser and select "View page source" to view the code implementation of the page:
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-cover.html)

**Note: The configured cover image may become invalid in certain mobile devices. For more information, please see the FAQ section.**

### Step 5: Multi-Definition Support
#### 5.1 Principle
We all know that you can choose different definitions for videos on Youku.com, Tudou.com or Tencent. How do we achieve this feature?
![](//mc.qcloudimg.com/static/img/5769d1bd31db2d9ed258d0bf62be3f0f/image.png)

First, you should know that **the players cannot change a video's definition**</font>, there is only one definition where the video source is generated, which is called **Original**. The original video has different encoding formats and encapsulation formats, and Web pages do not support all video playback formats. In VOD scenarios, the encoding format for videos must be H.264, and encapsulation format must be mp4 or flv.

So, how to achieve multi-definition selection?  This is where the Video Cloud comes into play:
- In LVB scenarios, the original video from VJ will be transcoded in real time in Tencent Cloud, then videos transcoded with different channels are distributed, such as the commonly seen **High Definition (HD)** and **Standard Definition (SD)**. Video from each channel has its own corresponding address:
```
http://2157.liveplay.myqcloud.com/2157_358535a.m3u8          // Original
http://2157.liveplay.myqcloud.com/2157_358535a_900.m3u8      // High Definition
http://2157.liveplay.myqcloud.com/2157_358535a_550.m3u8      // Standard Definition
```

- In VOD scenarios, once a video file is uploaded to Tencent Cloud, you can perform operation to transcode the video and generate videos of different definitions, such as the commonly seen **High Definition (HD)** and **Standard Definition (SD)**. Note that the uploaded original video is not transcoded by Tencent Cloud and cannot be played directly.
```
http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8         // Original, replaced with transcoded video of Ultra High Definition
http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8      // High definition
http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8      // Standard definition
```
Note: the uploaded original video is not transcoded by Tencent Cloud and cannot be played directly.

#### 5.2 Code Implementation
The following code segment allows player to support multiple definitions. In other words, it displays options used to select different definitions on the player's user interface.

```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"      : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f240.m3u8",//Replace the address with a functional playback address.
"m3u8_hd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f230.av.m3u8",
"m3u8_sd"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f220.av.m3u8",
"autoplay"  : true,      //Most mobile browsers including safari on iOS do not support auto video playback.
"coverpic"  : "http://www.test.com/myimage.jpg",
});
```

#### 5.3 Implementation Case
This is an online sample code segment which uses multi-definition selection and switching features. Right-click in a PC browser and select "View page source" to view the code implementation of the page:
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-clarity.html?autoplay=true)

You will see this under normal circumstances:
![](https://mc.qcloudimg.com/static/img/bc4c39cd88f1c17bec28fe1796fb691a/image.png)

**PC now supports video playback in multiple definitions as well as definition switching. This is currently not supported on mobile devices.**

### Step 6: Support Ad Access

Advertisement features are called when the player is initialized. Example:

```javascript
var player = new TcPlayer('id_test_video', {
  /* Advertisement-related parameter */
  "adTagUrl": "http://ad_tag_url",
  "onAdError": function(error) {},
  "auth": {
    "app_id": "your_app_id",
    "user_id": "your_user_id",
    "license": "your_license"
  },
  /* logo parameter */
  "logo": {
    "image": 'https://www.tencent.com/images/global/logo.png',
    "link": 'http://www.tencent.com',
  },
  /* Adaptive layout */
  "autoResize": false, // Adaptive width is the container width, aspect ratio is maintained as the original ratio of width*height.
  /* Other parameter */
  "width": '480', "height": '320',
  "m3u8": "http://video_url",
});
```


### Step 7: Change Player Logo

If you have already paid to use the player, your customers can upload their own logos. 
Maximum size is 40pt * 40pt,keep the logo in the middle of 16pt * 16pt.

### Parameters of Other Features

| Parameter     | Type             | Default Value | Parameter Description                    |
| ------------- | ---------------- | ------------- | ---------------------------------------- |
| adTagurl      | URL String       | None          | VAST advertisement protocol URL address  |
| onAdError     | Function         | error         | Pass a function, which is called back when an advertisement error occurs.  `error`: { ima.AdErrorEvent } type is AdErrorEvent protocal error. Document:  [https://developers.google.com/interactive-media-ads/docs/sdks/html5/v3/apis#ima.AdErrorEvent](https://developers.google.com/interactive-media-ads/docs/sdks/html5/v3/apis#ima.AdErrorEvent) |
| auth          | Object           | None          | Authentication target. Authentication information you need to pass includes app_id, user_id, license. You can't call advertisement feature if any information is missing. Refer to Tencent Cloud for relevant information and pass the required information when calling the player |
| auth▪ app_id  | String           | None          | Indicates whether this is a TC Player customer. The information is used for player authentication |
| auth▪ user_id | String           | None          | Indicates how many user_ids can be generated under a customer to be used for different services. This information is used for player authentication |
| auth▪ license | String           | None          | Indicates whether to purchase advertisement feature. This information is used for player advertisement feature authentication |
| logo          | Object           | None          | Relevant logo object which declares the image to be used and which URL to redirect to when the logo is clicked |
| logo▪ image   | Image URL String | None          | Image address                            |
| logo▪ link    | URL String       | None          | Redirection address                      |
| autoResize    | Boolean          | false         | Whether to use adaptive layout. Default is false. If this is enabled, the adaptive width will be the parent container width of the DOM node you passed, while the aspect ratio will be maintained as the original width*height ratio |



### Step 8: Customize Error Notification

It's possible that you're not satisfied with our default error notifications, such as "Network error, check your network configuration or if the playback link is correct" or "Video decoding error", because they may seem too boring. For this reason, TC Player supports notification customization:

#### 8.1 Code Implementation
The following code is the core code used to allow the player to support custom notifications. The configured notifications are mainly placed in the "wording" attribute.
```javascript
var player = new TcPlayer('id_test_video', {
"m3u8"   : "http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8",//Replace the address with a functional playback address.
"autoplay" : true,      //This capability is not supported in safari browser on iOS.
"coverpic" : "http://www.test.com/myimage.jpg",
"wording": {
    2032: "Video request failed, check your network.",
    2048: "m3u8 file request failed, this may be caused by network error or cross-domain issue."
}
});
```

#### 8.2 Implementation Case
This is an online sample code segment which uses custom notification feature. Right-click in a PC browser and select "View page source" to view the code implementation of the page:
[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?m3u8=http://2527.vod.myqcloud.com/2527_b393eb1.f230.av.m3u8)

#### 8.3 Error Code Reference Table
| Code | Notification                             | Description                              |
| ---- | ---------------------------------------- | ---------------------------------------- |
| 1    | Network error, check your network configuration or if the playback link is correct | (Error prompted by H5)                   |
| 2    | Network error, check your network configuration or if the playback link is correct | Web player cannot decode the video format (error prompted by H5) |
| 3    | Video decoding error                     | (Error prompted by H5)                   |
| 4    | Current system environment does not support this video format | (Error prompted by H5)                   |
| 5    | Current system environment does not support this video format | The player detects that the current browser environment does not support the passed video. The reason may be that the current browser does not support MSE, or Flash plug-in is not enabled |
| 10   | Do not use the player under "file" protocol, or video playback may fail |                                          |
| 11   | Used parameter is incorrect. Check the player calling code |                                          |
| 12   | Enter video playback address             |                                          |
| 13   | The LVB has ended, come back later       | The (NetConnection.Connect.Closed) event is triggered during a normal RTMP playback (error prompted by Flash) |
| 1001 | Network error, check your network configuration or if the playback link is correct | Network disconnected ( NetConnection.Connect.Closed) (error prompted by Flash) |
| 1002 | Failed to acquire video, check if the playback link is valid | Failed to pull playback file (NetStream.Play.StreamNotFound), this may be caused by a server error or that the video file does not exist (error prompted by Flash) |
| 2032 | Failed to acquire video, check if the playback link is valid | (error prompted by Flash)                |
| 2048 | Failed to load video file, cross-domain access is rejected | Failed to request for m3u8 file, this may be caused by network error or cross-domain issue (error prompted by Flash) |

Note:<br>
Code 1-4 are native HTML5 events.<br>
Due to the black box feature of Flash and the uncertainty of H5 video playback standards, the error notifications will be irregularly updated.

## Source Code Reference
This is an online sample code segment. Right-click in a PC browser and select "View page source" to view the code implementation of the page:

[http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true)

You can also use it to test your player. Append the address of the video to be played after the link and refresh to play the video:

```
http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html?autoplay=true&m3u8=http://2527.vod.myqcloud.com/2527_b3907044441c11e6a46d294f954f93eb.f230.av.m3u8
```

## Parameter List
Here are all parameters supported by the player as well as their detailed description.

| Parameter             | Type     | Default Value   | Parameter Description
|-----------------|--------- |--------  |-------------------------------------------- |
| m3u8            | String   | None       |  m3u8 playback URL (original)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535a.m3u8 |
| m3u8_hd         | String   | None       |  m3u8 playback URL (high definition)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535ahd.m3u8 |
| m3u8_sd         | String   | None       |  m3u8 playback URL (standard definition)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535asd.m3u8 |
| flv             | String   | None       |  flv playback URL (original)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535a.flv |
| flv_hd          | String   | None       |  flv playback URL (high definition)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535ahd.flv |
| flv_sd          | String   | None       |  flv playback URL (standard definition)  <br> Example:  http://2157.liveplay.myqcloud.com/2157_358535asd.flv |
| mp4             | String   | None       |  mp4 playback URL (original)  <br> Example:  http://200002949.vod.myqcloud.com/200002949_b6ffc.f0.mp4 |
| mp4_hd          | String   | None       |  mp4 playback URL (high definition)  <br> Example:  http://200002949.vod.myqcloud.com/200002949_b6ffc.f40.mp4 |
| mp4_sd          | String   | None       |  mp4 playback URL (standard definition)  <br> Example:  http://200002949.vod.myqcloud.com/200002949_b6ffc.f20.mp4 |
| rtmp            | String   | None       |  rtmp playback URL (original)  <br> Example:  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88 |
| rtmp_hd         | String   | None       |  rtmp playback URL (high definition)  <br> Example:  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88hd |
| rtmp_sd         | String   | None       |  rtmp playback URL (standard definition)   <br> Example:  rtmp://2157.liveplay.myqcloud.com/live/2157_280d88sd |
| width           | Number   | None       | Required parameter, used to configure player width (in pixels)   <br> Example:   640   |
| height          | Number   | None       | Required parameter, used to configure player height (in pixels)   <br> Example:  480  |
| volume          | Number   | 0.5      | Used to configure initial volume. Range: 0-1 [v2.2.0+]    <br> Example:  0.6   |
| live            | Boolean  | false    | Required parameter, used to configure whether the video is LVB video. This determines whether to render certain controls such as the time axis, and is used to differentiate between VOD and LVB processing logics  <br> Example:   true  |
| autoplay        | Boolean  | false    | Whether to enable auto-playback<br>Note: This option is only effective on most PC platforms  <br> Example:   true |
| coverpic        | String / Object | None | Preview cover image. You can either pass an image address, or an object containing image address (src) and display style (style). <br>Available styles: <br>"default": image is displayed 1:1 in the center <br>"stretch": stretch the image to fill up the player area. This may distort the image <br>"cover": horizontally stretch the image while keeping its ratio to fill up the player area. The image may not be fully displayed in the area    <br> Example:   "http://www.test.com/myimage.jpg" <br>Or<br>{"style": "cover", "src": "http://www.test.com/myimage.jpg"} |
| controls        | String   | "default" | "default": display default controls. "none": do not display controls. "system": display system controls on mobile devices Note: You need to configure this as "system" if you want to use system full screen mode on mobile devices. The default full screen solution uses Fullscreen API + pseudo-full screen [Example](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-consoles.html)  <br> Example:   "system"  |
| flash           | Boolean  | true     | Whether to prioritize flash to play videos. <br>Note: this option is only effective on PC platforms [v2.2.0+]  <br> Example:   true  |
| h5_flv          | Boolean  | false    | Whether to enable flv.js to play flv videos. If this is enabled, players will use flv.js to play flv videos in browsers that support MSE. However, since not all such browsers can use flv.js, players do not enable this attribute by default. [v2.2.0+]   <br> Example:  true |
| x5_player       | Boolean  | false    | Whether to enable TBS to play flv videos. If this is enabled, players will directly transmit the flv playback addresses to `<video>` to play in TBS mode (for example, WeChat on Android or QQ Browser). [TBS Video Playback](https://x5.tencent.com/tbs/product/video.html) [v2.2.0+]   <br> Example:   true   |
| x5_type         | String   | None       | Declare to enable single-layer H5 player by using the "x5-video-player-type" attribute of "video". Available value: h5 (this is an experimental attribute of TBS kernel, and is not supported for non-TBS kernels). [Standard for Docking TBS H5 Single-Layer Player](https://x5.tencent.com/tbs/guide/video.html)   <br> Example:  "h5"  |
| x5_fullscreen   | String   | None       | Declare whether to enter TBS full screen mode when playing a video, by using the "x5-video-player-fullscreen" attribute of "video". Available value: true (this is an experimental attribute of TBS kernel, and is not supported for non-TBS kernels).    <br> Example:  "true"   |
| x5_orientation  | Number   | None       | Declare the orientation supported by TBS player, using the "x5-video-orientation" attribute of "video". Available values: 0 (landscape), 1: (portrait), 2: (landscape &verbar; portrait rotates with mobile phone movement).  (This is an experimental attribute of TBS kernel, and is not supported for non-TBS kernels) [v2.2.0+]  <br> Example:   0   |
| wording         | Object   | None       | Custom notification   <br> Example:   { 2032:  'Video request failed, check your network'}  |
| listener        | Function | None       | Event monitor callback function. A JSON object is passed to this function  <br> Example:  function(msg){<br>//Event processing <br>}  |

## List of Instance Methods
Here's a list of methods supported by player instances.

| Method             | Parameter                   | Returned Value                       | Description                                    |  Example
|-----------------|------------------------|----------------------------- |----------------------------------------|---------------------|
| play()           | None                     | None                           | Start video playback                             | player.play() |
| pause()          | None                     | None                           | Pause video playback                             | player.pause() |
| togglePlay()     | None                     | None                           | Toggle video playback status                          | player.togglePlay() |
| mute(muted)      | {Boolean} [optional]       | true,false {Boolean}         | Toggle mute status. The current mute status is returned if no parameter is passed      | player.mute(true) |
| volume(val)      | {int} Range: 0-1 [optional]  | Range: 0-1                    | Configure volume. The current volume is returned if no parameter is passed             | player.volume(0.3) |
| playing()        | None                     | true,false {Boolean}         | Return whether the video is currently being played                         | player.playing() |
| duration()       | None                     | {int}                       | Acquire video duration <br>Note: this is only applicable for VOD | player.duration() |
| currentTime(time) | {int} [optional]           | {int}                       | Configure video playback time point. The currently playback time point is returned if no parameter is passed <br>Note: this is only applicable for VOD | player.currentTime() |
| fullscreen(enter)| {Boolean} [optional]       | true,false {Boolean}         | Call the full screen API (Fullscreen API). Pseudo-full screen mode is not available when the full screen API is used. The current full screen status is returned if no parameter is passed <br>Note: mobile devices do not provide APIs for full screen mode, and you cannot acquire their full screen status | player.fullscreen(true) |
| buffered()       | None                     |  0-1                        | Acquire buffer data percentage for video <br>Note: this is only applicable for VOD | player.buffered()  |


## Advanced Guide
Here, we'll introduce some advanced methods for using video player SDK.

### Prioritize H5 for Video Playback
TC Player combines HTML5 `<video>` and Flash to play videos. By default, the player chooses the more suitable one for different playback environments.

Although browser providers have already begun to give up their support for Flash plug-in, most browsers in China still do not support MSE, users cannot switch to H5 `<video>` playback mode when playing FLV HLS (m3u8) videos, and RTMP videos must be played using Flash mode.
For this reason, TC Player still enables Flash playback mode first by default, and only uses H5 `<video>` to play videos if it detects that Flash plug-in is unavailable.

Using Flash mode by default is because this mode supports the most video formats, while H5 `<video>` only supports MP4 (h.264) by default (other video formats not provided by Tencent Cloud are not discussed here), it can only support HLS (m3u8) and FLV under certain conditions.

Starting from 2.2.0, TC Player allows users to configure the attribute for playback mode priority. If you want to use H5 `<video>` as preferential playback mode, you can configure the "flash" attribute as "false", so the player will enable H5 `<video>` to play videos by default, and use Flash mode if H5 `<video>` is unavailable. If Flash plug-in is not detected, you will see a notification: "Current system environment does not support this video format".


### Monitor Event
TC Player combines HTML5 `<video>` and Flash to play videos, so the events triggered when playing videos using these two methods are mostly the same. Based on the standards of H5 `<video>`, we converted Flash playback events to a certain degree to achieve unified playback event names. TC Player captures and transparently transmits the original events triggered when playing videos using these two playback methods.

[H5 Event Reference List](https://www.w3.org/wiki/HTML/Elements/video#Media_Events)
[Flash Event Reference List](http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/events/NetStatusEvent.html)

Unified event list

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
Note:
* The fullscreen event cannot be monitored if full screen mode is enabled by using the system control bar.

Events specific to Flash mode
```
netStatus
```

Note: Due to the black box feature of Flash and that H5 video playback standards are realized in different ways on different platforms, events are triggered differently and can yield different results. You can keep an eye out for these differences while developing.<br>

Different events triggered on mobile device and PC Flash when video is loaded to "ready to play" status while auto-playback is disabled
Mobile device:
![Mobile Device](//mc.qcloudimg.com/static/img/ddf4e9ff5998dc84b1887fba0e94d446/image.png)
PC Flash:
![PC Flash](//mc.qcloudimg.com/static/img/f49d8aa8ef678b63ac73e69f254c20bb/image.png)

Note: The differences above exist between two platforms. There are also differences between different mobile devices and Apps.<br>

Application case:

By using event monitoring, you can implement auto-reconnection when playback fails. [Online Example](http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-reconnect.html)

## Update Log
We provide major version introductions in the process of continuous update and perfection of TC Player, to make it easier for users to keep track of the conditions in these versions. Some of the historical bug fixes and minor versions are not listed.

| Date             | Version     | Update
|-----------------|--------- |-------------------------------------------- |
| 2016.12.28      | 2.0.0    | Initial version  |
| 2017.3.4        | 2.1.0    | Till 2017.6.30, TC Player has gone through multiple iterative development processes and has finally become stable. Feature descriptions in current documents are all based on this version, unless specified otherwise.   |
|2017.6.30       | 2.2.0    | 1. Added parameters for controlling playback environment determination:  flash, h5_flv, x5_player. <br>2. Adjusted player initialization logic and optimized error notification effect. <br>3. Added support for flv.js, which can be used to play flv videos if conditions are met<br>4. Added support for the "x5-video-orientation" attribute,<br> 5. Added playback environment determination logic. Users can adjust the priority of H5 and Flash through parameter, and decide whether to enable TBS playback. <br>6. Version number publication method is used to prevent causing impact to users that use previous versions. <br> 7. Optimized timestamps for triggering events (unified as standard time). <br>8. Bug fixes |

## FAQs

- **Which browsers are supported by TC Player?**

    TC Player has been tested to support the following browsers: PC: IE 10+, Edge, Chrome, Firefox, QQ Browser, MAC Safari. Mobile: Android 4.4+, iOS 8.0+, WeChat, Mobile QQ, QQ Browser, Chrome, Safari.
    To support IE 8 and IE 9, you must introduce the Polyfill script before introducing the player script. As shown below:
    ```
    <!--[if lt IE 9]>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-shim.js" charset="utf-8"></script>
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/libs/es5-sham.js" charset="utf-8"></script>
    <![endif]-->
    <script src="//imgcache.qq.com/open/qcloud/video/vcplayer/TcPlayer-2.2.0.js" charset="utf-8"></script>;
    ```

- **On mobile devices, the video does not go into full screen when TC Player is switched to full screen mode, and browser interface is still displayed?**

    First, you should know that the full screen solution provided by TC Player is to use Fullscreen API + pseudo-full screen. If the browser supports Fullscreen API, then the video container will fill up the entire screen when the player goes into full screen mode, and the control bar will be the control bar provided by TC Player, as shown in the image.
    ![](//mc.qcloudimg.com/static/img/df40b2b49390f8fc314fd040ba026156/image.png)
    (Android Chrome)

    If the browser does not support Fullscreen API, then pseudo-full screen mode will be used, as shown in the image:
    ![](//mc.qcloudimg.com/static/img/d5746d9bef48b411c3bac576fe6925b1/image.png)![](//mc.qcloudimg.com/static/img/1e20288d6f69a5cf7a886f95edd40ec3/image.png)
    (Left: WeChat on Android. Right: WeChat on iOS)

    The control bars displayed in these two full screen modes are both TC Player-provided control bars, and you enter these modes by clicking on the full screen button on the control bar or by using the method provided by TC Player.
    But the control bar provided by TC Player may not always be displayed on mobile devices, as their webview hijacks the video playback in most situations and uses the control bar provided by webview. In this case, the TC Player control bar will not be displayed, and you cannot use the full screen solution provided by TC Player. As shown in the image:
    ![](//mc.qcloudimg.com/static/img/d027ca6fce35059e05428128b9823d70/image.png)![](//mc.qcloudimg.com/static/img/b28d69f15a60321d1a6e2b3a93b53038/image.png)
    (Left: WeChat on Android, where video playback is hijacked by TBS. Right: iOS, where video playback is hijacked by QQ Browser)
    Upon entering full screen mode:
    ![](//mc.qcloudimg.com/static/img/0ab29e27c7aa89587cec96d7530ab4f7/image.png)![](//mc.qcloudimg.com/static/img/a260a96ed73d2a4d7d0260c4584a128a/image.png)
    (Left: WeChat on Android. Right: QQ Browser on iOS)
    As you can see, the control bar is different from the TC Player one. No APIs are provided for JS in this full screen mode, so TC Player cannot realize this mode.
    (We usually refer to the full screen mode where the video covers the whole screen as **System Full Screen**, and the mode where the video covers the whole browser page area as **Pseudo-Full Screen**.)
    To sum up, if you can see the browser interface after going into full screen mode, then it is pseudo-full screen. You can only use the system-provided control bar if you want to go into system full screen mode on mobile devices. You may choose the control bar type by using the "controls" attribute of TC Player.

- **Why is the screen stretched when the video is played in H5?**

    Video stretching is not supported when playing in H5. Check if the player container width/height configuration is correct.

- **Why can't I cover my own div on top of the video?**

    Different browsers implement the `<video>` tag in different ways. For example, if you open a web page in QQ or WeChat (on Android system), then it's very likely that X5 browser kernel is used (the kernel which is bound with QQ or WeChat, a.k.a. the QQ Browser kernel). For certain reasons, the QQ Browser team implemented such a solution that "the video `<video>` must be placed in the top layer"(for more relevant information, please see [QQ Browser Documentation](http://x5.tencent.com/guide?id=2009)). However, due to a coordinations recently, the QQ Browser Team is gradually changing this policy. This issue may have already been solved in the latest X5 browser kernel when you read this document.

- **Why is the configured cover image not working?**

    This is the same problem with the previous one ("cannot cover div on top of the video"). The cover image cannot be displayed as long as the browser does not allow elements to cover up the `<video>` tag.

- **Why is video displayed in full screen mode by default in certain mobile browsers?**

  If the video is played through inline playback inside the App (that is, your own App encapsulates an iOS webview control which is used to display web pages. In this mode, you can customize the details of webview, which may have different performance from standard Safari browser), you can configure the "webkit-playsinline" attribute for the `<video>` tag in HTML (or configure the "playsinline" attribute if you're using iOS 10), then configure "allowsInlineMediaPlayback" for webview. In this way, videos will be played in non-full screen mode (inline playback) when you open pages in the App.

  If you open the page in Safari on iOS 10, you can realize non-full screen playback (inline playback) by using the method above (configure "playsinline" attribute for the `<video>` tag). You cannot disable auto full screen playback for Safari on systems below iOS 10. This attribute is already added for our browser. It only needs to be supported by the devices.

  For Android devices, it is widely known that there are many different customized versions for Android systems, and each system realizes the `<video>` tag in a different way, without a universal standard. For this reason, video playback capabilities on Android have much lower consistency compared with iOS. The "webkit-playsinline playsinline" attribute is already added for the player according to current universal method. It only needs to be supported by the devices.

- **Why can't I realize auto video playback in mobile browsers?**

  There are only two ways to realize auto video playback on mobile web: by configuring the "autoplay" attribute for the `<video>` tag, or by calling the "play()" method provided by the `<video>` tag. However, auto video playback has always been prohibited on mobile web, thus the universal method now is to trigger video playback by users actions. For example, monitor ontap events of users and call the "play()" method. It is possible that certain customized webviews support the "autoplay" attribute of the `<video>` tag, or can realize auto video playback by calling other special functions. Videos can be played automatically when you open the pages in these webviews. Our player will add the "autoplay" attribute for the `<video>` tag if "autoplay" is configured as "true". Now we only need the devices to support this attribute.

- **Why does the Flash player have two play buttons in Chrome on PC?**

  Flash will no longer be automatically played starting from Chrome 42 (Google purchased WebRTC and made it open-source for a reason). Chrome only plays major Flash contents automatically, while the other Flash contents will be paused, unless users enable them manually.

- **Why can I play LVB videos in browsers on PC, but not on mobile devices?**

    Currently, only hls (m3u8) protocol is supported for playing LVB videos in mobile browsers. Thus, you need to confirm whether the LVB stream pulling addresses contain URL for pulling hls (m3u8) stream. The video cannot be played on mobile phones if you only provide an flv or rtmp address for the player.


