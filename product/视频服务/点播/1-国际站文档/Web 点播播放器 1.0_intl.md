## Feature Description

This document describes how to use the Web Player (Web SDK) of Tencent Cloud VOD service, which allows users to directly use the proven video playback capability. Through flexible APIs, the SDK can be easily integrated with self-built Web Apps to achieve the playing with desktop Apps. At the same time, the Web SDK provides the capability of uploading videos at Web end.

The file formats supported by the SDK are limited by the global hotlink protection feature. For more information, please see FAQs on the official website. This document is intended for developers who want to use Tencent Cloud VOD player Web SDK for development and have basics knowledge in JavaScript.

## Supported Features

### Playback Format
The following table lists the video formats supported by Web SDK:

| Playback Format | PC Browser | Mobile Browser |
|---------------|----------------------|---------------------|
| HLS (m3u8) | Yes | Yes |
| MP4              | Yes | Yes |
| FLV               | No | No |

**Android system compatibility:** Unlike iPhones that only use a Safari browser, a wide range of native browsers may come with Android phones. For this reason, compatibility of Android browsers has become a problem that plagues the industry. Therefore, the above table does not apply to all Android phones.

### Upload format
Video formats supported by the SDK for upload are as follows:

| Standard | Detailed Format |
|-------------  | ------------------------------------------|
| Microsoft | WMV, WM, ASF, ASX |
| REAL | RM, RMVB, RA, RAM |
| MPEG | MPG, MPEG, MPE, VOB, DAT |
| Others    |  MOV, 3GP, MP4, MP4V, M4V, MKV, AVI, FLV, F4V |

**Transcode service of the VOD platform:** Since MP4 and HLS (m3u8) formats are relatively widely supported for both PC and mobile browsers, Tencent Cloud VOD platform always publishes the uploaded videos in these formats.

### Platform compatibility
It requires excessive effort to create two sets of codes for smartphone browser and PC browser. However, by using this player, the same code will adapt itself to PC browser/smartphone browser, which means the player will automatically choose the optimal playback method according to the platform it runs on. For example: On PC, the service will use Flash player as first priority in order to cope with various video formats. On smartphone, the service will use HTML5 technology to play videos instead.

## Preparations

