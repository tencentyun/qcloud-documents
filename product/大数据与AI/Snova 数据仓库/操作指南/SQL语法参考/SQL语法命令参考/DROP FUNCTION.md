删除一个函数。

## 概要
```sql
DROP FUNCTION [IF EXISTS] name ( [ [argmode] [argname] argtype 
    [, ...] ] ) [CASCADE | RESTRICT]
```

## 描述
DROP FUNCTION 删除一个存在函数的定义。要执行这个命令该用户必须是该函数的拥有者。必须要指定参数类型，因为几个不同的函数可能存在同名，但其参数列表不同。

## 参数
IF EXISTS
如果函数不存在，不会抛出错误。这种情况下会发出通知。

name
存在函数的名称（可选方案限定）。

argmode
参数的模式：IN、OUT、INOUT 或 VARIADIC。如果省略，则默认是 IN。注意 DROP FUNCTION 实际上并不会注意 OUT 参数，因为仅需要输入参数就能决定函数的身份。索引列出 IN、INOUT 和 VARIADIC 参数即可。

argname
参数的名字。注意 DROP FUNCTION 实际上并不注意参数名字，因为仅需要参数数据类型就能决定函数的身份。

argtype
函数参数的数据类型（可选方案限定）如果有的话。

CASCADE
自动删除依赖于该函数的对象，例如操作符号。

RESTRICT
如果有任何对象依赖于该函数，则拒绝删除该函数，这是默认的。

## 示例
删除平方根函数：
```
DROP FUNCTION sqrt(integer);
```

## 兼容性
SQL 标准中定义了 DROP FUNCTION 语句，但是这和该命令不兼容。

## 另见
CREATE FUNCTION、ALTER FUNCTION
