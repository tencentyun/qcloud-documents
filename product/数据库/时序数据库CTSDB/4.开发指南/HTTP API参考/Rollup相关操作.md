## 建立Rollup任务 ##
### 请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}为rollup任务的名称
方法：PUT
### 请求参数 ###
无
### 请求内容 ###
| 参数名称        | 必选            | 类型            | 描述            |
|-----------------|-----------------|-----------------|-----------------|
| base_metric    | 是              | string          | Rollup依赖的metric名称 |
| rollup_metric  | 是              | string          | Rollup产生的metric名称 |
| base_rollup    | 否              | string          | 依赖的rollup任务：任务执行前会检查应时间段的依赖任务是否完成执行（父） |
| query           | 否              | string          | 过滤数据的查询条件，由很多个元素和操作对组成，例如name:host AND type:max OR region:gz|
| group_tags     | 是              | Array           | 进行聚合的维度列，可以包含多列 |
| copy_tags      | 否              | Array           | 不需要聚合的维度列：group_tags确定时，多条数据的copy_tags的值相同 |
| fields          | 是              | Map             | 指定聚合的名称、方法和字段，例如：{"cost_total":{"sum": {"field":"cost"}},"cpu_usage_avg":{ "avg": { "field":"cpu_usage"}}}|
| interval        | 是              | string          | 聚合粒度，如1s,5minute,1h,1d等 |
| delay           | 否              | string          | 延迟执行时间    |
| start_time     | 否              | string          | 开始时间：从该时间开始周期性执行rollup，默认为当前时间 |
| end_time       | 否              | string          | 结束时间：到达该时间后不再调度 ，默认为时间戳最大值 |
| options         | 否              | map             | 聚合选项，跟新建metric选项一致 |

### 返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### JSON示例说明 ###
请求：`POST /_rollup/ctsdb_rollup_task_test`

请求数据：

    {
    "base_metric": "ctsdb_test",
    "rollup_metric": "ctsdb_rollup_metric_test",
    "query" : "cpuUsage:20",
    "group_tags": ["region"],
    "fields": {
    "cpuUsage_total": {
    "sum": {
    "field": "cpuUsage"
    }
    }
    },
    "interval": "1h",
    "delay": "5m",
    "start_time": "1511918989",
    "options": {
    "expire_day": 365
    }
    }

返回：

    {
    "acknowledged": true,
    "message": "create rollup success"
    }

## 获取所有Rollup任务 ##
### 请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 请求路径和方法 ###
路径：`/_rollups`
方法：GET
### 请求参数 ###
无
### 请求内容 ###
无
### 返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### JSON示例说明 ###
请求：`GET /_rollups`

返回：

    {
    "result": {
    "rollups": [
    "rollup_jgq_6",
    "rollup_jgq_60"
    ]
    },
    "status": 200
    }

## 获取某个Rollup任务 ##
### 请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}为rollup任务的名称
方法：GET
### 请求参数 ###
无
### 请求内容 ###
无
### 返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### JSON示例说明 ###
请求：`GET /_rollup/rollup_hgh1`

返回：

    {
    "result": {
    "rollup_jgq_6": {
    "base_metric": "hgh1",
    "rollup_metric": "rollup_hgh1",
    "group_tags": [
    "appid",
    "domain",
    "paymode"
    ],
    "copy_tags": [
    "protocol",
    "vip"
    ],
    "fields": {},
    "interval": "1h",
    "delay": "5m",
    "depend_rollup": "hello",
    "options": {
    "expire_day": 93
    },
    "start_time": 1504310400,
    "end_time": 2147483647
    }
    },
    "status": 200
    }

## 删除Rollup任务 ##
### 请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}，为rollup任务的名称
方法：DELETE
### 请求参数 ###
无
### 请求内容 ###
无
### 返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### JSON示例说明 ###
请求：`DELETE /_rollup/ctsdb_rollup_task_test`

返回：

    {
    "acknowledged": true,
    "message": "update rollup success"
    }

## 启停Rollup任务 ##
### 请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}/update`，${rollup_task_name}为rollup任务的名称
方法：POST
### 请求参数 ###
无
### 请求内容 ###
--------

  |参数名称 |     必选 |  类型   |  描述|
|----|----|----|----|
 | state    |     是    | string  | running/pause|
  |start_time  | 否 |    string |  开始时间：从该时间开始周期性执行rollup，默认为当前时间|
  |end_time   |  否  |   string|   结束时间：到达改时间后不再调度，默认为时间戳最大值|
  |options  |     否|     map |     聚合选项，跟新建metric选项一致|

### 返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。

### JSON示例说明 ###
请求：`POST /_rollup/ctsdb_rollup_task_test/update`

请求数据：

    {
    "state":"running",
    "start_time": "1511918989",
    "end_time": "1512019765",
    "options": {
    "expire_day": 365
    }
    }

返回：

    {
    "acknowledged": true,
    "message": "update rollup success"
    }