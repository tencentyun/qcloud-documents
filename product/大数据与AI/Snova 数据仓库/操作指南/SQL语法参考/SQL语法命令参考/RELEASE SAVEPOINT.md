销毁一个之前定义的保存点。

## 概要
```sql
RELEASE [SAVEPOINT] savepoint_name
```

## 描述
RELEASE SAVEPOINT 销毁在当前事务中之前定义的一个保存点。

销毁一个保存点会使得它不能再作为一个回滚点，但是它没有其他用户可见的行为。它不会撤销在该保存点被建立之后执行命令的效果（要这样做，可参见**ROLLBACK TO SAVEPOINT**）。当不再需要一个保存点时销毁它允许系统在事务结束之前回收一些资源。

RELEASE SAVEPOINT 也会销毁所有在该保存点建立之后建立的保存点。

## 参数
savepoint_name
要销毁的保存点的名称。

## 示例
建立并销毁一个保存点：

```sql
BEGIN;
    INSERT INTO table1 VALUES (3);
    SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (4);
    RELEASE SAVEPOINT my_savepoint;
COMMIT;
```

上述事务将插入3和4。

## 兼容性
该命令符合 SQL 标准。标准指定了关键词 SAVEPOINT 是强制需要的，但是在数据库中允许将其忽略。

## 另见
BEGIN、SAVEPOINT、ROLLBACK TO SAVEPOINT、COMMIT
