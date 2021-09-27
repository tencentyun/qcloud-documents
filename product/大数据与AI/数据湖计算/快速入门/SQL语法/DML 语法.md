## DELETE Statement
从指定表中删除行。如果指定了 where 子句，则只删除匹配的行。否则，将删除表中的所有行。

### 语法
```
DELETE FROM table_name [ WHERE condition ]
```
### 参数
- [table_name]：表名。
- [where condition]：可选 where 条件，用于条件删除，如果不加则整张表删除。

### 示例
```
DELETE FROM lineitem WHERE shipmode = 'AIR';
```
```
DELETE FROM lineitem WHERE orderkey IN (SELECT orderkey FROM orders WHERE priority = 'LOW');
```
```
DELETE FROM orders;
```

### 限制
Spark 不支持该操作，需要使用其它方式替换，例如，可参考 [Insert OverWrite](#jump1) 方式去覆写表。

## INSERT Statement
插入一条新行记录到一个表中。如果指定了列名列表，则它们必须与查询生成的列列表完全匹配。表中不在列列表中的每一列都将填充一个空值。如果未指定列列表，则查询生成的列必须与插入的表中的列完全匹配。

### 语法
- **Presto：**
```
INSERT INTO table_name [ ( column [, ... ] ) ] query
```
- **Spark：**
```
INSERT INTO table_identifier [ partition_spec ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query }
```

### 参数
- `[ partition_spec ]`：分区列和值。例如 dt='2021-06-01'。
- `[ ( column [, ... ] ) ]`：列的所有。
- `[table_name] | table_identifier`：表名。
- `[query]`：一个通用 Select 查询语句。

### 示例
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

### 限制
Presto 不支持插入分区的操作，如果需要插入分区的话可以采用 spark 引擎执行。

[](id:jump1)
## INSERT OVERWRITE Statement
INSERT OVERWRITE 语句使用新值覆盖表中的现有数据。插入的行可以由值表达式或查询结果指定。

### 语法
- **Spark 引擎：**
```
INSERT OVERWRITE [ TABLE ] table_identifier [ partition_spec [ IF NOT EXISTS ] ] [ ( column_list ) ]
    { VALUES ( { value | NULL } [ , ... ] ) [ , ( ... ) ] | query }
```
- **Presto 引擎：**不支持该语法

### 参数
- `[ TABLE ]`：关键字，可省略。
- `table_identifier`：表名。
- `partition_spec [ IF NOT EXISTS ]`：分区列表，例如`PARTITION \(dt='2021-05-14'\) IF NOT EXISTS`。

### 示例
插入分区表：
```
INSERT OVERWRITE students PARTITION 
(student_id = 11215016) IF NOT EXISTS 
(address, name) VALUES ('Hangzhou, China', 'Kent Yao Jr.')
```

### 限制
Presto 不支持 INSERT OVERWRITE 操作，如果需要覆写表和分区的话可以采用 spark 引擎执行。

## SELECT Statement
`SELECT` 语句：从零个或多个表中检索数据行。
### 语法
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

### 参数
- **[ WITH with_query [, ....] ]**：可使用 WITH 来展平嵌套查询或简化子查询。不支持使用 WITH 子句创建递归查询。WITH 子句在查询中位于 SELECT 列表之前，定义一个或多个子查询，以便在 SELECT 查询中使用。每个子查询均定义一个临时表，与可在 FROM 子句中引用的视图定义类似。只有在查询运行时才使用这些表。
 - `with_query` 语法为：
```
subquery_table_name [ ( column_name [, ...] ) ] AS (subquery)
```
其中：
   - subquery\_table\_name 是临时表的唯一名称，该临时表用于定义 WITH 子句子查询的结果。每个 subquery 都必须具有一个可在 FROM 子句中引用的表名称。
   - column\_name \[, ...\] 是可选的输出列名称列表。列名称数目必须等于或小于 subquery 定义的列数。
   - subquery 是任意查询语句。
- `[ ALL | DISTINCT ] select_expression`：`select_expression` 确定要选择的行。默认值为 `ALL`。使用 `ALL` 会被视为与省略它相同；将会选定所有列的所有行，并保留重复项。当列包含重复值时，请使用`DISTINCT`仅返回不同的值。
- `FROM from_item [, ...]`：指示要查询的输入，其中 from\_item 可以是视图、联接构造或如下所述的子查询。`from_item` 可以是：
```
table_name [ [ AS ] alias [ (column_alias [, ...]) ] ]
```
其中，`table_name`是要从中选择行的目标表的名称，`alias` 是要提供 SELECT 语句输出的名称，column\_alias 定义指定`alias`的列。

- JOIN
```
join_type from_item [ ON join_condition | USING ( join_column [, ...] ) ]
```
其中，join\_type 为以下值之一：
 - `[ INNER ] JOIN`
 - `LEFT [ OUTER ] JOIN`
 - `RIGHT [ OUTER ] JOIN`
 - `FULL [ OUTER ] JOIN`
 - `CROSS JOIN`
 - `ON join_condition`，如果使用 `join_condition`，您可以为多个表中的联接键指定列名称；如果使用 `join_column`，则要求 join\_column 在两个表中都存在。
 - `[ WHERE condition ]`，根据您指定的 condition 筛选结果，返回满足条件的结果集。
- **\[ GROUP BY \[ ALL \| DISTINCT \] grouping\_expressions \[, ...\] \]**：将 SELECT 语句的输出分成多个具有匹配值的行。
 - ALL 和 DISTINCT 确定重复的分组集是否各自产生不同的输出行。如果省略，则会采用 ALL。
 - grouping\_expressions 允许您执行复杂的分组操作。grouping\_expressions 元素可以是对输入列执行的任何函数（如 SUM、AVG 或 COUNT 等），或是一个按位置选择输出列的序号（从1开始）。
GROUP BY 表达式可以按照不在 SELECT 语句的输出中显示的输入列名称对输出进行分组。所有输出表达式都必须是存在于 GROUP BY 子句中的聚合函数或列。您可以使用单个查询来执行需要聚合多个列集的分析。这些复杂的分组操作不支持包含输入列的表达式。只允许使用列名或序号。
通常，您可以使用 UNION ALL 实现和这些 GROUP BY 操作相同的结果，但使用 GROUP BY 的查询具有一次读取数据的优点，而 UNION ALL 三次读取底层数据，因此可能会在数据源发生变化时造成不一致的结果。
 - `GROUP BY CUBE` 为给定的列集生成所有可能的分组集。
 - `GROUP BY ROLLUP` 为给定的列集生成所有可能的小计。
- **[ HAVING condition ]**：与聚合函数和 GROUP BY 子句一起使用。控制哪些组处于选中状态，从而消除不满足 condition 的组。此筛选在计算组和聚合之后发生。
- **[{UNION | INTERSECT | EXCEPT} [ALL | DISTINCT] union_query\]]]**：`UNION`、`INTERSECT`和`EXCEPT`将多个结果组合在一起`SELECT`语句转换到单个查询中。`ALL`或者`DISTINCT`控制包含在最终结果集中的行的唯一性。`UNION`将第一个查询生成的行与第二个查询生成的行组合在一起。为了消除重复，UNION 构建一个散列表，这会消耗内存。为了更好的性能，可考虑使用 UNION ALL，如果您的查询不需要消除重复项。将会按从左到右的顺序处理多个 UNION 子句，除非您使用圆括号显式定义处理顺序。
`INTERSECT`仅返回第一个和第二个查询的结果中存在的行。
`EXCEPT`返回第一个查询结果中的行，不包括第二个查询找到的行。
`ALL` 会导致包含所有行，即使这些行是相同的。
`DISTINCT`只导致唯一行包含在组合结果集中。
- **[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]**：按一个或多个输出 expression 对结果集进行排序。当子句包含多个表达式时，将根据第一个`expression`对结果集进行排序。然后，第二个`expression`应用于具有第一个表达式中的匹配值的行，以此类推。每个 `expression` 可以指定 `SELECT` 中的输出列或按位置指定输出列的序号（从1开始）。在任何`GROUP BY`或 `HAVING` 子句之后，作为最后一个步骤，会计算 ORDER BY。`ASC` 和 `DESC` 确定是 按升序还是按降序对结果进行排序。默认 `NULL` 排序是 `NULLS LAST`，无论是按升序还是按降序排序。

