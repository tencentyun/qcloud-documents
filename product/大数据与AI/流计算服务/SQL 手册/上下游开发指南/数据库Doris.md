## 介绍

Flink Connector Doris 目前支持通过 Flink 将数据写入 Doris，基于 [开源版本](https://doris.apache.org/master/zh-CN/extending-doris/flink-doris-connector.html) 实现。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围

Flink Connector Doris 目前仅支持 Doris sink。支持的 Doris 版本为0.14.0及以上版本，并且要求开启配置 `enable_http_server_v2 = true`。

## DDL 定义

```sql
CREATE TABLE doris_sink_table (
  id INT,
  name VARCHAR
) WITH (
  'connector' = 'doris',                    -- 固定值 'doris'
  'fenodes' = 'FE_IP:FE_HTTP_PORT',       -- Doris FE http 地址
  'table.identifier' = 'test.sales_order',  -- Doris 表名 格式：db.tbl
  'username' = 'root',                      -- 访问Doris的用户名，拥有库的写权限
  'password' = 'password',                  -- 访问Doris的密码
  'sink.batch.size' = '500',                -- 单次写BE的最大行数
  'sink.batch.interval' = '1s'              -- flush 间隔时间，超过该时间后异步线程将 缓存中数据写入BE。 默认值为1秒，支持时间单位ms、s、min、h和d。设置为0表示关闭定期写入。
);
```

## WITH 参数

| 参数                | 说明                                                         | 是否必填 | 备注           |
| ------------------- | ------------------------------------------------------------ | -------- | -------------- |
| connector           | 源表类型                                                     | 是       | 固定值 `doris` |
| fenodes             | Doris FE http 地址                                           | 是       | -              |
| table.identifier    | Doris 表名，格式：db1.tbl1                                   | 是       | -              |
| username            | 访问 Doris 的用户名                                          | 是       | -              |
| password            | 访问 Doris 的密码                                            | 是       | -              |
| sink.batch.size     | 单次写 BE 的最大行数                                         | 否       | 默认100        |
| sink.max-retries    | 写 BE 失败之后的重试次数                                     | 否       | 默认1          |
| sink.batch.interval | flush 间隔时间，超过该时间后异步线程将缓存中数据写入 BE。默认值为1秒，支持时间单位 ms、s、min、h 和 d。设置为0，表示关闭定期写入 | 否       | 默认1s         |
| sink.properties.\*  | Stream load 的导入 [参数](https://doris.apache.org/master/zh-CN/administrator-guide/config/fe_config.html#%E9%85%8D%E7%BD%AE%E9%A1%B9%E5%88%97%E8%A1%A8)。例如 `sink.properties.column_separator' = ','`等 | 否       | -              |


## 类型映射

<table>
  <tr>
    <th><b>Doris 字段类型</th>
    <th><b>Flink 字段类型</th>
  </tr>
  <tr>
    <td>NULL_TYPE</td>
    <td>NULL</td>
  </tr>
   <tr>
    <td>BOOLEAN</td>
    <td>BOOLEAN</td>
  </tr>
  <tr>
    <td>TINYINT</td>
    <td>TINYINT</td>
  </tr>
  <tr>
    <td>SMALLINT</td>
    <td>SMALLINT</td>
  </tr>
  <tr>
    <td>INT</td>
    <td>INT</td>
  </tr>
   <tr>
    <td>BIGINT</td>
    <td>BIGINT</td>
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
    <td>TIME</td>
  </tr>
  <tr>
    <td>DATE</td>
    <td rowspan="5">STRING</td>
  </tr>
  <tr>
    <td>DATETIME</td>
  </tr>
   <tr>
    <td>CHAR</td>
  </tr>
  <tr>
    <td>LARGEINT</td>
  </tr>
  <tr>
    <td>VARCHAR</td>
  </tr>
  <tr>
    <td>DECIMAL</td>
    <td rowspan="2">DECIMAL</td>
  </tr>
  <tr>
    <td>DECIMALV2</td>
  </tr>
  <tr>
    <td>HLL</td>
    <td>Unsupported datatype</td>
  </tr>
</table>


## 代码示例

```sql
CREATE TABLE datagen_source_table ( 
	id INT, 
	name STRING 
) WITH ( 
  'connector' = 'datagen',
  'rows-per-second'='1'  -- 每秒产生的数据条数
);

CREATE TABLE doris_sink_table (
  id INT,
  name STRING
) WITH (
  'connector' = 'doris',                    -- 固定值 'doris'
  'fenodes' = 'FE_IP:FE_RESFUL_PORT',       -- Doris FE http 地址
  'table.identifier' = 'test.sales_order',  -- Doris 表名 格式：db.tbl
  'username' = 'root',                      -- 访问Doris的用户名，拥有库的写权限
  'password' = 'password',                  -- 访问Doris的密码
  'sink.batch.size' = '500',                -- 单次写BE的最大行数
  'sink.batch.interval' = '1s'              -- flush 间隔时间，超过该时间后异步线程将 缓存中数据写入BE。 默认值为1秒，支持时间单位ms、s、min、h和d。设置为0表示关闭定期写入。
);

INSERT INTO doris_sink_table select * from datagen_source_table;
```


## 注意事项
### Upsert

若需要 Upsert ，则要求 Doris 表必须是 Uniqe 模型或者 Aggregate 模型。建表示例如下：
```sql
-- Uniqe 模型建表语句
CREATE TABLE `doris_sink_table` (
    `id`   int(11),
    `name` varchar(32)
) 
UNIQUE KEY(`id`) 
DISTRIBUTED BY HASH(`id`) BUCKETS 10
PROPERTIES("replication_num" = "3");

-- Aggregate 模型建表语句
CREATE TABLE `doris_sink_table` (
    `id`   int(11),
    `name` varchar(32) REPLACE DEFAULT '0'
) 
AGGREGATE KEY('id')
DISTRIBUTED BY HASH(`id`) BUCKETS 10
PROPERTIES("replication_num" = "3");  -- 注意若 BE 节点不够，会报 `Failed to find enough host in all backends` 错误，可适当减少该值。
```

### 用户权限

用户必须拥有对应的库的写权限。

```
CREATE USER 'test' IDENTIFIED BY 'test_passwd';
GRANT ALL ON test TO test;
```
