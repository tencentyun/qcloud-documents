## Feature Overview

Tencent Cloud LVB player Web SDK solution allows users to directly use the tried-and-tested video playing capability. Through flexible APIs, the SDK can be easily integrated with user's Web Apps to achieve the playing with desktop Apps. At the same time, the Web SDK provides the capability of uploading videos at Web end.<br>
The files that can be played by the SDK are limited by the global hotlink protection feature. For more information, please see FAQs on the official website.<br>
This document is intended for developers who are considering using Tencent Cloud LVB player Web SDK for development and have grasped the basics of JavaScript language.



## Supported Formats


### Playback Format
The following table lists the LVB video formats supported by Web SDK:

| Playback Format    | PC Browser   |  Mobile Browser |
|-------------|------|--------|
| HLS (m3u8) | Yes | Yes   |
| RTMP        | Yes | No |
| FLV         | Yes | No |

> **Android system compatibility**
> Unlike iPhones that only use Safari browser, mobiles running on Android OS use a variety of versions of system standard browsers. For this reason, compatibility of Android mobile browsers has become a problem that plagues the industry. Therefore, the above table **does not apply to all Android mobiles**.


## Preparations

### Step 1: Activate the service
Sign up for a Tencent Cloud account and activate the **LVB** service.
### Step 2: Create a channel
Go to the LVB console and create an LVB channel.<br>[LVB Management](https://console.cloud.tencent.com/live)
### Step 3: Obtain an ID
You can find the LVB channel on the console and manage it. You can find the app_id on the console interface, and find the channel ID in **Basic Settings**.

![](//mc.qcloudimg.com/static/img/c891d20153fe9e46e1647bd7494ab021/image.png)

### Step 4: Prepare pages
Introduce the initialization script to the page in which you want to play videos (including PC or H5)


```
<script src="//qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>;
```



>Note: **<font color="red">The playback page should be accessed with IP address or domain name. Playback is not allowed if you directly open the static page.</font>**

>Note: The channel ID and APPID can also be obtained through the server API. [Link to the reference document](https://cloud.tencent.com/doc/api/258/4714)


## Basic Usage of APIs

### Step 1: Add a player container

 Place a player container in the page where you want to display the player.<span class="anchor" id="step1"><span id="basic_use"></span>

 For example, add the following codes in index.html:
```
<div id="id_video_container" style="width:100%; height:auto;"></div>
```
The container's ID, width, and height can be customized.

### Step 2: Create a Player object

Create a player object in the JavaScript that is introduced at the bottom of the page. In this case, the player constructor is used.
```
var player = new qcVideo.Player("id_video_container", {
"channel_id": "16093104850682282611",
"app_id": "1251783441",
"width" : 480,
"height" : 320
});
```
Call the constructor to generate a player object and find the LVB stream to play based on the channel\_id and app\_id. If channel\_id and app\_id do not exist, the video can be played with the LVB address. An example is provided in the [Case 3 in API Use Cases](#case3). You can control the player with the Player object. For more information, please see the Overview of API Methods below the parameter options of player object.

### Complete Instance Codes
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

>Note: Add a player container as described in [Step 1](#step1) of [Part 4: Basic Usage of API](#basic_use) before using API.

### Case 1: Play LVB video on a PC or mobile device (H5)

**LVB SDK works in the same way both on PC and H5 device. The SDK detects the platform and selects the best playback scheme**. For example, on PC platform, SDK prefers a Flash player to adapt to different video formats (A Flash player version above 10 is required. Otherwise you are prompted to upgrade the Flash player). On a mobile device (H5), SDK uses a video label to play videos (If the browser does not support H5, you are prompted to use QQ browser). The SDK supports playing videos using both channel ID and video file address.
>Note: The two playback methods cannot be used at the same time.

### Case 2: Play videos using channel ID
```
var option = {
"channel_id": "16093425727656143421",
"app_id": "1251132611",
"width" : 480,
"height" : 320

//...You can use other custom attributes
};

var player = new qcVideo.Player("id_video_container", option);
```
**Note: LVB key mode is not supported when playing videos using channel ID.**
### Case 3: Play videos using LVB video address 
If neither app_id nor channel_id exists, the player can alternatively use LVB video address to play the video.<span class="anchor" id="case3">
```
var option = {
"live_url" : "http://2157.liveplay.myqcloud.com/2157_358535a.m3u8",
"live_url2" : "http://2000.liveplay.myqcloud.com/live/2000_2a1.flv",
"width" : 480,
"height" : 320

//...You can use other custom attributes
};

var player = new qcVideo.Player("id_video_container", option);
```

> Note: A maximum of two playback addresses (live\_url and live\_url2) are required. If both of them are passed, an address for which the platform can provide the best support is selected for playback. For example, on PC, RTMP or FLV format is preferred, while on a mobile H5, HLS format is preferred.

### Case 4: How to use "On-screen Comment"
After the initialization of player, you can add on-screen comments for videos by calling the addBarrage(barrage) method of player object. For more information on parameters, please see Overview of API Methods.

Example: Add two on-screen comments for the video that is being played

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"Center", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```
>Note: <font color="red">On-screen comment is only implemented at the frontend. Backend support should be self-developed. This feature only applies to Flash players on PC, but not supported in H5.</font>


##  Overview of API Methods

### 1. Constructor

```
qcVideo.Player(id, option, listener);
```

 **id**: String ;  <font color="red">Required</font>. This parameter indicates the ID of the container where the player is located in the page and can be customized.

  **option**: Object ; <font color="red">Required</font>. This parameter indicates the options that can be set for player's parameters. The options are as follows:

| Parameter             | Type   | Default Value | Description   |
|------------------|--------|--------|---------------------------------------------------------------------------------------------------|
| channel\_id      | String | None     | The parameter is <font color="red">required</font> if the LVB video is played using video ID.                                                                    |
| app\_id          | String | None     | The parameter is <font color="red">required</font> if the LVB video is played using video ID. For the videos under the same account, this parameter remains the same.                                            |
| width            | Number | None     | <font color="red">Required parameter</font>, used to configure player width (in pixel). Example: 640                                                       |
| height           | Number | None     | <font color="red">Required parameter</font>, used to configure player height (in pixel). Example: 480                                                       |
| cache\_time      | Number | 0.3    | The maximum cache time before the LVB video playback starts. This parameter can help avoid stutter in RTMP video caused by insufficient downstream bandwidth (Optional).<br> <font color="red">Note: This parameter only applies to Flash players on PC.</font>   |
| h5\_start\_patch | Object | None     | Start to play pre-video ads on H5 (Optional)<br>{ <br>url : image address, <br>stretch: false //Indicate whether the image is stretched to occupy the full screen of player. Default value is false<br>}                                                                                                  |
| wording          | Object | None     | LVB messages can be customized (Optional. For more information, please see [Error Codes](#errorcode))<br>{	<br>	'1' 	: 'Database error',<br> '2'		: 'Cannot connect to LVB source. The LVB source has not pushed video content (hls)',<br> '3'		: 'LVB has finished (hls)',<br>'113'	: 'Connection timeout. Try again later',<br>'114'	: 'Connection timeout. Try again later',<br>'1000'	: 'Incorrect channelID or APPID',<br>'1001'	: 'Invalid parameter. Failed to obtain the bizid',<br>'1009'	: 'LVB source has expired',<br>'10000'	: 'Connection timeout. Check network settings',<br> '10008'	: 'Wrong password. Enter again', //Invalid password<br>'10020'	: 'Insufficient balance in LVB account. Top up it in time',  <br>'11044'	: 'Invalid request',<br> '11045'	: 'channelID is missing in the request parameter',<br> '11046'	: 'Wrong password. Enter again',<br> '20110'	: 'Wrong password. Enter again',<br>'20113'	: 'LVB has finished. Try again later' , //'downstream type does not exist' Pulling stream does not exist<br>'20201'	: 'LVB has finished. Try again later', //get upstream info error'  Error while querying pushing stream<br> '20301'	: 'LVB channel does not exist. Verify channel ID',<br>'TipReconnect'	: 'Reconnecting'<br>'TipRequireSafari'	: 'Current browser does not support video playback. Use safari to watch the video'<br>'TipRequireFlash'	: 'Current browser does not support video playback. Play the video by downloading the latest QQ browser or installing FLASH player'<br>'TipVideoinfoResolveError'	: 'An error occurred while resolving video information. Check whether the parameter is correct, //No json data is returned from API. Data cannot be resolved<br>'TipVideoinfoError'	: 'Video information error. Check whether the parameter is correct',<br>'TipConnectError'	: 'Failed to connect to the service. Check the network settings',<br>'TipConnectDeny'	: 'Connection to the service is denied', //flash request triggered a security exception<br>'TipLiveEnd'		: 'LVB has finished. Try again later',  // NetStream.Play.Stop event, <br>'TipStreamNotFound'	: ''LVB has finished. Try again later' //Failed to connect to LVB source; the LVB source has not pushed video content<br>}                                                                                                 |
| live\_url        | String | None     | LVB address. HLS/RTMP/FLV format are supported.<br>It is <font color="red">required</font> when video is played using video address                                                                       |
| live\_url2       | String | None    | LVB address. HLS/RTMP/FLV format are supported (Optional)                                                                      |
| volume           | Number | 0.5    | Set the initial volume value ranging from 0 to 1. Default value is 0.5. (Optional)<br><font color="red">Note: This parameter only applies to Flash players.</font>                                                                    |
| https             | Number | 0   | Enable or disable HTTPS for playback pages. 0: Disable; 1: Enable.                                                                    |
| hide_volume_tips  | Number | 0   | Whether the volume tip is hidden. 0: Displayed; 1: Hidden<br><font color="red">Note: This parameter only applies to Flash players.</font>                                                                    |
| x5_type           | String | None   | Enable the H5 player at the same layer through the video attribute "x5-video-player-type". Value: h5. (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For more information, please see [TBS Document](http://x5.tencent.com/guide?id=4000) )                            |
| x5_fullscreen     | String | None   | Enter the full screen mode during video play. Supported value: true: Enable (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For details, refer to [TBS Document](http://x5.tencent.com/guide?id=4000) )                                                       |
| WMode             | String  | window | In window mode, you cannot put other page elements over the Flash player. You can change this into opaque or parameter values for other flash wmode if required. Other elements can be placed over the flash player.<br> <font color="red">Note: This parameter only applies to Flash players on PC.  </font>                                                                  |

**listener**: Object; Optional; List of callback functions in case of playing status change.

| Function Name                                                 | Type     | Description   |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| playStatus<span id="playstatus" class="anchor"></span> | function | Triggered in case of playing status change; callback function's parameter "status": String<br>Returned values:<br>ready: "Player is ready"; playing: "Playing   "; playEnd: "Play has finished"; error: "Play has finished with an exception or error" //Since the playback event trigger conditions vary with mobile devices, it is recommended to listen the error when listening the playEnd event to prevent the callback from being executed incorrectly.  <br>type: String. The type of error is returned when an error occurs. <br>Example: function(status, type){ ... }   |

### 2. Settings and actions

The player objects returned by the constructors can be set using the following methods:

| Method                 | Description                          |
|----------------------|-------------------------------|
| resize(width,height) | Parameter: width :int;height :int <br>Feature: Set width and height for current player<br>Returned value: None                       |
| play()                                                  | Feature: Start playback.<br>Returned value: Int (common error code)<br><font color="red">Note: This feature only applies to Flash players on PC.</font>                                                            |
| stop()                                                  | Feature: Stop playback.<br>Returned value: Int (common error code)<br><font color="red">Note: This feature only applies to Flash players on PC.</font>                                                                    |
| pause()                                                       | Feature: Pause the playback of current video.<br>Returned value: Int (common error code)<br><font color="red">Note: This feature only applies to Flash players on PC.</font>                                                                                   |
| resume()                                                      | Feature: Resume playback.<br>Returned value: Int (common error code)<br><font color="red">Note: This feature only applies to Flash players on PC.</font>        |
| addBarrage(barrage) | Parameter: barrage://Array on-screen comment information   <br> \[{   <br>"type":"content", //message type, content: plain text <font color="red">(required)  </font>   <br>"content":"hello world", //text message <font color="red">(required)  </font>  <br>"time":"1.101",//The time length (in sec) between the moment when the current method is called for adding a caption and the moment when the caption is displayed. <font color="red">(required)  </font>   <br>"style": "C64B03;35",// Separated by semicolons; the first is color value, and the second is font size (optional) <br>"postion":"center" //Location <br>center: centered; bottom: at the bottom; up: at the top (optional) }, ... \]  <br>Feature: Add on-screen comments     <br>Returned value: Int [Error Codes](#errorcode) <br> Note: <font color="red">On-screen comment is only implemented at frontend, and backend functions should be self-developed. This feature only applies to Flash players on PC.</font>                                                                                   |
| closeBarrage()                                                | Feature: Close On-screen Comment. When On-screen Comment is closed, call addBarrage again to enable it. <br>Returned value: Int [Error Codes](#errorcode)  <br> Note: <font color="red">On-screen comment is only implemented at frontend, and backend features should be self-developed. This feature only applies to Flash players on PC.</font>                                                                                   |

The common error codes of the above methods are as follows:
  
| Error Code<span id="errorcode"></span> | Description |
|---------|---------|
| 200 | Operation successful | 
| 0  | Player not fully initialized | 
| -2 | Unknown operation command | 


## Troubleshooting

### Error Codes

List of error codes during the use of SDK<span id="errorcode"></span>

- Error messages returned from frontend

| Message  | Description                                       |
|-------|--------------------------------------------|
| An error occurred while resolving video information. Check whether the parameter is correct. | No JSON data is returned from API. Data cannot be resolved. |
| Video information error. Check whether the parameter is correct. | An error occurred while resolving video information |
| Failed to connect the service. Check the network settings. | Failed to obtain the video channel information. |
| Connection to service is denied.   | Flash request triggered a security exception. |
| Video data is missing. | Video source data is missing. |
| LVB has finished. Try again later. | NetStream.Play.Stop event |
| LVB has finished. Try again later. | Failed to connect to the LVB source. The LVB source has not pushed video content |


- Error messages returned from backend

| Code  | Message | Description                                       |
|-------|-----------|---------------------------------------|
| 1   	| Database error | Database connection timeout or an error occurred during query. |
| 2     | Failed to connect to LVB source. LVB source has not pushed video content (hls). | M3U8 file cannot be obtained due to LVB source connection failure. |
| 3     | LVB has finished (hls). | Manifest is not a valid M3U8 file, or LVB source has finished. |
| 113	| Connection timeout. Try again later. | The parameter is incorrect. |
| 1000 | Incorrect channelID or APPID | The app_id entered is incorrect (length is incorrect). |
| 1001 | Invalid parameter. Failed to obtain the bizid. | The app_id entered is incorrect (length is correct but content is not). |                  
| 1009  | LVB source has expired. | The broadcast address is invalid. LVB source has expired.                 |
| 10000 | Request timeout | Pulling player configuration information and video information timed out. Check network and try again. Timeout is 10 seconds       |
| 10001 | Failed to resolve the data | Failed to solve the data obtained by pulling player configuration information and video information. It may be caused by a network problem or server exception        |
| 10002 | Connection timeout. Try again later | Failed to pull player configuration information and video information. It may be caused by a network problem or server exception        |
| 10008 | Wrong password. Enter again. | Invalid password                             |
| 10020 | Insufficient balance in LVB account. Top up it in time| The balance is insufficient. |
| 11044 | Invalid request | The APPID is missing.                                 |
| 11045 | Channel ID is missing in the request parameter. | Channel ID is missing.                            |
| 11046 | Wrong password. Enter again. | Password is missing                           |
| 20110 | Wrong password. Enter again. | Invalid password                            |
| 20113 | LVB has finished. Try again later. | Pulling stream does not exist (downstream type does not exist). |
| 20201  | LVB has finished. Try again later. | An error occurred while querying pushing stream (get upstream info error). |
| 20301  | LVB channel does not exist. Check the channel ID. | Channel_id is incorrect (app_id is correct). |



>Note: In case of any error code that is not listed in this table, contact customer service. Our engineers can help you solve the problem.

### FAQs

- **Why is the screen stretched when the video is played in H5?**

    Answer: H5 is unable to stretch the screen. Check whether the width and height of player is set correctly.

- **Why did I receive the message that "The LVB has finished. Try again later"?**

    Answer: If you get no response from the LVB address when attempting to connect to this address and fail to connect to it even after five attempts, this message appears. In this case, you need to verify whether the video stream is being pushed and whether the network connectivity is normal.

-  **The video cannot be hidden on the QQ browser.**

    Answer: QQ browser takes over the video playback feature from H5, and the X5 kernel uses self-developed player to play videos. QQ browsers use a unified playback interface to ensure a good user experience. For more information, please see [QQ Browser Documentation](http://x5.tencent.com/guide?id=2009).

-  **Video is automatically played in full screen mode on iOS.**

	Answer: By default, video is played in full screen mode on iOS system due to the webkit setting. To achieve inline playback within an App, you can set the webkit-playsinline attribute. Currently, any Safari browser on iOS below 10 is unable to disable the automatic use of full screen mode.

-  **Why does the Flash player have two play buttons in Chrome on PC?**

	Answer: As of Chrome 42, Flash is not played automatically any longer. Only main Flash content is automatically played, and other content is not, unless user opens it manually.

-  **Why can the LVB video be played in browsers on PC but cannot on mobile devices?**

    Answer: Currently, only HLS videos are supported in the browsers on mobile devices. Check whether the LVB pulling address contains HLS pulling URL.

