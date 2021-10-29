## 简介

CDC是数据融合的高速链路。数据在OLTP与分析引擎间稳定、安全、高效地保持准实时同步。这样既能保留OLTP功能、优势能力与业务使用习惯，也能充分利用分析引擎极致性能。

基于CDC的架构，用户能灵活组合所需的OLTP引擎与分析引擎。可以使用已有的OLTP，也可以新建专用OLTP。一个分析引擎可以通过CDC与多个OLTP建立数据同步，并能按需解绑定，满足数据多合一的需求。除此之外，CDC还提供了数据过滤，数据映射，且能进行自动化地异构数据转换。

通过CDC支持了可插拔的OLTP，充分发挥分析引擎对海量数据的支持能力，满足多种场景需求。

### CDC功能

CDC功能列表如下。

- 高性能且稳定的数据同步能力。为用户提供告警等监控措施。
- 支持库表结构，全量数据，增量数据的多种组合数据同步。
- 支持选择部分库表同步。
- 支持多种源实例网络类型。

- 支持库表名映射修改。可以修改特定库表名，或者添加统一后缀。
- 支持自动化表结构转换，表字段类型转换。自动将表引擎转换为ReplicatedReplacingMergeTree。
- 支持用户自定义时间类分区键。方便用户做数据冷热分离。
- 支持完整DML和高频DDL。
- 增量阶段支持断点续传。
- 支持多合一。

### CDC及OLTP限制

目前OLTP支持MySQL数据库，对更多数据库的支持将陆续推出。

**支持的MySQL版本**

| MySQL 供应商   | 版本                                              |
| -------------- | ------------------------------------------------- |
| 社区版、企业版 | 5.6、5.7                                          |
| 腾讯云         | 云数据MySQL 5.6、云数据MySQL 5.7                  |
| AWS            | RDS MySQL 5.7、Aurora MySQL 5.6、Aurora MySQL 5.7 |

**功能限制**

- 源表必须包含主键或者不可为NULL的唯一键。

- 若选择增量同步。

  - 要求MySQL开启GTID。

  - 要求开启binlog，且要求为ROW和FULL格式。

  - 支持高频DDL同步

    > !
    >
    > 对于删除类操作，为保障数据安全，我们会转义为改名操作。
    
    <table>
    <thead>
      <tr>
        <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对象</th>
        <th>DDL</th>
        <th>备注</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Database</td>
        <td>create、drop</td>
        <td>drop操作转义为重命名操作：将库名修改为“deleted_unix时间戳_原库名”。</td>
      </tr>
      <tr>
        <td rowspan="3">Table</td>
        <td rowspan="3">create、rename、drop、truncate、alter</td>
        <td>drop操作转义为重命名操作：将表名修改为“deleted_unix时间戳_原表名”。 </td>
      </tr>
      <tr>
        <td>truncate操作转义为：将表名修改为“deleted_unix时间戳_原表名”并新建本地表。</td>
      </tr>
      <tr>
          <td>rename操作<b>不支持移动表</b>：RENAME TABLE&nbsp;&nbsp;&nbsp;current_db.tbl_name TO other_db.tbl_name;</td>
      </tr>
      <tr>
        <td>Column</td>
        <td>add、drop、rename、change、modify、alter</td>
        <td></td>
      </tr>
    </tbody>
    </table>


- 命名限制

  | 对象               | 限制                                       |
  | ------------------ | ------------------------------------------ |
  | 库表名映射修改     | 只支持字母，数字和下划线，长度不超过1024。 |
  | 指定全局分区键列名 | 只支持字母，数字和下划线，长度不超过1024。 |
  | 集群名             | default_cluster                            |