
## 前言 
CTSDB 是一款分布式、可扩展、支持近实时数据搜索与分析的时序数据库，且兼容 Elasticsearch 常用的 API 接口。对于很多用户，想要将 MySQL 中的数据导入到 CTSDB 中，而又找不到一种较好的方法，这里给出一种简单快捷的方式，轻松将 MySQL 中的数据同步到 CTSDB。

## 工具介绍 
go-mysql-elasticsearch 是一款开源的高性能的 MySQL 数据同步 Elasticsearch 的工具，其由 go 语言开发，编译及使用都非常简单。go-mysql-elasticsearch 的原理也很简单，首先使用 mysqldump 获取当前 MySQL 的数据，然后在通过此时 binlog 的 name 和 position 获取增量数据，再根据 binlog 构建 restful api 写入数据到 Elasticsearch 中。由于 CTSDB 基于 Elasticsearch 开发，因此，可以完美对接 go-mysql-elasticsearch，导入 MySQL 数据。

## MySQL 数据同步 CTSDB 步骤 
### MySQL 样例数据构建 
既然读者有 MySQL 导入 CTSDB 的需求，那 MySQL 的安装就不用多说了。这里为了整个流程的完整性，就从样例数据的灌入开始，用 go 写了一个小工具，生成一些样例数据并灌入到 MySQL 中，表结构如下： 
```
    mysql> desc test_table;
	+-----------+-------------+------+-----+---------+----------------+
	| Field     | Type        | Null | Key | Default | Extra          |
	+-----------+-------------+------+-----+---------+----------------+
	| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
	| timestamp | bigint(20)  | YES  |     | NULL    |                |
	| cpu_usage | float       | YES  |     | NULL    |                |
	| host_ip   | varchar(20) | YES  |     | NULL    |                |
	| region    | varchar(20) | YES  |     | NULL    |                |
	+-----------+-------------+------+-----+---------+----------------+
```
以上创建了一个名为 test_table 的表，然后向该表灌入2000条样例数据，部分数据如下所示： 
```
    mysql> select * from test_table;
    +------+------------+-----------+-------------+-----------+
    | id   | timestamp  | cpu_usage | host_ip | region|
    +------+------------+-----------+-------------+-----------+
    |1 | 1527676339 |  0.23 | 192.168.1.1 | beijing   |
    |2 | 1527676399 |  0.78 | 192.168.1.2 | shanghai  |
    |3 | 1527676459 |   0.2 | 192.168.1.3 | guangzhou |
    |4 | 1527676519 |  0.47 | 192.168.1.4 | shanghai  |
    |5 | 1527676579 |  0.13 | 192.168.1.5 | beijing   |
    |6 | 1527676639 |  0.15 | 192.168.1.1 | beijing   |
    |7 | 1527676699 |  0.07 | 192.168.1.2 | shanghai  |
    |8 | 1527676759 |  0.17 | 192.168.1.3 | guangzhou |
    |9 | 1527676819 |  0.94 | 192.168.1.4 | shanghai  |
    |10| 1527676879 |  0.06 | 192.168.1.5 | beijing   |
```
至此，MySQL 端的样例数据准备完毕。

### CTSDB metric 创建 
 现在，我们在 CTSDB 上创建一个和 MySQL 一样的表结构，用于存储对应的数据，创建接口如下所示： 
```
    POST /_metric/test_metric
	{
	  "time": {
	    "name": "timestamp",   # 与 MySQL 表中的 timestamp 对应，CTSDB 常用的时间域
	    "format": "strict_date_optional_time || epoch_second"
	  },
	  "tags": {
	    "region": "string",
	    "host_ip": "string"
	  },
	  "fields": {
	    "cpu_usage": "float"   # fields 域代表指标列，很明显 cpu_usage 代表需要监控 CPU 使用率指标
	  }
	}
```
至此，CTSDB 中的表结构也准备好了，下面我们使用 go-mysql-elasticsearch 来同步数据。

