## 建立 Rollup 任务
在海量数据场景下，业务系统每天甚至每小时会产生 PB 级别数据。而时序数据的最主要的特点就是海量性、时效性和趋势性，因此通常情况下，使用数据的系统（例如监控系统或数据分析系统）通常只需要最近时间段内的高精度数据，而历史数据只需降精度（Downsampling）保存即可。用户可通过配置 Rollup 任务定时聚合历史数据保存至新的数据表。Rollup 任务不仅能降精度保存历史数据，也能提高查询性能，降低存储成本。需要注意的是，Rollup 任务会自动根据 base_metric 建立子表，继承父表的所有配置，如果指定 options，会覆盖父表配置。

### 1. 请求地址
地址为实例的 IP 和 PORT，可从控制台获取到，例如：10.13.20.15:9200。

### 2. 请求路径和方法
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`为 Rollup 任务的名称。
方法：PUT

### 3. 请求参数
无

### 4. 请求内容
| 参数名称      | 必选 | 类型   | 描述                                                         |
| ------------- | ---- | ------ | ------------------------------------------------------------ |
| base_metric   | 是   | string | Rollup 依赖的 metric 名称（父表）                            |
| rollup_metric | 是   | string | Rollup 产生的 metric 名称（子表）                            |
| base_rollup   | 否   | string | 依赖的 Rollup 任务，任务执行前会检查相应时间段的依赖任务是否完成执行 |
| query         | 否   | string | 过滤数据的查询条件，由很多个元素和操作对组成，例如：`name:host AND type:max OR region:gz` |
| group_by      | 是   | Array  | 进行聚合的维度列，可以包含多列                               |
| function      | 是   | Map    | 指定聚合的名称、方法和字段，其字段只能选自 base_metric 里的 fields 字段，如果 base_metric 的 fields 为空，则无法设置 rollup，function 有 sum、avg、min、max、set、any、first、last、percentiles 等。例如：`{"cost_total":{"sum": {"field":"cost"}},"cpu_usage_avg":{ "avg": { "field":"cpu_usage"}}}` |
| interval      | 是   | string | 聚合粒度（rollup 产生数据的时间精度），例如1s、5m（5分钟）、1h、1d等 |
| frequency     | 否   | string | 调度频率，例如5m、1h、1d等，默认等于 interval                |
| delay         | 否   | string | 延迟执行时间，写入数据通常有一定的延时，避免丢失数据，例如5m、1h等 |
| start_time    | 否   | string | 开始时间，从该时间开始周期性执行 Rollup，默认为当前时间      |
| end_time      | 否   | string | 结束时间，到达该时间后不再调度 ，默认为时间戳最大值          |
| options       | 否   | map    | rollup_metric 选项，跟新建 metric 选项一致                   |

### 5. 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6. CURL 示例说明
请求：
```
curl -u root:le201909 -H 'Content-Type:application/json' -X PUT 172.16.345.14:9201/_rollup/ctsdb_rollup_task_test -d'
{
    "base_metric": %{base_metric_name},      
    "rollup_metric": %{rollup_metric_name},    
    "base_rollup": %{base_rollup_name},        
    "query" : "name:host AND type:max",   
    "group_by": ["host"],   
    "function": {
        "cost_total":  {
            "sum": { 
                "field": "cost"
            }
        },
        "cpu_usage_avg": {
            "avg": {
                "field": "cpu_usage"
            }
        },
        "value": {   
          "percentiles": {      
            "field": "value",
            "percents": [
              95
            ]
          }
        },
        "metricName": {
          "set": {              
            "value": "cpu_usage"
          }
        },
        "appid": {
          "any": {             
            "field": "appid"
          }
        },
         "first_value": { 
          "first": {           
            "field": "value"
          }
        },
         "last_value": {
          "last": {             
            "field": "value"
          }
        }
    },
    "interval": "1m",           
    "frequency": "5m",          
    "delay": "1m",             
    "start_time": "1502892000",
    "end_time": "2147483647",
    "options": {
        "expire_day": 365
    }
}
'

