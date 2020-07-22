设置置当前会话的会话用户标识符和当前用户标识符。

## 概要

```sql
SET [SESSION | LOCAL] SESSION AUTHORIZATION rolename
 
SET [SESSION | LOCAL] SESSION AUTHORIZATION DEFAULT
 
RESET SESSION AUTHORIZATION
```

## 描述

这个命令把当前 SQL 会话的会话用户标识符和当前用户标识符设置为 rolename。用户名可以被写成一个标识符或者一个字符串。例如，可以使用这个命令临时成为一个无特权用户并且稍后切换回来成为一个超级用户。

会话用户标识符初始时被设置为客户端提供的（可能已认证的）用户名。 当前用户标识符通常等于会话用户标识符，但是可能在 setuid 函数和类似的机制的环境中发生临时更改。也可以使用 **SET ROLE** 更改它。当前用户标识符与权限检查相关。

会话用户标识符只能在初始会话用户已认证用户具有超级用户特权时被更改。否则，只有该命令指定已认证用户名时才会被接受。

DEFAULT 和 RESET 形式把会话用户标识符和当前用户标识符重置为初始的已认证用户名。这些形式可以由任何用户执行。

## 参数

SESSION
指明命令作用于当前会话。这是默认值。

LOCAL
指明命令只作用于当前事务中。在 COMMIT 或者 ROLLBACK 之后，会话级设置继续恢复影响。**如果该命令执行在事务外时，SET LOCAL 没有任何的影响**。

rolename
假定的角色名。

NONE
RESET
重置当前角色（用户）标识符成为当前会话角色（用户）标识符（即用来登录的角色）。

## 示例
```sql
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter        | peter
 
SET SESSION AUTHORIZATION 'paul';
 
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 paul         | paul
```

## 兼容性
SQL 标准允许一些其他表达式出现在文本 rolename 的位置上，但是实际上这些选项并不重要。数据库允许标识符语法（rolename），而 SQL 标准不允许。SQL 不允许在事务中使用这个命令，而数据库并不做此限制。和 RESET 语法一样，SESSION 和 LOCAL 修饰符是数据库的扩展。

## 另见
SET ROLE
