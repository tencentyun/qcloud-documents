定义一个新的方案。

## 概要

```sql
CREATE SCHEMA schema_name [AUTHORIZATION username] 
   [schema_element [ ... ]]
 
CREATE SCHEMA AUTHORIZATION rolename [schema_element [ ... ]]
```

## 描述

CREATE SCHEMA 将新的方案输入到当前的数据库中。方案名称必须与当前数据库中现有的名称不同。

方案本质上就是一个命名空间：它包含命名对象（表、数据类型、函数和操作符），这些名字可能会与该方案中其他对象的名字重叠。命名对象通过将其名称以方案名称作为其前缀进行限定，或者通过设置包含所需方案的搜索路径进行访问。指定非限定对象名称的 CREATE 命令在当前方案中创建对象（搜索路径前面的对象，可以使用函数 current_schema 确定）。

可选择地是，CREATE SCHEMA 可以包含子命令来在新方案中创建对象。这些子命令本质上和创建方案之后发出的单独命令相同，除了如果使用 AUTHORIZATION 子句，所有创建的对象由该角色有用。

## 参数

schema_name
创建方案的名称，如果省略，则用户名被用作方案名。该名字不能以 pg_ 开头，因为这些名字是为系统目录方案保存的。

rolename
拥有该方案的角色的名称。如果省略，默认为执行该命令的角色。只有超级用户可以创建属于其他角色的方案，除了他们自己。

schema_element
定义在方案中创建对象的 SQL 语句。目前只有 CREATE TABLE、CREATE VIEW、CREATE INDEX、CREATE SEQUENCE、CREATE TRIGGER 和 GRANT 被认作为 CREATE SCHEMA 中的子句。其他对象可能在方案创建之后以单独的命令来创建。

注意：数据库不支持触发器。

## 注意
要创建方案，该调用用户必须要有当前数据库的 CREATE 权限或者是超级用户。

## 示例
创建一个方案：

```sql
CREATE SCHEMA myschema;
```

为角色 joe 创建一个方案（该方案也叫 joe）：

```sql
CREATE SCHEMA AUTHORIZATION joe;
```

## 兼容性

SQL 标准允许 DEFAULT CHARACTER SET 子句在 CREATE SCHEMA 中，还有比现在支持的更多的子命令类型。

SQL 标准指定了在 CREATE SCHEMA 中的子命令可以出现在任何顺序。目前数据库实现不能处理子命令中所有转发引用的问题。有时，有必要重新排序子命令，以避免转发引用。

根据 SQL 标准，方案的拥有者通常拥有里面的所有对象。数据库允许对象包含不是方案对象本身拥有的对象。这当且仅当方案拥有者给其他人授权了 CREATE 权限。

## 另见

ALTER SCHEMA、DROP SCHEMA

 