```

返回：
```
{
    "acknowledged": true,
    "message": "create rollup success"
}
```

## 获取所有 Rollup 任务的名称
### 1. 请求地址
地址为实例的 IP 和 PORT，可从控制台获取到，例如：10.13.20.15:9200。

### 2. 请求路径和方法
路径：`/_rollups`
方法：GET

### 3. 请求参数
无

### 4. 请求内容
无

### 5. 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6. CURL 示例说明
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X GET 172.16.345.14:9201/_rollups`

返回：
```
{
    "result": 
	{
	    "rollups": 
		[
		    "rollup_jgq_6",
		    "rollup_jgq_60"
	    ]
    },
    "status": 200
}
```

## 获取某个 Rollup 任务的详细信息
### 1. 请求地址
地址为实例的 IP 和 PORT，例如：10.13.20.15:9200。

### 2. 请求路径和方法
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`为 Rollup 任务的名称。
方法：GET

### 3. 请求参数
指定 v 参数可以查看 rollup 的具体进度，返回结构中的 @last_end_time 为 rollup 最新进度。

### 4. 请求内容
无

### 5. 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6. CURL 示例说明
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X GET 172.16.345.14:9201/_rollup/rollup_jgq_6?v`

返回：
```
{
  "result": {
    "rollup_jgq_6": {
    "base_metric": "cvm_device-300",
       "rollup_metric": "cvm_device-86400",
       "query": "metricName:cpu_usage AND statType:max",
       "group_by": [
         "vm_uuid"
       ],
       "function": {
         "value": {
           "percentiles": {
             "field": "value",
             "percents": [
               95
             ]
           }
         },
         "metricName": {
           "set": {
             "value": "cpu_usage"
           }
         },
         "appid": {
           "any": {
             "field": "appid"
           }
         }
       },
       "interval": "1d",
       "delay": "5m",
       "options": {
         "expire_day": 186
       },
       "frequency": "1d",
       "start_time": 1534003200,
       "end_time": 2147483647,
       "@state": "running",             // 运行状态
       "@timestamp": 1550766085000,     // rollup 任务信息更新的时间点
       "@last_end_time": 1550764800     // rollup 任务正确执行到的时间点

    }
  },
  "status": 200
}
```

## 删除 Rollup 任务
### 1. 请求地址
地址为实例的 IP 和 PORT，例如：10.13.20.15:9200。

### 2. 请求路径和方法
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`，为 Rollup 任务的名称。
方法：DELETE

### 3. 请求参数
无

### 4. 请求内容
无

### 5. 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6. CURL 示例说明
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X DELETE 172.16.345.14:9201/_rollup/ctsdb_rollup_task_test`

返回：
```
{
    "acknowledged": true,
    "message": "delete rollup success"
}
```

## 更新 Rollup 任务
### 1. 请求地址
地址为实例的 IP 和 PORT，例如：10.13.20.15:9200。

### 2. 请求路径和方法
路径：`/_rollup/${rollup_task_name}/update`，`${rollup_task_name}`为 Rollup 任务的名称。
方法：POST

### 3. 请求参数
无

### 4. 请求内容
| 参数名称   | 必选 | 类型   | 描述                                                    |
| ---------- | ---- | ------ | ------------------------------------------------------- |
| state      | 是   | string | running/pause                                           |
| start_time | 否   | string | 开始时间，从该时间开始周期性执行 Rollup，默认为当前时间 |
| end_time   | 否   | string | 结束时间，到达改时间后不再调度，默认为时间戳最大值      |
| options    | 否   | map    | 聚合选项，跟新建 metric 选项一致                        |

### 5. 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6. CURL 示例说明
请求：
```
curl -u root:le201909 -H 'Content-Type:application/json' -X POST 172.16.345.14:9201/_rollup/ctsdb_rollup_task_test/update -d'
{
    "state":"running",
    "start_time": "1511918989",
    "end_time": "1512019765",
    "options": 
	{
    	"expire_day": 365
    }
}'
```

返回：
```
{
    "acknowledged": true,
    "message": "update rollup success"
}
```
