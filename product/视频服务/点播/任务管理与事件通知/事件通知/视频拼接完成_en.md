## Event Name
ConcatComplete

## Event Description
If an APP is configured with event notification, after a video stitching task is completed, VOD backend will notify the APP backend of the event.

For details about the way in which the APP backend receives the event notification, refer to [Introduction to Server Event Notification](/document/product/266/7829).

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Callback type, which is always ConcatComplete |
| data | Object | Specific callback data |
| data.vodTaskId | String | ID of stitching task  |
| data.fileInfo | Array | Information on the outputted stitched video file |

Each element in data.fileInfo array is an Object, and each parameter has the following meaning:

| Name | Type | Description |
|---------|---------|---------|
| fileType | String | Type of the stitched file |
| status | Integer | Error message for this type of file, 0: Succeeded; other values: Failed. Refer to Error Code Description for details |
| message | String | Error message |
| fileId | String | ID of the stitched file |
| fileUrl | String | URL of the stitched file  |

## Example

- For [HTTP Callback](/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [Reliable Notification Based on Message Queue](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of [PullEvent API](/document/product/266/7818).

### Example: Video stitching succeeded

```javascript
{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "vodTaskId": "Concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": 0,
                "message": "",
                "fileId": "14508071098244931831",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8"
            },
            {
                "fileType": "mp4",
                "status": 0,
                "message": "",
                "fileId": "14508071098244929440",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
            }
        ]
    }
}
```

### Example: Video stitching failed

```javascript
{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "status": -1,
        "message": "",
        "vodTaskId": "Concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": -43001,
                "message": ""
            },
            {
                "fileType": "mp4",
                "status": -43001,
                "message": ""
            }
        ]
    }
}
```

### Error Code Description

The status field in the event notification packet indicates the result of the video processing task. For details, refer to [Error Code Description Regarding Video Processing Operations](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).
