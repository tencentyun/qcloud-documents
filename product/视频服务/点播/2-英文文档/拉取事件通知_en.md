## API Name
PullEvent

## Feature Description
1. This API is used to get event notifications from the VOD server. For details, refer to [Server Event Notification](https://cloud.tencent.com/document/product/266/7829).
2. The API is a long Round Robin mode. That is, if there is any unconsumed event on the server, it will be returned to the requester immediately; If there isn't any unconsumed event on the server, the request will be suspended in the backend until a new event is generated ;
3. The API can suspend the request for up to 5 seconds. It is recommended that the requester set the timeout to 10 seconds;
4. If the server returns an event, the caller must call [ConfirmEvent](/document/product/266/7819) to confirm that the event notification has been processed. Otherwise, the event notification will be pulled again.

### Request Method

#### Request Domain
vod.api.qcloud.com

### Peak Calling Frequency
1,000 counts/min

#### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

#### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=PullEvent
&COMMON_PARAMS
```
#### API Response

#### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0:  Succeeded; other values:  Failed |
| message | String | Error message |
| eventList | Array | List of events returned by the server |
| eventList.msgHandle | String | Event handler, the caller must call ConfirmEvent to confirm that the message has been received |
| eventList.eventContent | Object | Specific event content, refer to [Introduction to Server Event Notification](/document/product/266/7829) |

#### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| 1000 | Invalid parameter  |
| 1001 | Internal error  |
| 2000 | Internal error  |

#### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "eventList": [  // Pull the list of server event notifications, which includes two event notifications
        {
            "msgHandle": "MsgHandle1",  // The handler of the first event notification
            "eventContent": { // The content of the first event notification
                "version": "4.0",
                "eventType": "NewFileUpload", // This field indicates that the type of the event notification is "Video Upload Completed"
                "data": {
                    "fileId": "14508071098244959037",
                    "fileUrl": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
                    "transcodeTaskId": "transcode-0bee89b07a248e27c83fc3d5951213c1",
                    "porncheckTaskId": "porncheck-f5ac8127b3b6b85cdc13f237c6005d80"
                }
            }
        },
        {
            "msgHandle": "MsgHandle2", // The handler of the second event notification
            "eventContent": { // The content of the second event notification
                "version": "4.0",
                "eventType": "ConcatComplete", // This field indicates that the type of the event notification is "Video Stitching Completed"
                "data": {
                    "status": 0,
                    "message": "",
                    "vodTaskId": "concat-1edb7eb88a599d05abe451cfc541cfbd",
                    "fileInfo": [
                        {
                            "fileId": "14508071098244931831",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8",
                            "fileType": "m3u8"
                        },
                        {
                            "fileId": "14508071098244929440",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4",
                            "fileType": "mp4"
                        }
                    ]
                }
            }
        }
    ]
}
```

