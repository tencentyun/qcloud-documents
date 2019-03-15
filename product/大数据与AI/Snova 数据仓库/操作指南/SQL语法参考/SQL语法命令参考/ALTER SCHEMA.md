更改一个模式定义。

## 概要

```sql
ALTER SCHEMA name RENAME TO newname
 
ALTER SCHEMA name OWNER TO newowner
```

## 描述
ALTER SCHEMA更改一个模式定义。

用户必须拥有该模式才能去使用ALTER SCHEMA。要重命名一个模式，用户还必须拥有该数据库的CREATE特权。要更改拥有者，用户还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该数据库上的CREATE特权。注意超级用户自动拥有所有这些特权。

## 参数
name
现有模式的名称。

newname
该模式的新名称。新名称不能以pg_开头,因为这些名称被保留用于系统模式。

newowner
该模式的新的拥有者。

## 兼容性
没有ALTER SCHEMA语句在SQL标准中。

## 另见
CREATE SCHEMA、DROP SCHEMA
