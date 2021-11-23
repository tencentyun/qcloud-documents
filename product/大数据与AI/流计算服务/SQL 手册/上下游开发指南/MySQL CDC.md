## 介绍

MySQL 的 CDC 源表，支持对 MySQL 数据库的全量和增量读取，并保证 Exactly Once 语义。MySQL CDC 底层使用了 Debezium 来做 CDC（Change Data Capture）。

工作机制如下：

1. 获取一个全局读锁，从而阻塞住其他数据库客户端的写操作。 
2. 开启一个可重复读语义的事务，来保证后续在同一个事务内读操作都是在一个一致性快照中完成的。
3. 读取 Binlog 的当前位置。
4. 读取连接器中配置的数据库和表的模式（schema）信息。
5. 释放全局读锁，允许其他的数据库客户端对数据库进行写操作。 
6. 扫描全表，当全表数据读取完后，会从第3步中得到的 Binlog 位置获取增量的变更记录。
   Flink 作业运行期间会周期性执行快照，记录下 Binlog 位置，当作业崩溃恢复时，便会从之前记录的 Binlog 点继续处理，从而保证 Exactly Once 语义。

## 版本说明

| Flink 版本 | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| 1.11      | <li>支持 mysql 版本为 5.6</li>                       |
| 1.13      | <li>支持 mysql 版本为 5.7 以上 和 8.x</li><li>默认配置，需要 source 表有 pk。如果 source 表没有 pk，需要 with 参数需要设置 `'scan.incremental.snapshot.enabled' = 'false'`</li><li>如果 mysql 主键类型是 `bigint unsigned`，需在 with 中添加 `'debezium.bigint.unsigned.handling.mode' = 'precise'`</li> |

## 使用范围

MySQL CDC 只支持作为源表。

## DDL 定义

```sql
CREATE TABLE `mysql_cdc_source_table` (
  `id` INT,
  `name` STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'mysql-cdc',	  -- 固定值 'mysql-cdc'
  'hostname' = '192.168.10.22',   -- 数据库的 IP
  'port' = '3306',                -- 数据库的访问端口
  'username' = 'debezium',        -- 数据库访问的用户名（需要提供 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD 权限）
  'password' = 'hello@world!',    -- 数据库访问的密码
  'database-name' = 'YourDatabase',   -- 需要同步的数据库
  'table-name' = 'YourTable'      -- 需要同步的数据表名
);
```

## WITH 参数

