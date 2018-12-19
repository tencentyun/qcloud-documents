### 1.请求地址 ###
地址为实例的IP和PORT，可从控制台获取到，例如10.13.20.15:9200
### 2.请求路径和方法 ###
路径：`/_metric/${metric_name}`，`${metric_name}`为需要删除的metric的名称<br/>
方法：DELETE
### 3.请求参数 ###
无
### 4.请求内容 ###
无
### 5.返回内容 ###
需要通过error字段判断请求是否成功，若返回内容有error字段则请求失败，具体错误详情请参照error字段描述。
### 6.JSON示例说明 ###
请求：`DELETE /_metric/ctsdb_test1`<br/>
返回：

    {
	    "acknowledged": true,
	    "message": "delete metric ctsdb_test1 success!"
    }
