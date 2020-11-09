定位一个游标。

## 概要

```sql
MOVE [ forward_direction {FROM | IN} ] cursorname
```

其中 forward_direction 可以为空或者下列之一：

```sql
    NEXT
    FIRST
    LAST
    ABSOLUTE count
    RELATIVE count
    count
    ALL
    FORWARD
    FORWARD count
    FORWARD ALL
```

## 描述
MOVE 重新定位一个游标而不检索任何数据。 MOVE 的工作完全像 FETCH 命令，但是它只定位游标并且不返回行。

>!在数据库中向后移动一个游标是不可能的，因为在数据库中不支持滚动游标。只能够用 MOVE 向前移动游标位置。

**输出**
成功完成时，MOVE 命令返回的命令标签形式是：
```sql
MOVE count
```
count 是一个具有同样参数的 FETCH 命令会返回的行数（可能为零）。

## 参数
forward_direction
见 FETCH 获取更多信息。

cursorname
一个打开的游标名称。

## 示例
开始一个事务：

```sql
BEGIN;
```

建立一个游标：

```sql
DECLARE mycursor CURSOR FOR SELECT * FROM films;
```

使用游标 mycursor 向前移动五行：

```sql
MOVE FORWARD 5 IN mycursor;
MOVE 5
```

获取之后的一行（第六行）：

```sql
FETCH 1 FROM mycursor;
 code  | title  | did | date_prod  |  kind  |  len
-------+--------+-----+------------+--------+-------
 P_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
(1 row)
```

关闭游标，结束事务：

```sql
CLOSE mycursor;
COMMIT;
```

## 兼容性
在 SQL 标准中没有 MOVE 语句。

## 另见
DECLARE、FETCH、CLOSE
