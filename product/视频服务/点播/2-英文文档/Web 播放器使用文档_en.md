## Foreword
This document describes how to use the Web Player of Tencent Cloud VOD service, helping users quickly integrate with self-built Web Apps to achieve the playback feature via flexible APIs. This document is suitable for developers with basic Javascript knowledge.
## Capability Overview
Tencent Cloud VOD WEB Player achieves video playback using HTML5 `<video>` tag and Flash. If the browser does not hijack video playback, a multi-platform unified video playback can be realized. In combination with the Tencent Cloud VOD service, it provides Hotlink protection, HLS encrypted playback and other features.

### Supported Video Formats

| Playback Format | PC Browser | Mobile Browser |
|------------|-----------------------------------|---------------------------------------|
| HLS (m3u8) | IE 11/10/9/8 with Flash enabled | Android 4+ and iOS native browsers |
| MP4 | IE 8 with Flash enabled | Android 4.4+ and iOS native browsers |

### Supported Platforms
**PC**: Latest modern browsers (Chrome, Firefox, Safari, Edge, and QQ browsers) and conventional browsers (IE11/10/9/8 with Flash enabled) are supported. For conventional browsers on Win7, only IE8 is supported.
**Mobile**: All browsers applying the HTML5 `<video>` standard are supported, such as Android Chrome, iOS Safari, WeChat, Mobile QQ, and Mobile QQ browser.
When you use this player, the same code can adapt itself to PC/mobile browser, which means the player automatically selects the optimal playback method according to the platform it runs on. For example, in the IE11/10/9/8 browser, a Flash player will be used as a substitute of HTML5 to play HLS. In Chrome and other modern browsers, HTML5 technology is preferred for video playback. In mobile browsers, HTML5 technology is used for video playback.
### VOD Transcoding Service
Since MP4 and HLS (m3u8) formats are widely supported for both PC and mobile browsers, Tencent Cloud VOD platform always publishes the uploaded videos in these formats.
## Preparations
### Step 1: Activate the service
Sign up for a Tencent Cloud account at [Tencent Cloud official website](https://cloud.tencent.com/), and activate the **VOD** service.
### Step 2: Upload files
After VOD service is activated, go to [VOD Management](https://console.cloud.tencent.com/vod/videolist) to upload new video files. The activated VOD service is required for this step.
### Step 3: Obtain fileID and appID
After the video is uploaded and transcoded, you can find the fileID (the most basic information for the player to play videos) in the Video Management page. The appID can be found in the Video Management page. In the figure below, the ID on the left is the video fileID, while the other one is the appID.
![](//mc.qcloudimg.com/static/img/fcad44c3392b229f3a53d5f8b2c52961/image.png)
## Initializing Web Player
After the preparation is complete, you can add a video player to your web page following the 3 steps below.
### Step 1: Introduce files in the page
Introduce player style and script files to the appropriate positions
```
 <link href="//imgcache.qq.com/open/qcloud/video/tcplayer/tcplayer.css" rel="stylesheet">
 <script src="//imgcache.qq.com/open/qcloud/video/tcplayer/tcplayer.min.js"></script>
```
### Step 2: Place the player container
Place a player container in the page where you want to display the player. For example, add the following code into index.html. The container ID, width and height can be customized.
```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playinline x5-playinline>
</video>
```
>**Notes:**
> * The player container must has a `<video>` tag.
> * The player-container-id in the example is the ID of the player container and can be set by users.
> * It is recommended to set the size of the player container area using CSS, which is more flexible than the attribute setting, and can achieve full screen, container self-adaptation and other effects.
> * The attribute "preload" in the example specifies whether to load the video after the page is loaded. It is usually set to "auto" for faster video playback. Other available values include meta (indicating only metadata is loaded when the page is loaded) and none (indicating video is not loaded when the page is loaded). The mobile does not automatically load the video due to system limitations.
> * playsinline, webkit-playinline, and x5-playinline are used for in-line playback when the standard mobile browser does not hijack video playback. Here is an example. Please use it as needed.

### Step 3: Initialize code
Add the following initialization script to the page initialization code and enter the fileID and appID obtained in the preparation.
```
var player = TCPlayer('player-container-id', { // player-container-id is the player container ID, which must be the same as in html.
    fileID: '4564972818956091133', // Enter the fileID of the video to be played (Required)
    appID: '1253668508' // Enter the appID of the VOD account (Required)
  });
```
>**Note:**
>* The video to be played must be transcoded by Tencent Cloud, because the original video may not be played in the browser.

### Complete example page:
[Sample Code Link](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-base.html)
## How to Use
The following describes the features of the player, including best practices and notes.
### Setting Player Size
Here are some methods to set the player size:

* Set the width and height attributes of `<video>` tag. The two attributes are measured in pixels rather than percentage (e.g. width = "100px" or width = 100).
* Set the size via CSS. Values in pixels/percentages are supported​(e.g. width:"100px" or width:"100%").

If the width and height are not set, the display size of the player will be set based on the obtained video definition. If the size of the visible area of the browser is smaller than the video definition, the player area will exceed the browser's viewable area, so it is recommended not to do so. The best practice is to set the player size via CSS.
CSS can be used to achieve full screen, container self-adaptation and other effects.

Example:
[Setting Size via CSS](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-size.html)
[Covering Visible Area of Web Page](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-size-full-viewport.html)
[Equal-Ratio Adaptation](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-size-adaptive.html)

### Playback at Multiple Definitions
(1) Set multiple definitions for transcoding in the console, as shown below
![](https://mc.qcloudimg.com/static/img/b2c4b5d61ae28cb4558e15bcbcb3bd87/image.png)

(2) After the video is transcoded, multiple files with different definitions are generated. Go to **Console** -> **Video Management**, click the video in the video list, and the following figure appears
![](https://mc.qcloudimg.com/static/img/3a60f37c5c6d429bffb7e96023c948e9/image.png)

After the above two steps are completed, the video is available in multiple definitions and can be played in the Tencent Cloud VOD player using fileID and appID.
Definition selection effect is as shown below:
![](https://mc.qcloudimg.com/static/img/d35731fae08327c66602ee3b7be77c2c/image.png)

>**Note:**
> * This feature does not work when the browser hijacks video playback, which often happens in mobile browsers. In this case, use the browser's player instead.

Example:
[Multiple Definitions](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-base.html)
### Specifying Playback Definitions
It can be classified into two types: specifying a playback definition, and enabling a player to play a video at a specified definition.

#### Specifying a Playback Definition
Specify a playback definition using the "definition" parameter of the player

| Value | Description |
|-------|----------|
| 10 | MP4 Mobile definition |
| 20 | MP4 SD |
| 30 | MP4 HD |
| 40 | MP4 Ultra HD |
| 210 | HLS Mobile definition |
| 220 | HLS SD |
| 230 | HLS HD |
| 240 | HLS Ultra HD |

The following example illustrates how to specify the video playback definition to MP4 mobile definition:
[Specify Playback Definition](http://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-definition.html)

#### Enabling a Player to Play a Video at a Specified Definition

* Go to **Console** -> **Web Player Management**, select a player configuration, and then set to the default image quality.
![](https://mc.qcloudimg.com/static/img/3bcad59bcbb2ae35c2ce02bba1f8cefd/image.png)

* Go to **Console** -> **Video Management**, associate the video with a player configuration, and then the associated player configuration will be used when a video is played by Tencent Cloud Player.
![](https://mc.qcloudimg.com/static/img/82dc40ee75db110ab2d77749ec059d80/image.png)

>**Notes:**
> * If the video at the default definition does not exist, the first file in the video definition list will be played. For example, if the player is configured to play a Ultra HD video by default, but the video is only in SD and HD, the SD one will be played.
> * After the player configuration is completed in the console, it takes about 10 minutes for this configuration to take effect on all CDN nodes.
> * This feature does not work when the browser hijacks video playback.

### Auto-Resume
Auto-resume can be enabled only when a video is played via fileID. A unique fileID is required for the player to record the video duration. If the page is closed while the playback is not completed, the video can be played from the last viewing time point after the payback page is opened again in the same browser.
The auto-resume feature can be enabled using the following parameters:

```
var player = TCPlayer('player-container-id', {
    fileID: '', // Enter the fileID of the video to be played (Required)
    appID: '', // Enter the appID of the VOD account (Required)
    plugins:{
        ContinuePlay: { // Enable the remembering last played position feature
          // auto: true, // Optional. Whether to resume from the last played position automatically
          // text:'Last played position ', // Optional. Prompt text
          // btnText: 'Resume playback' // Optional. Button text
        },
      }
  });
```
After auto-resume is enabled, you can see the effect as follows:
![](https://mc.qcloudimg.com/static/img/e155be329a6fec959e1ad6b361add390/image.png)

Example:
[Auto-Resume](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-continue-play.html)

>**Notes:**
> - This feature is available only for videos that are transcoded by Tencent Cloud and played via fileID and appID.
> - This feature uses localStorage to store the playback time points, so browsers must support localStorage.
> - This feature does not work when the browser hijacks video playback.
> - This feature cannot be used across multiple terminals/browsers. For example, a video not completely played on a PC-side browser cannot be resumed on a mobile browser or on another browser on the same PC. If more APIs are needed, please develop them by yourself.

### Setting Player Logo
You can configure the logo for Tencent Cloud VOD Player. Specifically, go to **Console** -> **Web Player Management**, select a player configuration, and then click the Appearance column to set the logo.
After the logo is set, it will appear at the specified position when you use this player to play videos.

Example:
[Show Logo](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-logo.html)

>**Notes:**
> - After the player configuration is completed in the console, it takes about 10 minutes for this configuration to take effect on all CDN nodes.
> - The logo you set will not display if the browser hijacks video playback.

### Video Ads
Tencent Cloud VOD player allows you to add pre-roll, mid-roll, and post-roll ads as well as hyperlinks. Specifically, go to **Console** -> **Web Player Management**, select a player configuration, and then click the Video ads column to configure relevant information.
By default, the video ad is centered horizontally and vertically on the screen. If the size of the image is larger than the screen, the image will be scaled according to the player's width and is centered horizontally. The parts beyond the screen cannot display.
You can customize the style of video ads via CSS.
```
.tcp-image-patch-start{} /* Pre-roll ad style Class */
.tcp-image-patch-pause{} /* Mid-roll ad style Class */
.tcp-image-patch-ended{} /* Post-roll ad style Class */
```

Example:
[Video ad](https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-image-patch.html)

>**Notes:**
> * It is recommended to use an image that is less than 50KB and does not go beyond the display area of the player to prevent the video initialization speed from being affected.
> * After the player configuration is completed in the console, it takes about 10 minutes for this configuration to take effect on all CDN nodes.
> * The video ad you set will not display if the browser hijacks video playback.

### Referer Hotlink Protection
For more information on how to enable Referer hotlink protection, please see [Referer Hotlink protection](https://cloud.tencent.com/document/product/266/14046).

The following parameters must be added for player initialization:
```
var player = TCPlayer('player-container-id', {
     fileID: '', // Enter the fileID of the video to be played (Required)
     appID: '', // Enter the appID of the VOD account (Required)
     flash:{
         swf: '//[Tencent Cloud Isolated Domain]/vod-player/[appID]/[fileID]/tcplayer/player.swf' // swf file URL (Required)
     }
   });
```
The swf url must be added. The browser using Flash for playback will go to this URL to obtain the Flash player. When the Flash player initiates a video request, the Referer of the request will bring the url or the url of the page.

>**Notes:**
> * The Referer of the video request initiated by the player in Flash mode will bring the swf url in IE and Firefox, which is different from the url of the page in Chrome.
> * You can also download the player.swf file to your CDN server, add the swf parameter, and direct it to your CDN server path.
> * The isolated domain name provided by Tencent Cloud is a unique domain name for each user. One appID corresponds to one domain name. Its format is usually [appID].vod2.myqcloud.com.
> * The domain name of the player swf url must be added into the whitelist.

### Key Hotlink Protection
For more information on how to enable Key hotlink protection, please see [Key Hotlink Protection](https://cloud.tencent.com/document/product/266/14047).

The following parameters must be added for player initialization:
```
var player = TCPlayer('player-container-id', {
     fileID: '', // Enter the fileID of the video to be played (Required)
     appID: '', // Enter the appID of the VOD account (Required)
     t: '',
     us: '',
     sign:''
   });
```
For more information on parameters t, us and sign, please see [Key Hotlink Protection](https://cloud.tencent.com/document/product/266/14047).

>**Notes:**
> * t, us and sign must be generated in accordance with [Key Hotlink Protection](https://cloud.tencent.com/document/product/266/14047). The player will obtain the video Hotlink protection URL for playback based on the 3 parameters passed in the player initialization code.
> * If the Referer hotlink protection is also enabled, just add the parameters to the sample code of the Referer hotlink protection.

### Trial Mode
You need to enable the Key hotlink protection before using the trial mode. For more information on how to enable Key hotlink protection, please see [Key Hotlink protection](https://cloud.tencent.com/document/product/266/14047).

The following parameters must be added for player initialization:
```
var player = TCPlayer('player-container-id', {
     fileID: '', // Enter the fileID of the video to be played (Required)
     appID: '', // Enter the appID of the VOD account (Required)
     t: '',
     us: '',
     sign:'',
     exper:''
   });
```
For more information on parameters t, us, sign and exper, please see [Key Hotlink Protection](https://cloud.tencent.com/document/product/266/14047).

>**Notes:**
> * t, us, sign and exper must be generated in accordance with [Key Hotlink protection](https://cloud.tencent.com/document/product/266/14047). The player will obtain the video Hotlink protection URL with specified trial duration for playback based on the 4 parameters passed in the player initialization code.
> * The trial duration of the video played by the player is specified by the exper parameter. Unlike the previous trial mode that controls the duration on the player side, the player does not obtain the complete video.

### HLS Encrypted Playback
For more information on how to enable the HLS encrypted playback, please see [Video Encryption](https://cloud.tencent.com/document/product/266/9638).

>**Notes:**
> * If the playback page or Flash swf url does not match the domain name of the decryption key server, the Key server needs to deploy corssdomain.xml and CORS (Cross-origin resource sharing) to allow Flash and JavaScript to obtain the decryption key across domains.
> * The domain name of the swf url is configured in crossdomain.xml, and the xml file must be placed in the root directory of the Key server.
> * A video can only be encrypted once, strictly in accordance with the video encryption documentation.
> * The length of the decryption key must be 16 bytes, and it must have no whitespace characters at the start and end.

