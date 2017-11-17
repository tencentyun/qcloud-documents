## 接口名称
BanningVod

## 功能说明
禁止视频播放，使视频播放地址失效。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 希望获取的视频的ID |
| refreshCdn | 否 | Int | 是否刷新Cdn, 0: 不刷新, 其他值: 刷新，默认为0 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/api/213/6976) |

## 请求示例

### 禁播并且刷新对应的CDN

<pre>
https://vod.api.qcloud.com/v2/index.php?Action=BanningVod
&fileId=12345
&refreshCdn=1
&COMMON_PARAMS
</pre>

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| replayUrl | String | 回看视频播放地址。原视频播放地址失效后，可使用该地址播放禁播的视频。 |


### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1000 | 无效参数  |
| 1001 | 内部错误  |
| 1050 | 内部错误  |
| 1102 | 内部错误  |
| 1702 | 内部错误  |
| 10009 | 文件状态异常  |

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "replayUrl": "http://251000333.vod2.myqcloud.com/xxxxxx/xxxxxx/f0.mp4"
}
```
