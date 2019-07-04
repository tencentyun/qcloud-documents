回滚当前事务到一个保存点。

## 概要
```sql
ROLLBACK [WORK | TRANSACTION] TO [SAVEPOINT] savepoint_name
```

## 描述
回滚在该保存点被建立之后执行的所有命令。该保存点保持有效并且可以在以后再次回滚到它（如果需要）。

ROLLBACK TO SAVEPOINT 隐式地销毁在所提及的保存点之后建立的所有保存点。

## 参数

WORK
TRANSACTION
可选关键词。他们没有任何影响。

savepoint_name
要回滚到的保存点名称。

## 注解
使用 RELEASE SAVEPOINT 销毁一个保存点而丢弃在它建立之后被执行的命令的效果。

指定一个没有被建立的保存点是一种错误。

相对于保存点，游标有一点非事务的行为。在保存点被回滚时，任何在该保存点内被打开的游标将会被关闭。如果一个先前打开的游标在一个保存点内被 FETCH 命令影响，而该保存点后来又被回滚，那么该游标将保持 FETCH 使它指向的位置（即由 FETCH 导致的游标动作不会被回滚）。
回滚也不能撤销关闭一个游标。如果一个游标的执行导致事务中止，它会被置于一种不能被执行的状态，这样当事务被用 ROLLBACK TO SAVEPOINT 恢复后，该游标也不再能被使用。

## 示例
要撤销在 my_savepoint 建立后执行的命令的效果：
```sql
ROLLBACK TO SAVEPOINT my_savepoint;
```

游标位置不会受保存点回滚的影响：

```sql
BEGIN;
DECLARE foo CURSOR FOR SELECT 1 UNION SELECT 2;
SAVEPOINT foo;
FETCH 1 FROM foo;
column 
----------
        1
ROLLBACK TO SAVEPOINT foo;
FETCH 1 FROM foo;
column 
----------
        2
COMMIT;
```

## 兼容性
SQL 标准指定了关键词 SAVEPOINT 是必需的，但是在数据库（和Oracle）中允许该关键词被省略。SQL 只允许 WORK 而不是 TRANSACTION 作为一个 ROLLBACK 之后的噪声次。
另外，SQL 有一个可选的子句 AND [NO] CHAIN，当前在数据库中是不支持的。 其他方面，该命令符合 SQL 标准。

## 另见
BEGIN、COMMIT、SAVEPOINT、RELEASE SAVEPOINT、ROLLBACK
