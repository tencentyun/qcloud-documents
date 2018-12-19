## Feature Description

Tencent Cloud LVB player Web SDK solution allows users to directly use the proven video playback capability. Through flexible APIs, the SDK can be easily integrated with user's Web Apps to achieve the playing with desktop Apps. At the same time, the Web SDK provides the capability of uploading videos at Web end.<br>
The file formats supported by the SDK are limited by the global hotlink protection feature. For more information, please see FAQs on the official website.<br>
This document is intended for developers who want to use Tencent Cloud LVB player Web SDK for development and have basics knowledge in JavaScript.



## Supported Formats


### Playback format
The following table lists the LVB video formats supported by Web SDK:

| Playback Format    | PC Browser   |  Mobile Browser |
|-------------|------|--------|
| HLS (m3u8) | Yes | Yes |
| RTMP        | Yes | No |
| FLV         | Yes | No |

> **Android system compatibility**
> Unlike iPhones that only use a Safari browser, a wide range of native browsers may come with Android phones. For this reason, compatibility of Android browsers has become a problem that plagues the industry. Therefore, the above table **does not apply to all Android phones**.


## Preparations

### Step 1: Activate the service
Sign up for a Tencent Cloud account and activate the **LVB** service.
### Step 2: Create a channel
Go to the LVB console and create an LVB channel.<br>[LVB Management](https://console.cloud.tencent.com/live)
### Step 3: Obtain an ID
You can find and manage the LVB channel in the console. You can find its app_id on the console interface. The channel's id can be found in **Basic Settings**.

![](//mc.qcloudimg.com/static/img/c891d20153fe9e46e1647bd7494ab021/image.png)

### Step 4: Prepare pages
Introduce the initialization script to the page on which you want to play videos (including PC or H5)


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
A player object will be created when the constructor is called, and the player will find and play the video located with channel\_id and app\_id. If the channel\_id and app\_id do not exist, the video can be located and played with the LVB address. An example is provided in the [Case 3 in API Use Cases](#case3). You may control the player using the player object "player". Parameter options for the player object are described in details in the Overview of API Methods section below.

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

>Note: Add a player container as described in [step1](#step1) of [Part 4: Basic Usage of API](#basic_use) before using API.

### Case 1: Play LVB video on a PC or mobile device (H5)

**LVB SDK works in the same way both on PC and H5. The SDK detects the platform and selects the best playback scheme**. For example, on PC platform, SDK prefers a Flash player to adapt to different video formats (A Flash player version above 10 is required. Otherwise you are prompted to upgrade the Flash player). On a mobile device (H5), SDK uses a video label to play videos (If the browser does not support H5, you are prompted to use QQ browser). The SDK supports playing videos using both channel ID and video file address.
>Note: The two playback methods cannot be used at the same time.

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
**Note: LVB key mode is not supported when playing videos using channel ID.**
### Case 3: Play videos using LVB video address 
If neither app_id nor channel_id exists, the player can alternatively use LVB video address to play the video.<span class="anchor" id="case3">
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

> Note: A maximum of two playback addresses (live\_url and live\_url2) are supported. If both of them are passed, an address for which the platform can provide the best support is selected for playback. For example: on PC, RTMP or FLV format is preferred, while on a mobile H5, HLS format is preferred.

### Case 4: How to use "On-screen Comment"
After the player is initialized, call the player object method "addBarrage(barrage)" to add live comments to videos. For more information on parameters, see [Overview of API Methods].

Example: Add two on-screen comments for the video that is being played

```
var barrage = [
{"type":"content", "content":"hello world", "time":"1"},
{"type":"content", "content":"Center", "time":"1", "style":"C64B03;30","position":"center"}
];
player.addBarrage(barrage);
```
>Note: <font color="red">Live commenting can only be achieved from the frontend. You will need to develop backend features on your own. Live commenting is only functional when playing videos on PC Flash player. It is not supported for H5.</font>


##  Overview of API Methods

### 1. Constructor

```
qcVideo.Player(id, option, listener);
```

 **id**: String ;  <font color="red">Required</font>. This parameter indicates the ID of the container where the player is located in the page and can be customized.

  **option**: Object ; <font color="red">Required</font>. This parameter indicates the options that can be set for player's parameters. The options are as follows:

| Parameter | Type | Default Value | Description |
|------------------|--------|--------|---------------------------------------------------------------------------------------------------|
| channel\_id      | String | None | The parameter is <font color="red">required</font> if the LVB video is played using video ID. |
| app\_id          | String | None | The parameter is <font color="red">required</font> if the LVB video is played using video ID. For the videos under the same account, this parameter remains the same. |
| width            | Number | None | <font color="red">Required</font>, used to configure player width (in pixel). Example: 640 |
| height           | Number | None | <font color="red">Required</font>, used to configure player height (in pixel). Example: 480 |
| cache\_time      | Number | 0.3    | The maximum cache time before the LVB video playback starts. This parameter can help avoid stutter in RTMP video caused by insufficient downstream bandwidth (Optional). <br> <font color="red">Note: This parameter only applies to Flash players on PC.</font> |
| h5\_start\_patch | Object | None | Start to play pre-video ads on H5 (Optional)<br>{ <br>url : image address, <br>stretch: false //Indicates whether the image is stretched to fit the full screen of player. Default value is false<br>}                                                                                                  |
| wording          | Object | None | LVB messages can be customized (Optional; For details, refer to [Error Code](#errorcode))<br>{	<br>	'1' 	: 'Database error',<br> '2'		: 'Cannot connect to LVB source; the LVB source has not pushed video content (hls)',<br> '3'		: 'LVB has finished (hls)',<br>'113'	: 'Connection timeout; please try again later',<br>'114'	: 'Connection timeout; please try again later',<br>'1000'	: 'Incorrect channelID or APPID',<br>'1001'	: 'Invalid parameter; failed to obtain the bizid',<br>'1009'	: 'LVB source has expired',<br>'10000'	: 'Connection timeout; Please check network settings',<br> '10008'	: 'Wrong password; please enter again',  //Invalid password<br>'10020'	: 'Insufficient balance in LVB account; please top up it in time',  <br>'11044'	: 'Invalid request',<br> '11045'	: 'channelID is missing in the request parameter',<br> '11046'	: 'Wrong password, please enter again',<br> '20110'	: 'Wrong password, please enter again',<br>'20113'	: 'LVB has finished; please try again later' ,  //'downstream type does not exist' Pulling stream does not exist<br>'20201'	: 'LVB has finished; please try again later',  //get upstream info error'  Error while querying pushing stream<br> '20301'	: 'LVB channel does not exist; please verify channel ID',<br>'TipReconnect'	: 'Reconnecting'<br>'TipRequireSafari'	: 'Current browser does not support video play; please use safari to watch the video'<br>'TipRequireFlash'	: 'Current browser does not support video play; you can play the video by downloading the latest QQ browser or installing FLASH player'<br>'TipVideoinfoResolveError'	: 'Error while parsing video information; please check whether the parameter is correct,  //No json data is returned from API; cannot parse the data<br>'TipVideoinfoError'	: 'Video information error; please check whether the parameter is correct',<br>'TipConnectError'	: 'Failed to connect to the service; please check the network settings',<br>'TipConnectDeny'	: 'Connection to the service is denied',  //flash request triggered a security exception<br>'TipLiveEnd'		: 'LVB has finished; please try again later',   // NetStream.Play.Stop event, <br>'TipStreamNotFound'	: ''LVB has finished; please try again later'  //Failed to connect to LVB source; the LVB source has not pushed video content<br>} |
| live\_url        | String | None     | LVB address; support hls/rtmp/flv formats<br>It is <font color="red">required</font> when video is played using video address |
| live\_url2       | String | None | LVB address. hls/rtmp/flv formats are supported (Optional) |
| volume           | Number | 0.5    | Set the initial volume value ranging from 0 to 1. Default value is 0.5. (Optional)<br><font color="red">Note: This parameter only applies to Flash players.</font> |
| https             | Number | 0   | Enable or disable HTTPS for playback pages. 0: Disable; 1: Enable. |
| hide_volume_tips  | Number | 0   | Indicate whether the volume tip is hidden. 0: Displayed; 1: Hidden <br><font color="red">Note: This parameter only applies to Flash players.</font> |
| x5_type           | String | None | Enable the H5 player at the same layer through the video attribute "x5-video-player-type". Value: h5. (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For more information, please see [TBS Document](http://x5.tencent.com/guide?id=4000)) |
| x5_fullscreen     | String | None | Enter the full screen mode during video play. Supported value: true: Enable (This attribute is an experimental one of TBS kernel and is not supported by non-TBS kernel. For details, refer to [TBS Document](http://x5.tencent.com/guide?id=4000)) |
| WMode             | String  | window | When in window mode, you cannot put other page elements over the Flash player. You can change this into opaque or parameter values for other flash wmode if required. Other elements can be placed over the flash player. <br><font color="red">Note: This parameter only applies to Flash players on PC</font> |

**listener**: Object; Optional; List of callback functions in case of playing status change.

| Function Name | Type | Description |
|----------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| playStatus<span id="playstatus" class="anchor"></span> | function | Triggered when playback status changes. Callback function parameter "status": String <br>returned values: <br>ready: "Player is ready", playing: "Playback in progress", playEnd: "Playback ended", error: "Play has finished with an exception or error"  //Since the playback event trigger conditions vary with mobile devices, it is recommended to listen the error when listening the playEnd event to prevent the callback from being executed incorrectly. <br>type: String  The type of error is returned when an error occurs. <br>Example: function(status, type){ ... } |

### 2. Settings and actions

The player objects returned by the constructors can be set using the following methods:

| Method | Description |
|----------------------|-------------------------------|
| resize(width,height) | Parameter: width: int; height: int <br>Function: Set the width and height for current player. <br>Returned value: none |
| play()                                                  | Function: Start to play video.<br>Returned value: Int (common error code)<br><font color="red">Note: This function only applies to Flash players on PC.</font> |
| stop()                                                  | Function: Stop playing video.<br>Returned value: Int (common error code)<br><font color="red">Note: This function only applies to Flash players on PC.</font> |
| pause()                                                       | Function: Pause playing current video.<br>Returned value: Int (common error code)<br><font color="red">Note: This function only applies to Flash players on PC.</font> |
| resume()                                                      | Function: Resume playing video.<br>Returned value: Int (common error code)<br><font color="red">Note: This function only applies to Flash players on PC.</font> |
| addBarrage(barrage) | Parameter: barrage:, array barrage information <br> \[{   <br>"type":"content",  // Message type, content: plain text <font color="red">(Required)</font> <br> "content":"hello world",  // Text message <font color="red">(Required)</font> <br> "time":"1.101" ,//The time length (in sec) between the moment when the current method is called for adding a caption and the moment when the caption is displayed. <font color="red">(Required)</font> <br> "style": "C64B03;35" ,// Separated by semicolons; the first is color value, and the second is font size (optional) <br> "postion":"center"  // Location <br> center: center, bottom: bottom, up: top (optional) }, ... \] <br> Function: Add on-screen comments<br> Returned value: Int [Error Codes](#errorcode) <br> Note: <font color="red">On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC. </font> |
| closeBarrage()                                                |Function: disable on-screen comment. Call addBarrage again to re-enable the feature. <br> Returned value: Int [Error Codes](#errorcode) <br> Note: <font color="red">On-screen comment is only implemented at frontend, and backend functions should be self-developed. This function only applies to Flash players on PC. </font> |

The common error codes of the above methods are as follows:
  
| Error Code<span id="errorcode"></span> | Description |
|---------|---------|
| 200 |Operation successful | 
| 0  | Player not fully initialized | 
| -2 | Unknown operation command | 


## Troubleshooting

### Error codes

List of error codes during the use of SDK<span id="errorcode"></span>

- Error messages returned from the frontend

| Message | Description |
|-------|--------------------------------------------|
| An error occurred while parsing video information. Check whether the parameter is correct. | No JSON data is returned from API. Data cannot be parsed. |
| Video information error. Check whether the parameter is correct. | An error occurred while parsing video information |
| Failed to connect the service. Check the network settings. | Failed to obtain the video channel information. |
| Connection to service is denied.   | Flash request triggered a security exception. |
| Video data is missing. | Video source data is missing. |
| LVB has finished. Try again later. | NetStream.Play.Stop event |
| LVB has finished. Try again later. | Failed to connect to the LVB source. The LVB source has not pushed video content |


- Error messages returned from the backend

| Code  | Message | Description |
|-------|-----------|---------------------------------------|
| 1   	| Database error | Database connection timed out or an error occurred during query. |
| 2     | Failed to connect to LVB source. LVB source has not pushed video content (hls). | M3U8 file cannot be obtained due to LVB source connection failure. |
| 3     | LVB has finished (hls). | Manifest is not a valid M3U8 file, or LVB source has finished. |
|113	| Connection timeout. Try again later. | The parameter is incorrect. |
|1000 | Incorrect channelID or APPID | The app_id is incorrect (length error). |
|1001 | Invalid parameter. Failed to obtain the bizid. | The app_id is incorrect (with a correct length but wrong content). |                  
| 1009  | LVB source has expired. | The broadcast address is invalid. LVB source has expired. |
| 10000 | Request timeout | Timeout when pulling player configuration and video information. Check your network and try again. Timeout is 10 seconds. |
| 10001 | Failed to parse data | Failed to parse the data obtained by pulling player configuration and video information. It may be caused by a network problem or server exception |
| 10002 | Connection timeout. Try again later | Failed to pull player configuration and video information. It may be caused by a network problem or server exception |
| 10008 | Wrong password. Enter again. | Invalid password |
|10020 | Insufficient balance in LVB account. Top up it in time | The balance is insufficient. |
| 11044 | Invalid request | The APPID is missing |
| 11045 | Channel ID is missing in the request parameter. | Channel ID is missing |
| 11046 | Wrong password. Enter again. | Password is missing |
| 20110 | Wrong password. Enter again. | Invalid password |
| 20113 | LVB has finished. Try again later. | Pulling stream does not exist (downstream type is not exist). |
|20201  | LVB has finished. Try again later. | An error occurred while querying pushing stream (get upstream info error). |
|20301  | LVB channel does not exist. Check the channel ID. | Incorrect channel_id (app_id is correct). |



>Note: In case of any error code that is not listed in this table, contact customer service. Our engineers can help you solve the problem.

### FAQs

- **Why is the screen stretched when the video is played in H5?**

    Answer: Video stretching is not supported when playing video in H5. Check if the player container has right width/height configuration.

- **Why did I receive the message that "The LVB has finished. Try again later"?**

    Answer: If you get no response from the LVB address when attempting to connect to this address and fail to connect to it even after five attempts, this message appears. In this case, you need to verify whether the video stream is being pushed and whether the network connectivity is normal.

-  **The video cannot be hidden on the QQ browser.**

    Answer: QQ browser has taken over the video playback function in HTML5, and the X5 kernel uses self-developed player to play videos. QQ browser uses a unified playback interface to ensure user experience. For more information, see [QQ Browser Documentation](http://x5.tencent.com/guide?id=2009)

-  **Video is automatically played in full screen mode on iOS.**

	Answer: By default, video is played in full screen mode on iOS system due to the webkit setting. To achieve inline playback within an App, you can set the webkit-playsinline attribute. Any Safari browser not for iOS 10 or higher is unable to disable the automatic use of full screen mode.

-  **Why does the Flash player have two play buttons in Chrome on PC?**

	Answer: As of Chrome 42, Flash is not played automatically any longer. Only main Flash content is automatically played, and other content is not, unless user opens it manually.

-  **Why can I play LVB videos in browsers on PC, but not on mobile devices?**

    Answer: Only HLS videos are supported in the browsers on mobile devices. Check whether the LVB pulling address contains an HLS pulling URL.

