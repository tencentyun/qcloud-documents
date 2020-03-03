移除一个视图。

## 概要

```
DROP VIEW [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

## 描述
DROP VIEW 移除一个现有的视图。只有一个视图的所有者才能移除它。

## 参数
IF EXISTS
如果该视图不存在则不会抛出一个错误，而是发出一个提示。

name
要移除的视图的名称（可以是方案限定的）。

CASCADE
自动删除依赖于该视图的对象（例如其他视图），然后删除所有依赖于那些对象的对象。

RESTRICT
如果有任何对象依赖于该视图，则拒绝删除它。这是默认值。

## 示例
移除一个名为 topten 的视图：

```
DROP VIEW topten;
```

## 兼容性
DROP VIEW 这个命令符合 SQL 标准，不过该标准只允许在每个命令中删除一个视图，并且没有 IF EXISTS 选项。该选项是数据库的一个扩展。

## 另见
CREATE VIEW
