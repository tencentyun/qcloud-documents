## 接口名称
ModifyVodInfo

## 功能说明
1. 修改视频文件的描述信息，包括分类、名称、描述等。
2. 修改视频文件的过期时间（仅点播4.0支持）。  

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 文件id |
| fileName | 否 | String | 文件名称 |
| fileIntro | 否 | String | 文件描述 |
| classId | 否 | Integer | 分类id |
| expireTime| 否 | String | 视频过期时间，格式: Y-m-d H:i:s，如2017-10-01 00:00:00。视频过期之后，该视频及其所有附属对象（转码结果、雪碧图等）将都被删除 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=ModifyVodInfo
&fileId=16092504232103571137
&fileName=newName
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误  |
| 1000 | 无效参数  |
| 1016 | 内部错误  |
| 10008 | 文件不存在  |

### 应答示例
```javascript
{
    "code": 0,
    "message": ""
}
```
