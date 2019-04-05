计算一个行集合。

## 概要

```sql
VALUES ( expression [, ...] ) [, ...]
   [ORDER BY sort_expression [ASC | DESC | USING operator] [, ...]]
   [LIMIT {count | ALL}] [OFFSET start]
```

## 描述
VALUES 计算由值表达式指定的一个行值或者一组行值。更常见的是把它用来生成一个大型命令内的"常量表"，但是它也可以被独自使用。

当多于一行被指定时，所有行都必须具有相同数量的元素。 结果表的列数据类型由出现在该列的表达式的显式或者推导类型组合决定，决定的规则与 UNION 相同。

在大型的命令中，在语法上允许 VALUES 出现在 SELECT 出现的任何地方。因为语法把它当做一个 SELECT，可以为一个 VALUES 命令使用 ORDERBY、LIMIT 和 OFFSET 子句。

## 参数

expression
要在结果表（行集合）中指定位置计算并且插入的一个常量或者表达式。在一个出现于 INSERT 顶层的 VALUES 列表中， expression 可以被 DEFAULT 替代以表示应该插入目标列的默认值。 当 VALUES 出现在其他环境中时，不能使用 DEFAULT。

sort_expression
一个指示如何排序结果行的表达式或者整型常量。这个表达式可以用 column1、column2 等来引用该 VALUES 结果的列。更多细节，参见 SELECT 的参数中的“ORDER BY 子句”。

operator
一个排序操作符。更多细节，参见 SELECT 的参数中的“ORDER BY 子句”。

LIMIT count
OFFSET start
要返回的最大行数。更多细节，参见 SELECT 的参数中的“LIMIT 子句”。

## 注解
应该避免具有大量行的 VALUES 列表，否则可能会碰到内存不足失败或者很差的性能。出现在 INSERT 中的 VALUES 是一种特殊情况（因为想要的列类型可以从 INSERT 的目标表得知，并且不需要通过扫描该 VALUES 列表来推导），因此它可以处理比其他环境中更大的列表。

## 示例
一个纯粹的 VALUES 命令：

```sql
VALUES (1, 'one'), (2, 'two'), (3, 'three');
```

这将返回一个具有两列、三行的表。它实际等效于：

```sql
SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';
```

更常用地，VALUES 可以被用在一个大型 SQL 命令中。 在 INSERT 中最常用：

```sql
INSERT INTO films (code, title, did, date_prod, kind)
    VALUES ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');
```

在 INSERT 环境中，一个 VALUES 列表的项可以是 DEFAULT 指示应该使用该列的默认值而不是指定一个值：

```sql
INSERT INTO films VALUES
    ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 
minutes'),
    ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama', DEFAULT);
```

VALUES 也可以被用在可以写 子-SELECT 的地方，例如在一个 FROM 子句中：

```sql
SELECT f.* FROM films f, (VALUES('MGM', 'Horror'), ('UA', 
'Sci-Fi')) AS t (studio, kind) WHERE f.studio = t.studio AND 
f.kind = t.kind;
UPDATE employees SET salary = salary * v.increase FROM 
(VALUES(1, 200000, 1.2), (2, 400000, 1.4)) AS v (depno, 
target, increase) WHERE employees.depno = v.depno AND 
employees.sales >= v.target;
```

注意：当 VALUES 被用在一个 FROM 子句中时， 需要提供一个 AS 句，与 SELECT 相同。 不需要为所有的列用 AS 子句指定名称，但是那样做是一种好习惯。在数据库中，VALUES 的默认列名是 column1、column2 等，但在其他数据库系统中可能会不同。

当在 INSERT 中使用 VALUES 时，值都会被自动地强制为相应目标列的数据类型。当在其他环境中使用时，有必要指定正确的数据类型。如果项都是带引号的字符串常量，强制第一个就足以为所有项假设数据类型：

```sql
SELECT * FROM machines WHERE ip_address IN 
(VALUES('192.168.0.1'::inet), ('192.168.0.10'), 
('192.0.2.43'));
```

注意：对于简单的 IN 测试，最好使用 IN 的 list-of-scalars 形式，而不是写一个上面那样的 VALUES 查询。标量列表方法的书写更少并且更加高效。

## 兼容性
VALUES 符合 SQL 标准，但 LIMIT 和 OFFSET 是数据库的扩展。

## 另见
INSERT、SELECT
