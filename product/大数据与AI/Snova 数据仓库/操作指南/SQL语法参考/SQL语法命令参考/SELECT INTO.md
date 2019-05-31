从一个查询的结果定义一个新表。

## 概要
```sql
[ WITH with_query [, ...] ]
SELECT [ALL | DISTINCT [ON ( expression [, ...] )]]
    * | expression [AS output_name] [, ...]
    INTO [TEMPORARY | TEMP] [TABLE] new_table
    [FROM from_item [, ...]]
    [WHERE condition]
    [GROUP BY expression [, ...]]
    [HAVING condition [, ...]]
    [{UNION | INTERSECT | EXCEPT} [ALL] select]
    [ORDER BY expression [ASC | DESC | USING operator] [NULLS {FIRST | LAST}] [, ...]]
    [LIMIT {count | ALL}]
    [OFFSET start]
    [FOR {UPDATE | SHARE} [OF table_name [, ...]] [NOWAIT] 
    [...]]
```

## 描述
SELECT INTO 创建一个新表并且用一个查询计算得到的数据填充它。这些数据不会像普通的 SELECT 那样被返回给客户端。新表的列具有和 SELECT 的输出列相关的名称和数据类型。

## 参数
SELECT INTO 主要的参数同 **SELECT** 是一样的。

TEMPORARY
TEMP
如果被指定，该表被创建为一个临时表。

new_table
要创建的表的名字（可以是方案限定的）。

## 示例
创建一个新表 films_recent 由表 films 的最近项构成：

```sql
SELECT * INTO films_recent FROM films WHERE date_prod >= 
'2016-01-01';
```

## 兼容性
SQL 标准使用 SELECT INTO 表示把值选择到一个宿主程序的标量变量中，而不是创建一个新表。数据库使用 SELECT INTO 来表示创建是由历史原因的。最好在新的应用中使用 CREATE TABLE AS 来实现该目的。

## 另见
SELECT、CREATE TABLE AS
