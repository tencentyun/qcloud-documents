
本文主要介绍通过 DTS 数据迁移功能从公网自建 MySQL 迁移数据至腾讯云 TDSQL MySQL版 实例。TDSQL MySQL版 是腾讯自研的分布式数据库，具备强一致高可用、全球部署架构、分布式水平扩展、高性能、企业级安全等特性，是云上分布式数据库的最佳选择。

## [前提条件](id:qttj)
- 已 [创建 TDSQL MySQL版](https://cloud.tencent.com/document/product/557/10236)，支持版本：MySQL 5.6、MySQL 5.7。
- 需要您在目标端 TDSQL MySQL版 中创建迁移帐号，需要帐号权限：待迁移对象的全部读写权限。
- 待迁移源端自建 MySQL，支持版本：MySQL 5.6、MySQL 5.7。
- 需要您在源端MySQL中提前创建好数据库：`__tencentdb__`。
- 需要您在源端 MySQL 中创建迁移帐号。
  - 全实例迁移，需要的帐号权限如下：
```
GRANT SELECT ON *.* TO ‘迁移帐号’;
CREATE USER ‘迁移帐号’@‘%’ IDENTIFIED BY ‘迁移密码’;  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO ‘迁移帐号’@‘%’;  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO ‘迁移帐号’@‘%’;  
```
 - 部分库表迁移，需要的帐号权限如下：
```
GRANT SELECT ON 待迁移的库.* TO ‘迁移帐号’;
CREATE USER ‘迁移帐号’@‘%’ IDENTIFIED BY ‘迁移密码’;  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO ‘迁移帐号’@‘%’;  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO ‘迁移帐号’@‘%’;  
GRANT SELECT ON `mysql`.* TO ‘迁移帐号’@‘%’;
```

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行迁移。
- 源端 MySQL 中待迁移的表支持没有主键或唯一索引，并且不会导致目标数据库中出现重复数据。在全量迁移过程通过有锁迁移来实现，锁表过程中会短暂阻塞写入操作。
- TDSQL MySQL版 的存储空间须是源端自建 MySQL 数据库所占用存储空间的1.2倍以上。
- 源端自建 MySQL 如果是非 GTID 实例，DTS 不支持源端 HA（Highly Available）切换，一旦源端自建 MySQL 发生切换可能会导致 DTS 增量同步中断。
- 关于视图：
	- 全量迁移阶段，源端的视图会忽略，不予迁移。
	- 增量阶段，源端产生的视图 DDL，只会回放在目标实例的第一个分片。

## 支持迁移类型
- 结构迁移：目标端 TDSQL MySQL版 实例暂不支持结构迁移，所以需要您在迁移前在目标端完成对应库和分布式表的创建；如果目标端没有对应的表结构，DTS 会自动创建没有 shard  key 的单表。
- 全量迁移：DTS 支持将源端 MySQL 数据库迁移对象中的全量数据，全部迁移到目标端 TDSQL MySQL版。
- 增量同步：在全量数据迁移的基础上，DTS 会读取并解析源端自建 MySQL 数据库的 binlog 信息，将源端自建 MySQL 中的增量更新同步到目标 TDSQL MySQL版。通过增量数据同步完成自建应用在不停服的情况下平滑迁移到腾讯云。

## 增量同步支持的 SQL 操作
| 操作类型 | 支持同步的 SQL 操作                                            |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE <br>VIEW：CREATE VIEW、ALTER VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX |

## 前置检查
启动数据迁移任务前，需要进行前置检查，主要检查内容和检查点如下：

| 检查内容             | 检查点                                                       |
| -------------------- | ------------------------------------------------------------ |
| 连接数据库检查           | 源库和目标库网络能够连通                                     |
| 周边检查             | 检查环境变量 innodb_stats_on_metadata=off                     |
| 版本检查             | 源库和目标库 MySQL 版本必须为 5.6、5.7，且源库版本必须小于或等于目标库版本 |
| 部分实例参数检查     | - table_row_format 不能为 Fixed<br>- 源库和目标库 lower_case_table_names 变量必须一致<br>- 检查目标端 max_allowed_packet 参数，至少为4M<br>- 源库变量 connect_timeout 必须大于10 |
| 源端权限检查       | 同 [前提条件](#qttj) 的帐号权限                                     |
| 目标端权限检查     | 目标云数据库 MySQL 的帐号需要具有如下权限：ALTER,  ALTER ROUTINE,  CREATE,  CREATE ROUTINE,  CREATE TEMPORARY TABLES,  CREATE USER,  CREATE VIEW,  DELETE,  DROP,  EVENT,  EXECUTE,  INDEX,  INSERT,  LOCK TABLES,  PROCESS,  REFERENCES,  RELOAD,  SELECT,  SHOW DATABASES,  SHOW VIEW,  TRIGGER,  UPDATE |
| 目标实例内容冲突检测 | 目标库不能有和源库冲突的库表                                 |
| 目标实例空间检查     | 目标库的空间大小须是源库待迁移库表空间的1.2倍以上 |
| Binlog 参数检查       | - 源端 binlog_format 变量必须为 ROW<br>- 源端 log_bin 变量必须为 ON<br>- 源端 binlog_row_image 变量必须为 FULL<br>- 源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode<br>- 不允许设置 do_db, ignore_db<br>- 对于源实例为从库的情况，log_slave_updates 变量必须为 ON |
| 外键依赖检查         | - 外键依赖只能是 no action 和 restrict 两种类型<br>- 部分库表迁移时，有外键依赖的表必须齐全 |
| 视图检查             | 只允许和迁移目标 user@host 相同的 definer                       |
| 其他警告项检查       | - 检查源库和目标库的 max_allowed_packet，如果源库大于目标库，会有警告<br>- 目标库的 max_allowed_packet 小于1GB，会有警告<br>- 如果源库和目标库的字符集不一致，会有警告<br>- 对于全量迁移（没有增量），发警告告知用户这种全量迁移没有锁，不保证数据一致 |

## 操作步骤
1. 登录 [DTS 数据迁移控制台](https://console.cloud.tencent.com/dts/migration?rid=8&page=1&pagesize=20)，单击【新建迁移任务】，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击【0元购买】，目前 DTS 数据迁移功能免费使用。
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击【新建】。
>?如果连通性测试失败，请根据提示进行排查并解决后再次重试。
>
<table>
<thead><tr><th>设置类型</th><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td rowspan=3>任务设置</td>
<td>任务名称</td>
<td>设置一个具有业务意义的名称，便于任务识别</td></tr>
<tr>
<td>运行模式</td>
<td>支持立即执行和定时执行：立即执行，则完成任务校验通过后立即启动任务；定时执行，需要配置一个任务执行时间则到时间后启动任务。</td></tr>
<tr>
<td>标签</td>
<td>标签用于从不同维度对资源分类管理。如现有标签不符合您的要求，请前往控制台管理标签。</td></tr>
<tr>
<td rowspan=8>源库设置</td>
<td>源库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>选择“普通”。</td></tr>
<tr>
<td>接入类型</td><td>选择“公网”。</td></tr>
<tr>
<td>所属地域</td><td>源库所属地域为 DTS 服务出口地域，选择离自建实例最近的一个地域即可。</td></tr>
<tr>
<td>主机地址</td><td>源库 MySQL 访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库 MySQL 访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“TDSQL MySQL版”。</td></tr>
<tr>
<td>接入类型</td><td>选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>上一步中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标端 TDSQL MySQL版 实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标端 TDSQL MySQL版 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标端 TDSQL MySQL版 的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击【保存】。
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>- 目标端为 TDSQL MySQL版 实例暂不支持结构迁移。<br>- 如果只进行数据全量迁移，请选择全量迁移。<br>- 如果需要不停机平滑迁移，请选择全量 + 增量迁移。</td></tr>
<tr>
<td>迁移对象</td>
<td>- 如果需要整个实例迁移，请选择整个实例，不包括系统库，如 information_schema、mysql、performance_schema、sys。 <br>- 如果需要指定库表迁移，请选择指定对象。</td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/1101e817e99b5a53cc4a088c55b84810.png"  style="margin:0;">
5. 在校验任务页面，进行校验，校验任务通过后，单击【启动任务】。
 -  校验任务通过后，根据选择的运行模式启动迁移任务。
 -  如果校验任务不通过，可以查看具体检查项和失败原因，待问题解决后重新发起校验任务。
![](https://main.qcloudimg.com/raw/c8a82a647ce9d5bc21f902f35011e120.png)
6. 返回数据迁移任务列表，任务进入创建中状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
 -  撤销任务：在迁移过程中，如您需要撤销迁移任务，可以单击【撤销】。撤销任务不会对目标实例中的数据进行清理；再次启动可能导致校验失败，您可能需要手动清空目标库内可能产生冲突的数据库或数据表，才能再次启动迁移任务。
 -  完成任务：在增量数据同步过程中，如您确认目标端数据和源端数据已经保持一致，也就是目标与源库数据差距为0MB，及目标与源库时间延迟为0秒时，您可以单击【完成】。单击完成后，迁移任务不再进行数据同步，也意味着本次数据迁移已完成。
 -  查看任务：您可以单击任务 ID 进入任务详情页，查看迁移任务详情和迁移对象列表。
![](https://main.qcloudimg.com/raw/f7d0088711ded04f30dfb3d28450f5fb.png)
