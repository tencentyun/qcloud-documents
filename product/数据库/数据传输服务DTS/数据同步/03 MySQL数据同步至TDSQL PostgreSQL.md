
本文为您介绍如何使用 DTS 数据同步功能将云数据库 MySQL 同步数据至腾讯云企业级分布式数据库 TDSQL PostgreSQL版 及 TDSQL-A PostgreSQL版。

## 前提条件
- 已创建 [云数据库 MySQL](https://cloud.tencent.com/document/product/236/46433) 实例，数据同步支持的源数据库版本为：MySQL 5.6、MySQL 5.7。
- 已创建 [TDSQL PostgreSQL版](https://cloud.tencent.com/document/product/1129/39893) 或 [TDSQL-A PostgreSQL版](https://cloud.tencent.com/document/product/1378/54472) 实例。
- 需要在源端 MySQL 实例中创建迁移帐号，需要的帐号权限包括 `RELOAD`、`LOCK TABLES`、`REPLICATION CLIENT`、`REPLICATION SLAVE`、`SELECT`，`SHOW VIEW`、`PROCESS`，获取权限的方式如下：
```
GRANT RELOAD, LOCK TABLES, REPLICATION CLIENT, REPLICATION SLAVE, SELECT, SHOW VIEW, PROCESS 
ON *.* TO '迁移帐号'@'%' 
IDENTIFIED BY '迁移密码';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%'; //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
FLUSH PRIVILEGES;
```
- 需要在目标端 TDSQL PostgreSQL版 或 TDSQL-A PostgreSQL版 实例中创建迁移帐号，需要的帐号权限包括：`DELETE`、`TRUNCATE`、`INSERT`、`REFERENCES`、`SELECT`、`UPDATE`、`TRIGGER`，获取权限的方式如下：
```
GRANT DELETE, TRUNCATE, INSERT, REFERENCES, SELECT, UPDATE, TRIGGER 
ON ALL TABLES IN SCHEMA schema_name TO user_name（迁移账号）;
```

## 注意事项 
- MySQL 中的 schema 与 database 概念的意义相同，均对应于 TDSQL PostgreSQL版（或 TDSQL-A PostgreSQL版）中的 schema，TDSQL PostgreSQL版（或 TDSQL-A PostgreSQL版）的目标 database 在配置同步任务时须要指定。
- 建议启动同步功能之前对目标实例进行备份，避免同步过程失败引起的数据残留。
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 云数据库 MySQL 需要同步的表必须具有主键。
- 全量迁移过程通过有锁迁移来实现，锁表过程中会短暂（秒级）阻塞写入操作。

## 应用限制
- 目前应用仅支持数据同步，在进行同步之前，您需要创建对应的模式、表和视图。
- 当前仅支持源端数据库同步表的 DML 操作, 不支持 DDL 相关操作。

## 操作限制
同步过程中请勿进行如下操作，否则会导致数据同步任务失败。
- 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
- 请勿在源库写入 Binlog 格式为 Statement 的数据。
- 请勿在源库上执行清除 Binlog 的操作。

## 支持的 SQL 操作
| 操作类型 | 支持同步的 SQL 操作               |
| -------- | ------------------------------- |
| DML      | INSERT、UPDATE、DELETE、REPLACE |
| DDL      | 暂不支持 DDL 相关操作             |

## 环境要求
<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<ul>
<li>源库和目标库网络能够连通。</li>
<li>源库所在的服务器须具备足够的出口带宽，否则将影响迁移速率。</li>
<li>源库中需要同步的表必须具有主键。</li>
<li>源库编码是 utf8 或 utf8mb4 编码。</li>
<li>实例参数要求：
<ul>
<li>参数 innodb_stats_on_metadata 须置为 OFF。</li>
<li>参数 lower_case_table_names 须置为0。</li>
<li>参数 connect_timeout 须大于10。</li>
<li>建议将参数 skip-name-resolve 置为 ON，减少连接超时的可能性。</li>
</ul></li>
<li>Binlog 参数要求：
<ul>
<li>参数 log_bin 须置为 ON。</li>
<li>参数 binlog_format 须置为 ROW。</li>
<li>参数 binlog_row_image 须置为 FULL。</li>
<li>MySQL 5.6 及以上版本源库参数 gtid_mode 不为 ON 时会出现 WARNING 提示，建议将参数 gtid_mode 置为 ON。</li>
<li>不允许设置 do_db, ignore_db 过滤条件。</li>
<li>源实例为从库时，参数 log_slave_updates 须置为 ON。</li>
</ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能是 no action 和 restrict 两种类型。</li>
<li>部分库表迁移时，有外键依赖的表必须齐全。</li>
</ul></li>
<li>DTS 对数据类型为 FLOAT 的迁移浮点精度为38位，对数据类型为 DOUBLE 的迁移浮点精度为308位，需要确认是否符合预期。</li>
</ul></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库编码是 utf8 编码。</li>
<li>目标库的空间大小须是源库待同步库表空间的1.2倍以上（全量数据同步会并发执行 INSERT 操作，导致目标数据库的表产生碎片，因此全量同步完成后目标数据库的表存储空间很可能会比源实例的表存储空间大）。</li>
<li>目标数据库中的模式（schema）和表（table）须提前创建。</li>
<li>源数据库与目标数据库中的表的字段名称须一一对应，任何一端的表缺少字段都会报错。</li>
<li>源数据库中如果有 zerofill 属性的字段，会通过 WARNING 提示同步完成后目标数据库中对应的字段丢失前置0。</li>
</td></tr>
</table>

## 操作步骤
本文介绍的同步功能相关事项既适应于 TDSQL PostgreSQL版，也适应于 TDSQL-A PostgreSQL版，现以 TDSQL-A PostgreSQL版 为例对操作步骤进行说明。

1. 登录 [数据同步购买页](https://buy.cloud.tencent.com/dts)，选择相应配置，单击**立即购买**。
  - 计费模式：支持“包年包月”和“按量计费”模式，当前阶段免费，后续计费会通过邮件和站内信方式提前1个月通知用户。
  - 源实例类型：目前仅支持 MySQL。
  - 源实例地域：选择后不支持再次修改，请选择源实例所在的地域。
  - 目标实例类型：支持 TDSQL PostgreSQL版、TDSQL-A PostgreSQL版。
  - 目标实例地域：选择后不支持再次修改，请选择目标实例所在的地域。
  - 同步任务规格：目前只支持标准版。
2. 确认弹出对话框中的信息，确认无误后，单击**立即购买**，返回数据同步列表，可看到刚创建的数据同步任务，刚创建的同步任务需要进行配置后才可以使用。
![](https://main.qcloudimg.com/raw/a04a3a73d5c7f60db8322d4ab191943c.png)
3. 在 [数据同步列表](https://console.cloud.tencent.com/dts/replication)，单击**操作**列的**配置**，进入配置同步任务页面。
4. 在配置同步任务页面，配置源端实例、帐号及密码，配置目标端实例、帐号及密码，测试连通性后，单击**下一步**。
  - 任务名称：DTS 会自动生成一个任务名称，用户可以根据实际情况进行设置。
  - 运行模式：支持立即执行和定时执行。
  - 源实例类型：选择的云数据库实例类型，不可修改。
  - 源实例地域：选择的云数据库实例所在地域，不可修改。
  - 接入类型：目前支持云数据库。
  - 实例 ID：选择源实例 ID。
  - 源实例数据库帐号和密码：填入实际 [数据库帐号和密码](https://cloud.tencent.com/document/product/236/10305)，并单击**测试连通性**。
  - 目标实例类型：选择的目标实例类型，不可修改。
  - 目标实例地域：选择的目标实例所在地域，不可修改。
  - 接入类型：目前支持**云数据库**。
  - 实例 ID：选择目标实例 ID。
  - 数据库名称：同步到 TDSQL-A PostgreSQL版 所在的数据库名称。
  - 目标实例数据库帐号和密码：填入实际 [数据库帐号和密码](https://console.cloud.tencent.com/tdsqla/instance-tdapg)，并单击**测试连通性**。
![](https://main.qcloudimg.com/raw/d60c52130ae340e039c8ba0ea4a5fa72.png)
5. 在设置同步选项和同步对象页面，选择相应配置，单击**保存并下一步**。
 - 初始化类型：目前只支持**全量数据初始化**。
 - 表内有数据：提供全量同步阶段的冲突处理机制，支持**前置校验并报错**和**继续执行若冲突报错**两种策略。
    - 前置校验并报错：如果目标端同名表内有数据则直接报错。
    - 继续执行若冲突报错：导入数据与目标端同名表中数据冲突时报错。
 - 冲突处理机制：提供增量同步阶段的冲突处理机制，支持**冲突报错**、**冲突忽略**、**冲突覆盖**三种机制。
    - 冲突报错：在同步时发现表主键冲突，报错并暂停数据同步。
    - 冲突忽略：在同步时发现表主键冲突，保留原主键记录，继续后续数据同步。
    - 冲突覆盖：在同步时发现表主键冲突，使用新记录覆盖原主键记录。
 - 同步操作类型：目前只支持 DML 操作。
 - 同步对象：在源库中选择待同步的表对象。
>?
>- 如果用户在同步过程中确定会使用 gh-ost、pt-osc 等工具对某张表做 Online DDL，则**同步对象**需要选择这个表所在的整个库（或者整个实例），不能仅选择这个表，否则无法同步 Online DDL 变更产生的临时表数据到目标数据库。
>- 如果用户在同步过程中确定会对某张表使用 rename 操作（例如将 table A rename 为 table B），则**同步对象**需要选择 table A 所在的整个库（或者整个实例），不能仅选择 table A，否则系统会报错。
>
![](https://main.qcloudimg.com/raw/f2f695b6642285d3310dca726ae92418.png)
6. 在校验任务页面，完成校验并全部校验项通过后，单击**启动任务**。
如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
![](https://main.qcloudimg.com/raw/ab3e60e1bc90a11c9529458281615b6b.png)
7. 返回数据同步任务列表，任务开始进入**运行中**状态。
>?停止任务，则直接关闭任务，请您确保数据同步完成后再关闭任务。
>
![](https://main.qcloudimg.com/raw/4f7e5d83a8100adb48bdaed2b55bb8cc.png)
8. （可选）您可以单击任务名，进入任务详情页，查看任务初始化状态和监控数据。
![](https://main.qcloudimg.com/raw/4e5726065558e7e0181e7a2f24effd5e.png)

