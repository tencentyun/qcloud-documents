## API Name
FinishUploadEx

## Feature Description
1. This API is used to upload the video from the APP **client** to the VOD server;
2. This API can also be used for the APP **server** to upload video to the VOD server. But for this scenario, we recommend using the server upload SDK or server upload API ([InitUpload](/document/product/266/7809)/[UploadPart](/document/product/266/7810)/[FinishUpload](/document/product/266/7811));
3. As video files are generally large, they need to be uploaded in parts. The upload process involves three steps: [Initialize Upload (UGC)](/document/product/266/7902), [Multipart Upload (UGC)](/document/product/266/7903), and [Finish Upload (UGC)](/document/product/266/7904), as shown in the following figure;
4. Instant upload and resuming upload from breakpoints are supported;
5. If the client reports the fileID to the APP server after uploading, the APP server can check the validity of the fileID according to the verification information field provided by the API and prevent the client from tampering the information of the uploaded file;
6. The API logic is relatively complex. There are UGC upload SDKs of various languages encapsulated in the VOD service to make it easier for developers to call the API. For more information. see [Overview of UGC Video Upload](/document/product/266/7835).

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
| fileSha | Yes | String | File sha |
| signature | Yes | String | Signature for UGC upload. Refer to UGC Video Upload Signature Generation |

### Request Example

```
https://vod2.qcloud.com/v2/index.php?Action=FinishUploadEx
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&signature=IEmbRAPy5IgIAFnt7XPAToaY3RRzPUFLSURVZ
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
| verify_content | String | Information validity verification content, which can be used to verify whether the reported fileID is valid when the client reports the fileID information of the uploaded file to the service server (refer to "Validity Verification Instruction" for how to use it). This field can be ignored if there is no need for verification |

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

```javascript
{
    "code": 0,
    "message": "",
    "fileId": "7031868222808505913",
    "verify_content": "MzMyOTY0NGIwNTk4YTc2YzZjNDljNTk3YTJhNzNkOGE1ZjA3YWJlOUV4cFRpbWU9MTQ4ODE2MDI2NCZGaWxlSWQ9NzAzMTg2ODIyMjgwODUwNTkxMw=="
}
```

### Validity Verification Instruction

The fileId of the uploaded file will be acquired after the client has finished the uploading process. Usually, the APP server will require the client to report the fileId of uploaded file to the server to use as record for managing uploaded videos. However, the APP server cannot ensure the validity of fileId that is uploaded by the user, because it is possible for the user to tamper with the fileId.

To verify the validity of user-uploaded fileID, the user may require the client to report the verify_content field (acquired from the response packet when the upload is completed), together with fileId, to the APP server. The APP server will then able to verity the validity of fileId by using verify_key, which is delivered by the VOD service.

#### Example
Any user who wishes to verify the validity of fileId can quest the verify_key used for verification from the VOD customer. The verify_key in this example is the string ```"6367c48dd193d56ea7b0baad25b19455e529f5ee"```.

fileId and verify_content will be acquired when the client has completed the upload. Here, we assume the fileId and verify_content are the strings ```"7031868222808505913"``` and ```"MzMyOTY0NGIwNTk4YTc2YzZjNDljNTk3YTJhNzNkOGE1ZjA3YWJlOUV4cFRpbWU9MTQ4ODE2MDI2NCZGaWxlSWQ9NzAzMTg2ODIyMjgwODUwNTkxMw=="```, respectively.

The client needs to report both fileId and verify_content to the APP server.

The APP server will perform BASE64 decoding on the received verify_content and obtain binary content. The first 20 bytes of the content is HashedContent, the rest is PlainText.

PlainText is in the form of characters. The PlainText in this example is the string ```"ExpTime=1488160264&FileId=7031868222808505913"```. The APP server can verity if the content of PlainText has expired (ExpTime is beyond the current server time) as well as whether the reported content is consistent (whether FileId is consistent). Verification is considered failure if the content has expired or is inconsistent.

If PlainText verification succeeds, the PlainText will be encrypted using HAMC-SHA1 algorithm and verify_key as private key (the result after encryption in this example is presented as the hexadecimal value ```3329644b0598a76c6c49c597a2a73d8a5f07abe9```). The verification is considered successful if this result matches with the HashedContent mentioned above. Otherwise, the verification fails.
