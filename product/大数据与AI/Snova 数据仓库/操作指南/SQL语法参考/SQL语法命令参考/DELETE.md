从表中删除行。

## 概要

```sql
DELETE FROM [ONLY] table [[AS] alias]
      [USING usinglist]
      [WHERE condition | WHERE CURRENT OF cursor_name ]
```

## 描述

DELETE 从指定的表中删除满足 WHERE 子句的行，如果该 WHERE 子句是空的，则会删除整个表行，该结果是有效的，只不过时个空表。

默认情况下，DELETE 会删除指定表中的行和他所有的子表。如果用户希望仅从特定指定的表中删除，请使用 ONLY 子句。

有两种使用包含在数据库中其他表的信息来删除行的方式：使用 sub-selects，或者在 USING 子句中指定额外的表。哪种技术更适合取决于具体情况。

如果指定了 WHERE CURRENT OF 子句，则删除的行是从指定的游标中最近读取的行。

用户必须有对表的 DELETE 权限才能从中删除。

**输出**

成功完成后， DELETE 命令返回表单的命令标签。

```sql
DELETE count
```

删除行的数量，如果数量为0，没有满足删除条件的行（这并不认为是一个错误）。

## 参数

ONLY
如果指定，仅从提名的表中删除行。如果没有指定，也会处理任何从提名的表继承的表。

table
存在表的名字（可选方案限定）。

alias
目标表的别名。当提供了别名，它完全隐藏了表的实际名字。例如给定 DELETE FROM foo AS f，该 DELETE 语句的其他部分必须将此表称为 f 而不是 foo。

usinglist
表达式列表，允许其他表的列出现在 WHERE 条件中。这和 SELECT 语句中 FROM 子句中可以指定的表的列表相似，例如，可以指定表的别名。不要重复使用 usinglist 中的目标表，除非用户希望设置自连接。

condition
返回类型为 boolean 的表达式，该表达式决定那些要删除的行。

cursor_name
要在 WHERE CURRENT OF 条件下使用的游标的名字。要删除的行是从该有游标最近读取的行。游标必须是 DELETE  目标表上的简单（非连接，非聚合）查询。
WHERE CURRENT OF 不能和布尔条件一起指定。
该 DELETE...WHERE CURRENT OF 游标语句只能在服务器上执行，例如交互式 psql 会话或脚本。语言扩展（如PL/pgSQL）不支持可更新游标。
更多有关创建有游标的信息，请参阅 DECLARE。

## 注意
数据库使用户在 WHERE 条件中通过指定在 USING 指定其他表来引用其他表的列。 例如对来自 rank 表的名为 Hannah的列，可能会这样做：

```sql
DELETE FROM rank USING names WHERE names.id = rank.id AND 
name = 'Hannah';
```

这里发生的本质是一个在 rank 和 names表之间的连接，所有成功连接的行都被标记为删除。该语法是不标准的。但是，相比子查询风格，该连接风格通常比较容易写，也能更快执行，例如：

```sql
DELETE FROM rank WHERE id IN (SELECT id FROM names WHERE name 
= 'Hannah');
```

当使用 DELETE 来删除表中的所有行（例如： DELETE * FROM *table*;），数据库添加了隐式的 TRUNCATE 命令（当用户权限允许时）。 该添加的 TRUNCATE 命令释放了被删除行所占的空间，而没有执行表的 VACUUM 操作。这提升了后续查询的扫描性能，有助于临时表经常插入和删除的 ELT 工作负载。

不支持在特定分区（子表）上直接执行 UPDATE 和 DELETE 命令。相反，这些命令必须在根分区表（使用 CREATE TABLE 命令创建的表）上执行。

## 示例
删除除了 musicals 之外的所有 films：

```sql
DELETE FROM films WHERE kind <> 'Musical';
```

清除表 films：

```sql
DELETE FROM films;
```

使用连接删除：

```sql
DELETE FROM rank USING names WHERE names.id = rank.id AND 
name = 'Hannah';
```

## 兼容性
该命令服从 SQL 标准，除了数据库的扩展 USING 子句。

## 另见

DECLARE、TRUNCATE
