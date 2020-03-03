## API Name
UploadPartEx

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
> - The API only supports POST method, and does not support GET method.

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| fileSha | Yes | String | File SHA (note that this is not the SHA of the current part). It must be consistent with the fileSha entered when initializing the upload (InitUpload) |
| offset | Yes | Integer | Relative offset of the part in a file; the value must be an integral multiple of dataSize |
| dataSize | Yes | Integer | Part size, refer to the description below |
| dataMd5 | Yes | String | md5 of the uploaded data in the part, for calculation method, refer to the description below |
| signature | Yes | String | Signature for UGC upload. Refer to UGC Video Upload Signature Generation |

**Calculation method of dataMd5:**

1. Use [MD5 Hash Algorithm](https://zh.wikipedia.org/wiki/MD5) to calculate the hash value of the entire video file to get a 128-bit (16-byte) binary string;
2. Encode the binary string in hexadecimal format, and the encoding algorithm must use lowercase letters, ie, a-f, not A-F.

**About dataSize:**

1. Except for the last part, the values of dataSize of other parts must be consistent with the values entered when initializing the upload (InitUpload);
2. The dataSize of the last part must be less than or equal to the value of dataSize entered when initializing the upload (InitUpload);

**For example:**

1. If you need to upload a video file of 6,000,000 bytes (about 5.72 MB), and the dataSize is configured as 1,048,576 (1 MB) when initializing the upload;
2. The entire video will be divided into six parts. The dataSize of the first five parts is 1,048,576 (1 MB), and their offsets are 0, 1,048,576, 2,097,152, 3,145,728 and 4,194,304 respectively;
1. For the last part, the dataSize is 757,120 (calculation method: 6,000,000 - 5 * 1,048,576), and the offset is 5,242,880.

### Request Example
The following is the request URL. The actual video data should be submitted in the body of the POST request.

```
https://vod2.qcloud.com/v2/index.php?Action=UploadPartEx
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&offset=0
&dataSize=1048576
&dataMd5=0bee89b07a248e27c83fc3d5951213c1
&signature=IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZ
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| Code | Integer | < 0: Failed; 0: Succeeded |
| message | String | Error message|
| codeDesc | String | Error message recorded in the backend, for Tencent Cloud backend positioning |
| canRetry | Integer | A negative code means an error occurred when uploading. The error can be resolved by retrying if this value is 1, otherwise you must perform troubleshooting |

### Error Code Description
| Error Code | Description |
|---------|---------|
| 4000-7000 | Refer to [Common Error Codes](/document/product/266/7783)  |
| -10001 | Error when checking common parameters |
| -10002 | Error when checking signatures |
| -10003 | Error when checking protocol parameters |
| -10004 | Failed to write cache information |
| -10005 | Failed to get cache information |
| -10006 | Invalid packet |

### Response Example

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "",
    "canRetry": 0
}
```

