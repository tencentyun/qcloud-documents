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
CREATE DATABASE创建一个新的数据库。要创建一个新的数据库，用户必须是超级用户或者有CREATEDB特权。

默认情况下，创建者即为新数据库的所有者。超级用户可以使用其他用户创建数据库通过OWNER子句。他们甚至可以创建没有特殊权限的用户拥有的数据库。有CREATEDB特权的非超级用户只能创建自己拥有的数据库。

默认情况下，将通过克隆标准系统数据库创建新数据库template1。可以通过写指定不同的模板TEMPLATE名称。特别是，通过写TEMPLATE template0，用户可以创建一个仅包含由Database预定义的标准对象的干净数据库。将对用户希望避免复制内容添加到template1的任何安装对象中非常有用。

## 参数
name
要创建的数据库的名称。

dbowner
将拥有新数据库的数据库用户的名称，或DEFAULT 使用默认的所有者（执行该命令的用户）。

默认
要创建新数据库的模板的名称，或默认使用默认模板（template1）。

encoding
在新数据库中使用的字符集编码。指定一个字符串常量（例如：'SQL_ASCII'），一个整数编码号，或DEFAULT使用默认编码。

tablespace
将与新数据库相关联的表空间的名称，或DEFAULT使用模板数据库的表空间。此表空间将是用于在此数据库中创建的对象的默认表空间。

connlimit
最大并发连接数可以使用。缺省值-1表示没有限制。

## 注解
CREATE DATABASE不能在事务块内执行。

当用户通过指定其名称作为模板来复制数据库时，在复制数据库时，不会将其他会话连接到模板数据库。到模板数据库的新连接被锁定，直到CREATE DATABASE完成。

该CONNECTION LIMIT没有对超级用户执行。

## 示例
要创建一个新的数据库：

```sql
CREATE DATABASE gpdb;
```

创建数据库sales由用户salesapp拥有，默认表空间为salesspace：

```sql
CREATE DATABASE sales OWNER salesapp TABLESPACE salesspace;
```

创建数据库music支持ISO-8859-1字符集：

```sql
CREATE DATABASE music ENCODING 'LATIN1';
```

## 兼容性

SQL标准中没有CREATE DATABASE语句。数据库等同于目录，其创建是由实现定义的。

## 另见

ALTER DATABASE、DROP DATABASE
