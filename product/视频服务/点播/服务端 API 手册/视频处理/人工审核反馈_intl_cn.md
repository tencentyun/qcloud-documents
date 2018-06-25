## 接口名称
ReplyManualReview

## 功能说明
1. 流式任务的人工审核阶段，需要通过该接口反馈审核结果；
2. 更多参考[服务端事件通知](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
1000次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| manualReviewId | 是 | String | 审核任务Id |
| result | 是 | String | Pass/Reject |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=ReplyManualReview
&manualReviewId=12519899xx-Procedure-d7c9631c15ecf653b1ff67e34cb04692-fdc9631c15ecf653b1ff67e34cb0469c
result=Pass
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
