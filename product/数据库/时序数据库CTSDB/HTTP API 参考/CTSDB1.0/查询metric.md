
## 获取所有 metric 
### 请求地址
地址为实例的 IP 和 PORT，可从控制台获取到，例如10.13.20.15:9200。

### 请求路径和方法 
路径：`/_metrics`
方法：GET

### 请求参数 
无

### 请求内容 
无

### 返回内容 
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### CURL 示例说明
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X GET 172.16.345.14:9201/_metrics`

返回：

```
{
    "result": 
	{
	    "metrics": 
		[
		    "ctsdb_test",
		    "ctsdb_test1"
	    ]
    },
    "status": 200
}
```

## 获取特定 metric 

### 请求地址 
地址为实例的 IP 和 PORT，可从控制台获取到，例如10.13.20.15:9200。

### 请求路径和方法 
路径：`/_metric/${metric_name}`，`${metric_name}`为metric的名称。
方法：GET

### 请求参数
无

### 请求内容 
无

### 返回内容 
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

### CURL 示例说明
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X GET 172.16.345.14:9201/_metric/ctsdb_test`

返回：
```
{
    "result": 
	{
	    "ctsdb_test": 
		{
		    "tags": 
			{
		    	"region": "string"
		    },
		    "time": 
			{
			    "name": "timestamp",
			    "format": "epoch_second"
		    },
		    "fields": 
			{
		    	"cpuUsage": "float"
		    },
		    "options": 
			{
			    "expire_day": 7,
			    "refresh_interval": "10s",
			    "number_of_shards": 5
		    }
	    }
    },
    "status": 200
}
```
