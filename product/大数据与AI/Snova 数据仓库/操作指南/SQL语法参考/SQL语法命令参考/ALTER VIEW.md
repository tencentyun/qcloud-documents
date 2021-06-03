更改一个视图的定义。

## 概要
```sql
ALTER VIEW name RENAME TO newname
```

## 描述
ALTER VIEW 更改一个视图的定义。唯一当前可用的功能是重命名视图。要执行此命令用户必须是视图的拥有者。

## 参数
name
一个现有文件空间的名称（可以是限定模式）。

newname
视图的新名称。

## 注解
一些 ALTER TABLE 的变体可以很好的用于视图，例如重命名视图时可以使用 ALTER TABLE RENAME。但是要更改视图的所有者或者模式，目前用户必须通过使用 ALTER TABLE。

## 示例
把视图 myview 重命名为 newview：
```sql
ALTER VIEW myview RENAME TO newview;
```
更改表空间 myfs 的所有者：
```sql
ALTER FILESPACE myfs OWNER TO dba;
```

## 兼容性
ALTER VIEW 是一种数据库的 SQL 标准扩展。

## 另见
CREATE VIEW、DROP VIEW
