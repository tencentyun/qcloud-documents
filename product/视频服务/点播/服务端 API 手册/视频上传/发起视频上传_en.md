## API Name
ApplyUpload

## Feature Description
1. Initiate video (and cover image) upload operation and obtain meta-information (such as upload path and upload signature) of file upload to Tencent Cloud COS.
2. For which step of the server upload process the API is in, please see [Server Upload Overview](https://cloud.tencent.com/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B).

## SDK
It is recommended to use [VOD Server SDK](https://cloud.tencent.com/document/product/266/7982) to call the API.

## Request Method

### Request Domain
vod.api.qcloud.com

### Max Calling Frequency
100/min

### Parameter Description
| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| videoType | Yes | String | Video file type |
| videoName | No | String | Video file name |
| videoSize | No | Integer | Video file size (in bytes) |
| coverType | No | String | Cover image file type |
| coverName | No | String | Cover image file name |
| coverSize | No | Integer | Cover image file size (in bytes) |
| procedure | No | String | Operations of follow-up video tasks, please see [Parameter Template and Task Flow](https://cloud.tencent.com/document/product/266/10263) |
| COMMON_PARAMS | Yes |  | For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) |

### Request Example
```
https://vod.api.qcloud.com/v2/index.php?Action=ApplyUpload
&videoType=mp4&coverType=jpg
&COMMON_PARAMS
```
## API Response

### Parameter Description
| Parameter | Type | Description |
|---------|---------|---------|
| code | Integer | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| video | Array | COS upload information of video file |
| cover | Array | COS upload information of cover image file |
| storageBucket | String | Bucket used for COS upload |
| storageRegion | String | Region used for COS upload |
| vodSessionKey | String | Session Key used for VOD to confirm the upload process |

#### COS Upload Information Result Set
| Parameter | Type | Description |
|---------|---------|---------|
| storagePath | String | Target path of COS upload |

### Error Codes
| Error Code | Description |
|---------|---------|
| 4000-7000 | For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/266/7783) |
| 32001 | Internal service error  |

### Response Example
```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "video": {
        "storagePath": "/6c0f1c00vodgzp251000333/dee2156d24820810452266402/f0.mp4"
    },
    "cover": {
        "storagePath": "/6c0f1c00vodgzp251000333/dee2156d24820810452266402/24820810452266403.jpg"
    },
    "storageBucket": "6c0f1c00vodgzp251000333",
    "storageRegion": "gzp",
    "vodSessionKey": "3KEGq9DWHl1xF819mM4jVFkGn5WON80NwN/rTrx56UoEFApIV9DQ7t5m1g4hASR11gKWwGxkignB3AmhKOpUnym7wyNEHOwDJPcT5fBu66iCLcW7bhyRfDSsQcVpX0Wt96RKSsZFf62jeAB+e5640U8rMPV3Rf2eR+y1AgI+EC3JZU5iZbjLX4qNVI4RuLvLGcCUkYqWAYeqfHMYjvz0Fzhg6KuxnLicfs4D0gpyoX1X6gcsX8cWS0S0jCaZ+Q/r29IlU/w6E+UDFuk5yZik+whNxaZ/mOrctqr25jQ="
}
```
