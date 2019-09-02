## Event Name
CreateSnapshotByTimeOffsetComplete

## Event Description
If an APP is configured with event notification, after a screenshot task by time offset is completed, VOD backend will notify the APP backend of the event.

For details about the way in which the APP backend receives the event notification, refer to [Introduction to Server Event Notification](/document/product/266/7829).

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Callback type, which is always CreateSnapshotByTimeOffsetComplete |
| data | Object | Specific callback data |
| data.vodTaskId | String | ID of task of capturing screenshot by time offset  |
| data.vodTaskId | String | File ID of screenshot captured by time offset  |
| data.definition | Integer | Screenshot specifications. Refer to [Specifications for Screenshots Captured by Time Offset](/document/product/266/8097) |
| data.picInfo | Array | Information on the outputted screenshot captured by time offset |

Each element in data.picInfo array is an Object, and each parameter has the following meaning:

| Name | Type | Description |
|---------|---------|---------|
| timeOffset | Integer | Time offset of screenshot, in millisecond |
| url | String | URL of screenshot file  |
| status | Integer | Error code, 0: Succeeded, other values: Failed |

## Example

- For [HTTP Callback](/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [Reliable Notification Based on Message Queue](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of [PullEvent API](/document/product/266/7818).

### Example: Task of capturing video screenshot by time offset succeeded

```javascript
{
    "version": "4.0",
    "eventType": "CreateSnapshotByTimeOffsetComplete",
    "data": {
        "vodTaskId": "CreateSnapshotByTimeOffset-1edb7eb88a599d05abe451cfc541cfbd",
        "fileId": "14508071098244929440",
        "definition": 10,
        "picInfo": [
            {
                "status": 0,
                "timeOffset": 3123213,
                "url": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/xx1.png"
            },
            {
                "status": 0,
                "timeOffset": 3123123,
                "url": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/xx2.png"
            }
        ]
    }
}
```

### Example: Task of capturing video screenshot by time offset failed
```javascript
{
    "version": "4.0",
    "eventType": "CreateSnapshotByTimeOffsetComplete",
    "data": {
        "vodTaskId": "CreateSnapshotByTimeOffset-1edb7eb88a599d05abe451cfc541cfbd",
        "fileId": "9031868222841494656",
        "definition": 20,
        "picInfo": [
            {
                "status": -46204,
                "timeOffset": 1000000
            }
        ]
    }
}
```

### Error Code Description

The status field in the event notification packet indicates the result of the video processing task. For details, refer to [Error Code Description Regarding Video Processing Operations](/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).

