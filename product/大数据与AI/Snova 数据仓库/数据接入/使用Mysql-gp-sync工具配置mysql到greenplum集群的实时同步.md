## 背景说明
目前云数据仓库 PostgreSQL 集群需要实时同步来自 mysql 的数据变更，这里提供一个实时同步工具。
- 此工具是根据 [Sync MySQL data into elasticsearch](https://github.com/siddontang/go-mysql-elasticsearch) 和 [Sync MySQL data into elasticsearch or postgresql](https://github.com/frainmeng/go-mysql-elasticsearch) 的 mysql 开源工具修改扩展而来，可支持根据 mysql 数据库的 bin_log 实时同步 DML 变更到对应的云数据仓库 PostgreSQL 集群中。
- 此工具仅支持一个 mysql 源和一个云数据仓库 PostgreSQL 集群之间的同步，目前仅支持表粒度的同步，并且无法同步表 DDL 结构变更，在开启实时同步前需要预先在云数据仓库 PostgreSQL 集群迁移历史数据。

#### 工具下载
[mysql-gp-sync.zip](https://packagedown-online-1256722404.cos.ap-guangzhou.myqcloud.com/sync/mysql-gp-sync-1.2.1.zip)

#### 实时同步限制
- 需同步的 mysql 表必须包含主键。
- 暂不支持同步 mysql 表前缀索引。
- 暂不支持同步 DDL 操作。
- 暂时只能支持一个 MySQL 集群和一个云数据仓库 PostgreSQL 集群的同步。

## 部署实时同步步骤
1. 迁移历史数据。在迁移历史数据时，需要首先进行停服操作。停服后，记录下目前的 binlog 信息，可以用如下命令进行查询。
```
show master status;
```
2. 在云数据仓库 PostgreSQL 集群上创建需要迁移的表，使用 datax 工具进行批量导入。
3. 配置 binlog 的 pos 信息，然后部署启动 mysql-gp-sync 服务。

## 同步前 mysql 数据库配置
该同步工具需要基于 mysql binlog 同步机制，所以需要开启 mysql binlog 功能，并且需要将 binlog 格式切换为 row 模式，可以通过下述语句查询 binlog 设置。
```shell
show variables like 'log_bin';
show variables like 'binlog_format';
```
腾讯云 binlog 设置文档，可参考 [开启 MySQL 的 binlog 功能](https://cloud.tencent.com/developer/article/1464748)。

## mysql-gp-sync 服务部署
下载安装包`mysql-gp-sync.zip`，并部署在一台 Linux 服务器上，然后解压安装包。解压后可看到多个文件，其中 mysql-gp-sync.toml 是服务配置文件，配置文件示例如下：
```toml
# 需要进行同步数据的源端 mysql
mysql_addr = "127.0.0.1:3306"
mysql_user = "root"
mysql_pass = "123456"
mysql_charset = "utf8"

# 目的端云数据仓库 PostgreSQL 连接配置
pg_host = "139.155.20.126"
pg_port = 5432
pg_user = "gpadmin"
pg_pass = "123456"
pg_dbname = "qidian_api"

# 存放已经完成同步的位移点的文件目录（binlog 同步 pos 和进程文件）
data_dir = "./var"

# statsd 监控地址，如果部署了 statsd 服务会发起推送
statsd_host = "127.0.0.1"
statsd_port = 8125
statsd_prefix = "dbsync"

# 伪装成 slave 时候，配置的 server-id，针对同一 mysql 集群配置的不同的同步进程 id 需要不一致
server_id = 1001
flavor = "mysql"

# 并发配置
# 并发线程数
concurrent_size = 6

#并发缓冲区大小，尽量设置为并发线程数的整数倍
concurrent_ack_win = 2048

# MySQL 数据源配置，支持多个 db 和表
[[source]]
schema = "advanced"
tables = ["t_user"]

# MySQL 数据到 PG 后的分发规则，支持多个表
[[rule]]
# mysql 库表的配置
schema = "advanced"
table = "t_user"
# pg 库表的配置
pg_schema = "public"
pg_table = "t_user"
```

配置参数说明：

| 字段          | 说明                |
| ------------- | ------------------- |
| mysql_addr    | mysql 服务器网络地址 |
| mysql_user    | mysql 用户名          |
| mysql_pass    | mysql 密码             |
| mysql_charset | mysql 编码           |

| 字段      | 说明                             |
| --------- | -------------------------------- |
| pg_host   |  master 节点服务地址     |
| pg_port   |  master 节点服务端口     |
| pg_user   |  master 数据库连接用户名 |
| pg_pass   |  master 数据库连接密码   |
| pg_dbname |  postgresql 数据库密码  |

| 字段          | 说明                                        |
| ------------- | ------------------------------------------- |
| data_dir      | 存放一些记录文件，例如进程号和 bin_log 同步 pos |
| statsd_host   | statsd 监控地址（如果部署）                    |
| statsd_port   | statsd 监控端口（如果部署）                   |
| statsd_prefix | statsd 指标前缀                                   |

| 字段               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| server_id          | 作为 mysql 的 slaverid，针对同一 mysql 源不同的进程需要配置不同的集群 |
| flavor             | 可填 mysql 或者 mariadb                                         |
| skip_no_pk_table   | 是否忽略没有主键的表                                         |
| concurrent_size    | 并发线程数                                                   |
| concurrent_ack_win | 并发缓冲区大小，需要设置为并发线程数的整数倍                 |

| 表数组                          | 字段      | 说明                   |
| ------------------------------- | --------- | ---------------------- |
| source(表示需要监听的mysql库表) | schema    | mysql 数据库配置        |
| source                          | tables    | 数组，需要同步的表列表 |
| rule(表示映射规则)              | schema    | 需要映射的 mysql 数据库  |
| rule                            | table     | 需要映射的 mysql 表      |
| rule                            | pg_schema | 映射到的 schema         |
| rule                            | pg_table  | 映射到的表             |

## 设置当前 bin_log 偏移量
`./var`目录中存在一个 master.info 文件，配置如下：
```
bin_name = "mysql-bin.000005"
bin_pos = 708735
```
表示从 bin_name 这个文件的708735位置开始进行同步。
>!如果不配置该文件，会从头开始进行同步，每次同步后服务会更新该文件信息。

## 启动和停止 mysql-gp-sync
启动服务进程，在命令行文件夹中执行：
```
./start.sh
```
终止服务进程，在命令行文件夹中执行：
```
./stop.sh
```

## 服务定时监控重启
服务进程可能由于一些故障原因而重启，为了能够降低人工处理的复杂度，可通过配置 crontab 来进行自动进程监控重启，配置示例如下：
```
crontab -e
增加下面这行，表示1分钟检查一次，注意这里需要填写部署的路径
*/1 * * * * /Users/Downloads/mysql-gp-sync/monitor_process.sh
```

## 日志查错
在部署路径中有一个 sync.log 文件会实时打印程序执行的步骤，当进程出错退出时，可用于定位问题，日志中 ERROR 等级日志用于错误定位，如果定位有困难可通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 咨询。
