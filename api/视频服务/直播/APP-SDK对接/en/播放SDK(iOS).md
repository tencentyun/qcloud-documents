## Introduction
The RTMP SDK of Tencent Cloud consists of two parts: **the pusher** and **the player**. This document introduces the related information of the player SDK.

The player SDK supports two standard steam media protocols: **RTMP** and **FLV**. In general, FLV is recommended.

![struct](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_play_sdk_struct.jpg)

The player DEMO interface in the SDK is as follows:

![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_introduction.jpg)

## Fundamentals
 
### Step 1: Create a controller
To display the play interface, you need to create a ViewController, which is inherited from UIViewController. It can be named PlayerController.

```objectivec
#import "TxPush.h"
@interface PlayerController : UIViewController
{
    TXLivePlayer * _txLivePlayer;
	// ...  
}
```

### Step 2:  Creates a player object
Create a **LivePlayer** object, and associate it with the view of the current controller.

```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setupVideoWidget:[UIScreen mainScreen].bounds containView:_myView insertIndex:0]
```

### Step 3:  Binding the rendering interface
There is a _myView parameter in the example code in step 2. This parameter is used to specify the rendering area of video image: the SDK will build an image control on _myView and use it to render the video picture in real time.

If you want to implement UI controls like bullet screen and flower presenting on the rendering picture, you can create a brother view at the same level as _myView as shown below, and superimpose it onto  _myView. Simply, it will be helpful if _myView is only used to render the UI code clear to compilation.
 ![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)

If you want to adjust the size of the rendering interface, just the size of myView. The internal video picture will be adapted automatically according to the size change of myView.

> **[How to make animation?]**
> Animation can be made for myView freely, but note that the target attribute of making animation should be the transform attribute of myView, instead of the frame attribute.
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale (0.3, 0.3); // Shrinks by 1/3
        }];
```

### Step 4:  Start the player
The following code section can be used to start the player:

```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV]; //FLV recommended
```

### Step 5:  Filling & adapting & rotating
If you want to adjust the screen display mode, the SDK also offers several options:
![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)

- **setRenderMode**

| Option | Description  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | Spread this image on the full screen proportionally, and cut off the excess part. Black edges will not be left around the picture under this mode, but some areas may be cut out and cannot be displayed completely.  | 
| RENDER_MODE_FILL_EDGE | Scale the image proportionally and adapt it to the longest edge. After scaling, neither the width nor the height will exceed the display area, the picture is centered, and black edges may be left.  | 

- **setRenderRotation**

| Option | Description  |
|---------|---------|
| HOME_ORIENTATION_DOWN | Normal play (The Home button is just below the picture) | 
| HOME_ORIENTATION_RIGHT | Rotate the picture clockwise by 90° (the Home button is directly to the right of the picture) | 
| HOME_ORIENTATION_UP | Rotate the picture clockwise by 180° (the Home button is just above the picture) | 
| HOME_ORIENTATION_LEFT | Rotate the picture clockwise by 270° (the Home button is directly to the left of the picture) | 



### Step 6:  Hardware acceleration
For businesses requiring blue-ray (1080p) quality, e.g. game LVB, you need to enable hardware acceleration.

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```
 It is strongly recommended to use **stopPlay** before switching to hardware decoding, and then use **startPlay** after switching. Otherwise severely blurred screen may occur.
 
### Step 7:  How to reduce delay and decrease lagging?
#### Why is the latency
**Delay** here refers to the time lag between the VJ and the viewer, and **stuttering** refers playback stops over 500ms.
Video playback quality is affected by network condition. 
![tx_live_service_lag](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_live_service_lag.jpg)

The cloud service and client App introduce buffering to ensure smooth playback, however it will inevitably cause longer delay.
Therefore high delay means high playback quality and low delay brings lower quality. You need to keep a balance between them. Take HLS protocol for example, it introduces 10-30 seconds of delay to achieve a smooth playback.

#### Three Modes
Tencent Cloud provides 3 solutions for latency control:

