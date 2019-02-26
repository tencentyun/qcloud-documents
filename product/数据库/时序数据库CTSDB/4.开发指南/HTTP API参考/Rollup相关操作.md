## 建立Rollup任务 ##
在海量数据场景下，业务系统每天甚至每小时会产生PB级别数据。而时序数据的最主要的特点就是海量性、时效性和趋势性，因此，通常情况下，使用数据的系统例如监控系统或数据分析系统通常只需要最近时间段内的高精度数据，而历史数据只需降精度（Downsampling）保存即可。用户可通过配置Rollup任务定时聚合历史数据保存至新的数据表。Rollup任务不仅能降精度保存历史数据，也能提高查询性能，降低存储成本。需要注意的是，Rollup任务会自动根据base_metric建立子表，继承父表的所有配置，如果指定options，会覆盖父表配置。
### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`为Rollup任务的名称<br/>
方法：PUT
### 3.请求参数 ###
无
### 4.请求内容 ###
| 参数名称        | 必选            | 类型            | 描述            |
|-----------------|-----------------|-----------------|-----------------|
| base_metric    | 是              | string          | Rollup依赖的metric名称（父表） |
| rollup_metric  | 是              | string          | Rollup产生的metric名称（子表）|
| base_rollup    | 否              | string          | 依赖的Rollup任务，任务执行前会检查相应时间段的依赖任务是否完成执行（可以不指定） |
| query           | 否              | string          | 过滤数据的查询条件，由很多个元素和操作对组成，例如`name:host AND type:max OR region:gz`|
| group_tags     | 是              | Array           | 进行聚合的维度列，可以包含多列 |
| copy_tags      | 否              | Array           | 不需要聚合的维度列，group_tags确定时，多条数据的copy_tags的值相同 |
| fields          | 是              | Map             | 指定聚合的名称、方法和字段，其字段只能选自 base_metric 里的fields字段，如果base_metric的fields为空，则无法设置rollup。例如：`{"cost_total":{"sum": {"field":"cost"}},"cpu_usage_avg":{ "avg": { "field":"cpu_usage"}}}`|
| interval        | 是              | string          | 聚合粒度，如1s、5minute、1h、1d等 |
| delay           | 否              | string          | 延迟执行时间，写入数据通常有一定的延时，避免丢失数据 |
| start_time     | 否              | string          | 开始时间，从该时间开始周期性执行Rollup，默认为当前时间 |
| end_time       | 否              | string          | 结束时间，到达该时间后不再调度 ，默认为时间戳最大值 |
| options         | 否              | map             | 聚合选项，跟新建metric选项一致 |

这里通过一个例子来说明group_tags与copy_tags：例如我们需要rollup机器的监控数据，为了区分具体的机器，会指定ip作为聚合的维度列，也将其加入group_tags，而对于region、host等，只要ip确定后，对于同一个ip的region与host是相同的，不需要作为聚合的维度列，只需要原封不动的拷贝到相应的聚合结果即可，因此将其加入copy_tags。

### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`POST /_rollup/ctsdb_rollup_task_test`

请求数据：

    {
	    "base_metric": "ctsdb_test",
	    "rollup_metric": "ctsdb_rollup_metric_test",
	    "query" : "cpuUsage:20",
	    "group_tags": ["ip"],
		"copy_tags": ["region", "host"], 
	    "fields": 
		{
		    "cpuUsage_total": 
			{
			    "sum": 
				{
			    	"field": "cpuUsage"
			    }
		    }
	    },
	    "interval": "1h",
	    "delay": "5m",
	    "start_time": "1511918989",
	    "options": 
		{
	    	"expire_day": 365
	    }
    }

返回：

    {
	    "acknowledged": true,
	    "message": "create rollup success"
    }

## 获取所有Rollup任务 ##
### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_rollups`<br/>
方法：GET
### 3.请求参数 ###
无
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`GET /_rollups`

返回：

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

## 获取某个Rollup任务 ##
### 1.请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`为Rollup任务的名称<br/>
方法：GET
### 3.请求参数 ###
指定v参数可以查看rollup的具体进度，返回结构中的@last_end_time为rollup最新进度。
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`GET /_rollup/rollup_jgq_6?v`

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
	      "end_time": 2147483647,
	      "@state": "running",
	      "@timestamp": 1512205503000,
	      "@last_end_time": 1512205200
	    }
	  },
	  "status": 200
	}

## 删除Rollup任务 ##
### 1.请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}`，`${rollup_task_name}`，为Rollup任务的名称<br/>
方法：DELETE
### 3.请求参数 ###
无
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### 6.JSON示例说明 ###
请求：`DELETE /_rollup/ctsdb_rollup_task_test`

返回：

    {
	    "acknowledged": true,
	    "message": "delete rollup success"
    }

## 启停Rollup任务 ##
### 1.请求地址 ###
地址为实例的IP和PORT，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_rollup/${rollup_task_name}/update`，`${rollup_task_name}`为Rollup任务的名称
方法：POST
### 3.请求参数 ###
无
### 4.请求内容 ###
--------

  |参数名称 |     必选 |  类型   |  描述|
|----|----|----|----|
 | state    |     是    | string  | running/pause|
  |start_time  | 否 |    string |  开始时间，从该时间开始周期性执行Rollup，默认为当前时间|
  |end_time   |  否  |   string|   结束时间，到达改时间后不再调度，默认为时间戳最大值|
  |options  |     否|     map |     聚合选项，跟新建metric选项一致|

### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### 6.JSON示例说明 ###
请求：`POST /_rollup/ctsdb_rollup_task_test/update`

请求数据：

    {
	    "state":"running",
	    "start_time": "1511918989",
	    "end_time": "1512019765",
	    "options": 
		{
	    	"expire_day": 365
	    }
    }

返回：

    {
	    "acknowledged": true,
	    "message": "update rollup success"
    }