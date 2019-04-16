# Tencent Video Cloud RTMP SDK Documentation - Joint Broadcasting - Upgraded Solution (Android) #

-----------------------------------------------------------------------------------------------------------------

This document introduces how to interface with the upgraded Tencent Video Cloud joint broadcasting solution. For more information on how to interface with the old joint broadcasting solution, please see [Android Joint Video Broadcasting (old solution)](https://cloud.tencent.com/document/product/454/8091). If it is your first time to use the joint broadcasting feature, we strongly recommend you to use the upgraded joint broadcasting solution.

### Demo
Before introducing the guide on interfacing with the upgraded joint broadcasting solution, we will provide joint broadcasting Demo from version 2.0.3, to help you quickly understand how the joint broadcasting works.

![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/linkmic_demo_step.png)

If user A and user B start a joint broadcasting session, the method in joint broadcasting Demo is:

1. Both user A and user B generate their push URLs and pull URLs respectively. Please note that, **pull URLs must contain hotlink protection key (i.e. parameters "bizid", "txSecret" and "txTime")**. For more information about the method for generating URLs, please see [Accelerated Pull URL](https://cloud.tencent.com/document/product/454/8872#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E4.BA.92.E7.9B.B8.E6.8B.89.E6.B5.818) below:

```
Push URL A: rtmp://3891.livepush.myqcloud.com/live/3891_streamA?bizid=3891&txSecret=9d6e1a1ec1dde00dab718e5684ad53a3&txTime=5919D07F

Pull URL A: rtmp://3891.liveplay.myqcloud.com/live/3891_streamA?bizid=3891&txSecret=9d6e1a1ec1dde00dab718e5684ad53a3&txTime=5919D07F

Push URL B:rtmp://3891.livepush.myqcloud.com/live/3891_streamB?bizid=3891&txSecret=d37f5d7c6a3cd426105e57d6eb4900e8&txTime=5919D07F

Pull URL B:rtmp://3891.liveplay.myqcloud.com/live/3891_streamB?bizid=3891&txSecret=d37f5d7c6a3cd426105e57d6eb4900e8&txTime=5919D07F
```

2. In the joint broadcasting Demo TAB interface, user A and user B scan **their push URLs** and enable push respectively. You can click "Primary VJ" or "Secondary VJ" buttons at the bottom right corner to simulate primary VJ push or secondary VJ push;
3. In the joint broadcasting Demo TAB interface, user A and user B click "+" button at the top right corner, scan *each other's pull URL*, and add a pull stream;
4. After step 2 and step 3, user A and user B have pulled each other's video stream during push, that is, a real-time two-way video session is established between two users, as shown below.

![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/linkmic_demo_example.png)

Notes:
- In Step 3 "scan a pull URL and add a pull stream", the hotlink protection key must be added in the pull URL. Only with this key, can pull playback be achieved in the Demo by using accelerated pull API discussed later in this document, to reduce video latency and eliminate audio echo;
- In this joint broadcasting Demo, since we only establish a real-time two-way video session between primary VJ and secondary VJ without mixing video streams, the third-party viewers can only see the video image of primary VJ. In practice, the joint broadcasting can only be achieved by mixing video streams of primary and secondary VJs using [Video Stream Mixing Method](https://cloud.tencent.com/document/product/454/8872#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E5.90.AF.E5.8A.A8.E6.B7.B7.E6.B5.8111) discussed later in this document.

### Interfacing Guide

To use the upgraded joint broadcasting solution, you need to upgrade SDK to version 2.0.1 or above. Compared to the old solution, the upgraded one is more powerful with the following key features:

- Multi-way joint broadcasting is supported, and a maximum of 3 secondary VJs can join with primary VJ in a video broadcasting session at a time
- The location of secondary screen after stream mixing can be customized
- You can start a video stream mixing process in a more flexible way. Any two video streams (four streams at most) can be mixed into one video by calling CGI


You can start a joint video broadcasting session using upgraded solution by following the three steps below:

1. **Enable push**: Before starting a push process, a secondary VJ should send a request for joint broadcasting to primary VJ, and then enable push after receiving a response for acceptance of joint broadcasting from primary VJ. If the push is successful, the secondary VJ will send its pull URL to primary VJ, so that primary VJ can pull its video stream;
2. **Pull each other's stream**: Primary VJ and secondary VJ pull each other's video stream using accelerated pull API provided by RTMP SDK (to significantly reduce the latency), so that a two-way video session can be established between primary VJ and secondary VJ;
3. **Enable stream mixing**: By calling video stream mixing CGI provided by Video Cloud, you can overlay the video of secondary VJ onto the video stream of primary VJ (including audio), and other viewers can see the video images of both primary VJ and secondary VJ automatically.

If multiple secondary VJs join with primary VJ in a broadcasting session at the same time: for step 2, secondary VJs are required to pull each other's stream to establish multi-way video session; for step 3, you need to overlay the videos of secondary VJs onto the video stream of primary VJ by calling stream mixing CGI.



### Step 1: Enable push

In the upgraded solution, when enabling push, both primary and secondary VJs **don't need to add joint broadcasting parameter after their push URLs**. However in old solution, the primary VJ needs to add the joint broadcasting parameter "mix=layer:b;session_id:xxxx;t_id:1" and secondary VJ needs to add "mix=layer:s;session_id:xxxx;t_id:1" to enable video stream mixing on server. For upgraded solution, the video stream mixing is enabled by calling backend CGI to provide a higher flexibility;

For more information on how to enable LVB push feature at the VJ side, please see [Android Push](https://cloud.tencent.com/document/product/454/7885). If it is your first time to use RTMP SDK, please be sure to read relevant document about basic push features.

There are two points to note about the push under the joint broadcasting mode: 1. You need to enable echo elimination; 2. You need to control latency using appropriate control policy. Actually, you don't need to worry about these two points. We strongly recommend you to use video quality configuration API "setVideoQuality" provided by SDK with a version of 1.9.2 or above. Each of the following enumerated video qualities corresponds to a set of quality parameters (such as video resolution, bitrate, frame rate, whether to enable echo elimination), and all of them have been optimized, please feel free to use.

```
/**
 * Video quality description
 */
public static final int VIDEO_QUALITY_STANDARD_DEFINITION       = 1;  //Standard definition
public static final int VIDEO_QUALITY_HIGH_DEFINITION           = 2;  //High definition
public static final int VIDEO_QUALITY_SUPER_DEFINITION          = 3;  //Ultra high definition
public static final int VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER    = 4;  //Primary VJ, used under the joint broadcasting mode
public static final int VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER     = 5;  //Secondary VJ, used under the joint broadcasting mode
```


Detailed description of the above three video qualities

- VIDEO_QUALITY_STANDARD_DEFINITION: Standard definition - A resolution of 360 * 640 is used, and the bitrate is adaptive within the range of 400 kbps - 800 kbps. If the network environment of VJ is unsatisfactory, the video quality may be lowered during LVB, but the overall stutter rate will stay low. Software encoding is used. Even through software encoding is high in power consumption, it is more applicable for moving images than hardware coding.
- VIDEO_QUALITY_HIGH_DEFINITION: High definition - A resolution of 540 * 960 is used, and the bitrate is fixed to 1000 kbps. If the network environment of VJ is unsatisfactory, the video quality will remain unchanged during LVB, but stutters and frame skips may occur frequently.  Software encoding is used. Even through software encoding is high in power consumption, it is more applicable for moving images than hardware coding.
- VIDEO_QUALITY_SUPER_DEFINITION: Ultra high definition - A resolution of 720 * 1280 is used, and the bitrate is fixed to 1500 kbps. It has a high requirement for uplink bandwidth of VJ, and is suitable for business scenarios where videos are viewed in large screens.
- VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER: Primary VJ - It is used by primary VJ in joint broadcasting mode. Since it is the primary screen for viewers, a resolution of 540 * 960 is preferred for clarity.
- VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER: Secondary VJ - It is used by secondary VJ in joint broadcasting mode. Since it is the secondary screen, a resolution of 320 * 480 and a bitrate of 350 kbps are used for fluency.

Notes:

1. For a live show, it is recommended to use "high definition".
2. After using setVideoQuality, you can still configure the video quality using TXLivePushConfig, and the last configured value shall prevail.
3. If you watch videos on your phone, it is generally recommended not to use "high definition", because after many times of subjective evaluation on video qualities, they are nearly the same for videos played on small screens.

#### Primary VJ Push
Primary VJ enables push by calling the following APIs:

```
TXLivePushConfig config = new TXLivePushConfig();
config.setAudioSampleRate(48000); //Audio sampling rate is 48 KB by default. Do not set it to another value 
mLivePusher = new TXLivePusher(context);
mLivePusher.setPushListener(listener);
mLivePusher.setConfig(config);
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION); //Non-joint broadcasting mode: High definition
mLivePusher.startCameraPreview(txCloudVideoView);
mLivePusher.startPusher(pusherUrl);
```


If a secondary VJ joins with primary VJ in a broadcasting session, that is "after the first secondary VJ join a joint broadcasting session", please call:

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER); //Joint broadcasting mode: Primary VJ
```


If no secondary VJ joins with primary VJ in a broadcasting session, that is "after the last secondary VJ exits from a joint broadcasting session", please call:

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION); //Non-joint broadcasting mode: High definition
```


By calling API setVideoQuality, SDK will automatically select the optimal video quality parameters, such as resolution, frame rate, bitrate and bitrate control policy. Please note that, if no secondary VJ joins with primary VJ in a broadcasting session, it is strongly recommended not to select VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER. Because this mode is designed to minimize the latency, the fluency may be affected. If echo elimination is enabled at the same time, there may be a compromise on performance.

#### Secondary VJ Push
Secondary VJ enables push by calling the following APIs:

```
TXLivePushConfig config = new TXLivePushConfig();
config.setAudioSampleRate(48000); //Audio sampling rate is 48 KB by default. Do not set it to another value 
mLivePusher = new TXLivePusher(context);
mLivePusher.setPushListener(listener);
mLivePusher.setConfig(config);
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER);	//Joint broadcasting mode: Secondary VJ
mLivePusher.startCameraPreview(txCloudVideoView);
mLivePusher.startPusher(pusherUrl);
```


By calling API setVideoQuality and selecting VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER, SDK will automatically select the optimal video quality parameters, such as resolution, frame rate, bitrate and bit rate control policy, and enable audio echo elimination at the same time.

Notes:

- Before starting a push process, secondary VJ should send a request for joint broadcasting to primary VJ, and then enable push after receiving a response for acceptance of joint broadcasting from primary VJ.
- If the push is successful, that is, after secondary VJ receives push enabling event PUSH_EVT_PUSH_BEGIN, it will send its pull URL to primary VJ, so that the primary VJ can pull its video stream. For multi-way joint broadcasting, secondary VJs need to send their pull URLs to each other for pulling.
- The only reason for secondary VJ pull is start a joint broadcasting session. Please do not add the pull URL of secondary VJ into your APP's LVB list.

### Step 2: Pull each other's stream

Under the joint broadcasting mode, the primary VJ and secondary VJ must pull each other's stream using accelerated pull API provided by SDK. Before we introduce how to use the accelerated pull API, you need to know three scenarios where primary VJ and secondary VJ need to pull each other's stream:

- Before a secondary VJ joins a broadcasting session, viewers watch primary VJ's video using generic pull API (document [Android Pull](https://cloud.tencent.com/document/product/454/7886)). After a secondary VJ joins a broadcasting session, viewers must watch primary VJ's video using accelerated pull API. After a secondary VJ exits from a joint broadcasting session, viewers must change the API to generic pull API to watch primary VJ's video.
- Before joining a broadcasting session, the primary VJ does not need to pull the video stream. Under the joint broadcasting mode, the primary VJ needs to watch secondary VJ's video using accelerated pull API.
- If multiple secondary VJs (a maximum of three VJs is supported currently) join with primary VJ in a broadcasting session at the same time: The primary VJ needs to pull each secondary VJ's video stream using the accelerated pull API. In addition to primary VJ's video stream, a secondary VJ also needs to pull the video streams of other secondary VJs.

Next, we will introduce how to use the accelerated pull API in details:

#### 1. URL used to generate the accelerated pull linkage

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/RTMP加速拉流地址.png)

Please note:

- URL must use RTMP playback protocol, because the delay time cannot be minimized to seconds with FLV protocol.
- A hotlink protection signature is required for playback URL. For more information about signature method, please see [Push Hotlink Protection Calculation](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F). Since almost all the Tencent Cloud customers are configured with push hotlink protection key, you can directly use this key to reduce your access expenses. You can use the pull hotlink protection key if you configure it when accessing Tencent Cloud LVB.

#### 2. Set player parameters

The parameter "type" of startPlay needs to be set to **PLAY_TYPE_LIVE_RTMP_ACC** added in version 1.8.2.

Example on how to use the accelerated pull API

```
String playUrl = "rtmp://8888.liveplay.myqcloud.com/live/8888_test?bizid=8888&txSecret=xxxx&txTime=xxx"; //The accelerated pull URL must be configured with hotlink protection key
TXLivePlayConfig playConfig = new TXLivePlayConfig();
mLivePlayer = new TXLivePlayer(context);
mLivePlayer.setConfig(playConfig);
mLivePlayer.setPlayListener(listener);
mLivePlayer.setPlayerView(mVideoView);
mLivePlayer.startPlay(playUrl, TXLivePlayer.PLAY_TYPE_LIVE_RTMP_ACC); //Start playback. The parameter "type" must be set to PLAY_TYPE_LIVE_RTMP_ACC
```


Notes:

The accelerated linkage cannot be used to play videos by viewers. Since the accelerated linkage uses the bandwidth of core node whose cost is several times higher than that of ordinary CDN bandwidth, it is only applicable for the real-time audio and video linkages among VJs. Meanwhile, Tencent Cloud sets a limit on the number of linkages of each stream watched using accelerated pull API. Currently, a maximum of 5 linkages is supported.

### Step 3: Launch stream mixing

Video stream mixing is aimed to place the video image(s) of one or more (three at most) secondary VJs on top of the video stream (including audio) of primary VJ, so that viewers can watch the video image(s) of secondary VJ(s). Tencent Video Cloud provides stream mixing feature by offering common API externally, which enables you to start or end a stream mixing process by calling stream mixing CGI at any time. You can also customize the method for stream mixing, that is, specify the relative location of secondary screen to primary screen.

Next, we will introduce how to use stream mixing CGI:

#### 1. Send a request for the this CGI using HTTP protocol

```
http://fcgi.video.qcloud.com/common_access
```


#### 2. Pass the authentication parameter using GET method

```
http://fcgi.video.qcloud.com/common_access?cmd=appid&interface=Mix_StreamV2&t=t&sign=sign
```


- **cmd**: Enter LVB APPID, which is used for differentiating the identity of different customers
- **interface**: Always entered with Mix_StreamV2
- **t (expiration time)**: UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT). This field indicates the expiration time of request. Please add 60 seconds of offset to the current time (in sec)
- **sign (security signature)**: sign = MD5(key + t), that is, to compute the MD5 value by concatenating the strings of the encryption key and t. The encryption key here is the API authentication key you set in Tencent Cloud LVB [Console](https://console.cloud.tencent.com/live/livecodemanage)

Example on how to calculate security signature **sign** 

```
key = "40328529ca4381a80c6ecf2e6aa57438"                    //API authentication key 
t = 1490858347                                              //t (expiration time)
key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //Concatenate the strings of the key and t
sign = MD5 (key + t) = "7f29ed83c61b77de1b0d66936fd4fd44"   //Compute the MD5 value for concatenated strings
```


#### 3. Pass stream mixing parameter using POST method

Stream mixing parameter is a string with JSON format, which is used to specify the video streams to be mixed and the method of stream mixing, as shown in the example below

```
{
    "timestamp":int(time.time()),           # UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT)
    "eventId":int(time.time()),             # Stream mixing event ID. Use the time stamp at the backend
    "interface":
    {
        "interfaceName":"Mix_StreamV2",	    # Fixed value: "Mix_StreamV2"
        "para":
        {
            "app_id": appid,                # Enter LVB APPID
            "interface": "mix_streamv2.start_mix_stream_advanced",  # Fixed value"mix_streamv2.start_mix_stream_advanced"
            "mix_stream_session_id" : "3891_denny1",                # Enter steam ID of primary VJ
            "output_stream_id": "3891_denny1",                      # Enter steam ID of primary VJ
            "input_stream_list":
            [
                # Primary VJ: Background image
                {
                    "input_stream_id":"3891_denny1",    # Steam ID
                    "layout_params":
                    {   
                        "image_layer": 1                # Image layer ID: Primary VJ: 1; Secondary VJ: 2, 3, 4 in sequence
                    }   
                },
                # Secondary VJ 1
                {
                    "input_stream_id":"3891_denny2",    # Steam ID
                    "layout_params":
                    {   
                        "image_layer": 2,               # Image layer ID
                        "image_width": 160,             # Secondary VJ image width
                        "image_height": 240,            # Secondary VJ image height
                        "location_x": 380,              # x offset: Lateral offset from the top left corner of primary VJ's background image
                        "location_y": 630               # y offset: Vertical offset from the top left corner of primary VJ's background image
                    }   
                 },
                # Secondary VJ 2
                 {
                     "input_stream_id":"3891_denny3",
                     "layout_params":
                     {
                         "image_layer": 3,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 390
                     }
                 },
                # Secondary VJ 3
                 {
                     "input_stream_id":"3891_denny4",
                     "layout_params":
                     {
                         "image_layer": 4,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 150
                     }
                 }
            ]
        }
    }
}
```


Detailed description of stream mixing parameters

- For the above stream mixing parameters, fields starting with # are annotations with python format;
- Fileds timestamp and eventId are specified with current time (in sec);
- Fileds mix_stream_session_id and output_stream_id are entered with stream ID of primary VJ;
- Field input_stream_list is an array, containing the information of video streams to be mixed. This array must contain primary VJ's video streams with the number limited to four streams, because only 4 video streams are allowed to be mixed at the backend;
- Field layout_params is used to configure the video stream layout parameter. The image of primary VJ is displayed in full screen view by default. You only need to enter 1 in field image_layer, and other fields are not required. image_layer is image layer ID. For secondary VJs, you can enter 2, 3 or 4 in sequence;
- Fields image_width, image_height, location_x and location_y are used to define the relative location of secondary screen to primary screen. Please note that, the top and bottom corners of secondary screen must reside within the primary screen, that is, the value range of location_x is from 0 to the width of primary screen; the value range of location_y is from 0 to the height of big screen; the combined values of location_x + image_width cannot exceed the width of primary screen; the combined values of location_y + image_height cannot exceed the height of primary screen;


#### 4. A string with JSON format is returned by CGI as follows:

```
{"code":0, "message":"Success!", "timestamp":1490079362}
```
    

- **code**: Error code; 0: Successful; other values: Failed.
- **message**: Error description information
- **timestamp**: Time stamp. The value is the same as timestamp in stream mixing parameter


Other notes about enabling video stream mixing

- Stream mixing CGI does not show when to start or end a mixing process. "Whether to perform stream mixing" and "the number of streams to be mixed" depend on the number of video streams in stream parameter input_stream_list array. If the number of video streams is larger than 1, the stream mixing process will start, and if there is only one video stream of primary VJ, the stream mixing process will end;
- It is recommended to generate the authentication parameter at your APP's backend server, because in consideration of confidentiality, API authentication key cannot be stored in frontend APP. We recommend you to generate the stream mixing parameter at the primary VJ side, because only primary VJ knows "whether a joint broadcasting session starts (whether to enable stream mixing)" and "which secondary VJ(s) will join a broadcasting session (which video streams need to be mixed)". The stream mixing CGI request can be initiated either from backend server (you need to send the stream mixing parameter to backend to send the stream mixing request), or at primary VJ side (you need to request for the authentication parameter from backend);
- Before starting a stream mixing process, you need to ensure that the push of primary VJ and secondary VJ is successful, that is, you must call the stream mixing CGI after receiving push success event PUSH_EVT_PUSH_BEGIN. Otherwise, the call will fail, and the field "code" in CGI response packet is not 0.
- When a failure message is returned if you call the stream mixing CGI after receiving the event PUSH_EVT_PUSH_BEGIN, you can use retry policy. It is recommended to retry up to five times, with 2 seconds between each attempt. The reason for this is because PUSH_EVT_PUSH_BEGIN event only means SDK has successfully sent the first video key frame to the server, but the lag synchronization of stream status occurs at the video cloud backend.


### How is upgraded joint broadcasting solution compatible with the old one

If you interface with the upgraded joint broadcasting solution, there is no problem of incompatibility with the old solution, and you can ignore the following section.

If you interfaced with the old joint broadcasting solution before, please solve the problem of incompatibility with the old solution using the following method.

The reason why upgraded and old joint broadcasting solutions are incompatible is that in upgraded solution, primary VJ and secondary VJ do not need to add joint broadcasting parameter after the push URL during push, which leads to two compatibility problems:

#### Problem 1
If primary VJ uses the new version, while secondary VJ uses the old one, the secondary VJ cannot pull the low-latency stream of primary VJ using the accelerated pull API, so they cannot start a video session;

**Solution**: In new version, when primary VJ starts the push process, the parameter "&mix=session_id:xxxx" should be added after the push URL. Please make sure that the value of session_id is the same with that of session_id in joint broadcasting parameter of secondary VJ who uses the old version.

#### Problem 2
If primary VJ uses the old version, while secondary VJ uses the new one, the primary VJ cannot pull the low-latency stream of secondary VJ using the accelerated pull API, so they cannot start a video session. In addition, the video stream mixing cannot be enabled at the backend, so viewers cannot see the secondary VJ's screen;

**Solution**: In new version, when secondary VJ starts the push process, the joint broadcasting parameter "mix=layer:s;session_id:xxxx;t_id:1" should be added after the push URL in a way as usual. Please make sure that the value of session_id is the same with that of session_id in joint broadcasting parameter of primary VJ who uses the old version.
