本文为您介绍使用数据传输服务 DTS 从 MySQL 数据库同步数据至 MySQL 数据库的过程。

## 前提条件
- 所支持的数据库及版本请参见 [数据同步介绍](https://cloud.tencent.com/document/product/571/56513)。
- 需要您在源端 MySQL 中创建迁移帐号，需要的帐号权限如下：
```sql
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SELECT ON *.* TO "迁移帐号"@"%" IDENTIFIED BY "迁移密码";
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO "迁移帐号"@"%";
FLUSH PRIVILEGES;
```

## 前置检查
在数据同步任务启动前，需要进行前置检查，主要检查内容和检查点如下：

| 检查内容                               | 检查点                                                       |
| -------------------------------------- | ------------------------------------------------------------ |
| 校验目标数据库 schema 和 table是否存在 | schema 和 table 必须提前创建好，如果没有创建好，则会报错     |
| 校验当前用户是否拥有目标数据表权限     | 针对要同步的表，首先判断当前用户是否是该表的 owner（owner 拥有所有权限），如果不是，则查看 information\_schema.table\_privilege 表中的授权信息，必须保证拥有：Delete、Truncate、Insert、References、Select、Update、TRIGGER 的授权权限，否则会报错 |
| 校验目标端磁盘空间是否充足             | 目标库的可用空间和源端需要的空间进行对比                     |
| 校验源端数据库权限                     | 对源实例检查是否有权限：Reload、LockTable、ReplClient、ReplSlave、Select、REPLICATION CLIENT |
| 校验源端 MySQL connect\_timeout 参数   | 校验 MySQL 侧的 connect\_timeout 参数是否小于10，如果小于则会报错 |
| 校验源端和目标端数据库连接             | 校验源MySQL 和目标MySQL是否能正确连接                        |
| 校验源端和目标端数据库版本             | 检查是否满足版本要求(参见前提条件第一点信息)                 |
| 目标端权限检查                         | 目标云数据库 MySQL 的帐号需要具有如下权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE |
| 校验源端优化参数                       | innodb\_stats\_on\_metadata 指标需要关闭                     |
| 校验源端 binlog 参数                   | binlog\_format 须为 ROW；binlog\_row\_image 须为 FULL；log\_bin 须为 ON；gtid\_mode 须为ON |
| 校验主键约束                           | 源端需要同步的表必须有主键                                   |
| 校验源数据库编码                       | 源端必须是 utf8 或 utf8mb4                                   |
| 校验 MySQL 表名大小写配置是否配置正确  | 校验 lower\_case\_table\_names 参数是否为0，如果为0则配置不正确 |

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 为了避免数据重复，请确保需要同步的表具有主键或者非空唯一键

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
<td>源实例类型</td><td>选择 MySQL（包括云数据库 MySQL 及自建 MySQL）或 TDSQL-C MySQL</td></tr>
<tr>
<td>源实例地域</td><td>选择源实例所在地域</td></tr>
<tr>
<td>目的实例类型</td><td>选择 MySQL（包括云数据库 MySQL 及自建 MySQL）或 TDSQL-C MySQL</td></tr>
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
<td>已存在同名表</td><td>前置校验并报错：存在同名表则报错，流程不再继续忽略并继续执行：全量数据和增量数据直接追加目标实例的表中</td></tr>
<tr>
<td rowspan=2>数据同步选项</td>
<td>冲突处理机制</td>
<td><ul><li>冲突报错：在同步时发现表主键冲突，报错并结束数据同步<li>冲突忽略：在同步时发现表主键冲突，保留原主键记录，继续后续数据同步<li>冲突覆盖：在同步时发现表主键冲突，用新记录覆盖原主键记录</td></tr>
<tr>
<td>同步操作类型</td><td>支持操作：Insert、Update、Delete、DDL</td></tr>
<tr>
<td rowspan=2>同步对象选项</td>
<td>源实例库表对象</td><td>选择待同步的对象，支持库级别和表级别</td></tr>
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

