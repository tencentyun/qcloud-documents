## 描述
ARRAY &lt;T> 是由 T 类型元素组成的数组，不能作为 key 列使用。目前支持在 Duplicate 模型的表中使用。

T 支持的类型有：
```
BOOLEAN, TINYINT, SMALLINT, INT, BIGINT, LARGEINT, FLOAT, DOUBLE, DECIMAL, DATE,
DATETIME, CHAR, VARCHAR, STRING
```
>! 使用前需要在 fe.conf 中添加 `enable_array_type=true` 配置项。

## 示例
建表示例如下：
```sql
mysql> CREATE TABLE `array_test` (
  `id` int(11) NULL COMMENT "",
  `c_array` ARRAY<int(11)> NULL COMMENT ""
) ENGINE=OLAP
DUPLICATE KEY(`id`)
COMMENT "OLAP"
DISTRIBUTED BY HASH(`id`) BUCKETS 1
PROPERTIES (
"replication_allocation" = "tag.location.default: 1",
"in_memory" = "false",
"storage_format" = "V2"
);
```
插入数据示例：
```sql
mysql> INSERT INTO `array_test` VALUES (1, [1,2,3,4,5]);
mysql> INSERT INTO `array_test` VALUES (2, array(6,7,8)), (3, array()), (4, null);
```
查询数据示例：
```sql
mysql> SELECT * FROM `array_test`;
+------+-----------------+
| id   | c_array         |
+------+-----------------+
|    1 | [1, 2, 3, 4, 5] |
|    2 | [6, 7, 8]       |
|    3 | []              |
|    4 | NULL            |
+------+-----------------+
```

