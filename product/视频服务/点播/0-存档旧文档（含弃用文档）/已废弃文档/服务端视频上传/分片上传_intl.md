## API Name
UploadPart

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
vod2.qcloud.com

> Note:
> - Domain name for video uploads is different from those of other APIs at the server. It is *not** vod.api.qcloud.com;
> - The API only supports POST method, and does not support GET method.

### Peak Calling Frequency
10,000 counts/min

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileSha | Yes | String | The entire file SHA (not the SHA of the current part) must be consistent with the fileSha entered when initializing the upload (InitUpload) |
| offset | Yes | Integer | Relative offset of the part in a file; the value must be an integral multiple of dataSize |
| dataSize | Yes | Integer | Part size, refer to the description later |
| dataMd5 | Yes | String | md5 of the upload data of the part, for calculation method, refer to the description later |
| COMMON_PARAMS | Yes |  | Refer to [Common Parameters](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

**Calculation method of dataMd5:**

1. Use [MD5 Hash Algorithm](https://zh.wikipedia.org/wiki/MD5) to calculate the hash value of the entire video file to get a 128-bit (16-byte) binary string;
1. Encode the binary string in hexadecimal format, and the encoding algorithm must use lowercase letters, ie, a-f, not A-F.

**About dataSize:**

1. Except for the last part, the value of dataSize of other parts must be consistent with the value entered when initializing the upload (InitUpload);
1. The value of dataSize of the last part must be less than or equal to the value of dataSize entered when initializing the upload;

**For example:**

1. If you need to upload a video file of 6,000,000 bytes (about 5.72MB), set the dataSize to 1,048,576 (1MB) when initializing the upload;
1. The entire video will be divided into six parts. For the first five parts, each dataSize is 1,048,576 (1MB), and their offsets are 0, 1,048,576, 2,097,152, 3,145,728 and 4,194,304 respectively;
1. For the last part, the dataSize is 757,120 (calculation method: 6,000,000 - 5 * 1,048,576), and the offset is 5242880.

### Request Example
The following is the request URL. The real video data should be submitted in the body of the POST request.

```
https://vod2.qcloud.com/v2/index.php?Action=UploadPart
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&offset=0
&dataSize=1048576
&dataMd5=0bee89b07a248e27c83fc3d5951213c1
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

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| -10001 | Error when checking common parameters |
| -10002 | Error when checking signatures |
| -10003 | Error when checking protocol parameters |
| -10004 | Failed to write cache information |
| -10005 | Failed to get cache information |
| -10006 | Invalid packet size |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "",
    "canRetry": 0
}
```

