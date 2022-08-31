
## 背景

Canal 是阿里巴巴开源的一款通过解析 MySQL 数据库增量日志，达到增量数据订阅和消费目的 CDC 工具。canal 解析 MySQL 的 binlog 后可投递到 kafka 一类的消息中间件，供下游系统进行分析处理。
如果您正在或考虑使用 canal 同步 MySQL 的增量变更记录到 kafka，腾讯云数据接入平台（DIP）提供了完美兼容此场景的能力。
本文介绍 canal 拉取 MySQL 变更记录并投递到 kafka 的简易使用场景以及 DIP 相应的替换处理方式。

## DIP 订阅 MySQL 功能列表

- 允许选择多库多表。
- 允许指定根据列对消息进行分区同步。
- 允许通过正则匹配选择多表。
- 支持存量数据的同步。
- 同时支持 DDL、DML 类型的变更。
- 兼容 canal、debezium 等消息格式。


## 案例说明
  
前提：已有 MySQL 实例和 kafka 实例
  
### canal 订阅 MySQL 变更记录到 kafka
  
1. 下载 canal server： `canal.deployer-1.1.x.tar.gz` 并解压。
<dx-codeblock>
:::  shell
tar -zxvf canal.deployer-1.1.x.tar.gz
:::
</dx-codeblock>
2. 进入解压目录，配置 conf/example/instance.properties 文件，下面展示必须配置的 mysql 实例信息以及消息中间件的 topic、partition 等信息：
  ```
  canal.instance.master.address=xx.xx.xx.xx:3306
  canal.instance.dbUsername=user
  canal.instance.dbPassword=password
  canal.mq.topic=canal-test-1
  canal.mq.partition=0
  ```
3. 进入解压目录，配置 conf/canal.properties 文件，下面展示必须配置的消息中间件实例信息：
  ```
  canal.serverMode = kafka
  kafka.bootstrap.servers = xx.xx.xx.xx:9092
  kafka.acks = all
  kafka.compression.type = none
  kafka.batch.size = 16384
  kafka.linger.ms = 1
  kafka.max.request.size = 1048576
  kafka.buffer.memory = 33554432
  kafka.max.in.flight.requests.per.connection = 1
  kafka.retries = 0
  ```
4. 启动 canal server：
<dx-codeblock>
:::  shell
sh bin/startup.sh
:::
</dx-codeblock>
启动 canal server 后，canal 开始根据配置获取 MySQL 的增量变更消息并推送到 kafka 集群。

### DIP 订阅 MySQL 变更记录到 kafka

1. 新建连接，选择 MySQL 实例，DIP 同时支持腾讯云 MySQL 实例和云上自建 MySQL 实例：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/70d74980d3b886eaab1601e93061595f.png)
2. 新建数据接入任务，选择 MySQL 数据订阅（Binlog）：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/6134fc3d168293fc9b42209cb94ea2f3.png)
3. 数据源选择**第一步**中配置的连接，DIP 支持多种订阅库表的方式，包括全部库表、批量选择、正则匹配：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/6b83a89f0328049dd09221499ab77b6c.png)
4. DIP 提供了高级配置选项，您可以根据业务需求自行进行选择配置，其中数据格式选择 Canal 格式：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/7b79b6677f0dd201dea1e8af2ce0d269.png)
5. 最后配置 canal 的数据目标，DIP 支持将消息推送到 Ckafka 实例中的 Topic 或单独创建的 DIP Topic：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/5135e72b53da32e62c97ed1ed26c57fc.png)
6. 可在控制台查看 Topic 的落盘消息情况：
  ![image](https://qcloudimg.tencent-cloud.cn/raw/a9e0d0ce5067eba1785ccdfcd3941acb.png)

## 更多功能

### 多种上游数据源的订阅

除了订阅 MySQL 数据源，DIP 同时支持订阅其他多种上游数据源，如 Postgresql、MongoDB、MariaDB、SQL Server 等。

### 可视化实时监控面板

DIP 提供了可视化的实时监控面板，可以一键更改配置信息、一键查看各种性能指标、一键查看 Topic 中落盘的消息内容，能够做到高可靠、免运维。

### 对标 logstash 的数据处理

DIP 提供了对标 logstash 的数据处理能力，仅需通过界面进行编辑即可创建多种数据处理规则。详情参见 [数据处理规则说明](https://cloud.tencent.com/document/product/1591/77082)。

### 多种下游数据源的投递

DIP 支持多种下游数据源的消息推送功能，包括 Elastic Search、ClickHouse 等。如果您正在或考虑使用 canal 将消息同步到 kafka 以外的其他数据源，DIP 同样提供了相应的能力。
