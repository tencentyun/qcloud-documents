## 介绍

HBase Connector 提供了对 HBase 集群的读写支持。Oceanus 已经提供了内置的`flink-connector-hbase` Connector 组件。

## 版本说明

| Flink 版本 | 说明                            |
| :-------- | :------------------------------ |
| 1.11      | 支持 hbase-1.4.x                |
| 1.13      | 支持 hbase-1.4.x 和 hbase-2.2.x |

## 使用范围

可以作为源表，以及Tuple、Upsert 数据流的目的表。

## 示例

### 用作数据源（Source）

```
CREATE TABLE dim_hbase (
  rowkey STRING,
  cf ROW < school_name STRING >,
  PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
  'connector' = 'hbase-1.4',                       -- Flink 1.13 支持 hbase-2.2
  'table-name' = 'dim_hbase',                      -- Hbase 表名
  'zookeeper.quorum' = 'ip:port,ip:port,ip:port'   -- Hbase 的 zookeeper 地址
);

-- Logger Sink 可以将输出数据打印到 TaskManager 的日志中
-- 程序包下载地址：https://github.com/tencentyun/flink-hello-world/releases
-- 需要先在【程序包管理】中上传该程序包，然后在【作业参数】中引用它
CREATE TABLE CustomSink ( 
  rowkey STRING, 
  school_name STRING 
) WITH ( 
  'connector' = 'logger',
  'print-identifier' = 'DebugData'
);

INSERT INTO  CustomSink SELECT dim_hbase.rowkey, dim_hbase.cf.school_name as school_name FROM dim_hbase;
```

### 用作数据目的（Sink）

```
CREATE TABLE random_source ( 
  rowkey STRING, 
  school_name STRING 
  ) WITH ( 
  'connector' = 'datagen', 
  'rows-per-second'='1',            -- 每秒产生的数据条数
  'fields.rowkey.length'='10',      -- 随机字符串的长度
  'fields.school_name.length'='10'  -- 随机字符串的长度
);

CREATE TABLE dim_hbase (
  rowkey STRING,
  cf ROW < school_name STRING >,
  PRIMARY KEY (rowkey) NOT ENFORCED
) WITH (
  'connector' = 'hbase-1.4',                          -- Flink 1.13 支持 hbase-2.2
  'table-name' = 'dim_hbase',                         -- Hbase 表名
  'zookeeper.quorum' = 'ip:port,ip:port,ip:port',     -- Hbase 的 zookeeper 地址
  'sink.buffer-flush.max-size' = '50KB',              -- 写入 Hbase 前，内存中缓存的数据条数。调大该值有利于提高 Hbase 写入性能，但会增加写入延迟和内存使用。
  'sink.buffer-flush.max-rows' = '10'                 -- 将缓存数据周期性写入到 Hbase 的间隔，可以控制写入 Hbase 的延迟。
);

INSERT INTO dim_hbase SELECT rowkey, ROW(school_name) FROM random_source;
```

## WITH 参数

| 参数                       | 说明                                                         | 是否必填 | 备注                                                         |
| :------------------------- | :----------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| connector                  | 表类型                                                       | 是       | 固定值为 `hbase-1.4`                                         |
| table-name                 | HBase 表名                                                   | 是       | -                                                            |
| zookeeper.quorum           | HBase 的 zookeeper 地址                                      | 是       | -                                                            |
| zookeeper.znode.parent     | HBase 在 zookeeper 中的根目录                                | 否       | -                                                            |
| null-string-literal        | HBase 字段类型为字符串时，如果 Flink 字段数据为 null，则将该字段赋值为 null-string-literal，并写入 HBase | 否       | 默认为 null                                                  |
| sink.buffer-flush.max-size | 写入 HBase 前，内存中缓存的数据量（字节）大小。调大该值有利于提高 HBase 写入性能，但会增加写入延迟和内存使用。**仅作为 Sink 时使用** | 否       | 默认值为2MB，支持字节单位 B、KB、MB 和 GB，不区分大小写。设置为0表示不进行缓存 |
| sink.buffer-flush.max-rows | 写入 HBase 前，内存中缓存的数据条数。调大该值有利于提高 HBase 写入性能，但会增加写入延迟和内存使用。**仅作为 Sink 时使用** | 否       | 默认值为1000，设置为0表示不进行缓存                          |
| sink.buffer-flush.interval | 将缓存数据周期性写入到 HBase 的间隔，可以控制写入 HBase 的延迟。**仅作为 Sink 时使用**。 | 否       | 默认值为1秒，支持时间单位 ms、s、min、h 和 d。设置为0表示关闭定期写入 |

