移除一个表空间。

## 概要

```sql
DROP TABLESPACE [IF EXISTS] tablespacename
```

## 描述
DROP TABLESPACE 从系统中移除一个表空间。

一个表空间只能被其拥有者或超级用户删除。在一个表空间能被删除前，其中必须没有任何数据库对象。即使当前数据库中没有对象正在使用该表空间，也可能有其他数据库的对象存在于其中。

## 参数
IF EXISTS
如果该表空间不存在则不会抛出一个错误，而是发出一个提示。

tablespacename
要移除的表空间的名称。

## 示例
移除名为 mystuff 的表空间：

```sql
DROP TABLESPACE mystuff;
```

## 兼容性
DROP TABLESPACE 是数据库的一个扩展。

## 另见
CREATE TABLESPACE、ALTER TABLESPACE
