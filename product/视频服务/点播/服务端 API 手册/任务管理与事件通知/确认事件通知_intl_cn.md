## 接口名称
ConfirmEvent

## 功能说明
1. 开发者调用拉取事件通知，获取到事件之后，必须调用该接口来确认消息已经收到；
2. 更多参考[服务端事件通知](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
1000次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| msgHandle.n | 是 | String | 事件句柄，n 从0开始递增。开发者获取到事件句柄后，等待确认的有效时间为30秒 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=ConfirmEvent
&msgHandle.0=XXXX
&msgHandle.1=YYYY
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
| 1000 | 无效参数  |
| 1001 | 内部错误  |
| 2000 | 内部错误  |

### 应答示例
```javascript
{
    "code": 0,
    "message": ""
}
```
