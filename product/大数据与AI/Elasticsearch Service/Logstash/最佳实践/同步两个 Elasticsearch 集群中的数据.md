使用 Logstash 可以完成同步两个 Elasticsearch 集群中的数据，例如把数据从自建的 Elasticsearch 集群同步到腾讯云上的 Elasticsearch 集群，或者同步两个腾讯云上的 Elasticsearch 集群中的数据。下面介绍如何使用腾讯云 Logstash 同步两个 Elasticsearch 集群中的数据。

## 创建管道
登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，选择需要操作的实例，单击实例 **ID/名称**，进入实例基本信息页面。切换到“管道管理”页签，单击**新建管道**，创建一个管道。
![](https://main.qcloudimg.com/raw/123a56e009cd371e6ce7a498f79d49a1.png)
进入新建管道页面，单击**引用模板**，同时引用“input-elasticsearch”和“output-elasticsearch”两个模板：
![](https://main.qcloudimg.com/raw/b2f664a511a2ba7c603d832627b2b19b.png)
![](https://main.qcloudimg.com/raw/3ff3d5eac3201d3b429346c5da8ece70.png)

在管道配置中，分别针对“input-elasticsearch”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-elasticsearch
- hosts：elasticsearch 集群地址列表
- user：elasticsearch 集群账号
- password：elasticsearch 集群密码
- index：索引名称
- query：es 查询语句，用于查询某一部分的数据
- schedule：是否开启定时任务持续从 elasticsearch 集群中拉取数据，如果不配置，则只会拉取一次
- scroll：批量从 elasticsearch 集群中拉取数据时，用于保持 scroll context 的时间，默认为"1m"
- size：批量从 elasticsearch 集群中拉取数据时，每个批次拉取多少条数据，默认为1000
- type：标识字段
- docinfo：是否在 event 中填充索引名称，type 以及 id 等文档元信息，默认为 false

查看更多参数，详情可参见 [input-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-inputs-elasticsearch.html#plugins-inputs-elasticsearch-index)。

### output-elasticsearch
- hosts：elasticsearch 集群地址列表
- user：elasticsearch 集群账号
- password：elasticsearch 集群密码
- index：索引名称
- document\_type：索引 type，对于不同版本的 ES 集群，该字段有不同的默认值，5.x及以下版本的集群，默认会使用 input 中指定的 type 字段。如果 type 字段不存在，则该字段的值为 doc；6.x版本的集群，该字段默认值为 doc；7.x版本的集群，该字段默认值为\_doc；8.x版本的集群，不会使用该字段
- document_id：文档 ID

查看更多参数，详情可参见 [output-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-outputs-elasticsearch.html)。

在配置完管道后，单击**保存并部署**即可创建一个管道并自动部署。
![](https://main.qcloudimg.com/raw/4624ba100e9b21f31f63972c4be9d2c6.png)

## 查看日志
在控制台查看 Logstash 的运行日志，如果没有 ERROR 级别的日志，则说明管道运行正常。
![](https://main.qcloudimg.com/raw/0e5944ab1f376bea38de7855cad69649.png)

## 查看数据写入情况
进入到 output-elasticsearch 中定义的输出端的 ES 集群对应的 kibana 页面，在 Dev tools 工具栏里查看索引是否存在，以及索引的文档数量是否正确：
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)
