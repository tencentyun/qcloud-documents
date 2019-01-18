## 获取所有metric ##
### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_metrics`<br/>
方法：GET
### 3.请求参数 ###
无
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`GET /_metrics`

返回：

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

## 获取特定metric ##
### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_metric/${metric_name}`，`${metric_name}`为metric的名称<br/>
方法：GET
### 3.请求参数 ###
无
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。
### 6.JSON示例说明 ###
请求：`GET /_metric/ctsdb_test`

返回：

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
    
