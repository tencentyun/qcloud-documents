更改一种过程语言的定义。

## 概要
```sql
ALTER LANGUAGE name RENAME TO newname
ALTER LANGUAGE name OWNER TO new_owner
```

## 描述
ALTER LANGUAGE 更改特定数据库的过程语言的定义。唯一的功能是重命名该语言或者为它赋予一个新的拥有者。用户必须是超级用户或语言的所有者才能使用 ALTER LANGUAGE。

## 参数
name
一种语言的名称。

newname
该语言的新名称。

new_owner
该语言的新的所有者。

## 兼容性
在标准 SQL 中没有 ALTER LANGUAGE 语法。

## 另见
CREATE LANGUAGE、DROP LANGUAGE
