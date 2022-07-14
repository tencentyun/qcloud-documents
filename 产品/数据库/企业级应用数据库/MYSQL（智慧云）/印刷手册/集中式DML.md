## DELETE语法
DELETE 是从表中删除行的 DML 语句。
DELETE 语句可以以 WITH 子句开头，以定义可在 DELETE 中访问的公共表表达式
### **单表语法**
```
DELETE  [QUICK] [IGNORE] FROM tbl_name [[AS] tbl_alias]
    	[PARTITION (partition_name [, partition_name] ...)]
    	[WHERE where_condition]
    	[ORDER BY ...]
    	[LIMIT row_count]
```
DELETE 语句从 tbl_name 中删除行并返回删除的行数。 要检查已删除的行数，请调用 ROW_COUNT() 函数 
### 主要条款
可选 WHERE 子句中的条件标识要删除的行。 如果没有 WHERE 子句，则删除所有行。
where_condition 是一个表达式，对于要删除的每一行，它的计算结果为真。 
如果指定了 ORDER BY 子句，则按指定的顺序删除行。 LIMIT 子句限制了可以删除的行数。 这些子句适用于单表删除，但不适用于多表删除。
### 多表语法
```
DELETE [QUICK] [IGNORE]
    tbl_name[.*] [, tbl_name[.*]] ...
    FROM table_references
    [WHERE where_condition]

DELETE [QUICK] [IGNORE]
    FROM tbl_name[.*] [, tbl_name[.*]] ...
    USING table_references
    [WHERE where_condition]
```
### 权限
您需要对表具有 DELETE 权限才能从中删除行。 对于任何只读的列，您只需要 SELECT 特权，例如在 WHERE 子句中命名的列。
### 性能
当您不需要知道删除的行数时，TRUNCATE TABLE 语句是一种比不带 WHERE 子句的 DELETE 语句更快的清空表的方法。 与 DELETE 不同，TRUNCATE TABLE 不能在事务中使用，也不能在表上有锁的情况下使用。 
为确保给定的 DELETE 语句不会花费太多时间，DELETE 的LIMIT row_count 子句指定要删除的最大行数。 如果要删除的行数大于限制，则重复 DELETE 语句，直到受影响的行数小于 LIMIT 值。
### 分区表支持
DELETE 支持使用 PARTITION 子句进行显式分区选择，该子句采用一个或多个分区或子分区（或两者）的逗号分隔名称列表，从中选择要删除的行。 未包含在列表中的分区将被忽略。 给定一个分区表 t，其分区名为 p0，执行 DELETE FROM t PARTITION (p0) 语句对表具有与执行 ALTER TABLE t TRUNCATE PARTITION (p0) 相同的效果； 在这两种情况下，分区 p0 中的所有行都将被删除。
测试。 例如， DELETE FROM t PARTITION (p0) WHERE c < 5 仅从分区 p0 中删除条件 c < 5 为真的行； 不会检查任何其他分区中的行，因此不会受到 DELETE 的影响。
PARTITION 子句也可用于多表 DELETE 语句。 对于在 FROM 选项中命名的每个表，您最多可以使用一个这样的选项。
### 修饰符
该 DELETE 语句支持以下修饰符：
- IGNORE 修饰符使 MySQL 在删除行的过程中忽略可忽略的错误。 （在解析阶段遇到的错误以通常的方式处理。）由于使用 IGNORE 而被忽略的错误将作为警告返回。
删除顺序
如果 DELETE 语句包含 ORDER BY 子句，则按该子句指定的顺序删除行。 这主要与 LIMIT 结合使用。 例如，以下语句查找与 WHERE 子句匹配的行，按时间戳列对它们进行排序，然后删除第一个（最旧的）行：
```
DELETE FROM somelog WHERE user = 'jcole' ORDER BY timestamp_column LIMIT 1;
```

### InnoDB表
如果要从大表中删除许多行，则可能会超出 InnoDB 表的锁表大小。 为了避免这个问题，或者只是为了尽量减少表保持锁定的时间，以下策略（根本不使用 DELETE）可能会有所帮助：
1. 选择不删除的行放入与原表结构相同的空表中：
INSERT INTO t_copy SELECT * FROM t WHERE ...;
2. 使用 RENAME TABLE 以原子方式将原始表移开，并将副本重命名为原始名称：
RENAME TABLE t TO t_old，t_copy TO t;
3. 删除原始表：
DROP TABLE t_old;
在 RENAME TABLE 执行时，没有其他会话可以访问所涉及的表，因此重命名操作不受并发问题的影响。 

### 多表删除
您可以在 DELETE 语句中指定多个表以根据 WHERE 子句中的条件从一个或多个表中删除行。 您不能在多表 DELETE 中使用 ORDER BY 或 LIMIT。 
对于第一个多表语法，仅删除 FROM 子句之前列出的表中的匹配行。 对于第二种多表语法，仅删除 FROM 子句中（在 USING 子句之前）列出的表中的匹配行。 效果是您可以同时从多个表中删除行，并拥有仅用于搜索的附加表：
```
DELETE t1, t2 FROM t1 INNER JOIN t2 INNER JOIN t3
WHERE t1.id=t2.id AND t2.id=t3.id;
```
要么：
```
DELETE FROM t1, t2 USING t1 INNER JOIN t2 INNER JOIN t3
WHERE t1.id=t2.id AND t2.id=t3.id;
```
这些语句在搜索要删除的行时使用所有三个表，但仅从表 t1 和 t2 中删除匹配的行。
前面的示例使用 INNER JOIN，但多表 DELETE 语句可以使用 SELECT 语句中允许的其他类型的连接，例如 LEFT JOIN。 例如，要删除 t1 中存在但在 t2 中没有匹配项的行，请使用 LEFT JOIN：
```
DELETE t1 FROM t1 LEFT JOIN t2 ON t1.id=t2.id WHERE t2.id IS NULL;
```
如果您使用 DELETE 涉及 InnoDB 具有外键约束 的表的多表 语句 ，则TDSQL优化器可能会按照与其父/子关系不同的顺序处理表。 在这种情况下，语句失败并回滚。 相反，您应该从单个表中删除并依赖于 提供 的 ON DELETE 功能， InnoDB 以便相应地修改其他表。
>!如果声明表的别名，则在引用表时必须使用别名：`DELETE t1 FROM test AS t1, test2 WHERE ...`多表 DELETE 中的表别名应仅在语句的 table_references 部分中声明。 在其他地方，允许使用别名引用，但不允许使用别名声明。

