## API Name
CommitUpload

## Feature Description
1. Confirm upload of video files (and cover image files), and obtain playback URLs and file IDs.
2. For which step of the server upload the API is in, please see [Server Upload Overview](https://cloud.tencent.com/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B).

## SDK
It is recommended to use [VOD server SDK](https://cloud.tencent.com/document/product/266/7982) to call the API.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| vodSessionKey | Yes | String | Session Key obtained when VOD initiates the upload |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=CommitUpload
&vodSessionKey=3KEGq9DWHl1xF819mM4jVFkGn5WON80NwN/rTrx56UoEFApIV9DQ7t5m1g4hASR11gKWwGxkignB3AmhKOpUnym7wyNEHOwDJPcT5fBu66iCLcW7bhyRfDSsQcVpX0Wt96RKSsZFf62jeAB+e5640U8rMPV3Rf2eR+y1AgI+EC3JZU5iZbjLX4qNVI4RuLvLGcCUkYqWAYeqfHMYjvz0Fzhg6KuxnLicfs4D0gpyoX1X6gcsX8cWS0S0jCaZ+Q/r29IlU/w6E+UDFuk5yZik+whNxaZ/mOrctqr25jQ=
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| video | Array | Execution result information of uploading video files |
| cover | Array | Execution result information of uploading cover image files |
| fileId | String | ID of a video file |

#### Result Set of Executing File Upload
| Parameter | Type | Description |
|---------|---------|---------|
| url | String | Video file playback URL (cover image download URL) |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783)  |
| 31001 | Incorrect VodSessionKey  |
| 32001 | Internal service error |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "video": {
        "url": "http://251000333.vod2.myqcloud.com/6c0f1c00vodgzp251000333/dee2125c24820810452266399/f0.mp4"
    },
    "cover": {
        "url": "http://251000333.vod2.myqcloud.com/6c0f1c00vodgzp251000333/dee2125c24820810452266399/24820810452266400.jpg"
    },
    "fileId": "24820810452266399"
}
```
