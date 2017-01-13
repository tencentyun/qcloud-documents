## Features

**Online VOD** means that video files have been stored on the server, and you can implement the **Download and playback** function on the player when have access to the file playback URL.

VOD currently uses FLV, MP4 and HLS formats. We will introduce them respectively:
-**MP4**: A more classic file format, which is supported on most mobile terminals and PC browsers (on iOS and most Android devices, you can play this format using the system browser, or using FLASH on the PC). But the MP4 video file format is complex, so the processing cost is high. The complexity of the index table causes very low loading speeds for MP4 files of more than 5 minutes of will be very slow.

-**HLS**: a standard strongly recommended by Apple, which is supported on most mobile terminals (on iOS and most Android devices, you can play this format using the system browser). However, its support on IE depends on the secondary development of FLASH (for example, Tencent Cloud FLASH player). The streamlined m3u8 index structure can avoid slow loading caused by the **MP4** index. It is a very good choice for VOD.

-**FLV**: a standard strongly recommended by Adobe, which is the most popular encapsulation format on the LVB platform. On the PC, FLASH can provide strong supports. However, on the mobile terminal, only those players implemented on Apps support this format (or using the FLV player), and most phone browsers does not support it. Currently, Tencent Cloud LVB recording use the FLV format.
![](//mc.qcloudimg.com/static/img/9e79a1e82a61b5ae6c45e6da93f3980a/image.png)

## Fundamentals
The Application Program Interfaces (APIs) of online Video on Demand (VOD) still uses the API class of the Live Video Broadcasting (LVB), that is, TXLivePlayer. Therefore, the use of the API class is similar in many ways.

### step 1: Create a player object.
```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setLogLevel:LOGLEVEL_INFO];
_txLivePlayer.delegate = self; //Play event to be processed
```

### Step 2:  Set the display view.
The player object internally has a rendering UIView. You need to provide a parent view so that the player adds the UIView to the parent view. The parent view can be a view of UIViewController or any view created by you. In addition, you need to provide a frame to specify the position of the rendering view in the parent view.
```objectivec
[_txLivePlayer setupVideoWidget:_videoWidgetFrame containView:self.view insertIndex:0];
```

### Step 3:  Start the player
Use the following codes to start the player:
```objectivec
NSString *vodUrl = @"http://2527.vod.myqcloud.com/xxx.mp4";
[_txLivePlayer startPlay:vodUrl type:PLAY_TYPE_VOD_MP4];
```
Different from the LVB scenario, the parameter in startPlay is **PLAY_TYPE_VOD_MP4**, that is, MP4 online VOD.

### Step 4:  Adjust the progress.
You can drag the progress bar to adjust playback progress, which is the most obvious difference of VOD compared with LVB. In addition, VOD also supports **Pause** and **Resume**, which are unavailable in LVB, because pause at the player end is meaningless if the streamer does not pause.
```objectivec
// Adjust progress
[_txLivePlayer seek:slider.value];
// Pause
[_txLivePlayer pause];
// Resume
[_txLivePlayer resume];
```

### Step 5:  Screen adjustment
If you want to adjust the screen display mode, the SDK also offers several options:
![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_render_mode.jpg)

##### setRenderMode
* RENDER_MODE_FULL_FILL_SCREEN – Fits the image to the screen and trims the excessive part. No black border is left in this mode
* RENDER_MODE_ADJUST_RESOLUTION – Scales up/down the image. The width and height of the scaled image will not exceed the display area. The image is centered and black boarders may be left 

##### setRenderRotation
* RENDER_ROTATION_PORTRAIT - Normal portrait display, best suitable for human figures
* RENDER_ROTATION_LANDSCAPE - Landscape display, more suitable for game LVB

##### resetVideoWidgetFrame
This API is used to dynamically adjust the position and size of the video rendering area during play.


## States
### 1. Playback Events
We may or may not care states in LVB, but VOD is different. We must notice the following three events:

| Event ID                   | Value   | Description   |
| :--------------------- | :--- | :----- |
| PLAY_EVT_PLAY_BEGIN | 2004 | Video playback starts |
| PLAY_EVT_PLAY_PROGRESS | 2005 | Video playback progress |
| PLAY_EVT_PLAY_END | 2006 | Video playback ends |

The progress notification is slightly complicated, because four parameters are contained in param. The following are example codes explaining how to deal with progress notification
```objectivec
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param;
{
    NSDictionary* dict = param;
    
    dispatch_async(dispatch_get_main_queue(), ^{
        if (EvtID == PLAY_EVT_PLAY_BEGIN) {
            // The following are codes to deal with the playback display events, which means no turning chrysanthemum any more
            [self stopLoadingAnimation];
        } else if (EvtID == PLAY_EVT_PLAY_PROGRESS && !_startSeek) {
           // The following are codes to deal with playback progress
            float progress = [dict[EVT_PLAY_PROGRESS] floatValue];
            _playStart.text = [NSString stringWithFormat:@"%02d:%02d",
            (int)progress/60,(int)progress%60];
            [_playProgress setValue:progress];
            float duration = [dict[EVT_PLAY_DURATION] floatValue];
            if (duration > 0 && _playProgress.maximumValue != duration) {
                [_playProgress setMaximumValue:duration];
                _playDuration.text = [NSString stringWithFormat:@"%02d:%02d",
                (int)duration/60,(int)duration%60];
            }
            return ;
        } else if (EvtID == PLAY_ERR_NET_DISCONNECT || EvtID == PLAY_EVT_PLAY_END) {
          // The following are codes to the PLAY_END event
            [self stopRtmp];
            _play_switch = NO;
            [_btnPlay setImage:[UIImage imageNamed:@"start"] forState:UIControlStateNormal];
            [[UIApplication sharedApplication] setIdleTimerDisabled:NO];
            [_playProgress setValue:0];
            _videoPause = NO;
        }
        
        long long time = [(NSNumber*)[dict valueForKey:EVT_TIME] longLongValue];
        int mil = time % 1000;
        NSDate* date = [NSDate dateWithTimeIntervalSince1970:time/1000];
        NSString* Msg = (NSString*)[dict valueForKey:EVT_MSG];
        [self appendLog:Msg time:date mills:mil];
    });
}
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

