### go-mysql-elasticsearch 使用  
由于 go-mysql-elasticsearch 是用 go 语言开发，因此首先安装 go，官方要求的版本是 1.6 以上，go 的安装非常简单，参考官方文档 [下载](https://golang.org/dl/)、[安装](https://golang.org/doc/install#install)，然后开始安装 go-mysql-elasticsearch，整个步骤如下：
```
$ go get github.com/siddontang/go-mysql-elasticsearch
$ cd $GOPATH/src/github.com/siddontang/go-mysql-elasticsearch
$ make
```
工具安装好后，需要进行一些合理地配置我们才能愉快地使用，下面将会给出一个配置范例，并给予相应地注释说明：
```
 # 注意：go-mysql-elasticsearch 的默认配置文件在 go-mysql-elasticsearch/etc/river.toml
	# MySQL address, user and password
	# user must have replication privilege in MySQL.
	my_addr = "127.0.0.1:3306"
	my_user = "root"
	my_pass = "123456"
	my_charset = "utf8"
	# Set true when elasticsearch use https
	#es_https = false
	# CTSDB 地址
	es_addr = "9.6.174.42:13982"
	# 如果使用的是带权限的 CTSDB，需要设置用户名和密码
	es_user = "root"
	es_pass = "changeme"
	# Path to store data, like master.info, if not set or empty,
	# we must use this to support breakpoint resume syncing. 
	# TODO: support other storage, like etcd. 
	data_dir = "./var"  # 存储的是 binlog 的名字及位置
	# Inner http status address
	stat_addr = "127.0.0.1:12800"
	# pseudo server id like a slave 
	server_id = 1001
	# mysql or mariadb
	flavor = "mysql"
	# mysqldump execution path
	# if not set or empty, ignore mysqldump.
	mysqldump = "mysqldump"
	# minimal items to be inserted in one bulk
	bulk_size = 512
	# force flush the pending requests if we don't have enough items >= bulk_size
	flush_bulk_time = "200ms"
	# Ignore table without primary key
	skip_no_pk_table = true
	# MySQL data source
	[[source]]
	schema = "mysql_es"
	# Only below tables will be synced into Elasticsearch.
	# "t_[0-9]{4}" is a wildcard table format, you can use it if you have many sub tables, like table_0000 - table_1023
	# I don't think it is necessary to sync all tables in a database.
	tables = ["test_*"]
	[[rule]]
	schema = "mysql_es"   # MySQL 数据库名
	table = "test_table"  # MySQL 表名
	index = "test_metric"  # CTSDB 中 metric 名
	type = "doc"          # 文档类型
```
以上配置，为测试所使用的配置，如果您有更高级的需求可以参考官方文档，合理进行配置。配置 ok 后，我们来运行 go-mysql-elasticsearch，如下所示： 
```
    $  ./bin/go-mysql-elasticsearch -config=./etc/river.toml
    2018/05/31 21:43:44 INFO  create BinlogSyncer with config {1001 mysql 127.0.0.1 3306 root   utf8 false false <nil> false false 0 0s 0s 0}
    2018/05/31 21:43:44 INFO  run status http server 127.0.0.1:12800
    2018/05/31 21:43:44 INFO  skip dump, use last binlog replication pos (mysql-bin.000002, 194296) or GTID %!s(<nil>)
    2018/05/31 21:43:44 INFO  begin to sync binlog from position (mysql-bin.000002, 194296)
    2018/05/31 21:43:44 INFO  register slave for master server 127.0.0.1:3306
    2018/05/31 21:43:44 INFO  start sync binlog at binlog file (mysql-bin.000002, 194296)
    2018/05/31 21:43:44 INFO  rotate to (mysql-bin.000002, 194296)
    2018/05/31 21:43:44 INFO  rotate binlog to (mysql-bin.000002, 194296)
    2018/05/31 21:43:44 INFO  save position (mysql-bin.000002, 194296)
```

这里需要注意 ，由于 go-mysql-elasticsearch 需要利用 binlog，而且 binlog 一定要变成 row-based format 格式，因此在 MySQL 必须配置如下参数： 
```
# binlog 参数必须要配置如下：
log_bin=mysql-bin
binlog_format = ROW
server-id=1
```
现在，我们来看一下 CTSDB 中是否成功导入了 MySQL 中的数据： 
```
    GET test_metric/_search?size=1000
    {
      "sort": [
    {
      "timestamp": {
    "order": "desc"
      }
    }
      ], 
      "docvalue_fields": ["timestamp", "host_ip", "region", "cpu_usage"]
    }
    #结果：
    {
      "took": 8,
      "timed_out": false,
      "_shards": {
    "total": 3,
    "successful": 3,
    "skipped": 0,
    "failed": 0
      },
      "hits": {
    "total": 2000,
    "max_score": null,
    "hits": [
      {
    "_index": "test_metric@1525363200000_30",
    "_type": "doc",
    "_id": "2000",
    "_score": null,
    "fields": {
      "host_ip": [
    "192.168.1.5"
      ],
      "region": [
    "beijing"
      ],
      "cpu_usage": [
    0.05000000074505806
      ],
      "timestamp": [
    1527807286000
      ]
    },
    "sort": [
      1527807286000
    ]
      },
      ......
    }
```

## 小结 
可以看到，使用 go-mysql-elasticsearch，仅需要在配置文件里面写规则，就能非常方便的将数据从 MySQL 同步给 ES。上面仅举了一些简单的例子，如果有更多的需求可以参考 go-mysql-elasticsearch的官方文档。

除了本文所介绍的工具外，这里再推荐两种工具：
- py-mysql-elasticsearch-sync，该工具是使用 Python语言编写，与 go-mysql-elasticsearch 的原理类似，都是使用 binlog 来实现数据的同步，安装及使用见 [官方文档 ](https://github.com/zhongbiaodev/py-mysql-elasticsearch-sync)。
- logstash，使用 logstash 同步数据时需要安装 logstash-input-jdbc、logstash-output-elasticsearch 两个插件，具体使用参考 [官方文档](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-jdbc.html)  、[elastic 官方文档](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-elasticsearch.html)。
如果您在使用上述工具中遇到问题，可通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 解决。