### Step 1: Activate the service
Sign up for a Tencent Cloud account at [Tencent Cloud official website](https://cloud.tencent.com/), and activate the **VOD** service.

### Step 2: Upload files
After the VOD service is activated, go to [VOD Video Management](http://console.cloud.tencent.com/vod/videolist) to upload new video files. Since the document is meant to introduce how to use the player, this operation can help you obtain your own online video address. You are unable to enter this page if you haven't activated VOD service.

### Step 3: Obtain an ID
After the video is uploaded, you can find the file ID (the most basic information for the player to play videos) in the Video Management page. The player also includes Quality Statistics feature. You need to verify your APPID which can be queried in the Video Management page before using the player. In the figure below, the ID on the left is the video file ID, while the other one is your APPID.
![](https://main.qcloudimg.com/raw/c3454da2c5369b27fc4cf038f286215c.png)

### Step 4: Prepare pages
Introduce the initialization script to the page in which you want to play videos (including PC or H5):
```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>;
```

**Local file restriction: You cannot play local files using the player due to cross-domain issues. You must access the player through an IP or domain--this is why we asked you to upload a video file first and acquire its online playback address.**

## Adding Player
You can add a video player into your page by following the two simple steps below.

### Step 1: Add a player container
Place a player container in the page where you want to display the player. For example, add the following code into index.html. The container ID, width and height can be customized.
```
<div id="id_video_container" style="width:100%; height:auto;"></div>;
```

### Step 2: Create a Player object
Next, create a player object in the introduced JavaScript using a player constructor.
```
var player = new qcVideo.Player("id_video_container", {
    "file_id": "1465197896261041838",
    "app_id": "125132611",
    "width":640,
    "height":480
});
```
The constructor is used to generate a player object and find the corresponding video to play based on file_id and app_id. You can control the player with the player object. For more information, please see [Overview of API Methods](#third_video) for the parameter options of player object.

### Complete sample code
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
### case 1: How do I play a video if I have the video address but not the file_id and app_id?
Video playback address need to be passed, in which case file_id and app_id are not required. JS example:
```
    var option = {
    "width": 640,
    "height": 480,
    //...You may use other custom attributes
    "third_video": {
    "urls":{
            20 : "http://208.vod.myqcloud.com/204.mp4"//This is only an example. Please replace this with actual video address
        }
    }
};
var player = new qcVideo.Player("id_video_container", option);
```

The "urls" attribute of the "third_video" parameter is an Object, where you can pass multiple video addresses with different video definitions. Detailed parameter descriptions can be found in [Overview of API Methods](#third_video).

>**Note:**
>"urls" should include at least one video address

### case 2: How to use "On-screen Comment"?
After the initialization of player, you can add on-screen comments for videos by calling the addBarrage(barrage) method of player object. For more information on parameters, please see [Overview of API Methods](#barrage). For example, add two on-screen comments for the video that is being played:

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"Center", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```

> **Note:**
> **On-screen comment is only implemented at the frontend. Backend support should be self-developed. This feature only applies to Flash players on PC, but not supported in H5.**

### Case 3: How do I perform some operations at the end of the video, such as video recommendation?

Use the listener parameter and pass a callback function for the playStatus event. This function will be called when the playback status changes. For description on the specific callback function parameters, please see [API Overview](#playstatus).

For example:

```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720
    //...You may use other custom attributes
};
var listener = {
    playStatus: function (status){
        //TODO
        console.log(status);
    }
};
var player = new qcVideo.Player("id_video_container", option, listener);
```

### Case 4: How to make the player remember video playback progress and start playing the video from the same point the next time?

In "option", set the parameter "remember" to 1. The player records the time point when the video was stopped in the previous playback, and continues from this point upon the next playback. For example:
```
var option ={
    "file_id":"1465197896261041838",
    "app_id":"125132611",
    "width":800,
    "height":720,
    "remember":1
    //...You may use other custom attributes
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

> **Note:**
> Password feature is only available when playing videos by passing video IDs.

### Case 7: How to generate a link that is shared by using a QR code or a link?

 Example (please replace the appid and fileid in the link with actual IDs):

```
http://play.video.qcloud.com/qrplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=640&sh=426&$def=20&wmode=transparent
```

```
http://play.video.qcloud.com/iplayer.html?appid=1251769111&fileid=14651978969211156176147&autoplay=0&sw=1800&sh=1200&def=20&wmode=transparent
```

### Case 8: How to specify video playback definition?

Use the "definition" parameter to specify the definition with which the video is played (on condition that the definition is available for this video). This is available for two playback methods: play with video ID and play with address. See [Parameter Description](#definition) link for more information. For example:
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

## Overview of API Methods

### Constructor
```
qcVideo.Player(id, option, listener);
```

**ID**: String; **Required**; This parameter indicates the ID of the container where the player is located in the page <span id="constructor"></span> and can be customized.
**option**: Object ; **Required**.
This parameter indicates the options that can be set for player's parameters. The options are as follows:

| Parameter | Type | Default Value | Description |
|--------------------------------------------------------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file_id                                               | String  | None | Unique ID of the VOD file. This is **Required** when playing video by video ID |
| app_id                                                | String  | None | The parameter is **Required** if the LVB video is played using video ID. For the videos under the same account, this parameter remains the same. |
| width                                                  | Number  | None | **Required**, used to configure player width (in pixel). Example: 640 |
| height                                                 | Number  | None | **Required**, used to configure player height (in pixel). Example: 480 |
| auto_play                                             | Number  | 0      | Whether auto playback is allowed. 0: Disable; 1: Enable <br> **Note: This parameter only applies to Flash players on PC.** |
| disable_full_screen                                  | Number  | 0      | Whether full-screen mode is allowed. 0: Enable; 1: Disable <br>**Note: This parameter only applies to Flash players on PC.** |
| disable_drag                                          | Number  | 0      | Whether users are allowed to drag the video progress bar. 0: Allow; 1: Disallow <br> **Note: This parameter only applies to Flash players on PC.** |
| stretch_full                                          | Number  | 0      | Whether the video is scaled up to the same size as the player. 0: Do not scale up. 1: Scale up to full screen <br> **Note: This parameter only applies to Flash players on PC.** |
| stop_time                                             | Number  | None | Trial mode. For example, if you set it to "60", the video playback stops in 60 seconds, and the "playStatus" event is triggered at the same time |
| remember                                               | Number  | 0      | Whether to remember last played position. 0: No. 1: Yes. If enabled, the time point when the video was stopped in the previous playback will be recorded and the next playback will start from this position. <br> **Note: This parameter only applies to Flash players on PC.** |
| playbackRate                                           | Number  | 1      | Playback speed. For example,"2" means the video will be played at double speed, while "0.5" means half speed. <br> **Note: This option is only applies to H5 players** |
| hide_h5_setting                                      | Boolean | false  | Whether to hide the H5 Settings button. true: Hide. false: Do not hide |
| hide_h5_error                                        | Boolean | false  | Whether to hide error messages prompted by H5. <br> **Note: This parameter only applies to H5 players.** |
| WMode                                                  | String  | window | When in window mode, you cannot put other page elements over the Flash player. You can change this into opaque or parameter values for other flash wmode if required. <br> **Note: This parameter only applies to Flash players on PC.** |
| stretch_patch                                         | Boolean | false  | If configured as "true", the video ad that is displayed when the video starts, ends or pauses will be enlarged to cover the whole player. |
| definition<span id="definition"></span> | Number  | None | Used to specify the definition with which the video will be played. The configured definition must be available for the video. Available values: 10, 20, 30, 40, 210, 220, 230, 240. For more information about the relation between these values and video types, see the parameter descriptions for [third_video](#third_video). |
| videos                                                 | Array   | None     | When hotlink protection is enabled, you can achieve player playback by configuring an accessible video address for "videos". The definition type is obtained by matching the URL with the URL prefix queried through the backend. For more information, please see [User Guide on Hotlink Protection](https://cloud.tencent.com/doc/product/266/2875).<br> For example: [`http://xxx.myqcloud.com/xxxyy\_f220.m3u8?**sign**=xxx`,<br>...<br>] |
| third_video <span id="third_video"></span>                  | Object  | None | This option is only used when playing videos by using video addresses.<br>Parameter Example: <br>{'duration': 20,  //Video duration (in sec). Optional parameter. If not passed, the video duration will be automatically updated when MetaData is loaded. <br> **Note: This parameter is required in case of MP4 playback.** <br> 'urls': { // (**At least one address must be included. Be careful about the video format**) <br> 10: "address for mp4 mobile videos", <br> 20: "address for mp4 SD videos", <br> 30: "address for mp4 HD videos", <br> 40: "address for mp4 ultra high definition videos", <br> 210: "address for hls mobile videos", <br> 220: "address for hls SD videos", <br> 230: "address for hls HD videos", <br> 240: "address for hls ultra high definition videos" <br> } <br> } <br> **Note: If you simulate a mobile device in Chrome or other PC browsers, please use an address for MP4 videos.** |

**listener**: Object; Optional; List of callback functions in case of playing status change.

| Function Name | Type | Description |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| fullScreen                                               | function | Triggered when entering/exiting full-screen mode. Callback function parameter: isFullScreen: Boolean <br>Returned value: true: enter full screen, false: exit full screen <br>Example: ```function(isFullScreen){ ... }```  <br>**Note: This event only applies to PC Platform Flash Player** |
| playStatus<span id="playstatus" class="anchor"></span> | function | Triggered when playback status changes. Callback function parameter "status": String <br>Returned value: ready: "Player is ready"; seeking: "Search"; suspended: "Pause"; playing: "Playback in progress"; playEnd: "Playback ended"; stop: "Triggered by the end of trial duration"; error: "Triggered in case of H5 playback error" <br> Example: function(status, msg){ ... } |
| dragPlay                                                 | function | Triggered when you drag and change the progress bar; second: Number <br> Returned value: Final progress bar position (in sec) <br> Example: ```function(second){ ... }```  <br> **Note: This event only applies to PC Platform Flash Player** |


### Obtain parameter and status

Here are the methods for obtaining parameters and statuses for player object that is returned by the constructor

| Method | Returned Value | Description |
|----------------|------------------------------------------------------------|-----------------------------|
| getVolume      | Number. Value range: 0-1 | Obtain the current volume |
| getDuration    | Number (in sec) | Obtain the total duration of the current video |
| getCurrentTime | Number (in sec) | Obtain the current playback position |
| isSeeking      | Boolean ; true indicates "loading" | Whether the current playback status is "loading" |
| isSuspended    | Boolean ; true indicates "paused" | Whether the current playback status is "paused" |
| isPlaying      | Boolean ; true indicates "playing" | Whether the current playback status is "playing" |
| isPlayEnd      | Boolean ; true indicates "playback ended" | Whether the current playback status is "playback ended" |
| getWidth       | Number(int)                                                | Get the width of current player |
| getHeight      | Number(int)                                                | Get the height of current player |
| getClarity     | Number(int) (1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition") | Get the current video definition |
| getAllClaritys | Array&lt;int&gt; ( 1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition") | Get all available definitions for the current video |

### Settings and actions

The player objects returned by the constructors can be set using the following methods:

| Method | Description |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| resize(width,height)                                          | Parameter: width: int; height: int <br>Function: Set the width and height for current player. <br>Returned value: none |
| play(second)                                                  | Parameter: second: int (in sec) <br>Function: Start playback. You can specify a time point at which the video starts to play <br>Returns: int [Error Codes](https://cloud.tencent.com/document/product/267/13506)<br> Note: "second" can only be a null value or 0 when you play a video by using a video address |
| pause()                                                       | Function: Pause the playback of current video<br> Returned value: int [Error codes](https://cloud.tencent.com/document/product/267/13506) |
| resume()                                                      | Funtion: Resume playback. <br>Returned value: int [Error codes](https://cloud.tencent.com/document/product/267/13506) |
| setClarity(clarity)                                           | Parameter: clarity, int definition. Value range: (1: "Mobile", 2: "Standard definition", 3: "High definition", 4: "Ultra high definition")<br>Function: Change video definition <br>Returned value: Int [Error Codes](https://cloud.tencent.com/document/product/267/13506) <br>Note: Make sure that the definition is available for the current video before configuring it using "clarity", otherwise the player may choose a definition based on the default player rules |
| changeVideo(opt)                                              |Parameter: opt Object; Contains the basic information of the video to be played. This is nearly identical to the "second" parameter of the constructor. For more information, please see [Constructor Instruction](#constructor)<br>Function: Change video dynamically <br> Returned value: int [Error Codes](https://cloud.tencent.com/document/product/267/13506) |
| addBarrage(barrage) <span id="barrage"></span>| Parameter: barrage, array barrage information <br> \[{   <br>"type":"content",  // Message type, content: plain text (**Required**) <br> "content":"hello world",  // Text message (**required**) <br> "time":"1.101" ,//The time length (in sec) between the moment when the current method is called for adding a caption and the moment when the caption is displayed. (**Required**) <br> "style": "C64B03;35" ,// Separated by semicolons; the first is color value, and the second is font size (optional) <br> "postion":"center"  // Location <br> center: center, bottom: bottom, up: top (optional) }, ... \] <br> Function: Add on-screen comments<br> Returned value: int [Error Codes](https://cloud.tencent.com/document/product/267/13506) <br> Note: **On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC.** |
| closeBarrage()                                                |Function: disable on-screen comment. Call addBarrage again to re-enable the feature. <br> Returned value: int [Error codes](https://cloud.tencent.com/document/product/267/13506) <br> Note: **On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC.** |
The common error codes of the above methods are as follows:
  
| Error Code<span id="errorcode"></span> | Description |
|---------|---------|
| 200 |Operation successful | 
| 0  | Player not fully initialized | 
| -1 | Failed to change video dynamically. Required parameter is missing | 
| -2 | Unknown operation command | 
| -3 | Playback time is beyond valid playback range | 


## Video File Upload

Users can use VOD Web SDK to upload videos. Tencent Cloud Video users can therefore upload video files using Web. The SDK supports uploading via HTML5, but it's not possible for browsers that do not support HTML5.

For more information on how to proceed, see [Cloud VOD Web Upload SDK](http://video.qcloud.com/sdk/upload.html).
