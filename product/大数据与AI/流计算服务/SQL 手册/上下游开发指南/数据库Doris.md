## 介绍

Flink Connector Doris 目前支持通过 Flink 将数据写入 Doris，基于 [开源版本](https://doris.apache.org/master/zh-CN/extending-doris/flink-doris-connector.html) 实现。

## 版本说明

| Flink 版本 | 说明     |
| :-------- | :------- |
| 1.11      | 支持     |
| 1.13      | 暂不支持 |

## 使用范围

Flink Connector Doris 目前仅支持 Doris sink。支持的 Doris 版本为0.14.0及以上版本，并且要求开启配置 enable_http_server_v2=true。

## 示例

```
CREATE TABLE random_source ( 
    id INT,
    f_random_str VARCHAR
  ) WITH ( 
	'connector' = 'datagen', 
	'rows-per-second'='200',               -- 每秒产生的数据条数
	'fields.f_sequence.kind'='sequence',   -- 有界序列（结束后自动停止输出）
	'fields.f_sequence.start'='1',         -- 序列的起始值
	'fields.f_sequence.end'='10000',       -- 序列的终止值
	'fields.f_random.kind'='random',       -- 无界的随机数
	'fields.f_random.min'='1',             -- 随机数的最小值
	'fields.f_random.max'='10000',         -- 随机数的最大值
	'fields.f_random_str.length'='10'      -- 随机字符串的长度
);

CREATE TABLE flink_doris_sink (
    id INT,
    f_random_str VARCHAR
    ) 
    WITH (
      'connector' = 'doris',                    -- 固定值 'doris'
      'fenodes' = 'FE_IP:FE_RESFUL_PORT',       -- Doris FE http 地址
      'table.identifier' = 'test.sales_order',  -- Doris 表名 格式：db.tbl
      'username' = 'root',                      -- 访问Doris的用户名，拥有库的写权限
      'password' = 'password',                  -- 访问Doris的密码
      'sink.batch.size' = '500',                -- 单次写BE的最大行数
      'sink.batch.interval' = '1s'              -- flush 间隔时间，超过该时间后异步线程将 缓存中数据写入BE。 默认值为1秒，支持时间单位ms、s、min、h和d。设置为0表示关闭定期写入。
);

INSERT INTO flink_doris_sink select * from random_source;
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
| sink.batch.interval | flush 间隔时间，超过该时间后异步线程将缓存中数据写入 BE。默认值为1秒，支持时间单位 ms、s、min、h 和 d。设置为0，表示关闭定期写入。 | 否       | 默认1s         |
| sink.properties.\*  | Stream load 的导入 [参数](https://doris.apache.org/master/zh-CN/administrator-guide/config/fe_config.html#%E9%85%8D%E7%BD%AE%E9%A1%B9%E5%88%97%E8%A1%A8)。例如 `sink.properties.column_separator' = ','`等 | 否       | -              |

## 数据类型映射

<table>
  <tr>
    <th><b>Doris Type 字段类型</th>
    <th><b>Flink Type 字段类型</th>
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

## 注意事项
### Upsert
若需要 upsert，则要求 doris 表必须带 UNIQUE KEY 约束，例如 UNIQUE KEY(\`id\`)，doris 底层表建表语句如下：
```
CREATE TABLE `sales_order` (
	`id` int(11),
	`f_random_str` varchar(32)
) 
UNIQUE KEY(`id`) 
DISTRIBUTED BY HASH(`id`) BUCKETS 10;
```

### 用户权限
用户必须拥有对应的库的写权限。
```
CREATE USER 'test' IDENTIFIED BY 'test_passwd';
GRANT ALL ON test TO test;
```
