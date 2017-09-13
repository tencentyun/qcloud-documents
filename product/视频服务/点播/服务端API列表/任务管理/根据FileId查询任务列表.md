## 接口名称
GetTaskListByFileId

## 功能说明
1. 根据FileId查询任务列表。

注意：只会查找到三天内的任务

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 文件ID |
| order       | 否    | String | 结果排序，asc：按创建时间升序 desc：按创建时间降序。 不填默认为asc             |
| next        | 否    | Integer | 从该数据开始查找，如果order是asc，则查找创建时间大于该值的，否则，查找创建时间小于该值的                                |
| startTime        | 否    | Integer | 查询创建时间大于该时间的任务，目前任务信息只保存3天，所以该值必须大于三天前的时间戳                                    |
| endTime        | 否    | Integer | 查询创建小于该时间的任务，目前任务信息只保存3天，所以该值必须大于三天前的时间戳                                     |
| size      | 否    | Integer | 查找个数，范围在10-100之间。 不填默认为10                         |
| status      | 否    | String | 任务状态，Processing/Finish 两种                         |    
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=GetTaskListByFileId
&fileId=9031868223218623494
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| vodTaskList | Array | 转码模板信息列表 |
| vodTaskList.vodTaskId | String | 任务ID |
| vodTaskList.type | String | 任务类型 |
| vodTaskList.status | String | 任务状态，取值 PROCESSING/FINISH |
| vodTaskList.createTime | Integer | 任务创建时间（Unix时间戳） |
| vodTaskList.updateTime | Integer | 任务信息最近更新时间（Unix时间戳） |
                 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1000 | 无效参数  |
| 10702 | 内部错误  |

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "procedureList": [
        {
            "vodTaskId": "1251132654-Procedure-d7c9631c15ecf653b1ff67e34cb04692",
			"type":"procedure",
			"status": "PROCESSING",
            "createTime": 1485156352,
            "updateTime": 1485156352
        },
        {
			"type":"transcode"
			"status": "PROCESSING",
            "vodTaskId": "1251132654-Procedure-d7c9631c15ecf653b1ff67e34cb04692",
            "createTime": 1485156352,
            "updateTime": 1485156352
        }
    ]
}
```