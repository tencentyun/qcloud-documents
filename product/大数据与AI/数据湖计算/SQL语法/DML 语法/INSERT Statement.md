插入一条新行记录到一个表中。如果指定了列名列表，则它们必须与查询生成的列列表完全匹配。表中不在列列表中的每一列都将填充一个空值。如果未指定列列表，则查询生成的列必须与插入的表中的列完全匹配。

## 语法
- **Presto：**
```
INSERT INTO table_name [ ( column [, ... ] ) ] query
```
- **Spark：**
```
INSERT INTO table_identifier [ partition_spec ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query }
```

## 参数
- `[ partition_spec ]`：分区列和值。例如 dt='2021-06-01'。
- `[ ( column [, ... ] ) ]`：列的所有。
- `[table_name] | table_identifier`：表名。
- `[query]`：一个通用 Select 查询语句。

## 示例
Presto 和 Spark 通用插入示例：
```
INSERT INTO orders SELECT * FROM new_orders;
```
```
INSERT INTO cities VALUES (1, 'China');
```
```
INSERT INTO nation (nationkey, name, regionkey, comment)
VALUES (26, 'POLAND', 3, 'no comment');
```

**Spark 样例：**
插入分区使用一个 select 查询：
```
INSERT INTO students PARTITION (student_id = 444444) SELECT name, address FROM persons WHERE name = 'dlc'
```
插入分区：
```
INSERT INTO students PARTITION (student_id = 11215017) (address, name) VALUES  ('Shen zhen, China', 'tester')
```

## 限制
Presto 不支持插入分区的操作，如果需要插入分区的话可以采用 spark 引擎执行。
