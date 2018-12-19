## Event Name
NewFileUpload

## Event Description
If an APP is configured with event notification, after a video upload task is completed, VOD backend will notify the APP backend of the event.

For details about the way in which the APP backend receives the event notification, refer to [Introduction to Server Event Notification](/document/product/266/7829).

### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| version | String | Callback version number, which is always 4.0 |
| eventType | String | Callback type, which is always NewFileUpload |
| data.fileId | String | Unique ID obtained after a stitching request is initiated |
| data.fileUrl | String | URL obtained after video upload is completed  |
| data.transcodeTaskId | String | If transcoding is initiated after the video is uploaded, the parameter is ID of the transcoding task |
| data.porncheckTaskId | String | If a porn detection is initiated after the video is uploaded, the parameter is ID of the porn detection task |

## Example

- For [HTTP Callback](/document/product/266/7829#http.E5.9B.9E.E8.B0.83), the following is the HTTP Post Body;
- For [Reliable Notification Based on Message Queue](/document/product/266/7829#.E5.9F.BA.E4.BA.8E.E6.B6.88.E6.81.AF.E9.98.9F.E5.88.97.E7.9A.84.E5.8F.AF.E9.9D.A0.E9.80.9A.E7.9F.A5), the following is the content of eventList.eventContent in the returned packet of [PullEvent API](/document/product/266/7818).

```javascript
{
    "version": "4.0",
    "eventType": "NewFileUpload",
    "data": {
        "fileId": "14508071098244959037",
        "fileUrl": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
        "transcodeTaskId": "transcode-0bee89b07a248e27c83fc3d5951213c1",
        "porncheckTaskId": "porncheck-f5ac8127b3b6b85cdc13f237c6005d80"
    }
}
```






