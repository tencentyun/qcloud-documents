## Overview
Recording & Replay means record user's entire LVB session and then replay it as VOD.

The number of VJs is often small at the early stage of introduction of an App. Adding recording & replay in the LVB list can give more information on the App's viewer end.

Even if the number of VJs grows significantly with the increasing popularity of an App, the accumulation of good LVB content is still necessary. In addition to name, photos and other personal information of VJ, replays of historical LVBs is also an indispensable part of VJ's profiles.

![](//mc.qcloudimg.com/static/img/504f32f7112d7dd9ab6c4ec10cb20099/image.png)

## Enable Recording
Recording & Replay is built on Tencent Cloud's **VOD service**. To use this feature, you need to [Activate VOD Service](http://console.cloud.tencent.com/video) on Tencent Cloud console. After the service is enabled, you can find the new recorded files in [Video Management](http://console.cloud.tencent.com/video/videolist) on VOD console.

How to enable recording? There are two methods:

### 1. Enable recording globally
You can enable or disable recording for all LVB streams on ["LVB Console" -> "Access Management" -> "LVB Code Access" -> "Access Configuration"](https://console.cloud.tencent.com/live/livecodemanage), as shown below:

![](//mc.qcloudimg.com/static/img/302dd405148cb9ccd016c3deafc6027d/image.png)

### 2. Specify a room for recording
When the recording of all LVB streams is disabled, you can enable recording for important video streams individually by appending **&record=mp4**, **&record=hls** or **&record=mp4|hls** to the push URL.
```
rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb&record=mp4&record_interval=5400
```
Notes:
- The video wrapper formats supported by recording feature are mp4, hls and flv. For more information about the VOD formats, see [DOC](https://www.cloud.tencent.com/document/product/454/7937#3.-.E5.B8.B8.E8.A7.81.E7.9A.84.E7.82.B9.E6.92.AD.E5.8D.8F.E8.AE.AE.E6.9C.89.E5.93.AA.E4.BA.9B.EF.BC.9F).

- record=mp4|hls|flv delimiter-based format is used to specify multiple formats in which the video is recorded at a time (mobile browsers only support playback of MP4 and HLS videos).

- Changing resolution or switching between landscape/portrait modes during LVB is not supported for mp4 videos.
  
- If the specified recording format is flv or mp4, you can specify the recording length of a single video fragment using the parameter record_interval (in sec). The maximum length is 90 minutes (i.e. 5,400 seconds). If no value is specified, the default length is 30 minutes (i.e. 1,800 seconds).
 
- HLS (m3u8) file is on a fragmentation basis in essence, so you can always get a single m3u8 file as long as no push interruption occurs during LVB. But in case of a push interruption during LVB, fragmentation will occur in the process of recording (you will get multiple m3u3 files). One of the common problems would be switching of App to background. To solve this problem, you're recommended to use background push solution.
 
## Getting File
When a new recorded video file is generated, a playback URL will be generated. You can process it based on your business needs. In Mini LVB, we directly put together the recording file URL and the room list to fill in the gap of insufficient online VJs.

You can implement many extensions based on your business scenarios. For example, you can add the URL to a VJ's personal information as a historical program for that VJ; or put it in the replay list to recommend a high-quality video to your App users after manual filtering.

How to get the URL of the recorded file? in the following two ways:

### 1. Listen to notification passively
You can use Tencent Cloud's **[Event Notification Service](https://www.cloud.tencent.com/doc/api/258/5957)**: Register a **callback URL** for your server on Tencent Cloud, which will be used to let Tencent Cloud notify you of the generation of a new recorded file.

![](//mc.qcloudimg.com/static/img/b50c901fb4d529daf3405e78bc69908d/image.png)

The following is a typical notification message, which indicates: a new FLV recorded file with ID 9192487266581821586 has been generated, and the playback URL is:`http://200025724.vod.myqcloud.com/200025724_ac92b7y81a22c4a3e937c9e61c2624af7.f0.flv`.
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

### 2. Query files actively
You can check if any new recorded file is generated on a regular basis using Tencent Cloud's query API (**[Live_Tape_GetFilelist](https://www.cloud.tencent.com/doc/api/258/5960)**). However, this method is not recommended for frequent use due to its unsatisfactory real-timeness and reliability since it has a slow response in case of a query for a large number of channels and cannot be called at a high frequency (only suitable for the channels that have just finished).

## FAQs
### 1. How does LVB recording work?

![](//mc.qcloudimg.com/static/img/cbb2aae6b5e767db1d30cb51d147948d/image.png)

When you enable the recording for an LVB stream, the audio data will be bypassed to the recording system. Every frame pushed from VJ's mobile phone will be written into the recording file by the recording system.

If an LVB push is interrupted, the access layer will immediately send a notification to the recording server to implement the file that is being written, store it into the VOD system and generate an index, so that you can see this new recording file in the VOD system. Meanwhile, if you have configured a recording event notification, the recording system will notify the server you configured earlier of such information as **index ID** and **online playback URL** of the file.

However, an error will occur in the processes of transferring and processing of a large file on the cloud. To ensure success, the maximum recording length of a file is 90 minutes, and you can specify a shorter fragment using parameter record_interval.


### 2. How many recording files are generated in an LVB process?
- If the duration of an LVB is too short (for example, shorter than 1 second), there may be no file recorded.

- If the duration of an LVB is not long (shorter than record_interval), and the push is not interrupted during LVB, there is only one file.

- If the duration of an LVB is very long (longer than record_interval), the video will be fragmented based on the length of time specified in record_interval, to avoid the time uncertainty of the flow of the file with a longer duration in a distributed system.

- If the push is interrupted during an LVB (SDK will re-push later), a new fragment will be generated every time the interruption occurs.

### 3. How do I know which files belong to a certain LVB?
To be precise, as PAAS, Tencent Cloud does not know how to define your LVB. If one of your LVBs lasted for 20 minutes, during which a push interruption caused by network switching occurred, and the LVB was stopped and restarted once manually. Should we calculate the number of LVBs as one or three?

For normal MLVB scenarios, the period between the following two interfaces is defined as one LVB session:
![](//mc.qcloudimg.com/static/img/1df26077a3e59479b658aef63ab7f83d/image.png)

Therefore, the time information sent from App client is very important. If you wish to define that the files recorded during this period belong to this LVB, you just need to retrieve received recording notification using LVB code and time information (each recording notification event will come with information such as stream_id, start_time and end_time).


### 4. How to stitch fragments?
Currently, Tencent Cloud allows you to use cloud API to stitch video fragments. For more information about this API, see [Video Stitching](/document/product/266/7821).
