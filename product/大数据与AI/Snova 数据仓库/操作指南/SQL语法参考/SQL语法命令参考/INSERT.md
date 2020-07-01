在表中创建新行。

## 概要

```sql
INSERT INTO table [( column [, ...] )]
   {DEFAULT VALUES | VALUES ( {expression | DEFAULT} [, ...] ) 
   [, ...] | query}
```

## 描述
INSERT 将新行插入到一个表中。我们可以插入一个或者更多由值表达式指定的行，或者插入来自一个查询的零行或者更多行。

目标列的名称可以以任意顺序列出。如果没有给出列名列表，默认的方式是按照表在定义时列的顺序。VALUES 子句或者 query 提供的值会被从左至右关联到这些显式或者隐式给出的目标列。

每一个没有出现在显式或者隐式列列表中的列都将被默认填充，如果为该列声明过默认值则用默认值填充，否则用空值填充。

如果任意列的表达式不是正确的数据类型，将会尝试自动类型转换。

为了向表中插入数据，用户必须拥有在其上的 INSERT 特权。

**输出**
成功完成时，INSERT 命令会返回以下形式的命令标签：
```sql
INSERT oid count
```
count 是被插入的行数。 如果 count 正好为 1 并且目标表具有 OID，那么 oid 就是分配给被插入行的 OID。否则 oid 为零。

## 参数
table
一个已有表的名称（可以被方案限定）。

column
在表中的列的名称。如有必要，列名可以用一个子域名或者数组下标限定（指向一个组合列的某些列中插入会让其他域为空）。

DEFAULT VALUES
所有列都将被其默认值填充。

expression
要赋予给相应列的表达式或者值。

DEFAULT
相应的列将被其默认值填充。

query
提供要被插入行的查询（SELECT 语句）。其语法描述参考 SELECT 语句。

## 注解
要插入数据到一个分区表中，需要指定根分区表，该表通过  CREATE TABLE 命令创建，也需要在 INSERT 命令中指定分区表的一个叶子分区表，如果对于指定的叶子分区表数据是无效的，将抛出错误。在 INSERT 命令中，目前还不支持指定叶子分区表。其他 DML 命令，例如 UPDATE 和 DELETE，在指定一个叶子分区表的执行也不支持。这些命令一定是执行在根分区表中，即通过 CREATE TABLE 创建的表。

对于追加优化表，数据库支持最大并行度为127的并行 INSERT 事务插入到一个追加优化表中。

## 示例
插入当条行到表 films 中：

```sql
INSERT INTO films VALUES ('UA502', 'Bananas', 105, 
'1971-07-13', 'Comedy', '82 minutes');
```

在这个示例中，列 length 被忽略，因此它将被默认值填充：

```sql
INSERT INTO films (code, title, did, date_prod, kind) VALUES 
('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');
```

这个示例中对列 date_prod 使用了 DEFAULT 子句而不是指定一个具体的值：

```sql
INSERT INTO films VALUES ('UA502', 'Bananas', 105, DEFAULT, 
'Comedy', '82 minutes');
```

插入一条全部都是由默认值组成的行：

```sql
INSERT INTO films DEFAULT VALUES;
```

通过语法多行的 VALUES 语法同时插入多条行的数据：

```sql
INSERT INTO films (code, title, did, date_prod, kind) VALUES
    ('B6717', 'Tampopo', 110, '1985-02-10', 'Comedy'),
    ('HG120', 'The Dinner Game', 140, DEFAULT, 'Comedy');
```

在这个示例中，从具有相同表结构的表 tmp_films 插入若干的行到表 films：

```sql
INSERT INTO films SELECT * FROM tmp_films WHERE date_prod < 
'2004-05-07';
```

## 兼容性
INSERT 符合 SQL 标准。标准不允许省略列名列表但不通过 VALUES 或者query填充所有列的情况。

query 子句可能的限制在 SELECT 有介绍。

## 另见
COPY、SELECT、CREATE EXTERNAL TABLE