正确：
```
DELETE a1, a2 FROM t1 AS a1 INNER JOIN t2 AS a2
WHERE a1.id=a2.id;

DELETE FROM a1, a2 USING t1 AS a1 INNER JOIN t2 AS a2
WHERE a1.id=a2.id;
```
不正确：
```
DELETE t1 AS a1, t2 AS a2 FROM t1 INNER JOIN t2
WHERE a1.id=a2.id;

DELETE FROM t1 AS a1, t2 AS a2 USING t1 INNER JOIN t2
WHERE a1.id=a2.id; 
```
## INSERT语法
语法如下：
```
INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...
      |
      VALUES row_constructor_list
    }
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {SELECT ... | TABLE table_name}
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

row_constructor_list:
    ROW(value_list)[, ROW(value_list)][, ...]

assignment:
    col_name = [row_alias.]value

assignment_list:
    assignment [, assignment] ...
```
>!一般情况下，由于子查询效率不高，尽量使用join的代替子查询

示例：
```
DROP TABLE if exists `test_shard_table1`;
CREATE TABLE `test_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_shard_table1 (id, b, c) VALUES 
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE if exists `test_shard_table2`;
CREATE TABLE `test_shard_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT  CHARSET=utf8  COLLATE=utf8_bin shardkey=id;
INSERT INTO test_shard_table2 (id, d, c) VALUES
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
(7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

SELECT COUNT(B)
FROM test_shard_table1
WHERE id IN
(SELECT c FROM test_shard_table2 WHERE id>5);

SELECT MAX(c), MIN(c)
FROM test_shard_table1 WHERE c IN
(SELECT c FROM test_shard_table2 WHERE id<8)
AND id>4 ORDER BY c;
```

## INSERT
语法如下：
```
INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...
      |
      VALUES row_constructor_list
    }
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {SELECT ... | TABLE table_name}
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

row_constructor_list:
    ROW(value_list)[, ROW(value_list)][, ...]

assignment:
    col_name = [row_alias.]value

assignment_list:
    assignment [, assignment] ...
```
INSERT 将新行插入到现有表中。语句的 INSERT ... VALUES、INSERT ... VALUES ROW() 和 INSERT ... SET 形式根据显式指定的值插入行。 INSERT ... SELECT 表单插入从另一个表或多个表中选择的行。您还可以在使用 INSERT ... TABLE 从单个表中插入行。如果要插入的行会导致 UNIQUE 索引或 PRIMARY KEY 中的重复值，则带有 ON DUPLICATE KEY UPDATE 子句的 INSERT 可以更新现有行。
插入表需要对该表具有 INSERT 权限。如果使用 ON DUPLICATE KEY UPDATE 子句并且重复键导致执行 UPDATE，则该语句需要对要更新的列具有 UPDATE 特权。对于已读取但未修改的列，您只需要 SELECT 特权（例如，对于仅在 ON DUPLICATE KEY UPDATE 子句中 col_name=expr 赋值的右侧引用的列）。
插入分区表时，您可以控制哪些分区和子分区接受新行。 PARTITION 子句采用表的一个或多个分区或子分区（或两者）的逗号分隔名称列表。如果要由给定 INSERT 语句插入的任何行与列出的分区之一不匹配，则 INSERT 语句将失败并显示错误发现行与给定分区集不匹配。
tbl_name 是应插入行的表。 指定语句为其提供值的列，如下所示：
- 在表名后面提供一个用括号括起来的以逗号分隔的列名列表。 在这种情况下，每个命名列的值必须由 VALUES 列表、VALUES ROW() 列表或 SELECT 语句提供。 对于 INSERT TABLE 形式，源表中的列数必须与要插入的列数相匹配。
- 如果您没有为 INSERT ... VALUES 或 INSERT ... SELECT 指定列名列表，则表中每一列的值必须由 VALUES 列表、SELECT 语句或 TABLE 语句提供。 如果您不知道表中列的顺序，请使用 DESCRIBE tbl_name 查找。
- SET 子句通过名称显式指示列，以及分配给每个列的值。
- 列值可以通过多种方式给出：
- 如果未启用严格 SQL 模式，则任何未显式指定值的列都将设置为其默认（显式或隐式）值。 例如，如果您指定的列列表未命名表中的所有列，则未命名的列将设置为其默认值。 
- 如果启用了严格 SQL 模式，并且 INSERT 语句没有为每个没有默认值的列指定显式值，则会生成错误。 
- 如果列列表和 VALUES 列表都为空，则 INSERT 将创建一行，其中每一列都设置为其默认值：
```
INSERT INTO tbl_name () VALUES();
```

如果未启用严格模式，TDSQL对任何没有明确定义默认值的列使用隐式默认值。 如果启用了严格模式，如果任何列没有默认值，则会发生错误。
- 使用关键字 DEFAULT 将列显式设置为其默认值。 这使得编写将值分配给除少数列之外的所有列的 INSERT 语句变得更容易，因为它使您能够避免编写不包括表中每一列的值的不完整 VALUES 列表。 否则，您必须提供与 VALUES 列表中的每个值对应的列名称列表。
- 如果显式插入生成的列，则唯一允许的值是 DEFAULT。
- 在表达式中，您可以使用 DEFAULT(col_name) 为列 col_name 生成默认值。
- 如果表达式数据类型与列数据类型不匹配，则可能会发生提供列值的表达式 expr 的类型转换。 根据列类型，给定值的转换可能会导致不同的插入值。 例如，将字符串 '1999.0e-2' 插入 INT、FLOAT、DECIMAL(10,6) 或 YEAR 列会分别插入值 1999、19.9921、19.992100 或 1999。 INT 和 YEAR 列中存储的值是 1999，因为字符串到数字的转换只查看字符串的初始部分，因为它可能被视为有效的整数或年份。 对于 FLOAT 和 DECIMAL 列，字符串到数字的转换将整个字符串视为有效的数值。
- 表达式 expr 可以引用先前在值列表中设置的任何列。 例如，您可以这样做，因为 col2 的值引用了之前已分配的 col1：
```
INSERT INTO tbl_name (col1,col2) VALUES(15,col1*2);
```

