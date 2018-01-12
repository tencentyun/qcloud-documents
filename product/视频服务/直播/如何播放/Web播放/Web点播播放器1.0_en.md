## Feature Overview

This document describes how to use the Web Player (Web SDK) of Tencent Cloud VOD service, which allows users to directly use the tried-and-tested video playback capability. Through flexible APIs, the SDK can be easily integrated with self-built Web Apps to achieve the playing with desktop Apps. At the same time, the Web SDK provides the capability of uploading videos at Web end.

The files that can be played by the SDK are limited by the global hotlink protection feature. For more information, please see FAQs on the official website.

This document is intended for developers who are considering using Tencent Cloud VOD player Web SDK for development and have grasped the basics of JavaScript language.


## Features

### Playback Format
Video formats supported by the Web SDK are as follows:

| Playback Format    | PC Browser     | Mobile Browser |
|---------------|----------------------|---------------------|
| HLS (m3u8) | Yes   | Yes   |
| MP4              | Yes   | Yes   |
| FLV               | No | No |

> **Android system compatibility**
> Unlike iPhones that only use Safari browser, mobiles running on Android OS use a variety of versions of system standard browsers. For this reason, compatibility of Android mobile browsers has become a problem that plagues the industry. Therefore, the above table **does not apply to all Android mobiles**.

 
### Upload Format
Videos formats that are supported by the SDK for upload are as follows:

| Standard Format    |   Details                                  |
|-------------  | ------------------------------------------|
| Microsoft    | WMV, WM, ASF, ASX                            |
| REAL  | RM, RMVB, RA, RAM                            |
| MPEG | MPG, MPEG, MPE, VOB, DAT                     |
| Others    |  MOV, 3GP, MP4, MP4V, M4V, MKV, AVI, FLV, F4V |

> **Transcode service of the VOD platform**
> Since MP4 and HLS (m3u8) formats are better supported for both PC and mobile browsers, Tencent Cloud VOD platform always publishes the uploaded videos in these formats.

### Platform Compatibility
It requires excessive effort to create two sets of codes for mobile and PC browsers respectively. However, by using this player, the same code can adapt itself to PC/mobile browser, which means the player automatically selects the optimal playback method according to the platform it runs on. For example, on PC platform, SDK prefers a Flash player to adapt to different video formats. On a mobile device, HTML5 technology is used to play videos.

## Preparations

### Step 1: Activate the service
First, you need to sign up for a Tencent Cloud account and activate the **VOD** service.

