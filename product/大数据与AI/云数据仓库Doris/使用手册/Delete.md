## 批量删除
目前 Doris 支持 [Broker Load（HDFS数据）](https://cloud.tencent.com/document/product/1387/70831)，[Routine Load（Kafka 数据）](https://cloud.tencent.com/document/product/1387/80258)， [Stream load（本地文件）](https://cloud.tencent.com/document/product/1387/70832)等多种导入方式，对于数据的删除目前只能通过 delete 语句进行删除，使用 delete 语句的方式删除时，每执行一次 delete 都会生成一个新的数据版本，如果频繁删除会严重影响查询性能，并且在使用 delete 方式删除时，是通过生成一个空的 rowset 来记录删除条件实现，每次读取都要对删除条件进行过滤，同样在条件较多时会对性能造成影响。
对比其他的系统，greenplum 的实现方式更像是传统数据库产品，snowflake 通过 merge 语法实现。

对于类似于 cdc 数据导入的场景，数据中 insert 和 delete 一般是穿插出现的，面对这种场景我们目前的导入方式也无法满足，即使我们能够分离出 insert 和 delete 虽然可以解决导入的问题，但是仍然解决不了删除的问题。使用批量删除功能可以解决这些个别场景的需求。数据导入有三种合并方式：
1. APPEND: 数据全部追加到现有数据中；
2. DELETE: 删除所有与导入数据key 列值相同的行；
3. MERGE: 根据 DELETE ON 的决定 APPEND 还是 DELETE。

### 基本原理
通过增加一个隐藏列`__DORIS_DELETE_SIGN__`实现，因为我们只是在 unique 模型上做批量删除，因此只需要增加一个类型为 bool 聚合函数为 replace 的隐藏列即可。在 BE 各种聚合写入流程都和正常列一样，读取方案有两个：
在 FE 遇到select * 等扩展时去掉`__DORIS_DELETE_SIGN__`列，并且默认加上 `__DORIS_DELETE_SIGN__ != true` 的条件， BE 读取时都会加上一列进行判断，通过条件确定是否删除。

#### 导入
导入时在 FE 解析时将隐藏列的值设置成 `DELETE ON` 表达式的值，其他的聚合行为和 replace 的聚合列相同。

#### 读取
读取时在所有存在隐藏列的 olapScanNode 上增加`__DORIS_DELETE_SIGN__ != true` 的条件，BE 不感知这一过程，正常执行。

#### Cumulative Compaction
Cumulative Compaction 时将隐藏列看作正常的列处理，Compaction 逻辑没有变化。

#### Base Compaction
Base Compaction 时要将标记为删除的行的删掉，以减少数据占用的空间。

### 启用批量删除支持
启用批量删除支持有一下两种形式：
1. 通过在 FE 配置文件中增加`enable_batch_delete_by_default=true` 重启fe 后新建表的都支持批量删除，此选项默认为 false。
2. 对于没有更改上述 FE 配置或对于以存在的不支持批量删除功能的表，可以使用如下语句： `ALTER TABLE tablename ENABLE FEATURE "BATCH_DELETE"` 来启用批量删除。本操作本质上是一个 schema change 操作，操作立即返回，可以通过`show alter table column` 来确认操作是否完成。

那么如何确定一个表是否支持批量删除，可以通过 设置一个session variable 来显示隐藏列 `SET show_hidden_columns=true` ，之后使用`desc tablename`，如果输出中有`__DORIS_DELETE_SIGN__` 列则支持，如果没有则不支持。

### 语法说明
导入的语法设计方面主要是增加一个指定删除标记列的字段的 colum 映射，并且需要在导入的数据中增加一列，各种导入方式设置的语法如下。

#### Stream Load
`Stream Load` 的写法在header 中的 columns 字段增加一个设置删除标记列的字段， 示例 `-H "columns: k1, k2, label_c3" -H "merge_type: [MERGE|APPEND|DELETE]" -H "delete: label_c3=1"`。

#### Broker Load
`Broker Load` 的写法在 `PROPERTIES` 处设置删除标记列的字段，语法如下：
```sql
LOAD LABEL db1.label1
(
    [MERGE|APPEND|DELETE] DATA INFILE("hdfs://abc.com:8888/user/palo/test/ml/file1")
    INTO TABLE tbl1
    COLUMNS TERMINATED BY ","
    (tmp_c1,tmp_c2, label_c3)
    SET
    (
        id=tmp_c2,
        name=tmp_c1,
    )
    [DELETE ON label_c3=true]
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

#### Routine Load
`Routine Load`的写法在  `columns`字段增加映射，映射方式同上，语法如下：
```sql
CREATE ROUTINE LOAD example_db.test1 ON example_tbl 
 [WITH MERGE|APPEND|DELETE]
 COLUMNS(k1, k2, k3, v1, v2, label),
 WHERE k1 > 100 and k2 like "%doris%"
 [DELETE ON label=true]
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

### 注意事项
1. 由于除`Stream Load` 外的导入操作在doris 内部有可能乱序执行，因此在使用`MERGE` 方式导入时如果不是`Stream Load`，需要与 load sequence 一起使用，具体的语法可以参照 [sequence 列](https://cloud.tencent.com/document/product/1387/70877)  相关的文档。
2. `DELETE ON` 条件只能与 MERGE 一起使用。

### 使用示例
#### 查看是否启用批量删除支持
```sql
mysql> SET show_hidden_columns=true;
Query OK, 0 rows affected (0.00 sec)

mysql> DESC test;
+-----------------------+--------------+------+-------+---------+---------+
| Field                 | Type         | Null | Key   | Default | Extra   |
+-----------------------+--------------+------+-------+---------+---------+
| name                  | VARCHAR(100) | No   | true  | NULL    |         |
| gender                | VARCHAR(10)  | Yes  | false | NULL    | REPLACE |
| age                   | INT          | Yes  | false | NULL    | REPLACE |
| __DORIS_DELETE_SIGN__ | TINYINT      | No   | false | 0       | REPLACE |
+-----------------------+--------------+------+-------+---------+---------+
4 rows in set (0.00 sec)
```

#### Stream Load 使用示例
1. 正常导入数据：
```bash
curl --location-trusted -u root: -H "column_separator:," -H "columns: siteid, citycode, username, pv" -H "merge_type: APPEND"  -T ~/table1_data http://127.0.0.1:8130/api/test/table1/_stream_load
```
其中的 APPEND 条件可以省略，与下面的语句效果相同：
```bash
curl --location-trusted -u root: -H "column_separator:," -H "columns: siteid, citycode, username, pv" -T ~/table1_data http://127.0.0.1:8130/api/test/table1/_stream_load
```

2. 将与导入数据 key 相同的数据全部删除：
```bash
curl --location-trusted -u root: -H "column_separator:," -H "columns: siteid, citycode, username, pv" -H "merge_type: DELETE"  -T ~/table1_data http://127.0.0.1:8130/api/test/table1/_stream_load
```
假设导入表中原有数据为:
```text
+--------+----------+----------+------+
| siteid | citycode | username | pv   |
+--------+----------+----------+------+
|      3 |        2 | tom      |    2 |
|      4 |        3 | bush     |    3 |
|      5 |        3 | helen    |    3 |
+--------+----------+----------+------+
```
导入数据为：
```text
3,2,tom,0
```
导入后数据变成:
```text
+--------+----------+----------+------+
| siteid | citycode | username | pv   |
+--------+----------+----------+------+
|      4 |        3 | bush     |    3 |
|      5 |        3 | helen    |    3 |
+--------+----------+----------+------+
```

3. 将导入数据中与`site_id=1` 的行的 key 列相同的行。
```bash
curl --location-trusted -u root: -H "column_separator:," -H "columns: siteid, citycode, username, pv" -H "merge_type: MERGE" -H "delete: siteid=1"  -T ~/table1_data http://127.0.0.1:8130/api/test/table1/_stream_load
```
假设导入前数据为：
```text
+--------+----------+----------+------+
| siteid | citycode | username | pv   |
+--------+----------+----------+------+
|      4 |        3 | bush     |    3 |
|      5 |        3 | helen    |    3 |
|      1 |        1 | jim      |    2 |
+--------+----------+----------+------+
```
导入数据为：
```text
2,1,grace,2
3,2,tom,2
1,1,jim,2
```
导入后为：
```text
+--------+----------+----------+------+
| siteid | citycode | username | pv   |
+--------+----------+----------+------+
|      4 |        3 | bush     |    3 |
|      2 |        1 | grace    |    2 |
|      3 |        2 | tom      |    2 |
|      5 |        3 | helen    |    3 |
+--------+----------+----------+------+
```

## Sql Delete 操作
Delete 不同于其他导入方式，它是一个同步过程，与 Insert into 相似，所有的 Delete 操作在 Doris 中是一个独立的导入作业，一般 Delete 语句需要指定表和分区以及删除的条件来筛选要删除的数据，并将会同时删除 base 表和 rollup 表的数据。

### 语法
delete 操作的语法详见官网 DELETE 语法。

### 返回结果
Delete 命令是一个 SQL 命令，返回结果是同步的，分为以下几种：
1. 执行成功
如果 Delete 顺利执行完成并可见，将返回下列结果，`Query OK`表示成功。
```sql
mysql> delete from test_tbl PARTITION p1 where k1 = 1;
Query OK, 0 rows affected (0.04 sec)
{'label':'delete_e7830c72-eb14-4cb9-bbb6-eebd4511d251', 'status':'VISIBLE', 'txnId':'4005'}
```

2. 提交成功，但未可见。
Doris 的事务提交分为两步：提交和发布版本，只有完成了发布版本步骤，结果才对用户是可见的。若已经提交成功了，那么就可以认为最终一定会发布成功，Doris 会尝试在提交完后等待发布一段时间，如果超时后即使发布版本还未完成也会优先返回给用户，提示用户提交已经完成。若如果 Delete 已经提交并执行，但是仍未发布版本和可见，将返回下列结果：
```sql
 mysql> delete from test_tbl PARTITION p1 where k1 = 1;
 Query OK, 0 rows affected (0.04 sec)
 {'label':'delete_e7830c72-eb14-4cb9-bbb6-eebd4511d251', 'status':'COMMITTED', 'txnId':'4005', 'err':'delete job is committed but may be taking effect later' }
```
结果会同时返回一个 json 字符串：
`affected rows`：表示此次删除影响的行，由于Doris的删除目前是逻辑删除，因此对于这个值是恒为0。
`label`：自动生成的 label，是该导入作业的标识。每个导入作业，都有一个在单 database 内部唯一的 Label。
`status`：表示数据删除是否可见，如果可见则显示`VISIBLE`，如果不可见则显示`COMMITTED`。
`txnId`：这个Delete job对应的事务id。
`err`：字段会显示一些本次删除的详细信息。
3. 提交失败，事务取消。
如果 Delete 语句没有提交成功，将会被 Doris 自动中止，返回下列结果：
```sql
mysql> delete from test_tbl partition p1 where k1 > 80;
ERROR 1064 (HY000): errCode = 2, detailMessage = {错误原因}
```
示例：
例如说一个超时的删除，将会返回 timeout 时间和未完成的`(tablet=replica)`。
```sql
mysql> delete from test_tbl partition p1 where k1 > 80;
ERROR 1064 (HY000): errCode = 2, detailMessage = failed to delete replicas from job: 4005, Unfinished replicas:10000=60000, 10001=60000, 10002=60000
```

**综上，对于 Delete 操作返回结果的正确处理逻辑为：**
1. 如果返回结果为 `ERROR 1064 (HY000)`，则表示删除失败。
2. 如果返回结果为 `Query OK`，则表示删除执行成功。
	- 如果 `status` 为 `COMMITTED`，表示数据仍不可见，用户可以稍等一段时间再用 `show delete` 命令查看结果。
	- 如果 `status` 为 `VISIBLE`，表示数据删除成功。

### Delete 操作相关 FE 配置
**TIMEOUT 配置**
总体来说，Doris 的删除作业的超时时间限制在30秒到5分钟时间内，具体时间可通过下面配置项调整
- `tablet_delete_timeout_second`
delete 自身的超时时间是可受指定分区下 tablet 的数量弹性改变的，此项配置为平均一个 tablet 所贡献的 timeout 时间，默认值为2。
假设此次删除所指定分区下有5个 tablet，那么可提供给 delete 的 timeout 时间为10秒，由于低于最低超时时间30秒，因此最终超时时间为30秒。

- `load_straggler_wait_second`
如果用户预估的数据量确实比较大，使得5分钟的上限不足时，用户可以通过此项调整 timeout 上限，默认值为300。

**TIMEOUT 的具体计算规则为(秒)**
```
TIMEOUT = MIN(load_straggler_wait_second, MAX(30, tablet_delete_timeout_second * tablet_num))
```

- `query_timeout`
因为 delete 本身是一个 SQL 命令，因此删除语句也会受 session 限制，timeout 还受 Session 中的 `query_timeout` 值影响，可以通过 `SET query_timeout = xxx` 来增加超时时间，单位是秒。

**IN 谓词配置**
- `max_allowed_in_element_num_of_delete`
如果用户在使用 in 谓词时需要占用的元素比较多，用户可以通过此项调整允许携带的元素上限，默认值为1024。

### 查看历史记录
用户可以通过 show delete 语句查看历史上已执行完成的删除记录。
语法如下：
```sql
SHOW DELETE [FROM db_name]
```
使用示例：
```sql
mysql> show delete from test_db;
+-----------+---------------+---------------------+-----------------+----------+
| TableName | PartitionName | CreateTime          | DeleteCondition | State    |
+-----------+---------------+---------------------+-----------------+----------+
| empty_tbl | p3            | 2020-04-15 23:09:35 | k1 EQ "1"       | FINISHED |
| test_tbl  | p4            | 2020-04-15 23:09:53 | k1 GT "80"      | FINISHED |
+-----------+---------------+---------------------+-----------------+----------+
2 rows in set (0.00 sec)
```

### 注意事项
不同于 Insert into 命令，delete 不能手动指定`label`，有关 label 的概念可以查看 [Insert Into](https://cloud.tencent.com/document/product/1387/70875) 文档。

### 更多帮助
关于 **delete** 使用的更多详细语法，请参阅 TODO: delete 命令手册，也可以在 Mysql 客户端命令行下输入 `HELP DELETE` 获取更多帮助信息。