但是以下是不合法的，因为 col1 的值指的是 col2，它是在 col1 之后赋值的：
```
INSERT INTO tbl_name (col1,col2) VALUES(col2*2,15);
```
使用 VALUES 语法的 INSERT 语句可以插入多行。 为此，请包含多个以逗号分隔的列值列表，将列表括在括号内并用逗号分隔。 例子：
```
INSERT INTO tbl_name (a,b,c)  VALUES(1,2,3), (4,5,6), (7,8,9);
```
每个值列表必须包含与每行插入的值一样多的值。 以下语句无效，因为它包含一个包含九个值的列表，而不是三个包含三个值的列表：
```
INSERT INTO tbl_name (a,b,c) VALUES(1,2,3,4,5,6,7,8,9);
```
- 如果使用 IGNORE 修饰符，则执行 INSERT 语句时发生的可忽略错误将被忽略。 例如，如果没有 IGNORE，复制表中现有 UNIQUE 索引或 PRIMARY KEY 值的行会导致重复键错误并且语句被中止。 使用 IGNORE，该行被丢弃并且不会发生错误。 忽略的错误会生成警告。IGNORE 对插入到分区表中的插入有类似的影响，其中找不到与给定值匹配的分   区。如果没有 IGNORE，这    样的 INSERT 语句会因错误而中止。使用 INSERT IGNORE 时，对于包含不匹配值的行，插入操作会以静默方式 失败，但会插入匹配的行。如果未指定 IGNORE，则会触发错误的数据转换会中止语句。使用 IGNORE，将无效值调整为最接近的值并插    入；产生警告但语句不会中止。您可以使用 REPLACE 而不是 INSERT 来覆盖旧行。在处理包含重复旧行的唯一键值的新行时，REPLACE 是     INSERT IGNORE 的对应物：新行替换旧行而不是被丢弃。
- 如果您指定 ON DUPLICATE KEY UPDATE，并且插入的行会导致 UNIQUE 索引或 PRIMARY KEY 中出现重复值，则会发生旧行的 UPDATE。 如果将行作为新行插入，则每行的受影响行值为 1，如果更新现有行，则为 2，如果现有行设置为其当前值，则为 0。 如果在连接到 mysqld 时为 mysql_real_connect() C API 函数指定 CLIENT_FOUND_ROWS 标志，则如果现有行设置为其当前值，则受影响的行值为 1（而不是 0）。 

### INSERT ... SELECT语法
```
INSERT [IGNORE]
    	[INTO] tbl_name
    	[PARTITION (partition_name [, partition_name] ...)]
    	[(col_name [, col_name] ...)]
    	{SELECT ... | TABLE table_name}
    	[ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```
使用 INSERT ... SELECT，您可以从 SELECT 语句的结果中快速将多行插入到一个表中，该语句可以从一个或多个表中进行选择。 例如：
```
INSERT INTO tbl_temp2 (fld_id)
SELECT tbl_temp1.fld_order_id
FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```
以下条件适用于 INSERT ... SELECT 语句，除非另有说明，否则也适用于 INSERT ... TABLE：
- 指定 IGNORE 以忽略会导致重复键违规的行。
- INSERT 语句的目标表可能出现在查询的 SELECT 部分的 FROM 子句中，或者作为由 TABLE 命名的表。 但是，您不能在子查询中插入表并从同一个表中进行选择。当从同一个表中选择和插入时，TDSQL创建一个内部临时表来保存来自 SELECT 的行，然后将这些行插入到目标表中。 但是，当 t 是 TEMPORARY 表时，不能使用 INSERT INTO t ... SELECT ... FROM t，因为在同一语句中不能两次引用 TEMPORARY 表。 出于同样的原因，当 t 是临时表时，您不能使用 INSERT INTO t ... TABLE t。 
- AUTO_INCREMENT 列照常工作。
- 为确保二进制日志可用于重新创建原始表，TDSQL不允许 INSERT ... SELECT 或 INSERT ... TABLE 语句的并发插入。
- 为避免 SELECT 和 INSERT 引用同一个表时出现歧义的列引用问题，请为 SELECT 部分中使用的每个表提供唯一的别名，并使用适当的别名限定该部分中的列名。 

## REPLACE语法
语法如下：
```
REPLACE
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...
      |
      VALUES row_constructor_list
    }

REPLACE 
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list

REPLACE
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {SELECT ... | TABLE table_name}

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

row_constructor_list:
    ROW(value_list)[, ROW(value_list)][, ...]

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```
REPLACE 的工作方式与 INSERT 完全相同，但如果表中的旧行与 PRIMARY KEY 或 UNIQUE 索引的新行具有相同的值，则在插入新行之前删除旧行。  
>! 仅当表具有 PRIMARY KEY 或 UNIQUE 索引时，REPLACE 才有意义。 否则，它就等同于 INSERT，因为没有索引可用于确定新行是否与另一行重复。


所有列的值均取自 REPLACE 语句中指定的值。任何缺失的列都设置为其默认值，就像 INSERT 一样。您不能引用当前行中的值并在新行中使用它们。如果您使用诸如 SET col_name = col_name + 1 之类的赋值，则对右侧列名的引用将被视为 DEFAULT(col_name)，因此该赋值等效于 SET col_name = DEFAULT(col_name) + 1。
要使用 REPLACE，您必须同时拥有表的 INSERT 和 DELETE 权限。
如果显式替换生成的列，则唯一允许的值是 DEFAULT。
REPLACE 支持使用 PARTITION 子句的显式分区选择，其中包含以逗号分隔的分区、子分区或两者的名称列表。与 INSERT 一样，如果无法将新行插入到这些分区或子分区中的任何一个中，则 REPLACE 语句将失败并显示错误“找到与给定分区集不匹配的行”。 
REPLACE 语句返回一个计数以指示受影响的行数。这是删除和插入的行的总和。如果单行 REPLACE 的计数为 1，则插入了一行并且没有删除任何行。如果计数大于 1，则在插入新行之前删除了一个或多个旧行。如果表包含多个唯一索引并且新行重复不同唯一索引中不同旧行的值，则单行可以替换多个旧行。
受影响的行数可以很容易地确定 REPLACE 是只添加了一行还是还替换了任何行：检查计数是 1（添加）还是更大（替换）。
您不能在子查询中替换到一个表并从同一个表中进行选择。
TDSQL使用以下算法进行 REPLACE（和 LOAD DATA ... REPLACE）：
1. 尝试将新行插入表中
2. 由于主键或唯一索引发生重复键错误而导致插入失败：
a. 从表中删除具有重复键值的冲突行
b. 再次尝试将新行插入表中

考虑由以下 CREATE  TABLE 语句创建的表：
```
DROP TABLE IF EXISTS test;
CREATE TABLE test (
 	 id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  	data VARCHAR(64) DEFAULT NULL,
  	ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```
