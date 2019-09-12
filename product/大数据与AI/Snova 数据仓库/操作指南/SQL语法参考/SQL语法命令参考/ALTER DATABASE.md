更改数据库的属性。

## 概要

```sql
ALTER DATABASE name [ WITH CONNECTION LIMIT connlimit ]
 
ALTER DATABASE name SET parameter { TO | = } { value | DEFAULT }
 
ALTER DATABASE name RESET parameter
 
ALTER DATABASE name RENAME TO newname
 
ALTER DATABASE name OWNER TO new_owner
```

## 描述

ALTER DATABASE 更改一个数据库的属性。

第一种形式更改数据库的允许连接限制。只有数据库所有者或超级用户可以更改此设置。

第二种和第三种形式更改了数据库的配置参数的会话默认值。每当随后在该数据库中启动新会话时，指定的值将成为会话默认值。修改会话连接中的数据库默认值。只有数据库所有者或超级用户可以更改数据库的会话默认值。某些参数不能以这种方式设置，或只能由超级用户设置。

第四种形式更改数据库的名称。只有数据库所有者或超级用户可以重命名数据库；非超级用户也必须具有 CREATEDB 特权。用户不能重命名，需要首先切换到其他数据库。

第五种形式更改数据库的所有者。要更改所有者，用户必须拥有数据库，并且也是新拥有角色的直接或间接成员，并且必须具有 CREATEDB 特权。
>!超级用户自动拥有所有这些权限。

## 参数
name
要更改其属性的数据库的名称。

connlimit
最大并发连接数可能。缺省值-1表示没有限制。

parameter value
将指定配置参数的数据库的会话默认值设置为给定值。如果值是 DEFAULT 或者等效使用 RESET 则删除数据库特定的设置，因此系统范围的默认设置将在新会话中继承。使用 RESET ALL 清除所有特定于数据库的设置。 

newname
数据库的新名称。

new_owner
数据库的新所有者。

## 示例
设置默认方案的搜索路径为 mydatabase 数据库：

```sql
ALTER DATABASE mydatabase SET search_path TO myschema, 
public, pg_catalog;
```

## 注意
还可以为特定角色（用户）而不是数据库设置配置参数会话默认值。如果存在冲突，角色特定的设置将覆盖数据库特定的设置。参见 ALTER ROLE。

## 兼容性
ALTER DATABASE 语句是一个数据库的扩展。

## 另见
CREATE DATABASE、DROP DATABASE、SET
