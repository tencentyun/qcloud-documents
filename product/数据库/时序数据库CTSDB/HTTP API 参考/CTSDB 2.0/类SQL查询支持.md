
CTSDB 2.0 支持使用类 SQL 语句进行查询，仅为了方便初学者使用；如关注查询时效，仍推荐使用 CTSDB 原生查询语句。

## 请求地址
地址为实例的 IP 和 PORT，可从控制台获取到，例如10.13.20.15:9200。

## 请求路径和方法
路径：`_nlpcn/sql`
方法：GET

## 请求参数
可在查询时加入 pretty 参数值来获得整理格式后的返回响应，具体请参见示例。

## 请求内容
查询主要有普通查询和聚合查询，具体请求内容请参照示例。

## 返回内容
需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。如参数名或表名的错误，需要自行检查更正。

## CURL 示例说明
具体查询请参考下列示例。

所有示例使用的 metric 结构如下所示：
```
   {
       "ctsdb_test" : {
         "tags" : {
           "region" : "string"
         },
         "time" : {
           "name" : "timestamp",
           "format" : "epoch_millis"
         },
         "fields" : {
           "cpuUsage" : "float",
           "diskUsage" : "string",
           "dcpuUsage" : "integer"
         },
         "options" : {
           "expire_day" : 7,
           "refresh_interval" : "10s",
           "number_of_shards" : 5
         }
       }
   }
```

普通查询的 CURL 示例：
```
curl -u root:le201909 -H 'Content-Type: application/json' -XGET 172.xx.xx.4:9201/_nlpcn/sql?pretty -d 'select docvalue(cpuUsage) from ctsdb_test limit 1'
```

普通查询的响应示例：
```
{
  "took" : 22,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "ctsdb_test@1646064000000_1",
        "_type" : "_doc",
        "_id" : "XMzBRX8BfqojiIOn8jFa",
        "_score" : 1.0,
        "fields" : {
          "cpuUsage" : [
            10.0
          ]
        }
      }
    ]
  }
}
```

>?普通查询时，所查询字段，需要加 docvalue 使实例从其列存区拿取数据。

带搜索条件的普通查询的 CURL 示例：
```
curl -u root:le201909 -H 'Content-Type: application/json' -XGET 172.xx.xx.4:9201/_nlpcn/sql?pretty -d 'select docvalue(cpuUsage) from ctsdb_test where region="shanghai" limit 1'
```

带搜索条件的普通查询的响应示例：
```
{
  "took" : 13,
  "timed_out" : false,
  "_shards" : {
    "total" : 10,
    "successful" : 10,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "ctsdb_test@1646064000000_1",
        "_type" : "_doc",
        "_id" : "XszBRX8BfqojiIOn8jFb",
        "_score" : 0.0,
        "fields" : {
          "cpuUsage" : [
            30.0
          ]
        }
      }
    ]
  }
}
```
>?带搜索条件的普通查询时，用做查询条件的字段，不需要加docvalue。

按某  tag 字段分组聚合查询的 CURL 示例：
```
curl -u root:le201909 -H 'Content-Type: application/json' -XGET 172.xx.xx.14:9201/_nlpcn/sql?pretty -d 'select max(cpuUsage) from ctsdb_test group by region'
```

按某 tag 字段分组聚合查询的响应示例：
```
{
  "took" : 33,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "region" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "beijing",
          "doc_count" : 1,
          "MAX(cpuUsage)" : {
            "value" : 20.0
          }
        },
        {
          "key" : "chengdu",
          "doc_count" : 1,
          "MAX(cpuUsage)" : {
            "value" : 10.0
          }
        },
        {
          "key" : "shanghai",
          "doc_count" : 1,
          "MAX(cpuUsage)" : {
            "value" : 30.0
          }
        }
      ]
    }
  }
}
```

>?按某 tag 字段分组聚合查询时，用于分组的字段，不需要加 docvalue。

按时间聚合分组查询的 CURL 示例：
```
curl -u root:le201909 -H 'Content-Type: application/json' -XGET 172.xx.xx.4:9201/_nlpcn/sql?pretty -d 'select max(cpuUsage) from ctsdb_test GROUP BY date_histogram(field="timestamp","interval"="1d")'
```

按时间聚合分组查询的响应示例：
```
{
  "took" : 30,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "date_histogram(field=timestamp,interval=1d)" : {
      "buckets" : [
        {
          "key_as_string" : "2022-03-01 00:00:00",
          "key" : 1646092800000,
          "doc_count" : 3,
          "MAX(cpuUsage)" : {
            "value" : 30.0
          }
        }
      ]
    }
  }
}
```

