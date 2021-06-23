本文为您介绍使用数据传输服务 DTS 从 MySQL 数据库同步数据至 MySQL 数据库的过程。

## [前提条件](id:qttj)
- 支持的数据库及版本请参见 [数据同步介绍](https://cloud.tencent.com/document/product/571/56513)。
- 需要您在源端 MySQL 中创建迁移帐号，需要的帐号权限如下：
```sql
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SELECT ON *.* TO '迁移帐号'@'%' IDENTIFIED BY '迁移密码';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%';
FLUSH PRIVILEGES;
```

## 同步检查项
启动数据迁移任务前，需要进行前置检查，主要检查内容和检查点如下：

| 检查内容                               | 检查点                                                       |
| -------------------------------------- | ------------------------------------------------------------ |
| 连接数据库检查 | 源库和目标库网络能够连通     |
| 周边检查     | 检查环境变量 innodb_stats_on_metadata=off |
| 版本检查             | 源库和目标库 MySQL 版本必须为 5.5、5.6、5.7、8.0，且源库版本必须小于或等于目标库版本                     |
| 部分实例参数检查                     | - table_row_format 不能为 Fixed <br> - 源库和目标库 lower_case_table_names 变量必须一致 <br> - 检查目标端 max_allowed_packet 参数，至少为4M <br> - 源库变量 connect_timeout 必须大于10  |
| 源端权限检查   | 同 [前提条件](#qttj) 的帐号权限   |
| 目标端权限检查             | 目标云数据库 MySQL 的帐号需要具有如下权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE                        |
| 目标实例内容冲突检测             | - 如果“同名表处理策略”选择了“前置检查并报错”，则目标库不能有和源库冲突的库表，否则会报错<br>- 如果选择了“忽略并继续”，则无要求，同步表结构时遇到同名表会跳过               |
| 目标实例空间检查                         | - 如果选择了“数据初始化”，则目标库的空间大小须是源库待初始化库表空间的1.2倍以上<br>- 如果目标实例非腾讯云 MySQL，无法获取剩余空间，则不会检查，请用户自行保证剩余空间充足 |
| Binlog 参数检查                       | - 源端 binlog_format 变量必须为 ROW<br>- 源端 log_bin 变量必须为 ON<br>- “冲突处理策略”选择“冲突覆盖”时，源端 binlog_row_image 变量必须为 FULL<br>- 源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode<br>- 不允许设置 do_db、ignore_db<br>- 对于源实例为从库的情况，log_slave_updates 变量必须为 ON                     |
| 外键依赖检查                   | - 外键依赖只能是 no action 和 restrict 两种类型<br>- 部分库表同步时，有外键依赖的表必须齐全 |
| 视图检查                           | 只允许和同步目标 user@host 相同的 definer                                   |
| 无主键表检查（阿里云）           | MySQL 5.6 待同步表不能存在无主键表，MySQL 5.7 等其他版本不限制                                   |
| 无主键表检查（AWS）                       | 待同步表不能存在无主键表                                   |
| 其他警告项检查  | - 检查源库和目标库的 max_allowed_packet，如果源库大于目标库，会有警告<br>- 目标库的 max_allowed_packet 小于1GB，会有警告<br>- 如果源库和目标库的字符集不一致，会有警告<br>- 固定警告：提醒用户如果待同步表没有主键或者非空唯一键，有数据重复的风险 |

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 为了避免数据重复，请确保需要同步的表具有主键或者非空唯一键。

## 支持同步的 SQL 操作
| 操作类型 | SQL 操作语句                                                  |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE                                       |
| DDL      | CREATE DATABASE、DROP DATABASE、ALTER DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE、CREATE VIEW、ALTER VIEW、DROP VIEW、CREATE INDEX、DROP INDEX |

## 操作步骤
1. 登录 [数据同步购买页](https://buy.cloud.tencent.com/dts)，选择相应配置，单击【立即购买】。
<table>
<thead><tr><th>参数</th><th>描述</th></tr></thead>
<tbody><tr>
<td>计费模式</td><td>支持包年包月和按量计费。目前免费，将来开始计费前1个月会通过邮件和站内信方式提前通知用户</td></tr>
<tr>
<td>源实例类型</td><td>选择 MySQL（包括云数据库 MySQL 及自建 MySQL）</td></tr>
<tr>
<td>源实例地域</td><td>选择源实例所在地域</td></tr>
<tr>
<td>目的实例类型</td><td>选择 MySQL（包括云数据库 MySQL 及自建 MySQL）</td></tr>
<tr>
<td>目的实例地域</td><td>选择目的实例所在地域</td></tr>
<tr>
<td>同步任务规格</td><td>目前只支持标准版</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/94b1751564b042ad7c9c6dc3c3bf2e29.png"  style="margin:0;">
2. 购买完成后，返回 [数据同步列表](https://console.cloud.tencent.com/dts/replication)，可看到刚创建的数据同步任务，刚创建的同步任务需要进行配置后才可以使用。
3. 在数据同步列表，单击“操作”列的【配置】，进入配置同步任务页面。
![](https://main.qcloudimg.com/raw/b21f1336854375bb1343c7ccb144900b.png)
4. 在配置同步任务页面，配置源端实例、帐号密码，配置目标端实例、帐号和密码，测试连通性后，单击【下一步】。
>?
>- 对 AWS 支持的数据库版本有：RDS MySQL 5.6、5.7、8.0；Aurora MySQL 5.6、 5.7。
>- 对阿里云支持的数据库版本有：RDS 5.6、5.7、8.0；PolarDB 5.6、5.7、8.0。
<table>
<thead><tr><th>设置项</th><th>参数</th><th>描述</th></tr></thead>
<tbody><tr>
<td rowspan=2 >任务设置</td>
<td>任务名称</td>
<td>DTS 会自动生成一个任务名称，用户可以根据实际情况进行设置</td></tr>
<tr>
<td>运行模式</td><td>支持立即执行和定时执行两种模式</td></tr>
<tr>
<td rowspan=4 >源实例设置</td>
<td>源实例类型</td>
<td>购买时所选择的云数据库实例类型，不可修改</td></tr>
<tr>
<td>源实例地域</td>
<td>购买时选择的云数据库实例所在地域，不可修改</td></tr>
<tr>
<td>服务提供商</td>
<td>支持普通（包括腾讯云 MySQL 数据库及自建 MySQL 数据库）、AWS、阿里云</td></tr>
<tr>
<td>接入类型</td>
<td>根据服务提供商选择会有所不同，如服务提供商选择普通，接入类型可选云数据库、云主机自建、公网、云联网；若服务提供商选择其他云厂商，接入类型可选公网</td></tr>
<tr>
<td rowspan=3 >目标实例设置</td>
<td>目标实例类型</td><td>所选择的目标实例类型，不可修改</td></tr>
<tr>
<td>目标实例地域</td><td>选择的目标实例所在地域，不可修改</td></tr>
<tr>
<td>接入类型</td><td>选择目标数据库类型</td></tr>
</tbody></table>
<strong>接入类型说明</strong><br>在源实例及目标实例设置中，根据接入类型选择的不同，会要求填写不同的参数，对应情况见下表：
<table>
<thead><tr><th>服务提供商</th><th>接入类型</th><th>实例 ID</th><th>云主机实例</th><th>主机地址</th><th>端口</th><th>账号</th><th>密码</th></tr></thead>
<tbody><tr>
<td rowspan=4>普通</td><td>云数据库</td>
<td>&#10003;</td><td>×</td><td>×</td><td>×</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr>
<td>云主机自建</td><td>×</td><td>&#10003;</td><td>×</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr>
<td>公网</td><td>×</td><td>×</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr>
<td>云联网</td><td>×</td><td>×</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr>
<td>AWS</td>
<td>公网</td><td>×</td><td>×</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
<tr>
<td>阿里云</td>
<td>公网</td><td>×</td><td>×</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/d5ed42367196f718c62a90c3a3a37088.png"  style="margin:0;">
5. 在设置同步选项和同步对象页面，将对数据初始化选项、数据同步选项、同步对象选项进行设置，在设置完成后单击【保存并下一步】。
<table>
<thead><tr><th>设置项</th><th>参数</th><th>描述</th></tr></thead>
<tbody><tr>
<td rowspan=2>数据初始化选项</td>
<td>初始化类型</td>
<td><ul><li>结构初始化：同步任务执行时会先将源实例中表结构初始化到目标实例中<li>全量数据初始化：同步任务执行时会先将源实例中数据初始化到目标实例中<li>默认两者都勾上，可根据实际情况取消</td></tr>
<tr>
<td>已存在同名表</td>
  <td><ul><li>前置校验并报错：存在同名表则报错，流程不再继续<li>忽略并继续执行：全量数据和增量数据直接追加目标实例的表中</td>
  </tr>
<tr>
<td rowspan=2>数据同步选项</td>
<td>冲突处理机制</td>
<td><ul><li>冲突报错：在同步时发现表主键冲突，报错并暂停数据同步<li>冲突忽略：在同步时发现表主键冲突，保留原主键记录，继续后续数据同步<li>冲突覆盖：在同步时发现表主键冲突，用新记录覆盖原主键记录</td></tr>
<tr>
<td>同步操作类型</td><td>支持操作：Insert、Update、Delete、DDL</td></tr>
<tr>
<td rowspan=2>同步对象选项</td>
<td>源实例库表对象</td><td>选择待同步的对象，支持库级别和表及视图级别</td></tr>
<tr>
<td>已选对象</td><td>展示已选择的同步对象，支持库表映射</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/272026696de9d8dd15b0034f7bf8f0dd.png"  style="margin:0;">
<strong>库表映射</strong>：在已选对象中，鼠标放在右侧将出现编辑按钮，单击后可在弹窗中填写映射名。
<img src="https://main.qcloudimg.com/raw/533a454e1edc2dded72ac92b65948f31.png"  style="margin:0;">
6. 在校验任务页面，完成校验并全部校验项通过后，单击【启动任务】。
>?在校验结果中出现告警项不影响启动任务，但推荐单击【查看详情】获取建议进行调整。
>
![](https://main.qcloudimg.com/raw/9ec59e1cbcf8144d2f3bff7e1aeffa5c.png)
7. 返回数据同步任务列表，任务开始进入“运行中”状态。
>?选择“操作”列的【更多】 >【结束】可关闭同步任务，请您确保数据同步完成后再关闭任务。
>
![](https://main.qcloudimg.com/raw/c2106f47038d8719c878498a4049e98a.png)
8. （可选）您可以单击任务名，进入任务详情页，查看任务初始化状态和监控数据。

