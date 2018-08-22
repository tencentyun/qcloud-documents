
**&Lt;live-player&gt;** is a functional tag in mini programs to support the audio/video downstream (playback) capability. This document mainly describes how to use the tag.

## Supported Version
-  WeChat App for iOS: 6.5.21 and later 
-  WeChat App for Android: 6.5.19 and later 
-  Mini program basic library: 1.7.0 and later 

> With wx.getSystemInfo, you can obtain the version information of the current basic library.

## Use Limits
For policy and compliance considerations, &lt;live-pusher&gt; and &lt;live-player&gt; are not supported by all WeChat mini programs:

- Mini programs of personal and enterprise accounts only support the categories in the following table:

<table>
  <tr align="center">
    <th width="200px">Primary Category</th>
    <th width="700px">Sub-category</th>
  </tr>
  <tr align="center">
    <td>"Social"</td>
		<td>LVB</td>
  </tr>
	<tr align="center">
    <td>"Education"</td>
		<td>Online education</td>
  </tr>
	<tr align="center">
    <td>"Healthcare"</td>
		<td>Internet hospital and public hospital</td>
  </tr>
	<tr align="center">
    <td>"Government Affairs and Livelihood"</td>
		<td>All secondary categories</td>
  </tr>
	<tr align="center">
    <td>"Finance"</td>
		<td>Funds, trusts, insurance, banking, securities/futures, micro-credit of non-financial institutions, credit investigation, and consumer finance</td>
  </tr>
</table>

- For mini programs meeting requirements of categories, you need to enable the component permissions in <font color='red'>"Settings" -> "API Settings"</font> of the mini program management backend, as shown below:

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

Note: If your Mini Program still does not work after the settings are correctly made, that may be because the cache within the WeChat is not updated. Delete the mini program, restart WeChat, and try again.

## Attributes
| Attribute Name | Type | Default Value | Description |
|:-------:|:-------:|:-------:|---------|
| src | String | | Playback URL for audio/video downstream, which can be in the RTMP and FLV format |
| mode | String | live |  live, RTC|
| autoplay | Boolean | false | Whether to play automatically |
| muted | Boolean | false | Whether to mute |
| orientation | String | vertical | vertical, horizontal |
| object-fit | String | contain | contain, fillCrop |
| background-mute | Boolean | false | Turn off the sound when WeChat is running in the backend |
| min-cache | Number | 1 | Minimum buffer delay (in sec) |
| max-cache | Number | 3 | Maximum buffer delay (in sec) |
| bindstatechange | EventHandler |  | Specifies a JavaScript function to accept the player event |
| bindfullscreenchange | EventHandler |  | Specifies a JavaScript function to accept the full screen event |
| debug | Boolean | false | Whether to enable the debug mode |

## Sample Code
```html
<view id='video-box'>  
    <live-player
		wx:for="{{player}}"
		id="player_{{index}}"
		mode="RTC"
		object-fit="fillCrop"
		src="{{item.playUrl}}" 
		autoplay='true'
		bindstatechange="onPlay">
   </live-player>
 </view> 
```