-**Automatic mode**: This mode can be selected if you are unsure of what your major scenario is.
> Set setAutoAdjustCache to ON in the player to enable the automatic mode. In this mode, the player automatically adjusts latency according to the network conditions. The default latency adjustment range is 1 - 5s. You can also use setMinCacheTime and setMaxCacheTime to edit this value. 

-**Speed mode**: applicable to scenarios requiring low latency
For Speed mode, SetMinCacheTime = setMaxCacheTime = 1s. , the difference between the autotic mode and speed mode is that their MaxCacheTime values are different (in speed mode MaxCacheTime is generally relatively low, while in the automatic mode MaxCacheTime is higher). This flexibility is mainly due to the automatic control technology in the SDK, which automatically adjusts delay without causing lagging. The MaxCacheTime parameter is used to adjust the speed: The higher the MaxCacheTime value is, the more conservative the controlled speed is, and therefore the lower the lagging probability is.
 
-**Smooth mode**: mainly applicable to the**game LVB**and**VOD** and other scenarios which have rather lower requirements for delay.
> When the setAutoAdjustCache switch in the player is turned off, the smooth mode is selected. In this mode, the player uses the same processing strategies as in the cache of the Adobe FLASH kernel: when video lagging appears, it will enter the loading state until the cache is full; then it enters the playing state until the next irresistible network fluctuation occurs. By default, the cache is 5s, which you can change using setCacheTime.
> 
> In less delay-demanding scenarios, this simple model will be more reliable. We introduce this model in the Tencent Cloud SDK mainly because we accept the suggestion of many excellent clients: they want to achieve smooth switching between loading and playing in the playback process. However, in speed mode, pursuit of low delay will lead to too frequent such switching and therefore cause frequent occurrence of the loading symbol.

#### Code interworking
```objectivec
TXLivePlayConfig*  _config = [[TXLivePlayConfig alloc] init];
// Automatic mode
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1;
_config.maxAutoAdjustCacheTime = 5;
// Speed mode
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1;
_config.maxAutoAdjustCacheTime = 1;
// Smooth mode
_config.bAutoAdjustCacheTime   = NO;
_config.cacheTime              = 5;

[_txLivePlayer setConfig:_config];
```

## States

### 1. Principles
The following figure shows the internal technical details of the SDK player:

![SDK internal principles] (http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_player_status_14.jpg)

The simple description is that the RTMP SDK will **attempt to connect to the network** after you **invoke startPlay**. If everything proceeds smoothly, **the main loop of play** will start, and the **current internal status** (net status) will be notified in the SDK every second. If a problem occurs midway, it will be notified in the form of **event**, **warning** or **error**.

### 2. Code Interworking
To get RTMP SDK status notices, provide a **Listener** for the **Player** object. Then all SDK information will be fed back to your App via the Listener.

```objectivec
@interface PlayController ()<UITextFieldDelegate, TXLivePlayListener>
@end
_txLivePlayer.delegate = self;

#pragma - TXLivePlayListener
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param;
{
    // here your code.
}

-(void) onNetStatus:(NSDictionary*) param;
{
    // here your code.
}
```

### 3. Playback Events
You must know several key events in the playback process. Otherwise the process may not be able to run smoothly.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_BEGIN | 2004 | Video playback starts. If the loading symbol appears, then it is the time to stop playback | 
| PLAY_EVT_PLAY_PROGRESS | 2005 | Video playback progress. The current progress and overall progress will be informed | 
| PLAY_EVT_PLAY_LOADING | 2007 | Video loading. If video playback can be recovered, then there will be a BEGIN event |  

We here mention in particular switching between BEGIN and LOADING states:
In the**smooth mode**, the interval from LOADING to BEGIN is generally more than 1s, so this switching process is more obvious.

In**speed mode**, which focuses on low delay, the interval from LOADING to BEGIN may be very fast and frequent. It means that if you at this time display and hide video screen, you experience will be very poor, which is in particular not recommended.

If you use the speed mode, it is recommended that you ignore the LOADING event notices (as Inke does), since the most common lagging is the one lasting hundreds of milliseconds. Or you add a loading animation on the video screen, such as turning chrysanthemum. <font color = 'red'> You are not recommended to overemphasize the UI performance of this switching</font>. Otherwise it is not suitable for the show LVB mode.

