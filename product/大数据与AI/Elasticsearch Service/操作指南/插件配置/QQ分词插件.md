QQ 分词插件是由腾讯云 ES 团队与腾讯 NLP 团队联合研发的中文分词插件，在腾讯内部广泛应用于 QQ、微信、浏览器等业务。在传统词典分词的基础上，增加了 NER 命名实体识别，同时支持自定义词库功能。QQ 分词插件经过多年的应用实践和不断打磨优化，在分词准确度、分析速度等关键指标上均处于业界领先，您可以在腾讯云 ES 中使用 QQ 分词插件来完成文档的分析和检索。

### 使用须知
QQ 分词插件仅支持数据节点规格在2核8G及以上的集群，如果集群未安装 QQ 分词插件，请在插件列表页面安装 QQ 分词插件（analysis-qq）。

QQ 分词插件提供如下的分析器（analyzer）和分词器（tokenizer）：
- 分析器：qq_smart, qq_max, qq_smart_ner, qq_max_ner
- 分词器：qq_smart, qq_max, qq_smart_ner, qq_max_ner

您可以使用上述的分析器和分词器完成文档的分析和查询。您也可以通过词库配置功能，自定义更新分词词库，详情请参见下文的配置词库。

> ?
>- `qq_max` 和 `qq_smart` 有什么区别？
>  - qq_max：会将文本做最细粒度的拆分，例如会将“西红柿鸡蛋汤”拆分为“西红柿鸡蛋汤、西红柿鸡蛋、鸡蛋汤、西红柿，鸡蛋、汤、鸡、蛋”。
>  - qq_smart：会做最粗粒度的拆分，例如会将“西红柿鸡蛋汤”拆分为“西红柿、鸡蛋、汤”。
>- ner 是什么？为什么 ner 功能要独立一个分词器？
ner 是 Named Entity Recognition（命名实体识别）的简称，可以识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等。对于这一类专有名词，不需要用户上传自定义词库。将 ner 功能单独保证为一个分词器，主要是因为 ner 功能需要加载一个模型，首次加载时间比较长。

### 使用步骤
1. 登录已安装 QQ 分词插件的集群对应的 Kibana 控制台。登录控制台的具体步骤请参考 [通过 Kibana 访问集群](https://cloud.tencent.com/document/product/845/19541)。
2. 单击左侧导航栏的 Dev Tools。
3. 在 Console 中使用 QQ 分词插件的分析器创建索引。
```
PUT /index
   {
     "mappings": {
       "_doc": {
         "properties": {
           "content": {
             "type": "text",
             "analyzer": "qq_max",
             "search_analyzer": "qq_smart"
           }
         }
       }
     }
   }
```
上面的语句创建了一个名称为`index`的索引，类型为`_doc`（ES 7及以上版本需要在创建索引时加入`?include_type_name=true`才能支持类型）。包含了一个`content`属性，类型为`text`，并使用了`qq_max`和`qq_smart`分析器。执行成功后，将返回如下结果。
```
{
     "acknowledged": true,
     "shards_acknowledged": true,
     "index": "index"
   }
```
4. 添加文档。
```
POST /index/_doc/1
   {
     "content": "我从微信上下载了王者荣耀"
   }
POST /index/_doc/2
   {
     "content": "住建部:9月底前完成名镇名村景观资源登记"
   }
POST /index/_doc/3
   {
     "content": "中国气象台最新天气预报"
   }
POST /index/_doc/4
   {
     "content": "我家住在中国古建筑保护协会附近"
   }
```
上面的语句导入了4个文档，将使用`qq_max`分析器对文档进行分析。
5. 使用关键词高亮的方式查询文档。
```
GET index/_search
   {
     "query" : { "match" : { "content" : "中国" }},
     "highlight" : {
       "pre_tags" : ["<tag1>", "<tag2>"],
       "post_tags" : ["</tag1>", "</tag2>"],
       "fields" : {"content": {}}
     }
   }
```
上面的语句在所有`_doc`类型的文档中，使用`qq_smart`分析器，搜索`content`字段中包含`中国`的文档。执行成功后，返回如下结果。
```
{
     "took" : 108,
     "timed_out" : false,
     "_shards" : {
       "total" : 1,
       "successful" : 1,
       "skipped" : 0,
       "failed" : 0
     },
     "hits" : {
       "total" : {
         "value" : 2,
         "relation" : "eq"
       },
       "max_score" : 0.7199211,
       "hits" : [
         {
           "_index" : "index",
           "_type" : "_doc",
           "_id" : "4",
           "_score" : 0.7199211,
           "_source" : {
             "content" : "我家住在中国古建筑保护协会附近"
           },
           "highlight" : {
             "content" : [
               "我家住在<tag1>中国</tag1>古建筑保护协会附近"
             ]
           }
         },
         {
           "_index" : "index",
           "_type" : "_doc",
           "_id" : "3",
           "_score" : 0.6235748,
           "_source" : {
             "content" : "中国气象台最新天气预报"
           },
           "highlight" : {
             "content" : [
               "<tag1>中国</tag1>气象台最新天气预报"
             ]
           }
         }
       ]
     }
   }
```

### 使用自定义词典
QQ 分词插件支持自定义词典的配置，词典上传后会触发集群的滚动重启，请确保集群处于 GREEN 状态，并且没有单副本索引。
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，在集群列表页，单击集群【ID/名称】进入集群详情页。
![](https://main.qcloudimg.com/raw/3a8640bd4e23dfa56ec76eda69fdc33f.png)
2. 单击【插件列表】，进入插件列表管理页面。
![](https://main.qcloudimg.com/raw/74d7f3915d9055d00c8c4194dd2ac655.png)
3. 找到 QQ 分词插件（analysis-qq），单击右侧【更新词典】。
4. 词典文件要求如下。
 - 词典文件必须为utf-8编码，一行一个词，且文件扩展名为`.dic`。
 - 单个文件最大为10M，上传文件总数最多为10个。
5. 单击保存。保存后，不会触发集群重启，但需要若干分钟触发集群变更使词典文件生效。

### 排查测试
如果您在使用 QQ 分词插件时，得到的结果不符合预期，可以通过下面的语句对分析器和分词器进行排查测试。
```
GET _analyze
{
  "text": "我家住在中国古建筑保护协会附近",
  "analyzer": "qq_max"
}

GET _analyze
{
  "text": "我家住在中国古建筑保护协会附近",
  "tokenizer": "qq_smart"
}
```

