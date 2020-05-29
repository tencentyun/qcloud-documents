删除一个文件空间。

## 概要

```sql
DROP FILESPACE [IF EXISTS] filespacename
```

## 描述
DROP FILESPACE 从数据库中删除一个文件空间定义和它的系统生成的数据目录。

文件空间只能被它的拥有者或超级用户删除。该文件空间必须清空所有的表空间对象之后才能被删除。可能情况是其他数据库的表空间还在使用该文件空间，即使当前数据库中没有使用该文件空间的表空间。

## 参数
IF EXISTS
如果文件空间不存在，也不会抛出错误，这种情况下会发出通知。

tablespacename
要删除的文件空间的名字。

## 示例
删除表空间 myfs：

```sql
DROP FILESPACE myfs;
```

## 兼容性

SQL 标准中或者 PostgreSQL 中没有 DROP FILESPACE 语句。

## 另见

ALTER FILESPACE、DROP TABLESPACE
