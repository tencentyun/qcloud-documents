### 请求地址 
地址为实例的 IP 和 PORT，可从控制台获取到，例如10.13.20.15:9200

### 请求路径和方法 
路径：`/_metric/${metric_name}/delete`，`${metric_name}`为 metric 的名称
方法：PUT

### 请求参数 
无

### 请求内容
| 参数名称        | 必选            | 类型            | 描述            |
|---------|---------|---------|---------|
| tags            | 否              | Array             | 枚举需要删除的维度字段，如`"tags": ["ip"]` |
| fields          | 否              | Array             | 枚举需要删除的指标字段，如`"fields": ["diskUsage"]` |
>!由于历史数据不可被修改，删除字段后metric信息不会立即变更，需要等待下一个子表产生。如果需要确认删除操作是否成功，可通过`GET /_metric/${metric_name}?v`接口进行确认。

### 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### JSON 示例说明
请求：`PUT /_metric/ctsdb_test1/delete`

请求数据：

	{
		"tags": ["ip"],        
		"fields": ["cpu"]   
	}
返回：

    {
	    "acknowledged": true,
	    "message": "update ctsdb_test1 metric success!"
    }
