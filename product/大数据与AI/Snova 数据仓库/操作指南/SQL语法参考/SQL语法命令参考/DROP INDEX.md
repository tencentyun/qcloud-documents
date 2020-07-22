删除一个索引。

## 概要

```sql
DROP INDEX [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

## 描述
DROP INDEX 从数据库系统上删除一个存在的索引。要执行这个命令用户必须是索引的拥有者。

## 参数

IF EXISTS
如果索引不存在，不会抛出错误。这种情况下会发出通知。

name
存在索引的名字（可选方案限定）。

CASCADE
自动删除依赖于该索引的对象。

RESTRICT
如果有任何对象依赖于该索引，则拒绝删除该对象（默认）。

## 示例

删除索引 title_idx：

```sql
DROP INDEX title_idx;
```

## 兼容性
DROP INDEX 是数据库语言扩展。SQL 标准中没有该索引的规定。

## 另见
ALTER INDEX、CREATE INDEX、REINDEX
