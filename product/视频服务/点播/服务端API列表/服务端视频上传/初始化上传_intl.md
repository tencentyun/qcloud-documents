## API Name
InitUpload

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
| fileName | Yes | String | Local name of a video file. The length should be limited to 40 bytes, and the name cannot contain characters such as \ / : * ? " < > (excluding file extensions such as .mp4) |
| fileSha | Yes | String | SHA value of a video file, for calculation method, refer to the description later |
| fileSize | Yes | Integer | Total size of a video file, in bytes |
| DataSize | Yes | Integer | Size of each part when calling the multipart upload API (UploadPart). Available values include 524288 (512KB) and 1048576 (1MB) |
| fileType | Yes | String | Type of a video file, a video's file extension, such as mp4 and flv |
| tags.n | No | String | Video tag |
| classId | No | Integer | Category ID of the video |
| isTranscode | No | Integer | Whether to perform transcode. 0: No; 1: Yes. If the video is not transcoded, , you can transcode it via console or call ([Video Transcode API](/document/product/266/7822)) after completion of upload |
| isScreenshot | No | Integer | Whether to take screenshot. 0: No (default), 1: Yes |
| isWatermark | No | Integer | Whether to add watermark. 0: No (default), 1: Yes. Be sure to select watermark file and determine watermark location in advance if you choose to add watermark. Otherwise the upload process may fail |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

** Calculation method of fileSha:**

1. Use [SHA-1 Hash Algorithm](https://zh.wikipedia.org/wiki/SHA-1) to calculate the hash value of the entire video file to get a 160-bit (20-byte) binary string;
1. Encode the binary string in hexadecimal format, and the encoding algorithm must use lowercase letters, ie, a-f, not A-F.

### Request Example
```
https://vod2.qcloud.com/v2/index.php?Action=InitUpload
&fileName=test
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=20350000
&dataSize=1048576
&fileType=mp4
&tags.1=foo
&tags.2=bar
&isTranscode=1
&isScreenshot=1
&isWatermark=1
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | <0: Failed; 0: Initialization succeeded, you can upload the file in parts; 1: File partially exists. You can resume upload from the breakpoint; 2: File already exists, no need to upload again (instant upload) |
| message | String | Error message|
| listParts | Array | If upload can be resumed from a breakpoint (or the code is 1), the array will list the parts already existing in the server and they won't be uploaded again |
| ListParts.offset | Integer | Relative offset of the existing part in a file |
| listParts.dataSize | Integer | Size of the existing part |
| listParts.dataMd5 | String | md5 of the existing part |
| codeDesc | String | Error message recorded in the backend |
| dataSize | Integer | Return when code is 1; it indicates you can resume the upload from the breakpoint; as the file was uploaded in parts in a certain size, such size shall also be deemed as the dataSize for subsequent multipart upload (UploadPart) |
| fileId | String | Return when code is 2; it means the file already exists. The value indicates the fileId of the video file |
| url | String | Return when code is 2; it means the file already exists. The value indicates the url of the video file |
| canRetry | Integer | code < 0: error when uploading; a value of 1 means such error can be resolved if you retry the request; otherwise, you must perform troubleshooting |

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

**Normal upload:**

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "",
    "canRetry": 0
}
```

**Resuming upload from the breakpoint:**

The following response packet size indicates that the first and second 1MB blocks of the video file already exist; you just need to upload the other blocks of the file in parts (UploadPart).

```javascript
{
    "code": 1,
    "message": "",
    "codeDesc": "",
    "canRetry": 0,
    "listParts": [
        {
            "offset": 0,
            "dataSize": 1048576,
            "dataMd5": "0bee89b07a248e27c83fc3d5951213c1"
        },
        {
            "offset": 1048576,
            "dataSize": 1048576,
            "dataSha": "f5ac8127b3b6b85cdc13f237c6005d80"
        }
    ]
}
```

**Instant upload:**

```javascript
{
    "code": 2,
    "message": "",
    "fileId": "16092504232103571364",
    "url": "http://10013.vod2.myqcloud.com/vod10013/16092504232103571364/f0.mp4"
}
```

**Upload failed:**

```javascript
{
    "code": -10001,
    "message": "invalid arg",
    "canRetry" : 0
}
```
