## Event Name
ClipComplete

## Event Description
If an app is configured with event notification, after a video clipping task is completed, VOD backend will notify the app backend of the event.

For details about the way in which the app backend receives the event notification, refer to [introduction to server event notification](https://cloud.tencent.com/document/product/266/7829).

### Parameter Description
| Parameter | Type | Description |
|---------|---------|----------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Callback type, which is always ClipComplete |
| data | Object | Specific callback data |
| data.vodTaskId | String | Clipping task ID  |
| data.srcFileId | String | The file ID of original file of clipping task |
| data.fileInfo | Object | Information on the output clipped video file |

Each element of data.fileInfo has the following meaning:

| Parameter | Type | Description |
|---------|---------|---------|
| fileType | String | Type of the clipped file |
| status | Integer | Error message for this type of file. 0: successful; other values: failed. For more information, please see Error Codes |
| message | String | Error message |
| fileId | String | ID of the clipped file |
| fileUrl | String | URL of the clipped file  |

## Example

- For [HTTP callback](https://cloud.tencent.com/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [reliable notification based on message queue](https://cloud.tencent.com/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of API [PullEvent](https://cloud.tencent.com/document/product/266/7818).

### Example: Video clipping succeeded

```javascript
{
    "version": "4.0",
    "eventType": "ClipComplete",
    "data": {
        "vodTaskId": "clipVideo-0a78cf44c4285026a4c",
        "srcFileId": "16092504232103571364",
        "fileInfo": {
            "fileType": "mp4",
            "status": 0,
            "message": "",
            "fileId": "14508071098244929440",
            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
        }
    }
}
```

### Example: Video clipping failed

```javascript
{
    "version": "4.0",
    "eventType": "ClipComplete",
    "data": {
        "vodTaskId": "clipVideo-0a78cf44c4285026a4c",
        "srcFileId": "16092504232103571364",
        "fileInfo": {
            "status": -43001,
            "message": ""
        }
    }
}
```

### Error Codes

The status field in the event notification packet indicates the result of the video processing task. For more information, please see [error codes regarding video processing operations](https://cloud.tencent.com/document/product/266/7783#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E6.93.8D.E4.BD.9C.E9.94.99.E8.AF.AF.E7.A0.81.E8.AF.B4.E6.98.8E).
