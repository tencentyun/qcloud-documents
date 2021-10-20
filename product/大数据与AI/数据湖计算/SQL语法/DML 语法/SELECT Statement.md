`SELECT` 语句：从零个或多个表中检索数据行。

## 语法
```
[ WITH with_query [, ...] ]
SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition ]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]
[ LIMIT [ count | ALL ] ]
```

## 参数
####  [ WITH with_query [, ....] ]
可使用 WITH 来展平嵌套查询或简化子查询。`with_query` 语法如下：
```
subquery_table_name [ ( column_name [, ...] ) ] AS (subquery)
```
 - subquery\_table\_name 是临时表的唯一名称，该临时表用于定义 WITH 子句子查询的结果。每个 subquery 都必须具有一个可在 FROM 子句中引用的表名称。
 - column\_name \[, ...\] 是可选的输出列名称列表。列名称数目必须等于或小于 subquery 定义的列数。
 - subquery 是任意查询语句。
   
####  [ ALL | DISTINCT ] select_expr
ALL 和 DISTINCT 选项指定是否应返回重复的行。如果没有给出这些选项，则默认值为 ALL（返回所有匹配的行）。DISTINCT 指定从结果集中删除重复行。

####  FROM from_item [, ...]
from\_item 可以是视图、表、子查询，如果多表 join，支持的 join 类型如下：
 - `[ INNER ] JOIN`
 - `LEFT [ OUTER ] JOIN`
 - `RIGHT [ OUTER ] JOIN`
 - `FULL [ OUTER ] JOIN`
 - `CROSS JOIN`
 - `ON join_condition`，如果使用 `join_condition`，您可以为多个表中的联接键指定列名称；如果使用 `join_column`，则要求 join\_column 在两个表中都存在。

####  [ WHERE condition ]
根据您指定的 condition 筛选结果，返回满足条件的结果集。

####  [ GROUP BY [ ALL | DISTINCT ] grouping_expressions [, ...] ]
GROUP BY 表达式可以按照指定的列名对输出进行分组。

####  [HAVING condition ]
与聚合函数和 GROUP BY 子句一起使用。控制哪些组处于选中状态，从而消除不满足 condition 的组。此筛选在计算组和聚合之后发生。

####  [{UNION | INTERSECT | EXCEPT} [ALL | DISTINCT] union_query]
`UNION`、`INTERSECT` 和 `EXCEPT` 将多个结果组合在一起，`UNION` 将第一个查询生成的行与第二个查询生成的行组合在一起。为了消除重复，UNION 构建一个散列表，这会消耗内存。为了更好的性能，建议使用 UNION ALL。
- `INTERSECT` 仅返回第一个和第二个查询的结果中存在的行。
- `EXCEPT` 返回第一个查询结果中的行，不包括第二个查询找到的行。

####  [ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]
按一个或多个输出 expression 对结果集进行排序，当子句包含多个表达式时，将根据第一个 `expression` 对结果集进行排序。然后，第二个 `expression` 应用于具有第一个表达式中的匹配值的行，以此类推。


## 示例
### WITH Clause
WITH 子句定义在查询中使用的命名关系。它允许展平嵌套查询或简化子查询。例如，以下查询是等效的：
```
WITH x AS (SELECT a, MAX(b) AS b FROM t GROUP BY a)
SELECT a, b FROM x;
```
也可以跟多个子查询：
```
WITH
  t1 AS (SELECT a, MAX(b) AS b FROM x GROUP BY a),
  t2 AS (SELECT a, AVG(d) AS d FROM y GROUP BY a)
SELECT t1.*, t2.*
FROM t1
JOIN t2 ON t1.a = t2.a;
```

### GROUP BY Clause
GROUPBY 子句将 SELECT 语句的输出分成包含匹配值的行组。简单的 GROUPBY 子句可以包含由输入列组成的任何表达式，也可以是按位置选择输出列的序数：
```
SELECT count(*), nationkey FROM customer GROUP BY 2;
```
```
SELECT count(*), nationkey FROM customer GROUP BY nationkey;
```
```
SELECT count(*) FROM customer GROUP BY mktsegment;
```

### GROUPING SETS
分组集允许用户指定要分组的列的多个列表。不属于给定分组列子列表的列被设置为空。
```
SELECT origin_state, origin_zip, destination_state, sum(package_weight)
FROM shipping
GROUP BY GROUPING SETS (
    (origin_state),
    (origin_state, origin_zip),
    (destination_state));
```
```
SELECT origin_state, NULL, NULL, sum(package_weight)
FROM shipping GROUP BY origin_state
UNION ALL
SELECT origin_state, origin_zip, NULL, sum(package_weight)
FROM shipping GROUP BY origin_state, origin_zip
UNION ALL
SELECT NULL, NULL, destination_state, sum(package_weight)
FROM shipping GROUP BY destination_state;
```

