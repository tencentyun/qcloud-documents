## 接口名称
CommitUpload

## 功能说明
1. 确认视频文件（和视频封面文件）的上传，获取文件的播放地址和文件 ID。
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
| vodSessionKey | 是 | String | 点播发起上传时获取的会话Key |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=CommitUpload
&vodSessionKey=3KEGq9DWHl1xF819mM4jVFkGn5WON80NwN/rTrx56UoEFApIV9DQ7t5m1g4hASR11gKWwGxkignB3AmhKOpUnym7wyNEHOwDJPcT5fBu66iCLcW7bhyRfDSsQcVpX0Wt96RKSsZFf62jeAB+e5640U8rMPV3Rf2eR+y1AgI+EC3JZU5iZbjLX4qNVI4RuLvLGcCUkYqWAYeqfHMYjvz0Fzhg6KuxnLicfs4D0gpyoX1X6gcsX8cWS0S0jCaZ+Q/r29IlU/w6E+UDFuk5yZik+whNxaZ/mOrctqr25jQ=
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| video | Array | 视频文件执行上传结果信息 |
| cover | Array | 封面文件执行上传结果信息 |
| fileId | String | 视频文件的文件ID |

#### 执行上传文件结果集
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| url | String | 视频文件播放地址(封面文件的下载地址) |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 31001 | VodSessionKey错误  |
| 32001 | 服务内部错误 |

### 应答示例
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