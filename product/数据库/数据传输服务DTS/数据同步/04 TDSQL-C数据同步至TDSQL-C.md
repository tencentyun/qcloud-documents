本文介绍使用数据传输服务 DTS 从 TDSQL-C MySQL 数据库同步数据至腾讯云 TDSQL-C MySQL 数据库的操作指导。

MySQL 到 TDSQL-C MySQL 的数据同步、TDSQL-C MySQL 到 MySQL 的数据同步，与  TDSQL-C MySQL 到 TDSQL-C MySQL 的数据同步要求一致，可参考本场景相关内容。

## 注意事项 
- DTS 在执行全量数据同步时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 为了避免数据重复，请确保需要同步的表具有主键或者非空唯一键。

## 前提条件
- 已 [创建云原生数据库 TDSQL-C](https://cloud.tencent.com/document/product/1003/30505)。
- 需要具备源数据库的权限如下：
```
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW VIEW,PROCESS,SELECT ON *.* TO '迁移帐号'@'%' IDENTIFIED BY '迁移密码';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%'; //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
FLUSH PRIVILEGES;
```
- 需要具备目标数据库的权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。
- 源数据库和目标数据库符合同步功能和版本要求，请参考 [数据同步支持的数据库](https://cloud.tencent.com/document/product/571/58672) 进行核对。

## 应用限制
- 只支持同步基础表和视图，不支持同步函数、触发器、存储过程等对象。
- 在导出视图结构时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和同步用户的 user2 是否一致，如果不一致，则会修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为同步用户的 user2（[DEFINER = user2]）。
- 源端如果是非 GTID 实例，DTS 不支持源端 HA 切换，一旦源端 TDSQL-C 发生切换可能会导致 DTS 增量同步中断。
- 只支持同步 InnoDB、MySIAM、TokuDB 三种数据库引擎，如果存在这三种以外的数据引擎表则默认跳过不进行同步。

## 操作限制
同步过程中请勿进行如下操作，否则会导致同步任务失败。
- 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
- 请勿在源库上执行分布式事务。
- 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
- 请勿在源库上执行清除 Binlog 的操作。
- 在同步增量阶段，请勿删除系统库表 `__tencentdb__`。 

## 支持的 SQL 操作
| 操作类型 | 支持同步的 SQL 操作                                          |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE                                       |
| DDL      | CREATE DATABASE、DROP DATABASE、ALTER DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE、CREATE VIEW、DROP VIEW、CREATE INDEX、DROP INDEX |

## 环境要求
<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<ul><li>源库和目标库网络能够连通。</li>
<li>实例参数要求：
<ul>
<li>源库 server_id 参数需要手动设置，且值不能设置为0。</li>
<li>源库表的 row_format 不能设置为 FIXDE。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置一致。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 binlog_row_image 变量必须设置为 FULL。</li>
<li>TDSQL-C MySQL 5.6 及以上版本 gtid_mode 变量不为 ON 时会报警告，建议打开 gtid_mode。</li>
<li>不允许设置 do_db，ignore_db。</li>
<li>源实例为从库时，log_slave_updates 变量必须设置为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 NO ACTION，RESTRICT 两种类型。</li>
<li>部分库表同步时，有外键依赖的表必须齐全。</li>
</ul></li></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库需要有足够的存储空间，如果初始类型选择“全量数据初始化”，则目标库的空间大小须是源库待同步库表空间的1.2倍以上。</li>
<li>目标库不能有和源库同名的表、视图等同步对象。</li>
<li>目标库 max_allowed_packet 参数设置数值至少为4M。</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadata必须设置为 OFF。</td></tr>
</table>

## 操作步骤
1. 登录 [数据同步购买页](https://buy.cloud.tencent.com/dts)，选择相应配置，单击**立即购买**。
<table>
<thead><tr><th>参数</th><th>描述</th></tr></thead>
<tbody><tr>
<td>计费模式</td><td>支持包年包月和按量计费。目前免费，将来开始计费前1个月会通过邮件和站内信方式提前通知用户。</td></tr>
<tr>
<td>源实例类型</td><td>选择 TDSQL-C MySQL。</td></tr>
<tr>
<td>源实例地域</td><td>选择源实例所在地域。</td></tr>
<tr>
<td>目的实例类型</td><td>选择 TDSQL-C MySQL。</td></tr>
<tr>
<td>目的实例地域</td><td>选择目的实例所在地域。</td></tr>
<tr>
<td>同步任务规格</td><td>目前只支持标准版。</td></tr>
</tbody></table>
2. 购买完成后，返回 [数据同步列表](https://console.cloud.tencent.com/dts/replication)，可看到刚创建的数据同步任务，刚创建的同步任务需要进行配置后才可以使用。
3. 在数据同步列表，单击**操作**列的**配置**，进入配置同步任务页面。
![](https://main.qcloudimg.com/raw/2c5f68ff0bfc4b75998cfe3f92210ed6.png)
4. 在配置同步任务页面，配置源端实例、帐号密码，配置目标端实例、帐号和密码，测试连通性后，单击**下一步**。
<table>
<thead><tr><th width="10%">设置项</th><th width="15%">参数</th><th width="75%">描述</th></tr></thead>
<tbody><tr>
<td rowspan=2 >任务设置</td>
<td>任务名称</td>
<td>DTS 会自动生成一个任务名称，用户可以根据实际情况进行设置。</td></tr>
<tr>
<td>运行模式</td><td>支持立即执行和定时执行两种模式。</td></tr>
<tr>
<td rowspan=6 >源实例设置</td>
<td>源实例类型</td>
<td>购买时所选择的云数据库实例类型，不可修改。</td></tr>
<tr>
<td>源实例地域</td>
<td>购买时选择的云数据库实例所在地域，不可修改。</td></tr>
<tr>
<td>接入类型</td>
<td>根据实际情况选择，本场景选择“云数据库”。
<ul>
<li>公网：源数据库可以通过公网 IP 访问。</li>
<li>云主机自建：源数据库部署在 <a href="https://cloud.tencent.com/document/product/213">腾讯云服务器 CVM</a> 上。</li>
<li>专线接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/216">专线接入</a> 方式与腾讯云私有网络打通。</li>
<li>VPN接入：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/554">VPN 连接</a> 方式与腾讯云私有网络打通。</li>
<li>云数据库：源数据库属于腾讯云数据库实例。</li>
<li>云联网：源数据库可以通过 <a href="https://cloud.tencent.com/document/product/877">云联网</a> 与腾讯云私有网络打通。</li><li>私有网络 VPC：源数据和目标数据库都部署在腾讯云上，且有 <a href="https://cloud.tencent.com/document/product/215">私有网络</a>。</li></ul>对于第三方云厂商数据库，一般可以选择公网方式，也可以选择 VPN 接入，专线或者云联网的方式，需要根据实际的网络情况选择。不同接入类型的准备工作请参考 <a href="https://cloud.tencent.com/document/product/571/59968">准备工作概述</a>。</td></tr>
<tr>
<td>实例 ID</td><td>源数据库实例 ID。</td></tr>
<tr>
<td>帐号</td><td>源数据库帐号。</td></tr>    
<tr>
<td>密码</td><td>源数据库密码。</td></tr>       
<tr>
<td rowspan=6 >目标实例设置</td>
<td>目标实例类型</td><td>所选择的目标实例类型，不可修改。</td></tr>
<tr>
<td>目标实例地域</td><td>选择的目标实例所在地域，不可修改。</td></tr>
<tr>
<td>接入类型</td><td>选择目标数据库类型。</td></tr>
<tr>
<td>实例 ID</td><td>目标数据库实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标数据库帐号。</td></tr>    
<tr>
<td>密码</td><td>目标数据库密码。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/b40bd5a54eaeef3d23bb3464312b0097.png" style="zoom:50%;" />
5. 在设置同步选项和同步对象页面，将对数据初始化选项、数据同步选项、同步对象选项进行设置，在设置完成后单击**保存并下一步**。
>? 
>- 当**初始化类型**仅选择**全量数据初始化**，系统默认用户在目标库已经创建了表结构，不会进行表结构迁移，也不会校验源库和目标库是否有同名表，所以当用户同时在**已存在同名表**项选择**前置校验并报错**，则校验并报错功能不生效。
>- 仅选择**全量数据初始化**的场景，用户需要提前在目标库创建好表结构。
>- 如果用户在同步过程中确定会使用 gh-ost、pt-osc 等工具对某张表做 Online DDL，则**同步对象**需要选择这个表所在的整个库，不能仅选择这个表（或者整个实例），否则无法同步 Online DDL 变更产生的临时表数据到目标数据库。
>- 如果用户在同步过程中确定会对某张表使用 rename 操作（例如将 table A rename 为 table B），则**同步对象**需要选择 table A 所在的整个库（或者整个实例），不能仅选择 table A，否则系统会报错。
>
<table>
<thead><tr><th>设置项</th><th>参数</th><th>描述</th></tr></thead>
<tbody>
<tr>
<td rowspan=2>数据初始化选项</td>
<td>初始化类型</td>
<td><ul><li>结构初始化：同步任务执行时会先将源实例中表结构初始化到目标实例中。<li>全量数据初始化：同步任务执行时会先将源实例中数据初始化到目标实例中。默认两者都勾上，可根据实际情况取消。</td></tr>
<tr>
<td>已存在同名表</td>
<td><ul><li>前置校验并报错：存在同名表则报错，流程不再继续。<li>忽略并继续执行：全量数据和增量数据直接追加目标实例的表中。</td></tr>
<tr>
<td rowspan=2>数据同步选项</td>
<td>冲突处理机制</td>
<td><ul><li>冲突报错：在同步时发现表主键冲突，报错并暂停数据同步任务。<li>冲突忽略：在同步时发现表主键冲突，保留目标库主键记录。<li>冲突覆盖：在同步时发现表主键冲突，用源库主键记录覆盖目标库主键记录。</td></tr>
<tr>
<td>同步操作类型</td><td>支持操作：Insert、Update、Delete、DDL。</td></tr>
<tr>
<td rowspan=2>同步对象选项</td>
<td>源实例库表对象</td><td>选择待同步的对象，支持库级别和表及视图级别。</td></tr>
<tr>
<td>已选对象</td><td>展示已选择的同步对象，支持库表映射。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/272026696de9d8dd15b0034f7bf8f0dd.png"  style="zoom:50%;">
<strong>库表映射</strong>：在已选对象中，鼠标放在右侧将出现编辑按钮，单击后可在弹窗中填写映射名。
<img src="https://main.qcloudimg.com/raw/533a454e1edc2dded72ac92b65948f31.png"  style="zoom:50%;">
6. 在校验任务页面，完成校验并全部校验项通过后，单击**启动任务**。
如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
![](https://main.qcloudimg.com/raw/1871bfc0cb585ff2ac190bb706baf36e.png)
7. 返回数据同步任务列表，任务开始进入**运行中**状态。 
>?选择**操作**列的**更多** > **结束**可关闭同步任务，请您确保数据同步完成后再关闭任务。
>
![](https://main.qcloudimg.com/raw/41165637339063c13bb8cc720e8e6541.png)
8. （可选）您可以单击任务名，进入任务详情页，查看任务初始化状态和监控数据。