### 4. End Events
| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_PLAY_END | 2006 | Video playback ends | 
| PLAY_ERR_NET_DISCONNECT | -2301 | Disconnected from the network, and you can give up after three rescue attempts. Restart video playback and try it again | 

The end of a playback process may be caused by the PLAY_END event, which is the normal end, or by the NET_DISCONNECT event, in which the reason may be disconnected work, or failure to pull data from the server end.

>**Protocol differences**
>> If the LVB address of RTMP, the protocol itself has a relatively perfect command (EOF) to inform the server that video playback has ended, which is the PLAY_END event. For a VOD address, the player also can know the end of the VOD file via a particular method, so the PLAY_END event is also applicable.
> 
> But for the **FLV**protocol which does not support the end notification mechanism, you cannot receive the PLAY_END event, but rely on the NET_DISCONNECT event to know that **"the VJ has left!"**
> 
> A recommended practice is that the VJ informs all viewers after stopping push by sending a group message through the chat message channel.

### 5. Alarm Events
You may not care the following events. We list them here just to tell you what happens. You can use them to send data reports.

| Event ID                 ||    Value  |  Description                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL | 2101 | Failed to decode the current video frame |
| PLAY_WARNING_AUDIO_DECODE_FAIL | 2102 | Failed to decode the current audio frame |
| PLAY_WARNING_RECONNECT | 2103 | Disconnected from the network, automatic reconnection has started (after three reconnection attempts, the PLAY_ERR_NET_DISCONNECT event will be sent directly) |
| PLAY_WARNING_RECV_DATA_LAG | 2104 | Unstable packet transmission from network: It may be caused by insufficient downlink bandwidth, or due to non-uniform push steams at the VJ end |
| PLAY_WARNING_VIDEO_PLAY_LAG | 2105 | The current video playback has lagging |
| PLAY_WARNING_HW_ACCELERATION_FAIL | 2106 | Failed to start hard decoding, soft decoding is used |
| PLAY_WARNING_VIDEO_DISCONTINUITY | 2107 | Current video frames are discontinuous and frame loss may occur|
| PLAY_WARNING_DNS_FAIL | 3001 | RTMP-DNS resolution failed (sent only for the RTMP address) |
| PLAY_WARNING_SEVER_CONN_FAIL | 3002 | RTMP server connection failed (sent only for the RTMP address) |
| PLAY_WARNING_SHAKE_FAIL | 3003 | RTMP server handshaking failed (sent only for the RTMP address) |

### 6. Connection Events
There are also several server connection events that you may not care. They are used to measure and count server connection time and server response time, and are of little use in user interface interaction.

| Event ID                     |    Value  |  Description                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC | 2001 | Connected to the server |
| PLAY_EVT_RTMP_STREAM_BEGIN | 2002 | Connected to the server and starts pull streams (sent only for the RTMP address) |
| PLAY_EVT_RCV_FIRST_I_FRAME | 2003 | The network receives the first renderable video packet (IDR) |


### 7. Status Callback 
 **onNetStatus** is triggered once per second to provide real-time feedback on the status of the current streamer, telling you status of current network conditions and video quality.
  
|   Evaluation parameter                   |  Description                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE | Current CPU utilization | 
| NET_STATUS_VIDEO_WIDTH | Video resolution – Width |
| NET_STATUS_VIDEO_HEIGHT | Video resolution - Height |
| NET_STATUS_NET_SPEED | Current receiving speed of network data |
| NET_STATUS_NET_JITTER | Network jitter, the higher network jitter is, the more unstable the network is |
| NET_STATUS_VIDEO_FPS | The current frame rate for stream media videos |
| NET_STATUS_VIDEO_BITRATE | Current bit rate for stream media videos, in kbps |
| NET_STATUS_AUDIO_BITRATE | Current bit rate for stream media audios, in kbps |
| NET_STATUS_CACHE_SIZE | Cache (jitterbuffer) size. If the current cache size is 0, it is not far from lagging |
| NET_STATUS_SERVER_IP | IP of the connected server | 
















