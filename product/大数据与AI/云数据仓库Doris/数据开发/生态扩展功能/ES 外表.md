Doris-On-ES 将 Doris 的分布式查询规划能力和 ES（Elasticsearch）的全文检索能力相结合，提供更完善的 OLAP 分析场景解决方案：
1. ES 中的多 index 分布式 Join 查询。
2. Doris 和 ES 中的表联合查询，更复杂的全文检索过滤。

本文档主要介绍该功能的实现原理、使用方式等。

## 名词解释

### Doris 相关
- FE：Frontend，Doris 的前端节点，负责元数据管理和请求接入。
- BE：Backend，Doris 的后端节点，负责查询执行和数据存储。

### ES 相关
- DataNode：ES 的数据存储与计算节点。
- MasterNode：ES 的 Master 节点，管理元数据、节点、数据分布等。
- scroll：ES内置的数据集游标特性，用来对数据进行流式扫描和过滤。
- _source：导入时传入的原始 JSON 格式文档内容。
- doc_values：ES/Lucene 中字段的列式存储定义。
- keyword：字符串类型字段，ES/Lucene 不会对文本内容进行分词处理。
- text：字符串类型字段，ES/Lucene 会对文本内容进行分词处理，分词器需要用户指定，默认为 standard 英文分词器。

## 使用方法
### 创建 ES 索引
```json
PUT test
{
   "settings": {
      "index": {
         "number_of_shards": "1",
         "number_of_replicas": "0"
      }
   },
   "mappings": {
      "doc": { // ES 7.x版本之后创建索引时不需要指定type，会有一个默认且唯一的`_doc` type
         "properties": {
            "k1": {
               "type": "long"
            },
            "k2": {
               "type": "date"
            },
            "k3": {
               "type": "keyword"
            },
            "k4": {
               "type": "text",
               "analyzer": "standard"
            },
            "k5": {
               "type": "float"
            }
         }
      }
   }
}
```

### ES 索引导入数据
```json
POST /_bulk
{"index":{"_index":"test","_type":"doc"}}
{ "k1" : 100, "k2": "2020-01-01", "k3": "Trying out Elasticsearch", "k4": "Trying out Elasticsearch", "k5": 10.0}
{"index":{"_index":"test","_type":"doc"}}
{ "k1" : 100, "k2": "2020-01-01", "k3": "Trying out Doris", "k4": "Trying out Doris", "k5": 10.0}
{"index":{"_index":"test","_type":"doc"}}
{ "k1" : 100, "k2": "2020-01-01", "k3": "Doris On ES", "k4": "Doris On ES", "k5": 10.0}
{"index":{"_index":"test","_type":"doc"}}
{ "k1" : 100, "k2": "2020-01-01", "k3": "Doris", "k4": "Doris", "k5": 10.0}
{"index":{"_index":"test","_type":"doc"}}
{ "k1" : 100, "k2": "2020-01-01", "k3": "ES", "k4": "ES", "k5": 10.0}
```

