## Interfacing Guide

This session describes pure push and pure playback on the mobile side, which are implemented through Tencent Cloud RTMP SDK. The business logics, such as messages, on-screen comments, giving a like and floating stars, will be discussed later.

1. First generate one pair of push and playback URLs on [LVB Console](https://www.qcloud.com/doc/api/258/6445) to test push and LVB watching.
2. Interface with the RTMP pushing feature. The process usually takes 0.5 to 1 day.
3. Interface with the Live online LVB feature. The process usually takes 0.5 to 1 day.
4. Interface with the VOD feature (depending on the requirement): First [Activate VOD Service](https://www.qcloud.com/doc/api/258/6208#2.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.82.B9.E6.92.AD.E6.9C.8D.E5.8A.A1), and then add &record=flv (or mp4) at the end of the push URL to record the pushed video. After that, the video can be found on the [VOD Console](http://console.qcloud.com/video/videolist).
5. Next, change the test URL to the formal push/pull URL after interfacing of [LVB Backend](https://www.qcloud.com/doc/api/258/6447) is completed.

## RTMP Push
RTMP push means that the SDK completes audio and video collection and coding, and then the standard RTMP is used to push the audio and video streams to the specified push URL.

- **Camera LVB ([iOS Platform](https://www.qcloud.com/doc/product/454/6946) & [Android Platform](https://www.qcloud.com/doc/product/454/6947))**
Camera LVB means that the SDK collects the camera images and microphone sound, and then completes the coding and push work. The iOS 7, Android 4.2 and OSs of higher versions are supported.

- *Screencap LVB ([iOS Platform](https://www.qcloud.com/doc/product/454/6948) & [Android Platform](https://www.qcloud.com/doc/product/454/6949))**
Screencap LVB means that the SDK collects the mobile phone screen images and microphone sound, and then completes the coding and push work. The iOS 10, Android 5.0 and OSs of higher versions are supported.

- **Advanced Application ([References](https://www.qcloud.com/doc/product/454/6955))**
  + Customers who want to know how RTMP SDK works internally
  + Customer who have experience in audio and video development and needs to customize parameters in line with their scenarios
  + Customers who only use RTMP SDK to push streams

## Online LVB (LIVE)
A video source being pushed in real time is watched during online LVB. In comparison with the VOD for which the video is pre-loaded to a local place several minutes in advance and then played step by step, several more difficult problems need to be fixed when it comes to online LVB:

- **Low Delay**
For online LVB, it is necessary to ensure that the delay from the VJ to the audience is not too high, for example, the minimum delay of the RTMP and FLV protocols must be limited to 2-3 seconds. This means that the idea of "large buffer & secure broadcast" does not work anymore.

- **Less Stutter**
Since the delay cannot be too high, video buffer cannot be too frequent. As a result, the stutter problem cannot be offset by large buffers. The increasingly high delay due to stutter must also be fixed.

- **Instant Broadcasting**
The video can be watched immediately when a Live room is opened. This is the basic requirement for a qualified LVB App. Therefore, if a player does not support instant broadcasting, it's definitely a poor one.

Now, the performance of the RTMP SDK of Tencent Cloud in the above three aspects has been recognized by customers, and the interfacing work costs little and usually takes less than 1 day.

- [References for iOS Platform](https://www.qcloud.com/doc/product/454/6950) 
- [References for Android platform](https://www.qcloud.com/doc/product/454/6952) 

## Video on Demand (VOD)
VOD is largely different from Online LVB in terms of the way it works and the approach to optimize, but is basically the same as Online LVB in terms of API. Pay attention to the following two differences:
- The event notifications of VOD include the PLAY_EVT_PLAY_PROGRESS progress notification, which is not supported in Online LVB.
- For VOD and LVB, the video type must not be wrongly selected when startPlay is called. Fast motions will be presented if the LVB player is used to play VOD video.

The VOD player of RTMP SDK is designed for recording playback demands of LVB customers, so we will not pursue completeness in format support. We only provide support to three VOD formats: FLV (supporting resolution switching and landscape/portrait screen switching), HLS, and MP4.

If the LVB video has been received, the VOD feature can be implemented anytime:
- [References for iOS Platform](https://www.qcloud.com/doc/product/454/6953) 
- [References for Android platform](https://www.qcloud.com/doc/product/454/6954) 

## Source Code Reference
Set out below is the position of Mini LVB source codes interfaced with RTMP SDK:


### iOS Platform

| Type | Feature | Description |
|---------|---------|---------|
| TCPusherMgr | The logic layer code of push module | It performs protocol communication with the service server to acquire URL.  |
| TCPushController | The main controller of push module | It accommodates the rendering view, logic view and push related logic; meanwhile, it also receives the event notification of SDK layer.  |
| TCPushDecorateView | The interface view of push module | It presents the message list, bullet screen animation, viewer list, beauty, whitening and other UIs, wherein the logic interaction with the SDK needs to be processed by the main controller.  |
| TCPlayerMgr | The logic layer code of playback module | It performs protocol communication with the service server to acquire URL.  |
| TCPlayController | The main controller of playback module | It accommodates the rendering view, logic view and playback related logic; meanwhile, it also receives the event notification of SDK layer.  |
| TCPlayDecorateView | The interface view of playback module | It presents the message list, bullet screen animation, viewer list, and other UIs, wherein the logic interaction with the SDK needs to be processed by the main controller.  |

### Android Platform

| Type | Feature | Description |
|---------|---------|---------|
| TCPusherMgr.java | LVB management class | It communicates with the backend, pulls the LVB URL, and notifies the backend to exit LVB. |
| TCLivePublisherActivity.java | Push module activity | All the push management, message management and animation effects are implemented in this class. |
| TCPlayerMgr.java | Playback management class | It communicates with the backend, and notifies the backend to enter the room, exit from the room, and use the "giving a like" feature |
| TCLivePlayerActivity.java | Playback module activity |Including VOD and LVB. All the playback management, message management and animation effects are implemented in this class. |



