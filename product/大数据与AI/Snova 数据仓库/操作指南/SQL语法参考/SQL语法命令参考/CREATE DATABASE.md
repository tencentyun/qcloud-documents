创建一个新的数据库。

## 概要

```sql
CREATE DATABASE name [ [WITH] [OWNER [=] dbowner]
                     [TEMPLATE [=] template]
                     [ENCODING [=] encoding]
                     [TABLESPACE [=] tablespace]
                     [CONNECTION LIMIT [=] connlimit ] ]
```

## 描述
CREATE DATABASE 创建一个新的数据库。要创建一个新的数据库，用户必须是超级用户或者有 CREATEDB 特权。

默认情况下，创建者即为新数据库的所有者。超级用户可以使用其他用户创建数据库通过 OWNER 子句。他们甚至可以创建没有特殊权限的用户拥有的数据库。有 CREATEDB 特权的非超级用户只能创建自己拥有的数据库。

默认情况下，将通过克隆标准系统数据库创建新数据库 template1。可以通过写指定不同的模板 TEMPLATE 名称。特别是，通过写 TEMPLATE template0，用户可以创建一个仅包含由 Database 预定义的标准对象的干净数据库。将对用户希望避免复制内容添加到 template1 的任何安装对象中非常有用。

## 参数
name
要创建的数据库的名称。

dbowner
将拥有新数据库的数据库用户的名称，或 DEFAULT 使用默认的所有者（执行该命令的用户）。

默认模板
要创建新数据库的模板的名称，或默认使用默认模板（template1）。

encoding
在新数据库中使用的字符集编码。指定一个字符串常量（例如：'SQL_ASCII'），一个整数编码号，或 DEFAULT 使用默认编码。

tablespace
将与新数据库相关联的表空间的名称，或 DEFAULT 使用模板数据库的表空间。此表空间将是用于在此数据库中创建的对象的默认表空间。

connlimit
最大并发连接数可以使用。缺省值-1表示没有限制。

## 注解
CREATE DATABASE 不能在事务块内执行。

当用户通过指定其名称作为模板来复制数据库时，在复制数据库时，不会将其他会话连接到模板数据库。到模板数据库的新连接被锁定，直到 CREATE DATABASE 完成。

该 CONNECTION LIMIT 没有对超级用户执行。

## 示例
要创建一个新的数据库：

```sql
CREATE DATABASE gpdb;
```

创建数据库 sales 由用户 salesapp 拥有，默认表空间为 salesspace：

```sql
CREATE DATABASE sales OWNER salesapp TABLESPACE salesspace;
```

创建数据库 music 支持 ISO-8859-1 字符集：

```sql
CREATE DATABASE music ENCODING 'LATIN1';
```

## 兼容性

SQL 标准中没有 CREATE DATABASE 语句。数据库等同于目录，其创建是由实现定义的。

## 另见

ALTER DATABASE、DROP DATABASE
