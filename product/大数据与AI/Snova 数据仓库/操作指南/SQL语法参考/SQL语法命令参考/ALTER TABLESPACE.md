更改一个表空间的定义。

## 概要

```sql
ALTER TABLESPACE name RENAME TO newname
 
ALTER TABLESPACE name OWNER TO newowner
```

## 描述
ALTER TABLESPACE 可用于更改一个表空间的定义。

要使用 ALTER TABLESPACE，用户必须拥有该表空间。要修改拥有者，用户还必须是新拥有角色的直接或者间接成员（超级用户自动拥有这些特权）。

## 参数

name
一个现有表空间的名称。

newname
新的表空间的名称。新的表空间名称不能以 pg_ 或 gp_ 开头（这类名称保留用于系统表空间）。

newowner
该表空间的新拥有者。

## 示例

重命名表空间 index_space 为 fast_raid：

```sql
ALTER TABLESPACE index_space RENAME TO fast_raid;
```

更改表空间 index_space 的所有者：

```sql
ALTER TABLESPACE index_space OWNER TO mary;
```

## 兼容性

在 SQL 标准中没有 ALTER TABLESPACE 语句。

## 另见

CREATE TABLESPACE、DROP TABLESPACE
