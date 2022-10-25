sequence 列目前只支持 Uniq 模型，Uniq 模型主要针对需要唯一主键的场景，可以保证主键唯一性约束，但是由于使用 REPLACE 聚合方式，在同一批次中导入的数据，替换顺序不做保证。替换顺序无法保证则无法确定最终导入到表中的具体数据，存在了不确定性。

为了解决这个问题，Doris 支持了 sequence 列，通过用户在导入时指定 sequence 列，相同 key 列下，REPLACE 聚合类型的列将按照 sequence 列的值进行替换，较大值可以替换较小值，反之则无法替换。该方法将顺序的确定交给了用户，由用户控制替换顺序。

## 适用场景
Sequence 列只能在 Uniq 数据模型下使用。

## 基本原理
通过增加一个隐藏列`__DORIS_SEQUENCE_COL__`实现，该列的类型由用户在建表时指定，在导入时确定该列具体值，并依据该值对 REPLACE 列进行替换。

### 建表
创建 Uniq 表时，将按照用户指定类型自动添加一个隐藏列`__DORIS_SEQUENCE_COL__`。

### 导入
导入时，FE 在解析的过程中将隐藏列的值设置成 `order by` 表达式的值(broker load 和 routine load)，或者`function_column.sequence_col`表达式的值(stream load), value列将按照该值进行替换。隐藏列`__DORIS_SEQUENCE_COL__`的值既可以设置为数据源中一列，也可以是表结构中的一列。

### 读取
请求包含 value 列时需要需要额外读取`__DORIS_SEQUENCE_COL__`列，该列用于在相同 key 列下，REPLACE 聚合函数替换顺序的依据，较大值可以替换较小值，反之则不能替换。

### Cumulative Compaction
Cumulative Compaction 时和读取过程原理相同。

### Base Compaction
Base Compaction 时读取过程原理相同。

### 使用语法
建表时语法方面在 property 中增加了一个属性，用来标识`__DORIS_SEQUENCE_COL__`的类型
导入的语法设计方面主要是增加一个从 sequence 列的到其他 column 的映射，各个导入方式设置的将在下面介绍。

#### 建表
创建 Uniq 表时，可以指定 sequence 列类型。
```
PROPERTIES (
    "function_column.sequence_type" = 'Date',
);
```
sequence_type 用来指定 sequence 列的类型，可以为整型和时间类型。

#### stream load

stream load 的写法是在 header 中的`function_column.sequence_col`字段添加隐藏列对应的 source_sequence 的映射， 示例：
```
curl --location-trusted -u root -H "columns: k1,k2,source_sequence,v1,v2" -H "function_column.sequence_col: source_sequence" -T testData http://host:port/api/testDb/testTbl/_stream_load
```

#### broker load
在`ORDER BY` 处设置隐藏列映射的 source_sequence 字段。
```
LOAD LABEL db1.label1
(
    DATA INFILE("hdfs://host:port/user/data/*/test.txt")
    INTO TABLE `tbl1`
    COLUMNS TERMINATED BY ","
    (k1,k2,source_sequence,v1,v2)
    ORDER BY source_sequence
)
WITH BROKER 'broker'
(
    "username"="user",
    "password"="pass"
)
PROPERTIES
(
    "timeout" = "3600"
);
```

#### routine load
映射方式同上，示例如下：
```
   CREATE ROUTINE LOAD example_db.test1 ON example_tbl 
    [WITH MERGE|APPEND|DELETE]
    COLUMNS(k1, k2, source_sequence, v1, v2),
    WHERE k1 > 100 and k2 like "%doris%"
    [ORDER BY source_sequence]
    PROPERTIES
    (
        "desired_concurrent_number"="3",
        "max_batch_interval" = "20",
        "max_batch_rows" = "300000",
        "max_batch_size" = "209715200",
        "strict_mode" = "false"
    )
    FROM KAFKA
    (
        "kafka_broker_list" = "broker1:9092,broker2:9092,broker3:9092",
        "kafka_topic" = "my_topic",
        "kafka_partitions" = "0,1,2,3",
        "kafka_offsets" = "101,0,0,200"
    );
```

## 启用 sequence column 支持
在新建表时如果设置了`function_column.sequence_type` ，则新建表将支持 sequence column。
对于一个不支持 sequence column 的表，如果想要使用该功能，可以使用如下语句来启用。
```
ALTER TABLE example_db.my_table ENABLE FEATURE "SEQUENCE_LOAD" WITH PROPERTIES ("function_column.sequence_type" = "Date")
```
如果确定一个表是否支持 sequence column，可以通过设置一个 session variable来显示隐藏列 `SET show_hidden_columns=true` ，之后使用`desc tablename`，如果输出中有`__DORIS_SEQUENCE_COL__` 列则支持，如果没有则不支持。

## 使用示例
下面以 stream load 为例 展示下使用方式
1. 创建支持 sequence column 的表。
表结构如下：
```
MySQL > desc test_table;
+-------------+--------------+------+-------+---------+---------+
| Field       | Type         | Null | Key   | Default | Extra   |
+-------------+--------------+------+-------+---------+---------+
| user_id     | BIGINT       | No   | true  | NULL    |         |
| date        | DATE         | No   | true  | NULL    |         |
| group_id    | BIGINT       | No   | true  | NULL    |         |
| modify_date | DATE         | No   | false | NULL    | REPLACE |
| keyword     | VARCHAR(128) | No   | false | NULL    | REPLACE |
+-------------+--------------+------+-------+---------+---------+
```

2. 正常导入数据。
导入如下数据：
```
1       2020-02-22      1       2020-02-22      a
1       2020-02-22      1       2020-02-22      b
1       2020-02-22      1       2020-03-05      c
1       2020-02-22      1       2020-02-26      d
1       2020-02-22      1       2020-02-22      e
1       2020-02-22      1       2020-02-22      b
```
此处以 stream load 为例， 将 sequence column 映射为 modify_date 列。
```
curl --location-trusted -u root: -H "function_column.sequence_col: modify_date" -T testData http://host:port/api/test/test_table/_stream_load
```
结果为：
```
MySQL > select * from test_table;
+---------+------------+----------+-------------+---------+
| user_id | date       | group_id | modify_date | keyword |
+---------+------------+----------+-------------+---------+
|       1 | 2020-02-22 |        1 | 2020-03-05  | c       |
+---------+------------+----------+-------------+---------+
```
在这次导入中，因 sequence column 的值（也就是 modify_date 中的值）中'2020-03-05'为最大值，所以 keyword 列中最终保留了 c。

3. 替换顺序的保证。
上述步骤完成后，接着导入如下数据：
```
1       2020-02-22      1       2020-02-22      a
1       2020-02-22      1       2020-02-23      b
```
查询数据：
```
MySQL [test]> select * from test_table;
+---------+------------+----------+-------------+---------+
| user_id | date       | group_id | modify_date | keyword |
+---------+------------+----------+-------------+---------+
|       1 | 2020-02-22 |        1 | 2020-03-05  | c       |
+---------+------------+----------+-------------+---------+
```
由于新导入的数据的 sequence column 都小于表中已有的值，无法替换。
再尝试导入如下数据：
```
1       2020-02-22      1       2020-02-22      a
1       2020-02-22      1       2020-03-23      w
```
查询数据：
```
MySQL [test]> select * from test_table;
+---------+------------+----------+-------------+---------+
| user_id | date       | group_id | modify_date | keyword |
+---------+------------+----------+-------------+---------+
|       1 | 2020-02-22 |        1 | 2020-03-23  | w       |
+---------+------------+----------+-------------+---------+
```
此时就可以替换表中原有的数据。
