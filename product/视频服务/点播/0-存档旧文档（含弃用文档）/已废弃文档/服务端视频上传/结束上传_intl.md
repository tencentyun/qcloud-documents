## API Name
FinishUpload

## Feature Description
1. This API is used to upload the video from the APP **server** to the VOD server;
1. For UGC videos that need to be uploaded from the **client** (iOS/Android/Web) to the VOD server, this API is **not applicable**, because the SecretId and SecretKey of APP are not allowed to be exposed to the client; instead, the method described in [Overview of UGC video upload](/document/product/266/7835) is available;
1. As video files are generally large, they need to be uploaded in parts. The upload process involves three steps: [Initialize Upload](/document/product/266/7809), [Upload in Parts](/document/product/266/7810), and [Finish Upload](/document/product/266/7811), as shown in the following figure;
1. Instant upload and resuming upload from breakpoints supported;
1. As this API has very complex logic, the VOD server is encapsulated with a multi-language SDK to simplify the developer's call; it is recommended that developers directly use the server SDK to upload the local videos to the server.

![](//mc.qcloudimg.com/static/img/0e4d6bd7e7b153089d9bc5982947964e/image.png)

## Event Notification
Completion of file upload can trigger [Event Notification - Video Upload Completed](/document/product/266/7830). It can be used by the APP backend server to monitor the video upload behavior in the VOD system.

For details, refer to [Introduction to Server Event Notification](/document/product/266/7829).

## Request Method

### Request Domain
Vod2.qcloud.com

> Note:
> - Domain name for video uploads is different from those of other APIs at the server. It is *not** vod.api.qcloud.com;
> - The API only supports GET method, and does not support POST method.

### Peak Calling Frequency
100 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileSha | Yes | String | File sha |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### Request Example

```
https://vod2.qcloud.com/v2/index.php?Action=FinishUpload
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| Code | Integer | < 0: Failed; 0: Succeeded |
| message | String | Error message|
| codeDesc | String | Error message recorded in the backend, for Tencent Cloud backend positioning |
| canRetry | Integer | code < 0: error when uploading; a value of 1 means such error can be resolved if you retry the request; otherwise, you must perform troubleshooting |
| fileId | String | File id |
| url | String | File url |

### Error Code Description
| Error Code | Description |
|---------|---------|
| -10001 | Error when checking common parameters |
| -10002 | Error when checking signatures |
| -10003 | Error when checking protocol parameters |
| -10004 | Failed to write cache information |
| -10005 | Failed to get cache information |
| -10006 | Invalid packet size |

If an error code other than the above occurs, it may be an occasional failure cause by the network disconnection. When an error code is less than 0 and canRetry is 1, the error can be resolved if you retry the request.

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "fileId": "7031868222808505913",
    "url": "http://10013.vod2.myqcloud.com/vod10013/7031868222808505913/f0.mp4"
}
```
