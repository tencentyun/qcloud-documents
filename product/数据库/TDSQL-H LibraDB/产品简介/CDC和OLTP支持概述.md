## 简介
CDC（Change Data Capture）是数据融合的高速链路。数据在 OLTP 与分析引擎间稳定、安全、高效地保持准实时同步。这样既能保留 OLTP 功能、优势能力与业务使用习惯，也能充分利用分析引擎极致性能。

基于 CDC 的架构，用户能灵活组合所需的 OLTP 引擎与分析引擎。可以使用已有的 OLTP，也可以新建专用 OLTP。一个分析引擎可以通过 CDC 与多个 OLTP 建立数据同步，并能按需解绑定，满足数据多合一的需求。除此之外，CDC 还提供了数据过滤，数据映射，且能进行自动化地异构数据转换。

通过 CDC 支持了可插拔的 OLTP，充分发挥分析引擎对海量数据的支持能力，满足多种场景需求。

## CDC 功能
- 高性能且稳定的数据同步能力。
- 为用户提供告警等监控措施。
- 支持库表结构、全量数据、增量数据的多种组合数据同步。
- 支持选择部分库表同步。
- 支持多种源实例网络类型。
- 支持库表名映射修改。可以修改特定库表名，或者添加统一后缀。
- 支持自动化表结构转换，表字段类型转换。自动将表引擎转换为 ReplicatedReplacingMergeTree。
- 支持用户自定义时间类分区键。方便用户做数据冷热分离。
- 支持完整 DML 和高频 DDL。
- 增量阶段支持断点续传。
- 支持多合一。

## CDC 及 OLTP 限制
目前 OLTP 支持 MySQL 数据库，对更多数据库的支持将陆续推出。

#### 支持的 MySQL 版本

| MySQL 供应商   | 版本                                              |
| -------------- | ------------------------------------------------- |
| 社区版、企业版 | 5.6、5.7                                          |
| 腾讯云         | 云数据库 MySQL 5.6、云数据库 MySQL 5.7                  |
| AWS            | RDS MySQL 5.7、Aurora MySQL 5.6、Aurora MySQL 5.7 |

#### 功能限制
- 源表必须包含主键或者不可为 NULL 的唯一键。
- 源实例不可只读。
- 若选择增量同步。
  - 要求 MySQL 开启 GTID。
  - 要求开启 binlog，且要求为 ROW 和 FULL 格式。
  - 支持高频 DDL 同步。
- DDL 支持
<table>
<thead>
<tr><th>对象</th><th>DDL</th><th>备注</th></tr></thead>
<tbody><tr>
<td>Database</td>
<td>create、drop</td>
<td>drop 操作转义为重命名操作：将库名修改为“deleted_unix时间戳_原库名”</td></tr>
<tr>
<td rowspan="3">Table</td>
<td rowspan="3">create、rename、drop、truncate、alter</td>
<td>drop 操作转义为重命名操作：将表名修改为“deleted_unix时间戳_原表名” </td></tr>
<tr>
<td>truncate 操作转义为：将表名修改为“deleted_unix时间戳_原表名”并新建本地表</td></tr>
<tr>
<td>rename 操作不支持移动表：`RENAME TABLE current_db.tbl_name TO other_db.tbl_name;`</td></tr>
<tr>
<td>Column</td>
<td>add、drop、rename、change、modify、alter</td>
<td>-</td></tr>
</tbody></table>
>!
>- 当分析引擎是 LibraSQL 10.3.203 及更早期版本时，由于 Database Engine 不支持 [atomic engine](https://clickhouse.com/docs/en/engines/database-engines/atomic/)，下述 DDL 不支持：rename、drop、truncate、alter rename table、drop database。
>- 对于删除类操作，为保障数据安全，我们会转义为改名操作。
>- 库表 DDL 同步说明：
>  - “同步对象”选择“整个实例”，在链路建立后：OLTP 新增的对象及其修改均能同步到分析引擎。
>  - “同步对象”选择“指定对象”，且指定对象为整库时，在链路建立后：OLTP 指定库中新增的表及其修改会同步到分析引擎，但不会同步其他库的变化。
>  
- 命名限制
<table>
<thead><tr><th>对象</th><th>限制</th></tr></thead>
<tbody><tr>
<td>库表名映射修改</td>
<td>只支持字母，数字和下划线，长度不超过1024</td></tr>
<tr>
<td>指定全局分区键列名</td>
<td>只支持字母，数字和下划线，长度不超过1024</td></tr>
<tr>
<td>分析引擎集群名</td>
<td>default_cluster</td></tr>
</tbody></table>