### Doris 中创建 ES 外表
具体建表语法参照 [CREATE TABLE](https://doris.apache.org/zh-CN/docs/dev/sql-manual/sql-reference/Data-Definition-Statements/Create/CREATE-TABLE)。
```sql
CREATE EXTERNAL TABLE `test` // 不指定schema，自动拉取es mapping进行建表 
ENGINE=ELASTICSEARCH 
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"type" = "doc",
"user" = "root",
"password" = "root"
);

CREATE EXTERNAL TABLE `test` (
  `k1` bigint(20) COMMENT "",
  `k2` datetime COMMENT "",
  `k3` varchar(20) COMMENT "",
  `k4` varchar(100) COMMENT "",
  `k5` float COMMENT ""
) ENGINE=ELASTICSEARCH // ENGINE必须是Elasticsearch
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"type" = "doc",
"user" = "root",
"password" = "root"
);
```

参数说明：

参数 | 说明
---|---
**hosts** | ES 集群地址，可以是一个或多个，也可以是 ES 前端的负载均衡地址
**index** | 对应的 ES 的 index 名字，支持 alias，如果使用 doc_value，需要使用真实的名称
**type** | index 的 type，ES 7.x 及以后的版本不传此参数
**user** | ES 集群用户名
**password** | 对应用户的密码信息

- ES 7.x 之前的集群请注意在建表的时候选择正确的**索引类型 type**。
- 认证方式目前仅支持 HTTP Basic 认证，并且需要确保该用户有访问：/\_cluster/state/、\_nodes/http 等路径和 index 的读权限；集群未开启安全认证，用户名和密码不需要设置。
- Doris 表中的列名需要和 ES 中的字段名完全匹配，字段类型应该保持一致。
-  **ENGINE** 必须是 **Elasticsearch**。

#### 过滤条件下推
`Doris On ES`一个重要的功能就是过滤条件的下推: 过滤条件下推给ES，这样只有真正满足条件的数据才会被返回，能够显著的提高查询性能和降低Doris和Elasticsearch的CPU、memory、IO使用量

`enable_new_es_dsl`代表是否使用新版dsl生成逻辑, 后续 bug 修复和迭代都在新版dsl开发, 默认为`true`, 可在`fe.conf`中进行修改

下面的操作符（Operators）会被优化成如下 ES Query：

| SQL syntax  | ES 5.x+ syntax | 
|-------|:---:|
| =   | term query|
| in  | terms query   |
| > , < , >= , ⇐  | range query |
| and  | bool.filter   |
| or  | bool.should   |
| not  | bool.must_not   |
| not in  | bool.must_not + terms query |
| is\_not\_null  | exists query |
| is\_null  | bool.must_not + exists query |
| esquery  | ES原生json形式的QueryDSL   |

#### 数据类型映射

Doris\ES  |  byte | short | integer | long | float | double| keyword | text | date
------------- | ------------- | ------  | ---- | ----- | ----  | ------ | ----| --- | --- |
tinyint  | &#10003; |  |  |  |   |   |   |   |
smallint | &#10003; | &#10003; |  | |   |   |   |   |
int | &#10003; |  &#10003; | &#10003; | |   |   |   |   |
bigint | &#10003;  | &#10003;  | &#10003;  | &#10003; |   |   |   |   |
float |   |   |   |   | &#10003; |   |   |   |
double |   |   |   |   |   | &#10003; |   |   |
char |   |   |   |   |   |   | &#10003; | &#10003; |
varchar |  |   |   |   |   |   | &#10003; | &#10003; |
date |   |   |   |   |   |   |   |   | &#10003;|  
datetime |   |   |   |   |   |   |   |   | &#10003;|


### 启用列式扫描优化查询速度（enable\_docvalue\_scan=true）
```sql
CREATE EXTERNAL TABLE `test` (
  `k1` bigint(20) COMMENT "",
  `k2` datetime COMMENT "",
  `k3` varchar(20) COMMENT "",
  `k4` varchar(100) COMMENT "",
  `k5` float COMMENT ""
) ENGINE=ELASTICSEARCH
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"user" = "root",
"password" = "root",
"enable_docvalue_scan" = "true"
);
```

参数说明：

参数 | 说明
---|---
**enable\_docvalue\_scan** | 是否开启通过 ES/Lucene 列式存储获取查询字段的值，默认为 false

开启后 Doris 从 ES 中获取数据会遵循以下两个原则：
* **尽力而为**：自动探测要读取的字段是否开启列式存储（doc_value: true），如果获取的字段全部有列存，Doris 会从列式存储中获取所有字段的值。
* **自动降级**：如果要获取的字段只要有一个字段没有列存，所有字段的值都会从行存`_source`中解析获取。

#### 优势
默认情况下，Doris On ES 会从行存也就是`_source`中获取所需的所有列，`_source`的存储采用的行式+json的形式存储，在批量读取性能上要劣于列式存储，尤其在只需要少数列的情况下尤为明显，只获取少数列的情况下，docvalue 的性能大约是_source 性能的十几倍。

#### 注意
1. `text`类型的字段在 ES 中是没有列式存储，因此如果要获取的字段值有`text`类型字段会自动降级为从`_source`中获取。
2. 在获取的字段数量过多的情况下(`>= 25`)，从`docvalue`中获取字段值的性能会和从`_source`中获取字段值基本一样。


### 探测 keyword 类型字段（enable\_keyword\_sniff=true）
```sql
CREATE EXTERNAL TABLE `test` (
  `k1` bigint(20) COMMENT "",
  `k2` datetime COMMENT "",
  `k3` varchar(20) COMMENT "",
  `k4` varchar(100) COMMENT "",
  `k5` float COMMENT ""
) ENGINE=ELASTICSEARCH
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"user" = "root",
"password" = "root",
"enable_keyword_sniff" = "true"
);
```

参数说明：

参数 | 说明
---|---
**enable\_keyword\_sniff** | 是否对 ES 中字符串类型分词类型（**text**） `fields` 进行探测，获取额外的未分词（**keyword**）字段名（multi-fields 机制）

在 ES 中可以不建立 index 直接进行数据导入，这时候 ES 会自动创建一个新的索引，针对字符串类型的字段 ES 会创建一个既有`text`类型的字段又有`keyword`类型的字段，这就是 ES 的 multi fields 特性，mapping 如下：
```json
"k4": {
   "type": "text",
   "fields": {
      "keyword": {   
         "type": "keyword",
         "ignore_above": 256
      }
   }
}
```
对 k4进行条件过滤时例如=，Doris On ES 会将查询转换为 ES 的 TermQuery。
SQL 过滤条件：
```sql
k4 = "Doris On ES"
```
转换成 ES的query DSL 为：
```json
"term" : {
    "k4": "Doris On ES"

}
```
因为  k4的第一字段类型为`text`，在数据导入的时候就会根据k4设置的分词器（如果没有设置，就是 standard 分词器）进行分词处理得到 doris、on、es 三个 Term，如下 ES analyze API 分析：
```json
POST /_analyze
{
  "analyzer": "standard",
  "text": "Doris On ES"
}
```
分词的结果是：

```json
{
   "tokens": [
      {
         "token": "doris",
         "start_offset": 0,
         "end_offset": 5,
         "type": "<ALPHANUM>",
         "position": 0
      },
      {
         "token": "on",
         "start_offset": 6,
         "end_offset": 8,
         "type": "<ALPHANUM>",
         "position": 1
      },
      {
         "token": "es",
         "start_offset": 9,
         "end_offset": 11,
         "type": "<ALPHANUM>",
         "position": 2
      }
   ]
}
```
查询时使用的是：
```json
"term" : {
    "k4": "Doris On ES"
}
```
`Doris On ES`这个 term 匹配不到词典中的任何 term，不会返回任何结果，而启用`enable_keyword_sniff: true`会自动将`k4 = "Doris On ES"`转换成`k4.keyword = "Doris On ES"`来完全匹配 SQL 语义，转换后的 ES query DSL 为：
```json
"term" : {
    "k4.keyword": "Doris On ES"
}
```
`k4.keyword` 的类型是`keyword`，数据写入 ES 中是一个完整的 term，所以可以匹配。

### 开启节点自动发现
默认为 true（nodes\_discovery=true）。
```sql
CREATE EXTERNAL TABLE `test` (
  `k1` bigint(20) COMMENT "",
  `k2` datetime COMMENT "",
  `k3` varchar(20) COMMENT "",
  `k4` varchar(100) COMMENT "",
  `k5` float COMMENT ""
) ENGINE=ELASTICSEARCH
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"user" = "root",
"password" = "root",
"nodes_discovery" = "true"
);
```

参数说明：

参数 | 说明
---|---
**nodes\_discovery** | 是否开启 EST 节点发现，默认为 true

当配置为 true 时，Doris 将从 ES 找到所有可用的相关数据节点(在上面分配的分片)。如果 ES 数据节点的地址没有被 Doris BE 访问，则设置为 false。ES 群部署在与公共 Internet 隔离的内网，用户通过代理访问。

### ES 集群是否开启 HTTPS 访问模式
如果开启应设置为`true`，默认为 false(http\_ssl\_enabled=true) 。
```sql
CREATE EXTERNAL TABLE `test` (
  `k1` bigint(20) COMMENT "",
  `k2` datetime COMMENT "",
  `k3` varchar(20) COMMENT "",
  `k4` varchar(100) COMMENT "",
  `k5` float COMMENT ""
) ENGINE=ELASTICSEARCH
PROPERTIES (
"hosts" = "http://192.168.0.1:8200,http://192.168.0.2:8200",
"index" = "test",
"user" = "root",
"password" = "root",
"http_ssl_enabled" = "true"
);
```

参数说明：

参数 | 说明
---|---
**http\_ssl\_enabled** | ES 集群是否开启 HTTPS 访问模式

目前会 fe/be 实现方式为信任所有，这是临时解决方案，后续会使用真实的用户配置证书。

### 查询用法
完成在 Doris 中建立 ES 外表后，除了无法使用 Doris 中的数据模型（rollup、预聚合、物化视图等）外并无区别。

#### 基本查询
```sql
select * from es_table where k1 > 1000 and k3 ='term' or k4 like 'fu*z_'
```

#### 扩展的 esquery(field, QueryDSL)
通过`esquery(field, QueryDSL)`函数将一些无法用 sql 表述的 query 如 match_phrase、geoshape 等下推给 ES 进行过滤处理，`esquery`的第一个列名参数用于关联`index`，第二个参数是ES的基本`Query DSL`的 json 表述，使用花括号`{}`包含，json 的`root key`有且只能有一个，如 match_phrase、geo_shape、bool 等。
match_phrase 查询：
```sql
select * from es_table where esquery(k4, '{
        "match_phrase": {
           "k4": "doris on es"
        }
    }');
```
geo相关查询：

```sql
select * from es_table where esquery(k4, '{
      "geo_shape": {
         "location": {
            "shape": {
               "type": "envelope",
               "coordinates": [
                  [
                     13,
                     53
                  ],
                  [
                     14,
                     52
                  ]
               ]
            },
            "relation": "within"
         }
      }
   }');
```

bool 查询：
```sql
select * from es_table where esquery(k4, ' {
         "bool": {
            "must": [
               {
                  "terms": {
                     "k1": [
                        11,
                        12
                     ]
                  }
               },
               {
                  "terms": {
                     "k2": [
                        100
                     ]
                  }
               }
            ]
         }
      }');
```


## 原理
```              
+----------------------------------------------+
|                                              |
| Doris      +------------------+              |
|            |       FE         +--------------+-------+
|            |                  |  Request Shard Location
|            +--+-------------+-+              |       |
|               ^             ^                |       |
|               |             |                |       |
|  +-------------------+ +------------------+  |       |
|  |            |      | |    |             |  |       |
|  | +----------+----+ | | +--+-----------+ |  |       |
|  | |      BE       | | | |      BE      | |  |       |
|  | +---------------+ | | +--------------+ |  |       |
+----------------------------------------------+       |
   |        |          | |        |         |          |
   |        |          | |        |         |          |
   |    HTTP SCROLL    | |    HTTP SCROLL   |          |
+-----------+---------------------+------------+       |
|  |        v          | |        v         |  |       |
|  | +------+--------+ | | +------+-------+ |  |       |
|  | |               | | | |              | |  |       |
|  | |   DataNode    | | | |   DataNode   +<-----------+
|  | |               | | | |              | |  |       |
|  | |               +<--------------------------------+
|  | +---------------+ | | |--------------| |  |       |
|  +-------------------+ +------------------+  |       |
|   Same Physical Node                         |       |
|                                              |       |
|           +-----------------------+          |       |
|           |                       |          |       |
|           |      MasterNode       +<-----------------+
| ES        |                       |          |
|           +-----------------------+          |
+----------------------------------------------+
```
1. 创建 ES 外表后，FE 会请求建表指定的主机，获取所有节点的 HTTP 端口信息以及 index 的 shard 分布信息等，如果请求失败会顺序遍历 host 列表直至成功或完全失败。
2. 查询时会根据 FE 得到的一些节点信息和 index 的元数据信息，生成查询计划并发给对应的 BE 节点。
3. BE 节点会根据**就近原则**即优先请求本地部署的 ES 节点，BE 通过`HTTP Scroll`方式流式的从 ES index 的每个分片中并发的从`_source` 或 `docvalue` 中获取数据。
4. Doris 计算完结果后，返回给用户。

## 最佳实践
### 时间类型字段使用建议
在 ES 中，时间类型的字段使用十分灵活，但是在 Doris On ES 中如果对时间类型字段的类型设置不当，则会造成过滤条件无法下推。
创建索引时对时间类型格式的设置做最大程度的格式兼容：
```json
 "dt": {
     "type": "date",
     "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
 }
```
在 Doris 中建立该字段时建议设置为 `date` 或 `datetime`，也可以设置为 `varchar` 类型，使用如下 SQL 语句都可以直接将过滤条件下推至 ES：
```sql
select * from doe where k2 > '2020-06-21';

select * from doe where k2 < '2020-06-21 12:00:00'; 

select * from doe where k2 < 1593497011; 

select * from doe where k2 < now();

select * from doe where k2 < date_format(now(), '%Y-%m-%d');
```

注意在 ES 中如果不对时间类型的字段设置`format`，默认的时间类型字段格式为：
```
strict_date_optional_time||epoch_millis
```
导入到 ES 的日期字段如果是时间戳需要转换成`ms`，ES 内部处理时间戳都是按照`ms`进行处理的，否则 Doris On ES 会出现显示错误。

### 获取 ES 元数据字段`_id`
导入文档在不指定`_id`的情况下 ES 会给每个文档分配一个全局唯一的`_id`即主键, 用户也可以在导入时为文档指定一个含有特殊业务意义的`_id`；如果需要在 Doris On ES 中获取该字段值，建表时可以增加类型为`varchar`的`_id`字段：
```sql
CREATE EXTERNAL TABLE `doe` (
  `_id` varchar COMMENT "",
  `city`  varchar COMMENT ""
) ENGINE=ELASTICSEARCH
PROPERTIES (
"hosts" = "http://127.0.0.1:8200",
"user" = "root",
"password" = "root",
"index" = "doe"
}
```

>! 
>- `_id` 字段的过滤条件仅支持 `=` 和 `in` 两种。
>- `_id` 字段只能是 `varchar` 类型。

## 常见问题
1. Doris On ES 对 ES 的版本要求。
ES 主版本大于5，ES 在2.x 之前和5.x 之后数据的扫描方式不同，目前支持仅5.x 之后的。

2. 是否支持 X-Pack 认证的 ES 集群？
支持所有使用 HTTP Basic 认证方式的 ES 集群。

3. 一些查询比请求 ES 慢很多？
是，例如_count 相关的 query 等，ES 内部会直接读取满足条件的文档个数相关的元数据，不需要对真实的数据进行过滤。

4. 聚合操作是否可以下推？
目前 Doris On ES 不支持聚合操作如 sum，avg，min/max 等下推，计算方式是批量流式的从 ES 获取所有满足条件的文档，然后在 Doris 中进行计算。