- TABLESAMPLE BERNOULLI \| SYSTEM \(percentage\)：可选运算符，用于根据采样方法从表中选择行。`BERNOULLI` 选择每个位于表样本中的行，概率为 percentage。将会扫描表的所有物理块，并根据样本 percentage 和在运行时计算的随机值之间的比较来跳过某些行。借助 `SYSTEM`，表被划分成数据的逻辑段，而且表按此粒度采样。 将会选择特定段中的所有行，或者根据样本 percentage 和在运行时计算的随机值之间的比较来跳过该段。
- `SYSTEM` 采样取决于连接器。此方法不保证独立采样概率。

### 示例
**WITH Clause**
功能：WITH 子句定义在查询中使用的命名关系。它允许展平嵌套查询或简化子查询。例如，以下查询是等效的：
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
**GROUP BY Clause**
功能：GROUPBY 子句将 SELECT 语句的输出分成包含匹配值的行组。简单的 GROUPBY 子句可以包含由输入列组成的任何表达式，也可以是按位置选择输出列的序数：
```
SELECT count(*), nationkey FROM customer GROUP BY 2;
```
```
SELECT count(*), nationkey FROM customer GROUP BY nationkey;
```
```
SELECT count(*) FROM customer GROUP BY mktsegment;
```

**GROUPING SETS**
功能：分组集允许用户指定要分组的列的多个列表。不属于给定分组列子列表的列被设置为空。

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

