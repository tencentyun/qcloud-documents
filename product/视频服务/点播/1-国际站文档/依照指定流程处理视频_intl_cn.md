## 接口名称
ProcessFileByProcedure

## 功能说明
该接口依照指定的流程参数对视频文件进行处理，可以指定的处理流程主要有：转码、创建雪碧图截图等。目前，具体流程参数需要与腾讯云点播商定。
*本接口只支持点播4.0*

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 处理的视频文件的ID |
| procedure | 否 | String | 流程参数 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFileByProcedure
&fileId=12345
&procedure=SomeProcedure
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| transcodeTaskId | String | 转码任务id（如果流程指定了转码任务 |
| imageSpriteTaskId | String | 雪碧图任务id（如果流程指定了创建雪碧图任务） |

如果流程指定了其他任务，应答参数里会包括相应的任务id。

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误  |
| 1000 | 无效参数  |
| 1001 | 内部错误  |
| 1003 | 内部错误  |
| 2000 | 内部错误  |
| 10008 | 文件不存在  |
| 10022 | 内部错误 |
| 50005 | Procedure重复任务已存在 |
| 50006 | Procedure任务创建失败 |
| 50007 | Procedure参数无效 |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
	"procedureTaskId":"125xx-Procedure-6a651e8d148c512af27f3b5f3d60f43a"
    
}
```
如果开启了回调通知，每个任务完成后会单独回调，参见[服务端事件通知简介](/document/product/266/7829)。