## 类型映射

HBase 将所有的数据存为字节数组。读写操作时需要将数据进行序列化和反序列化。Flink 与 HBase 的数据转换关系如下：

<table>
  <tr>
    <th><b>Flink SQL 类型</th>
    <th><b>HBase 转换</th>
  </tr>
  <tr>
    <td>CHAR / VARCHAR / STRING</td>
    <td>byte[] toBytes(String s) <br> String toString(byte[] b)</td>
  </tr>
  <tr>
    <td> BOOLEAN</td>
    <td>byte[] toBytes(boolean b)<br>boolean toBoolean(byte[] b)</td>
  </tr>
  <tr>
    <td> BINARY / VARBINARY</td>
    <td>byte[]</td>
  </tr>
  <tr>
    <td> DECIMAL </td>
    <td>byte[] toBytes(BigDecimal v)<br>BigDecimal toBigDecimal(byte[] b)</td>
  </tr>
  <tr>
    <td> TINYINT </td>
    <td>new byte[] { val } <br> bytes[0] </td>
  </tr>
  <tr>
    <td> SMALLINT </td>
    <td>byte[] toBytes(short val)<br>short toShort(byte[] bytes)</td>
  </tr>
  <tr>
    <td> INT </td>
    <td>byte[] toBytes(int val)<br>int toInt(byte[] bytes)</td>
  </tr>
  <tr>
    <td> BIGINT </td>
    <td>byte[] toBytes(long val)<br>long toLong(byte[] bytes)</td>
  </tr>
  <tr>
    <td> FLOAT </td>
    <td>byte[] toBytes(float val)<br>float toFloat(byte[] bytes)</td>
  </tr>
  <tr>
    <td> DOUBLE </td>
    <td>byte[] toBytes(double val)<br>double toDouble(byte[] bytes)</td>
  </tr>
    <tr>
    <td> DATE </td>
    <td>将日期转换成自1970.01.01以来的天数，用 int 表示，并通过 byte[] toBytes(int val) 转换成字节数组</td>
  </tr>
  <tr>
    <td> TIME </td>
    <td>将时间转换成自00:00:00以来的毫秒数，用 int 表示，并通过 byte[] toBytes(int val) 转换成字节数组</td>
  </tr>
  <tr>
    <td> TIMESTAMP </td>
    <td>将时间戳转换成自1970-01-01 00:00:00以来的毫秒数，用 long 表示，并通过 byte[] toBytes(long val) 转换成字节数组</td>
  </tr>
  <tr>
    <td> ARRAY </td>
    <td> 不支持 </td>
  </tr>
  <tr>
    <td> MAP / MULTISET </td>
    <td> 不支持 </td>
  </tr>
  <tr>
    <td> ROW </td>
    <td> 不支持 </td>
  </tr>
</table>


## 注意事项

HBase Connector 一般会使用 DDL 语句中定义的主键，以 upsert 模式工作，与外部系统交换变更日志信息。因此，必须在 HBase 的 rowkey 字段上定义主键（必须声明 rowkey 字段）。如果未声明 PRIMARY KEY 子句，则 HBase 连接器默认将 rowkey 作为主键。
