#### SET ROLE

设置当前会话的当前用户标识符。

##### 概要

```sql
SET [SESSION | LOCAL] ROLE rolename
 
SET [SESSION | LOCAL] ROLE NONE
 
RESET ROLE
```

##### 描述

这个命令把当前SQL会话的当前用户标识符设置为rolename。角色名可以写成一个标识符或者一个字符串。在SET ROLE后，对SQL命令的权限检查时就 好像该角色就是原先登录的角色一样。

当前会话用户必须是指定的角色rolename的一个成员。如果会话用户是一个超级用户，则可以选择任何角色。

NONE和RESET形式把当前用户标识符重置为当前会话用户标识符。这些形式可以由任何用户执行。

##### 参数

SESSION

指明命令作用于当前会话。这是默认值。

LOCAL

指明命令只作用于当前事务中。在COMMIT或者ROLLBACK之后，会话级设置继续恢复影响。注意SET LOCAL好像没有任何的影响，如果该命令执行在事务外时。

rolename

在会话中用来进行权限检查的有角色名。

NONE

RESET

重置当前角色（用户）标识符成为当前会话角色（用户）标识符（即用来登录的角色）。

##### 注解

使用这个命令可以增加特权或者限制特权。如果会话用户角色具有 INHERITS属性，则它会自动具有它能SET ROLE到的所有角色的全部特权。在这种情况下。SET ROLE 实际会删除所有直接分配给会话用户的特 权以及分配给会话用户作为其成员的其他角色的特权，只留下所提及 角色可用的特权。换句话说，如果会话用户没有NOINHERITS属性， SET ROLE 会删除直接分配给会话用户的特权而得到所提及角色可用的特权。

特别地，当一个超级用户选择SET ROLE 到一个非超级用户角色时，它们会丢失其超级用户特权。

SET ROLE的效果堪比SET SESSION AUTHORIZATION，但是涉及的特权检查完全不同。 还有，SET SESSION AUTHORIZATION决定后来的SET ROLE 命令可以使用哪些角色，不过用SET ROLE更改角色并不会改变后续SET ROLE能够使用的角色集。

##### 示例

```sql
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter        | peter
 
SET ROLE 'paul';
 
SELECT SESSION_USER, CURRENT_USER;
 session_user | current_user 
--------------+--------------
 peter        | paul
```

##### 兼容性

数据库允许标识符语法（rolename），而SQL标准要求 角色名被写成字符串。 SQL 不允许在事务中使用这个命令；但数据库并不做此限制。和RESET语法一样，SESSION和LOCAL 修饰符是数据库的扩展。

##### 另见

SET SESSION AUTHORIZATION