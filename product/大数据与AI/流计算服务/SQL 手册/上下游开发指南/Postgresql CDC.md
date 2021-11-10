## 介绍

Postgres 的 CDC 源表（即 Postgres 的流式源表）用于依次读取 PostgreSQL 数据库全量快照数据和变更数据，保证不多读也不少读一条数据。即使发生故障，也能采用 Exactly Once 方式处理。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围

PostgreSQL CDC 只支持作为源表。支持的 PostgreSQL 版本为9.6及以上版本。

## DDL 定义

```sql
CREATE TABLE postgres_cdc_source_table (
  id INT,
  name STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'postgres-cdc',             -- 固定值 'postgres-cdc'
  'hostname' = 'yourHostname',              -- 数据库的 IP
  'port' = '5432',                          -- 数据库的访问端口
  'username' = 'yourUserName',              -- 数据库访问的用户名（需要提供 REPLICATION、LOGIN、SCHEMA、DATABASE、SELECT权限）
  'password' = 'yourPassWord',              -- 数据库访问的密码
  'database-name' = 'yourDatabaseName',     -- 需要同步的数据库
  'schema-name' = 'yourSchemaName',         -- 需要同步的数据表所属schema (支持正则表达式)
  'table-name' = 'yourTableName',           -- 需要同步的数据表名 (支持正则表达式)
  'debezium.slot.name' = 'customSlotName'   -- 定义一个唯一slot名称
);
```

## WITH 参数

| 参数                 | 说明                                   | 是否必填 | 备注                                                         |
| :------------------- | :------------------------------------- | :------- | :----------------------------------------------------------- |
| connector            | 源表类型                               | 是       | 固定值为 `postgres-cdc`                                      |
| hostname             | Postgres 数据库的 IP 地址或者 Hostname | 是       | -                                                            |
| username             | Postgres 数据库服务的用户名            | 是       | 有特定权限（包括 REPLICATION、LOGIN、SCHEMA、DATABASE、SELECT）的 Postgres 用户 |
| password             | Postgres 数据库服务的密码              | 是       | -                                                            |
| database-name        | Postgres 数据库名称                    | 是       | -                                                            |
| schema-name          | Postgres Schema 名称                   | 是       | Schema 名称支持正则表达式以读取多个 Schema 的数据            |
| table-name           | Postgres 表名                          | 是       | 表名支持正则表达式以读取多个表的数据                         |
| port                 | Postgres 数据库服务的端口号            | 否       | 默认值为5432                                                 |
| decoding.plugin.name | Postgres Logical Decoding 插件名称     | 否       | 根据 Postgres 服务上安装的插件确定。支持的插件列表如下：<li/>decoderbufs（默认值）<li/>wal2json<li/>wal2json_rds<li/>wal2json_streaming<li/>wal2json_rds_streaming<li/>pgoutput |
| debezium.\*          | Debezium 属性参数                      | 否       | 从更细粒度控制 Debezium 客户端的行为。例如`'debezium.slot.name' = 'xxxx'`，以避免出现 `PSQLException: ERROR: replication slot "dl_test" is active for PID 19997` 详情请参见 [配置属性](https://debezium.io/documentation/reference/1.2/connectors/postgresql.html?spm=a2c4g.11186623.2.10.4d4874ffcSv4ob#postgresql-connector-properties) |

## 类型映射

Postgres CDC 和 Flink 字段类型对应关系如下：

<table>
  <tr>
    <th><b>Postgres CDC 字段类型</th>
    <th><b>Flink 字段类型</th>
  </tr>
  <tr>
    <td>SMALLINT</td>
    <td rowspan="4">SMALLINT</td>
  </tr>
  <tr>
    <td>INT2</td>
  </tr>
  <tr>
    <td>SMALLSERIAL</td>
  </tr>
  <tr>
    <td>SERIAL2</td>
  </tr>
   <tr>
    <td>INTEGER</td>
    <td rowspan="2">INT</td>
  </tr>
  <tr>
    <td>SERIAL</td>
  </tr>
  <tr>
    <td>BIGINT</td>
    <td rowspan="2">BIGINT</td>
  </tr>
  <tr>
    <td>BIGSERIAL</td>
  </tr>
  <tr>
    <td>REAL</td>
    <td rowspan="2">FLOAT</td>
  </tr>
  <tr>
    <td>FLOAT4</td>
  </tr>
    <tr>
    <td>FLOAT8</td>
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
    <td>BOOLEAN</td>
  </tr>
  <tr>
    <td>DATE</td>
    <td>DATE</td>
  </tr>
  <tr>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>CHAR(n)</td>
    <td rowspan="5">STRING</td>
  </tr>
  <tr>
    <td>CHARACTER(n)</td>
  </tr>
  <tr>
    <td>VARCHAR(n)</td>
  </tr>
  <tr>
    <td>CHARACTER VARYING(n)</td>
  </tr>
  <tr>
    <td>TEXT</td>
  </tr>
  <tr>
    <td>BYTEA</td>
     <td>BYTES</td>
  </tr>
</table>


## 代码示例

```sql
CREATE TABLE postgres_cdc_source_table (
  id INT,
  name STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'postgres-cdc',             -- 固定值 'postgres-cdc'
  'hostname' = 'yourHostname',              -- 数据库的 IP
  'port' = '5432',                          -- 数据库的访问端口
  'username' = 'yourUserName',              -- 数据库访问的用户名（需要提供 REPLICATION、LOGIN、SCHEMA、DATABASE、SELECT权限）
  'password' = 'yourPassWord',              -- 数据库访问的密码
  'database-name' = 'yourDatabaseName',     -- 需要同步的数据库
  'schema-name' = 'yourSchemaName',         -- 需要同步的数据表所属schema (支持正则表达式)
  'table-name' = 'yourTableName',           -- 需要同步的数据表名 (支持正则表达式)
  'debezium.slot.name' = 'customSlotName'   -- 定义一个唯一slot名称
);

CREATE TABLE `print_table` (
  `id` INT,
  `name` STRING
) WITH (
 'connector' = 'print'
);
insert into print_table select * from postgres_cdc_source_table;
```

## 注意事项
#### 用户权限
用来同步的用户至少具有 REPLICATION、LOGIN、SCHEMA、DATABASE、SELECT 权限。
```sql
CREATE ROLE debezium_user REPLICATION LOGIN; 
GRANT USAGE ON SCHEMA schema_name TO debezium_user;
GRANT USAGE ON DATABASE schema_name TO debezium_user;
GRANT SELECT ON scheam_name.table_name, scheam_name.table_name TO debezium_user;
```