| 参数                                     | 说明                                                         | 是否必填 | 备注                                                         |
| :--------------------------------------- | :----------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| connector                                | 源表类型                                                     | 是       | 固定值为 `mysql-cdc`                                         |
| hostname                                 | MySQL 数据库的 IP 地址或者 Hostname                          | 是       | -                                                            |
| port                                     | MySQL 数据库服务的端口号                                     | 否       | 默认值为3306                                                 |
| username                                 | MySQL 数据库服务的用户名                                     | 是       | 有特定权限（包括 SELECT、RELOAD、SHOW DATABASES、REPLICATION SLAVE 和 REPLICATION CLIENT）的 MySQL 用户 |
| password                                 | MySQL 数据库服务的密码                                       | 是       | -                                                            |
| database-name                            | MySQL 数据库名称                                             | 是       | 数据库名称支持正则表达式以读取多个数据库的数据               |
| table-name                               | MySQL 表名                                                   | 是       | 表名支持正则表达式以读取多个表的数据                         |
| server-id                                | 数据库客户端的一个 ID                                        | 否       | 该 ID 必须是 MySQL 集群中全局唯一的。建议针对同一个数据库的每个作业都设置一个不同的 ID，可以设置为一个范围值，例如`5400-5405`。默认会随机生成一个5400 - 6400的值 |
| server-time-zone                         | 数据库在使用的会话时区                                       | 否       | 例如 Asia/Shanghai，该参数控制了 MySQL 中的 TIMESTAMP 类型如何转成 STRING 类型 |
| append-mode                              | 开启 append 流模式                                             | 否       | 例如：将 mysql-cdc 数据以 append 的方式同步到 hive                |
| debezium.min.row.count.to.stream.results | 当表的条数大于该值时，会使用分批读取模式                     | 否       | 默认值为1000。Flink 采用以下方式读取 MySQL 源表数据：<li/>全量读取：直接将整个表的数据读取到内存里。优点是速度快，缺点是会消耗对应大小的内存，如果源表数据量非常大，可能会有 OOM 风险<li/>分批读取：分多次读取，每次读取一定数量的行数，直到读取完所有数据。优点是读取数据量比较大的表没有 OOM 风险，缺点是读取速度相对较慢 |
| debezium.snapshot.fetch.size             | 在 Snapshot 阶段，每次读取 MySQL 源表数据行数的最大值        | 否       | 仅当分批读取模式时，该参数生效                               |
| debezium.skipped.operations              | 需要过滤的 oplog 操作。操作包括 c 表示插入，u 表示更新，d 表示删除。默认情况下，不跳过任何操作，以逗号分隔。 | 否       | -                                                            |
| debezium.\*                              | Debezium 属性参数                                            | 否       | 从更细粒度控制 Debezium 客户端的行为。例如`'debezium.snapshot.mode' = 'never'`，详情请参见 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/mysql.html?spm=a2c4g.11186623.2.9.28af38b6Z3SJlk#mysql-connector-configuration-properties_debezium) |
| scan.incremental.snapshot.enabled        | 增量快照                                                     | 否       | Flink1.13支持，默认为 true                                         |
| scan.incremental.snapshot.chunk.size     | 当读取表的快照时，表快照捕获的表的块大小(行数)。             | 否       | Flink1.13支持，默认为8096                                         |
| scan.incremental.snapshot.chunk.size     | 当读取表快照时，每次轮询的最大读取大小。                     | 否       | Flink1.13支持，默认为1024                                         |

## 可用元数据（仅 Flink1.13 及以上版本集群可使用）

以下元数据只能作为表定义中的只读（VIRTUAL）列：

<table>
    <tr>
        <th>列</th>
        <th>数据类型</th>
        <th>描述</th>
    </tr>
    <tr>
        <td>database_name</td>
        <td>STRING NOT NULL</td>
        <td>包含该 Row 的数据库名称</td>
    </tr>
    <tr>
        <td>table_name</td>
        <td>STRING NOT NULL</td>
        <td>包含该 Row 的表名称</td>
    </tr>
    <tr>
        <td>op_ts</td>
        <td>TIMESTAMP_LTZ(3) NOT NULL</td>
        <td>Row 在数据库中进行更改的时间</td>
    </tr>
    <tr>
        <td>batch_id</td>
        <td>BIGINT</td>
        <td>binlog 的批 id</td>
    </tr>
    <tr>
        <td>is_ddl</td>
        <td>BOOLEAN</td>
        <td>是否 DDL 语句</td>
    </tr>
    <tr>
        <td>mysql_type</td>
        <td>MAP</td>
        <td>数据表结构</td>
    </tr>
    <tr>
        <td>update_before</td>
        <td>ARRAY</td>
        <td>未修改前字段的值</td>
    </tr>
    <tr>
        <td>pk_names</td>
        <td>ARRAY</td>
        <td>主键字段名</td>
    </tr>
    <tr>
        <td>sql</td>
        <td>STRING</td>
        <td>暂时为空</td>
    </tr>
    <tr>
        <td>sql_type</td>
        <td>MAP</td>
        <td>sql_type 表的字段到 java 数据类型 ID 的映射</td>
    </tr>
    <tr>
        <td>ts</td>
        <td>TIMESTAMP_LTZ(3) NOT NULL</td>
        <td>收到该 ROW 并处理的当前时间</td>
    </tr>
    <tr>
        <td>op_type</td>
        <td>STRING</td>
        <td>数据库操作类型，例如 INSERT/DELETE 等</td>
    </tr>
