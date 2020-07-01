## 接口名称
CreateImageSprite

## 功能说明
1. 对视频文件进行截图，生成雪碧图，生成的雪碧图规格参见[雪碧图截图规格说明](/document/product/266/8099)；
1. 截取雪碧图任务结束之后，如果APP配置了服务端事件通知，则会产生截取雪碧图完成事件通知。

## 事件通知
雪碧图截取成功可触发[事件通知-截取雪碧图完成](/document/product/266/8104)。APP后台可据此监听点播系统中的视频截取雪碧图行为。

更多参见[服务端事件通知简介](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明

| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 文件的FileID |
| definition | 是 | Integer | 雪碧图截图规格，参见[雪碧图截图规格说明](/document/product/266/8099) |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

```
https://vod.api.qcloud.com/v2/index.php?Action=CreateImageSprite
&fileId=96000077184630899
&definition=10
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功；其他值: 失败 |
| message | String | 错误信息 |
| vodTaskId | String | 任务id |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误 |
| 1000 | 无效参数 |
| 1108 | 内部错误 |
| 1152 | 内部错误 |
| 1801 | 内部错误 |
| 1802 | 内部错误 |
| 2000 | 内部错误 |
| 2001 | 内部错误 |
| 10009 | 文件状态异常 |
| 10010 | 内部错误 |
| 10012 | 内部错误 |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "vodTaskId": ""
}
```
