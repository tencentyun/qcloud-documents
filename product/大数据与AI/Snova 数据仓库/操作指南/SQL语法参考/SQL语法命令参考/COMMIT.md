提交当前事务。

## 概要

```sql
COMMIT [WORK | TRANSACTION]
```

## 描述
COMMIT 提交当前事务。所有由该事务所作的更改会变得对他人可见并且被保证在崩溃发生时仍能持久。

## 参数

WORK
TRANSACTION
可选的关键词。它们没有效果。

## 注解
使用 ROLLBACK 中止一个事务。
当不在一个事务内时发出 COMMIT 不会产生危害，但是它会产生一个警告消息。

## 示例
要提交当前事务并且让所有更改持久化：

```sql
COMMIT;
```

## 兼容性
SQL 标准仅指定了两种形式：COMMIT 和 COMMIT WORK。除此之外，这个命令完全符合。

## 另见

BEGIN、END、START TRANSACTION、ROLLBACK
