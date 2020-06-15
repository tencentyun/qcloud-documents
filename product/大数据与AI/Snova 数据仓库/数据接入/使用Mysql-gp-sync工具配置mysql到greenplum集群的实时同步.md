#### 背景说明

目前现网greenplum集群需要实时同步来自mysql的数据变更，这里提供一个实时同步工具

**说明:** 该工具是根据github.com/siddontang/go-mysql-elasticsearch和github.com/frainmeng/go-mysql-elasticsearch的mysql开源工具修改扩展而来，可以支持根据mysql数据库的bin_log实时同步DML变更到对应的greenplum集群中

**注意:** 该工具仅支持一个mysql源和一个greenplum集群之间的同步,目前仅支持表粒度的同步,并且无法同步表DDL结构变更，在开启实时同步前需要预先在greenplum集群迁移历史数据。

#### 部署实时同步步骤

建议的同步方式:

1.首先迁移历史数据，在迁移历史数据时，需要首先进行停服操作，停下服务后，记录下目前的binlog信息,可以用如下命令进行查询

```
show master status;
```

2.在greenplum集群上创建需要需要迁移的表，使用datax工具进行批量导入

3.配置binlog的pos信息，然后部署启动mysql-gp-sync服务

#### 同步前mysql数据库配置

该同步工具需要基于mysql binlog同步机制，所以需要开启mysql binlog功能，并且需要将将binlog格式切换为row模式,可以通过下述两条语句查询binlog设置

```shell
show variables like 'log_bin';
show variables like 'binlog_format';
```

腾讯云binlog设置文档:https://cloud.tencent.com/developer/article/1464748

#### mysql-gp-sync服务部署

下载安装包 mysql-gp-sync.zip,并且部署在一台linux服务器上,解压

解压后可以看到多个文件,其中mysql-gp-sync.toml是服务配置文件，配置文件示例如下:

```toml
# 需要进行同步数据的源端mysql
mysql_addr = "127.0.0.1:3306"
mysql_user = "root"
mysql_pass = "123456"
mysql_charset = "utf8"

# 目的端greenplum连接配置
pg_host = "139.155.20.126"
pg_port = 5432
pg_user = "gpadmin"
pg_pass = "123456"
pg_dbname = "qidian_api"

# 存放已经完成同步的位移点的文件目录(binlog同步pos和进程文件)
data_dir = "./var"

# statsd监控地址，如果部署了statsd服务会发起推送
statsd_host = "127.0.0.1"
statsd_port = 8125
statsd_prefix = "dbsync"

# 伪装成slave时候，配置的server-id,针对同一mysql集群配置的不同的同步进程id需要不一致
server_id = 1001
flavor = "mysql"

# 是否忽略没有主键的表
skip_no_pk_table = false

# 并发配置
# 并发线程数
concurrent_size = 6

#并发缓冲区大小，尽量设置为并发线程数的整数倍
concurrent_ack_win = 2048


# MySQL 数据源配置，支持多个db和表
[[source]]
schema = "advanced"
tables = ["t_user"]


# MySQL 数据到 PG 后的分发规则,支持多个表
[[rule]]
#mysql 库表的配置
schema = "advanced"
table = "t_user"
# pg 库表的配置
pg_schema = "public"
pg_table = "t_user"
```

配置参数说明:

| 字段          | 说明                |
| ------------- | ------------------- |
| mysql_addr    | mysql服务器网络地址 |
| mysql_user    | mysql_pass          |
| mysql_pass    | 123456              |
| mysql_charset | mysql编码           |

| 字段      | 说明                             |
| --------- | -------------------------------- |
| pg_host   | greenplum master节点服务地址     |
| pg_port   | greenplum master节点服务端口     |
| pg_user   | greenplum master数据库连接用户名 |
| pg_pass   | greenplum master数据库连接密码   |
| pg_dbname | greenplum postgresql 数据库密码  |

| 字段          | 说明                                        |
| ------------- | ------------------------------------------- |
| data_dir      | 存放一些记录文件,比如进程号和bin_log同步pos |
| statsd_host   | statsd监控地址(如果部署)                    |
| statsd_port   | statsd监控端口(如果部署)                    |
| statsd_prefix | dbsync                                      |

| 字段               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| server_id          | 作为mysql的slaverid,针对同一mysql源不同的进程需要配置不同的集群 |
| flavor             | 可填mysql或者mariadb                                         |
| skip_no_pk_table   | 是否忽略没有主键的表                                         |
| concurrent_size    | 并发线程数                                                   |
| concurrent_ack_win | 并发缓冲区大小，需要设置为并发线程数的整数倍                 |

| 表数组                          | 字段      | 说明                   |
| ------------------------------- | --------- | ---------------------- |
| source(表示需要监听的mysql库表) | schema    | mysql数据库配置        |
| source                          | tables    | 数组，需要同步的表列表 |
| rule(表示映射规则)              | schema    | 需要映射的mysql数据库  |
| rule                            | table     | 需要映射的mysql表      |
| rule                            | pg_schema | 映射到的schema         |
| rule                            | pg_table  | 映射到的表             |

#### 设置当前bin_log偏移量

./var目录中存在一个master.info文件,里面配置如下

```
bin_name = "mysql-bin.000005"
bin_pos = 708735
```

表示从bin_name这个文件的708735 postion开始进行同步

**注意** 如果不配置该文件,会从头开始进行同步,每次同步后服务会更新该文件信息

#### 启动和停止mysql-gp-sync

在命令行文件夹中执行:

```
./start.sh
```

可以启动服务进程

在命令行文件夹中执行:

```
./stop.sh
```

可以终止服务进程

#### 服务定时监控重启

服务进程可能由于一些故障原因重启，为了能够降低人工处理的复杂度，可以通过配置crontab来进行自动进程监控重启,配置示例如下:

```
crontab -e
增加下面这行，表示1分钟检查一次，注意这里需要填写部署的路径
*/1 * * * * /Users/Downloads/mysql-gp-sync/monitor_process.sh
```

#### 日志查错

在部署路径中有一个sync.log文件会实时打印程序执行的步骤，当进程出错退出时，可以用于定位问题



