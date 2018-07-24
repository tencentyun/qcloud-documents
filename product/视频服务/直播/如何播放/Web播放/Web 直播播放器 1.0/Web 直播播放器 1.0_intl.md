## Feature Description

Tencent Cloud LVB player Web SDK solution allows users to directly use the proven video playback capability. Through flexible APIs, the SDK can be easily integrated with user's Web Apps to achieve the playing with desktop Apps. At the same time, the Web SDK provides the capability of uploading videos at Web end.<br>
The file formats supported by the SDK are limited by the global hotlink protection feature. For more information, please see FAQs on the official website. This document is intended for developers who want to use Tencent Cloud LVB player Web SDK for development and have basics knowledge in JavaScript.

## Supported Formats
Playback Format: LVB video formats supported by the Web SDK.

| Playback Format | PC Browser | Mobile Browser |
|-------------|------|--------|
| HLS (m3u8) | Yes | Yes |
| RTMP        | Yes | No |
| FLV         | Yes | No |

**Android system compatibility**: Unlike iPhones that only use a Safari browser, a wide range of native browsers may come with Android phones. For this reason, compatibility of Android browsers has become a problem that plagues the industry. Therefore, the above table does not apply to all Android phones.


## Preparations

### Step 1: Activate the service
Sign up for a Tencent Cloud account at [Tencent Cloud official website](https://cloud.tencent.com/), and activate the **LVB** service.
### Step 2: Create a channel
Go to the [LVB console](https://console.cloud.tencent.com/live) and create an LVB channel.
### Step 3: Obtain an ID
You can find and manage the LVB channel in the console. You can find its app_id on the console interface. Click the channel to find its ID in **Basic Settings**.
![](https://main.qcloudimg.com/raw/046524dbb086e5cc9ffd910008641271.png)
![](https://main.qcloudimg.com/raw/28071257620b732c80f24b4739e14d6f.png)

### Step 4: Prepare pages
Introduce the initialization script to the page in which you want to play videos (including PC or H5).

```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>;
```

>**Note:**
>**The playback page should be accessed with IP address or domain name. Playback is not allowed if you directly open the static page;**
>Note: The channel ID and APPID can also be obtained through the server API. [Link to the reference document](https://cloud.tencent.com/document/api/267/5664).

## Basic Usage of APIs

### Step 1: Add a player container

 Place a player container in the page where you want to display the player. <span class="anchor" id="step1"><span id="basic_use"></span>For example, add the following code into index.html: 

```
<div id="id_video_container" style="width:100%; height:auto;"></div>
```

The container's ID, width, and height can be customized.

### Step 2: Create a Player object

Create a player object in the JavaScript that is introduced at the bottom of the page. In this case, the player constructor is used:
```
var player = new qcVideo.Player("id_video_container", {
"channel_id": "16093104850682282611",
"app_id": "1251783441",
"width" : 480,
"height" : 320
});
```
Call the constructor to generate a player object and find the LVB stream to play based on the channel_id and app_id. If channel_id and app_id do not exist, the video can be played with the LVB address. An example is provided in the [Case 3 in API Use Cases](#case3). You can control the player with the Player object. For more information, please see the Overview of API Methods below the parameter options of player object.

### Complete sample code
```
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0"/>
    <title>LVB</title>
</head>
<body>
<div id="id_video_container" style="width:100%; height:auto;"></div>
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script type="text/javascript">
    (function () {
        var player = new qcVideo.Player("id_video_container", {
            "channel_id": "16093104850682282611",
            "app_id": "1251783441",
            "width" : 480,
            "height" : 320
        });
    })()
</script>
</body>
</html>
```

## API Use Cases

Complete [Add a player container](#basic_use) as described in Basic Usage of APIs before using API.

### Case 1: Play LVB videos on PC or mobile device (H5)

LVB SDK works in the same way both on PC and H5 devices. The SDK detects the platform and selects the best playback scheme. For example, on PC platform, SDK prefers a Flash player to adapt to different video formats (A Flash player version above 10 is required. Otherwise you are prompted to upgrade the Flash player). On a mobile device (H5), SDK uses a video label to play videos (If the browser does not support H5, you are prompted to use QQ browser). The SDK supports playing videos using both channel ID and video file address.
> **Note:**
>The two playback methods cannot be used at the same time.

### Case 2: Play videos using channel ID
```
var option = {
"channel_id": "16093425727656143421",
"app_id": "1251132611",
"width" : 480,
"height" : 320

//...You may use other custom attributes
};

var player = new qcVideo.Player("id_video_container", option);
```
>**Note:**
>LVB key mode is not supported when playing videos using channel ID.

### Case 3: Play videos using LVB video address 
If neither app_id nor channel_id<span class="anchor" id="case3"><span id="case3"></span> exists, the player can alternatively use LVB video address to play the video.
```
var option = {
"live_url" : "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"live_url2" : "http://2000.liveplay.myqcloud.com/live/2000_2a1.flv",
"width" : 480,
"height" : 320

//...You may use other custom attributes
};

var player = new qcVideo.Player("id_video_container", option);
```

> **Note:**
> A maximum of two playback addresses (live\_url and live\_url2) are supported. If both of them are passed, the address for which the platform can provide the best support is selected for playback. For example, on PC, RTMP or FLV format is preferred, while on a mobile H5, hls format is preferred.

### Case 4: How to use "On-screen Comment"
After the initialization of player, you can add on-screen comments for videos by calling the addBarrage(barrage) method of player object. For more information on parameters, please see [Overview of API Methods](#api). For example, add two on-screen comments for the video that is being played:

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"Center", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```
>**Note:**
>**On-screen comment is only implemented at the frontend. Backend support should be self-developed. This feature only applies to Flash players on PC, but not supported in H5.**

## Overview of API Methods

### Constructor

```
qcVideo.Player(id, option, listener);
```

 **ID**<span class="anchor" id="api"><span id="api"></span>: String; **Required**; This parameter indicates the ID of the container where the player is located in the page and can be customized.
  **option**: Object ; **Required**. This parameter indicates the options that can be set for player's parameters. The options are as follows:

| Parameter | Type | Default Value | Description |
|------------------|--------|--------|---------------------------------------------------------------------------------------------------|
| channel_id      | String | None | This is **Required** when playing video by video ID |
| app_id          | String | None | The parameter is **Required** if the LVB video is played using video ID. For the videos under the same account, this parameter remains the same. |
| width            | Number | None | **Required**, used to configure player width (in pixel). Example: 640 |
| height           | Number | None | **Required**, used to configure player height (in pixel). Example: 480 |
| cache_time      | Number | 0.3    | The maximum cache time before the LVB video playback starts. This parameter can help avoid stutter in RTMP video caused by insufficient downstream bandwidth (Optional).<br> **Note: This parameter only applies to Flash players on PC.** |
| h5_start_patch | Object | None | Starts to play pre-video ads on H5 (Optional)<br>{ <br>url : image address, <br>stretch: false //Indicates whether the image is stretched to fit the full screen of player. Default value is false<br>} |
| wording          | Object | None | LVB messages can be customized (Optional; For details, refer to [Error Code](https://cloud.tencent.com/document/product/267/13500))<br>{	<br>	'1' 	: 'Database error',<br> '2'		: 'Cannot connect to LVB source; the LVB source has not pushed video content (hls)',<br> '3'		: 'LVB has finished (hls)',<br>'113'	: 'Connection timeout; please try again later',<br>'114'	: 'Connection timeout; please try again later',<br>'1000'	: 'Incorrect channelID or APPID',<br>'1001'	: 'Invalid parameter; failed to obtain the bizid',<br>'1009'	: 'LVB source has expired',<br>'10000'	: 'Connection timeout; Please check network settings',<br> '10008'	: 'Wrong password; please enter again',  //Invalid password<br>'10020'	: 'Insufficient balance in LVB account; please top up it in time',  <br>'11044'	: 'Invalid request',<br> '11045'	: 'channelID is missing in the request parameter',<br> '11046'	: 'Wrong password, please enter again',<br> '20110'	: 'Wrong password, please enter again',<br>'20113'	: 'LVB has finished; please try again later' ,  //'downstream type does not exist' Pulling stream does not exist<br>'20201'	: 'LVB has finished; please try again later',  //get upstream info error'  Error while querying pushing stream<br> '20301'	: 'LVB channel does not exist; please verify channel ID',<br>'TipReconnect'	: 'Reconnecting'<br>'TipRequireSafari'	: 'Current browser does not support video play; please use safari to watch the video'<br>'TipRequireFlash'	: 'Current browser does not support video play; you can play the video by downloading the latest QQ browser or installing FLASH player'<br>'TipVideoinfoResolveError'	: 'Error while parsing video information; please check whether the parameter is correct,  //No json data is returned from API; cannot parse the data<br>'TipVideoinfoError'	: 'Video information error; please check whether the parameter is correct',<br>'TipConnectError'	: 'Failed to connect to the service; please check the network settings',<br>'TipConnectDeny'	: 'Connection to the service is denied',  //Flash request triggered a security exception<br>'TipLiveEnd'		: 'LVB has finished; please try again later',   // NetStream.Play.Stop event, <br>'TipStreamNotFound'	: ''LVB has finished; please try again later'  //Failed to connect to LVB source; the LVB source has not pushed video content<br>} |
| live_url        | String | None | LVB address. hls/rtmp/flv formats are supported. <br>It is **required** when video is played using video address |
| live_url2       | String | None | LVB address. hls/rtmp/flv formats are supported (Optional) |
| volume           | Number | 0.5    | Set the initial volume value ranging from 0 to 1. Default value is 0.5. (Optional)**Note: This parameter only applies to Flash players.** |
| https             | Number | 0   | Enable or disable HTTPS for playback pages. 0: Disable; 1: Enable. |
| hide_volume_tips  | Number | 0   | Whether the volume tip is hidden. 0: Displayed; 1: Hidden<br>**Note: This parameter only applies to Flash players.**|
| x5_type           | String | None | Enable the H5 player at the same layer through the video attribute "x5-video-player-type". Value: H5. (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For more information, please see [TBS Document](http://x5.tencent.com/guide?id=4000)) |
| x5_fullscreen     | String | None | Enter the full screen mode during video play. Supported value: true: Enable (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For details, refer to [TBS Document](http://x5.tencent.com/guide?id=4000)) |
| WMode             | String  | window | When in window mode, you cannot put other page elements over the Flash player. You can change this into opaque or parameter values for other flash wmode if required. Other elements can be placed over the flash player. <br> **Note: This parameter only applies to Flash players on PC.** |

**listener**: Object; Optional; List of callback functions in case of playing status change.

| Function Name | Type | Description |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| playStatus<span id="playstatus" class="anchor"></span> | function | Triggered when playback status changes. Callback function parameter "status": String <br>returned values: <br>ready: "Player is ready", playing: "Playback in progress", playEnd: "Playback ended", error: "Play has finished with an exception or error"  //Since the playback event trigger conditions vary with mobile devices, it is recommended to listen the error when listening the playEnd event to prevent the callback from being executed incorrectly. <br>type: String  The type of error is returned when an error occurs. <br>Example: function(status, type){ ... } |

### Settings and actions

The player objects returned by the constructors can be set using the following methods:

| Method | Description |
|----------------------|-------------------------------|
| resize(width,height) | Parameter: width: int; height: int <br>Function: Set the width and height for current player. <br>Returned value: none |
| play()                                                  | Function: Start playback.<br>Returned value: int (common error code)<br>**Note: This function only applies to Flash players on PC.** |
| stop()                                                  | Function: Stop playback.<br>Returned value: int (common error code)<br>**Note: This function only applies to Flash players on PC.** |
| pause()                                                       | Function: Pause the playback of current video.<br>Returned value: int (common error code)<br>**Note: This function only applies to Flash players on PC.** |
| resume()                                                      | Function: Resume the playback of current video.<br>Returned value: int (common error code)<br>**Note: This function only applies to Flash players on PC.** |
| addBarrage(barrage) | Parameter: barrage // Array barrage information <br> \[{   <br>"type":"content",  // Message type, content: plain text (Required) <br> "content":"hello world",  // Text message (Required) <br> "time":"1.101" ,//The time length (in sec) between the moment when the current method is called for adding a caption and the moment when the caption is displayed. (Required) <br> "style": "C64B03;35" ,// Separated by semicolons; the first is color value, and the second is font size (optional) <br> "postion":"center"  // Location <br> center: center, bottom: bottom, up: top (optional) }, ... \] <br> Function: Add on-screen comments<br> Returned value: int [Error Codes](https://cloud.tencent.com/document/product/267/13500) <br> Note: **On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC.** |
| closeBarrage()                                                |Function: disable on-screen comment. Call addBarrage again to re-enable the feature. <br> Returned value: int [Error codes](https://cloud.tencent.com/document/product/267/13500) <br> Note: **On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC.** |

The common error codes of the above methods are as follows:
  
| Error Code<span id="errorcode"></span> | Description |
|---------|---------|
| 200 |Operation successful | 
| 0  | Player not fully initialized | 
| -2 | Unknown operation command | 
