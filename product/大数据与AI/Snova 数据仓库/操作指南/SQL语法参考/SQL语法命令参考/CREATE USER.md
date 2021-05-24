定义一个新的默认带有 LOGIN 权限的数据库角色。

## 概要
```sql
CREATE USER name [ [WITH] option [ ... ] ]
```
该 option 可以是：
```sql
      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | CREATEUSER | NOCREATEUSER
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
    | VALID UNTIL 'timestamp' 
    | IN ROLE rolename [, ...]
    | IN GROUP rolename [, ...]
    | ROLE rolename [, ...]
    | ADMIN rolename [, ...]
    | USER rolename [, ...]
    | SYSID uid    | RESOURCE QUEUE queue_name
```

## 描述
作为数据库2.2发行版，CREATE USER 已经由 **CREATE ROLE** 所替代，尽管为了向后兼容，它仍然被接受实用。

在 CREATE ROLE 和 CREATE USER 之间仅有的区别是 LOGIN 权限默认和 CREATE USER 一起创建，然而 NOLOGIN 权限默认和 CREATE ROLE 一起创建。

## 兼容性
在 SQL 标准中没有 CREATE USER 语句。

## 另见
CREATE ROLE
