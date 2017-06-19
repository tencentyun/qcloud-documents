
## Overview
Recording & Replay means recording user's entire LVB and replaying it as VOD as shown below:
![](//mc.qcloudimg.com/static/img/504f32f7112d7dd9ab6c4ec10cb20099/image.png)
The number of VJs is often small at the early stage of introduction of an App. Adding recording & replay in the LVB list can give more information on the App to viewers. Even if the number of VJs grows significantly with the increasing popularity of an App, the accumulation of good LVB content is still necessary. In addition to name, photos and other personal information of VJ, replays of historical LVBs is also an indispensable part of VJ's profile.

## Interfacing Guide
## 1 Enable VOD service
Recording & Replay is built on the backend clusters of Tencent Cloud's **VOD service**. To use this feature, you need to [Activate VOD Service](http://console.qcloud.com/video) first on Tencent Cloud console.

After the VOD service is enabled, you can find the new recorded files in [Video Management](http://console.qcloud.com/video/videolist) on the VOD console.

### 2 Enable LVB recording
Tencent Cloud supports recording the entire LVB. There are two ways of enabling recording:

#### 2.1. Global enabling
You can enable or disable recording for all LVB streams on [LVB Console](https://console.qcloud.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/89c0a7e2b64527afae86e304635300b3/image.png)

This method has been used so long since Tencent Cloud's first version of LVB Code where global recording feature was available. Currently, only FLV format is supported. 

#### 2.2 Selective enabling
When the recording for all LVB streams is disabled, you can enable recording for important video streams individually by appending **&record=flv** or **&record=mp4** to the push URL.
```
rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb&record=flv&record_interval=5400
```
Notes:
 - Changing resolution or switching between landscape/portrait modes is not supported for MP4 videos.
 
 - For HLS (m3u8) format, a manual configuration of storage bucket is needed at our backend by the end of November. Please contact us for manual handling.
 
 - the specified recording format is FLV or MP4, you can specify the recording length for a single video fragment using parameter record_interval (in seconds). The maximum length is 90 minutes (i.e. 5,400 seconds). If no value is specified, the default is 30 minutes (i.e. 1,800 seconds).
 
 - HLS (m3u8) file is on a fragmentation basis in essence, so you can always get a single m3u8 file as long as no push interruption occurs during LVB. But in case of a push interruption during LVB, fragmentation will occur in the process of recording (you will get multiple m3u3 files). One of the common problems would be switching of App to the background. To solve this problem, you're recommended to use background push solution ([iOS](https://www.qcloud.com/doc/product/454/6946#step-8.3A-.E5.90.8E.E5.8F.B0.E6.8E.A8.E6.B5.81) & Android](https://www.qcloud.com/doc/product/454/6947)).
 
 - record_name can be used to specify the recorded file's name, but is not recommended unless in special cases to avoid a too long URL.
 
 - record=mp4|hls|flv delimiter-based format is used to specify multiple formats in which the video is recorded at a time.

### 3. Implementation of recoded files
When a new recorded video file is generated, a playback URL will be generated. You can process it based on your business needs. In Mini LVB, we directly put together the recorded file URL and the LVB room list to fill in the gap of insufficient online VJs.

You can implement many extensions based on your business scenarios. For example, you can add the URL to a VJ's personal information as a historical program for that VJ, or put it in the replay list to recommend a high-quality video to your App users after manual filtering.

You can get the URL of the recorded file by the following two ways:

#### 3.1 Notification message
You can use Tencent Cloud's **[Event Notification Service](https://www.qcloud.com/doc/api/258/5957)**: Register a **callback URL** for your server on Tencent Cloud, which will notify you of the generation of a new recorded file via this URL.

![](//mc.qcloudimg.com/static/img/b50c901fb4d529daf3405e78bc69908d/image.png)

The following is a typical notification message, which indicates: a new FLV recorded file with ID 9192487266581821586 has been generated, and the playback URL is:"http://200025724.vod.myqcloud.com/200025724_ac92b7y81a22c4a3e937c9e61c2624af7.f0.flv".
```json
{
    "channel_id": "2121_15919131751",
    "end_time": 1473125627,
    "event_type": 100,
    "file_format": "flv",
    "file_id": "9192487266581821586",
    "file_size": 9749353,
    "sign": "fef79a097458ed80b5f5574cbc13e1fd",
    "start_time": 1473135647,
    "stream_id": "2121_15919131751",
    "t": 1473126233,
    "video_id": "200025724_ac92b781a22c4a3e937c9e61c2624af7",
    "video_url": "http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv"
}
```

#### 3.2. Active query
You can check if any new recorded file is generated on a regular basis using Tencent Cloud's query API (**[Live_Tape_GetFilelist](https://www.qcloud.com/doc/api/258/5960)**). However, this method is not recommended for frequent use due to its unsatisfactory real-timeness and reliability since it has a slow response in case of a query for a large number of channels and cannot be called at a high frequency (only suitable for the channels that have just finished). 

### 4 Playback on mobile devices
After obtaining the recorded file, your server can generate a playback URL, which the App obtains and delivers to the VOD playback module of the RTMP SDK. Then, the recorded file is available for playback:
- [Documentation for iOS Platform](https://www.qcloud.com/doc/api/258/4738)
- [Documentation for Android Platform](https://www.qcloud.com/doc/api/258/4739)
- [Documentation for Web Platform](https://www.qcloud.com/doc/api/258/5706)
