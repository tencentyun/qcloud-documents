删除一个数据库。

## 概要
```sql
DROP DATABASE [IF EXISTS] name
```

## 描述
>!DROP DATABASE 不能被撤销，请小心使用。

DROP DATABASE 删除了一个数据库。它删除了数据的目录条目并且删除了包含该数据的目录。它只能被拥有该数据库的用户执行。另外，当用户或者是其他用户正连接到该数据库时，是不能执行删除该数据库操作的（连接到 postgres 或其他数据库来发出此命令）。

## 参数
IF EXISTS
如果数据库不存在不会抛出异常。这种情况下发出通知。

name
要删除数据库的名字。

## 注意
DROP DATABASE 不能在事务块中执行。

当连接到目标数据库时，不能执行该命令。因此，使用程序 dropdb 来替代可能更方便一点。该命令是在此命令上的封装。

## 示例
删除叫 testdb 的数据库：
```sql
DROP DATABASE testdb;
```

## 兼容性
SQL 标准中没有 DROP DATABASE 语句。

## 另见
ALTER DATABASE、CREATE DATABASE
