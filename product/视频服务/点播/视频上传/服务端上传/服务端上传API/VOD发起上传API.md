## 接口名称
ApplyUpload

## 功能说明
1. 发起视频文件（和视频封面文件）的上传，获取文件上传到腾讯云对象存储 COS 的元信息（包括上传路径、上传签名等）。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| videoType | 是 | String | 视频文件类型 |
| videoName | 否 | String | 视频文件名称 |
| videoSize | 否 | Integer | 视频文件的大小(单位：字节) |
| coverType | 否 | String | 封面文件类型 |
| coverName | 否 | String | 封面文件名称 |
| coverSize | 否 | Integer | 封面文件的大小(单位：字节) |
| classId | 否 | Integer | 视频文件分类，默认为0 | 
| isTranscode | 否 | Integer | 视频是否转码，默认为0（0表示不发起转码，1表示发起转码） | 
| isScreenshot  | 否 | Integer | 视频是否截图，默认为0（0表示不截图，1表示截图） |
| isWatermark | 否 | Integer | 视频是否打水印，默认为0（0表示不打水印，1表示打水印） |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=ApplyUpload
&videoType=mp4
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| video | Array | 视频文件的 COS 上传信息 |
| cover | Array | 封面文件的 COS 上传信息 |
| storageAppid | String | COS 上传使用的 appid |
| storageBucket | String | COS 上传使用的 bucket |
| storageRegion | String | COS 上传的地域 |
| vodSessionKey | String | VOD 确认上传时使用的会话 Key |

#### COS上传信息结果集
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| storageSignature | String | COS 上传使用的签名 |
| storagePath | String | COS 上传的目的路径 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 32001 | 服务内部错误  |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "video": {
        "storageSignature": "K1SSfRpwkNy6EO3bvkK+31WKnw5hPTEwMDIyODUzJmI8NmMwZjFjMDB2b2RnenAyNTEwMDAzMzMmaz1BS0lESVdlN0F0STEwUFFrbThSRURsNFVPN0k2bXluNk5ERjcmZT0xNDkzMTA5MjYwJnQ9MTq5MjkzNjQ2MCZyPTQ1MjEwODE5mCZmPQ==",
        "storagePath": "/6c0f1c00vodgzp251000333/dee2156d24820810452266402/f0.mp4"
    },
    "cover": {
        "storageSignature": "7oYYOyab7dhs49YwdIhxPM04aFhhPTEwMDI8ODUzJmI9NmMwZjFjMDB2b2RnenAyNTEwMDAzMzMmaz1BS0lESVdlN0F0STEwUFFrbThSRURsNFVPN0k2bXluNk5ERjcmZT0xNDkzMTA5MjY4JnQ9MTQ5MjkzNjQ2MCZyPTk1ZDI3MTY0MSZmPQ==",
        "storagePath": "/6c0f1c00vodgzp251000333/dee2156d24820810452266402/24820810452266403.jpg"
    },
    "storageAppId": 10022853,
    "storageBucket": "6c0f1c00vodgzp251000333",
    "storageRegion": "gzp",
    "vodSessionKey": "3KEGq9DWHl1xF819mM4jVFkGn5WON80NwN/rTrx56UoEFApIV9DQ7t5m1g4hASR11gKWwGxkignB3AmhKOpUnym7wyNEHOwDJPcT5fBu66iCLcW7bhyRfDSsQcVpX0Wt96RKSsZFf62jeAB+e5640U8rMPV3Rf2eR+y1AgI+EC3JZU5iZbjLX4qNVI4RuLvLGcCUkYqWAYeqfHMYjvz0Fzhg6KuxnLicfs4D0gpyoX1X6gcsX8cWS0S0jCaZ+Q/r29IlU/w6E+UDFuk5yZik+whNxaZ/mOrctqr25jQ="
}
```