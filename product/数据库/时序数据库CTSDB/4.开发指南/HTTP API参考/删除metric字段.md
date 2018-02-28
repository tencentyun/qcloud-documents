### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_metric/${metric_name}/delete`，`${metric_name}`为metric的名称<br>方法：PUT
### 3.请求参数 ###
无
### 4.请求内容 ###
| 参数名称        | 必选            | 类型            | 描述            |
|---------|---------|---------|---------|
| tags            | 否              | Array             | 枚举需要删除的维度字段，如`"tags": ["ip"]` |
| fields          | 否              | Array             | 枚举需要删除的指标字段，如`"fields": ["diskUsage"]` |
> 注意：
> 由于历史数据不可被修改，删除字段后metric信息不会立即变更，需要等待下一个子表产生。如果需要确认删除操作是否成功，可通过`GET /_metric/${metric_name}?v`接口进行确认。<br>

### 5.返回内容 ###
需要通过error字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### 6.JSON示例说明 ###
请求：`PUT /_metric/ctsdb_test1/delete`<br>请求数据：

	{
		"tags": ["ip"],        
		"fields": ["cpu"]   
	}
返回：

    {
	    "acknowledged": true,
	    "message": "update ctsdb_test1 metric success!"
    }
