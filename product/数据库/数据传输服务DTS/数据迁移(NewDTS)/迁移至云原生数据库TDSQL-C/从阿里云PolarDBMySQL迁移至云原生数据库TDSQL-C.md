
本文主要介绍通过 DTS 数据迁移功能从阿里云 PolarDB MySQL 迁移数据至腾讯云原生数据库TDSQL-C（兼容 MySQL 版）。DTS 支持结构迁移、全量数据迁移以及增量数据迁移，可以实现在不停服的情况下，平滑迁移数据到云原生数据库TDSQL-C（兼容 MySQL 版）。

## [前提条件](id:qttj)
- 已 [创建云原生数据库TDSQL-C（兼容 MySQL 版）](https://cloud.tencent.com/document/product/1003/30505)。
- 需要您在目标端 TDSQL-C 中创建迁移帐号，需要帐号权限：待迁移对象的全部读写权限。
- 待迁移源端阿里云 PolarDB MySQL 能够通过公网访问，需要将阿里云 PolarDB MySQL 的公开可用性设置为是，支持数据库版本：MySQL 5.5、MySQL 5.6、MySQL 5.7。
- 需要您在源端阿里云 PolarDB MySQL 中创建迁移帐号，需要的帐号权限如下：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW
DATABASES,SHOW VIEW,PROCESS ON *.* TO '迁移帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%';  
GRANT SELECT ON `mysql`.* TO '迁移帐号'@'%';
```
- 部分库表迁移：`GRANT SELECT ON 待迁移的库.* TO '迁移帐号';`
- 全实例迁移：`GRANT SELECT ON *.* TO '迁移帐号';`

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行迁移。
- 源端 MySQL 中待迁移的表仅支持有主键的表。全量数据迁移过程通过无锁迁移来实现，全量迁移过程中不会阻塞写操作，对业务影响也更小。建议用户在源端数据表中添加主键再发起数据迁移。
- 全量数据无锁迁移过程如果发生 DDL 操作，有可能导致迁移任务失败，所以在 DTS 全量数据迁移过程请避免 DDL 操作。
- TDSQL-C 的存储空间须是源端阿里云 PolarDB MySQL 数据库所占用存储空间的1.2倍以上。

## 支持迁移类型
- 结构迁移：DTS 支持将迁移对象的结构定义迁移到目标实例中，目前 DTS 支持结构迁移的对象包括数据库、数据表、视图。
- 全量迁移：DTS 支持将源端 MySQL 数据库迁移对象中的全量数据，全部迁移到目标端 TDSQL-C。
- 增量同步：在全量数据迁移的基础上，DTS 会读取并解析源端 PolarDB MySQL 数据库的 binlog 信息，将源端 PolarDB MySQL 中的增量更新同步到目标 TDSQL-C。通过增量数据同步完成自建应用在不停服的情况下平滑迁移到腾讯云。

## 增量同步支持的 SQL 操作
| 操作类型 | 支持同步的 SQL 操作                                            |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE <br>VIEW：CREATE VIEW、ALTER VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX <br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 迁移准备
- 阿里云 PolarDB MySQL 默认 binlog 功能关闭，开启 binlog 需要重启集群内所有节点，会造成连接中断，操作请做好业务安排。
- 阿里云 PolarDB MySQL 中，loose_polar_log_bin 参数为全局（Global）级别参数。
- 登录阿里云 PolarDB MySQL 控制台，在**配置与管理** >**参数配置**中找到目标参数 loose_polar_log_bin：
 -   数据库引擎为 MySQL 5.6 的 PolarDB 集群，当前值修改为ON_WITH_GTID。
 -   数据库引擎为 MySQL 5.7 的 PolarDB 集群，当前值修改为ON。

## 前置检查
启动数据迁移任务前，需要进行前置检查，主要检查内容和检查点如下：

| 检查内容             | 检查点                                                       |
| -------------------- | ------------------------------------------------------------ |
| 连接数据库检查           | 源库和目标库网络能够连通                                     |
| 周边检查             | 检查环境变量 innodb_stats_on_metadata=off                     |
| 版本检查             | 源库和目标库 MySQL 版本必须为5.6、5.7，且源库版本必须小于或等于目标库版本 |
| 部分实例参数检查     | table_row_format 不能为 Fixed<br>源库和目标库 lower_case_table_names 变量必须一致<br>检查目标端 max_allowed_packet 参数，至少为4M<br>源库变量 connect_timeout 必须大于10 |
| 源端权限检查       | 同 [前提条件](#qttj) 的帐号权限                                     |
| 目标端权限检查     | 目标云数据库 MySQL 的帐号需要具有如下权限：ALTER,  ALTER ROUTINE,  CREATE,  CREATE ROUTINE,  CREATE TEMPORARY TABLES,  CREATE USER,  CREATE VIEW,  DELETE,  DROP,  EVENT,  EXECUTE,  INDEX,  INSERT,  LOCK TABLES,  PROCESS,  REFERENCES,  RELOAD,  SELECT,  SHOW DATABASES,  SHOW VIEW,  TRIGGER,  UPDATE |
| 目标实例内容冲突检测 | 目标库不能有和源库冲突的库表                                 |
| 目标实例空间检查     | 目标库的空间大小须是源库待迁移库表空间的1.2倍以上 |
| Binlog 参数检查       | 源端 binlog_format 变量必须为 ROW<br>源端 log_bin 变量必须为 ON<br>源端 binlog_row_image 变量必须为 FULL<br>源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode<br>不允许设置 do_db, ignore_db<br>对于源实例为从库的情况，log_slave_updates 变量必须为 ON |
| 外键依赖检查         | 外键依赖只能是 no action 和 restrict 两种类型<br>部分库表迁移时，有外键依赖的表必须齐全 |
| 视图检查             | 只允许和迁移目标 user@host 相同的 definer                       |
| 其他警告项检查       | 检查源库和目标库的 max_allowed_packet，如果源库大于目标库，会有警告<br>目标库的 max_allowed_packet 小于1GB，会有警告<br>如果源库和目标库的字符集不一致，会有警告<br>对于全量迁移（没有增量），发警告告知用户这种全量迁移没有锁，不保证数据一致 |
| 无主键表检查         | 待迁移表不能存在无主键表                                     |

## 操作步骤
1. 登录 [DTS 数据迁移控制台](https://console.cloud.tencent.com/dts/migration)，单击【新建迁移任务】，进入新建迁移任务页面。
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
<td rowspan=9>源库设置</td>
<td>源库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>选择“阿里云”。</td></tr>
<tr>
<td>数据库版本	</td><td>选择 PolarDB 5.6 或 PolarDB 5.7。</td></tr>
<tr>
<td>接入类型</td><td>选择“公网”。</td></tr>
<tr>
<td>所属地域</td><td>源库所属地域为 DTS 服务出口地域，请选择离阿里云 PolarDB MySQL 最近的一个地域即可。</td></tr>
<tr>
<td>主机地址</td><td>建议使用 PolarDB 的主地址，因为直接指向生成 Binlog 的主节点，具有更好的兼容性和稳定性。您可以在阿里云 PolarDB MySQL 的基本信息页面，获取数据库的访问地址。</td></tr>
<tr>
<td>端口</td><td>阿里云 PolarDB MySQL 访问端口，默认为3306。</td></tr>
<tr>
<td>帐号</td><td>阿里云 PolarDB MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>阿里云 PolarDB MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“TDSQL-C MySQL 版”。</td></tr>
<tr>
<td>接入类型</td><td>选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>上一步中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标端 TDSQL-C ID。</td></tr>
<tr>
<td>帐号</td><td>目标端 TDSQL-C 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标端 TDSQL-C 的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击【保存】。
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>如果只进行结构迁移，请选择结构迁移。<br>如果只进行数据全量迁移，请选择全量迁移。<br>如果需要不停机平滑迁移，请选择全量 + 增量迁移。</td></tr>
<tr>
<td>迁移对象</td>
<td>如果需要整个实例迁移，请选择整个实例，不包括系统库，如 information_schema、mysql、performance_schema、sys。 <br>如果需要指定库表迁移，请选择指定对象。</td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/51d26749a5a208f84c3750e9afc9ea32.png"  style="margin:0;">
5. 在校验任务页面，进行校验，校验任务通过后，单击【启动任务】。
 -  校验任务通过后，根据选择的运行模式启动迁移任务。
 -  如果校验任务不通过，可以查看具体检查项和失败原因，待问题解决后重新发起校验任务。
![](https://main.qcloudimg.com/raw/0a206c0f8f0c26da17ecb3b983c2ee52.png)
6. 返回数据迁移任务列表，任务进入创建中状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
 - 结构迁移 + 全量迁移任务：任务完成后会自动结束，在不需要任务撤销情况下，请勿手动结束否则会导致迁移数据丢失。
 - 全量迁移 + 增量迁移任务：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击【完成】结束增量数据同步。
    - 请选择合适时间手动完成增量数据同步，并完成业务切换。
    - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
    - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。
![](https://main.qcloudimg.com/raw/0d2f7bef47a658148d779afaefe4382b.png)
7. （可选）您也可以单击任务 ID 进入任务详情页，查看迁移任务详情和迁移对象列表。
