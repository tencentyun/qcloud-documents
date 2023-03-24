## 介绍
MySQL 的 CDC 源表，支持对 MySQL 数据库的全量和增量读取，并保证 Exactly Once 语义。MySQL CDC 底层使用了 Debezium 来做 CDC（Change Data Capture）。

### mysql-cdc 1.x 工作机制
1. 获取一个全局读锁，从而阻塞住其他数据库客户端的写操作。 
2. 开启一个可重复读语义的事务，来保证后续在同一个事务内读操作都是在一个一致性快照中完成的。
3. 读取 Binlog 的当前位置。
4. 读取连接器中配置的数据库和表的模式（schema）信息。
5. 释放全局读锁，允许其他的数据库客户端对数据库进行写操作。 
6. 扫描全表，当全表数据读取完后，会从第3步中得到的 Binlog 位置获取增量的变更记录。

Flink 作业运行期间会周期性执行快照，记录下 Binlog 位置，当作业崩溃恢复时，便会从之前记录的 Binlog 点继续处理，从而保证 Exactly once 语义。

### mysql-cdc 2.x 工作机制
1. mysql 表需要有主键，如果是联合主键则会选择数据表中的第一个主键作为全量阶段的 splitKey，其用来将数据分为多个分片(Chunk)。
2. 全量阶段使用无锁算法，无需给表加锁。
3. 整个同步过程分为两个阶段，全量阶段并发读取分片数据，全量阶段结束之后进入增量阶段，整个过程都支持 Checkpoint 从而保证 Exactly once 语义。

## 版本说明

| Flink 版本 | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| 1.11       | <li>支持 mysql 版本为 5.6</li>                               |
| 1.13       | <li>支持 mysql 版本为 5.6, 5.7, 8.x</li><li>默认配置，需要 source 表有 pk。如果 source 表没有 pk，需要 with 参数需要设置 `'scan.incremental.snapshot.enabled' = 'false'`</li> |
| 1.14       | <li>支持 mysql 版本为 5.6, 5.7, 8.x</li><li>默认配置，需要 source 表有 pk。如果 source 表没有 pk，需要 with 参数需要设置 `'scan.incremental.snapshot.enabled' = 'false'`</li> |

## 使用范围

MySQL CDC 只支持作为源表。

