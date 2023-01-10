## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：行级数据插入操作。

>? Presto 仅支持在 Hive 数据源的分区表上执行 insert overwrite，非分区表以及 Iceberg 数据源的表暂时不支持这个用法。

## 语法
```
INSERT OVERWRITE table_identifier [ partition_spec ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query 
```


## 参数
- `table_identifier`：指定表名，支持三段式，例如：catalog.database.table
- `partition_spec`：分区列和值。例如 dt='2021-06-01'。
- `column_list`：列的所有。
- `query`：一个通用 Select 查询语句。
	1. a SELECT statement
	2. a TABLE statement

## 示例
```
-- Insert Using a VALUES Clause
INSERT OVERWRITE students VALUES
    ('Ashua Hill', '456 Erica Ct, Cupertino', 111111),
    ('Brian Reed', '723 Kern Ave, Palo Alto', 222222);

-- Insert Using a SELECT Statement
INSERT OVERWRITE students PARTITION (student_id = 222222)
    SELECT name, address FROM persons WHERE name = "Dora Williams"

-- Insert Using a TABLE Statement
INSERT OVERWRITE students TABLE visiting_students

-- Insert with a column list
INSERT OVERWRITE students (address, name, student_id) VALUES
    ('Hangzhou, China', 'Kent Yao', 11215016)

-- Insert with both a partition spec and a column list
INSERT OVERWRITE students PARTITION (student_id = 11215016) (address, name) VALUES
    ('Hangzhou, China', 'Kent Yao Jr.')
```


