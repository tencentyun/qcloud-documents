## 接口名称
ApplyUpload

## 功能说明
1. 发起视频文件（和视频封面文件）的上传，获取文件上传到腾讯云对象存储 COS 的元信息（包括上传路径、上传签名等）。
2. 该 API 在服务端上传位于哪个步骤请参考[服务端上传综述](/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B)。

## SDK
建议使用[点播服务端 SDK](/document/product/266/7982) 进行 API 的调用。

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
| procedure | 否 | String | 视频后续任务操作，详见[任务流综述](/document/product/266/10263) |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=ApplyUpload
&videoType=mp4&coverType=jpg
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
| storageBucket | String | COS 上传使用的 bucket |
| storageRegion | String | COS 上传的地域 |
| vodSessionKey | String | VOD 确认上传时使用的会话 Key |

#### COS上传信息结果集
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| storagePath | String | COS 上传的目的路径 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783) |
| 32001 | 服务内部错误  |

### 应答示例
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