</table>


## 使用示例

```sql
CREATE TABLE `mysql_cdc_source_table` (
      `id` INT,
      `name` STRING,
      `database_name` string METADATA FROM 'meta.database_name',
      `table_name`    string METADATA FROM 'meta.table_name',
      `op_ts`         timestamp(3) METADATA FROM 'meta.op_ts',
      `op_type` string METADATA FROM 'meta.op_type',
      `batch_id` bigint METADATA FROM 'meta.batch_id',
      `is_ddl` boolean METADATA FROM 'meta.is_ddl',
      `update_before` ARRAY<MAP<STRING, STRING>> METADATA FROM 'meta.update_before',
      `mysql_type` MAP<STRING, STRING> METADATA FROM 'meta.mysql_type',
      `pk_names` ARRAY<STRING> METADATA FROM 'meta.pk_names',
      `sql` STRING METADATA FROM 'meta.sql',
      `sql_type` MAP<STRING, INT> METADATA FROM 'meta.sql_type',
      `ingestion_ts` TIMESTAMP(3) METADATA FROM 'meta.ts',
      PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
      'connector' = 'mysql-cdc',	  -- 固定值 'mysql-cdc'
      'hostname' = '192.168.10.22',   -- 数据库的 IP
      'port' = '3306',                -- 数据库的访问端口
      'username' = 'debezium',        -- 数据库访问的用户名（需要提供 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD 权限）
      'password' = 'hello@world!',    -- 数据库访问的密码
      'database-name' = 'YourDatabase',   -- 需要同步的数据库
      'table-name' = 'YourTable'      -- 需要同步的数据表名
      );
```

## MySQL 分库分表读取方式
目前 Oceanus 已支持 MySQL 分库分表的读取。

如果 MySQL 是一个分库分表的数据库，分成了 A_1、 A_2、A_3 ...等多个表，**且所有表的 schema 一致**，则可以通过 table-name 选项，指定一个正则表达式来匹配读取多张表，例如设置 table-name 为 **A\_.\*** ，监控所有 **A\_** 前缀的表。**database-name 选项也支持该功能**。

>? 如果 database-name 设置为正则匹配的话，需要使用`()`把正则式包围起来。 


## 类型映射

MySQL 的 CDC 和 Flink 字段类型对应关系如下：

<table>
  <tr>
    <th><b>MySQL CDC 字段类型</th>
    <th><b>Flink 字段类型</th>
  </tr>
  <tr>
    <td>TINYINT</td>
    <td>TINYINT</td>
  </tr>
  <tr>
    <td>SMALLINT</td>
    <td rowspan="2">SMALLINT</td>
  </tr>
  <tr>
    <td>TINYINT UNSIGNED</td>
  </tr>
  <tr>
    <td>INT</td>
    <td rowspan="3">INT</td>
  </tr>
  <tr>
    <td>MEDIUMINT</td>
  </tr>
  <tr>
    <td>SMALLINT UNSIGNED</td>
  </tr>
  <tr>
    <td>BIGINT</td>
    <td rowspan="2">BIGINT</td>
  </tr>
  <tr>
    <td>INT UNSIGNED</td>
  </tr>
  <tr>
    <td>BIGINT UNSIGNED</td>
    <td>DECIMAL(20, 0)</td>
  </tr>
  <tr>
    <td>FLOAT</td>
    <td>FLOAT</td>
  </tr>
  <tr>
    <td>DOUBLE</td>
    <td rowspan="2">DOUBLE</td>
  </tr>
  <tr>
    <td>DOUBLE PRECISION</td>
  </tr>
  <tr>
    <td>NUMERIC(p, s)</td>
    <td rowspan="2">DECIMAL(p, s)</td>
  </tr>
  <tr>
    <td>DECIMAL(p, s)</td>
  </tr>
  <tr>
    <td>BOOLEAN</td>
    <td rowspan="2">BOOLEAN</td>
  </tr>
  <tr>
    <td>TINYINT(1)</td>
  </tr>
  <tr>
    <td>DATE</td>
    <td>DATE</td>
  </tr>
  <tr>
    <td>TIME [(p)]</td>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>DATETIME [(p)]</td>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td rowspan="2">TIMESTAMP [(p)]</td>
    <td>TIMESTAMP [(p)]</td>
  </tr>
  <tr>
    <td>TIMESTAMP [(p)] WITH LOCAL TIME ZONE</td>
  </tr>
  <tr>
    <td>CHAR(n)</td>
    <td rowspan="3">STRING</td>
  </tr>
  <tr>
    <td>VARCHAR(n)</td>
  </tr>
  <tr>
    <td>TEXT</td>
  </tr>
  <tr>
    <td>BINARY</td>
    <td rowspan="3">BYTES</td>
  </tr>
  <tr>
    <td>VARBINARY</td>
  </tr>
  <tr>
    <td> BLOB</td>
  </tr>