### Step 2: Upload files
After the VOD service is activated, go to [VOD Video Management](http://console.cloud.tencent.com/video/videolist) to upload new video files. Since the document is meant to introduce how to use the player, this operation can help you obtain your own online video address. You are unable to enter this page if you haven't activated VOD service.


### Step 3: Obtain ID
After the video is uploaded, you can find the file ID (the most basic information for the player to play videos) in the Video Management page. The player also includes Quality Statistics feature. You need to verify your APPID which can be queried in the Video Management page before using the player.

 In the figure below, the ID on the left is the video file ID, while the other one is your APPID.
![](//mc.qcloudimg.com/static/img/c181f36d49bfa8532057a32c12b12269/image.jpg)

### Step 4: Prepare pages
Introduce the initialization script to the page in which you want to play videos (including PC or H5):
```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>;
```

> **Local file restriction**
>** You cannot play local files using the player due to cross-domain issues. You must access the player through an IP or domain name - this is why we asked you to upload a video file first and obtain its online playback address.**

## Adding Player
You can add a video player into your page by following the two simple steps below.

### Step 1: Add player container
 Place a player container in the page where you want to display the player. For example, add the following code into index.html. The container ID, width and height can be customized.
```
<div id="id_video_container" style="width:100%; height:auto;"></div>;
```

### Step 2: Create player object
 Next, create a player object in the introduced JavaScript using a player constructor.
```
var player = new qcVideo.Player("id_video_container", {
    "file_id": "1465197896261041838",
    "app_id": "125132611",
    "width":640,
    "height":480
});
```
The constructor is used to generate a player object and find the corresponding video to play based on file\_id and app\_id. You can control the player with the player object. For more information, please see Overview of API Methods below the parameter options of player object.

### Complete Instance Codes
```
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0"/>
    <title>VOD</title>
</head>
<body>
<div id="id_video_container" style="width:100%; height:auto;"></div>
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>
<script type="text/javascript">
    (function () {
        var player = new qcVideo.Player("id_video_container", {
            "file_id": "1465197896261041838",
            "app_id": "125132611",
            "width":640,
            "height":480
        });
    })()
</script>
</body>
</html>
```

## Other Cases
### Case 1: How do I play a video if I have the video address but not the file\_id and app\_id?
Video playback address need to be passed, in which case file\_id and app\_id are not required. JS example:
```
    var option = {
    "width": 640,
    "height": 480,
    //...You can use other custom attributes
    "third_video": {
    "urls":{
            20 : "http://208.vod.myqcloud.com/204.mp4"//This is only an example. Replace this with an actual video address
        }
    }
};
var player = new qcVideo.Player("id_video_container", option);
```

The "urls" attribute of the "third\_video" parameter is an Object, where you can pass multiple video addresses with different video definitions. Detailed parameter descriptions can be found in Overview of API Methods. [Link](#third_video).

>Note: "urls" should include at least one video address

### Case 2: How to use "On-screen Comment"?
After the initialization of player, you can add on-screen comments for videos by calling the addBarrage(barrage) method of player object. For more information on parameters, please see [Overview of API Methods](#barrage).

Example: Add two on-screen comments for the video that is being played

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"Center", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```

> Note: On-screen comment is only implemented at the frontend. Backend support should be self-developed. This feature only applies to Flash players on PC, but not supported in H5.

### Case 3: How do I perform some operations at the end of the video, such as video recommendation?

Use the listener parameter and pass a callback function for the playStatus event. For more information on parameters for callback function, please see API Overview. [Link](#playstatus)

Example:

```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720
    //...You can use other custom attributes
};
var listener = {
    playStatus: function (status){
        //TODO
        console.log(status);
    }
};
var player = new qcVideo.Player("id_video_container", option, listener);
```

### Case 4: How to make the player record video playback progress and start playing the video from the same point the next time?

In "option", set the parameter "remember" to 1. The player records the time point when the video was stopped in the previous playback, and continues from this point upon the next playback.

Example:
```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720,
    "remember":1
    //...You can use other custom attributes
};
var player = new qcVideo.Player("id_video_container", option);
```


### Case 5: How to make the player adjust its size automatically along with the web page?

Use the player object method "resize(width, height)" to modify player size dynamically.

```
player.resize(640, 480);
```

### Case 6: How to play videos that have been configured with passwords from Cloud Video Management?

Just like playing normal videos, SDK automatically displays a password input window. Playback starts after the password is entered.

> Note: Password feature is only available when you play videos by using video IDs.

### Case 7: How to generate a link that is shared by using a QR code or a link?

 Example (please replace the appid and fileid in the link with actual IDs):

[http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&\$def=20&wmode=transparent](http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&$def=20&wmode=transparent) ...

[http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent](http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent) ...

### Case 8: How to specify video playback definition?

Use the "definition" parameter to specify the definition with which the video is played (on condition that the definition is available for this video). This is available for two playback methods: play with video ID and play with address. [Link to parameter description](#definition)

Example:
```
var option ={
    "file_id":"14651978969261415426",
    "app_id":"1251606588",
    "definition":30,
    "width":800,
    "height":700
};

var player = new qcVideo.Player("id_video_container", option);
```



## API Method Overview

### 1. Constructor
```
qcVideo.Player(id, option, listener);
```

**id**: String ; Required.<span id="constructor"></span>
This parameter indicates the ID of the container where the player is located in the page and can be customized.

**option**: Object ; Required.
This parameter indicates the options that can be set for player's parameters. The options are as follows:

| Parameter                                                   | Type    | Default | Description                                                                                                                                                                                        |
|--------------------------------------------------------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file\_id                                               | String  | None     | Unique ID of the VOD file. This parameter is required if the video is played using video ID.                                                                                                                                              |
| app\_id                                                | String  | None     | The parameter is required if the LVB video is played using video ID. For the videos under the same account, this parameter remains the same.                                                                                                                                          |
| width                                                  | Number  | None       | Required parameter, used to configure player width (in pixel). Example: 640                                                                                                                                                     |
| height                                                 | Number  | None       | Required parameter, used to configure player height (in pixel). Example: 480                                                                                                                                                     |
| auto\_play                                             | Number  | 0      | Whether auto playback is allowed. 0: Disable; 1: Enable   <br> Note: This parameter only applies to Flash players on PC.                                                                                                                                                         |
| disable\_full\_screen                                  | Number  | 0      | Whether full-screen mode is allowed. 0: Enable; 1: Disable   <br> Note: This parameter only applies to Flash players on PC.                                                                                                                                                         |
| disable\_drag                                          | Number  | 0      | Whether users are allowed to drag the video progress bar. 0: Allow; 1: Disallow   <br> Note: This parameter only applies to Flash players on PC.                                                                                                                                                         |
| stretch\_full                                          | Number  | 0      | Whether the video is scaled up to the same size as the player. 0: Do not scale up. 1: Scale up to full screen          <br> Note: This parameter only applies to Flash players on PC.                                                                                                                                        |
| stop\_time                                             | Number  | None     | Trial mode. For example, if you set it to "60", the video playback stops in 60 seconds, and the "playStatus" event is triggered at the same time                                                                                                                                |
| remember                                               | Number  | 0      | Whether to remember last played position. 0: No. 1: Yes. If enabled, the time point when the video was stopped in the previous playback is recorded and the next playback starts from this position.   <br> Note: This parameter only applies to Flash players on PC.                                                                                              |
| playbackRate                                           | Number  | 1      | Playback speed. For example, "2" means the video is played at a double speed, while "0.5" means half speed.      <br> Note: This parameter only applies to H5 players currently.                                                                                                    |
| hide\_h5\_setting                                      | Boolean | false  | Whether to hide the H5 Settings button. true: Hide. false: Do not hide                                                                                                                                                 |
| hide\_h5\_error                                        | Boolean | false  | Whether to hide error messages prompted by H5. <br> Note: This parameter only applies to H5 players currently.                                                                                                                                                       |
| WMode                                                  | String  | window | In window mode, you cannot put other page elements over the flash player. You can change this into opaque or parameter values for other flash wmode if required.<br> Note: This parameter only applies to Flash players on PC.                                                                    |
| stretch\_patch                                         | Boolean | false  | If configured as "true", the video ad displayed when the video starts, ends or pauses is enlarged to cover the whole player.                                                                                                                                    |
| definition<span id="definition"></span> | Number  | None     | Used to specify the definition with which the video is played. The configured definition must be available for the video. Available values: 10, 20, 30, 40, 210, 220, 230, 240. For more information about the relation between these values and video types, please see the parameter descriptions for [third_video](#third_video).                                                                             |
| videos                                                 | Array   | None     | When hotlink protection is enabled, you can achieve player playback by configuring an accessible video address for "videos". The definition type is obtained by matching the URL with the URL prefix queried through the backend. For more information, please see [User Guide on Hotlink Protection](https://cloud.tencent.com/doc/product/266/2875).<br> For example: \[`http://xxx.myqcloud.com/xxxyy\_f220.m3u8?**sign**=xxx`, <br>...<br>\]                                                                                                                                                                                               |
| third\_video <span id="third_video"></span>                  | Object  | None     | This option is only used when playing videos by using video addresses<br>Parameter example: {<br>'duration': 20 , //Video duration (in sec). Optional parameter. If not passed, the video duration is automatically updated when MetaData is loaded.<br>Note: This parameter is also required in case of MP4 playback.<br>'urls' : { //(At least one address must be included. Enter the corresponding video formats)  <br>   10 : "mp4 mobile video address", <br>   20 : "mp4 standard definition video address",<br>   30 : "mp4 high definition video address", <br>   40 : "mp4 ultra high definition video address", <br>   210 : "hls mobile video address", <br>   220 : "hls standard definition video address" <br>   230 : "hls high definition video address", <br>   240 : "hls ultra high definition video address" <br>  }<br>}<br> Note: If you simulate playback supported on a mobile device in Chrome or other PC browser, video can be played only by using an MP4 address.  |

**listener**: Object; Optional; List of callback functions in case of playing status change.

| Function Name                                                 | Type     | Description   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| fullScreen                                               | function | Triggered when entering/exiting full-screen mode. Callback function parameter: isFullScreen:Boolean <br>Returned value: true: Full-screen ; false: Exit full-screen <br>Example: ```function(isFullScreen){ ... }```  <br> Note: This parameter only applies to Flash players on PC.    |
| playStatus<span id="playstatus" class="anchor"></span> | function | Triggered when playback status changes. Callback function parameter: status: String <br>Returned value: ready: "Player is ready"; seeking: "Search"; suspended: "Pause"; playing: "Playing"; playEnd: "Playback ended"; stop: "Triggered by the end of trial duration"; error: "Triggered in case of H5 playback error"  <br>Example: function(status, msg){ ... }   |
| dragPlay                                                 | function | Triggered when user drags and changes the progress bar ; second: Number  <br>Returned value: Final progress bar position (in sec) <br>Example: ```function(second){ ... }```  <br> Note: This parameter only applies to Flash players on PC.    |


### 2. Obtain Parameter and Status

Here are the methods for obtaining parameters and statuses for player object that is returned by the constructor

|   Method              |         Returned Value                                                   |       Description                       |
|----------------|------------------------------------------------------------|-----------------------------|
| getVolume      | Number. Value range: 0-1                                 | Obtain the current volume                |
| getDuration    | Number (in sec)                                             | Obtain the total duration of the current video          |
| getCurrentTime | Number (in sec)                                             | Obtain the current playback position            |
| isSeeking      | Boolean ; true indicates "loading"                                  | Whether the current playback status is "loading"   |
| isSuspended    | Boolean ; true indicates "paused"                                  | Whether the current playback status is "paused"   |
| isPlaying      | Boolean ; true indicates "playing"                                  | Whether the current playback status is "playing"   |
| isPlayEnd      | Boolean ; true indicates "playback ended"                                | Whether the current playback status is "playback ended" |
| getWidth       | Number (int)                                                | Obtain the current player width          |
| getHeight      | Number(int)                                                | Obtain the current player height          |
| getClarity     | Number(int) (1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition")      | Obtain the current video definition        |
| getAllClaritys | Array&lt;int&gt; ( 1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition") | Obtain all available definitions for the current video    |

### 3. Configuration and Action

The player objects returned by the constructors can be set using the following methods:

| Method                                                          | Description                                                                                                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| resize(width,height)                                          | Parameter: width :int; height :int                                            <br>Feature: Set width and height for current player                                         <br>Returned value: None                                                                                                              |
| play(second)                                                  | Parameter: second: int (in sec)                                                  <br>Feature: Start playback. You can specify the starting time point from which the video is played <br>Returned value: Int [Error Codes](#errorcode)<br>Note: For "second", you can only pass a null value or 0 when playing videos by using video addresses                                                               |
| pause()                                                       | Feature: Pause the play of current video <br>Returned value: Int [Error Codes](#errorcode)                                                                                     |
| resume()                                                      | Feature: Resume the current video playback <br>Returned value: Int [Error Codes](#errorcode)                                                                                     |
| setClarity(clarity)                                           | Parameter: clarity: int Video definition. Value range: (1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition")<br>Feature: Change video definition <br>Returned value: Int [Error Codes](#errorcode)                            <br>Note: Make sure that the definition is available for the current video before configuring it using "clarity", otherwise the player may choose a definition based on the default player rules                       |
| changeVideo(opt)                                              | Parameter: opt Object ; Contains the basic information of the video to be played. This is nearly identical to the second parameter of the constructor. For more information, please see [Constructor Instruction](#constructor);<br>Feature: Change video dynamically  <br>Returned value: Int [Error Codes](#errorcode) |
| addBarrage(barrage) <span id="barrage"></span>| Parameter: barrage://Array on-screen comment information   <br> \[{   <br>"type":"content", //message type, content: plain text (required)     <br>"content":"hello world", //text message (required)    <br>"time":"1.101",//The time length (in sec) between the moment when the current method is called for adding a caption and the moment when the caption is displayed. (required)     <br>"style": "C64B03;35",// Separated by semicolons; the first is color value, and the second is font size (optional) <br>"postion":"center" //Location <br>center: centered; bottom: at the bottom; up: at the top (optional) }, ... \]  <br>Feature: Add on-screen comments     <br>Returned value: Int [Error Codes](#errorcode) <br> Note: On-screen comment is only implemented at frontend, and backend functions should be self-developed. This feature only applies to Flash players on PC.                                                                                   |
| closeBarrage()                                                | Feature: Close On-screen Comment. When On-screen Comment is closed, call addBarrage again to enable it. <br>Returned value: Int [Error Codes](#errorcode)  <br> Note: On-screen comment is only implemented at frontend, and backend features should be self-developed. This feature only applies to Flash players on PC.                                                                                   |
The common error codes of the above methods are as follows:
  
| Error Code<span id="errorcode"></span> | Description |
|---------|---------|
| 200 | Operation successful | 
| 0  | Player not fully initialized | 
| -1 | Failed to change video dynamically. Required parameter is missing | 
| -2 | Unknown operation command | 
| -3 | Playback time is beyond valid playback range | 


## Video File Upload

Users can use VOD Web SDK to upload videos, to help Tencent Cloud Video users upload video files using Web.

Currently, the SDK supports uploading via HTML5 (upload is not available for browsers that do not support HTML5)

For more information about upload operations, please see: [http://video.qcloud.com/sdk/upload.html](http://video.qcloud.com/sdk/upload.html)



## Troubleshooting

### Error Codes

The table contains error codes that may occur when using the SDK. In case of any error code that is not listed in this table, contact customer service. Our engineers can help you solve the problem.

| Code  | Description               |
|-------|---------------------|
| 1003  | Incorrect password         |
| 10000 | Request timeout (Pulling player configuration information and video information timed out. Check network and try again. Timeout is 10 seconds)        |
| 10001 | Failed to resolve the data (Failed to solve the data obtained by pulling player configuration information and video information. It may be caused by a network problem or server exception)        |
| 10002 | Connection timeout. Try again later (Failed to pull player configuration information and video information. It may be caused by a network problem or server exception)        |
| 10008 | Incorrect APPID or File ID |
| 11044 | APPID is missing     |
| 11045 | File ID is missing     |
| 11046 | Password is missing        |


### FAQs

* **Why is the screen stretched when the video is played in H5?**

    Answer: H5 is unable to stretch the screen. Check whether the width and height of player is set correctly.

* **My QQ browser is downloading the video. How to stop it?**

    Answer: JS cannot intervene such actions due to the restrictions of the QQ mobile browser kernel. Similarly, the kernels of some browsers, such as UC, also provide auto video detection/download feature. Contact the developer of your browser to cancel this feature.

* **The video cannot be hidden on the QQ browser.**

    Answer: QQ browser takes over the video playback feature from H5, and the X5 kernel uses self-developed player to play videos. QQ browsers use a unified playback interface to ensure a good user experience. For more information, please see [QQ Browser Documentation](http://x5.tencent.com/guide?id=2009).
		
* **I didn't get the correct status information when calling relevant methods such as isPlaying().**

	Answer: In some mobile browsers and webviews, video playback is taken over by the browser's kernel, which means the SDK cannot obtain the correct playback status.

* **Video cannot be automatically played on mobile device after auto playback is set.**
	
	Answer: Most mobile browsers currently do not automatically load media files due to data traffic and other reasons. Users need to trigger actions when playing videos.
	
* **Video is automatically played in full screen mode on iOS.**

	Answer: By default, video is played in full screen mode on iOS system due to the webkit setting. To achieve inline playback within an App, you can set the webkit-playsinline attribute. Currently, any Safari browser on iOS below 10 is unable to disable the automatic use of full screen mode.

* **Why does the Flash player have two play buttons in Chrome on PC?**

	Answer: As of Chrome 42, Flash is not played automatically any longer. Only main Flash content is automatically played, and other content is not, unless user opens it manually.

