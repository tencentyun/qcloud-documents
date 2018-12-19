## API Name
SmallFileUpload

## Feature Description
1. This API is used to upload the video cover with size less than 1 MB

## Request Method

### Request Domain
vod2.qcloud.com

> Note:
> - Domain name for video uploads is different from those of other APIs at the server. It is *not* vod.api.qcloud.com;
> - The API supports POST method.

##### Parameter Description
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Command field, enter SmallFileUpload |
| fileName | Yes | String | Local name of the video file. If the name contains Chinese spaces, rawurlencode encoding is needed. The length should be limited to 40 characters, and the name cannot contain characters such as \ / : * ? " < > \ and | |
| fileSha | Yes | String | sha of a file. SHA-1 is used to calculate the content of the file |
| fileSize | Yes | Int64 | Total size of a file, in bytes. Note: This API can only upload the file with size less than 1M |
| dataSize | Yes | Int | Size of the part uploaded, which is equal to fileSize, for protocol alignment |
| fileType | Yes | String | Type of a video file. This can be known from the file extension |
| extra.usage | Yes | Int | To identify the usage of the file. 1: to upload specified video cover |
| extra.fileId | No | String | Enter when extra.usage=1, the corresponding video file id of the cover to be uploaded|

### Request Example
The following is the request URL. The real video data should be submitted in the body of the POST request.
```
https://vod2.qcloud.com/v2/index.php?Action=InitUpload
&fileName=test
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=1048576
&dataSize=1048576
&fileType=jpg
&COMMON_PARAMS
```

## API Response

##### Parameter Description
| Name | Type | Description |
|---------|---------|---------|
| code | Int | <0: Failed; 0: Initialization succeeded, you can upload the file in parts; 1: File partially exists. You can continue uploading the missing part (resume upload from the breakpoint); 2: File already exists, no need to upload again (instant upload) |
| message | String | Error message|
| listParts.offset | Int64 | Relative offset of a part, it exists when code=1 |
| listParts.dataSize | Int | Size of a part, it exists when code=1 |
| listParts.dataMd5 | String | md5 of a part, it exists when code=1 |
| codeDesc | String | Error message recorded in the backend |
| dataSize | Int | Size of a part, it returns when code=1. The value shall prevail in the front-end |
| fileId | String | File id, it returns when code=2 |
| canRetry | Int | code<0: whether it is allowed to be retried; canRetry=1: Allowed |

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
```
{
    "canRetry": 0,
    "code": 0,
    "codeDesc": "",
    "fileId": "11868222811305801",
    "message": "",
    "url": "http://1251132154.vod2.myqcloud.com/vod1251132154/9031868222807461771/11868222811305801.jpg"
}
```
