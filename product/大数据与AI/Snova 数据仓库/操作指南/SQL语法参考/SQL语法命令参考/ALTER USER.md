更改数据库用户（角色）的定义。

## 概要

```sql
ALTER USER name RENAME TO newname
 
ALTER USER name SET config_parameter {TO | =} {value | DEFAULT}
 
ALTER USER name RESET config_parameter
 
ALTER USER name [ [WITH] option [ ... ] ]
```

其中option can be：

```sql
      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | CREATEUSER | NOCREATEUSER
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
    | VALID UNTIL 'timestamp'
```

## 描述
ALTER USER是一个已弃用的命令，但由于历史原因仍然被接受，它是ALTER ROLE的别名。参见ALTER ROLE获取更多信息。

## 兼容性
ALTER USER语句是一个数据库扩展。SQL标准中使用用户的定义来实现。

## 另见
ALTER ROLE
