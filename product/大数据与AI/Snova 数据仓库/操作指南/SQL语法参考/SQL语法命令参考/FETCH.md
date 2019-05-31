使用游标从查询中检索行。

## 概要

```sql
FETCH [ forward_direction { FROM | IN } ] cursorname
```

其中 forward_direction 可以为空或者为下列之一：

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
FETCH 从之前创建的一个游标中检索行。

游标具有一个相关联的位置，FETCH 会用到该位置。 游标位置可能会位于查询结果的第一行之前、结果中任意行之上或者结果的最后一行之后。 
在被创建时，游标被定位在第一行之前。在取出 一些行后，该游标被定位在最近被取出的行上。如果 FETCH 运行超过了可用行的末尾，则该游标会被定位在最后一行之后。FETCH ALL 将总是让游标被定位于最后一行之后。

NEXT、FIRST、LAST、ABSOLUTE、RELATIVE 形式会在适当移动游标后取出一行。如果没有这样一行，将返回一个空结果，并且视情况将游标定位在第一行之前或者最后一行之后。

使用形式 FORWARD 的形式会在向前移动的方向上检索指定数量的行，然后将游标定位在最后返回的行上（如果 count 超过可用的行数，则定位在所有行之后）。注意在数据库中是不能够向后移动游标，因为不支持滚动游标。只能够用 FETCH 向前移动游标。

RELATIVE 0 、FORWARD 0 都会请求检索当前行但不移动游标，也就是重新取最近被取出的行。只要游标没有被定位在第一行之前或者最后一行之后，这种操作都会成功，否则不会返回任何行。

**输出**
如果成功完成，FETCH 命令返回一个下面形式的命令标签：
```sql
FETCH count
```
count 是取得的行数（可能为零）。注意在 psql 中，命令标签将不会实际显示，因为 psql 会显示被取得的行。

## 参数
forward_direction
定义获取方向以及要取得的行数。只有向前获取在数据库中是支持的。它可以是下列之一：

NEXT
取出下一行。如果省略 direction，这将是默认值。

FIRST
取出该查询的第一行（和 ABSOLUTE 1 相同）。只有在该游标第一次使用 FETCH 时是允许的。

LAST
取出该查询的最后一行（和 ABSOLUTE -1相同）。

ABSOLUTE count
取出查询的指定行。如果 count 的值超出范围就定位到最后一行之后。只有在被指定了 count 的行向前移动游标位置才能使用。

RELATIVE count
取出查询指定行 count 个后继行。RELATIVE 0 重新取出当前行（如果有）。只有在 count 向前移动游标位置时才允许。

count
获取后面 count 行（和 FORWARD count 相同）。

ALL
获取剩余的所有行（和 FORWARD ALL 相同）。

FORWARD
取出下一行（和 NEXT 相同）。

FORWARD count
取出接下来的 count 行。 FORWARD 0 重新取出当前行。

FORWARD ALL
取出所有剩下的行。

cursorname
一个已打开游标的名称。

## 注解
数据库不支持滚动游标，所以只能用 FETCH 向前移动游标位置。

ABSOLUTE 取行并不比用相对移动快多少，底层实现都必须遍历所有的中间行。

DECLARE 用来定义一个游标。使用 MOVE 可以改变游标的位置而不检索数据。

## 示例

开始一个事务：

```sql
BEGIN;
```

建立一个游标：

```sql
DECLARE mycursor CURSOR FOR SELECT * FROM films;
```

在游标 mycursor 中获取前五行：

```sql
FETCH FORWARD 5 FROM mycursor;
 code  |          title          | did | date_prod  |   kind   |  len
-------+-------------------------+-----+------------+----------+-------
 BL101 | The Third Man           | 101 | 1949-12-23 | Drama    | 01:44
 BL102 | The African Queen       | 101 | 1951-08-11 | Romantic | 01:43
 JL201 | Une Femme est une Femme | 102 | 1961-03-12 | Romantic | 01:25
 P_301 | Vertigo                 | 103 | 1958-11-14 | Action   | 02:08
 P_302 | Becket                  | 103 | 1964-02-03 | Drama    | 02:28
```

关闭游标并结束事务：

```sql
CLOSE mycursor;
COMMIT;
```

修改表 films 的游标 c_films 指向的当前位置的行的 kind 列的值：

```sql
UPDATE films SET kind = 'Dramatic' WHERE CURRENT OF c_films;
```

## 兼容性
SQL 标准只在嵌入式 SQL 和模块中使用游标。数据库允许游标在交互式的环境下使用。

这里描述的 FETCH 变体返回数据时就好像数据是一个 SELECT 结果，而不是被放在主变量中。除这一点之外，FETCH完全向上兼容于 SQL 标准。

涉及 FORWARD 形式的 FETCH ，以及形式 FETCH count 和 FETCHALL（其中 FORWARD 是隐式的）都是数据库扩展。不支持 BACKWARD。

SQL 标准只允许 FROM 在游标名之前。使用 IN 的选项是一种扩展。

## 另见
DECLARE、CLOSE、MOVE