当我们创建这个表并运行TDSQL客户端显示的语句时，结果如下：
```
mysql> REPLACE INTO test VALUES (1, 'Old', '2014-08-20 18:47:00');
Query OK, 1 row affected (0.04 sec)

mysql> REPLACE INTO test VALUES (1, 'New', '2014-08-20 18:47:42');
Query OK, 2 rows affected (0.04 sec)

mysql> SELECT * FROM test;
+----+------+---------------------+
| id | data | ts                  |
+----+------+---------------------+
|  1 | New  | 2014-08-20 18:47:42 |
+----+------+---------------------+
1 row in set (0.00 sec)
```
现在我们创建第二个表与第一个几乎相同，除了主键现在覆盖 2 列，如下所示（强调文本）：
```
DROP TABLE IF EXISTS test2;
CREATE TABLE test2 (
 	 id INT UNSIGNED NOT NULL AUTO_INCREMENT,
 	 data VARCHAR(64) DEFAULT NULL,
  	ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id, ts)
);
```
当我们在 test2 上运行与在原始测试表上相同的两个 REPLACE 语句时，我们得到了不同的结果：

```
mysql> REPLACE INTO test2 VALUES (1, 'Old', '2014-08-20 18:47:00');
Query OK, 1 row affected (0.05 sec)

mysql> REPLACE INTO test2 VALUES (1, 'New', '2014-08-20 18:47:42');
Query OK, 1 row affected (0.06 sec)

mysql> SELECT * FROM test2;
+----+------+---------------------+
| id | data | ts                  |
+----+------+---------------------+
|  1 | Old  | 2014-08-20 18:47:00 |
|  1 | New  | 2014-08-20 18:47:42 |
+----+------+---------------------+
2 rows in set (0.00 sec)
```
这是因为在 test2 上运行时，id 和 ts 列值必须与要替换的行的现有行的值匹配； 否则，插入一行。
## SELECT语法
语法如下：
```
SELECT
    	[ALL | DISTINCT | DISTINCTROW ]
   	 [HIGH_PRIORITY]
   	 [STRAIGHT_JOIN]
    [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
    [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr] ...
    [into_option]
    [FROM table_references
      [PARTITION partition_list]]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]
    [WINDOW window_name AS (window_spec)
        [, window_name AS (window_spec)] ...]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [into_option]
    [FOR {UPDATE | SHARE}
        [OF tbl_name [, tbl_name] ...]
        [NOWAIT | SKIP LOCKED]
      | LOCK IN SHARE MODE]
```
SELECT 语句最常用的子句如下：
- 每个 select_expr 表示您要检索的列。 必须至少有一个 select_expr。
- table_references 指示要从中检索行的一个或多个表。 
- SELECT 支持使用 PARTITION 子句的显式分区选择，其中包含 table_reference 中表名称后的分区或子分区（或两者）列表。 在这种情况下，仅从列出的分区中选择行，而忽略表的任何其他分区。
- WHERE 子句（如果给定）指示要选择的行必须满足的一个或多个条件。 where_condition 是一个表达式，对于要选择的每一行，它的计算结果为真。 如果没有 WHERE 子句，该语句将选择所有行。

在 WHERE 表达式中，您可以使用 TDSQL支持的任何函数和运算符，聚合（组）函数除外。SELECT 也可用   于检索在不参考任何表的情况下计算的行。
例如：
```
MySQL [test]> select 1+1;
+-----+
| 1+1 |
+-----+
|   2 |
+-----+
1 row in set (0.00 sec)
```
在没有引用表的情况下，您可以将 DUAL 指定为虚拟表名：
```
MySQL [test]> SELECT 1 + 1 FROM DUAL;
+-------+
| 1 + 1 |
+-------+
|     2 |
+-------+
1 row in set (0.00 sec)
```

DUAL 纯粹是为了方便那些要求所有 SELECT 语句都应该有 FROM 和其他可能的子句的人。 TDSQL可能会忽略这些子句。 如果没有引用表，TDSQL不需要 FROM DUAL。
通常，使用的子句必须完全按照语法描述中显示的顺序给出。 例如，HAVING 子句必须在任何 GROUP BY 子句之后和任何 ORDER BY 子句之前。 INTO 子句（如果存在）可以出现在语法描述指示的任何位置，但在给定语句中只能出现一次，不能出现在多个位置。 
select_expr 术语列表包含指示要检索哪些列的选择列表。 术语指定列或表达式或可以使用 *- 简写：
- 仅包含一个非限定 * 的选择列表可用作从所有表中选择所有列的简写：
```
SELECT * FROM t1 INNER JOIN t2 ...
```
- tbl_name.* 可用作限定的速记以从命名表中选择所有列：
```
SELECT t1.*, t2.* FROM t1 INNER JOIN t2 ...
```
- 将不合格的 * 与选择列表中的其他项目一起使用可能会产生解析错误。 为避免此问题，请使用限定的 tbl_name.* 引用：
```
SELECT AVG(score), t1.* FROM t1 ...
```

以下列表提供了有关其他 SELECT 子句的附加信息：
- 可以使用 AS alias_name 为 select_expr 赋予一个别名。 别名用作表达式的列名，可以在 GROUP BY、ORDER BY 或 HAVING 子句中使用。 例如：
```
SELECT CONCAT(last_name,', ',first_name) AS full_name 
FROM mytable ORDER BY full_name;
```
- 当使用标识符为 select_expr 设置别名时，AS 关键字是可选的。 但是，因为 AS 是可选的，如果您忘记了两个 select_expr 表达式之间的逗号，则会出现一个微妙的问题：TDSQL 将第二个解释为别名。 例如，在以下语句中，columnb 被视为别名：SELECT columna columnb FROM mytable;因此，在指定列别名时养成明确使用 AS 的习惯是一种很好的做法。
- 您可以使用 tbl_name 或 db_name.tbl_name 来引用默认数据库中的表以明确指定数据库。 您可以将列称为 col_name、tbl_name.col_name 或 db_name.tbl_name.col_name。 您不需要为列引用指定 tbl_name 或 db_name.tbl_name 前缀，除非引用不明确。 
- 可以使用 tbl_name AS alias_name 或 tbl_name alias_name 为表引用设置别名。 这些语句是等效的：
```
SELECT t1.name，t2.salary FROM employee AS t1，info AS t2
  WHERE t1.name = t2.name;

SELECT t1.name，t2.salary FROM employee t1，info t2
  WHERE t1.name = t2.name;
```
- 可以使用列名、列别名或列位置在 ORDER BY 和 GROUP BY 子句中引用为输出选择的列。 列位置是整数并以 1 开头：
```
SELECT college, region, seed FROM tournament
  ORDER BY region, seed;

SELECT college, region AS r, seed AS s FROM tournament
  ORDER BY r, s;

SELECT college, region, seed FROM tournament
  ORDER BY 2, 3;
```
要按相反顺序排序，请将 DESC（降序）关键字添加到排序依据的 ORDER BY 子句中的列名。 默认为升序； 这可以使用 ASC 关键字显式指定。不推荐使用列位置，因为该语法已从 SQL 标准中删除。
- TDSQL支持 ORDER BY 和分组功能，这也意味着您可以在使用 GROUP BY 时对任意一列或多列进行排序，如下所示：
```
SELECT a, b, COUNT(c) AS t FROM test_table GROUP BY a,b ORDER BY a,t DESC
```
- 当您使用 ORDER BY 或 GROUP BY 对 SELECT 中的列进行排序时，服务器仅使用 max_sort_length 系统变量指示的初始字节数对值进行排序。 
- GROUP BY 允许使用 WITH ROLLUP 修饰符。  
- HAVING 子句与 WHERE 子句一样，指定选择条件。 WHERE 子句指定选择列表中列的条件，但不能引用聚合函数。 HAVING 子句指定组的条件，通常由 GROUP BY 子句组成。 查询结果只包含满足 HAVING 条件的组。 （如果不存在 GROUP BY，则所有行都隐式地形成一个聚合组。）HAVING 子句几乎最后应用，就在项目被发送到客户端之前，没有优化。 （LIMIT 在 HAVING 之后应用。）SQL 标准要求 HAVING 必须仅引用 GROUP BY 子句中的列或聚合函数中使用的列。 但是，TDSQL支持此行为的扩展，并允许 HAVING 引用 SELECT 列表中的列和外部子查询中的列。如果 HAVING 子句引用不明确的列，则会出现警告。 在以下语句中， col2 不明确，因为它既用作别名又用作列名：
```
SELECT COUNT (col1) AS col2 FROM t GROUP BY col2 HAVING col2 = 2;
```

