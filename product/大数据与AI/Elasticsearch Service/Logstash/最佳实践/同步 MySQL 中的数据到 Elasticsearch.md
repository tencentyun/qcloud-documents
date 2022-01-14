使用 Logstash 可以把关系型数据库如 mysql、postgresql 中的数据同步到其它存储介质，下面介绍如何使用腾讯云 Logstash 同步 mysql 中的数据到 Elasticsearch。

## 创建管道
登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es/logstash)，选择需要操作的实例，单击实例【ID/名称】，进入实例基本信息页面。切换到“管道管理”页签，单击【新建管道】，创建一个管道。
![](https://main.qcloudimg.com/raw/123a56e009cd371e6ce7a498f79d49a1.png)
进入新建管道页面，单击【引用模板】，同时引用“input-jdbc”和“output-elasticsearch”两个模板：
![](https://main.qcloudimg.com/raw/b2f664a511a2ba7c603d832627b2b19b.png)
![](https://main.qcloudimg.com/raw/04ca52f36cf8e76895c50bfa2493613d.png)
在管道配置中，分别针对“input-jdbc”和“output-elasticsearch”进行配置，一些关键的配置参数说明如下：

### input-jdbc
- jdbc\_connection\_string：数据库连接地址
- jdbc\_user：数据库账号
- jdbc\_password：数据库账号密码
- jdbc\_driver_library：jdbc 驱动 jar 包，在 Logstash 节点的`/usr/local/service/logstash/extended-files`目录下，有大多数版本的 mysql 以及 postgresql 数据库的 jdbc 驱动 jar 包，可根据需要直接引用，可用的驱动 jar 包列表如下：
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
- jdbc\_driver\_class：jdbc 驱动类，对于 mysql 可填写“com.mysql.jdbc.Driver”，postgresql 可填写“org.postgresql.Driver”
- jdbc\_paging\_enabled：从数据库批量拉取数据时是否开启分页，可选值"true"或者"false"
- jdbc\_page\_size：jdbc 分页大小
- statement：用于拉取数据的 sql 语句
- tracking\_column：当在 statement 中指定了 sql\_last\_value 用于记录读取数据的 offset 时，使用数据库表中的哪个字段的值来记录 offset
- use\_column\_value：当在 statement 中指定了 sql\_last\_value 用于记录读取数据的 offset 时，是否使用数据库表中的字段；设置为 true 则使用 tracking_column 定义的字段，否则使用前一次 sql 语句执行时的时间戳
- schedule：是否开启定时任务持续执行 sql 语句，不设置的话则只会执行一次 sql 语句，执行结束后管道自动结束
- type：标识字段

查看更多参数的具体含义，详情可参见 [logstash-input-jdbc](https://www.elastic.co/guide/en/logstash/7.10/plugins-inputs-jdbc.html#plugins-inputs-jdbc-tracking_column)。

### output-elasticsearch
- hosts：elasticsearch 集群地址列表
- user：elasticsearch 集群账号
- password：elasticsearch 集群密码
- index：索引名称
- document\_type：索引 type，对于不同版本的 ES 集群，该字段有不同的默认值，5.x及以下版本的集群，默认会使用 input 中指定的 type 字段。如果 type 字段不存在，则该字段的值为 doc；6.x版本的集群，该字段默认值为 doc；7.x版本的集群，该字段默认值为\_doc；8.x版本的集群，不会使用该字段
- document_id：文档 ID

查看更多参数，详情可参见 [output-elasticsearch](https://www.elastic.co/guide/en/logstash/7.10/plugins-outputs-elasticsearch.html)。

在配置完管道后，单击【保存并部署】即可创建一个管道并自动部署。
![](https://main.qcloudimg.com/raw/4624ba100e9b21f31f63972c4be9d2c6.png)

## 实战案例
### 全量同步 mysql 表中的数据到 Elasticsearch
当 mysql 的某张表不再进行写入时，可使用如下配置全量地把数据同步到 Elasticsearch 集群中，管道配置如下：
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

### 增量同步 mysql 表中的数据到 Elasticsearch
当 mysql 的某张表在持续写入时，可使用如下配置，通过 sql\_last\_value 记录 offset，把数据增量地同步到 Elasticsearch 集群中，管道配置如下：
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
    schedule => "* * * * *"
    last_run_metadata_path => "/usr/local/service/logstash/temp/jdbc-sql_last_value.yml"
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
上述配置中指定了 tracking_column 为字段"id"，需要数据表中包含一个自增的"id"字段，当然可以根据实际情况使用不同的字段。

## 查看日志
在控制台中查看日志，如果没有 ERROR 级别的日志，则说明管道配置没有问题。
![](https://main.qcloudimg.com/raw/5e7e57882ac53f446b7e108b767a3c4e.png)

## 查看数据写入情况
进入到 output-elasticsearch 中定义的输出端的 ES 集群对应的 kibana 页面，在 Dev tools 工具栏里查看索引是否存在，以及索引的文档数量是否正确。
![](https://main.qcloudimg.com/raw/015063d8147cbd78ed18f046417b7a7a.png)
