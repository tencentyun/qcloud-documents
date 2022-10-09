## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：支持将在源表上运行的 SELECT 查询结果作为新行插入到目标表中。

## 语法
```
[ WITH with_query [ , ... ] ]
INSERT {INTO [<TABLE>]| TABLE} table_identifier [ partition_spec ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query }
```

## 参数
- `table_identifier`：指定表名，支持三段式，例如：`catalog.database.table`。
- `partition_spec`：分区列和值。例如 dt='2021-06-01'。
- `column_list`：列的所有。
- `query`：一个通用 Select 查询语句。      
	1. `a SELECT statement`     
	2. `a TABLE statement`

## 示例
```
INSERT INTO orders SELECT * FROM new_orders;
INSERT INTO cities VALUES (1, 'China');
INSERT INTO nation (nationkey, name, regionkey, comment)
VALUES (26, 'POLAND', 3, 'no comment');

-- INSERT INTO partition
INSERT INTO students PARTITION (student_id = 444444) SELECT name, address FROM persons WHERE name = 'dlc'
INSERT INTO students PARTITION (student_id = 11215017) (address, name) VALUES  ('Shen zhen, China', 'tester')

-- Insert Using a TABLE Statement
INSERT INTO students TABLE visiting_students;

-- with
WITH `tmp1` AS ((SELECT *
FROM `catalog1`.`db1`.`tbl1`)), `tmp2` AS ((SELECT *
FROM `tbl2`))
INSERT INTO `catalog1`.`db2`.`tbl1`
(SELECT `col1`, `col2`
FROM `tmp1` `a`
INNER JOIN `tmp2` `b` ON `a`.`col1` = `b`.`col2`)


INSERT INTO `catalog1`.`db2`.`tbl1`
WITH `tmp1` AS ((SELECT *
FROM `catalog1`.`db1`.`tbl1`)), `tmp2` AS ((SELECT *
FROM `tbl2`))
(SELECT `col1`, `col2`
FROM `tmp1` `a`
INNER JOIN `tmp2` `b` ON `a`.`col1` = `b`.`col2`)
```



