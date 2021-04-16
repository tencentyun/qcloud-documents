移除一个数据库角色。

## 概要
```sql
DROP ROLE [IF EXISTS] name [, ...]
```

## 描述
DROP ROLE 移除指定的角色。要删除一个超级用户角色，用户必须自己是一个超级用户。要删除一个非超级用户角色，用户必须要有 CREATEROLE 权限。

如果一个角色仍然被集簇中的任何一个数据库引用，它就不能被移除。如果尝试移除将会抛出一个错误。在删除角色之前，用户必须删除（或者重新授予所有权）它所拥有的所有对象并且收回该已经授予给该角色的在其他对象上的特权。REASSIGN OWNED 和 DROP OWNED 命令可以用于这个目的。

不过，没有必要移除涉及该角色的角色成员关系；DROP ROLE 会自动收回目标角色在其他角色中的成员关系，以及其他角色在目标角色中的成员关系。其他角色不会被删除也不被影响。

## 参数
IF EXISTS
如果该角色不存在则不要抛出一个错误，而是发出一个提示。

name
要移除的角色的名称。

## 示例
移除名为 sally 和 bob 的角色：
```sql
DROP ROLE sally, bob;
```

## 兼容性
SQL 标准定义了 DROP ROLE，但是它只允许一次删除一个角色并且它指定了和数据库不同的特权需求。

## 另见
REASSIGN OWNED、DROP OWNED、CREATE ROLE、ALTER ROLE、SET ROLE
