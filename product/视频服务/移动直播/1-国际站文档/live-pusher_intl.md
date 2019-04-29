
**&lt;live-pusher&gt;** is a functional tag in mini programs to support the audio/video upstream capability. This document mainly describes how to use the tag.

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
| url | String |  | Push URL for audio/video upstream |
| mode | String | RTC |  SD, HD, FHD, RTC|
| autopush | Boolean | false | Whether to start pushing |
| muted | Boolean | false | Whether to mute |
| enable-camera | Boolean | true | Enable/disable camera |
| auto-focus | Boolean | true | Manual/auto focusing |
| orientation | String | vertical | vertical, horizontal |
| beauty | Number | 0 | Beauty filter level from 0 to 9. A larger value indicates a stronger effect. |
| whiteness | Number | 0 | Whiteness level from 0 to 9. A larger value indicates a stronger effect. |
| aspect | String | 9:16 | 3:4, 9:16|
| min-bitrate | Number | 200 | The minimum bitrate that determines the worst image clarity |
| max-bitrate | Number | 1,000 | The maximum bitrate that determines the best image clarity |
| audio-quality | String | low | "low" for audio chats and "high" for HD sound | 
| waiting-image | String |  | Waiting image when WeChat is switched to the backend |
| waiting-image-hash | String |  | Waiting image check value when WeChat is switched to the backend |
| background-mute | Boolean | false | Disable the sound collection when WeChat is running in the backend |
| bindstatechange | String |  | Specifies a JavaScript function to accept audio/video events |
| debug | Boolean | false | Whether to enable the debug mode |

## Sample Code
```html
<view id='video-box'>  
	<live-pusher
	      id="pusher"
	      mode="RTC"
	      url="{{pusher.push_url}}" 
	      autopush='true'
	      bindstatechange="onPush">
	</live-pusher>  
 </view> 
```

