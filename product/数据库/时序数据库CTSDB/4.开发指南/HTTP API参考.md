简介
====
CTSDB支持 HTTP 协议进行数据写入和查询等操作。提供的HTTP API是RESTful
API，对资源的请求方式是通过向资源对应的URI发送标准的 HTTP 请求，比如 GET
用来获取资源，POST 用来新建资源（也可以用于更新资源），PUT
用来更新资源，
DELETE 用来删除资源等。用户可以通过HTTP
API几乎可以实现所有的数据操作。CTSDB通过提供VPC网络隔离和访问时提供用户名和密码的身份认证方式来保证数据的安全性，通过
JSON格式的结构体进行数据交换，每个请求都会返回一个标准的 HTTP
响应状态码和响应内容。若操作失败，用户可以根据响应内容获取到具体错误信息。

**系统限制**

- Metric命名：允许使用小写英文字母、数字、_、-的组合，且不能以_或-开头
- Metric中tags和fields限制：允许大小写英文字母、数字、_、-的任意组合，字段总数限制1000个
- 批量写入metric时写入点限制：建议单次bulk条数在1000~5000之间，物理大小在1-15MB大小之间

新建metric
==========
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_metric/${metric_name}`，${metric_name}为新建的metric的名称
方法：PUT
注意：metric名称必须为小写字母，不能以下划线开头，并且不能包含逗号
请求参数
--------
无
请求内容
--------
| 参数名称        | 必选            | 类型            | 描述            |
|---------|---------|---------|---------|
| tags            | 是              | map             | 维度列，至少包含一个维度，支持的数据类型：text（带有分词、全文索引的字符串）、string（不分词的字符串）、long, integer, short, byte, double, float，date，boolean。格式如：{"region": "string","set":  "long","host": "string"} |
| time            | 是              | map             | 时间列相关配置，例如：{"name": "timestamp", "format":  "epoch_second"}   |
| fields          | 是              | map             | 指标列，为了节省空间，建议使用最适合实际业务使用的类型，支持的数据类型：string（字符串）、long, integer, short, byte,double, float，date，boolean。例如：{"cpu_usage":"float"}  |
| options         | 否              | map             | 常用的调优配置信息，例如：{"expire_day":7,"refresh_interval":"10s","number_of_shards":5,"number_of_replicas": 1,"rolling_period":1}  |
注意：

- time字段的name默认为timestamp，时间格式（format）完全兼容es的时间格式。
- options选项及解释如下：
	> expire_day：数据过期时间，过期后数据自动清理，缺省情况下-1（代表永不过期）
	> 	refresh_interval：数据刷新频率，写入的数据从内存刷新到磁盘后可查询。认为10秒
	> 	number_of_shards：表分片数，小表可以忽略，大表按照一个分片至多25G设置分片数，默认为3
	> 	number_of_replicas：副本数，例如一主一副为1，缺省为1
	> 	rolling_period：子表时长（单位：天），CTSDB存储数据时，为了方便做数据过期和提高查询效率，根据特定时间间隔划分子表，缺省情况下由数据过期时间决定，下面具体说明缺省子表时长和过期时间的关系
  
	|过期时间 |    子表时长|
	|---------|---------|
	|  ≤15天     |       1天|
	 | >15天, ≤3个月|   7天|
	 | ＞3个月|          30天|
	 | 永不过期 |        无穷大|

返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`POST /_metric/ctsdb_test`

请求数据：
    
    {
    "tags":{
    "region":"string"
    },
    "time":{
    "name":"timestamp",
    "format":"epoch_second"
    },
    "fields":{
    "cpuUsage":"float"
    },
    "options":{
    "expire_day":7,
    "refresh_intercal":"10s",
    "number_of_shards":5
    }
    }

成功的返回：

	{
    "acknowledged": true,
    "message": "create ctsdb metric ctsdb_test success!"
    }

失败的返回：

    {
    "error": {
    "reason": "table ctsdb_test already exist",
    "type": "metric_exception"
    },
    "status": 201
    }

获取所有metric
==============
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_metrics`
方法：GET
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`GET /_metrics`

返回：

    {
    "result": {
    "metrics": [
    "ctsdb_test",
    "ctsdb_test1"
    ]
    },
    "status": 200
    }