**HAVING Clause**
功能：HAVING 子句与 aggregate 函数和 groupby 子句一起使用，以控制选择哪些组。HAVING 子句消除了不满足给定条件的组。
```
SELECT count(*), mktsegment, nationkey,
       CAST(sum(acctbal) AS bigint) AS totalbal
FROM customer
GROUP BY mktsegment, nationkey
HAVING sum(acctbal) > 5700000
ORDER BY totalbal DESC;
```

**IN**

功能：IN 操作符允许您在 WHERE 子句中规定多个值。

```
SELECT name
FROM nation
WHERE regionkey IN (SELECT regionkey FROM region)
```

**EXISTS**

功能：EXISTS 运算符用于判断查询子句是否有记录，如果有一条或多条记录存在返回 True，否则返回 False。

```
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition)
```

**USING**
功能：用 using 关键字进行简化。
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

**CROSS JOIN**

功能：交叉连接返回两个关系的笛卡尔积（所有组合）。

```
SELECT *
FROM nation
CROSS JOIN region
```

**LIMIT Clause**

功能：LIMIT 子句限制结果集中的行数。

```
SELECT orderdate FROM orders LIMIT 5
```

**ORDER BY Clause**

功能：ORDER BY 子句用于按一个或多个输出表达式对结果集进行排序。

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

**EXCEPT**

功能：EXCEPT 子句/操作符用于合并两个 SELECT 语句，并从那些没有被第二个 SELECT 语句返回的第一个 SELECT 语句返回行。这意味着 EXCEPT 仅返回行，在第二个 SELECT 语句不可用。

正如使用 UNION 操作，同样的规则时，使用 EXCEPT 操作符适用。

```
SELECT * FROM (VALUES 13, 42)
EXCEPT
SELECT 13
```

**INTERSECT**

功能：从 SELECT 语句返回两个或多个结果集的不同行。

```
SELECT * FROM (VALUES 13, 42)
INTERSECT
SELECT 1
```

**UNION**

将两个或多个 SELECT 语句的结果集合并到一个结果集中。

要保留结果集中的重复行，请使用`UNION ALL`运算符。

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

**TABLESAMPLE**
功能：
`BERNOULLI`

选择每一行作为表样本，概率为样本百分比。使用 Bernoulli 方法对表进行采样时，将扫描表的所有物理块并跳过某些行（基于采样百分比与运行时计算的随机值之间的比较）。

结果中包含一行的概率独立于任何其他行。这不会减少从磁盘读取采样表所需的时间。如果进一步处理采样输出，可能会影响总查询时间。

`SYSTEM`
这种采样方法将表划分为逻辑数据段，并以此粒度对表进行采样。此采样方法要么从特定数据段中选择所有行，要么跳过它（基于采样百分比和运行时计算的随机值之间的比较）。

在系统采样中选择的行将取决于所使用的连接器。例如，当与 Hive 一起使用时，它取决于数据在 HDFS 上的布局方式。这种方法不能保证独立的抽样概率。

```
SELECT *
FROM users TABLESAMPLE BERNOULLI (50);
```

```
SELECT *
FROM users TABLESAMPLE SYSTEM (75);
```

**转义**

要转义单引号，请在其前面加上另一个单引号，如以下示例所示：

```
Select 'dlc''test'
```

创建表的时候指定转义符或者逃逸符，比如使用下列方式创建：

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

## SELECT Statement - Spark

`SELECT` 语句：从零个或多个表中检索数据行。

### 语法

```
[ WITH with_query [ , ... ] ]
select_statement [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select_statement, ... ]
    [ ORDER BY { expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ] } ]
    [ DISTRIBUTE BY { expression [, ... ] } ]
    [ LIMIT { ALL | expression } ]
```

`select_statement` 包含下列查询：

```
SELECT [ ALL | DISTINCT ] { [ [ named_expression | regex_column_names ] [ , ... ] | TRANSFORM (...) ] }
    FROM { from_item [ , ... ] }
    [ WHERE boolean_expression ]
    [ GROUP BY expression [ , ... ] ]
    [ HAVING boolean_expression ]
```
### 参数
大部分语句的解释可以参考 Select Statement 中。

特殊子句比如像：

`[ DISTRIBUTE BY { expression [, ... ] } ]`

指定一组表达式，通过这些表达式对结果行进行重新分区。

### 示例
Spark distribute by 语句：

```
select * from test_table distribute by f1
```
