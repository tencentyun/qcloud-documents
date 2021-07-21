在某些场景中，业务服务端或云上组件的日志会归档存储到对象存储 COS 中，在需要进行查询时，需要从 COS 中获取并查询日志。此时，可借助 Logstash 自动地读取 COS 中指定 bucket 的日志文件，然后写入到 Elasticsearch 中，再使用 Kibana 可视化组件进行查询和分析。

## 创建管道
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，选择需要操作的实例，单击实例【ID/名称】，进入实例基本信息页面。
2. 在“实例基本信息”页，切换到“管道管理”页，单击【新建管道】，进入新建管道页面。
![](https://main.qcloudimg.com/raw/4c13071ced72ce67a44092064e14b77f.png)
3. 在“新建管道”页面，单击【引用模板】，同时引用“input-s3”和“output-elasticsearch”两个模板。
![](https://main.qcloudimg.com/raw/d9f18aae57a8d6c995633b5d9bda3df6.png)
![](https://main.qcloudimg.com/raw/1ef5faa2cf275499b3e674b40aac8d1d.png)

在管道配置中，分别针对“input-s3”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-s3
- access\_key\_id：腾讯云账号的 API 密钥 ID
- secret\_access\_key：腾讯云账号的 API 密钥 KEY
* endpoint：COS 对象存储的访问地址，不同地域的地址不同，如广州地域为 `https://cos.ap-guangzhou.myqcloud.com`
* bucket：COS 对象存储的 bucket
* region：COS 对象存储 bucket 所在的地域，如 ap-guangzhou
* prefix：要读取的日志文件名称前缀

查看更多参数，详情可参见 [input-s3](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-s3.html)。

### output-elasticsearch
* hosts：elasticsearch 集群地址列表
* user：elasticsearch 集群账号
* password：elasticsearch 集群密码
* index：索引名称
* document\_type：索引 type，对于不同版本的 ES 集群，该字段有不同的默认值，5.x及以下的集群，默认会使用 input 中指定的 type 字段，如果 type 字段不存在，则该字段的值为 doc；6.x的集群，该字段默认值为 doc；7.x的集群，该字段默认值为\_doc；8.x的集群，不会使用该字段
* document_id：文档 ID

查看更多参数，详情可参见 [output-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-outputs-elasticsearch.html)。

在配置完管道后，单击【保存并部署】即可创建一个管道并自动部署。
![](https://main.qcloudimg.com/raw/58b261bae58e77a378b00acb64b8eb08.png)

## 查看日志
在控制台查看 Logstash 的运行日志，如果没有 ERROR 级别的日志，则说明管道运行正常。
![](https://main.qcloudimg.com/raw/f732f32b31dd83591e864cf3b7de7b2c.png)

## 查看数据写入情况
进入到 output-elasticsearch 中定义的输出端的 ES 集群对应的 kibana 页面，在 Dev tools 工具栏里查看索引是否存在，以及索引的文档数量是否正确。
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)
