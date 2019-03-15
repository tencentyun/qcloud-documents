#### MOVE

定位一个游标

##### 概要

```sql
MOVE [ forward_direction {FROM | IN} ] cursorname
```

其中forward_direction可以为空或者下列之一：

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

##### 描述

MOVE重新定位一个游标而不检索任何数据。 MOVE的工作完全像FETCH命令，但是它只定位游标并且不返回行。

注意在数据库中向后移动一个游标是不可能的，因为在数据库中不支持滚动游标。只能够用MOVE向前移动游标位置。

**输出**

成功完成时，MOVE命令返回的命令标签形式是

```sql
MOVE count
```

count是一个 具有同样参数的FETCH命令会返回的 行数（可能为零）。

##### 参数

forward_direction

见FETCH获取更多信息。

cursorname

一个打开的游标名称。

##### 示例

-- 开始一个事务：

```sql
BEGIN;
```

-- 建立一个游标：

```sql
DECLARE mycursor CURSOR FOR SELECT * FROM films;
```

-- 使用游标mycursor向前移动5行：

```sql
MOVE FORWARD 5 IN mycursor;
MOVE 5
```

--获取之后的一行（第六行）

```sql
FETCH 1 FROM mycursor;
 code  | title  | did | date_prod  |  kind  |  len
-------+--------+-----+------------+--------+-------
 P_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
(1 row)
```

--关闭游标，结束事务：

```sql
CLOSE mycursor;
COMMIT;
```

##### 兼容性

在SQL标准中没有MOVE 语句。

##### 另见

DECLARE, FETCH, CLOSE