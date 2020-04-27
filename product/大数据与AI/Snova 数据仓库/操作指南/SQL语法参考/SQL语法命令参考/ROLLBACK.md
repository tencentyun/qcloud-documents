中止当前事务。

## 概要
```sql
ROLLBACK [WORK | TRANSACTION]
```

## 描述
ROLLBACK 回滚当前事务并且导致该事务所作的所有更新都被丢弃。

## 参数
WORK
TRANSACTION
可选关键词。它们没有任何影响。

## 注解
使用 COMMIT 可成功的结束一个事务。

在一个事务块之外发出 ROLLBACK 会发出一个警告并且不会有任何效果。

## 示例
丢弃当前事务所做的所有修改：

```sql
ROLLBACK;
```

## 兼容性
SQL 标准中只指定了两种形式 ROLLBACK 和 ROLLBACK WORK，其他方面，该命令完全符合 SQL 标准。

## 另见
BEGIN、COMMIT、SAVEPOINT、ROLLBACK TO SAVEPOINT
