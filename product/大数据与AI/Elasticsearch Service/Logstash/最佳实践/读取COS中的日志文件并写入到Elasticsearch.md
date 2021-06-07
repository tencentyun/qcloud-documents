在某些场景中，业务服务端的日志或者是云上组件的日志会归档存储到对象存储COS中，在需要进行查询的时候需要从COS中获取并查询日志，此时可以借助于Logstash自动地读取COS中指定bucket的日志文件，然后写入到Elasticsearch中，再使用Kibana可视化组件进行查询和分析。

## 创建管道
在“管道管理”页面，点击“新建管道”按钮，创建一个管道：
![](https://main.qcloudimg.com/raw/4c13071ced72ce67a44092064e14b77f.png)

进入管道配置页面，点击“引用模板”按钮，同时引用“input-s3”和“output-elasticsearch”两个模板：
![](https://main.qcloudimg.com/raw/d9f18aae57a8d6c995633b5d9bda3df6.png)
![](https://main.qcloudimg.com/raw/1ef5faa2cf275499b3e674b40aac8d1d.png)

在管道配置中，分别针对“input-s3”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-s3

* access\_key\_id: 腾讯云账号的API密钥ID
* secret\_access\_key: 腾讯云账号的API密钥KEY
* endpoint: COS对象存储的访问地址，不通地域的地址不同，如广州地域为https://cos.ap-guangzhou.myqcloud.com
* bucket: COS对象存储的bucket
* region: COS对象存储bucket所在的地域，如ap-guangzhou
* prefix: 要读取的日志文件名称前缀

查看更多参数，可以参考[input-s3](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-s3.html)

### output-elasticsearch

* hosts: elasticsearch集群地址列表
* user: elasticsearch集群账号
* password: elasticsearch集群密码
* index: 索引名称
* document\_type: 索引type，对于不同版本的ES集群，该字段有不同的默认值，5.x及以下的集群，默认会使用input中指定的type字段，如果type字段不存在，则该字段的值为doc;6.x的集群，该字段默认值为doc；7.x的集群，该字段默认值为_doc; 8.x的集群，不会使用该字段
* document_id: 文档ID

查看更多参数，可以参考[output-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-outputs-elasticsearch.html)

在配置完管道后，点击“保存并部署”创建一个管道并自动部署:
![](https://main.qcloudimg.com/raw/58b261bae58e77a378b00acb64b8eb08.png)

## 查看日志

在控制台查看Logstash的运行日志，如果没有ERROR级别的日志，则说明管道运行正常：
![](https://main.qcloudimg.com/raw/f732f32b31dd83591e864cf3b7de7b2c.png)

## 查看数据写入情况
进入到output-elasticsearch中定义的输出端的ES集群对应的kibana页面，在Dev tools工具栏里查看索引是否存在，以及索引的文档数量是否正确：
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)
