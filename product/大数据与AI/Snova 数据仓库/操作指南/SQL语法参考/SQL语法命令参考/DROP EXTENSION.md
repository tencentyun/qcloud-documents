从数据库中删除一个扩展。

## 概要

```sql
DROP EXTENSION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## 描述

DROP EXTENSION 从数据库中移除扩展。删除扩张也会导致其组件对象也被删除。

注意：用来创建扩展所需的支持扩展文件不会被删除。这些文件必须从数据库主机中手动删除。

用户必须拥有该扩展才能使用 DROP EXTENSION。

如果该扩展的任何对象正在数据库中使用，则该命令失败。例如，如果一个表是用扩展类型的列定义的，则要添加 CASCADE 选项来强制删除这些依赖对象。

重要提示： 在发出 DROP EXTENSION 带有 CASCADE 关键词的命令时，用户必须明白所有依赖于该扩展的对象，以避免意外的后果。

## 参数
IF EXISTS
如果扩展不存在，不会抛出异常。会发出通知。

name
安装的扩展的名字。

CASCADE
自动删除依赖于该扩展的对象，并且依次删除依赖于这些对象的所有对象。

RESTRICT
如果有对象依赖于该扩展，则拒绝删除该扩展，除了扩展成员对象。这是默认的。

## 兼容性
DROP EXTENSION 是数据库扩展。

## 另见
CREATE EXTENSION、ALTER EXTENSION
