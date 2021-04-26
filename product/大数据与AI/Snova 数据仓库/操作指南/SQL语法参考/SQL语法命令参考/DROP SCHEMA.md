移除一个 schema。

## 概要

```sql
DROP SCHEMA [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

## 描述
DROP SCHEMA 从数据库中移除方案。一个方案只能由其拥有者或一个超级用户删除。注意即使拥有者不拥有该方案中的某些对象，也能删除该方案（以及所有含有的对象）。

## 参数
IF EXISTS
如果该方案不存在则不会抛出一个错误，而是发出一个提示。

name
要移除方案的名称。

CASCADE
自动删除包含在该方案中的对象（表、函数等），然后删除所有依赖于那些对象的对象。

RESTRICT
如果该方案含有任何对象，则拒绝删除它。这是默认值。

## 示例
从数据库中移除一个名为 mystuff 的方案及其中所包含的对象：

```sql
DROP SCHEMA mystuff CASCADE;
```

## 兼容性
DROP SCHEMA 完全符合 SQL 标准，不过该标准只允许在每个命令中删除一个方案并且没有 IF EXISTS 选项。该选项是数据库的一个扩展。

## 另见
CREATE SCHEMA、ALTER SCHEMA
