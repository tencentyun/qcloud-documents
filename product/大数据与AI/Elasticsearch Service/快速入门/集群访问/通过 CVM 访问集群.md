腾讯云 ES 构建在用户 VPC 内，用户可以通过位于同一 VPC 下的 CVM 作为客户端，访问 ES 集群。ES 集群在 VPC 内的内网地址，可以在集群详情页查看。

## 查看内网地址

在列表页集群 ID>详情页基础配置中可查看内网地址。

![基本配置](https://main.qcloudimg.com/raw/3fa85f997895ed2e21b1abe9f7c1f9ee.png)  


## 创建文档
### 创建单个文档
输入命令行：
```
curl -XPUT http://10.0.0.2:9200/china/city/beijing -d'
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
    "_type":"city",
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
curl -XPOST http://10.0.0.2:9200/_bulk -d'
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
'
```

响应如下：
```
"took":9,"errors":false,"items":[{"index":{"_index":"china","_type":"city","_id":"beijing","_version":4,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"shanghai","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"guangzhou","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"city","_id":"shenzhen","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"city","_id":"chengdu","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"hangzhou","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}}]}
```

## 更新文档
重复上文创建单个文档的输入，就会更新指定 ID beijing 的文档。
响应如下：
```
{"_index":"china","_type":"city","_id":"beijing","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false}
```


## 查询文档
### 查询指定 ID
输入命令行：
```
curl -XGET 'http://10.0.0.2:9200/china/city/beijing?pretty'
```
响应如下：
```
{
  "_index" : "china",
  "_type" : "city",
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
curl -XGET 'http://10.0.0.2:9200/china/city/_search?pretty'
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
        "_type" : "city",
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
      }
    },
    ......
}
    
```

### 复杂查询
模拟 SQL：
```
select * from city where level.level=2
```

```
curl -XGET http://10.0.0.2:9200/china/city/_search?pretty -d'
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
        "_type" : "city",
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
        "_type" : "city",
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
```


```
curl -XGET http://10.0.0.2:9200/china/city/_search?pretty -d'
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
curl -XDELETE 'http://10.0.0.2:9200/china/city/beijing?pretty'
```

响应如下：
```
{
  "found" : true,
  "_index" : "china",
  "_type" : "city",
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
curl -XDELETE 'http://10.0.0.2:9200/china/city?pretty'
```
### 删除索引
```
curl -XDELETE 'http://10.0.0.2:9200/china?pretty'
```