优先考虑标准 SQL 行为，因此如果在 GROUP BY 中使用 HAVING 列名并作为选择列列表中的别名列，则优先考虑 GROUP BY 列中的列。
- 不要对应该在 WHERE 子句中的项目使用 HAVING。 例如，不要写以下内容：
```
SELECT col_name FROM tbl_nameHAVING col_name> 0;
```
改写这个：
```
SELECT col_name FROM tbl_nameWHERE col_name> 0;
```
- HAVING 子句可以引用聚合函数，而 WHERE 子句不能：
```
SELECT user, MAX(salary) FROM users
GROUP BY user HAVING MAX(salary) > 10;
```
- TDSQL允许重复的列名。 也就是说，可以有多个同名的 select_expr。 这是标准 SQL 的扩展。 因为 TDSQL还允许 GROUP BY 和 HAVING 引用 select_expr 值，这可能会导致歧义：
```
SELECT 12 AS a，FROM t GROUP BY a;
```

在该语句中，两列的名称均为 a。 为确保使用正确的列进行分组，请为每个 select_expr 使用不同的名称。
- WINDOW 子句（如果存在）定义可以由窗口函数引用的命名窗口。 
- TDSQL通过在 select_expr 值中搜索，然后在 FROM 子句中的表的列中搜索来解析 ORDER BY 子句中的非限定列或别名引用。 对于 GROUP BY 或 HAVING 子句，它在搜索 select_expr 值之前先搜索 FROM 子句。 
- LIMIT 子句可用于限制 SELECT 语句返回的行数。 LIMIT 接受一个或两个数字参数，它们都必须是非负整数常量，但以下情况除外：
- 在prepare的语句中，可以使用 ? 占位符。
- 在存储的程序中，可以使用整数值的例程参数或局部变量来指定 LIMIT 参数。

### JOIN语法
TDSQL对 SELECT 语句和多表 DELETE 和 UPDATE 语句的 table_references 部分支持以下 JOIN 语法：
```
table_references:
    	escaped_table_reference [, escaped_table_reference] ...

escaped_table_reference: {
    table_reference
  | { OJ table_reference }
}

table_reference: {
    table_factor
  | joined_table
}

table_factor: {
    tbl_name [PARTITION (partition_names)]
        [[AS] alias]
  | [LATERAL] table_subquery [AS] alias [(col_list)]
  | ( table_references )
}

joined_table: {
    table_reference {[INNER | CROSS] JOIN | STRAIGHT_JOIN} table_factor [join_specification]
  | table_reference {LEFT|RIGHT} [OUTER] JOIN table_reference join_specification
  | table_reference NATURAL [INNER | {LEFT|RIGHT} [OUTER]] JOIN table_factor
}

join_specification: {
    ON search_condition
  | USING (join_column_list)
}

join_column_list:
    column_name [, column_name] ...

index_list:
    index_name [, index_name] ...
```
表引用（当它引用分区表时）可能包含一个 PARTITION 子句，包括以逗号分隔的分区、子分区或两者的列表。 此选项跟在表的名称之后，并在任何别名声明之前。 此选项的效果是仅从列出的分区或子分区中选择行。 任何未在列表中命名的分区或子分区都将被忽略。 
与标准 SQL 相比，TDSQL 中对 table_factor 的语法进行了扩展。 该标准只接受 table_reference，而不是一对括号内的列表。
如果 table_reference 项列表中的每个逗号都被视为等效于内部联接，则这是一种保守的扩展。 例如：
```
SELECT * FROM t1 LEFT JOIN (t2，t3，t4)
                 ON (t2.a = t1.a AND t3.b = t1.b AND t4.c = t1.c)
```
相当于：
```
SELECT * FROM t1 LEFT JOIN (t2 CROSS JOIN t3 CROSS JOIN t4)
                 ON (t2.a = t1.a AND t3.b = t1.b AND t4.c = t1.c)
```
在 TDSQL中，JOIN、CROSS JOIN 和 INNER JOIN 在语法上是等价的（它们可以相互替换）。 在标准 SQL 中，它们不是等价的。 INNER JOIN 与 ON 子句一起使用，否则使用 CROSS JOIN。
通常，在仅包含内部连接操作的连接表达式中可以忽略括号。 TDSQL还支持嵌套连接。  
以下列表描述了在编写连接时要考虑的一般因素：
- 可以使用 tbl_name AS alias_name 或 tbl_name alias_name 为表引用设置别名：
```
SELECT t1.name，t2.salary
  FROM employee AS t1 INNER JOIN info AS t2 ON t1.name = t2.name;

SELECT t1.name，t2.salary
  FROM employee t1 INNER JOIN info t2 ON t1.name = t2.name;
```
- table_subquery 在 FROM 子句中也称为派生表或子查询。 此类子查询必须包含一个别名，以便为子查询结果提供表名，并且可以选择在括号中包含表列名列表。 一个简单的例子如下：
```
SELECT * FROM (SELECT 1,2,3) AS t1;
```
- 在没有连接条件的情况下，INNER JOIN 和 ,（逗号）在语义上是等效的：两者都在指定的表之间产生笛卡尔积（即，第一个表中的每一行都连接到第二个表中的每一行 ）。
但是，逗号运算符的优先级低于 INNER JOIN、CROSS JOIN、LEFT JOIN 等。 如果在存在连接条件时将逗号连接与其他连接类型混合使用，则可能会出现“on 子句”中的“未知列”列“col_name”形式的错误。 
- 与 ON 一起使用的 search_condition 是可以在 WHERE 子句中使用的形式的任何条件表达式。 通常，ON 子句用于指定如何连接表的条件，而 WHERE 子句限制将哪些行包含在结果集中。
- 如果在 LEFT JOIN 的 ON 或 USING 部分中没有与右表匹配的行，则将所有列都设置为 NULL 的行用于右表。 您可以使用此事实来查找表中在另一个表中没有对应项的行：
```
SELECT  left_tbl.*
  FROM left_tbl LEFT JOIN right_tbl ON left_tbl.id = right_tbl.id
  WHERE right_tbl.id IS NULL;
```
- USING(join_column_list) 子句命名必须存在于两个表中的列列表。 如果表 a 和 b 都包含列 c1、c2 和 c3，则以下连接比较两个表中的相应列：
```
a LEFT JOIN b USING (c1, c2, c3)
```

