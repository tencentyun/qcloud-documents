移除一个重写规则。

## 概要

```sql
DROP RULE [IF EXISTS] name ON relation [CASCADE | RESTRICT]
```

## 描述
DROP RULE 删除一个表或视图相关的重写规则。

## 参数
IF EXISTS
如果该规则不存在则不会抛出一个错误，而是发出一个提示。

name
要删除的规则的名称。

relation
该规则适用的表或视图的名称（可以是方案限定的）。

CASCADE
自动删除依赖于该规则的对象，然后删除所有依赖于那些对象的对象。

RESTRICT
如果有任何对象依赖于该规则，则拒绝删除它。这是默认值。

## 示例
移除一个在表 sales 上名为 sales_2006 的重写规则：

```sql
DROP RULE sales_2006 ON sales;
```

## 兼容性
DROP RULE 不是 SQL 标准中的语句。

## 另见
CREATE RULE

