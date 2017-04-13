## Basics
RTMP SDK includes two features, Push and Playback. Push works at the VJ side, while Playback, including Live Video Broadcasting (LVB) and Video On Demand (VOD), works at the viewer side. Before getting started with code interfacing, let's learn some basic facts:

- **LVB and VOD**
<font color='blue'>LVB's</font> video source is generated in real time, and it only makes sense when someone pushes the LVB stream. Therefore, once the VJ stops broadcasting, the LVB URL will become invalid. Since the video is played in real time, no progress bar is displayed on the player during the LVB.

 <font color='blue'>VOD's </font> video source is a file on cloud, which can be played at any time as long as it has not been deleted by the provider. Since the entire video file is stored on the server, a progress bar will be displayed during the playback.

- **Supported Protocols**
The commonly used LVB protocols are as follows. It is recommended to use the LVB URL based on FLV protocol (starting with "http" and ending with ".flv") at the APP side:
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

 The commonly used VOD protocols are as follows. Currently, the HLS-based URL (starting with "http" and ending with ".m3u8") is the mostly used in VOD:
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## Special Notes
Tencent Cloud RTMP SDK **DOES NOT** impose any limit on the source of playback URL, which means it is applicable to both Tencent Cloud and non-Tencent Cloud playback URLs. But the player in RTMP SDK only supports the LVB URLs in FLV, RTMP and HLS (m3u8) formats and the VOD URLs in FLV, MP4 and HLS (m3u8) formats.

## Interfacing Guide

### Step 1:  Add a View
To display the video views in a player, we first need to add the following codes in the layout xml file:
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### Step 2:  Create a Player
Next, create a **TXLivePlayer** object, and then use API `setPlayerView` to associate it with the **video_view** control we just added to the interface.
```java
// mPlayerView is the interface View added in Step1 
TXCloudVideoView mPlayerView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//Create a Player object
TXLivePlayer mLivePlayer = new TXLivePlayer(getActivity());
//Key Player object and interface View
mLivePlayer.setPlayerView(mPlayerView);
```

### Step 3:  Start the Player
```java
String flvUrl = "http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
mLivePlayer.startPlay(flvUrl, TXLivePlayer.PLAY_TYPE_LIVE_FLV); //FLV is recommended
```
Parameter type supports the following options. According to the feedback from some customers, **"fast forward" sometimes occurs during the playback**. In fact, this is caused by their confusion between LIVE_FLV and VOD_FLV.

| Option | Enumerated Value | Description |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | The input URL is a RTMP-based LVB URL |
| PLAY_TYPE_LIVE_FLV| 1 | The input URL is an FLV-based LVB URL |
| PLAY_TYPE_VOD_FLV | 2 | The input URL is a RTMP-based VOD URL |
| PLAY_TYPE_VOD_HLS | 3 | The input URL is an HLS (m3u8)-based VOD URL |
| PLAY_TYPE_VOD_MP4 |4 | The input URL is an MP4-based VOD URL |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | Low-latency LVB URL with a microphone link (only for scenarios where micropone is added) |
| PLAY_TYPE_LOCAL_VIDEO | 6 | Local video file on mobile phone |

### Step 4:  Adjust the View

- **view: Size and Position**
You can modify the size and position of the view by directly adjusting the size and position of the "video_view" control added in Step1.

- **setRenderMode: Full Screen or Self-Adaption**

| Option | Description |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | The full screen is filled with the view that is spread proportionally, with the excess parts cut out. In this mode, black edges will not appear on the screen, but the view may not be displayed completely because some areas are cut out. |  | 
| RENDER_MODE_FILL_EDGE | The view is scaled proportionally to adapt to the longest edge. Both the width and the height of the scaled view will not extend beyond the display area and the view is centered. In this mode, black edges maybe appear on the screen. |  | 

- **setRenderRotation: Screen Rotation**

