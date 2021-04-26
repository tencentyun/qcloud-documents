使用Logstash也可以把关系型数据库如mysql, postgresql中的数据同步到其它存储介质，下面介绍如何使用腾讯云Logstash同步mysql中的数据到Elasticsearch。

## 创建管道
在“管道管理”页面，点击“新建管道”按钮，创建一个管道：
![](https://main.qcloudimg.com/raw/4c13071ced72ce67a44092064e14b77f.png)

进入管道配置页面，点击“引用模板”按钮，同时引用“input-jdbc”和“output-elasticsearch”两个模板：
![](https://main.qcloudimg.com/raw/d9f18aae57a8d6c995633b5d9bda3df6.png)
![](https://main.qcloudimg.com/raw/beaa5a9747304572b81227604d253214.png)

在管道配置中，分别针对“input-jdbc”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-jdbc

* jdbc\_connection\_string：数据库连接地址
* jdbc\_user: 数据库账号
* jdbc\_password: 数据库账号密码
* jdbc\_driver_library: jdbc驱动jar包，在Logstash节点的/usr/local/service/logstash/extended-files目录下，有大多数版本的mysql以及postgresql数据库的jdbc驱动jar包，可根据需要直接引用，可用的驱动jar包列表如下:
	- mysql-connector-java-5.1.27.jar
	- mysql-connector-java-5.1.35.jar
	- mysql-connector-java-5.1.39-bin.jar
	- mysql-connector-java-5.1.39.jar
	- mysql-connector-java-5.1.40.jar
	- mysql-connector-java-5.1.43.jar
	- mysql-connector-java-5.1.47.jar
	- mysql-connector-java-5.1.48.jar
	- mysql-connector-java-5.1.9.jar
	- mysql-connector-java-6.0.2.jar
	- mysql-connector-java-6.0.6.jar
	- mysql-connector-java-8.0.11.jar
	- mysql-connector-java-8.0.17.jar
	- mysql-connector-java-8.0.18.jar
	- postgresql-42.0.0.jar
	- postgresql-42.1.4.jar
	- postgresql-42.2.0.jar
	- postgresql-42.2.10.jar
	- postgresql-42.2.13.jar
	- postgresql-42.2.1.jar
	- postgresql-42.2.8.jar
* jdbc\_driver\_class: jdbc驱动类，对于mysql可填写“com.mysql.jdbc.Driver”，postgresql可填：“org.postgresql.Driver”
* jdbc\_paging\_enabled： 从数据库批量拉取数据时是否开启分页，可选值"true"或者"false"
* jdbc\_page\_size: jdbc分页大小
* statement: 用于拉取数据的sql语句
* tracking\_column: 当在statement中指定了sql\_last\_value用于记录读取数据的offset时，使用数据库表中的哪个字段的值来记录offset
* use\_column\_value: 当在statement中指定了sql\_last\_value用于记录读取数据的offset时，是否使用数据库表中的字段；设置为true则使用tracking_column定义的字段，否则使用前一次sql语句执行时的时间戳
* schedule：是否开启定时任务持续执行sql语句，不设置的话则只会执行一次sql语句，执行结束后管道自动结束
* type：标识字段

查看更多参数的具体含义，请参考[logstash-input-jdbc](https://www.elastic.co/guide/en/logstash/7.10/plugins-inputs-jdbc.html#plugins-inputs-jdbc-tracking_column)

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

## 实战案例

### 全量同步mysql表中的数据到Elasticsearch
当mysql某张表不再进行写入时，可以使用如下配置全量地把数据同步到Elasticsearch集群中，管道配置如下：

```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://x.x.x.x:3306/logstash_test"
    jdbc_user => "user"
    jdbc_password => "xxxxx"
    jdbc_driver_library => "/usr/local/service/logstash/extended-files/mysql-connector-java-5.1.40.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_paging_enabled => "true"
    jdbc_page_size => "5000"
    statement => "select * from newTable0"
    type => "jdbc"
  }
}
output {
    elasticsearch {
        hosts => ["http://x.x.x.x:9200"]
        user => "elastic"
        password => "xxxxx"
        index => "newTable0"
    }
}
```

### 增量同步mysql表中的数据到Elasticsearch
当mysql某张表在持续进行写入，可以使用如下配置，通过sql\_last\_value记录offset，把数据增量地同步到Elasticsearch集群中，管道配置如下：

```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://x.x.x.x:3306/logstash_test"
    jdbc_user => "user"
    jdbc_password => "xxxxx"
    jdbc_driver_library => "/usr/local/service/logstash/extended-files/mysql-connector-java-5.1.40.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
    jdbc_paging_enabled => "true"
    jdbc_page_size => "5000"
    statement => "select * from newTable0 where id > :sql_last_value"
    use_column_value => true
    tracking_column => "id"
    type => "jdbc"
  }
}
output {
    elasticsearch {
        hosts => ["http://x.x.x.x:9200"]
        user => "elastic"
        password => "xxxxx"
        index => "newTable0"
    }
}
```
注意，上述配置中指定了tracking_column为字段"id"， 需要数据表中包含一个自增的"id"字段，当然可以根据实际情况使用不同的字段。


## 查看日志
在控制台中，查看日志，如果没有ERROR级别的日志，则说明管道配置没有问题：
![](https://main.qcloudimg.com/raw/5e7e57882ac53f446b7e108b767a3c4e.png)

## 查看数据写入情况
进入到output-elasticsearch中定义的输出端的ES集群对应的kibana页面，在Dev tools工具栏里查看索引是否存在，以及索引的文档数量是否正确：
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)