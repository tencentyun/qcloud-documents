## Features

**Online VOD** means that video files have been stored on the server, and you can implement the **Download and playback** function on the player when have access to the file playback URL.

VOD currently uses FLV, MP4 and HLS formats. We will introduce them respectively:
-**MP4**: A more classic file format, which is supported on most mobile terminals and PC browsers (on iOS and most Android devices, you can play this format using the system browser, or using FLASH on the PC). But the MP4 video file format is complex, so the processing cost is high. The complexity of the index table causes very low loading speeds for MP4 files of more than 5 minutes of will be very slow.

-**HLS**: a standard strongly recommended by Apple, which is supported on most mobile terminals (on iOS and most Android devices, you can play this format using the system browser). However, its support on IE depends on the secondary development of FLASH (for example, Tencent Cloud FLASH player). The streamlined m3u8 index structure can avoid slow loading caused by the **MP4** index. It is a very good choice for VOD.

-**FLV**: a standard strongly recommended by Adobe, which is the most popular encapsulation format on the LVB platform. On the PC, FLASH can provide strong supports. However, on the mobile terminal, only those players implemented on Apps support this format (or using the FLV player), and most phone browsers does not support it. Currently, Tencent Cloud LVB recording use the FLV format.

![](//mc.qcloudimg.com/static/img/9e79a1e82a61b5ae6c45e6da93f3980a/image.png)


## Basics
The online FLV VOD API still reuses the API class of LVB, namely, TXLivePlayer, so they have a lot of similarities in the using mode.

### Step 1: Adding interface elements
In order to be able to display the push preview interface, you need to add the following lines of codes to your layout xml file:
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
android:id="@+id/video_view"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:layout_centerInParent="true"
android:visibility="gone"/>
```

### Step 2:  Creates a player object
Next, create a **Player** object, which is the bearer of all the SDK invoking APIs. However, when a Player object is created, the **TXCloudVideoView** control we just added to the interface needs to be specified for it. It is responsible for picture rendering.
```java
TXCloudVideoView mPlayerView = (TXCloudVideoView) view.findViewById(R.id.video_view);
TXLivePlayer mLivePlayer = new TXLivePlayer(getActivity(), mPlayerView);
```

### Step 3:  Start the player
Use the following codes to start the player:
```java
String vodUrl = "http://2527.vod.myqcloud.com/xxx.flv";
mLivePlayer.startPlay(rtmpUrl, TXLivePlayer.PLAY_TYPE_VOD_FLV);
```
Different from the LVB scenario, here the parameter in startPlay is **PLAY_TYPE_VOD_FLV**, namely, online VOD.

### Step 4:  Adjusting the progress
You can drag the progress bar to adjust playback progress, which is the most obvious difference of VOD compared with LVB. In addition, VOD also supports **Pause** and **Resume**, which are unavailable in LVB, because pause at the player end is meaningless if the streamer does not pause.
```java
// Adjust progress
mLivePlayer.seek(seekBar.getProgress());
// Pause
mLivePlayer.pause();
// Resume
mLivePlayer.resume();
```

### Step 5:  Screen adjustment
If you want to adjust the screen display mode, the SDK also offers several options:
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_render_mode.jpg)
#####  setRenderMode
* RENDER_MODE_FULL_FILL_SCREEN – Fits the image to the screen and trims the excessive part. No black border is left in this mode
* RENDER_MODE_ADJUST_RESOLUTION – Scales up/down the image. The width and height of the scaled image will not exceed the display area. The image is centered and black boarders may be left

#####  setRenderRotation
* RENDER_ROTATION_PORTRAIT - Normal portrait display, best suitable for human figures
* RENDER_ROTATION_LANDSCAPE - Landscape display, more suitable for game LVB




## States
### 1. Playback Events
We may or may not care states in LVB, but VOD is different. We must notice the following three events:

| Event ID                   | Value   | Description   |
| :--------------------- | :--- | :----- |
| PLAY_EVT_PLAY_BEGIN | 2004 | Video playback starts |
| PLAY_EVT_PLAY_PROGRESS | 2005 | Video playback progress |
| PLAY_EVT_PLAY_END | 2006 | Video playback ends |

The progress notification is slightly complicated, because four parameters are contained in param. The following are example codes explaining how to deal with progress notification
```java
public class MyTestActivity implements ITXLivePlayListener{

@Override
public void onPlayEvent(int event, Bundle param) {
    // The following are codes to deal with the playback display events, which means no turning chrysanthemum any more
    if (event == TXLiveConstants.PLAY_EVT_PLAY_BEGIN) {
        stopLoadingAnimation();
    }
    // The following are codes to deal with playback progress
    else if (event == TXLiveConstants.PLAY_EVT_PLAY_PROGRESS) {
        int progress = param.getInt(TXLiveConstants.EVT_PLAY_PROGRESS); //Progress (count of seconds)
        int duration = param.getInt(TXLiveConstants.EVT_PLAY_DURATION); //Time (count of seconds)
        
				// Adjust the UI progress accordingly
				mSeekBar.setProgress(progress);
        mTextStart.setText(String.format("%2d:%2d",progress/60,progress%60));
        mTextDuration.setText(String.format("%2d:%2d",duration/60,duration%60));
        mSeekBar.setMax(duration);
        return;
    }
    // The following are codes to the PLAY_END event
    else if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT
		         || event == TXLiveConstants.PLAY_EVT_PLAY_END) {
        stopPlayRtmp();
        mVideoPlay = false;
    }
}
mLivePlayer.setPlayListener(this);
```

### 2. Error Notification
In terminal development, we usually spend more than 50% of the time dealing with error logics. However, the important logic that you need to care is only network disconnection.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_ERR_NET_DISCONNECT | -2301 | Disconnected from the network, and you can give up after three rescue attempts. Restart video playback and try it again |

### 3. General Warnings
You may not care the following events. We list them here just to tell you what happens. You can use them to send data reports.

| Event ID                           | Value   | Description                            |
| :----------------------------- | :--- | :------------------------------ |
| PLAY_WARNING_VIDEO_DECODE_FAIL | 2101 | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL | 2102 | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT | 2103 | Disconnected from the network, automatic reconnection has started (no retrial after three consecutive automatic reconnections) |
| PLAY_WARNING_RECV_DATA_LAG | 2104 | Unstable packet transmission from network: It may be caused by insufficient downlink bandwidth, or due to non-uniform push steams at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG | 2105 | The current video playback has lagging (intuitive feelings of viewers) |

### 4. Connection Events
There are also several server connection events that you may not care. They are used to measure and count server connection time and server response time, and are of little use in user interface interaction.

| Event ID                     |    Value  |  Description                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC | 2001 | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN | 2002 | Connected to the server and starts pull streams (sent only for the RTMP address) |
| PLAY_EVT_RCV_FIRST_I_FRAME | 2003 | The network receives the first renderable video packet (IDR) |


### 5. Status Callback 
 **onNetStatus** is triggered once per second to provide real-time feedback on the status of the current streamer, telling you status of current network conditions and video quality.
	
|   Evaluation parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_VIDEO_BITRATE | Current bit rate for stream media videos, in kbps |
| NET_STATUS_AUDIO_BITRATE | Current bit rate for stream media audios, in kbps |
| NET_STATUS_VIDEO_FPS | The current frame rate for stream media videos |
| NET_STATUS_NET_SPEED | Current receiving speed of network data |
| NET_STATUS_NET_JITTER | Network jitter, the higher network jitter is, the more unstable the network is |
| NET_STATUS_CACHE_SIZE | Cache (jitterbuffer) size. If the current cache size is 0, it is not far from lagging |




