## Ultra-low Latency
The RTC mode of &lt;live-player&gt; supports ultra-low latency linkages within 500 ms. It is suitable for such scenarios as video chats and remote control. To use ultra-low latency mode during the playback, the following points should be taken into consideration:
(1) If the push end is a WeChat Mini Program, use the RTC mode of &lt;live-pusher&gt;.
(2) If the push end is an iOS or Android SDK, use the MAIN_PUBLISHER mode of setVideoQuality.
(3) If the push end is Windows, do not use OBS due to the high latency. The [Windows SDK](https://cloud.tencent.com/document/product/454/7873#Windows) is recommended.
(4) Do not change the min-cache and max-cache values of &lt;live-player&gt;. Use the default values.
(5) Use the ultra-low latency playback URL, i.e. a URL starting with "rtmp://" with a hotlink protection signature, as shown below:

| Item | Example | Latency |
|---------|---------| ----- |
| Ordinary LVB URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc | >2s |
| Ultra-low latency URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc?bizid=bizid&txTime=5FD4431C&txSerect=20e6d865f462dff61ada209d53c71cf9 | < 500ms | 


## Attribute Description
- **src**
Indicates a playback URL for audio/video downstream, which can be in the RTMP format (URLs starting with "rtmp://") and FLV format (URLs starting with "http://" and ending with ".flv"). For more information on how to obtain the push URL of Tencent Cloud, please see [DOC](https://cloud.tencent.com/document/product/454/7915).
> The HLS (m3u8) protocol can be used in &lt;video&gt;, so the &Lt;live-player&gt; tag does not support HLS (m3u8). However, HLS (m3u8) protocol is not recommended for live videos. The delay using HLS will be 10 times higher than that using RTMP and FLV protocols.

- **mode**
The live mode is mainly used for LVB scenarios, such as game broadcasting, online education, and remote training. In this mode, the modules in mini programs will take smooth viewing experience as the priority. By setting the min-cache and max-cache attributes, you can adjust the latency experienced by viewers (playback). The following sections will further describe these two parameters.

 The RTC mode is mainly used in two-way or multi-person video chats, such as financial meetings, online customer service, auto insurance loss assessment, and training sessions. In this mode, the settings for min-cache and max-cache will not take effect, because the delay will be automatically controlled at a very low level (about 500 ms) in mini programs.
 
- **min-cache and max-cache**
The two parameters are used to specify the minimum and maximum buffer time for viewers. The **buffer time** works like a "reservoir", by which players can ease the impact of network fluctuations on viewing smoothness. When stutter or freezing occurs in network packets, the "emergency water" in the "reservoir" can keep players working for a short period of time. As long as the private network speed becomes normal again in this period, smooth video images are rendered continuously in players.

 The more "water" in the "reservoir", the better capability to resist the network fluctuations, and the higher latency for viewers as a consequence. Therefore, it is necessary to use different configurations in different scenarios to achieve the optimal experience balance.
  + For LVB streams with a relatively low bitrate (about 1 Mbps and mainly for character images), min-cache = 1 and max-cache = 3 are recommended.
	+ For LVB streams with a relatively high bitrate (about 2-3 Mbps and mainly for HD game images), min-cache = 3 and max-cache = 5 are recommended.

 In the RTC mode, the settings for the two parameters do not take effect.
 
- **orientation**
Indicates the image rendering orientation. horizontal: original image direction; vertical: 90° clockwise rotated.

- **object-fit**
Indicates the image filling mode. contain: Keep the original aspect ratio of an image, but black edges may appear if the aspect ratio of the video image does not match that of the &lt;live-player&gt; tag. fillCrop: Fill the screen, but the extra part of an image may be cut out if the aspect ratio of the video image does not match that of the &lt;live-player&gt; tag.


- **background-mute**
Indicates whether to turn off the sound when WeChat is running in the backend, to avoid the impact on the video that is being played in mini programs due to screen locking.

- **sound-mode**  
Specifies the playback mode, which can be: ear or speaker. ear: Play sound through a receiver; speaker: Play sound through a speaker. Default is speaker.

- **debug**
 Using the right tool is essential for debugging audio/video features. Mini programs provide the debug mode for the live-pusher tag. In the debug mode, a translucent log window is displayed on the window originally used to render the video images, which is used to display various audio/video metrics and events and reduce the difficulty of debugging. For more information on how to use it, please see [FAQ](https://cloud.tencent.com/document/product/454/7946#2.-.E5.8F.91.E7.8E.B0.E9.97.AE.E9.A2.98.E7.9A.84.E2.80.9C.E7.9C.BC.E7.9D.9B.E2.80.9D).


## Object Operations
- **wx.createLivePlayerContext()**
With the wx.createLivePlayerContext(), the &lt;live-player&gt; tag can be associated with a JavaScript object to perform operations on the object.

- **play** 
Start playback. If the "autoplay" attribute of &lt;live-player&gt; is set as "false" (default value), you can start playback using "play".

- **stop**
Stop playback.

- **pause**  
Pause playback and freeze the last frame.

- **resume**  
Resume playback. Use with "pause".

- **mute**
Turn off the sound.

- **requestFullScreen**
Enter full screen.

- **exitFullScreen**
Exit full screen.

```javascript
var player = wx.createLivePlayerContext('pusher');
player.requestFullScreen({
    success: function(){
		    console.log('enter full screen mode success!')
		}
		fail: function(){
		    console.log('enter full screen mode failed!')
		}
		complete: function(){
		    console.log('enter full screen mode complete!')
		}
});
```

## Internal Events
With the **bindstatechange** attribute of the **&lt;live-player&gt;** tag, you can bind an event handling function that listens on internal events and exception notifications of push module.

#### 1. Key events

| code | Event | Description |   
| :-------------------  |:------------ |  :------------------------ | 
| 2001 | PLAY_EVT_CONNECT_SUCC | Connected to the CVM |
| 2002 | PLAY_EVT_RTMP_STREAM_BEGIN | The server is transmitting audio/video data. | 
| 2003 | PLAY_EVT_RCV_FIRST_I_FRAME | The network receives the first piece of audio/video data. | 
| 2004 | PLAY_EVT_PLAY_BEGIN | Video playback starts. Before this event, you can use the default picture to represent the waiting status. |
| 2006 | PLAY_EVT_PLAY_END | Video playback ends | 
| 2007 | PLAY_EVT_PLAY_LOADING | In the loading status. In this case, the player is waiting for or collecting data from the server. |
| -2301 | PLAY_ERR_NET_DISCONNECT | Network disconnected and unable to reconnect. The player has stopped playing. | 

> When viewers is playing videos from a FLV URL starting with "HTTP://", mini programs will not throw the PLAY_EVT_PLAY_END event in case of disconnection of the LVB stream. This is because the FLV protocol does not define a stop event. As an alternative, you can monitor the PLAY_ERR_NET_DISCONNECT event.

#### 2. Warning Events
Errors in internal warnings are recoverable. The audio/video SDKs in mini programs initiate appropriate recovery measures. The purpose of the warning is mainly to prompt developers or end users of the error, as shown below:

| code | Event | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| 2101 | PLAY_WARNING_VIDEO_DECODE_FAIL | Failed to decode the current video frame |
| 2102 | PLAY_WARNING_AUDIO_DECODE_FAIL | Failed to decode the current audio frame |
| 2103 | PLAY_WARNING_RECONNECT | Network disconnected and auto reconnection has started (the PLAY_ERR_NET_DISCONNECT event will be thrown after three failed attempts) |
| 2104 | PLAY_WARNING_RECV_DATA_LAG | Video stream is not stable. This may be caused by bad network connection. | 
| 2105 | PLAY_WARNING_VIDEO_PLAY_LAG | Stutter occurred during the current video playback |
| 2106 | PLAY_WARNING_HW_ACCELERATION_FAIL | Failed to start hardware decoding. Use software decoding instead. |
| 2107 | PLAY_WARNING_VIDEO_DISCONTINUITY | Current video frames are discontinuous. This may be caused by frame loss. Blurred screen may occur. |
| 3001 | PLAY_WARNING_DNS_FAIL | DNS resolution failed (thrown only if the playback URL starts with "RTMP://") |
| 3002 | PLAY_WARNING_SEVER_CONN_FAIL | Server connection failed (thrown only if the playback URL starts with "RTMP://") |
| 3003 | PLAY_WARNING_SHAKE_FAIL | Server handshake failed (thrown only if the playback URL starts with "RTMP://") |

#### 3. Sample codes
```javascript
Page({
    onPlay: function(ret) {
        if(ret.detail.code == 2004) {
			    console.log('Video playback starts',ret);
        }
    },
	
	/**
	 * Lifecycle function - listening page loading
	 */
	onLoad: function (options) {
	//...
	}
})
```

## Notes
1. &lt;live-player&gt; is a native component created by a client, whose level is the highest. You can use &lt;cover-view&gt; and &lt;cover-image&gt; to overwrite it.

2. Do not use &lt;live-player&gt; in &lt;scroll-view&gt;.