## DDL 定义
```sql
CREATE TABLE `mysql_cdc_source_table` (
  `id` INT,
  `name` STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'mysql-cdc',      -- 固定值 'mysql-cdc'
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
| ---------------------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| connector                                | 源表类型                                                     | 是       | 固定值为 `mysql-cdc`                                         |
| hostname                                 | MySQL 数据库的 IP 地址或者 Hostname                          | 是       | -                                                            |
| port                                     | MySQL 数据库服务的端口号                                     | 否       | 默认值为3306                                                 |
| username                                 | MySQL 数据库服务的用户名                                     | 是       | 有特定权限（包括 SELECT、RELOAD、SHOW DATABASES、REPLICATION SLAVE 和 REPLICATION CLIENT）的 MySQL 用户 |
| password                                 | MySQL 数据库服务的密码                                       | 是       | -                                                            |
| database-name                            | MySQL 数据库名称                                             | 是       | 数据库名称支持正则表达式以读取多个数据库的数据               |
| table-name                               | MySQL 表名                                                   | 是       | 表名支持正则表达式以读取多个表的数据                         |
| server-id                                | 数据库客户端的一个 ID                                        | 否       | 该 ID 必须是 MySQL 集群中全局唯一的。建议针对同一个数据库的每个作业都设置不同的 ID 范围值，例如`5400-5405`。默认会随机生成一个6400 - Integer.MAX_VALUE 的值 |
| server-time-zone                         | 数据库在使用的会话时区                                       | 否       | 例如 Asia/Shanghai，该参数控制了 MySQL 中的 TIMESTAMP 类型如何转成 STRING 类型 |
| append-mode                              | 开启 append 流模式                                           | 否       | Flink1.13及以上版本支持, 例如：将 mysql-cdc 数据以 append 的方式同步到 hive |
| debezium.min.row.count.to.stream.results | 当表的条数大于该值时，会使用分批读取模式                     | 否       | 默认值为1000。Flink 采用以下方式读取 MySQL 源表数据：<li/>全量读取：直接将整个表的数据读取到内存里。优点是速度快，缺点是会消耗对应大小的内存，如果源表数据量非常大，可能会有 OOM 风险<li/>分批读取：分多次读取，每次读取一定数量的行数，直到读取完所有数据。优点是读取数据量比较大的表没有 OOM 风险，缺点是读取速度相对较慢 |
| debezium.snapshot.fetch.size             | 在 Snapshot 阶段，每次读取 MySQL 源表数据行数的最大值        | 否       | 仅当分批读取模式时，该参数生效                               |
| debezium.skipped.operations              | 需要过滤的 oplog 操作。操作包括 c 表示插入，u 表示更新，d 表示删除。默认情况下，不跳过任何操作，以逗号分隔 | 否       | -                                                            |
| scan.incremental.snapshot.enabled        | 增量快照                                                     | 否       | 默认为 true                                                  |
| scan.incremental.snapshot.chunk.size     | 当读取表的快照时，表快照捕获的表的块大小(行数)               | 否       | 默认为 8096                                                  |
| scan.lazy-calculate-splits.enabled       | 全量阶段JM中数据分片懒加载避免数据量太大，分片数据太多导致JM OOM | 否       | 默认为 true                                                  |
| scan.newly-added-table.enabled           | 动态加表                                                     | 否       | 默认为 false                                                 |
| scan.split-key.mode                      | 联合主键作为 splitkey 的模式                                 | 否       | 取值为 default / specific；其中 default 为默认逻辑，采用联合主键的第一个字段作为 splitkey；设置为 specific  需要设置 scan.split-key.specific-column 指定联合主键中的某个字段 |
| scan.split-key.specific-column           | 指定联合主键中某个字段作为 splitkey                          | 否       | 当 scan.split-key.mode 为 specific 时必填。取值为联合主键中某个字段名 |
| connect.timeout                          | 尝试连接到 MySQL 数据库服务器后在超时之前等待的最长时间      | 否       | 默认 30s                                                     |
| connect.max-retries                      | 建立MySQL连接尝试最大的次数                                  | 否       | 默认 3                                                       |
| connection.pool.size                     | 连接池大小                                                   | 否       | 默认 20                                                      |
| jdbc.properties.\*                       | 自定义JDBC URL参数，例如: `'jdbc.properties.useSSL' = 'false'` | 否       | 默认 20                                                      |
| heartbeat.interval                       | 发送心跳事件的时间间隔，用于跟踪最新可用的binlog偏移量, 一般用于解决慢表的问题(更新缓慢的数据表) | 否       | 默认 20                                                      |
| debezium.\*                              | Debezium 属性参数                                            | 否       | 从更细粒度控制 Debezium 客户端的行为。例如`'debezium.snapshot.mode' = 'never'`，详情请参见 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/mysql.html?spm=a2c4g.11186623.2.9.28af38b6Z3SJlk#mysql-connector-configuration-properties_debezium) |


## 可用元数据（Flink1.13 及以上版本可使用）

支持的元数据列：

<table>
<tr>
<th>列</th>
<th>数据类型</th>
<th>描述</th>
</tr>
<tr>
<td>database_name/meta.database_name</td>
<td>STRING NOT NULL</td>
<td>包含该 Row 的数据库名称</td>
</tr>
<tr>
<td>table_name/meta.table_name</td>
<td>STRING NOT NULL</td>
<td>包含该 Row 的表名称</td>
</tr>
<tr>
<td>op_ts/meta.op_ts</td>
<td>TIMESTAMP_LTZ(3) NOT NULL</td>
<td>Row 在数据库中进行更改的时间</td>
</tr>
<tr>
<td>meta.batch_id</td>
<td>BIGINT</td>
<td>binlog 的批 id</td>
</tr>
<tr>
<td>meta.is_ddl</td>
<td>BOOLEAN</td>
<td>是否 DDL 语句</td>
</tr>
<tr>
<td>meta.mysql_type</td>
<td>MAP</td>
<td>数据表结构</td>
</tr>
<tr>
<td>meta.update_before</td>
<td>ARRAY</td>
<td>未修改前字段的值</td>
</tr>
<tr>
<td>meta.pk_names</td>
<td>ARRAY</td>
<td>主键字段名</td>
</tr>
<tr>
<td>meta.sql</td>
<td>STRING</td>
<td>暂时为空</td>
</tr>
<tr>
<td>meta.sql_type</td>
<td>MAP</td>
<td>sql_type 表的字段到 Java 数据类型 ID 的映射</td>
</tr>
<tr>
<td>meta.ts</td>
<td>TIMESTAMP_LTZ(3) NOT NULL</td>
<td>收到该 ROW 并处理的当前时间</td>
</tr>
<tr>
<td>meta.op_type</td>
<td>STRING</td>
<td>数据库操作类型，例如 INSERT/DELETE 等</td>
</tr>
<tr>
<td>meta.file</td>
<td>STRING</td>
<td>全量阶段时为空。增量阶段时为数据来自的 binlog 文件名，例如 mysql-bin.000101</td>
</tr>
<tr>
<td>meta.pos</td>
<td>BIGINT</td>
<td>全量阶段时为0。增量阶段时为数据来自的 binlog 文件偏移，例如 143127802</td>
</tr>
<tr>
<td>meta.gtid</td>
<td>STRING</td>
<td>全量阶段时为 null。增量阶段时为数据对应的 gtid 值，例如 3d3c4464-c320-11e9-8b3a-6c92bf62891a:66486240</td>
</tr>
</table>



## 使用示例

```sql
CREATE TABLE `mysql_cdc_source_table` (
      `id` INT,
      `name` STRING,
      `database_name` string METADATA FROM 'database_name',
      `table_name`    string METADATA FROM 'table_name',
      `op_ts`         timestamp(3) METADATA FROM 'op_ts',
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
      'connector' = 'mysql-cdc',      -- 固定值 'mysql-cdc'
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

>? 如果 database-name 和 table-name 设置为正则匹配的话，需要使用`()`把正则式包围起来。 


## 类型映射

MySQL 的 CDC 和 Flink 字段类型对应关系如下：

<div class="wy-table-responsive">
<table class="colwidths-auto docutils">
<thead>
<tr>
<th class="text-left">MySQL type<a href="https://dev.mysql.com/doc/man/8.0/en/data-types.html"></a></th>
<th class="text-left">Flink SQL type<a href="{% link dev/table/types.md %}"></a></th>
<th class="text-left">NOTE</th>
</tr>
</thead>
<tbody>
<tr>
<td>TINYINT</td>
<td>TINYINT</td>
<td>-</td>
</tr>
<tr>
<td>SMALLINT<br>TINYINT UNSIGNED</td>
<td>SMALLINT</td>
<td>-</td>
</tr>
<tr>
<td>
INT<br>
MEDIUMINT<br>
SMALLINT UNSIGNED</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>
BIGINT<br>
INT UNSIGNED</td>
<td>BIGINT</td>
<td>-</td>
</tr>
<tr>
<td>BIGINT UNSIGNED</td>
<td>DECIMAL(20, 0)</td>
<td>-</td>
</tr>
<tr>
<td>
REAL<br>
FLOAT<br>
</td>
<td>FLOAT</td>
<td>-</td>
</tr>
<tr>
<td>
DOUBLE
</td>
<td>DOUBLE</td>
<td>-</td>
</tr>
<tr>
<td>
NUMERIC(p, s)<br>
DECIMAL(p, s)<br>
where p <= 38<br>
</td>
<td>DECIMAL(p, s)</td>
<td>-</td>
</tr>
<tr>
<td>
NUMERIC(p, s)<br>
DECIMAL(p, s)<br>
where 38 < p <= 65<br>
</td>
<td>STRING</td>
<td>MySQL 中 DECIMAL 数据类型的精度最高为 65，而 Flink 中 DECIMAL 的精度限制为 38。 所以如果您定义一个精度大于38的十进制列，您应该把它映射到STRING，以避免精度损失</td>
</tr>
<tr>
<td>
BOOLEAN<br>
TINYINT(1)<br>
BIT(1)
</td>
<td>BOOLEAN</td>
<td>-</td>
</tr>
<tr>
<td>DATE</td>
<td>DATE</td>
<td>-</td>
</tr>
<tr>
<td>TIME [(p)]</td>
<td>TIME [(p)]</td>
<td>-</td>
</tr>
<tr>
<td>TIMESTAMP [(p)]<br>
DATETIME [(p)]
</td>
<td>TIMESTAMP [(p)]
</td>
<td>-</td>
</tr>
<tr>
<td>
CHAR(n)
</td>
<td>CHAR(n)</td>
<td>-</td>
</tr>
<tr>
<td>
VARCHAR(n)
</td>
<td>VARCHAR(n)</td>
<td>-</td>
</tr>
<tr>
<td>
BIT(n)
</td>
<td>BINARY(⌈n/8⌉)</td>
<td>-</td>
</tr>
<tr>
<td>
BINARY(n)
</td>
<td>BINARY(n)</td>
<td>-</td>
</tr>
<tr>
<td>
VARBINARY(N)
</td>
<td>VARBINARY(N)</td>
<td>-</td>
</tr>
<tr>
<td>
TINYTEXT<br>
TEXT<br>
MEDIUMTEXT<br>
LONGTEXT<br>
</td>
<td>STRING</td>
<td>-</td>
</tr>
<tr>
<td>
TINYBLOB<br>
BLOB<br>
MEDIUMBLOB<br>
LONGBLOB<br>
</td>
<td>BYTES</td>
<td>对于 MySQL 中的 BLOB 数据类型，仅支持长度不大于 2,147,483,647(2 ** 31 - 1) 的 blob</td>
</tr>
<tr>
<td>
YEAR
</td>
<td>INT</td>
<td>-</td>
</tr>
<tr>
<td>
ENUM
</td>
<td>STRING</td>
<td>-</td>
</tr>
<tr>
<td>
JSON
</td>
<td>STRING</td>
<td>JSON 数据类型会在 Flink 中转换为 JSON 格式的 STRING</td>
</tr>
<tr>
<td>
SET
</td>
<td>ARRAY&lt;STRING&gt;</td>
<td>由于 MySQL 中的 SET 数据类型是一个可以有零个或多个值的字符串对象，所以它应该总是映射到一个字符串数组      </td>
</tr>
<tr>
<td>
GEOMETRY<br>
POINT<br>
LINESTRING<br>
POLYGON<br>
MULTIPOINT<br>
MULTILINESTRING<br>
MULTIPOLYGON<br>
GEOMETRYCOLLECTION<br>
</td>
<td>
STRING
</td>
<td>
MySQL 中的空间数据类型会被转换成固定 Json 格式的 STRING      </td>
</tr>
</tbody>
</table>
</div>

## 代码示例
```sql
CREATE TABLE `mysql_cdc_source_table` (
  `id` INT,
  `name` STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'mysql-cdc',      -- 固定值 'mysql-cdc'
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
### Checkpoint 相关
- 使用 cdc 1.0 ('scan.incremental.snapshot.enabled' = 'false')时，需要做的额外参数配置。
由于 cdc 1.0，读取全量数据阶段，是无法做 checkpoint的。 当需要同步的表较多、数据较大时，可能会导致多次 cp 失败，从而引发作业失败。可以通过作业高级参数 `execution.checkpointing.tolerable-failed-checkpoints: 100` 调整 checkpoint 失败的容忍次数。

- 使用 cdc 2.0 时，必须开启 checkpoint。
当作业的并行度不为1时，必须开启checkpoint。cdc 读取完全量数据后，需要等待一个 checkpoint 才能进入增量阶段。

### 关于使用 cdc 1.0 的风险告知
当表没有主键时，只能通过使用 with 参数 `'scan.incremental.snapshot.enabled' = 'false'` 开启 cdc 1.0 模式，会存在以下风险：
1. 默认会使用 FTWRL(flush table with read lock)。
2. 虽然 FTWRL 只会持有短暂的时间，但由于 FTWRL 的机制，可能会导致**锁库**。
3. FTWRL 可能会出现的情况如下：
	- 会等待正在执行的 update/select 操作完成。
	- 在等待 update/select 完成的期间，会导致 db 不可用。会阻塞新加入的 select 查询，这是 Mysql Query Cache 机制。

如果同时启动多个不同的 mysql cdc 1.0 的 source，大概率会碰到上述情况。

### 用户权限
用于同步的源数据库的用户必须拥有以下权限 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD。
```mysql
GRANT SELECT, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'user' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

### 全局读锁
上述的工作原理中，MySQL CDC 1.x 中可以看到第一步就会获取一个全局读锁，用于获取 schema 和 Binlog 位置。这里会阻塞其他客户端的写入，因此仍可能对线上业务造成影响。 若可以接受 At Least Once 语义，可通过设置 `'debezium.snapshot.locking.mode' = 'none'` 跳过这个阶段。


### 联合主键设置
例如，下面的 DDL 设置了`index1`、`index2`、`index3`、`index4` 4个字段为联合主键索引，要和 `PRIMARY KEY` 定义保持一致，顺序不会影响正常的同步。
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

### server-id   定义
不建议显式指定 `server-id`，Oceanus 平台会自动生成随机 `server-id` 值（默认会随机生成一个 `6400 - Integer.MAX_VALUE` 的值），以避免不同作业读取同一个库可能出现的 `server-id` 冲突问题。
如果必须要手动指定 `server-id` 值，建议设置为范围值，例如 `5400-5405`，因为每个并行读取器应该有一个唯一的服务器 ID，所以 `server-id` 必须是 `5400-5405` 这样的范围，且范围必须大于并行度。
指定 `server-id` 有以下两种方式：
1. `mysql-cdc` DDL 的 WITH 参数中指定。
2. 使用 SQL Hints 来指定 `server-id` 。
``` 
SELECT * FROM source_table /*+ OPTIONS('server-id'='5401-5404') */ ;
```

### 设置 MySQL 会话超时
全量阶段读取大型数据库的时候可能会超时，您可以对 MySQL 做一些配置来避免这个问题。
- `interactive_timeout ` 服务器在关闭交互式连接之前等待其活动的秒数。请参阅 [MySQL 文档](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout)。
- `wait_timeout ` 服务器在关闭非交互式连接之前等待其活动的秒数。请参阅 [MySQL 文档](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout)。

### Flink1.13及以上版本支持增量并发处理
增量快照是一种读取表快照的新机制。与旧的快照机制相比，增量快照有很多优点，包括：
1. 读取快照时，源可以是并行的。
2. 读取快照时，源可以在块粒度上执行检查点。
3. 读取快照时，源不需要获取全局读锁（FLUSH TABLES WITH read lock）。

