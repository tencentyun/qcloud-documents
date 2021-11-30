Elasticsearch 提供了功能全面的 RESTful API 与集群交互，详情请参见 Elasticsearch 官方的 [API 文档](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/index.html)。

腾讯云 ES 构建在用户 VPC 内，用户可以通过位于同一 VPC 下的 CVM 作为客户端访问 ES 集群。可通过**内网访问**和**外网访问**两种方式访问 ES 集群，**外网访问存在安全风险**，需谨慎开启。

>?
> - 外网访问仅用于开发调试，因系统会限制调用频次，所以不能用于生产环境。
> - 当前 ES 公网访问不计费，带宽10M。

## 查看内外网访问地址
在 [集群列表页](https://console.cloud.tencent.com/es)，单击集群 **ID/名称**进入详情页：
- 对于内网地址，在基础配置中可直接查看。
- 对于外网地址，出于安全考虑默认是关闭的。对于已开启 [ES 集群用户登录认证](https://cloud.tencent.com/document/product/845/42868) 的集群，支持开启公网地址。开启公网访问可能会为集群引入安全风险，同时也将允许通过 API 直接访问、操作甚至删除在 ElasticSearch 集群中的数据，请谨慎开启。

![基本配置](https://main.qcloudimg.com/raw/be3596330518dad66734369d62501beb.png)

## 测试访问
可通过 curl 的方式测试访问集群，不支持通过 ping 的方式测试连通性。

### 测试服务是否可访问
>?对于已开启 [ES 集群用户登录认证](https://cloud.tencent.com/document/product/845/42868) 的集群，登录时需要用户名和密码认证，具体规则为`curl action -u user:password host ...`，需要将 user、password 替换为自己实际的用户名和密码，将 host 替换为自己的 IP。

下面将以内网地址访问来演示各访问操作。输入命令：
```
curl -XGET http://10.0.17.2:9200
若开启了ES集群用户登录认证，请注意输入用户名密码
curl -XGET -u user:password http://10.0.17.2:9200
```
返回如下，表示集群访问正常，具体参数的值会根据集群的版本有所不同：
```
{
"name": "15589826570000*****",
"cluster_name": "es-******",
"cluster_uuid": "NGIm1M_zRw-L3o_gH****",
"version": {
  "number": "6.4.3",
  "build_flavor": "default",
  "build_type": "zip",
  "build_hash": "fe40335",
  "build_date": "2019-05-17T14:22:47.286024Z",
  "build_snapshot": false,
  "lucene_version": "7.4.0",
  "minimum_wire_compatibility_version": "5.6.0",
  "minimum_index_compatibility_version": "5.0.0"
},
"tagline": "You Know, for Search"
}
```

## 创建文档
### 创建单个文档
- 若集群未开启用户登录认证， 输入命令行：
```
curl -XPUT http://10.0.0.2:9200/china/_doc/beijing -H 'Content-Type: application/json' -d'
  {
  "name":"北京市",
  "province":"北京市",
  "lat":39.9031324643,
  "lon":116.4010433787,
  "x":6763,
  "level.range":4,
  "level.level":1,
  "level.name":"一线城市",
  "y":6381,
  "cityNo":1
  }
  '
```
- 若集群已开启用户登录认证，需要将下文中的 user、password 替换为自己集群实际的用户名和密码。输入命令行：
```
curl -XPUT -u user:password http://10.0.0.2:9200/china/_doc/beijing -H 'Content-Type: application/json' -d'
  {
  "name":"北京市",
  "province":"北京市",
  "lat":39.9031324643,
  "lon":116.4010433787,
  "x":6763,
  "level.range":4,
  "level.level":1,
  "level.name":"一线城市",
  "y":6381,
  "cityNo":1
  }
  '
```
  响应如下：
```
{
  "_index":"china",
  "_type":"_doc",
  "_id":"beijing",
  "_version":1,
  "result":"created",
  "_shards":{
      "total":2,
      "successful":1,
      "failed":0
  },
  "created":true
  }
```


### 创建多个文档

输入命令行：
```
curl -XPOST http://10.0.0.2:9200/_bulk -H 'Content-Type: application/json' -d'
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "beijing" } }
{"name":"北京市","province":"北京市","lat":39.9031324643,"lon":116.4010433787,"x":6763,"level.range":4,"level.level":1,"level.name":"一线城市","y":6381,"cityNo":1}
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "shanghai" } }
{"name":"上海市","province":"上海市","lat":31.2319526784,"lon":121.469443249,"x":7779,"level.range":4,"level.level":1,"level.name":"一线城市","y":4409,"cityNo":2}
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "guangzhou" } }
{"name":"广州市","province":"广东省越秀区吉祥路79号","lat":23.1317146641,"lon":113.2595185241,"x":6173,"level.range":4,"level.level":1,"level.name":"一线城市","y":2560,"cityNo":3}
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "shenzhen" } }
{"name":"深圳市","province":"广东省福田区新园路37号","lat":22.5455465546,"lon":114.0527779134,"x":6336,"level.range":4,"level.level":1,"level.name":"一线城市","y":2429,"cityNo":4}
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "chengdu" } }
{"name":"成都市","province":"四川省锦江区红星路4段-88号-附1号","lat":30.6522796787,"lon":104.0725574128,"x":4387,"level.level":2,"level.range":19,"level.name":"新一线城市","y":4304,"cityNo":5}
{ "index" : { "_index": "china", "_type" : "_doc", "_id" : "hangzhou" } }
{"name":"杭州市","province":"浙江省拱墅区环城北路316号","lat":30.2753694112,"lon":120.1509063337,"x":7530,"level.level":2,"level.range":19,"level.name":"新一线城市","y":4182,"cityNo":6}
'
```
响应如下：
```
"took":9,"errors":false,"items":[{"index":{"_index":"china","_type":"_doc","_id":"beijing","_version":4,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"_doc","_id":"shanghai","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"_doc","_id":"guangzhou","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"_doc","_id":"shenzhen","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"_doc","_id":"chengdu","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"_doc","_id":"hangzhou","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}}]
```

## 更新文档
重复上文创建单个文档的输入代码，即可更新指定 ID `beijing`的文档。 响应如下：
```
{"_index":"china","_type":"_doc","_id":"beijing","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false}
```

## 查询文档
### 查询指定 ID
输入命令行：
```
curl -XGET 'http://10.0.0.2:9200/china/_doc/beijing?pretty' -H 'Content-Type: application/json' 
```
响应如下：
```
{
"_index" : "china",
"_type" : "_doc",
"_id" : "beijing",
"_version" : 4,
"found" : true,
"_source" : {
  "name" : "北京市",
  "province" : "北京市",
  "lat" : 39.9031324643,
  "lon" : 116.4010433787,
  "x" : 6763,
  "level.range" : 4,
  "level.level" : 1,
  "level.name" : "一线城市",
  "y" : 6381,
  "cityNo" : 1
}
}
```

### 查询某个索引
输入命令行：
```
curl -XGET 'http://10.0.0.2:9200/china/_search?pretty' -H 'Content-Type: application/json' 
```
响应如下：
```
{
"took" : 0,
"timed_out" : false,
"_shards" : {
  "total" : 5,
  "successful" : 5,
  "skipped" : 0,
  "failed" : 0
},
"hits" : {
  "total" : 6,
  "max_score" : 1.0,
  "hits" : [
    {
      "_index" : "china",
      "_type" : "_doc",
      "_id" : "guangzhou",
      "_score" : 1.0,
      "_source" : {
        "name" : "广州市",
        "province" : "广东省越秀区吉祥路79号",
        "lat" : 23.1317146641,
        "lon" : 113.2595185241,
        "x" : 6173,
        "level.range" : 4,
        "level.level" : 1,
        "level.name" : "一线城市",
        "y" : 2560,
        "cityNo" : 3
      }
    }]
  },
  ......
}   
```

### 复杂查询
模拟 SQL：
```
select * from china where level.level=2
curl -XGET http://10.0.0.2:9200/china/_search?pretty -H 'Content-Type: application/json' -d'
{
  "query" : {
      "constant_score" : { 
          "filter" : {
              "term" : { 
                  "level.level" : 2
              }
          }
      }
  }
}'
```
响应如下：
```
{
"took" : 2,
"timed_out" : false,
"_shards" : {
  "total" : 5,
  "successful" : 5,
  "skipped" : 0,
  "failed" : 0
},
"hits" : {
  "total" : 2,
  "max_score" : 1.0,
  "hits" : [
    {
      "_index" : "china",
      "_type" : "_doc",
      "_id" : "chengdu",
      "_score" : 1.0,
      "_source" : {
        "name" : "成都市",
        "province" : "四川省锦江区红星路4段-88号-附1号",
        "lat" : 30.6522796787,
        "lon" : 104.0725574128,
        "x" : 4387,
        "level.level" : 2,
        "level.range" : 19,
        "level.name" : "新一线城市",
        "y" : 4304,
        "cityNo" : 5
      }
    },
    {
      "_index" : "china",
      "_type" : "_doc",
      "_id" : "hangzhou",
      "_score" : 1.0,
      "_source" : {
        "name" : "杭州市",
        "province" : "浙江省拱墅区环城北路316号",
        "lat" : 30.2753694112,
        "lon" : 120.1509063337,
        "x" : 7530,
        "level.level" : 2,
        "level.range" : 19,
        "level.name" : "新一线城市",
        "y" : 4182,
        "cityNo" : 6
      }
    }
  ]
}
}
```

### 聚合查询
模拟 SQL：
```
select level.level, count(1) from city group by level.level
curl -XGET http://10.0.0.2:9200/china/_search?pretty -H 'Content-Type: application/json' -d'
{
  "size" : 0,
  "aggs" : { 
      "city_level" : { 
          "terms" : { 
            "field" : "level.level"
          }
      }
  }
}'
```
响应如下：
```
{
"took" : 10,
"timed_out" : false,
"_shards" : {
  "total" : 5,
  "successful" : 5,
  "skipped" : 0,
  "failed" : 0
},
"hits" : {
  "total" : 7,
  "max_score" : 0.0,
  "hits" : [ ]
},
"aggregations" : {
  "city_level" : {
    "doc_count_error_upper_bound" : 0,
    "sum_other_doc_count" : 0,
    "buckets" : [
      {
        "key" : 1,
        "doc_count" : 4
      },
      {
        "key" : 2,
        "doc_count" : 3
      }
    ]
  }
}
}
```

## 删除文档
### 删除单个文档
输入命令行：
```
curl -XDELETE 'http://10.0.0.2:9200/china/_doc/beijing?pretty' -H 'Content-Type: application/json' 
```
响应如下：
```
{
"found" : true,
"_index" : "china",
"_type" : "_doc",
"_id" : "beijing",
"_version" : 5,
"result" : "deleted",
"_shards" : {
  "total" : 2,
  "successful" : 2,
  "failed" : 0
}
}
```

### 删除类型
```
curl -XDELETE 'http://10.0.0.2:9200/china/_doc?pretty' -H 'Content-Type: application/json' 
```

### 删除索引
```
curl -XDELETE 'http://10.0.0.2:9200/china?pretty' -H 'Content-Type: application
```
