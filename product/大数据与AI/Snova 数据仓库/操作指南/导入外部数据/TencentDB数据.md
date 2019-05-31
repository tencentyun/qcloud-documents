## 使用 kettle 导入 TencentDB 的数据
Kettle 是一款开源的 ETL 工具，纯 Java 编写，可以在 Window、Linux、Unix 上运行，数据抽取高效稳定。
[下载地址](http://kettle.pentaho.org/)

## 使用 data-loader 工具导入 TencentDB 的数据
data-loader 是一个简易的命令行工具，支持将 TencentDB 中全量或增量数据导入到 Snova 中。工具采用 Java 开发，用 JDBC 连接源数据库与目标数据库，可在 Windows 与 Linux 下运行，使用前需要安装 Java 运行环境，并设置环境变量 JAVA_HOME。
基本结构：
![](https://main.qcloudimg.com/raw/4a69153ce9c4eb4a1c124f20e880f502.png)
配置文件：
```
# 源数据库JDBC驱动，根据数据库类型指定相应的驱动
source.jdbc-driver:com.mysql.jdbc.Driver
# 源数据库JDBC连接URL，参考以下示例进行配置，主要配置数据库的主机地址，端口，数据库等参数。另外，useCursorFetch=true&defaultFetchSize=5000表示采用流式方式读取数据，为避免工具占用过大内存，通常需要配置
source.jdbc-url:jdbc:mysql://SourceCDB:4199/CDB?useCursorFetch=true&defaultFetchSize=5000
# 源数据库用户名，请确保该用户名有相应表的读权限
source.user:test
# 源数据库密码
source.password:abcd1234
# 源数据库抽取数据的SQL语句，支持动态参数的配置（使用?表示动态参数），参数由在run.sh脚本运行时传入
source.sql:SELECT * FROM FlinkRawMetrics WHERE id>=? AND id<?
# 如果source.sql中使用了动态参数，需要配置参数类型，有以下类型可用
# time - 时间类型，number - 数字类型，string – 字符串类型（默认）
source.sql.args-type:time

# 目标数据库JDBC驱动，导入目标数据库请设置为org.postgresql.Driver
target.jdbc-driver:org.postgresql.Driver
# 目标数据库JDBC连接URL，参考以下示例进行配置，主要配置数据库的主机地址，端口，数据库等参数。reWriteBatchedInserts=true表示启动批量导入，可提供导入效率，通常情况下需要设置
target.jdbc-url:jdbc:postgresql://DevPG:50010/postgres?reWriteBatchedInserts=true
# 目标数据库用户名，请确保该用户名有相应表的写权限
target.user:root
# 目标数据库密码
target.password:abcd1234
# 目标数据库中需要导入数据的表
target.table:FlinkRawMetrics
# 运行导入前是否需要清空目标表，通常在导入全量数据时需要设置为true
target.truncate-before-insert:true
# 运行导入前是否需要删除该阶段的部分数据，动态参数的使用方式与source.sql中的一致，通常在增量导入时设置，以确保重复运行该时间段的增量作业能够得到一致的结果
target.clear-sql-before-insert:DELETE FROM FlinkRawMetrics WHERE id>=? AND id<?
# 与source.sql.args-type用法相同
target.clear-sql-before-insert.args-type:true
# 批量导入的数据条数
target.batch-size:5000
```

### 准备工作
1. 在云数据库 MySQL 上创建原表，使用如下语句：
```
CREATE TABLE `EndpointAccessLog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time_` timestamp NULL DEFAULT NULL,
  `client_ip` varchar(16) DEFAULT NULL,
  `method` varchar(8) DEFAULT NULL,
  `uri` varchar(256) DEFAULT NULL,
  `protocol_version` varchar(16) DEFAULT NULL,
  `status_code` bigint(20) DEFAULT NULL,
  `app_id` bigint(20) DEFAULT NULL,
  `request_body_length` bigint(20) DEFAULT NULL,
  `response_body_length` bigint(20) DEFAULT NULL,
  `cost` bigint(20) DEFAULT NULL,
  `user_agent` varchar(256) DEFAULT NULL,
  `host` varchar(32) DEFAULT NULL,
  `date_` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `time_` (`time_`)
) ENGINE=InnoDB
```
在 time 字段上建立了索引，用于基于时间的增量抽取。
2. 在 Snova 上创建目标表，也需要在 time 字段上建立索引。

### 全量导入
全量导入用于离线一次性将数据源的数据导入到目标数据库中，仅运行一次，由运维人员手动触发。
1. 编写配置文件。
```
source.jdbc-driver:com.mysql.jdbc.Driver
source.jdbc-url:jdbc:mysql://SourceCDB:4199/CDB?useCursorFetch=true&defaultFetchSize=5000
source.user:test
source.password:abcd1234
source.sql:SELECT * FROM EndpointAccessLog   
target.jdbc-driver:org.postgresql.Driver
target.jdbc-url:jdbc:postgresql://TargetGP:13634/postgres?reWriteBatchedInserts=true
target.user:gptestuser
target.password:gptestuser
target.table: EndpointAccessLog
target.truncate-before-insert:true
target.batch-size:5000
```
2. 源表插入数据。
```
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('1','2018-06-08 17:01:09','10.59.226.106','POST','/messages/1253358381/SngapmQQ/cttree/','HTTP/1.0','200','1253358381','144670','5','9','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('2','2018-06-08 17:01:09','10.59.226.106','POST','/messages/1253358381/SngapmQQ/cttree/','HTTP/1.0','200','1253358381','107876','5','21','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('3','2018-06-08 17:01:09','100.98.236.186','GET','/topics/1251001049/sngapmfutu/timelineheader','HTTP/1.0','404','0','0','17','19','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
```
3. 运行作业。
![](https://main.qcloudimg.com/raw/3eba392fc3b2c3326894dbd73691ef35.png)
查看目标数据库中的数据，可以看到数据已经成功导入。
![](https://main.qcloudimg.com/raw/049494e76841f43ec12094e5d74bbf63.png)

### 增量导入
增量导入用于将截至上次作业运行后新增的数据导入目标数据库，相对于全量导入而言，其触发方式可以设定为手动触发，但通常情况下设置为自动触发（如每5分钟、每小时、每天触发一次），并发布到生产环境定期运行。
增量导入实现方式有多种，需要按照数据源的特征和需求设置相应的调度策略，本示例采用保存当前时间戳加上定时导入的方式。这里我们使用小时为单位进行增量导入，在全量导入时我们导入了2018-06-08 17点的数据，这里我们导入 2018-06-08 18点的数据。
1. 编写配置文件。
```
source.jdbc-driver:com.mysql.jdbc.Driver
source.jdbc-url:jdbc:mysql://SourceCDB:4199/CDB?useCursorFetch=true&defaultFetchSize=5000
source.user:test
source.password:abcd1234
source.sql:SELECT * FROM EndpointAccessLog WHERE time_>=? AND time<?
source.sql.args-type:time
target.jdbc-driver:org.postgresql.Driver
target.jdbc-url:jdbc:postgresql://TargetGP:13634/postgres?reWriteBatchedInserts=true
target.user:gptestuser
target.password:gptestuser
target.table: EndpointAccessLog
target.clear-sql-before-insert:DELETE FROM EndpointAccessLog WHERE time_>=? AND time <?
target.clear-sql-before-insert.args-type:time
target.batch-size:5000
```
其中，`WHERE time_>=? AND time<?` 部分为增量参数，需要配置。
2. 源表插入新增数据。
```
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('134240','2018-06-08 18:00:00','10.59.226.106','POST','/messages/1253358381/SngapmQQ/cttree/','HTTP/1.0','200','1253358381','109662','5','25','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('134241','2018-06-08 18:00:00','10.59.226.86','POST','/messages/1253358381/SngapmQQ/dfrate/','HTTP/1.0','200','1253358381','223329','5','21','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
insert into `EndpointAccessLog` (`id`, `time_`, `client_ip`, `method`, `uri`, `protocol_version`, `status_code`, `app_id`, `request_body_length`, `response_body_length`, `cost`, `user_agent`, `host`, `date_`) values('134242','2018-06-08 18:00:00','10.148.218.46','POST','/messages/1253358381/SngapmQQ/timelineio/','HTTP/1.0','200','1253358381','197122','5','28','CDP-SDK-JAVA/1.0','10_207_128_38','2018-06-08');
```
3. 运行增量作业。
 ![](https://main.qcloudimg.com/raw/dd4556cccf8a6685b4a66917cdf27247.png)
完成后，查看目标数据库中的数据，可以看到除了原来的数据外，新增的数据已经成功导入。
![](https://main.qcloudimg.com/raw/28d8cd469b6c485b3d2067997771bede.png)
