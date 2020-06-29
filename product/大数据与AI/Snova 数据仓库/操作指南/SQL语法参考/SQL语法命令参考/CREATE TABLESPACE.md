定义一个新的表空间。

## 概要

```sql
CREATE TABLESPACE tablespace_name [OWNER username] 
       FILESPACE filespace_name
```

## 描述

CREATE TABLESPACE 为用户的数据库系统注册一个新的表空间。该表空间的名字必须和系统中已存在其他任何表空间不同名。

一个表空间允许超级用户在文件系统上定义其他的位置，该位置中的驻有包含数据库对象（表和索引）在内的数据文件。

有适当权利的用户可以传递一个表空间名到 CREATE DATABASE，CREATE TABLE 或 CREATE INDEX 中来使这些对象的数据文件存储在指定的表空间中。

在数据库中，必须对 Master、每个 Segment、每个 Segment 镜像都有一个定义好的文件系统，为的就是让表空间在整个系统中有位置来存储它的对象。该文件系统位置的集合定义在文件空间对象中。在用户创建一个表空间之前，必须定义一个文件空间。参阅 gpfilespace 在“数据库实用指南”获取更多信息。

## 参数

tablespacename
要创建表空间名字，该名字不能以 pg_ 或 gp_ 开头，因为这些名字是为系统表空间预留的。

OWNER username
拥有该表空间用户的名字。如果省略，默认为执行该命令的用户。只有超级用户可以创建表空间，但是他们能分配表空间的所属权给非超级用户。

FILESPACE
数据库表空间的名字，该表空间由 gpfilespace 管理实用程序所定义。

## 注意
用户必须首先创建一个由表空间使用的文件空间。请参阅“数据库工具指南”中的 gpfilespace 以获取更多信息。

表空间仅在支持符号链接的系统上支持。

CREATE TABLESPACE 不能在事务块中执行。

## 示例
通过指定相应的要用文件空间，创建一个新的表空间。

```sql
CREATE TABLESPACE mytblspace FILESPACE myfilespace;
```

## 兼容性

CREATE TABLESPACE 是数据库扩展。

## 另见

CREATE DATABASE、CREATE TABLE、CREATE INDEX、DROP TABLESPACE、ALTER TABLESPACE

