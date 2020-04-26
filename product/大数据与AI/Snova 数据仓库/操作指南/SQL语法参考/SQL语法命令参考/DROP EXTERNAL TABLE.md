删除一个外部表定义。

## 概要

```sql
DROP EXTERNAL [WEB] TABLE [IF EXISTS] name [CASCADE | RESTRICT]
```

## 描述

DROP EXTERNAL TABLE 从数据库中删除一个存在的外部表定义。外部的数据资源和文件不会被删除。要执行这个命令用户必须是外部表的所有者。

## 参数

WEB
删除外部 Web 表的可选参数。

IF EXISTS
如果外部表存在，不会抛出异常。这种情况下会发出一个通知。

name
存在的外部表的名字（可选方案限定）。

CASCADE
自动删除依赖于外部表的对象（例如视图）。

RESTRICT
如果有对象依赖于外部表，则拒绝删除该外部表。这是默认的选项。

## 示例
删除叫 staging 的外部表，如果存在的话：

```sql
DROP EXTERNAL TABLE IF EXISTS staging;
```

## 兼容性

SQL 标准中没有 DROP EXTERNAL TABLE 语句。

## 另见

CREATE EXTERNAL TABLE
