删除一个程序语言。

## 概要
```sql
DROP [PROCEDURAL] LANGUAGE [IF EXISTS] name [CASCADE | RESTRICT]
```

## 描述
DROP LANGUAGE 会删除之前注册程序语言的定义。用户必须是超级用户或者是该语言的拥有者才能删除该语言。

## 参数
PROCEDURAL
可选关键字，没有效果。

IF EXISTS
如果该语言不存在，不会抛出错误。此种情况下发出通知。

name
存在的程序语言的名字。为了向后兼容，该名字必须要用单引号括起来。

CASCADE
自动删除依赖该语言的对象（例如用该语言写的函数）。

RESTRICT
如果有任何对象依赖于该语言，则拒绝删除该语言。这是默认的。

## 示例
删除程序语言 plsample：
```sql
DROP LANGUAGE plsample;
```

## 兼容性
SQL 标准中没有 DROP LANGUAGE 语句。

## 另见
ALTER LANGUAGE、CREATE LANGUAGE