一些连接示例：
```
SELECT * FROM table1，table2;

SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;

SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id;

SELECT * FROM table1 LEFT JOIN table2 USING (id);

SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id
  LEFT JOIN table3 ON table2.id = table3.id;
```
自然连接和使用 USING 的连接，包括外连接变体，根据 SQL2003 标准进行处理：
- NATURAL 连接的冗余列不会出现。 考虑这组语句：
```
DROP TABLE IF EXISTS T1,T2;
CREATE TABLE t1 (i INT primary key, j INT);
CREATE TABLE t2 (k INT primary key, j INT);
INSERT INTO t1 VALUES(1, 1);
INSERT INTO t2 VALUES(1, 1);
SELECT * FROM t1 NATURAL JOIN t2;
SELECT * FROM t1 JOIN t2 USING (j);
```
在第一个 SELECT 语句中，列 j 出现在两个表中，因此成为连接列，因此，根据标准 SQL，它应该在输出中只出现一次，而不是两次。 同样，在第二个 SELECT 语句中，列 j 在 USING 子句中命名，并且在输出中应该只出现一次，而不是两次。
因此，语句产生以下输出：
```
 +------+------+------+
| j    | i    | k    |
+------+------+------+
|    1 |    1 |    1 |
+------+------+------+
+------+------+------+
| j    | i    | k    |
+------+------+------+
|    1 |    1 |    1 |
+------+------+------+
```
根据标准 SQL 进行冗余列消除和列排序，产生以下显示顺序：
- 首先，按照它们在第一个表中出现的顺序合并两个连接表的公共列 
- 其次，第一个表独有的列，按照它们在该表中出现的顺序 
- 第三，第二个表独有的列，按照它们在该表中出现的顺序
使用合并操作定义替换两个公共列的单个结果列。 也就是说，对于两个 t1.a 和 t2.a，生成的单个连接列 a 定义为 a = COALESCE(t1.a, t2.a)，其中：
```
COALESCE(x, y) = (CASE WHEN x IS NOT NULL THEN x ELSE y END)
```
如果连接操作是任何其他连接，则连接的结果列由连接表的所有列的串联组成。
合并列的定义的结果是，对于外连接，如果两列之一始终为 NULL，合并列包含非 NULL 列的值。 如果两个列都不为 NULL，则两个公共列具有相同的值，因此选择哪一个作为合并列的值并不重要。 解释这一点的一种简单方法是考虑外部联接的合并列由 JOIN 的内部表的公共列表示。 假设表 t1(a, b) 和 t2(a, c) 的内容如下：
```
t1    t2
----  ----
1 x   2 z
2 y   3 w
```

然后，对于此连接，列 a 包含以下值 t1.a ：

```
mysql> SELECT * FROM t1 NATURAL LEFT JOIN t2;
+------+------+------+
| a    | b    | c    |
+------+------+------+
|    1 | x    | NULL |
|    2 | y    | z    |
+------+------+------+
```

相反，对于此连接，列 a 包含值 t2.a 。
```
mysql> SELECT * FROM t1 NATURAL RIGHT JOIN t2;
+------+------+------+
| a    | c    | b    |
+------+------+------+
|    2 | z    | y    |
|    3 | w    | NULL |
+------+------+------+
```
将这些结果与其他等效查询进行比较 JOIN ... ON ：
```
mysql> SELECT * FROM t1 LEFT JOIN t2 ON (t1.a = t2.a);
+------+------+------+------+
| a    | b    | a    | c    |
+------+------+------+------+
|    1 | x    | NULL | NULL |
|    2 | y    |    2 | z    |
+------+------+------+------+
mysql> SELECT * FROM t1 RIGHT JOIN t2 ON (t1.a = t2.a);
+------+------+------+------+
| a    | b    | a    | c    |
+------+------+------+------+
|    2 | y    |    2 | z    |
| NULL | NULL |    3 | w    |
+------+------+------+------+
```

- USING 子句可以重写为比较相应列的 ON 子句。 但是，虽然 USING 和 ON 很相似，但它们并不完全相同。 考虑以下两个查询：
```
a LEFT JOIN b USING (c1, c2, c3)
a LEFT JOIN b ON a.c1 = b.c1 AND a.c2 = b.c2 AND a.c3 = b.c3
```
关于确定哪些行满足连接条件，两个连接在语义上是相同的。
关于确定为 SELECT * 扩展显示哪些列，这两个连接在语义上并不相同。 USING 连接选择相应列的合并值，而 ON 连接选择所有表中的所有列。 对于 USING 连接，SELECT  *  选择以下值：
```
COALESCE(a.c1, b.c1), COALESCE(a.c2, b.c2), COALESCE(a.c3, b.c3)
```
对于 ON 连接，SELECT * 选择以下值：
```
  a.c1，a.c2，a.c3，b.c1，b.c2，b.c3
```
对于内部联接，COALESCE(a.c1, b.c1) 与 a.c1 或 b.c1 相同，因为两列具有相同的值。 使用外连接（例如 LEFT JOIN），两列之一可以为 NULL。 结果中省略了该列。
- ON 子句只能引用其操作数
   示例：
```
drop table if exists t1,t2,t3;
CREATE TABLE t1 (i1 INT primary key);
CREATE TABLE t2 (i2 INT primary key);
CREATE TABLE t3 (i3 INT primary key);
SELECT * FROM t1 JOIN t2 ON (i1 = i3) JOIN t3;
```
该语句失败并在“on 子句”错误中出现未知列“i3”，因为 i3 是 t3 中的一个列，它不是 ON 子句的操作数。 要使连接能够被处理，请按如下方式重写语句：
```
 SELECT * FROM t1 JOIN t2 JOIN t3 ON (i1 = i3);
```
 SELECT * FROM t1 JOIN t2 JOIN t3 ON (i1 = i3);