获取特定metric
==============
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_metric/${metric_name}`，${metric_name}为metric的名称
方法：GET
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`GET /_metric/ctsdb_test`

返回：

    {
    "result": {
    "ctsdb_test": {
    "tags": {
    "region": "string"
    },
    "time": {
    "name": "timestamp",
    "format": "epoch_second"
    },
    "fields": {
    "cpuUsage": "float"
    },
    "options": {
    "expire_day": 7,
    "refresh_intercal": "10s",
    "number_of_shards": 5
    }
    }
    },
    "status": 200
    }
    
删除metric
==========
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_metric/${metric_name}`，${metric_name}为需要删除的metric的名称
方法：DELETE
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`DELETE /_metric/ctsdb_test1`

返回：

    {
    "acknowledged": true,
    "message": "delete metric ctsdb_test1 success!"
    }

更新metric
==========
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_metric/${metric_name}/update`，${metric_name}为metric的名称
方法：PUT
请求参数
--------
无
请求内容
--------
请求的参数options为map类型的，必填，至少有一个属性。属性列举如下：

| 属性名称        | 必选            | 类型            | 描述            |
|---------|---------|---------|---------|
| expire_day     | 否              | string          | 数据过期时间，过期后数据自动清理，缺省情况下永不过期 |
| refresh_interval | 否              | string          | 数据刷新频率，写入的数据从内存刷新到磁盘后可查询，默认为10秒 |
| number_of_shards | 否              | string          | 表分片数，小表可忽略，大表按照一个分片至多25G设置分片数，默认为3 |
| number_of_replicas | 否              | string          | 副本数，例如一主一副为1，默认为1 |
| rolling_period | 否              | string          | 子表时长（单位：天），为了方便做数据过期清理和提高查询效率，根据特定时间间隔划分子表，缺省情况下由数据过期时间决定 |

返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`PUT /_metric/ctsdb_test/update`

请求数据：

    "options":{
    {
    "expire_day":15,
    "number_of_shards":10
    }
    }

返回：

    {
    "acknowledged": true,
    "message": "update ctsdb metric test111 success!"
    }

写入数据
========
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：
写入单个metric时为/${metric_name}/doc/_bulk，${metric_name}为metric的名称，批量写入metric时为/_bulk
方法：PUT
注意：doc关键字为写入数据的_type，为了便于以后系统做解析和升级，请务必加上doc关键字
请求参数
--------
无
请求内容
--------
写入单个metric和批量写入metric都需要一种NDJSON格式的结构数据，类似于如下结构：
元数据及操作数据n
需要写入的数据n
....
元数据及操作数据n
需要写入的数据n
注意：元数据及操作数据的格式类似于{ "index" : { "_index" :
"test", "_type" : "doc", "_id" : "1" }
}写入数据的格式类似于{ "field1" : "value1" ，"field2" : "value2"
}，请求体中最后一行需要加换行符
返回内容
--------
需要通过error字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误内容在error字段内。注意：若请求成功，但是errors（注意不是error）字段非等于false，则该errors字段具体指出写入失败的具体数据。
JSON示例说明
------------
**写入单个metric**

请求：`PUT /ctsdb_test/doc/_bulk`

请求数据：
    
    {"index":{}}
    {"region":"sh","cpuUsage":1.5,"timestamp":1505294650}

返回：

    {
    "took": 65,
    "errors": false,
    "items": [
    {
    "index": {
    "_index": "test@144000000_30",
    "_type": "doc",
    "_id": "AV_8cKnEUAkC9PF9L-2k",
    "_version": 1,
    "result": "created",
    "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
    },
    "created": true,
    "status": 201
    }
    }
    ]
    }

**写入多个metric**

请求：PUT /_bulk

请求数据：

    {"index":{"_index" : "ctsdb_test", "_type" : "doc" }}
    {"region":"sh","cpuUsage":2.5,"timestamp":1505294654}
    {"index":{"_index" : "ctsdb_test2", "_type" : "doc" }}
    {"region":"sh","cpuUsage":2.0,"timestamp":1505294654}

返回：

    {
    "took": 134,
    "errors": false,
    "items": [
    {
    "index": {
    "_index": "ctsdb_test@1505232000000_1",
    "_type": "doc",
    "_id": "AV_8eeo_UAkC9PF9L-2q",
    "_version": 1,
    "result": "created",
    "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
    },
    "created": true,
    "status": 201
    }
    },
    {
    "index": {
    "_index": "ctsdb_test2@1505232000000_1",
    "_type": "doc",
    "_id": "AV_8eeo_UAkC9PF9L-2r",
    "_version": 1,
    "result": "created",
    "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
    },
    "created": true,
    "status": 201
    }
    }
    ]
    }

查询数据
========
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`${metric_name}/_search`，${metric_name}为metric的名称
方法：GET
请求参数
--------
无
请求内容
--------
查询主要有普通查询和聚合查询，查询请求完全兼容es
api，具体请求内容请参照示例
返回内容
--------
需要通过error字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
### 普通查询

请求：`GET /ctsdb_test/_search`

请求数据：

    {
    "query": {
    "bool": {
    "filter": {
    "match_all": {}
    }
    }
    },
    "docvalue_fields": ["cpuUsage","timestamp"]
    }

注意：需要指定docvalue_fields字段来指明查询结果显示的字段，否则查询结果不包含fields字段。

返回：

    {
    "took": 4,
    "timed_out": false,
    "_shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
    },
    "hits": {
    "total": 4,
    "max_score": 1,
    "hits": [
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8s4uDUAkC9PF9L-2x",
    "_score": 1,
    "_routing": "100",
    "fields": {
    "cpuUsage": [
    10
    ],
    "timestamp": [
    1511772857000
    ]
    }
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tIMAUAkC9PF9L-2y",
    "_score": 1,
    "_routing": "100",
    "fields": {
    "cpuUsage": [
    20
    ],
    "timestamp": [
    1511773057000
    ]
    }
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tcbeUAkC9PF9L-2z",
    "_score": 1,
    "_routing": "100",
    "fields": {
    "cpuUsage": [
    20
    ],
    "timestamp": [
    1511773144000
    ]
    }
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_9CAo5UAkC9PF9L-20",
    "_score": 1,
    "_routing": "100",
    "fields": {
    "cpuUsage": [
    20
    ],
    "timestamp": [
    1511778531000
    ]
    }
    }
    ]
    }
    }

### 聚合查询

**普通聚合**

请求：`GET /ctsdb_test/_search`

请求数据：

    {
    "size": 20,
    "query": {
    "bool": {
    "filter": {
    "range": {
    "timestamp": {
    "gte": "2017-11-27T02:53:57Z",
    "lte": "2017-11-28T05:53:57Z",
    "format": "strict_date_optional_time",
    "time_zone": "+08:00"
    }
    }
    }
    }
    },
    "aggs": {
    "myname": {
    "max":{
    "field": "cpuUsage"
    }
    }
    }
    }

返回：

    {
    "took": 1,
    "timed_out": false,
    "_shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
    },
    "hits": {
    "total": 4,
    "max_score": 0,
    "hits": [
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8s4uDUAkC9PF9L-2x",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tIMAUAkC9PF9L-2y",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tcbeUAkC9PF9L-2z",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_9CAo5UAkC9PF9L-20",
    "_score": 0,
    "_routing": "100"
    }
    ]
    },
    "aggregations": {
    "myname": {
    "value": 20
    }
    }
    }

**Percentiles聚合**

请求：`GET /ctsdb_test/_search`

请求数据：

    {
    "size": 20,
    "query": {
    "bool": {
    "filter": {
    "range": {
    "timestamp": {
    "gte": "2017-11-27T02:53:57Z",
    "lte": "2017-11-28T05:53:57Z",
    "format": "strict_date_optional_time",
    "time_zone": "+08:00"
    }
    }
    }
    }
    },
    "aggs": {
    "myname": {
    "percentiles":{
    "field": "cpuUsage",
    "percents": [
    1,
    5,
    25,
    50,
    75,
    95,
    99
    ]
    }
    }
    }
    }

返回：

    {
    "took": 3,
    "timed_out": false,
    "_shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
    },
    "hits": {
    "total": 4,
    "max_score": 0,
    "hits": [
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8s4uDUAkC9PF9L-2x",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tIMAUAkC9PF9L-2y",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tcbeUAkC9PF9L-2z",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_9CAo5UAkC9PF9L-20",
    "_score": 0,
    "_routing": "100"
    }
    ]
    },
    "aggregations": {
    "myname": {
    "values": {
    "1.0": 10.299999999999999,
    "5.0": 11.5,
    "25.0": 17.5,
    "50.0": 20,
    "75.0": 20,
    "95.0": 20,
    "99.0": 20
    }
    }
    }
    }

**Cardinality聚合**

请求：`GET /ctsdb_test/_search`

请求数据：

    {
    "size": 20,
    "query": {
    "bool": {
    "filter": {
    "range": {
    "timestamp": {
    "gte": "2017-11-27T02:53:57Z",
    "lte": "2017-11-28T05:53:57Z",
    "format": "strict_date_optional_time",
    "time_zone": "+08:00"
    }
    }
    }
    }
    },
    "aggs": {
    "myname": {
    "cardinality":{
    "field": "cpuUsage"
    }
    }
    }
    }

返回：

    {
    "took": 3,
    "timed_out": false,
    "_shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
    },
    "hits": {
    "total": 4,
    "max_score": 0,
    "hits": [
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8s4uDUAkC9PF9L-2x",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tIMAUAkC9PF9L-2y",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tcbeUAkC9PF9L-2z",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_9CAo5UAkC9PF9L-20",
    "_score": 0,
    "_routing": "100"
    }
    ]
    },
    "aggregations": {
    "myname": {
    "value": 2
    }
    }
    }

**嵌套聚合**

请求：`GET /ctsdb_test/_search`

请求数据：

    {
    "size": 20,
    "query": {
    "bool": {
    "filter": {
    "range": {
    "timestamp": {
    "gte": "2017-11-27T02:53:57Z",
    "lte": "2017-11-28T05:53:57Z",
    "format": "strict_date_optional_time",
    "time_zone": "+08:00"
    }
    }
    }
    }
    },
    "aggs": {
    "NAME1": {
    "date_histogram": {
    "field": "timestamp",
    "interval": "quarter"
    },
    "aggs": {
    "myname": {
    "max": {
    "field": "cpuUsage"
    }
    }
    }
    }
    }
    }

返回：

    {
    "took": 1,
    "timed_out": false,
    "_shards": {
    "total": 10,
    "successful": 10,
    "skipped": 0,
    "failed": 0
    },
    "hits": {
    "total": 4,
    "max_score": 0,
    "hits": [
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8s4uDUAkC9PF9L-2x",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tIMAUAkC9PF9L-2y",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_8tcbeUAkC9PF9L-2z",
    "_score": 0,
    "_routing": "100"
    },
    {
    "_index": "ctsdb_test@1511712000000_1",
    "_type": "doc",
    "_id": "AV_9CAo5UAkC9PF9L-20",
    "_score": 0,
    "_routing": "100"
    }
    ]
    },
    "aggregations": {
    "NAME1": {
    "buckets": [
    {
    "key_as_string": "1506816000",
    "key": 1506816000000,
    "doc_count": 4,
    "myname": {
    "value": 20
    }
    }
    ]
    }
    }
    }

建立Rollup任务
==============
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}为rollup任务的名称
方法：PUT
请求参数
--------
无
请求内容
--------
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

返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
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

获取所有Rollup任务
==================
请求地址
--------
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_rollups`
方法：GET
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
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