## Attribute Description
- **url**
Indicates a push URL for audio/video upstream (URL starting with "rtmp://"). For more information on how to obtain the push URL of Tencent Cloud, please see [DOC](https://cloud.tencent.com/document/product/454/7915).
> The RTMP protocol in mini programs supports UDP acceleration version. Under the same network conditions, the RTMP of UDP version features better upstream speed and anti-jitter capability than the open source version.

- **mode**
The SD, HD and FHD modes are mainly used for LVB scenarios, such as game broadcasting, online education, and remote training. SD, HD and FHD indicate three different resolution options. In these modes, mini programs take high-definition and smooth viewing experience as the top priority over low latency.

 The RTC mode is mainly used in two-way or multi-person video chats, such as financial meetings, online customer service, auto insurance loss assessment, and training sessions. In this mode, minimized point-to-point latency and high-quality sound are the top priority. In this case, high definition and smoothness of video images may be reduced.

- **orientation and aspect**
Indicates the horizontal mode or vertical mode. Default is vertical mode. (The Home button is located directly below the image.) The aspect ratio of the video image is 3:4 or 9:16, i.e. width <  height. In the horizontal mode, the aspect ratio of the video image is 4:3 or 16:9, i.e. width  > height.

 The specific aspect ratio is determined by the "aspect" value. Default is 9:16 or 3:4. This is the case where the "orientation" attribute value is "vertical". If the "orientation" attribute value is "horizontal", the aspect ratio 3:4 and 9:16 is equivalent to 4:3 and 16:9 respectively.

- **min-bitrate and max-bitrate**
Video bitrate refers to the amount of video data output by a video encoder per second. With a definite video resolution, the higher the bitrate, the more data output per second, and the better the quality of the image.

 So the two attributes of min-bitrate and max-bitrate are used to determine the minimum and maximum definition of the output video image. Due to the limitation of the network upstream, these two values are limited. But the image clarity is a key metric for assessing the product experience, so the two attributes must hold proper values. The **"Parameter Settings"** section below describes how to set the values.
 
 Mini programs can automatically balance the resolution and bitrate. For example, for a bitrate of 2 Mbps, mini programs select 720p resolution to match, and for a bitrate of 300 Kbps, mini programs select a lower resolution to improve the encoding efficiency. Therefore, you can control the image quality simply by the min-bitrate and max-bitrate parameters.

- **waiting-image and waiting-image-hash**
To protect user privacy, mini programs hope to stop the camera's image collection when WeChat is running in the backend. However, this may lead to poor experience for users due to black screen or frozen screen (stay frozen on the last frame). To solve this problem, you can use the waiting-image attribute by setting an image with the meaning of "waiting" (waiting-image indicates the image URL and waiting-image-hash is the MD5 check value of the image). When WeChat is running in the backend, mini programs use the image as a substitute for the camera screen, using extremely low traffic to maintain the video stream for 3 minutes.

- **debug**
 Using the right tool is essential for debugging audio/video features. Mini programs provide the debug mode for the live-pusher tag. In the debug mode, a translucent log window is displayed on the window originally used to render the video images, which is used to display various audio/video metrics and events and reduce the difficulty of debugging. For more information on how to use it, please see [FAQ](https://cloud.tencent.com/document/product/454/7946#2.-.E5.8F.91.E7.8E.B0.E9.97.AE.E9.A2.98.E7.9A.84.E2.80.9C.E7.9C.BC.E7.9D.9B.E2.80.9D).

## Parameter Settings
The recommended values for these attributes are as follows:

| Scenario | mode | min-bitrate | max-bitrate | audio-quality | Description |
|-------------|:-------:| :-------------: | :-------:| :--------: | ------------ -|
| SD LVB | SD | 300 Kbps | 800 Kbps | high | For narrowband scenarios, such as outdoor or poor network conditions |
| HD LVB | HD | 600 Kbps | 1,200 Kbps | high | For most Apps; recommended for normal LVB scenarios |
| FHD LVB | FHD | 600 Kbps | 1,800 Kbps | high | For scenarios with high requirements for definition; HD is recommended for ordinary mobile phones users |
| Video customer service (user) | RTC | 200 Kbps | 500 Kbps | high | For scenarios that take sound as the priority over images, so do not set the image quality too high | 
| Auto insurance loss assessment (owner) | RTC | 200 Kbps | 1,200 Kbps | high | The image quality can be very high depending on different vehicles. |
| Multi-way conference (main speaker) | RTC | 200 Kbps | 1,000 Kbps | high | High image quality for the main speaker and low quality for participants |
| Multi-way conference (participants) | RTC | 150 Kbps | 300 Kbps | low | Do not set very high image quality and audio quality for participants |

> Unless very low bandwidth scenarios, do not set "low" for the audio-quality, because the audio quality and delay are much worse than those of the "high" mode.

## Object Operations
- **wx.createLivePusherContext()**
With the wx.createLivePusherContext(), the &lt;live-pusher&gt; tag can be associated with a JavaScript object to perform operations on the object.

- **start** 
Start push. If the "autopush" attribute of &lt;live-pusher&gt; is set as "false" (default value), you can start push using "start".

- **stop**
End push.

- **pause**
Pause push.

- **resume**
Resume push. Use with "pause".

- **switchCamera**
Switch between front and rear cameras.

- **snapshot**
Push screenshot. Use the same size as the component. The temporary path for screenshots is ret.tempImagePath.

```javascript
var pusher = wx.createLivePusherContext('pusher');
pusher.start({
    success: function(ret){
		    console.log('start push success!')
		}
		fail: function(){
		    console.log('start push failed!')
		}
		complete: function(){
		    console.log('start push complete!')
		}
});
```

## Internal Events
With the **bindstatechange** attribute of the **&lt;live-pusher&gt;** tag, you can bind an event handling function that listens on internal events and exception notifications of push module.

#### 1. Normal events

| code | Event | Description |   
| :-------------------  |:-------- |  :------------------------ | 
| 1001 | PUSH_EVT_CONNECT_SUCC | Connected to the CVM |
| 1002 | PUSH_EVT_PUSH_BEGIN | Handshake with the server completed; everything is OK; ready to start upstream push |
| 1003 | PUSH_EVT_OPEN_CAMERA_SUCC | Camera enabled. Cannot enable the camera if the camera has been occupied or you have limited permission to the camera. | 

#### 2. Critical errors

| code | Event | Description |  
| :-------------------  |:-------- |  :------------------------ | 
| -1301 | PUSH_ERR_OPEN_CAMERA_FAIL | Failed to enable the camera |
| -1302 | PUSH_ERR_OPEN_MIC_FAIL | Failed to enable the microphone |
| -1303 | PUSH_ERR_VIDEO_ENCODE_FAIL | Video encoding failed |
| -1304 | PUSH_ERR_AUDIO_ENCODE_FAIL | Audio encoding failed |
| -1305 | PUSH_ERR_UNSUPPORTED_RESOLUTION | Unsupported video resolution |
| -1306 | PUSH_ERR_UNSUPPORTED_SAMPLERATE | Unsupported audio sampling rate |
| -1307 | PUSH_ERR_NET_DISCONNECT | Network disconnected. Reconnection attempts have failed for three times, thus no more retries will be performed. Restart the push manually. |

#### 3. Warning events
Errors in internal warnings are recoverable. The audio/video SDKs in mini programs initiate appropriate recovery measures. The purpose of the warning is mainly to prompt developers or end users of the error, as shown below:

- **WARNING_NET_BUSY**
The upstream network is poor. It is recommended to remind users of improving the current network environment, such as getting users closer to their routers or switching to WiFi.

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
The request is rejected by the backend. This is usually caused by miscalculated txSecret in the URL, or because the URL is occupied by others. (Unlike playback URL, only one user can use the push URL.)

| code | Event | Description | 
| :-------------------  |:-------- |  :-----------------------| 
| 1101 | PUSH_WARNING_NET_BUSY | The upstream network is poor. It is recommended to remind users of improving the current network environment. |
| 1102 | PUSH_WARNING_RECONNECT | Network disconnected and auto reconnection has started (auto reconnection will be stopped after three failed attempts) |
| 1103 | PUSH_WARNING_HW_ACCELERATION_FAIL | Failed to start hardware decoding. Use software decoding instead. |
| 1107 | PUSH_WARNING_SWITCH_SWENC | Automatically switch to hardware encoding due to machine performance issues |
| 3001 | PUSH_WARNING_DNS_FAIL | DNS resolution failed and trigger retry process. |
| 3002 | PUSH_WARNING_SEVER_CONN_FAIL | Failed to connect to the server and trigger retry process. |
| 3003 | PUSH_WARNING_SHAKE_FAIL | Server handshake failed and trigger retry process. |
| 3004 | PUSH_WARNING_SERVER_DISCONNECT | Server actively disconnected and trigger retry process. |
| 3005 | PUSH_WARNING_SERVER_DISCONNECT | Socket linkage disconnected due to exception and trigger retry process. |

#### 4. Sample codes
```javascript
Page({
    onPush: function(ret) {
        if(ret.detail.code == 1002) {
			    console.log('Push is successful',ret);
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