- JOIN 的优先级高于逗号运算符 (,)，因此连接表达式 t1, t2 JOIN t3 被解释为 (t1, (t2 JOIN t3))，而不是 ((t1, t2) JOIN t3)。 这会影响使用 ON 子句的语句，因为该子句只能引用连接操作数中的列，并且优先级会影响对这些操作数是什么的解释。
 示例：
```
drop table if exists t1,t2,t3;
CREATE TABLE t1 (i1 INT primary key,j1 INT);
CREATE TABLE t2 (i2 INT primary key,j2 INT);
CREATE TABLE t3 (i3 INT primary key,j3 INT);
INSERT INTO t1 VALUES(1,1);
INSERT INTO t2 VALUES(1,1);
INSERT INTO t3 VALUES(1,1);
SELECT * FROM t1,t2 JOIN t3 ON (t1.i1 = t3.i3);
```
JOIN 优先于逗号运算符，因此 ON 子句的操作数是 t2 和 t3。 由于 t1.i1 不是任一操作数中的列，因此结果是“on 子句”错误中的未知列“t1.i1”。
要处理连接，请使用以下任一策略：
	- 用括号将前两个表显式分组，以便 ON 子句的操作数是 (t1, t2) 和 t3：
```
	SELECT * FROM (t1, t2) JOIN t3 ON (t1.i1 = t3.i3);
```
	- 避免使用逗号运算符并使用 JOIN 代替：
```
	SELECT * FROM t1 JOIN t2 JOIN t3 ON (t1.i1 = t3.i3);
```
优先级相同的解释也适用于与混合逗号操作语句 INNER JOIN ， CROSS JOIN ， LEFT JOIN ，并且 RIGHT JOIN ，所有这些都具有比逗号操作符更高的优先级。

### UNION语法
语法如下：
```
SELECT ...
UNION [ALL | DISTINCT] SELECT ...
[UNION [ALL | DISTINCT] SELECT ...]
```
UNION 将来自多个 SELECT 语句的结果组合到一个结果集中。 例子：
```
MySQL [test]> SELECT 1, 2;
+---+---+
| 1 | 2 |
+---+---+
| 1 | 2 |
+---+---+
1 row in set (0.00 sec)

MySQL [test]> SELECT 'a', 'b';
+---+---+
| a | b |
+---+---+
| a | b |
+---+---+
1 row in set (0.00 sec)

MySQL [test]> SELECT 1, 2 UNION SELECT 'a', 'b';
+---+---+
| 1 | 2 |
+---+---+
| 1 | 2 |
| a | b |
+---+---+
2 rows in set (0.01 sec)
```
### 结果集列名和数据类型
UNION 结果集的列名取自第一个 SELECT 语句的列名。
每个 SELECT 语句对应位置列出的选定列应具有相同的数据类型。 例如，第一个语句选择的第一列应该与其他语句选择的第一列具有相同的类型。 如果对应的 SELECT 列的数据类型不匹配，则 UNION 结果中列的类型和长度会考虑所有 SELECT 语句检索到的值。 例如，考虑以下情况，其中列长度不受第一个 SELECT 值长度的限制：
```
MySQL [test]> SELECT REPEAT('a',1) UNION SELECT REPEAT('b',20);
+----------------------+
| REPEAT('a',1)        |
+----------------------+
| a                    |
| bbbbbbbbbbbbbbbbbbbb |
+----------------------+
2 rows in set (0.02 sec)
```
### UNION DISTINCT 和 UNION ALL
默认情况下，将从 UNION 结果中删除重复的行。 可选的 DISTINCT 关键字具有相同的效果，但使其明确。 使用可选的 ALL 关键字，不会发生重复行删除，结果包括来自所有 SELECT 语句的所有匹配行。
您可以在同一查询中混合使用 UNION ALL 和 UNION DISTINCT。 混合 UNION 类型的处理方式是 DISTINCT 联合覆盖其左侧的任何 ALL 联合。 可以通过使用 UNION DISTINCT 显式生成 DISTINCT 联合，也可以通过使用不带 DISTINCT 或 ALL 关键字的 UNION 隐式生成。
## 子查询语法
子查询是 SELECT 另一个语句中的语句。
支持 SQL 标准要求的所有子查询形式和操作，以及一些特定于 TDSQL 的功能。
下面是一个子查询的示例：
```
SELECT * FROM t1 WHERE column1 in (SELECT column1 FROM t2);
```
>!通常不推荐使用子查询，一般需要将子查询修改为join或者进行优化改写。

### 子查询错误
有些错误仅适用于子查询。 本节介绍它们。
- 不支持的子查询语法：
```
ERROR 1235 (ER_NOT_SUPPORTED_YET)
SQLSTATE = 42000
Message = "This version of MySQL doesn't yet support
'LIMIT & IN/ALL/ANY/SOME subquery'"
```
-  这意味着TDSQL不支持以下形式的语句：
```
SELECT * FROM t1 WHERE s1 IN (SELECT s2 FROM t2 ORDER BY s1 LIMIT 1)
```
- 来自子查询的列数不正确：
```
ERROR 1241 (ER_OPERAND_COL)
SQLSTATE = 21000
Message = "Operand should contain 1 column(s)"
```
在这种情况下会发生此错误：
SELECT (SELECT column1，column2 FROM t2) FROM t1;
 如果目的是行比较，您可以使用返回多列的子查询。 在其他上下文中，子查询必须是标量操作数 
- 子查询中的行数不正确：
```
ERROR 1242 (ER_SUBSELECT_NO_1_ROW)
SQLSTATE = 21000
Message = "Subquery returns more than 1 row"
```
对于子查询必须最多返回一行但返回多行的语句，会发生此错误。 考虑以下示例：
```
SELECT * FROM t1 WHERE column1 = (SELECT column1 FROM t2);
```
如果 SELECT column1 FROM t2 只返回一行，则前面的查询有效。 如果子查询返回多于一行，则会出现错误 1242。 在这种情况下，查询应改写为：
```
SELECT * FROM t1 WHERE column1 = ANY(SELECT column1 FROM t2);
```
- 子查询中错误使用的表：
```
Error 1093 (ER_UPDATE_TABLE_USED)
SQLSTATE = HY000
Message = "You can't specify target table 'x'
for update in FROM clause"
```
在以下情况下会发生此错误，该情况尝试修改表并从子查询中的同一表中进行选择：
```
UPDATE t1 SET column2 = (SELECT MAX(column1) FROM t1);
```
您可以使用公用表表达式来解决此问题。

