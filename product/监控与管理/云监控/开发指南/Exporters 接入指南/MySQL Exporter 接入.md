## 使用场景

MySQL Exporter 是社区专门为采集 MySQL/MariaDB 数据库监控指标而设计开发。我们可以通过 Exporter 上报我们关心的数据库监控指标，用于异常报警和大盘展示。

支持的版本：

- MySQL >= 5.6
- MariaDB >= 10.1

>! MySQL/MariaDB < 5.6版本，将有部分监控指标无法采集。

## 下载安装

从社区下载开源 [MySQL Exporter](https://github.com/prometheus/mysqld_exporter/releases/) 进行安装，请根据实际的运行环境下载相应的 MySQL Server Exporter。

## 数据库授权

因为 MySQL Exporter 的运行需要再数据库中查询状态数据，所以要在监控的数据库实例中进行如下授权：
```
CREATE USER 'exporter'@'localhost' IDENTIFIED BY 'XXXXXXXX' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'localhost';
```

>?我们建议为该用户设置最大连接数限制，以避免因监控数据抓取对数据库带来影响。但上述并非在所有的数据库版本中都可以生效，例如，MariaDB 10.1 不支持该特性，详情请参见 [官方 resource-limit-options](https://mariadb.com/kb/en/create-user/#resource-limit-options) 说明。

## 运行 MySQL Exporter

MySQL Exporter 的运行有两种方式，可以通过环境变量进行配置，也可以通过指定数据库的配置文件进行篇日志。

- 方式1：使用环境变量运行：
```
export DATA_SOURCE_NAME='user:password@(hostname:3306)/'
./mysqld_exporter <flags>
```
- 方式2：使用 `~/.my.cnf` 配置文件运行：
```
./mysqld_exporter <flags>
```

## Collector 采集参数详解

MySQL Exporter 使用各种 `Collector` 来控制采集数据的启停，具体参数如下：

| 名称                                                     | MySQL 版本 | 描述                                                         |
| -------------------------------------------------------- | ---------- | ------------------------------------------------------------ |
| collect.auto_increment.columns                           | 5.1        | 在 information_schema 中采集 auto_increment 和最大值。       |
| collect.binlog_size                                      | 5.1        | 采集所有注册的 binlog 文件大小。                             |
| collect.engine_innodb_status                             | 5.1        | 从 SHOW ENGINE INNODB STATUS 中采集状态数据。                |
| collect.engine_tokudb_status                             | 5.6        | 从 SHOW ENGINE TOKUDB STATUS 中采集状态数据。                |
| collect.global_status                                    | 5.1        | 从 SHOW GLOBAL STATUS (默认开启) 中采集状态数据。            |
| collect.global_variables                                 | 5.1        | 从 SHOW GLOBAL VARIABLES (默认开启) 中采集状态数据。         |
| collect.info_schema.clientstats                          | 5.5        | 如果设置了 userstat=1，设置成 true 来开启用户端数据采集。    |
| collect.info_schema.innodb_metrics                       | 5.6        | 从 information_schema.innodb_metrics 中采集监控数据。        |
| collect.info_schema.innodb_tablespaces                   | 5.7        | 从 information_schema.innodb_sys_tablespaces 中采集监控数据。 |
| collect.info_schema.innodb_cmp                           | 5.5        | 从 information_schema.innodb_cmp 中采集 InnoDB 压缩表的监控数据。 |
| collect.info_schema.innodb_cmpmem                        | 5.5        | 从 information_schema.innodb_cmpmem 中采集 InnoDB buffer pool compression 的监控数据。 |
| collect.info_schema.processlist                          | 5.1        | 从 information_schema.processlist 中采集线程状态计数的监控数据。 |
| collect.info_schema.processlist.min_time                 | 5.1        | 线程可以被统计所维持的状态的最小时间。 (默认：0)             |
| collect.info_schema.query_response_time                  | 5.5        | 如果 query_response_time_stats 被设置成 ON，采集查询相应时间的分布。 |
| collect.info_schema.replica_host                         | 5.6        | 从 information_schema.replica_host_status 中采集状态数据。   |
| collect.info_schema.tables                               | 5.1        | 从 information_schema.tables 中采集状态数据。                |
| collect.info_schema.tables.databases                     | 5.1        | 设置需要采集表状态的数据库，或者设置成 `*` 来采集所有的数据库。  |
| collect.info_schema.tablestats                           | 5.1        | 如果设置了 userstat=1，设置成 true 来采集表统计数据。        |
| collect.info_schema.schemastats                          | 5.1        | 如果设置了 userstat=1，设置成 true 来采集 schema 统计数据。  |
| collect.info_schema.userstats                            | 5.1        | 如果设置了 userstat=1，设置成 true 来采集用户统计数据。      |
| collect.perf_schema.eventsstatements                     | 5.6        | 从 performance_schema.events_statements_summary_by_digest 中采集监控数据。 |
| collect.perf_schema.eventsstatements.digest_text_limit   | 5.6        | 设置正常文本语句的最大长度。 (默认：120)                     |
| collect.perf_schema.eventsstatements.limit               | 5.6        | 事件语句的限制数量。 (默认：250)                              |
| collect.perf_schema.eventsstatements.timelimit           | 5.6        | 限制事件语句“last_seen”可以保持多久， 单位为秒。 (默认：86400) |
| collect.perf_schema.eventsstatementssum                  | 5.7        | 从 performance_schema.events_statements_summary_by_digest summed 中采集监控数据。 |
| collect.perf_schema.eventswaits                          | 5.5        | 从 performance_schema.events_waits_summary_global_by_event_name 中采集监控数据。 |
| collect.perf_schema.file_events                          | 5.6        | 从 performance_schema.file_summary_by_event_name 中采集监控数据。 |
| collect.perf_schema.file_instances                       | 5.5        | 从 performance_schema.file_summary_by_instance 中采集监控数据。 |
| collect.perf_schema.indexiowaits                         | 5.6        | 从 performance_schema.table_io_waits_summary_by_index_usage 中采集监控数据。 |
| collect.perf_schema.tableiowaits                         | 5.6        | 从 performance_schema.table_io_waits_summary_by_table 中采集监控数据。 |
| collect.perf_schema.tablelocks                           | 5.6        | 从 performance_schema.table_lock_waits_summary_by_table 中采集监控数据。 |
| collect.perf_schema.replication_group_members            | 5.7        | 从 performance_schema.replication_group_members 中采集监控数据。 |
| collect.perf_schema.replication_group_member_stats       | 5.7        | 从 from performance_schema.replication_group_member_stats 中采集监控数据。 |
| collect.perf_schema.replication_applier_status_by_worker | 5.7        | 从 performance_schema.replication_applier_status_by_worker 中采集监控数据。 |
| collect.slave_status                                     | 5.1        | 从 SHOW SLAVE STATUS (默认开启) 中采集监控数据。             |
| collect.slave_hosts                                      | 5.1        | 从 SHOW SLAVE HOSTS 中采集监控数据。                         |
| collect.heartbeat                                        | 5.1        | 从 [heartbeat](#heartbeat-.E5.BF.83.E8.B7.B3.E6.A3.80.E6.B5.8B) 中采集监控数据。                  |
| collect.heartbeat.database                               | 5.1        | 数据库心跳检测的数据源。(默认：heartbeat)                    |
| collect.heartbeat.table                                  | 5.1        | 表心跳检测的数据源。 (默认：heartbeat)                       |
| collect.heartbeat.utc                                    | 5.1        | 对当前的数据库服务器使用 UTC 时间戳（`pt-heartbeat` is called with `--utc`）。（默认：false） |

## 全局配置参数

| 名称                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| config.my-cnf              | 用来读取数据库认证信息的配置文件 `.my.cnf` 位置。 (默认：`~/.my.cnf`) |
| log.level                  | 日志级别。 (默认：info)                                      |
| exporter.lock_wait_timeout | 为链接设置 lock_wait_timeout (单位：秒) 以避免对元数据的锁时间太长。(默认：2) |
| exporter.log_slow_filter   | 添加 log_slow_filter 以避免抓取的慢查询被记录（不支持 Oracle MySQL）。 |
| web.listen-address         | web 端口监听地址。                                           |
| web.telemetry-path         | metrics 接口路径。                                           |
| version                    | 打印版本信息。                                               |

## heartbeat 心跳检测

如果开启了 `collect.heartbeat`， mysqld_exporter 将通过心跳检测机制抓取复制延迟数据。

## 配置 Prometheus 的抓取 Job

当 MySQL Exporter 正常运行后，即可正常的将 Job 添加到 Prometheus 的抓取任务当中。示例如下：

```plaintext
...
  - job_name: 'mysqld_exporter'
    static_configs:
    - targets: ['your_exporter:port']                    
```

通常情况下 exporter 和数据库并不是运行同一台设备，所以数据上报的 `instance` 并不能真实描述是哪个实例，为了方便数据的检索和观察，我们可以将 `instance` 这个标签进行修改，用我们的数据库实例名 `cdb-xxx` 来替换将更加直观，示例如下：

```plaintext
...
  - job_name: 'mysqld_exporter'
    static_configs:
    - targets: ['your_exporter:port']
    relabel_configs:
     - source_labels: [__address__]
       regex: '.*'
       target_label: instance
       replacement: 'cdb-xxx'
```

## 启用数据库监控大盘并配置报警

### 开启 Grafana 监控大盘

腾讯云 Prometheus 托管服务帮我们在 grafana 中预先配置了 MySQL Exporter 的 dashboard，我们只需开启就可以直接查看数据。

![MySQL Exporter dashboard](https://main.qcloudimg.com/raw/61fc92e60a0bc5af7f9d7382510db190.jpg)

### 配置数据库报警

同样，腾讯云 Prometheus 托管服务为我们预先内置了一些 MySQL 数据库的报警策略，但是需要注意的是这些报警策略并不一定能满足我们的监控需要，我们需要根据自己的业务情况进行相应调整。

![MySQL Exporter alert](https://main.qcloudimg.com/raw/abb8680e123473f78c350201acac1abd.jpg)
