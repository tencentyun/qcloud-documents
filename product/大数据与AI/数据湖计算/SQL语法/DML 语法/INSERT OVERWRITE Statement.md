INSERT OVERWRITE 语句使用新值覆盖表中的现有数据。插入的行可以由值表达式或查询结果指定。

## 语法
- **Spark 引擎：**
```
INSERT OVERWRITE [ TABLE ] table_identifier [ partition_spec [ IF NOT EXISTS ] ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query }
```
- **Presto 引擎：**不支持该语法

## 参数
- `[ TABLE ]`：关键字，可省略。
- `table_identifier`：表名。
- `partition_spec [ IF NOT EXISTS ]`：分区列表，例如`PARTITION \(dt='2021-05-14'\) IF NOT EXISTS`。

## 示例
插入分区表：
```
INSERT OVERWRITE students PARTITION 
(student_id = 11215016) IF NOT EXISTS 
(address, name) VALUES ('Hangzhou, China', 'Kent Yao Jr.')
```

## 限制
Presto 不支持 INSERT OVERWRITE 操作，如果需要覆写表和分区的话可以采用 spark 引擎执行。