| Option | Description |
|---------|---------|
| HOME_ORIENTATION_DOWN | Normal play (The Home button is directly below the screen) | 
| HOME_ORIENTATION_RIGHT | The screen rotates 90° clockwise (the Home button is directly to the right of the screen) | 
| HOME_ORIENTATION_UP | The screen rotates 180° clockwise (the Home button is directly above the screen) | 
| HOME_ORIENTATION_LEFT | The screen rotates 270° clockwise (the Home button is directly to the left of the screen) | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### Step 5:  Adjust the Progress
Adjustment of playback progress **is only applicable to VOD**, because it is impossible to change the progress of LVB's real-time video source.
```java
// Adjust the progress
mLivePlayer.seek(seekBar.getProgress());
```

### Step 6:  Pause the Playback
- **VOD**
It goes without saying that you have known what use of the pause function is in VOD.

-**LVB**
For LVB, calling pause function means temporarily stopping stream-pull. The player will not be destroyed, but will display the last frame.

```java
//Pause
mLivePlayer.pause();
//Resume
mLivePlayer.resume();
```

### Step 7:  End the Playback
At the end of the playback, **be sure to destroy the View control**, especially before the next startPlay, otherwise a lot of memory leaks and a splash screen will occur.

At the same time, when exiting the playback interface, be sure to call the `onDestroy()` function for rendering View, otherwise memory leak and the warning message that **Receiver not registered** may occur.
```java
@Override
public void onDestroy() {
	super.onDestroy();
	mLivePlayer.stopPlay(true); // true indicates the last frame is cleared
	mPlayerView.onDestroy(); 
}
```

The boolean parameter of stopPlay means "whether to clear the last frame". The LVB players in the earlier versions of RTMP SDK's did not have the concept of Pause, so the boolean value is used to control the clearing of the last frame.

### Step 8:  Hardware Acceleration
For blu-ray (1080p) quality, it is difficult to get a smooth playback experience just by means of software decoding. Therefore, if your scenario focuses on LVB games, it is recommended to enable hardware acceleration.

It is strongly recommended to perform **stopPlay** before the switching between software decoding and hardware decoding, and then perform **startPlay** after switching. Otherwise seriously blurred screen may occur.

```java
 mLivePlayer.stopPlay(true);
 mLivePlayer.enableHardwareDecode(true);
 mLivePlayer.startPlay(flvUrl, type);
```

