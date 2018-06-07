# 1.前言 #
CTSDB是一款分布式、可扩展、支持近实时数据搜索与分析的时序数据库，且兼容Elasticsearch常用的API接口。对于很多用户，想要将Mysql中的数据导入到CTSDB中，而又找不到一种较好的方法，笔者这里给出一种简单快捷的方式，轻松将Mysql中的数据同步到CTSDB。
# 2.工具介绍 --- go-mysql-elasticsearch #
go-mysql-elasticsearch是一款开源的高性能的Mysql数据同步Elasticsearch的工具，其由go语言开发，编译及使用非常简单。go-mysql-elasticsearch的原理很简单，首先使用mysqldump获取当前MySQL的数据，然后在通过此时binlog的name和position获取增量数据，再根据binlog构建restful api写入数据到Elasticsearch中。由于CTSDB基于Elasticsearch开发，因此，可以完美对接go-mysql-elasticsearch，导入Mysql数据。下面笔者将会给出详细的使用步骤。
# 3.Mysql数据同步CTSDB步骤 #
## 3.1 Mysql样例数据构建 ##
既然读者有Mysql导入CTSDB的需求，那Mysql的安装就不用多说了。这里笔者为了整个流程的完整性，就从样例数据的灌入开始，笔者用go写了一个小工具，生成一些样例数据并灌入到Mysql中，表结构如下：<br>
	
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
以上创建了一个名为test_table的表，然后向该表灌入2000条样例数据，部分数据如下所示：<br>

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
    |   10 | 1527676879 |  0.06 | 192.168.1.5 | beijing   |
至此，Mysql端的样例数据准备完毕。
## 3.2 CTSDB metric创建 ##
 现在，我们在CTSDB上创建一个和Mysql一样的表结构，用于存储对应的数据，创建接口如下所示：<br>

    POST /_metric/test_metric
	{
	  "time": {
	    "name": "timestamp",   # 与Mysql表中的timestamp对应，CTSDB常用的时间域
	    "format": "strict_date_optional_time || epoch_second"
	  },
	  "tags": {
	    "region": "string",
	    "host_ip": "string"
	  },
	  "fields": {
	    "cpu_usage": "float"   # fields域代表指标列，很明显cpu_usage代表需要监控cpu使用率指标
	  }
	}
至此，CTSDB中的表结构也准备好了，下面我们使用go-mysql-elasticsearch来同步数据。
## 3.3 go-mysql-elasticsearch使用 ##
由于go-mysql-elasticsearch是用go语言开发，因此首先安装go，官方要求的版本是1.6以上，go的安装非常简单，参考官方文档，下载：https://golang.org/dl/， 安装：https://golang.org/doc/install#install， 然后开始安装 go-mysql-elasticsearch，整个步骤如下：<br>

    $ go get github.com/siddontang/go-mysql-elasticsearch
	$ cd $GOPATH/src/github.com/siddontang/go-mysql-elasticsearch
	$ make
工具安装好后，需要进行一些合理地配置我们才能愉快地使用，下面笔者将会给出一个配置范例，并给予相应地注释说明：<br>

    `# 注意：go-mysql-elasticsearch的默认配置文件在go-mysql-elasticsearch/etc/river.toml
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
	# 如果使用的是带权限的CTSDB，需要设置用户名和密码
	es_user = "root"
	es_pass = "changeme"
	# Path to store data, like master.info, if not set or empty,
	# we must use this to support breakpoint resume syncing. 
	# TODO: support other storage, like etcd. 
	data_dir = "./var"  # 存储的是binlog的名字及位置
	# Inner Http status address
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
	skip_no_pk_table = true  # 这里需要注意，go-mysql-elasticsearch会
	# MySQL data source
	[[source]]
	schema = "mysql_es"
	# Only below tables will be synced into Elasticsearch.
	# "t_[0-9]{4}" is a wildcard table format, you can use it if you have many sub tables, like table_0000 - table_1023
	# I don't think it is necessary to sync all tables in a database.
	tables = ["test_*"]
	[[rule]]
	schema = "mysql_es"   # Mysql数据库名
	table = "test_table"  # Mysql表名
	index = "test_metric"  # CTSDB中metric名
	type = "doc"          # 文档类型`
以上配置，为笔者测试所使用的配置，如果用户有更高级的需求可以参考官方文档，合理进行配置。配置ok后，我们来运行go-mysql-elasticsearch，如下所示：<br>

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
这里需要 注意 ，由于go-mysql-elasticsearch需要利用binlog，而且binlog一定要变成row-based format格式，同时需要用到canal组件来同步数据（canal模拟mysql slave的交互协议，伪装自己为mysql slave，向mysql master发送dump协议），因此在Mysql必须配置如下参数：<br>

    # 以下参数需要配置，否则必踩坑
    log_bin=mysql-bin
    binlog_format = ROW
    server-id=1
现在，我们来看看CTSDB中是否成功导入了Mysql中的数据：<br>

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
# 4.小结 #
可以看到，使用 go-mysql-elasticsearch，我们仅需要在配置文件里面写规则，就能非常方便的将数据从 MySQL 同步给 ES。上面仅仅举了一些简单的例子，如果有更多的需求可以参考 go-mysql-elasticsearch的官方文档。 <br>
除了本文所介绍的工具外，这里再推荐两种工具，一个是 py-mysql-elasticsearch-sync，该工具是使用python语言编写，与go-mysql-elasticsearch的原理类似，都是利用binlog来实现数据的同步，安装及使用见官方文档https://github.com/zhongbiaodev/py-mysql-elasticsearch-sync； 另一个工具是logstash，使用logstash同步数据时需要安装logstash-input-jdbc、logstash-output-elasticsearch两个插件，具体使用参考官方文档https://www.elastic.co/guide/en/logstash/current/plugins-inputs-jdbc.html 、https://www.elastic.co/guide/en/logstash/current/plugins-outputs-elasticsearch.html <br> 
如果你在使用上述工具中遇到问题，欢迎提工单联系我们。