</table>


## 代码示例
```sql
CREATE TABLE `mysql_cdc_source_table` (
  `id` INT,
  `name` STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'mysql-cdc',	  -- 固定值 'mysql-cdc'
  'hostname' = '192.168.10.22',   -- 数据库的 IP
  'port' = '3306',                -- 数据库的访问端口
  'username' = 'debezium',        -- 数据库访问的用户名（需要提供 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD 权限）
  'password' = 'hello@world!',    -- 数据库访问的密码
  'database-name' = 'YourDatabase',   -- 需要同步的数据库
  'table-name' = 'YourTable'      -- 需要同步的数据表名
);

CREATE TABLE `print_table` (
  `id` INT,
  `name` STRING
) WITH (
 'connector' = 'print'
);
insert into print_table select * from mysql_cdc_source_table;
```

## 注意事项
### 用户权限
用于同步的源数据库的用户必须拥有以下权限 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD。
```mysql
GRANT SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, SELECT, RELOAD  ON ${database}.${table} TO '${username}';
FLUSH PRIVILEGES;
```

### 全局读锁
上述的工作原理中，可以看到第一步就会获取一个全局读锁，用于获取 schema 和 Binlog 位置。这里会阻塞其他客户端的写入，因此仍可能对线上业务造成影响。 若可以接受 At Least Once 语义，可通过设置 `'debezium.snapshot.locking.mode' = 'none'` 跳过这个阶段。

### 只关注表的变更
若只关心表的变更，而不关心原有表中的数据，可通过设置 `'debezium.snapshot.mode' =  'schema_only'` 实现。具体可以参考 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/mysql.html?spm=a2c4g.11186623.2.9.28af38b6Z3SJlk#mysql-connector-configuration-properties_debezium)。

### 联合主键设置
例如，下面的 DDL 设置了`index1`、`index2`、`index3`、`index4` 4个字段为联合主键索引，这4个字段必须定义在 DDL 的最前面，而且顺序要和 `PRIMARY KEY` 定义保持一致。
```sql
CREATE TABLE db_order_dim (
  `index1` STRING,
  `index2` STRING,
  `index3` STRING,
  `index4` STRING,
  `field5` STRING,
  `field6` STRING,
  PRIMARY KEY(`index1`, `index2`, `index3`, `index4`) NOT enforced
) WITH (
  ...
);
```

### server-id	定义
建议显式的定义`server-id`，避免不同作业读取同一个库可能出现的冲突问题，可以设置为范围值，例如`5400-5405`，也可以是单个值。

### Flink1.13版本支持增量并发处理
增量快照是一种读取表快照的新机制。与旧的快照机制相比，增量快照有很多优点，包括：
1. 读取快照时，源可以是并行的。
2. 读取快照时，源可以在块粒度上执行检查点。
3. 读取快照时，源不需要获取全局读锁（FLUSH TABLES WITH read lock）。

如果您希望源并行运行，每个并行读取器应该有一个唯一的服务器 ID。此时，'server-id' 必须是'5400-6400'这样的范围，且范围必须大于并行度。
