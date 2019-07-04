Tencent Cloud ES is built on your VPC, and you can access the ES cluster by using a CVM in the same VPC as the client. The private network address of the ES cluster in your VPC can be viewed on the cluster details page.

## View Private Network Addresses

You can view the private network address in Basic Configuration of the cluster details page by clicking the cluster ID in the list page.

![Basic Configuration](https://main.qcloudimg.com/raw/3fa85f997895ed2e21b1abe9f7c1f9ee.png)  


## Create Documents
### Create a single document
Enter the following command:
```
curl -XPUT http://10.0.0.2:9200/china/city/beijing -d'
{
"name":"Beijing",
"province":"Beijing",
"lat":39.9031324643,
"lon":116.4010433787,
"x":6763,
"level.range":4,
"level.level":1,
"level.name":"first-tier city",
"y":6381,
"cityNo":1
}
'
```

The response is:

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

### Create multiple documents:
Enter the following command:
```
curl -XPOST http://10.0.0.2:9200/_bulk -d'
{ "index" : { "_index": "china", "_type" : "city", "_id" : "beijing" } }
{"name":"Beijing","province":"Beijing","lat":39.9031324643,"lon":116.4010433787,"x":6763,"level.range":4,"level.level":1,"level.name":"first-tier city","y":6381,"cityNo":1}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shanghai" } }
{"name":"Shanghai","province":"Shanghai","lat":31.2319526784,"lon":121.469443249,"x":7779,"level.range":4,"level.level":1,"level.name":"first-tier city","y":4409,"cityNo":2}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "guangzhou" } }
{"name":"Guangzhou","province":"No 79, Jixiang Road, Yuexiu District, Guangdong Province","lat":23.1317146641,"lon":113.2595185241,"x":6173,"level.range":4,"level.level":1,"level.name":"first-tier city","y":2560,"cityNo":3}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shenzhen" } }
{"name":"Shenzhen","province":"No 37, Xinyuan Road, Futian District, Guangdong Province","lat":22.5455465546,"lon":114.0527779134,"x":6336,"level.range":4,"level.level":1,"level.name":"first-tier city ","y":2429,"cityNo":4}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "chengdu" } }
{"name":"Chengdu","province":"No 88-1, 4th Section of Hongxing Road, Jinjiang District, Sichuan Province","lat":30.6522796787,"lon":104.0725574128,"x":4387,"level.level":2,"level.range":19,"level.name":"new first-tier city","y":4304,"cityNo":5}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "hangzhou" } }
{"name":"Hangzhou","province":"No 316, Huancheng North Road, Gongshu District, Zhejiang Province","lat":30.2753694112,"lon":120.1509063337,"x":7530,"level.level":2,"level.range":19,"level.name":"new first-tier city","y":4182,"cityNo":6}
'
```

The response is:

```
"took":9,"errors":false,"items":[{"index":{"_index":"china","_type":"city","_id":"beijing","_version":4,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"shanghai","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"guangzhou","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"city","_id":"shenzhen","_version":1,"result":"created","_shards":{"total":2,"successful":2,"failed":0},"created":true,"status":201}},{"index":{"_index":"china","_type":"city","_id":"chengdu","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}},{"index":{"_index":"china","_type":"city","_id":"hangzhou","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false,"status":200}}]}
```

## Update Documents
Repeating the input of creating a single document above will update the document with the specified ID Beijing.
The response is:

```
{"_index":"china","_type":"city","_id":"beijing","_version":2,"result":"updated","_shards":{"total":2,"successful":2,"failed":0},"created":false}
```


## Query Documents
### Query a specified ID
Enter the following command:
```
curl -XGET 'http://10.0.0.2:9200/china/city/beijing?pretty'
```
The response is:
```
{
  "_index" : "china",
  "_type" : "city",
  "_id" : "beijing",
  "_version" : 4,
  "found" : true,
  "_source" : {
    "name" : "Beijing",
    "province" : "Beijing",
    "lat" : 39.9031324643,
    "lon" : 116.4010433787,
    "x" : 6763,
    "level.range" : 4,
    "level.level" : 1,
    "level.name" : "first-tier city",
    "y" : 6381,
    "cityNo" : 1
  }
}
```

### Query an index
Enter the following command:
```
curl -XGET 'http://10.0.0.2:9200/china/city/_search?pretty'
```
The response is:
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
          "name" : "Guangzhou",
          "province" : "No 79, Jixiang Road, Yuexiu District, Guangdong Province",
          "lat" : 23.1317146641,
          "lon" : 113.2595185241,
          "x" : 6173,
          "level.range" : 4,
          "level.level" : 1,
          "level.name" : "first-tier city",
          "y" : 2560,
          "cityNo" : 3
        }
      }
    },
    ......
}
    
```

### Complex query
Simulate an SQL statement:

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
The response is:

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
          "name" : "Chengdu",
          "province" : "No 88-1, 4th Section of Hongxing Road, Jinjiang District, Sichuan Province",
          "lat" : 30.6522796787,
          "lon" : 104.0725574128,
          "x" : 4387,
          "level.level" : 2,
          "level.range" : 19,
          "level.name" : "new first-tier city",
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
          "name" : "Hangzhou",
          "province" : "No 316, Huancheng North Road, Gongshu District, Zhejiang Province",
          "lat" : 30.2753694112,
          "lon" : 120.1509063337,
          "x" : 7530,
          "level.level" : 2,
          "level.range" : 19,
          "level.name" : "new first-tier city",
          "y" : 4182,
          "cityNo" : 6
        }
      }
    ]
  }
}
```

### Aggregation query
Simulate an SQL statement:

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

The response is:

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

## Delete Documents
### Delete a single document
Enter the following command:
```
curl -XDELETE 'http://10.0.0.2:9200/china/city/beijing?pretty'
```

The response is:

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
### Delete a type
```
curl -XDELETE 'http://10.0.0.2:9200/china/city?pretty'
```
### Delete an index
```
curl -XDELETE 'http://10.0.0.2:9200/china?pretty'
```


