在当前事务中定义一个新的保存点。

## 概要

```sql
SAVEPOINT savepoint_name
```

## 描述
SAVEPOINT 在当前事务中建立一个新保存点。

保存点是事务内的一种特殊标记，它允许所有在它被建立之后执行的命令被回滚，把该事务的状态恢复到它处于保存点时的样子。

## 参数
savepoint_name
新保存点的名字。

## 注解
使用 **ROLLBACK TO SAVEPOINT** 回滚到一个保存点。 
使用**RELEASE SAVEPOINT**销毁一个保存点，但保持在它被建立之后执行的命令的效果。

保存点只能在一个事务块内建立。可以在一个事务内定义多个保存点。

## 示例
要建立一个保存点并且后来撤销在它建立之后执行的所有命令的效果：

```sql
BEGIN;
    INSERT INTO table1 VALUES (1);
    SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (2);
    ROLLBACK TO SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (3);
COMMIT;
```

上面的事务将插入值1和3，但不会插入2。

要建立并且稍后销毁一个保存点：

```sql
BEGIN;
    INSERT INTO table1 VALUES (3);
    SAVEPOINT my_savepoint;
    INSERT INTO table1 VALUES (4);
    RELEASE SAVEPOINT my_savepoint;
COMMIT;
```

上面的事务将插入3和4。

## 兼容性
当建立另一个同名保存点时，SQL 要求之前的那个保存点自动被销毁。在数据库中，旧的保存点会被保留，不过在进行回滚或释放时只能使用最近的那一个（释放较新的保存点将会导致较旧的保存点再次变得可以被 ROLLBACK TO SAVEPOINT 和 RELEASE SAVEPOINT 访问）。在其他方面，SAVEPOINT 完全符合 SQL。

## 另见
BEGIN、COMMIT、ROLLBACK、RELEASE SAVEPOINT、ROLLBACK TO SAVEPOINT
