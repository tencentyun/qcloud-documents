## 简介
MySQL 的 CDC 源表，支持对 MySQL 数据库的全量和增量读取，并保证 Exactly Once 语义。MySQL CDC 底层使用了 Debezium 来做CDC（capture data changes）。

其工作机制如下：
1. 获取一个全局读锁，从而阻塞住其他数据库客户端的写操作。 
2. 开启一个可重复读语义的事务，来保证后续在同一个事务内读操作都是在一个一致性快照中完成的。
3. 读取 Binlog 的当前位置。
4. 读取连接器中配置的数据库和表的模式（schema）信息。
5. 释放全局读锁，允许其他的数据库客户端对数据库进行写操作。 
6. 扫描全表，当全表数据读取完后，会从第3步中得到的 Binlog 位置获取增量的变更记录。

Flink 作业运行期间会周期性执行 checkpoint，记录下 Binlog 位置，当作业 Failover 时，便会从之前记录的 Binlog 点继续处理，从而保证 Exactly Once 语义。

## 使用范围
MySQL CDC 只支持作为源表。

## 示例
```sql
CREATE TABLE `MySQLSourceTable` (
    `id` bigint,
    `request_method` varchar(80),
    `response` varchar(80),
    PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
    'connector' = 'mysql-cdc',		-- 可选 'mysql-cdc' 和 'postgres-cdc'
    'hostname' = '192.168.10.22',   -- 数据库的 IP
    'port' = '3306',                -- 数据库的访问端口
    'username' = 'debezium',        -- 数据库访问的用户名（需要提供 SELECT 权限）
    'password' = 'hello@world!',    -- 数据库访问的密码
    'database-name' = 'YourData',   -- 需要同步的数据库
    'table-name' = 'YourTable'      -- 需要同步的数据表明
);
```

## 通用 WITH 参数

| 参数                                     | 说明                                                | 是否必填 | 备注                                                         |
| :--------------------------------------- | :--------------------------- | :------- | :----------------------------------- |
| connector                                | 源表类型                              | 是       | 固定值为 `mysql-cdc`                     |
| hostname                                 | MySQL 数据库的 IP 地址或者 Hostname          | 是       | -                                   |
| port                                     | MySQL 数据库服务的端口号                             | 否       | 默认值为3306                        |
| username                                 | MySQL 数据库服务的用户名                             | 是       | 有特定权限（包括 SELECT、RELOAD、SHOW DATABASES、REPLICATION SLAVE 和 REPLICATION CLIENT）的 MySQL 用户 |
| password                                 | MySQL 数据库服务的密码                               | 是       | -                            |
| database-name                            | MySQL 数据库名称            | 是       | 数据库名称支持正则表达式以读取多个数据库的数据       |
| table-name                               | MySQL 表名                     | 是       | 表名支持正则表达式以读取多个表的数据                       |
| server-id                                | 数据库客户端的一个 ID                                | 否       | 该 ID 必须是 MySQL 集群中全局唯一的。建议针对同一个数据库的每个作业都设置一个不同的 ID。默认会随机生成一个5400 - 6400的值 |
| server-time-zone                         | 数据库在使用的会话时区                              | 否       | 例如 Asia/Shanghai，该参数控制了 MySQL 中的 TIMESTAMP 类型如何转成 STRING 类型 |
| debezium.min.row.count.to.stream.results | 当表的条数大于该值时，会使用分批读取模式          | 否       | 默认值为1000。Flink 采用以下方式读取 MySQL 源表数据：<li>全量读取：直接将整个表的数据读取到内存里。优点是速度快，缺点是会消耗对应大小的内存，如果源表数据量非常大，可能会有 OOM 风险<li>分批读取：分多次读取，每次读取一定数量的行数，直到读取完所有数据。优点是读取数据量比较大的表没有 OOM 风险，缺点是读取速度相对较慢 |
| debezium.snapshot.fetch.size             | 在 Snapshot 阶段，每次读取 MySQL 源表数据行数的最大值 | 否       | 仅当分批读取模式时，该参数生效                             |
| debezium.*                               | Debezium 属性参数                                    | 否       | 从更细粒度控制 Debezium 客户端的行为。例如`'debezium.snapshot.mode' = 'never'`，详情请参见 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/mysql.html?spm=a2c4g.11186623.2.9.28af38b6Z3SJlk#mysql-connector-configuration-properties_debezium)。 |

## 类型映射
MySQL 的 CDC 和 Flink 字段类型对应关系如下：

| MySQL CDC 字段类型                    | Flink 字段类型                      |
| :----------------------------------- | :--------------------------------- |
| TINYINT                              | TINYINT                            |
| SMALLINT                             | SMALLINT                           |
| TINYINT UNSIGNED                     |                                    |
| INT                                  | INT                                |
| MEDIUMINT                            |                                    |
| SMALLINT UNSIGNED                    |                                    |
| BIGINT                               | BIGINT                             |
| INT UNSIGNED                         |                                    |
| BIGINT UNSIGNED                      | DECIMAL(20, 0)                     |
| BIGINT                               | BIGINT                             |
| FLOAT                                | FLOAT                              |
| DOUBLE                               | DOUBLE                             |
| DOUBLE PRECISION                     |                                    |
| NUMERIC(p, s)                        | DECIMAL(p, s)                      |
| DECIMAL(p, s)                        |                                    |
| BOOLEAN                              | BOOLEAN                            |
| TINYINT(1)                           |                                    |
| DATE                                 | DATE                               |
| TIME [(p)]                           | TIME [(p)] [WITHOUT TIMEZONE]      |
| DATETIME [(p)]                       | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| TIMESTAMP [(p)]                      | TIMESTAMP [(p)]                    |
| TIMESTAMP [(p)] WITH LOCAL TIME ZONE |                                    |
| CHAR(n)                              | STRING                             |
| VARCHAR(n)                           |                                    |
| TEXT                                 |                                    |
| BINARY                               | BYTES                              |
| VARBINARY                            |                                    |
| BLOB                                 |                                    |

## 注意事项
### 用户权限
用于同步的源数据库的用户必须拥有以下权限 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD。
```mysql
GRANT SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, SELECT, RELOAD  ON ${database}.${table} TO '${username}';
FLUSH PRIVILEGES;
```

### 全局读锁
上述的工作原理中，可以看到第一步就会获取一个全局读锁，用于获取 schema 和 Binlog 位置。这里会阻塞其他客户端的写入，因此仍可能对线上业务造成影响。 若可以接受 Exactly Once 语义，可通过设置 'debezium.snapshot.locking.mode' = 'none' 跳过这个阶段。

### 只关注表的变更
若只关心表的变更，而不关心原有表中的数据，可通过设置 'debezium.snapshot.mode' =  'schema_only' 实现。具体可以参考 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/mysql.html?spm=a2c4g.11186623.2.9.28af38b6Z3SJlk#mysql-connector-configuration-properties_debezium)。

