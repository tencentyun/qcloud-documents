本节简单介绍如何从远程 Hadoop 集群中批量加载数据文件到 Druid 集群中。本文操作均是以 Hadoop 用户进行，请先在 Druid 集群和 Hadoop 集群上都切换到 Hadoop 用户。

## 批量加载数据到 Druid 集群
1. 在对应远程 hadoop 集群上，以 Hadoop 用户执行以下新建目录命令：
```
hdfs dfs -mkdir /druid
hdfs dfs -mkdir /druid/segments
hdfs dfs -mkdir /quickstart
hdfs dfs -chmod 777 /druid
hdfs dfs -chmod 777 /druid/segments
hdfs dfs -chmod 777 /quickstart
```
>!如果 Druid 集群和 Hadoop 集群是两个独立集群，则目录需要建立在对应 Hadoop 集群上（之后的操作类似，注意分辨正确操作对应的集群）；如果在测试环境下 Druid 集群和 Hadoop 集群是同一个集群，则在同集群操作即可。
2. 上传测试包
Druid 集群下自带一个名为 Wikiticker 的数据集示例（默认路径 `/usr/local/service/druid/quickstart/tutorial/wikiticker-2015-09-12-sampled.json.gz`），将 Druid 集群内的数据集上传到对应远程 Hadoop 集群，**是在远程 Hadoop 集群上传**。
```
hdfs dfs -put wikiticker-2015-09-12-sampled.json.gz /quickstart/wikiticker-2015-09-12-sampled.json.gz
```
3. 编译索引文件
准备一个索引文件，仍然使用 Druid 集群的样例文件 `/usr/local/service/druid/quickstart/tutorial/wikipedia-index-hadoop.json`，命令如下：
```
{
  "type" : "index_hadoop",
  "spec" : {
    "dataSchema" : {
      "dataSource" : "wikipedia",
      "parser" : {
        "type" : "hadoopyString",
        "parseSpec" : {
          "format" : "json",
          "dimensionsSpec" : {
            "dimensions" : [
              "channel",
              "cityName",
              "comment",
              "countryIsoCode",
              "countryName",
              "isAnonymous",
              "isMinor",
              "isNew",
              "isRobot",
              "isUnpatrolled",
              "metroCode",
              "namespace",
              "page",
              "regionIsoCode",
              "regionName",
              "user",
              { "name": "added", "type": "long" },
              { "name": "deleted", "type": "long" },
              { "name": "delta", "type": "long" }
            ]
          },
          "timestampSpec" : {
            "format" : "auto",
            "column" : "time"
          }
        }
      },
      "metricsSpec" : [],
      "granularitySpec" : {
        "type" : "uniform",
        "segmentGranularity" : "day",
        "queryGranularity" : "none",
        "intervals" : ["2015-09-12/2015-09-13"],
        "rollup" : false
      }
    },
    "ioConfig" : {
      "type" : "hadoop",
      "inputSpec" : {
        "type" : "static",
        "paths" : "/quickstart/wikiticker-2015-09-12-sampled.json.gz"
      }
    },
    "tuningConfig" : {
      "type" : "hadoop",
      "partitionsSpec" : {
        "type" : "hashed",
        "targetPartitionSize" : 5000000
      },
      "forceExtendableShardSpecs" : true,
      "jobProperties" : {
        "yarn.nodemanager.vmem-check-enabled" : "false",
        "mapreduce.map.java.opts" : "-Duser.timezone=UTC -Dfile.encoding=UTF-8",
        "mapreduce.job.user.classpath.first" : "true",
        "mapreduce.reduce.java.opts" : "-Duser.timezone=UTC -Dfile.encoding=UTF-8",
        "mapreduce.map.memory.mb" : 1024,
        "mapreduce.reduce.memory.mb" : 1024
      }
    }
  },
  "hadoopDependencyCoordinates": ["org.apache.hadoop:hadoop-client:2.8.5"]
}
```
**说明：**
 - hadoopDependencyCoordinates 为依赖的 Hadoop 版本。
 - spec.ioConfig.inputSpec.paths 为输入文件路径。如果已经在 common.runtime.properties 配置中设置好集群连通性，可以使用相对路径（可参考 [Druid 使用](https://cloud.tencent.com/document/product/589/43556)）。否则，应该根据情况使用以`hdfs://`或者`cosn://`开头的相对路径。
 - tuningConfig.jobProperties 参数可以设置 mapreduce job 的相关参数。
4. 提交索引任务
接下来可以在 Druid 集群上提交任务将数据摄入，在 Druid 目录下以 Hadoop 用户执行：
```
./bin/post-index-task --file quickstart/tutorial/wikipedia-index-hadoop.json --url http://localhost:8090
```
成功后则会有如下类似的输出：
```
...
Task finished with status: SUCCESS
Completed indexing data for wikipedia. Now loading indexed data onto the cluster...
wikipedia loading complete! You may now query your data
```

## 数据查询
Druid 支持类 SQL 和原生 JSON 查询，下面将分别介绍，更多内容可参考 [官方文档](https://druid.apache.org/docs/latest/tutorials/tutorial-query.html)。

### sql 方式查询
Druid 支持多种 SQL 查询方式：
- 在 Web UI 的 Query 菜单中查询。
```
SELECT page, COUNT(*) AS Edits
FROM wikipedia
WHERE TIMESTAMP '2015-09-12 00:00:00' <= "__time" AND "__time" < TIMESTAMP '2015-09-13 00:00:00'
GROUP BY page
ORDER BY Edits DESC
LIMIT 10
```
- 在查询节点上使用命令行工具`bin/dsql`进行交互式查询。
```
[hadoop@172 druid]$ ./bin/dsql
Welcome to dsql, the command-line client for Druid SQL.
Connected to [http://localhost:8082/].
Type "\h" for help.
dsql> SELECT page, COUNT(*) AS Edits FROM wikipedia WHERE "__time" BETWEEN TIMESTAMP '2015-09-12 00:00:00' AND TIMESTAMP '2015-09-13 00:00:00' GROUP BY page ORDER BY Edits DESC LIMIT 10;
┌──────────────────────────────────────────────────────────┬───────┐
│ page                                                     │ Edits │
├──────────────────────────────────────────────────────────┼───────┤
│ Wikipedia:Vandalismusmeldung                             │    33 │
│ User:Cyde/List of candidates for speedy deletion/Subpage │    28 │
│ Jeremy Corbyn                                            │    27 │
│ Wikipedia:Administrators' noticeboard/Incidents          │    21 │
│ Flavia Pennetta                                          │    20 │
│ Total Drama Presents: The Ridonculous Race               │    18 │
│ User talk:Dudeperson176123                               │    18 │
│ Wikipédia:Le Bistro/12 septembre 2015                    │    18 │
│ Wikipedia:In the news/Candidates                         │    17 │
│ Wikipedia:Requests for page protection                   │    17 │
└──────────────────────────────────────────────────────────┴───────┘
Retrieved 10 rows in 0.06s.
```
- 用 HTTP 服务查询 SQL。
```
curl -X 'POST' -H 'Content-Type:application/json' -d @quickstart/tutorial/wikipedia-top-pages-sql.json http://localhost:18888/druid/v2/sql
```
格式化后的输出结果：
```
[
    {
        "page":"Wikipedia:Vandalismusmeldung",
        "Edits":33
    },
    {
        "page":"User:Cyde/List of candidates for speedy deletion/Subpage",
        "Edits":28
    },
    {
        "page":"Jeremy Corbyn",
        "Edits":27
    },
    {
        "page":"Wikipedia:Administrators' noticeboard/Incidents",
        "Edits":21
    },
    {
        "page":"Flavia Pennetta",
        "Edits":20
    },
    {
        "page":"Total Drama Presents: The Ridonculous Race",
        "Edits":18
    },
    {
        "page":"User talk:Dudeperson176123",
        "Edits":18
    },
    {
        "page":"Wikipédia:Le Bistro/12 septembre 2015",
        "Edits":18
    },
    {
        "page":"Wikipedia:In the news/Candidates",
        "Edits":17
    },
    {
        "page":"Wikipedia:Requests for page protection",
        "Edits":17
    }
]
```

### 原生 JSON 查询

- 在 Web UI 上 Query 菜单直接输入 json 查询。
```
{
     "queryType" : "topN",
     "dataSource" : "wikipedia",
     "intervals" : ["2015-09-12/2015-09-13"],
     "granularity" : "all",
     "dimension" : "page",
     "metric" : "count",
     "threshold" : 10,
     "aggregations" : [
         {
            "type" : "count",
            "name" : "count"
         }
     ]
}
```
- 在查询节点上 druid 方式目录下用 HTTP 提交。
```
curl -X 'POST' -H 'Content-Type:application/json' -d @quickstart/tutorial/wikipedia-top-pages.json http://localhost:18888/druid/v2?pretty
```
输出结果：
```
[ {
  "timestamp" : "2015-09-12T00:46:58.771Z",
  "result" : [ {
    "count" : 33,
    "page" : "Wikipedia:Vandalismusmeldung"
  }, {
    "count" : 28,
    "page" : "User:Cyde/List of candidates for speedy deletion/Subpage"
  }, {
    "count" : 27,
    "page" : "Jeremy Corbyn"
  }, {
    "count" : 21,
    "page" : "Wikipedia:Administrators' noticeboard/Incidents"
  }, {
    "count" : 20,
    "page" : "Flavia Pennetta"
  }, {
    "count" : 18,
    "page" : "Total Drama Presents: The Ridonculous Race"
  }, {
    "count" : 18,
    "page" : "User talk:Dudeperson176123"
  }, {
    "count" : 18,
    "page" : "Wikipédia:Le Bistro/12 septembre 2015"
  }, {
    "count" : 17,
    "page" : "Wikipedia:In the news/Candidates"
  }, {
    "count" : 17,
    "page" : "Wikipedia:Requests for page protection"
  } ]
} ]
```
