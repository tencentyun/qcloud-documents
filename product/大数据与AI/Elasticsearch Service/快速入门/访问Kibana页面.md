## 访问Kibana页面

在 ES 控制台 》ES 集群列表 》操作，点击 Kibana，跳转到该集群对应的 Kibana 访问页面，页面访问需要登录，账号为：elastic，密码为用户创建集群时设置的 Kibana 密码。

### 1、存储数据（添加文档）
![](https://main.qcloudimg.com/raw/24aaf4d9d3cd0b93f0e6654c9a2652cf.png)


添加文档：

```
PUT china/city/wuhan  
{
"name":"武汉市","province":"湖北省江岸区沿江大道188号",
"lat":30.5952548577,
"lon":114.2999398195,
"x":6384,"level.level":2,
"level.range":19,
"level.name":"新一线城市",
"y":4231,
"cityNo":7
}
```

添加多个文档：

```
POST _bulk 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "beijing" } } 
{"name":"北京市","province":"北京市","lat":39.9031324643,"lon":116.4010433787,"x":6763,"level.range":4,"level.level":1,"level.name":"一线城市","y":6381,"cityNo":1} 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shanghai" } } 
{"name":"上海市","province":"上海市","lat":31.2319526784,"lon":121.469443249,"x":7779,"level.range":4,"level.level":1,"level.name":"一线城市","y":4409,"cityNo":2} 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "guangzhou" } } 
{"name":"广州市","province":"广东省越秀区吉祥路79号","lat":23.1317146641,"lon":113.2595185241,"x":6173,"level.range":4,"level.level":1,"level.name":"一线城市","y":2560,"cityNo":3} 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shenzhen" } } 
{"name":"深圳市","province":"广东省福田区新园路37号","lat":22.5455465546,"lon":114.0527779134,"x":6336,"level.range":4,"level.level":1,"level.name":"一线城市","y":2429,"cityNo":4} 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "chengdu" } } 
{"name":"成都市","province":"四川省锦江区红星路4段-88号-附1号","lat":30.6522796787,"lon":104.0725574128,"x":4387,"level.level":2,"level.range":19,"level.name":"新一线城市","y":4304,"cityNo":5} 
{ "index" : { "_index": "china", "_type" : "city", "_id" : "hangzhou" } } 
{"name":"杭州市","province":"浙江省拱墅区环城北路316号","lat":30.2753694112,"lon":120.1509063337,"x":7530,"level.level":2,"level.range":19,"level.name":"新一线城市","y":4182,"cityNo":6}
```

### 2、配置需要查看的索引

可以配置上文中刚添加过的 china 索引。

![](https://main.qcloudimg.com/raw/8992ef1d9ee0987fca0a58db0b84b8e0.png)

![](https://main.qcloudimg.com/raw/66a1724eecc7a52603e9fc0fdccd5da8.png)

### 3、查看索引字段（maping)

![](https://main.qcloudimg.com/raw/0c34ce6b7fc3677c57fc998e9adcc68d.png)

### 4、查看索引已经存储的文档

![](https://main.qcloudimg.com/raw/cc9b88b6742b0066cfa19e6e50fa1370.png)

Kibana其他使用方式，可以进一步了解[官方文档](https://www.elastic.co/guide/en/kibana/5.6/getting-started.html)。


