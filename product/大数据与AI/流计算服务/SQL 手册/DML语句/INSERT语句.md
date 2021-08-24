## INSERT INTO
INSERT INTO 语句必须和 SELECT 子查询联用，SELECT 的数据会写入到指定的数据目的表（Table Sink）中。

### 语法
```
INSERT INTO 数据目的表
SELECT 子句
```

### 示例
将 SELECT 查询的结果插入名为 KafkaSink1 的数据目的表（Sink）。
```
INSERT INTO KafkaSink1
SELECT s1.time_, s1.client_ip, s1.uri, s1.protocol_version, s2.status_code, s2.date_
FROM KafkaSource1 AS s1, KafkaSource2 AS s2
WHERE s1.time_ = s2.time_ AND s1.client_ip = s2.client_ip;
```

## Table Sink 注意事项
### 选择合适的 Connector 程序包
- 如果在 WITH 参数里指定了某个 Sink，那么请务必勾选相应的【内置 Connector】，或自行上传相应的 Connector 程序包。
- 如果缺少符合条件的 Connector 程序包，作业启动时会抛出`org.apache.flink.table.api.ValidationException: Could not find any factory`异常信息。
- 对于读写 Kafka 的场景，推荐使用不带版本号的 `flink-connector-kafka`程序包，并将 `connector.version`参数设置为 `universal`，以获得最新的功能适配。**不建议**选择 `flink-connector-kafka-0.11` 等带版本号的旧版程序包。

### 排除计算列
对于 INSERT INTO 的数据目的表，**计算列**是不考虑在内的。例如，某个 Sink 的定义如下，那么在 INSERT INTO MySink 后的 SELECT 语句，必须包含 a (VARCHAR) 和 b (BIGINT) 两个字段，且不允许加入 c 字段，因为 c 是虚拟的计算列。
```
CREATE TABLE MySink (
   a VARCHAR,
   b BIGINT,
   c AS PROCTIME()
) WITH ( ... ... );
```

### Tuple 和 Upsert 数据流的区别
确保 Sink Table 定义了合适的 WITH 参数。例如有些 Connector 只支持作为数据源，不支持作为数据目的；还有的只支持 Tuple 类型的数据流，不支持 Upsert 数据流等。