### Step 9:  Recode the Captured Stream
Recoding Captured Stream means that during the LVB, the viewer can capture and record a segment of video by clicking the "Record" button and publish the recorded content via the video delivery platform (e.g. Tencent Cloud's VOD system) so that the content can be shared through UGC message on social platforms such as the "Moment" of WeChat.

![](//mc.qcloudimg.com/static/img/2963b8f0af228976c9c7f2b11a514744/image.png)

```java
// Specify an ITXVideoRecordListener to synchronize the progress and results of the recording
mLivePlayer.setVideoRecordListener(recordListener);
// Start recording. It can be placed in the response function of the "Record" button. Currently only recording video source is supported, recording Barrage or other content is not supported.
mLivePlayer.startRecord(int recordType);
// ...
// ...
// End the recording. It can be placed in the response function of the "End" button
mLivePlayer.stopRecord();
```

- The progress of recording is indicated as a time value by ITXVideoRecordListener's onRecordProgress.
- Recorded file is in the format of MP4, and is indicated by ITXVideoRecordListener's onRecordComplete.
- TXUGCPublish is responsible for uploading and publishing the video. For details on how to use it, refer to [UGC Small Video](https://www.qcloud.com/document/product/454/8843).
 
## Status Monitor
Tencent Cloud RTMP SDK is always designed on a basis of White Box. You can bind a **TXLivePlayListener** for TXLivePlayer object so that you can be informed of the internal status of SDK through onPlayEvent (Event Notification) and onNetStatus (Quality Feedback).

### 1. Playback Events
| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_BEGIN | 2004 | Video playback begins. The "loading" icon stops flashing at this point. | 
| PLAY_EVT_PLAY_PROGRESS | 2005 | The progress of video playback, including current progress and overall progress. **This is only applicable to VOD** | 
| PLAY_EVT_PLAY_LOADING | 2007 | Loading of video playback. If video playback is resumed, the event will be followed by a BEGIN event.|  

- **Do not hide the playback view after receiving PLAY_LOADING**
The time length between PLAY_LOADING and PLAY_BEGIN varies in a range from 5ms to 5s. Some customers consider hiding the view upon LOADING and displaying it upon BEGIN, which will cause serious flicker (especially in the LVB scenario). It is recommended to place a overlay of translucent Loading animation on top of the video view.

- **The frequency of LOADING is determined by the cacheTime**
In TXLivePlayConfig, attribute cacheTime can be set for player. Too small cacheTime value can cause a high frequency of LOADING. In case of frequent LOADING, please make an adjustment by referring to [Stutter & Latency](#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F).

- **Work with PLAY_PROGRESS playback progress**
If you have no idea abouthow to handle the PLAY_EVT_PLAY_PROGRESS event during VOD, refer to the sample code - [Playback Progress](https://www.qcloud.com/document/product/454/7887).

### 2. Ending Events
| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_END | 2006 | Video playback ends. | 
| PUSH_ERR_NET_DISCONNECT          | -2301 | Network connection is broken and fails to be restored even after several reconnection attempts. Please try again by restarting the playback. | 

- **How to check whether the LVB has ended?**
For **VOD**, we can use the PLAY_EVT_PLAY_END event to check whether the playback has ended.

 For **LVB**, RTMP SDK itself alone is unable to know whether the VJ has stopped pushing stream. It is expected that when the VJ stops pushing stream, RTMP SDK will soon find the data stream pull fails (WARNING_RECONNECT), and then retry it again until the PLAY_ERR_NET_DISCONNECT event is thrown after three failed attempts.

 The reason for this problem is that the standard playback protocol itself does not have a common STOP standard, so it is recommended to achieve your purpose by broadcasting a system message of **"LVB has ended"** through the chat room.
 
### 3. Warning Events
You don't need to consider the following events. We just list the information of these events for a synchronization purpose based on White Box design of SDK.

| Event ID                 |    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL | 2101 | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL | 2102 | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT | 2103 | Disconnected from the network and automatic reconnection has been started (after three reconnection attempts, the PLAY_ERR_NET_DISCONNECT event will be thrown directly) |
| PLAY_WARNING_RECV_DATA_LAG | 2104 | Unstable incoming packet from network: It may be caused by insufficient downstream bandwidth, or by the non-even outgoing stream at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG | 2105 | Stutter occurred during the current video playback |
| PUSH_WARNING_HW_ACCELERATION_FAIL | 2106 | Failed to start hard-coding; Soft-coding is used |
| PLAY_WARNING_VIDEO_DISCONTINUITY | 2107 | Current video frames are discontinuous and frame loss may occur|
| PLAY_WARNING_DNS_FAIL | 3001 | RTMP-DNS resolution failed (thrown only for a RTMP-based URL) |
| PLAY_WARNING_SEVER_CONN_FAIL | 3002 | RTMP server connection failed (thrown only for a RTMP-based URL) |
| PLAY_WARNING_SHAKE_FAIL | 3003 | RTMP server handshaking failed (thrown only for a RTMP-based URL) |

### 4. Connection Events
In addition, there are several server connection events used to measure and calculate the time for server connection. They are also outside your concern.

| Event ID                     |    Value  |  Description                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC | 2001 | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN | 2002 | Connected to the server and started to pull the stream (thrown only for a RTMP-based URL) |
| PLAY_EVT_RCV_FIRST_I_FRAME | 2003 | The network has received the first renderable video packet (IDR) |


### 5. Status Callback 
 **The onNetStatus**notification is triggered once per second to provide real-time feedback on the status of current pusher. Like a car dashboard, it can offer you a picture about what is happening inside the current SDK, so that you can keep track of current network conditions and video quality.
  
|   Evaluation Parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
NET_STATUS_CPU_USAGE | Instantaneous value of current CPU usage| 
| NET_STATUS_VIDEO_WIDTH | Video resolution – Width |
| NET_STATUS_VIDEO_HEIGHT | Video resolution - Height |
| NET_STATUS_NET_SPEED | Current speed at which the network data is received |
| NET_STATUS_NET_JITTER | Network jitter status - the bigger the network jitter is, the more unstable the network is |
| NET_STATUS_VIDEO_FPS | The video frame rate of current streaming media |
| NET_STATUS_VIDEO_BITRATE | Video bit-rate of current streaming media (kbps) |
| NET_STATUS_AUDIO_BITRATE | Audio bit-rate of current streaming media (kbps) |
| NET_STATUS_CACHE_SIZE | Size of cache (jitterbuffer). The cache length of 0 means that stutter will occur in all probability.|
| NET_STATUS_SERVER_IP | IP of the connected server | 

 
## Stutter & Latency
For **LVB products**, the pursuit of low stutter rate and low latency is always a hot topic. Many customers believe that stutter rate and latency totally depend on the quality of cloud. In fact, the pusher modules and**players themselves play a more critical, more decisive role in this respect**. With the same network environment and playback URL, a good player and a poor one can exhibit significant difference in terms of stutter rate and latency.

### 1. What You Must Know About Stutter and Latency
**Latency** is the delay of data transmission from VJ to viewer, and **stutter** refers to frame freezing that lasts for at least 500ms.

In a flawless network environment, it is possible to easily achieve an ultra-low latency without stutter. In reality, however, the imperfect network environment inevitably leads to congestion and packet loss during the data transmission over the Internet:
![tx_live_service_lag](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_live_service_lag.jpg)

In order to alleviate these unstable factors, some buffers need to be introduced to the cloud service and terminal APPs, which will inevitably cause latency.

Therefore, **latency and smoothness** are the two ends of a balance, focusing too much on low latency will lead to slight network fluctuations that produce significant stutter at the player side. Conversely, overemphasis on smoothness will cause high latency. A typical case is the HLS (m3u8) protocol, which ensures a smooth playback experience by introducing a latency of 10-30 seconds.

### 2. Three Modes
In order to allow you to get better playback experience without the need to have much knowledge about stream control and processing, Tencent Cloud RTMP SDK, being optimized over several versions, develops a set of automatic adjustment technologies, based on which three excellent latency control schemes are introduced:

-**Auto mode**: If you are not sure about what your main scenario is, you can use this mode.
> You can enter the Auto mode by turning on the setAutoAdjustCache switch in TXLivePlayConfig. In this mode, the player will automatically adjust latency based on current network conditions (by default, the player will automatically adjust latency within the range of 1s-5s. You can use setMinCacheTime and setMaxCacheTime to modify the default) to minimize the latency between VJ and viewer while ensuring sufficient smoothness, and thus to deliver a good interactive experience.

-**Speedy mode**: Suitable for **Showtime LVB** and other scenarios which have high requirement for latency.
> Speedy mode (set by making **SetMinCacheTime = setMaxCacheTime = 1s**) and Auto mode only differ in MaxCacheTime value (generally, MaxCacheTime is lower in Speedy mode and is higher in Auto mode). This flexibility can be largely attributed to the automatic control technology within the SDK, which automatically adjusts latency without causing stutter. MaxCacheTime is used to adjust the control speed -  the higher the MaxCacheTime value is, the more conservative the control speed is, and therefore the lower the probability of stutter becomes.
 
- **Smooth mode**: Suitable for **Game LVB** and other HD (high bit rate) LVB scenarios.
> You can enter the Smooth mode by turning off setAutoAdjustCache switch in the player. In this mode, the player uses a processing strategy that is similar to the caching strategy of the Adobe FLASH kernel. When stutter occurs in a video, the video will go into the loading status until the cache is full; then it will go into the playing status until the next network fluctuation that can't be resisted. By default, the cache time is 5s, which you can change using setCacheTime.
> 
> This seemingly simple mode will be more reliable in scenarios that have a low requirement for latency, because the mode in essence trades off latency slightly for a reduced stutter rate.

### 3. Code Interfacing
```java
TXLivePlayConfig mPlayConfig = new TXLivePlayConfig();

// Auto mode
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(5);

// Speedy mode
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);

// Smooth mode
mPlayConfig.setAutoAdjustCacheTime(false);
mPlayConfig.setCacheTime(5);

mLivePlayer.setConfig(mPlayConfig);
```
