## Enabling Recording
Recording & Replay is built on Tencent Cloud's **VOD service**. To use this feature, you need to [Activate VOD Service](http://console.cloud.tencent.com/video) first on Tencent Cloud console. After the VOD service is enabled, you can find the new recorded files in [Video Management](http://console.cloud.tencent.com/video/videolist) on the VOD console.

Recording can be enabled using the following two methods:
### 1. Enable recording globally
You can enable or disable recording for all LVB streams on **LVB Management [Console](https://console.cloud.tencent.com/live/livestat)** -> **Access Management** -> [**LVB Code Access (recommended)**](https://console.cloud.tencent.com/live/livecodemanage), as shown below:
![](//mc.qcloudimg.com/static/img/19b9dbfbf11a6f9438ddbdb37bc67ac4/image.png)

### 2. Enable recording for certain rooms
When the recording of all LVB streams is disabled, you can enable recording for important video streams individually by appending **&record=mp4**, **&record=hls** or **&record=mp4|hls** to the push URL. For example:
```
rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb&record=mp4&record_interval=5400
```
Notes:
- The video wrapper formats supported by the recording feature are MP4, HLS and FLV. For more information on the difference of VOD formats, please see [DOC](https://cloud.tencent.com/document/product/454/7937#3.-.E5.B8.B8.E8.A7.81.E7.9A.84.E7.82.B9.E6.92.AD.E5.8D.8F.E8.AE.AE.E6.9C.89.E5.93.AA.E4.BA.9B.EF.BC.9F).
- record=mp4|hls|flv delimiter-based format is used to specify multiple formats in which the video is recorded at a time (mobile browsers only support playback of MP4 and HLS videos).
- Changing resolution or switching between landscape/portrait modes during LVB is not supported for MP4 videos.
- If the specified recording format is FLV or MP4, you can specify the recording length for a single video fragment using parameter record_interval (in seconds). The maximum length is 90 minutes (i.e. 5,400 seconds). If no value is specified, the default is 30 minutes (i.e. 1,800 seconds).
- HLS (m3u8) file is on a fragmentation basis in essence, so you can always get a single m3u8 file as long as no push interruption occurs during LVB. But in case of a push interruption during LVB, fragmentation will occur in the process of recording (you will get multiple m3u8 files). One of the common problems would be switching of App to the backend. To solve this problem, you are recommended to use backend push solution.
 
## Getting File
When a new recorded video file is generated, a playback URL will be generated. You can process it based on your business needs. In Mini LVB, we directly put together the recorded file URL and the LVB room list to fill in the gap of insufficient online VJs. You can implement many extensions based on your business scenarios. For example, you can add the URL to a VJ's personal information as a historical program for that VJ, or put it in the replay list to recommend a high-quality video to your App users after manual filtering.

Playback URLs can be obtained using the following two methods:

### 1. Listen to notification passively
You can use Tencent Cloud's [Event Notification Service](https://cloud.tencent.com/doc/api/258/5957): Register a callback URL for your server on Tencent Cloud, which will notify you of the generation of any new recorded file.
![](//mc.qcloudimg.com/static/img/b50c901fb4d529daf3405e78bc69908d/image.png)
The following is a typical notification message, which indicates a new FLV recorded file with ID 9192487266581821586 has been generated, and the playback URL is: `http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv`.
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
You can check if any new recorded file is generated using Tencent Cloud's query API ([Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960)) on a regular basis. However, this method is not recommended for frequent use due to its unsatisfactory real-timeness and reliability since it has a slow response in case of a query for a large number of channels and cannot be called at a high frequency (only suitable for the channels that have just finished).
