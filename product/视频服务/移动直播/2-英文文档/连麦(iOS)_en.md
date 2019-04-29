This document mainly describes the interfacing solution of Tencent Cloud's joint broadcasting feature. If you want to learn the principle of the feature, please see [How to Achieve Joint Broadcasting?](https://cloud.tencent.com/document/product/454/8092)

## Version Updating
The joint broadcasting feature is enabled from RTMP SDK 1.8.2. Go to [Download Page](https://cloud.tencent.com/document/product/454/7873) to download the latest RTMP SDK. In addition, the sample codes of this solution have been integrated into the Mini LVB [DEMO](https://cloud.tencent.com/document/product/454/6991).

## Glossary
- **session_id**
> session_id is **a combination of numbers**( such as 1234) and cannot contain any letter. It is used in both push URL and playback URL for joint broadcasting and indicates the studio ID.
>
> We could have directly used the push **LVB code** of a VJ as the studio ID of joint broadcasting to save you from adding parameters because LVB code is the technical designation of LVB studio ID. However, due to historical reasons, background systems of the conventional LVB system and the joint broadcasting system have different key value types, with one being numbers and the other being strings. Therefore, we add the parameter session_id to avoid incompatibility.
> 
> This also brings some advantages. Push URLs are constructed and issued by your server, so your backend system controls the way to generate the session_id, and decides whether to invalidate the parameter after it is used and who is available for it. It is not a good thing to keep these controls in your backstage system.
 
- **Primary VJ & secondary VJ**
> Primary VJ and secondary VJ, which are frequently mentioned in the document, are titles from the perspective of viewers. Primary VJ refers to the VJ showed on the primary screen, generally the initiator of the studio. Secondary VJ is the joint broadcaster generally showed on the secondary screen, which is on the lower left or right corner of the screen.


## Simplifying Joint Broadcasting
For both intra-studio and cross-studio joint broadcasting, the nature is **one-way push + multi-way playback**

- **One-way push**:
Both primary VJ and secondary VJ(s) need to push to make their images visible to others, and should use their own LVB code for the push URL. In addition, they need to add some parameters in the push URL to tell the server that this LVB stream supports joint broadcasting.

- **Multi-way playback**:
For multi-way joint broadcasting, a VJ needs to play equal ways of audio and video data. The latency for joint broadcasting must be within 1 second, so you must use a low-latency playback solution:
 + Using **LVB code of the other side + session_id + push hotlink protection key** to construct a low-delay playback URL. 
 + Using playback parameter **PLAY_TYPE_LIVE_RTMP_ACC** to make TXLivePlayer more adapt to low-latency scenarios.

## Intra-Studio Joint Broadcasting
### Step 1. Primary VJ push
For more information on how to enable LVB feature at the VJ side, please see [iOS Push](https://cloud.tencent.com/document/product/454/7885). If it is your first time to use RTMP SDK, please be sure to read documents about basic push features.

![](//mc.qcloudimg.com/static/img/779bb742c46a415b505cb8b21c6b2c59/image.png)

Note: You need to pay attention to the following points:

- **1.1 Add joint broadcasting parameters to a push URL**
[How to Get a push URL](https://cloud.tencent.com/document/product/454/7915#.E5.90.8E.E5.8F.B0.E8.87.AA.E5.8A.A8 .E6.8B.BC.E8.A3.85.EF.BC.9F) details the construction rules of push URL. if you want to perform joint broadcasting, add additional parameters to the push URL:
![](//mc.qcloudimg.com/static/img/a066ac2f6caf1764b69477a9aa031d0e/image.png)

 **&mix=layer:s;session_id:1234;t_id:1** is used to tell Tencent Cloud that this LVB stream supports joint broadcasting, with the studio ID of joint broadcasting being 1234.
 
 The value of [session_id](#.E5.90.8D.E8.AF.8D.E8.A7.A3.E9.87.8A) can be any **combination of numbers** (such as 1234) and cannot contain any letter. Note: session_ids of two different studios cannot be the same, otherwise errors will occur to the background system. Parameters layer and tid are used for mixing streams on the background and are detailed in [Step 5.2](# step5 .-. E5.A4.9A.E8.B7.AF.E6.B7.B7.E6.B5.81).
 
- **1.2 TXLivePushConfig**
  + Enable echo cancellation enableAEC 
 + Enable hardware acceleration enableHWAcceleration 
 + Set push resolution to VIDEO_RESOLUTION_360_640 (the most common resolution used for LVB show)
 + Set push bitrate to 800 kbps, which is suitable for 360p. If you want a higher resolution, set the bitrate higher.
 + Set audio sampling rate to **AUDIO_SAMPLE_RATE_48000** (do not use other values)

 ``` 
 //Set push parameters first
 _txLivePush.config.enableAEC = YES;
 _txLivePush.config.enableHWAcceleration = YES;
 _txLivePush.config.videoResolution = VIDEO_RESOLUTION_360_640; // The most common resolution used for LVB show
 _txLivePush.config.videoBitratePIN = 800; // This bitrate is suitable for 360p. If you want a higher resolution, set the bitrate higher.
 _txLivePush.config.audioSampleRate = AUDIO_SAMPLE_RATE_48000;  // Do not use other values
 _txLivePush.config.audioChannels   = 1; // Single track
 //Then start push
 [_txLivePush startPush:rtmpUrl];
```

### Step 2. Request joint broadcasting
This step is intended to entitle the primary VJ to the decision-making right on interaction, and to give secondary VJ(s) session_id of low-latency linkage, which is used in step 4.
![](//mc.qcloudimg.com/static/img/8c22aa239260eb464e69ab5c1dacd87b/image.png)

As shown above: Viewer A requests to the VJ: "I want to perform joint broadcasting with you", and the VJ agrees or refuses. If the VJ agrees, the response message of the VJ must bring the session_id in Step 1.1 to A.

In practice, you can use C2C (Client To Client) message channel. Tencent Cloud IM service provides a C2C solution, and you can see [How to Build a Chat Room](https://cloud.tencent.com/document/product / 454/7980) to learn IM service usage.

### Step 3. Secondary VJ push
If the primary VJ agrees, viewer A will become a secondary VJ and then need to push, otherwise the primary VJ cannot see the image of the secondary VJ.
![](//mc.qcloudimg.com/static/img/e65523468a3cdf617f2215b5a07c139a/image.png)

The interfacing solution of secondary VJ push is the same as that of the primary VJ push in Step 1. You also need to pay attention to the following points:

- **3.1 Add joint broadcasting parameters to a push URL**
 + Please see Step 1.1 for the way to construct the push URL.
 + Secondary VJ(s) should use their own LVB code for the push URL, which should be **different from that of primary VJ**, otherwise Tencent Cloud will judge the push as repeated and refuse it.
 + For intra-studio joint broadcasting, it is recommended that the secondary VJ(s) use the session_id of the primary VJ.
 + For cross-studio joint broadcasting, the two VJs have started push before joint broadcasting, so the two session_ids can be different. Because session_id is required to be numbers, if LVB code is numbers, it can direclty used as session_id.
 
- **3.2 TXLivePushConfig**
 + Enable echo cancellation enableAEC 
 + Enable hardware acceleration enableHWAcceleration 
 + Set push resolution to VIDEO_RESOLUTION_320_480. Secondary VJ(s) do not need high resolution because they are shown on secondary screen to viewers
 + Set push bitrate to 300 kbps. High bitrate causes waste)
 + Set audio sampling rate to AUDIO_SAMPLE_RATE_48000 (do not use other values)

 ``` 
 //Set push parameters first
 _txLivePush.config.enableAEC = YES;
 _txLivePush.config.enableHWAcceleration = YES;
 _txLivePush.config.videoResolution = VIDEO_RESOLUTION_320_480; // Secondary VJ(s) do not need high resolution
 _txLivePush.config.videoBitratePIN = 300; // High bitrate causes waste
 _txLivePush.config.audioSampleRate = AUDIO_SAMPLE_RATE_48000;  // Do not use other values
 _txLivePush.config.audioChannels   = 1; // Single track
 
 //Then start push
 [_txLivePush startPush:rtmpUrl];
```


### Step 4. Create a low-latency playback linkage
After Step 1 - Step 3, both primary VJ and secondary VJ(s) have started push, so viewers can see two (or more) screens. However, this is far from enough because VJs can not see each other.

[iOS Playback](https://cloud.tencent.com/document/product/454/7880) details how to use playback feature on the viewer side. If CDN-issued [Playback URL](https://cloud.tencent.com/document/product/454/7915#.E5.90.8E.E5.8F.B0.E8.87.AA.E5.8A.A8.E6 .8B.BC.E8.A3.85.EF.BC.9F) could have been used between VJs, like between VJs and viewers, VJs could certainly see and hear each other.

However, CDN playback URL can cause **delay**, which is definitely unacceptable for real-time communication among VJs. Therefore, we need to adjust TXLivePlayer parameters to keep the delay between primary VJ and secondary VJ(s) below one second:

#### 4.1 Make the primary VJ visible to secondary VJ(s)
Secondary VJ(s) should **switch** to the accelerated linkage instead of using the previous CDN playback URL to receive audio and video streams of primary VJ in low delay.
![](//mc.qcloudimg.com/static/img/a98470959a254737e790f06622b2c4aa/image.png)

#### 4.2 Make secondary VJ(s) visible to the primary VJ
The primary VJ also need to see image(s) of secondary VJ(s), so a low-delay linkage needs to be **added** to receive audio and video streams of secondary VJ(s).
![](//mc.qcloudimg.com/static/img/e17f48dc39b0883cac8af03c39fe53f6/image.png)

#### 4.3 Enable low delay playback
For both primary VJ and secondary VJ(s), low-latency playback linkage can be achieved through **TXLivePlayer*. The method is as follows:

- **4.3.1 Generate a URL for low-latency linkage**
![](//mc.qcloudimg.com/static/img/59c492abef77cddaf026cfd7509de678/image.png)
 + URL must use RTMP as playback protocol because the delay time cannot be minimized to seconds with FLV protocol.
 + session_id must be that of the other side, meaning that secondary VJ(s) should use the session_id of primary VJ when constructing a playback URL. For intra-studio joint broadcasting, we do not need to consider this because both sides use the same session_id.
 +A hotlink protection signature is required for playback address. For more information about signature method, please see [Push Hotlink Protection Calculation](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F). Since almost all the Tencent Cloud customers are configured with **push** hotlink protection key, you can directly use this key to reduce your access expenses.


- **4.3.2 Modify player parameters**
 + The parameter type of startPlay needs to be set to **PLAY_TYPE_LIVE_RTMP_ACC** added in version 1.8.2.
 + Enable echo cancellation in TXLivePlayConfig enableAEC
 + Enable hardware acceleration in TXLivePlayConfig enableHWAcceleration
 + In TXLivePlayConfig, set playback mode to speedy mode and buffer time of the buffer to 200 ms
 
 ``` 
 //Set player parameters
 _txLivePlay.config.enableAEC = YES;              // Enable echo cancellation
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // Speedy​mode - there is obvious delay correction
 _txLivePlay.config.minAutoAdjustCacheTime = 0.2; // 200 ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 0.2; // 200 ms
 
 //Then start playback
 _txLivePlay.enableHWAcceleration = YES;          // Hardware decoding
 [_txLivePlay startPlay:rtmpUrl type:PLAY_TYPE_LIVE_RTMP_ACC];
```

>**Note**: <font color='black'>The accelerated linkage cannot be used to play videos by viewers.</font>
>
> Since the accelerated linkage uses the bandwidth of core node whose cost is several times higher than that of ordinary CDN bandwidth, it is only applicable for the real-time audio and video linkage among VJs.
> In audition, Tencent Cloud limits the number of accelerated linkage under a session_id. The current maximum is 3. It will be increased gradually but no more than 8.

### Step 5. Multi-stream mixing
Step 1 and Step 3 describe how should primary VJ and secondary VJ(s) use their own LVB codes for push. As long as LVB codes of two streams are obtained, all viewers can see video streams superimposed or combined by multiple screens, namely, joint broadcasting is established.

How to achieve video streams superimposed or combined by multiple screens? There are two ways:

#### 5.1 Stream mixing on the client 
RTMP SDK 1.8.2 starts to support multi-instance playback, meaning that you can play multiple LVB concurrently and that video views can be superimposed on each other. In this way, viewers can achieve stream mixing on the client as long as they get URLs of multiple VJs.

- **Advantages of stream mixing on the client**
  + Since App can control the presentation of the viewer side, the interface layout can be more flexible. For example, viewers can drag secondary screen to any location at will.
  
- **Disadvantages of stream mixing on the client**
  + Since downlink data are on multiple ways, bandwidth consumption is higher than that for stream mixing on the server.

- **How to achieve stream mixing on the client**?
  + Since RTMP SDK 1.8.2 starts to support the operation of multiple LVB player instances, you can create multiple TXLivePlayers to achieve multi-stream mixing at the viewer side.
  + It is recommended to use FLV playback URLs, which are more stable.
  + TXLivePlayConfig must be set to speedy mode of 1 second fixed cache to avoid large delay differences among multiple playback instances. The sample codes are as follows:
  
``` 
 //Modify player parameters
 _txLivePlay.config.enableAEC = NO;               // Echo cancellation is not needed at the viewer side
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // Speedy​mode - there is obvious delay correction
 _txLivePlay.config.minAutoAdjustCacheTime = 1;   // 1000 ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 1;   // 1000 ms
 //Then start playback
 _txLivePlay.enableHWAcceleration = YES;          // Hardware decoding
 [_txLivePlay startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

#### 5.2 Stream mixing on the server (Beta)
Stream mixing on the server is a new solution proposed by Tencent Cloud recently. Currently, it is available on the internet but is still in Beta for continuous optimization and improvement. It is an additional module of Tencent Cloud video transcoding cluster, and can directly mix multi-way video streams into one-way stream on the cloud to reduce the downlink bandwidth pressure.
![](//mc.qcloudimg.com/static/img/acc74a1e1a53eb7c248da22832ef894c/image.png)

- **Advantages of stream mixing on the server**
  + Smooth transition can be achieved on the viewer side because the playback URL remains unchanged during the whole joint broadcasting.
  + One-way data can effectively reduce bandwidth consumption under high-concurrence LVB.
  + Since streams are mixed on the server, audio-video synchronization can be better achieved.

- **Disadvantages of stream mixing on the server**
  + The in-Beta feature only supports one-versus-one stream mixing and is less stable.

- **How to enable stream mixing on the server?**
  + In step 1.1, add "layer" and "t_id" to parameter mix for primary VJ: `mix=layer:b;session_id:1234;t_id:1`.
	+ In step 3.1, add "layer" and "t_id" to parameter mix for secondary VJ(s): `mix=layer:s;session_id:1234;t_id:1`.
  + "layer:b" means primary VJ; "layer:s" means secondary VJ (s); and t_id means stream mixing template. Currently, only the template with t_id being 1, namely, primary screen + secondary screen, is supported.
  + After the above operations, once a secondary VJ starts push, a secondary screen will appear on the lower right corner of the LVB stream of primary VJ.



## Cross-Studio Joint Broadcasting
Tencent Cloud RTMP LVB supports cross-studio joint broadcasting for interaction. Therefore, secondary VJ(s) can either be viewers in the current studio or other VJ(s) in another LVB studio.

![](//mc.qcloudimg.com/static/img/f864df3868777e1fd0255c9c1b5f3fc2/image.png)

In interfacing solution, cross-studio joint broadcasting has slight difference with intra-studio joint broadcasting. Therefore, we describe the solution with reference to that of intra-studio joint broadcasting:

### Step 1. Primary VJ push
Please see [Step 1](# step1 .-. E2.80.9C.E5.A4.A.E.BB.BB.E6.92.AD.E2.80.9D.E6.8E.A8.E6. B5.81) of intra-studio joint broadcasting. For both intra-studio and cross-studio joint broadcasting, the primary VJ remains unchanged. You only need to declare in the push URL that joint broadcasting can be achieved.

### Step 2. Request joint broadcasting
- **Intra-studio joint broadcasting**: A viewer requests for joint broadcasting to primary VJ, and will become secondary VJ if the primary VJ agrees and gives the session_id.
- **Cross-studio joint broadcasting**: VJs in the two studios are pushing. Either of them can send a request message to the other for interaction. The situation that a viewer becomes the secondary VJ does not exist.

### Step 3. Secondary VJ push
- **Intra-studio joint broadcasting**: It is recommended that the secondary VJ uses the session_id of the primary VJ because this is simple and is the requirement for two LVB streams to mix on the background.
- **Cross-studio joint broadcasting**: Since VJs in the two studios are in LVB, they can independently specify session_ids without discussion in advance and only need to ensure that their session_ids are different.

### Step 4. Create a low-latency playback linkage
- **Cross-studio joint broadcasting**: Since primary VJ and secondary VJ(s) use different session_ids, VJs must use session_id of the other side when constructing low-delay playback URL, otherwise the video will stutter badly.

### Step 5. Multi-stream mixing
- **Cross-studio joint broadcasting**: Currently multi-stream mixing is only supported on the client and not supported on the server. We will enable a new commen cgi style API. By then, you can view its definition in [Tencent Cloud Server APIs](https://cloud.tencent.com/document/product/454/7920).










