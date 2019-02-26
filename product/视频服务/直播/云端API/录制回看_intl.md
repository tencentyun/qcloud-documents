
 ## Feature Description
Recording & Replay means recording user's entire LVB and replaying it as VOD as shown below:
![](//mccdn.qcloud.com/static/img/a8240c996be9eab19d5dc40b9e3df779/image.png)
The number of VJs is often small at the early stage of introduction of an application. Adding recording & replay in the LVB list can give more information on the application's viewer end. Even if the number of VJs grows significantly with the increasing popularity of an App, the accumulation of good LVB content is still necessary. In addition to name, photos and other personal information of a VJ, replays of historical LVBs is also an indispensable part of a VJ's profile.

## Activate Service
Recording & Replay is built on the backend clusters of Tencent Cloud's **VOD service**. To use this feature, you need to [Activate VOD Service](http://console.cloud.tencent.com/video) first on Tencent Cloud console.

After the VOD service is enabled, you can find the new recorded files in [Video Management](http://console.cloud.tencent.com/video/videolist) on the VOD console.

## Enabling Recording
Tencent Cloud supports recording the entire LVB. There are two ways of enabling recording:

- **Method 1: Enable globally**
You can enable or disable recording for all LVB streams on [LVB Console](https://console.cloud.tencent.com/live), as shown below:
![](//mc.qcloudimg.com/static/img/fd4a3e35fdb486d9d9053fe7f29760a8/image.png)

- **Method 2: Enable individually**
When the recording of all LVB streams is disabled, you can still enable recording for a very important video stream as follows: add the **&record=flv** or **&record=mp4** parameter to the end of the push URL. See the following figure:
```
rtmp://2121.livepush.myqcloud.com/live/2121_15919131751?txSecret=aaa&txTime=bbb&record=flv
```

## File Generation
- **Method 1: Message notification**
You can use Tencent Cloud **[Event Notification Service](https://cloud.tencent.com/doc/api/258/5957)**: Register a **callback URL** for your server on Tencent Cloud which will notify you of the generation of a new recorded file using this URL.

 The following is a typical notification message, which indicates: a new FLV recorded file with ID 9192487266581821586 has been generated, and the playback URL is: "http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv".
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

- **Method 2: Active query**
You can check whether any new recorded file is generated on a regular basis using Tencent Cloud's query API (**[Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960)**). However, this method is not recommended for frequent use due to its unsatisfactory timeliness and reliability since it has a slow response in case of a query for a large number of channels and cannot be called at a high frequency (only suitable for the channels that have just finished).

## Video Playing
After obtaining the recording file, your server can generate a play URL, which the application obtains and delivers to the VOD playing module of the RTMP SDK. Then, the recording file is available for playback:
- [Documentation for iOS Platform](https://cloud.tencent.com/doc/api/258/4738)
- [Documentation for Android Platform](https://cloud.tencent.com/doc/api/258/4739)
- [Documentation for Web Platform](https://cloud.tencent.com/doc/api/258/5706)
