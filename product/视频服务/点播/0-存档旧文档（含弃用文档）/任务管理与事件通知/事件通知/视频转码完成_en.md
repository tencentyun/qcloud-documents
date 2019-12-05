## Event Name
TranscodeComplete

## Event Description
If an APP is configured with event notification, after a video transcoding task is completed, VOD backend will notify the APP backend of the event.

For details about the way in which the APP backend receives the event notification, refer to [Introduction to Server Event Notification](/document/product/266/7829).

> Note:
> - During the whole transcoding process, videos of multiple specifications may be outputted, such as SD, HD, etc. Only when videos of all specifications are generated, the callback can be triggered.

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| version | String | Event notification version number, which is always 4.0 |
| eventType | String | Event type, which is always TranscodeComplete |
| data | Object | Specific callback data |
| data.status | Integer | Error code, 0: Succeeded; other values: Failed |
| data.message | String |　Error message  |
| data.fileId | String | ID of the transcoded file  |
| data.vodTaskId | String | ID of transcoding task  |

## Example

- For [HTTP Callback](/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [Reliable Notification Based on Message Queue](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of [PullEvent API](/document/product/266/7818).

### Example: Transcoding succeeded

```javascript
{
    "version": "4.0",
    "eventType": "TranscodeComplete",
    "data": {
        "status": 0,
        "message": "",
        "vodTaskId": "Transcode-1edb7eb88a599d05abe451cfc541cfbd",
        "fileId": "14508071098244931831",
        "fileName": "13425173277_2015-09-06-19-06-11_2015-09-06-19-16-11",
        "duration": 599,
        "coverUrl": "http://p.qpic.cn/videoyun/0/1203_8a5015084d4f47cd9a0bc5ecfe78aecb_1/640",
        "playSet": [
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f0.mp4",
                "definition": 0,
                "vbitrate": 246000,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f10.mp4",
                "definition": 10,
                "vbitrate": 149193,
                "vheight": 240,
                "vwidth": 320
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f20.mp4",
                "definition": 20,
                "vbitrate": 297656,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f220.av.m3u8",
                "definition": 220,
                "vbitrate": 524288,
                "vheight": 480,
                "vwidth": 640
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f30.mp4",
                "definition": 30,
                "vbitrate": 899976,
                "vheight": 960,
                "vwidth": 1280
            },
            {
                "url": "http://vcloud1203.tc.qq.com/1203_8a5015084d4f47cd9a0bc5ecfe78aecb.f40.mp4",
                "definition": 40,
                "vbitrate": 1746652,
                "vheight": 1440,
                "vwidth": 1920
            }
        ]
    }
}
```

### Example: Transcoding failed

```javascript
{
    "version": "4.0",
    "eventType": "TranscodeComplete",
    "data": {
        "status": -43001,
        "message": "",
        "fileId": "14508071098244931831",
        "vodTaskId": "Transcode-1edb7eb88a599d05abe451cfc541cfbd"
    }
}
```

### Error Code Description

The status field in the event notification packet indicates the result of the video processing task. For details, refer to [Error Code Description Regarding Video Processing Operations](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).
