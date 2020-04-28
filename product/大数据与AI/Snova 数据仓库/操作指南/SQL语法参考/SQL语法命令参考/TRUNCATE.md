清空一个表。

## 概要

```sql
TRUNCATE [TABLE] name [, ...] [CASCADE | RESTRICT]
```

## 描述
TRUNCATE 可以从一组表中快速地移除所有行。它具有和在每个表上执行无条件 DELETE 相同的效果，不过它会更快，因为没有实际扫描表，在大表上最有用。

要截断一个表，用户必须具有其上的 TRUNCATE 特权。

## 参数

name
要截断的表的名字（可以是方案限定的）。

CASCADE
因为关键字应用到外键引用上数据库还没有支持，所有没有效果。

RESTRICT
因为关键字应用到外键引用上数据库还没有支持，所有没有效果。

## 注解
TRUNCATE 将不会引发表上可能存在的任何用户定义的 ON DELETE 触发器。

TRUNCATE 不会截断任何从命名的表继承而来的表。只有命名的表被截断，它的子表不会截断。

TRUNCATE 不会截断任何一个分区表的子表。如果用户指定了一个分区表的子表，TRUNCATE 不会从子表以及它的孩子表上移除行。

## 示例
清空表 films：

```sql
TRUNCATE films;
```

## 兼容性
在 SQL 标准中没有 TRUNCATE 命令。

## 另见
DELETE、DROP TABLE
