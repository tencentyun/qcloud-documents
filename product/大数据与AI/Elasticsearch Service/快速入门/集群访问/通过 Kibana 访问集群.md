腾讯云 ES 包含 Kibana 模块，用户可以通过公网访问集群对应的 Kibana 页面，进行数据的可视化查询分析，以及数据的管理操作，您可以通过本教程开始 Kibana 的快速入门。

## 访问 Kibana 页面

### 入口
Kibana 页面有两个入口，分别位于集群列表页和集群详情页，详情如下图。单击对应的入口，会跳转到 Kibana 登录页面。

![列表页入口](https://main.qcloudimg.com/raw/49ac415dda4184125677f3d04f84cfe3.png)

![详情页入口](https://main.qcloudimg.com/raw/4c31ad620af4977f92ee1e28cbda48db.png)

### 登录
Kibana 页面访问需要登录，帐号为 elastic，密码为用户创建集群时设置的 Kibana 密码。如果忘记密码，可以在集群详情页重置密码。
出于安全考虑，用户可以配置 Kibana 页面访问黑白名单，来进行限制，详见 [Kibana 访问设置](https://cloud.tencent.com/document/product/845/16992)。

#### 开源版和基础版集群的登录页如下图所示：

![登录](https://main.qcloudimg.com/raw/e0cfe910c15ae171b116d822b3dcf3d7.png)

#### 白金版集群登录页如下图所示:

![白金版登陆](https://main.qcloudimg.com/raw/272088c161b9b9e3691e9460354ba1c3.png)


### 访问
登录 Kibana 页面后，如果用户是第一次使用，集群尚未存入用户自定义的索引数据，页面会提示用户配置索引，具体参考下文索引添加及访问部分。

![初始化页面](https://main.qcloudimg.com/raw/22db76fe961cb5aa118465d4947707c0.png)

## 索引添加及访问（存储数据） 
在 Kibana 页面左侧菜单，单击【Dev Tools】进入开发工具页面，用户可以通过控制台，向集群发送各种操作请求。下面将通过城市信息的数据存储操作的示例，演示如何通过控制台操作集群和存储数据。

### 添加索引

#### 定义索引的 mapping

索引名称 china ，类型名称为 city，以及详细的字段及类型信息。其中字段 loacation 的类型是 geo_point，可以表示地理位置信息； level 是对象类型，包含二级字段信息。关于字段类型说明，可查看官方文档 [Field Datatypes](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/mapping-types.html)。

![定义索引mapping](https://main.qcloudimg.com/raw/85704f5b4d47bcc971f6aaa95d58e24c.png)

```
PUT china
{
  "mappings": {
    "city": {
      "properties":{
        "name":{ "type": "keyword"  }, 
        "province":{ "type": "keyword"  }, 
        "location": {"type": "geo_point"},
        "x":{ "type": "integer" },
        "level":{
            "properties":{                
                "level":{ "type": "integer" },
                "range":{ "type": "integer" },
                "name":{ "type": "keyword" }
            }
        },
        "y":{ "type": "integer" },
        "cityNo":{ "type": "integer" } 
      }
    }
  }
}
```

#### 添加单个文档

![存入单条数据](https://main.qcloudimg.com/raw/1ca53899fe58347c285665d71160289b.png)

```
PUT china/city/wuhan 
{"name":"武汉市","province":"湖北省江岸区沿江大道188号","location":{"lat":30.5952548577,"lon":114.2999398195},"x":6384,"level":{"level":2,"range":19,"name":"新一线城市"},"y":4231,"cityNo":7}
```

#### 查询单个文档：

```
GET /china/city/wuhan
```

#### 添加多个文档

```
POST _bulk
{ "index" : { "_index": "china", "_type" : "city", "_id" : "beijing" } }
{"name":"北京市","province":"北京市","location":{"lat":39.9031324643,"lon":116.4010433787},"x":6763,"level":{"range":4,"level":1,"name":"一线城市"},"y":6381,"cityNo":1}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shanghai" } }
{"name":"上海市","province":"上海市","location":{"lat":31.2319526784,"lon":121.469443249},"x":7779,"level":{"range":4,"level":1,"name":"一线城市"},"y":4409,"cityNo":2}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "guangzhou" } }
{"name":"广州市","province":"广东省越秀区吉祥路79号","location":{"lat":23.1317146641,"lon":113.2595185241},"x":6173,"level":{"range":4,"level":1,"name":"一线城市"},"y":2560,"cityNo":3}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shenzhen" } }
{"name":"深圳市","province":"广东省福田区新园路37号","location":{"lat":22.5455465546,"lon":114.0527779134},"x":6336,"level":{"range":4,"level":1,"name":"一线城市"},"y":2429,"cityNo":4}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "chengdu" } }
{"name":"成都市","province":"四川省锦江区红星路4段-88号-附1号","location":{"lat":30.6522796787,"lon":104.0725574128},"x":4387,"level":{"level":2,"range":19,"name":"新一线城市"},"y":4304,"cityNo":5}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "hangzhou" } }
{"name":"杭州市","province":"浙江省拱墅区环城北路316号","location":{"lat":30.2753694112,"lon":120.1509063337},"x":7530,"level":{"level":2,"range":19,"name":"新一线城市"},"y":4182,"cityNo":6}
```

#### 查询多个文档：

```
GET /china/city/_search
```

### 访问索引

#### 配置 Kibana 访问索引

为了使用 Kibana，需要配置至少一个可以匹配到的索引。 输入上文创建的索引 china，单击【Next step】进入下一步：

![配置访问索引](https://main.qcloudimg.com/raw/0b471a536fef9d45ac04ba7d837447bf.png)

配置时间过滤字段用于通过时间过滤索引中的数据，如果索引中没有表示时间的字段可以选择不使用时间过滤功能，单击【Create index pattern】创建索引模式：

![配置时间过滤字段](https://main.qcloudimg.com/raw/82ed7b6622cb8583a800c7aa4e107d67.png)


查看索引对应的字段：

![查看索引字段](https://main.qcloudimg.com/raw/aae26c9bbd4f745cbf22cd1a17f49a30.png)

单击左侧菜单【Discover】，查看该索引下已经添加的文档：

![访问详细数据](https://main.qcloudimg.com/raw/54291ceed6f6863dc62428664d8c7eac.png)

## 可视化查询分析

Kibana 拥有可视化统计分析数据的能力，单击左侧菜单【Visualize】， 可以配置各种可视化的图表进行数据的分析。
例如：要统计上文中，china 索引下的不同等级。

![选择饼图](https://main.qcloudimg.com/raw/86c8bb60ea6e6c9b253e6d6bef3a20a1.png)

![选择索引](https://main.qcloudimg.com/raw/5351e277f60483b019212079bf2fd561.png)

配置指标是 count，按字段 level.level 进行分组聚合统计，单击【Save】保存。

![配置聚合统计](https://main.qcloudimg.com/raw/fb99da54b85611504f715b73df6d0eef.png)

Kibana 其他使用方式，可以进一步了解 [Kibana 官方文档](https://www.elastic.co/guide/en/kibana/6.4/getting-started.html)。

