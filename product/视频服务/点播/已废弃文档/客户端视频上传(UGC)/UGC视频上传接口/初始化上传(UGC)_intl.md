## API Name
InitUploadEx

## Feature Description
1. This API is used to upload the video from the APP **client** to the VOD server;
2. This API can also be used for the APP **server** to upload video to the VOD server. But for this scenario, we recommend using the server upload SDK or server upload API ([InitUpload](/document/product/266/7809)/[UploadPart](/document/product/266/7810)/[FinishUpload](/document/product/266/7811));
3. As video files are generally large, they need to be uploaded in parts. The upload process involves three steps: [Initialize Upload (UGC)](/document/product/266/7902), [Multipart Upload (UGC)](/document/product/266/7903), and [Finish Upload (UGC)](/document/product/266/7904), as shown in the following figure;
4. Instant upload and resuming upload from breakpoints are supported;
5. The API logic is relatively complex. There are UGC upload SDKs of various languages encapsulated in the VOD service to make it easier for developers to call the API. Refer to [Overview of UGC Video Upload](/document/product/266/7835) for details.

![](//mc.qcloudimg.com/static/img/03bceeaebef439eb218edd080ef4d7fa/image.png)

## Request Method

### Request Domain
vod2.qcloud.com

> Note:
> - Domain name for UGC video upload and server video upload is different from those of other server APIs. It is **not** vod.api.qcloud.com;
> - The method for generating signature for UGC video upload is different from that of server APIs. Refer to UGC Video Upload Signature Generation for details;
> - When uploading a single video file, all APIs that will be called (including [Initialize Upload (UGC)](/document/product/266/7902), [Multipart Upload (UGC)](/document/product/266/7903), [Finish Upload (UGC)](/document/product/266/7904)) use the same signature;
> - The API only supports GET method, and does not support POST method.

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileSha | Yes | String | SHA value of video file Calculation method will be described below |
| fileSize | Yes | Integer | Total size of video file (in bytes) |
| dataSize | Yes | Integer | The size of each part when calling the multipart upload API (UploadPartEx). Available values include 524288 (512KB) and 1048576 (1 MB) |
| signature | Yes | String | Signature for UGC upload. Refer to UGC Video Upload Signature Generation |

**Note:**

- Controls such as file name, file category and whether to transcode, are not specified by the client. These controls are passed via signature by the server.

** Calculation method of fileSha:**

1. Use [SHA-1 Hash Algorithm](https://zh.wikipedia.org/wiki/SHA-1) to calculate the hash value of the entire video file to get a 160-bit (20-byte) binary string;
2. Encode the binary string in hexadecimal format, and the encoding algorithm must use lowercase letters, ie, a-f, not A-F.

### Request Example
```
https://vod2.qcloud.com/v2/index.php?Action=InitUploadEx
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=20350000
&dataSize=1048576
&signature=IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZ
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Integer | <0: Failed; 0: Initialization succeeded, you can upload the file in parts; 1: File partially exists. You can resume upload from the breakpoint; 2: File already exists, no need to upload again (instant upload) |
| message | String | Error message|
| listParts | Array | If upload can be resumed from a breakpoint (code is 1), the array will list the parts already existing in the server and they won't be uploaded again |
| listParts.offset | Integer | Relative offset of the existing part in a file |
| listParts.dataSize | Integer | Size of the existing part |
| listParts.dataMd5 | String | md5 of the existing part |
| codeDesc | String | Error message recorded in the backend |
| dataSize | Integer | Return when code is 1; it indicates you can resume the upload from the breakpoint; as the file was uploaded in parts in a certain size, such size shall also be deemed as the dataSize for subsequent multipart upload (UploadPart) |
| fileId | String | Return when code is 2; it means the file already exists. The value indicates the fileId of the video file |
| url | String | Return when code is 2; it means the file already exists. The value indicates the url of the video file |
| canRetry | Integer | A negative code means an error occurred when uploading. The error can be resolved by retrying if this value is 1, otherwise you must perform troubleshooting |

### Error Code Description
| Error Code | Description |
|---------|---------|
| -10001 | Error when checking common parameters |
| -10002 | Error when checking signatures |
| -10003 | Error when checking protocol parameters |
| -10004 | Failed to write cache information |
| -10005 | Failed to get cache information |
| -10006 | Invalid packet |

If an error code other than the above occurs, it may be an occasional failure caused by network issues. For all negative error codes, if canRetry is 1, the error can be resolved if you retry the request.

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

**Resuming upload from breakpoint:**

The following response packet indicates that the first and second 1 MB parts of the video file already exist; you only need to upload the other parts of the file when performing multipart uploading (UploadPart).

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