### HAVING Clause
HAVING 子句与 aggregate 函数和 groupby 子句一起使用，以控制选择哪些组。HAVING 子句消除了不满足给定条件的组。
```
SELECT count(*), mktsegment, nationkey,
       CAST(sum(acctbal) AS bigint) AS totalbal
FROM customer
GROUP BY mktsegment, nationkey
HAVING sum(acctbal) > 5700000
ORDER BY totalbal DESC;
```

### IN
IN 操作符允许您在 WHERE 子句中规定多个值。
```
SELECT name
FROM nation
WHERE regionkey IN (SELECT regionkey FROM region)
```

### EXISTS
EXISTS 运算符用于判断查询子句是否有记录，如果有一条或多条记录存在返回 True，否则返回 False。

```
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition)
```

### USING
用 using 关键字进行简化。
- 查询必须是相等条件连接。
- 等值连接中的列必须具有相同的名称和数据类型。

```
SELECT *
FROM table_1
JOIN table_2
USING (key_A, key_B)
```

```
SELECT *
FROM (
    VALUES
        (1, 3, 10),
        (2, 4, 20)
) AS table_1 (key_A, key_B, y1)
LEFT JOIN (
    VALUES
        (1, 3, 100),
        (2, 4, 200)
) AS table_2 (key_A, key_B, y2)
USING (key_A, key_B);
```

### CROSS JOIN
交叉连接返回两个关系的笛卡尔积（所有组合）。

```
SELECT *
FROM nation
CROSS JOIN region
```

### LIMIT Clause
LIMIT 子句限制结果集中的行数。

```
SELECT orderdate FROM orders LIMIT 5
```

### ORDER BY Clause
ORDER BY 子句用于按一个或多个输出表达式对结果集进行排序。

```
语法：ORDER BY expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...]
```

```
SELECT name, age FROM person ORDER BY age
```

```
SELECT * FROM student
ORDER BY student_id
```

```
SELECT * FROM student
ORDER BY student_id,student_name
```

### EXCEPT
EXCEPT 子句/操作符用于合并两个 SELECT 语句，并从那些没有被第二个 SELECT 语句返回的第一个 SELECT 语句返回行。这意味着 EXCEPT 仅返回行，在第二个 SELECT 语句不可用。

正如使用 UNION 操作，同样的规则时，使用 EXCEPT 操作符适用。

```
SELECT * FROM (VALUES 13, 42)
EXCEPT
SELECT 13
```

### INTERSECT
从 SELECT 语句返回两个或多个结果集的不同行。

```
SELECT * FROM (VALUES 13, 42)
INTERSECT
SELECT 1
```

### UNION
将两个或多个 SELECT 语句的结果集合并到一个结果集中。要保留结果集中的重复行，请使用`UNION ALL`运算符。

```
SELECT 13
UNION
SELECT 42
```

```
SELECT id FROM a
UNION ALL
SELECT id FROM b;
```

### TABLESAMPLE
- `BERNOULLI`：选择每一行作为表样本，概率为样本百分比。使用 Bernoulli 方法对表进行采样时，将扫描表的所有物理块并跳过某些行（基于采样百分比与运行时计算的随机值之间的比较）。结果中包含一行的概率独立于任何其他行。这不会减少从磁盘读取采样表所需的时间。如果进一步处理采样输出，可能会影响总查询时间。
- `SYSTEM`：这种采样方法将表划分为逻辑数据段，并以此粒度对表进行采样。此采样方法要么从特定数据段中选择所有行，要么跳过它（基于采样百分比和运行时计算的随机值之间的比较）。在系统采样中选择的行将取决于所使用的连接器。例如，当与 Hive 一起使用时，它取决于数据在 HDFS 上的布局方式。这种方法不能保证独立的抽样概率。

```
SELECT *
FROM users TABLESAMPLE BERNOULLI (50);
```

```
SELECT *
FROM users TABLESAMPLE SYSTEM (75);
```

### 转义
要转义单引号，请在其前面加上另一个单引号，如以下示例所示：
```
Select 'dlc''test'
```
创建表的时候指定转义符或者逃逸符，例如使用下列方式创建：
```
CREATE EXTERNAL TABLE IF NOT EXISTS `csv_test_2222` (
      `_c0`  STRING,
      `_c1`  INTEGER,
      `_c2`  INTEGER,
      `_c3`  INTEGER
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
      'separatorChar' = '''',
      'quoteChar' = ''''
    )
    STORED AS `textfile`
    LOCATION 'cosn://dlc-nj-1258469122/csv/100M/
```
    