### 优化子查询
开发正在进行中，因此从长远来看，没有优化技巧可靠。 以下列表提供了一些您可能想要使用的有趣技巧。
- 将子句从外部移动到子查询内部。 例如，使用这个查询： 
```
SELECT * FROM t1
  WHERE s1 IN (SELECT s1 FROM t1 UNION ALL SELECT s1 FROM t2);
```
而不是这个：
```
SELECT * FROM t1
  WHERE s1 IN (SELECT s1 FROM t1) OR s1 IN (SELECT s1 FROM t2);
```
再举一个例子，使用这个查询：
```
SELECT (SELECT column1 + 5 FROM t1) FROM t2;
```
而不是这个查询：
```
SELECT (SELECT column1 FROM t1) + 5 FROM t2;
```
- 使用行子查询而不是相关子查询。 例如，使用此查询：
```
SELECT * FROM t1
  WHERE (column1，column2) IN (SELECT column1，column2 FROM t2);
```
而不是这个查询：
```
SELECT * FROM t1
  WHERE EXISTS (SELECT * FROM t2 WHERE t2.column1 = t1.column1
                AND t2.column2 = t1.column2);
```
这些技巧可能会导致程序变得更快或更慢。 使用像 BENCHMARK() 函数 这样的工具 ，你可以了解在你自己的情况下有什么帮助。 
### 将子查询重写为连接
有时，除了使用子查询之外，还有其他方法可以测试一组值中的成员资格。 此外，在某些情况下，不仅可以在没有子查询的情况下重写查询，但使用其中一些技术而不是使用子查询可能更有效。 其中一个是 IN() 构造：
例如，这个查询：
```
SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);
```
可以改写为：
```
SELECT DISTINCT t1.* FROM t1，t2 WHERE t1.id = t2.id;
```
查询：
```
SELECT * FROM t1 WHERE id NOT IN (SELECT id FROM t2);
SELECT * FROM t1 WHERE NOT EXISTS (SELECT id FROM t2 WHERE t1.id = t2.id);
```
可以改写为：
```
SELECT table1.*
  	FROM table1 LEFT JOIN table2 ON table1.id = table2.id
 	 WHERE table2.id IS NULL;
```
A LEFT [OUTER] JOIN 可以比等效的子查询更快，因为服务器可能能够更好地优化它 - 这一事实并非仅针对TDSQL服务器。 在SQL-92之前，外连接不存在，因此子查询是执行某些操作的唯一方法。  

## UPDATE语法
UPDATE 是一个修改表中行的DML语句。
单表语法：
```
UPDATE [IGNORE] table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]

value:
    {expr | DEFAULT}

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```

多表语法：
```
UPDATE [IGNORE] table_references
SET assignment_list
[WHERE where_condition]
```
对于单表语法，UPDATE 语句使用新值更新命名表中现有行的列。 SET 子句指示要修改的列以及应该给它们的值。每个值都可以作为表达式给出，或者使用关键字 DEFAULT 将列显式设置为其默认值。 WHERE 子句（如果给定）指定标识要更新哪些行的条件。如果没有 WHERE 子句，则更新所有行。如果指定了 ORDER BY 子句，则按指定的顺序更新行。 LIMIT 子句限制了可以更新的行数。
对于多表语法，UPDATE 更新 table_references 中命名的每个表中满足条件的行。每个匹配行都会更新一次，即使它多次匹配条件。对于多表语法，不能使用 ORDER BY 和 LIMIT。
对于分区表，该语句的单表和多表形式都支持使用 PARTITION 子句作为表引用的一部分。此选项采用一个或多个分区或子分区（或两者）的列表。只检查列出的分区（或子分区）是否匹配，并且不更新任何不在这些分区或子分区中的行，无论它是否满足 where_condition。
>!与将 PARTITION 与 INSERT 或 REPLACE 语句一起使用的情况不同，即使列出的分区（或子分区）中没有行与 where_condition 匹配，否则有效的 UPDATE ... PARTITION 语句也被认为是成功的。
where_condition 是一个表达式，对于要更新的每一行，它的计算结果为真。 
仅对实际更新的 UPDATE 中引用的列才需要 UPDATE 权限。 对于已读取但未修改的任何列，您只需要 SELECT 权限。

如果在表达式中访问要更新的表中的列，UPDATE 将使用该列的当前值。 例如，以下语句将 col1 设置为比其当前值大 1：
```
UPDATE t1 SET col1 = col1 + 1;
```
以下语句中的第二个赋值将 col2 设置为当前（更新后的） col1 值，而不是原始 col1 值。 结果是 col1 和 col2 具有相同的值。 此行为不同于标准 SQL。
```
UPDATE t1 SET col1 = col1 + 1,col2 = col1;
```
单表 UPDATE 分配通常从左到右进行评估。对于多表更新，不能保证按任何特定顺序执行分配。
如果您将一列设置为它当前拥有的值，TDSQL会注意到这一点并且不会更新它。
如果通过设置为 NULL 更新已声明为 NOT NULL 的列，则在启用严格 SQL 模式时会发生错误；否则，列被设置为列数据类型的隐式默认值，并且警告计数增加。数字类型的隐式默认值为 0，字符串类型为空字符串 ('')，日期和时间类型为“零”值。
如果显式更新生成的列，则唯一允许的值是 DEFAULT。
您可以使用 LIMIT row_count 来限制 UPDATE 的范围。 LIMIT 子句是行匹配限制。只要找到满足 WHERE 子句的 row_count 行，该语句就会立即停止，无论它们是否实际发生了更改。
如果 UPDATE 语句包含 ORDER BY 子句，则按该子句指定的顺序更新行。这在某些可能导致错误的情况下很有用。假设表 t 包含具有唯一索引的列 id。以下语句可能会因重复键错误而失败，具体取决于行更新的顺序：
```
UPDATE t SET id = id + 1;
```
例如，如果表的id 列中包含1 和2，并且在2 更新为3 之前将1 更新为2，则会发生错误。 为了避免这个问题，添加一个 ORDER BY 子句，使具有较大 id 值的行在具有较小值的行之前更新：
```
UPDATE t SET id = id + 1 ORDER BY id DESC;
```
您还可以执行涵盖多个表的 UPDATE 操作。 但是，不能将 ORDER BY 或 LIMIT 用于多表 UPDATE。 
table_references 子句列出了连接中涉及的表。 下面是一个例子：
```
UPDATE  items,month SET items.price=month.price
WHERE items.id=month.id;
```
