使用Logstash也可以完成同步两个Elasticsearch集群中的数据，比如把数据从自建的Elasticsearch集群同步到腾讯云上的Elasticsearch集群，或者同步两个腾讯云上的Elasticsearch集群中的数据。

## 创建管道
在“管道管理”页面，点击“新建管道”按钮，创建一个管道：
![](https://main.qcloudimg.com/raw/4c13071ced72ce67a44092064e14b77f.png)

进入管道配置页面，点击“引用模板”按钮，同时引用“input-elasticsearch”和“output-elasticsearch”两个模板：
![](https://main.qcloudimg.com/raw/d9f18aae57a8d6c995633b5d9bda3df6.png)
![](https://main.qcloudimg.com/raw/adc196cb94e5456976129df1ae07bab4.png)

在管道配置中，分别针对“input-elasticsearch”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-elasticsearch

* hosts: elasticsearch集群地址列表
* user: elasticsearch集群账号
* password: elasticsearch集群密码
* index: 索引名称
* query: es查询语句，用于查询某一部分的数据
* schedule: 是否开启定时任务持续从elasticsearch集群中拉取数据，如果不配置，则只会拉取一次
* scroll: 批量从elasticsearch集群中拉取数据时，用于保持scroll context的时间，默认为"1m"
* size: 批量从elasticsearch集群中拉取数据时，每个批次拉取多少条数据，默认为1000
* type: 标识字段
* docinfo: 是否在event中填充索引名称，type以及id等文档元信息，默认为false

查看更多参数，可以参考[input-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-inputs-elasticsearch.html#plugins-inputs-elasticsearch-index)

### output-elasticsearch

* hosts: elasticsearch集群地址列表
* user: elasticsearch集群账号
* password: elasticsearch集群密码
* index: 索引名称
* document\_type: 索引type，对于不同版本的ES集群，该字段有不同的默认值，5.x及以下的集群，默认会使用input中指定的type字段，如果type字段不存在，则该字段的值为doc;6.x的集群，该字段默认值为doc；7.x的集群，该字段默认值为_doc; 8.x的集群，不会使用该字段
* document_id: 文档ID

查看更多参数，可以参考[output-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-outputs-elasticsearch.html)

在配置完管道后，点击“保存并部署”创建一个管道并自动部署:
![](https://main.qcloudimg.com/raw/fb4a7d0144255af5a11f44d9966c866b.png)

## 查看日志
在控制台查看Logstash的运行日志，如果没有ERROR级别的日志，则说明管道运行正常：
![](https://main.qcloudimg.com/raw/0e5944ab1f376bea38de7855cad69649.png)
## 查看数据写入情况

进入到output-elasticsearch中定义的输出端的ES集群对应的kibana页面，在Dev tools工具栏里查看索引是否存在，以及索引的文档数量是否正确：
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)