获取某个Rollup任务
==================
请求地址
--------
地址为实例的IP和PORT，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}为rollup任务的名称
方法：GET
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
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

删除Rollup任务
==============
请求地址
--------
地址为实例的IP和PORT，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_rollup/${rollup_task_name}`，${rollup_task_name}，为rollup任务的名称
方法：DELETE
请求参数
--------
无
请求内容
--------
无
返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
JSON示例说明
------------
请求：`DELETE /_rollup/ctsdb_rollup_task_test`

返回：

    {
    "acknowledged": true,
    "message": "update rollup success"
    }

启停Rollup任务
==============
请求地址
--------
地址为实例的IP和PORT，例如10.13.20.15:9200
请求路径和方法
--------------
路径：`/_rollup/${rollup_task_name}/update`，${rollup_task_name}为rollup任务的名称
方法：POST
请求参数
--------
无
请求内容
--------

  |参数名称 |     必选 |  类型   |  描述|
|----|----|----|----|
 | state    |     是    | string  | running/pause|
  |start_time  | 否 |    string |  开始时间：从该时间开始周期性执行rollup，默认为当前时间|
  |end_time   |  否  |   string|   结束时间：到达改时间后不再调度，默认为时间戳最大值|
  |options  |     否|     map |     聚合选项，跟新建metric选项一致|

返回内容
--------
需要通过'error'字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。

JSON示例说明
------------
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