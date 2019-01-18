### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_metric/${metric_name}/update`，`${metric_name}`为metric的名称<br>
方法：PUT
### 3.请求参数 ###
无
### 4.请求内容 ###
字段tags、time、fields、options均为map类型的，选填，格式请参考API [新建metric](https://cloud.tencent.com/document/product/652/13604)。具体要求如下：<br>
tags：允许新增维度字段和修改已存在的维度字段类型，不会删除原有字段<br>
time：name不能修改，format允许修改<br>
fields：允许新增指标字段和修改已存在的指标字段类型，不会删除原有字段<br>
options属性列举如下：

| 属性名称        | 必选            | 类型            | 描述            |
|---------|---------|---------|---------|
| expire_day     | 否              | integer          | 数据过期时间，取值范围为非零整数，过期后数据自动清理，缺省情况下永不过期 |
| refresh_interval | 否              | string          | 数据刷新频率，写入的数据从内存刷新到磁盘后可查询，默认为10秒 |
| number_of_shards | 否              | integer          | 表分片数，取值范围为正整数，小表可忽略，大表按照一个分片至多25G设置分片数，默认为3 |
| number_of_replicas | 否              | integer          | 副本数，取值范围为非负整数，例如一主一副为1，默认为1 |
| rolling_period | 否              | integer          | 子表时长（单位：天），取值范围为非零整数，为了方便做数据过期清理和提高查询效率，根据特定时间间隔划分子表，缺省情况下由数据过期时间决定 |
| max_string_length | 否 | integer| 自定义字符串类型的值最大可支持的长度，取值范围为正整数，最大为2^31 - 1，默认为256 |
| default_date_format | 否              | string          | 自定义维度列和指标列 date类型的格式，默认为 strict_date_optional_time或epoch_millis |
| indexed_fields | 否 | array | 指定指标列中需要保留索引的字段，可指定多个，以数组形式指定 |
| default_type | 否              | string          | 指定新增字段的默认类型。可选项为tag、field，系统默认值为tag。 |
> 注意：<br>
> 1.由于历史数据不可被修改，更新字段后metric信息不会立即变更，需要等待下一个子表产生。如果需要确认更新操作是否成功，可通过`GET /_metric/${metric_name}?v`接口进行确认。<br>
> 2.只有为short、integer、float的字段才允许修改类型。其中short类型可被修改为integer和long类型；integer类型可被修改为long类型；float类型可被修改为double类型。

### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`PUT /_metric/ctsdb_test/update`<br>
请求数据：

	{
		"tags":{
			"set":"string"
		},
		"time":{
			"name":"timestamp",
			"format":"epoch_second"
		},
		"fields":{
			"diskUsage":"float"
		},
		"options":{
		    "expire_day":15,
		    "number_of_shards":10
	    }
    }
返回：

    {
	    "acknowledged": true,
	    "message": "update ctsdb metric test111 success!"
    }
