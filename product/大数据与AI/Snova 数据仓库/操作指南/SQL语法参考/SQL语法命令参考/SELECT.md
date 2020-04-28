从一个表或视图检索行。

## 概要

```
[ WITH with_query [, ...] ]
SELECT [ALL | DISTINCT [ON (expression [, ...])]]
  * | expression [[AS] output_name] [, ...]
  [FROM from_item [, ...]]
  [WHERE condition]
  [GROUP BY grouping_element [, ...]]
  [HAVING condition [, ...]]
  [WINDOW window_name AS (window_specification)]
  [{UNION | INTERSECT | EXCEPT} [ALL] select]
  [ORDER BY expression [ASC | DESC | USING operator] [NULLS {FIRST | LAST}] [, ...]]
  [LIMIT {count | ALL}]
  [OFFSET start]
  [FOR {UPDATE | SHARE} [OF table_name [, ...]] [NOWAIT] [...]]
```

其中 with_query 是：

```
with_query_name [( column_name [, ...] )] AS ( select )
```

其中 grouping_element 可以是下列之一：

```
()
expression
ROLLUP (expression [,...])
CUBE (expression [,...])
GROUPING SETS ((grouping_element [, ...]))
```

其中 window_specification 可以是：
```
  [window_name]
  [PARTITION BY expression [, ...]]
  [ORDER BY expression [ASC | DESC | USING operator] [NULLS {FIRST | LAST}] [, ...]
     [{RANGE | ROWS} 
          { UNBOUNDED PRECEDING
          | expression PRECEDING
          | CURRENT ROW
          | BETWEEN window_frame_bound AND window_frame_bound }]]
```

其中 window_frame_bound 可以是下列之一：
```
UNBOUNDED PRECEDING
expression PRECEDING
CURRENT ROW
expression FOLLOWING
UNBOUNDED FOLLOWING
```
 
其中 from_item 可以是下列之一：
```
[ONLY] table_name [[AS] alias [( column_alias [, ...] )]]
(select) [AS] alias [( column_alias [, ...] )]
with_query_name [ [AS] alias [( column_alias [, ...] )]]
function_name ( [argument [, ...]] ) [AS] alias
             [( column_alias [, ...] 
                | column_definition [, ...] )]
function_name ( [argument [, ...]] ) AS 
              ( column_definition [, ...] )
from_item [NATURAL] join_type from_item
          [ON join_condition | USING ( join_column [, ...] )]
```

## 描述
SELECT 从零或更多表中检索行。SELECT 的通常处理如下：
- WITH 子句中的所有查询都会被计算。这些查询实际充当了在 FROM 列表中可以引用的临时表。

2. FROM 列表中的所有元素都会被计算（FROM 中的每一个元素都是一个真实表或者虚拟表）。如果在 FROM 列表中指定了多于一个元素，它们会被交叉连接在一起。

3. 如果指定了 WHERE 子句，所有不满足该条件的行都会被从输出中消除。

4. 如果指定了 GROUP BY 子句，输出会被组合成由在一个或者多个值上匹配的行构成的分组，并且在其上计算聚集函数的结果。如果出现了 HAVING 子句，它会消除不满足给定条件的分组。

5. 如果指定了窗口表达式（可选的 WINDOW 子句），输出会根据位置（行）或者基于值（范围）的窗口帧来组织。

6. DISTINCT 从结果中消除重复的行。DISTINCT ON 消除在所有指定表达式上匹配的行。ALL（默认）将返回所有候选行，包括重复的行。

7. 对于每一个被选中的行，会使用 SELECT 输出表达式计算实际的输出行。

8. 通过使用操作符 UNION、 INTERSECT 和 EXCEPT，多于一个 SELECT 语句的输出可以被整合形成一个结果集。
UNION 操作符返回位于一个或者两个结果集中的全部行。
INTERSECT 操作符返回同时位于两个结果集中的所有行。
EXCEPT操作符返回 位于第一个结果集但不在第二个结果集中的行。
在所有三种情况下，重复行都会被消除（除非指定 ALL）。

9. 如果指定了 ORDER BY 子句，被返回的行会以指定的顺序排序。如果没有给定 ORDER BY，系统会以能最快产生行的顺序返回它们。

10. 如果指定了 LIMIT 或者 OFFSET 子句，SELECT 语句只返回结果行的一个子集。

11. 如果指定了 FOR UPDATE 或者 FOR SHARE，SELECT 语句会把被选中的行锁定而不让并发更新访问它们。

用户必须拥有在要读取值的表上的 SELECT 特权。FOR UPDATE、FOR SHARE 还要求 UPDATE 特权。

## 参数

**WITH 子句**
WITH 子句允许用户指定一个或者多个在主查询中可以其名称引用的子查询。在主查询期间子查询实际扮演了临时表或者视图的角色。每一个子查询都可以是一个 SELECT 或者 VALUES 语句。

对于每一个 WITH 子句，都必须指定一个名称（无需方案限定）。可选地，可以指定一个列名列表。如果省略该列表，会从该子查询中推导列名。主查询和 WITH 查询全部（理论上）都在同一时间被执行。

**SELECT 列表**
SELECT 列表（位于关键词 SELECT 和 FROM 之间）指定构成 SELECT 语句输出行的表达式。这些表达式可以（并且通常确实会）引用 FROM 子句中计算得到的列。

另一个名字可以被指定用于一个输出列的名称，使用 [AS] output_name。该名称最基本是出于显示目的标记列。一个输出列的名称可以被用来在 ORDER BY 以及 ORDER BY 子句中引用该列的值，但是不能用于 WHERE 和 HAVING 子句（在其中必须写出表达式）。
在大多数场景下，AS 关键词是可选的（例如当为一个列名、常量、函数调用、简单一元操作表达式声明一个别名）。 为了避免声明的别名与关键词冲突，输出名一定要使用双引号包含起来。推荐总是写上 AS 或者用双引号引用输出名称。

一个 SELECT 列表中的表达式可以为常量值、一个列引用、一个操作符调用、一个函数调用、一个窗口表达式、一个标量子查询（scalar subquery）等。
一些构造可以分类为一个表达式但是不符合通用的语法规则。这些通常有一个操作符或者函数的语义。可以在输出列表中写来取代表达式，它是被选中行的所有列的一种简写方式。还可以写 table_name.，它是只来自那个表的所有列的简写形式。

**FROM 子句**
FROM 子句为 SELECT 指定一个或者更多源表。如果指定了多个源表，结果将是所有源表的笛卡尔积（交叉连接）。但是通常会增加限定条件，来把返回的行限制为该笛卡尔积的一个小子集。FROM 子句可以包含下列元素：
table_name
一个现有表或视图的名称（可以是方案限定的）。如果在表名前指定了 ONLY，则只会扫描该表。如果没有指定 ONLY，该表及其所有后代表（如果有）都会被扫描。

alias
一个包含别名的 FROM 项的替代名称。别名被用于让书写简洁或者消除自连接中的混淆（其中同一个表会被扫描多次）。当提供一个别名时，表或者函数的实际名称会被隐藏。例如给定 FROM foo AS f，SELECT 的剩余部分就必须以 f 而不是 foo 来引用这个 FROM 项。如果写了一个别名，还可以写一个列别名列表来为该表的一个或者多个列提供替代名称。

select
一个子-SELECT 可以出现在 FROM 子句中。这就好像把它的输出创建为一个存在于该 SELECT 命令期间的临时表。注意 子-SELECT 必须用圆括号包围，并且必须为它提供一个别名，也可以在这里使用一个 VALUES 命令。

with_query_name
在 FROM 子句中，可以通过写一个 WITH 查询的名称来引用 WITH 查询，就好像该查询的名称是一个表名。WITH 查询的名称不能包含一个方案限定词。可以像表一样，以同样的方式提供一个别名。

function_name
函数调用可以出现在 FROM 子句中（对于返回结果集合的函数特别有用，但是可以使用任何函数）。这就好像把该函数的输出创建为一个存在于该 SELECT 命令期间的临时表。可以用和表一样的方式提供一个别名。
如果写了一个别名，还可以写一个列别名列表来为该函数的组合返回类型的一个或者多个属性提供替代名。如果函数被定义为返回 record 数据类型，那么必须出现一个别名或者关键词 AS，后面跟上形为 ( column_name data_type [, ... ] ) 的列定义列表。列定义列表必须匹配该函数返回的列的实际数量和类型。

join_type
下列之一：
- **[INNER] JOIN**
- **LEFT [OUTER] JOIN**
- **RIGHT [OUTER] JOIN**
- **FULL [OUTER] JOIN**
- **CROSS JOIN**

对于 INNER 和 OUTER 连接类型，必须指定一个连接条件，即 NATURALON join_condition 或者 USING ( join_column [, ...]) 之一（只能有一种）。其含义见下文。对于 CROSS JOIN，上述子句不能出现。

一个 JOIN 子句联合两个 FROM 项（ 为方便我们称之为"表"，尽管实际上它们可以是任何类型的 FROM 项）。如有必要可以使用圆括号确定嵌套的顺序。在没有圆括号时，JOIN 会从左至右嵌套。在任何情况下，JOIN 的联合比分隔 JOIN-列表项的逗号更强。

CROSS JOIN 和 INNER JOIN 会产生简单的笛卡尔积，也就是与在 FROM 的顶层列出两个表得到的结果相同，但是要用连接条件（如果有）约束该结果。CROSS JOIN 与 INNER JOIN ON(TRUE) 等效，也就是说条件不会移除任何行。这些连接类型只是一种记号上的方便，因为没有什么是用户用纯粹的 FROM 和 WHERE 能做而它们不能做的。

LEFT OUTER JOIN 返回被限制过的笛卡尔积中的所有行（即所有通过了其连接条件的组合行），外加左手表中没有相应的通过了连接条件的右手行的每一行的拷贝。通过在右手列中插入空值，这种左手行会被扩展为连接表的完整行。注意在决定哪些行匹配时，只考虑 JOIN 子句自身的条件之后才应用外条件。

相反，RIGHT OUTER JOIN 返回所有连接行，外加每 一个没有匹配上的右手行（在左端用空值扩展）。这只是为了记号 上的方便，因为用户可以通过交换左右表把它转换成一个 LEFT OUTER JOIN。

FULL OUTER JOIN 返回所有连接行，外加每 一个没有匹配上的左手行（在右端用空值扩展），再外加每一个没有匹配上的右手行（在左端用空值扩展）。

ON join_condition
join_condition 是一个会得到 boolean 类型值的表达式（类似于一个 WHERE 子句），它说明一次连接中哪些行被认为相匹配。

USING (join_column [, ...])
形式 USING ( a, b, ... ) 的子句是 ON left_table.a = right_table.a AND left_table.b = right_table.b ... 的简写。还有，USING 表示每一对相等列中只有一个会被包括在连接输出中。

NATURAL
NATURAL 是列出在两个表中所有具有相同名称的列的 USING 的简写。

**WHERE 子句**
可选的 WHERE 子句的形式：
```sql
WHERE condition
```
其中 condition 是任一计算得到 boolean 类型结果的表达式。任何不满足这个条件的行都会从输出中被消除。如果用一行的实际值替换其中的 变量引用后，该表达式返回真，则该行符合条件。

**GROUP BY 子句**
可选的 GROUP BY 子句的形式：
```sql
GROUP BY grouping_element [, ...]
```

grouping_element 可以为下列之一：
```sql
()
expression
ROLLUP (expression [,...])
CUBE (expression [,...])
GROUPING SETS ((grouping_element [, ...]))
```

GROUP BY 将会把所有被选择的行中共享相同分组表达式值的那些行压缩成一个行。一个被用在 expression 可以是输入列名、输出列（SELECT 列表项）的名称或序号或者由输入列值构成的任意表达式。在出现歧义时，GROUP BY 名称将被解释为输入列名而不是输出列名。

聚集函数（如果使用）会在组成每一个分组的所有行上进行计算，从而为每一个分组产生一个单独的值（如果有聚集函数但是没有 GROUP BY子 句，则查询会被当成是由所有选中行构成的一个单一分组）。当存在 GROUP BY 子句或者任何聚集函数时，SELECT 列表表达式不能引用非分组列（除非它出现在聚集函数中或者它函数依赖于分组列），因为这样做会导致返回非分组列的值时会有多种可能的值。

数据库有下面增加的 OLAG 分组扩展（通常被称为*supergroups*）：
ROLLUP
一个 ROLLUP 分组是 GROUP BY 分组的扩展。该分组创建一个从最细的级别到一个粗粒度级别上卷聚集操作，后面紧跟着一系列的分组列（或者表达式）。ROLLUP 接受一个有序的分组列，计算在 GROUP BY 中指定的标准聚集值，然后从右到左进一步创建高层次的部分和，最后创建了累积和。一个 ROLLUP 分组能够看做一系列的分组集。例如：
```sql
GROUP BY ROLLUP (a,b,c) 
```
等价于：
```sql
GROUP BY GROUPING SETS( (a,b,c), (a,b), (a), () ) 
```
一个有 n 个元素的 ROLLUP 翻译为 n+1 分组集。同时，在 ROLLUP 中指定分组表达式的顺序很重要。

CUBE
CUBE 分组是 GROUP BY 子句的一个扩展。它能够为给定的分组列（或者表达式）所有可能的组合创建部分和。在多维分析上，CUBE 为指定维度的、可计算的数据立方体计算出所有的部分和。例如：
```sql
GROUP BY CUBE (a,b,c) 
```
等价于：
```sql
GROUP BY GROUPING SETS( (a,b,c), (a,b), (a,c), (b,c), (a), 
(b), (c), () ) 
```
一个有 n 个元素的 CUBE 翻译为 2n 个分组集。 在任何需要交叉表报表的场景下，考虑使用 CUBE。CUBE 典型的适用于查询中从多个维度中使用列而不是一个列代表不同层次上使用列。例如一个常用的交叉列表可能需要分类汇总为月、所有组合的状态和产品。

GROUPING SETS
GROUP BY 子句中，可以在想要使用 GROUPING SETS 表达式的地方选择性指定分组集合。这允许精确的规范在多个维度而不用计算整个 ROLLUP 或 CUBE。例如：
```sql
GROUP BY GROUPING SETS( (a,c), (a,b) )
```
如果使用分组扩展子句 ROLLUP、CUBE 或者 GROUPING SETS，有两个挑战将会出现。 首先，如何决定哪些结果行需要是部分和，以及给定的部分和的准确聚集层次。或者用户如何区别包含 NULL 或者由 ROLLUP 、CUBE 产生"NULL"值的结果行。第二，当在 GROUP BY 子句中指定了重复分组，如何决定哪些结果行是冗余的，有两个额外的分组函数可以使用在 SELECT 列表中帮助：
- **grouping(column      [, ...])**：grouping 函数能够被应用到一个或者更多的分组属性上来从正规的分组行区分开超级聚集行（这对将一个超级聚集行中表示所有值集合的“NULL”与普通行中的 NULL 区分开很有用）。该函数中的每个参数产生一个位，要么为1或者0，其中1意味着结果行是超级聚集的，0意味着结果行来自于普通聚集。
grouping 函数通过将这些位当做一个二进制数然后将它们转换为一个十进制的书，返回一个整数。
- **group_id()**：对于包含有冗余分组集，group_id 函数被用来鉴别在输出中的冗余行。所有 *unique* 分组集输出行将有一个为0的 group_id 值。对于每个检测到的冗余的分组集，group_id 函数分配一个大于0的 group_id。
在一个特定的冗余分组集中的所有行被有相同的 group_id 值。

**WINDOW 子句**
WINDOW 子句是用来定义一个能够被用在一个窗口函数（例如：rank 或 avg）的 OVER() 表达式中的窗口。 例如：

```sql
SELECT vendor, rank() OVER (mywindow) FROM sale
GROUP BY vendor
WINDOW mywindow AS (ORDER BY sum(prc*qty));
```

一个 WINDOW 子句有一般的形式：

```sql
WINDOW window_name AS (window_specification)
```

其中 window_specification 可以为：

```sql
[window_name]
[PARTITION BY expression [, ...]]
[ORDER BY expression [ASC | DESC | USING operator] [NULLS {FIRST | LAST}] [, ...]
    [{RANGE | ROWS} 
      { UNBOUNDED PRECEDING
      | expression PRECEDING
      | CURRENT ROW
      | BETWEEN window_frame_bound AND window_frame_bound }]]
             其中 window_frame_bound可以为下列之一：
               UNBOUNDED PRECEDING
               expression PRECEDING
               CURRENT ROW
               expression FOLLOWING
               UNBOUNDED FOLLOWING
```

window_name
给窗口说明一个名字。

PARTITION BY
PARTITION BY 子句基于指定表表达式的唯一值将结果集组织为逻辑组。当同窗口函数使用，函数将被单独地应用到每个分片。例如，如果用户在一个列名后紧跟一个 PARTITION BY，结果集将会通过列的不同值进行分割。如果忽略，整个结果集被看做一个分片。

ORDER BY
ORDER BY 子句定义如何对结果集的每个分片进行排序。如果忽略，返回的行按照效率高的方式返回，可能每次有所不同。 
注意：缺乏连贯顺序的数据类型的列，例如，time，在一个窗口说明的 ORDER BY 子句不适合作为排序字段。时间，有或者没有时区，缺少一个明确的顺序，由于加法和减法没有预期的效果。例如，下面的一般不为真：x::time < x::time + '2 hour'::interval。

ROWS | RANGE
通过使用 ROWS 或者 RANGE 子句来表示窗口的界（bounds）。窗口的界可能为一个分区的一个，多个行或者所有行。可以根据一系列的值距离当前行的值偏移量来表达（RANGE）或者依据距离当前行的偏移行数来表达（ROWS）。
当使用 RANGE 子句，一定要使用一个 ORDER BY 子句。这是因为执行产生窗口的计算需要值是排好序的。另外，ORDER BY 子句不能包含多于一个的表达式，同时表达式的必须为一个日期或者一个数值。当使用 ROWS 或者 RANGE子句，如果用户只指定了一个开始行，那么当前行会作为窗口的最后一行。

**PRECEDING**：PRECEDING 子句定义以当前行为参考点窗口的第一行的位置。开始行依据距离当前行的前驱行数来表达。例如，在 ROWS 框架中，5 PRECEDING 设置窗口开始于当前的第五个前驱行。在 RANGE 框架中，设置窗口开始于按照给定顺序的当前行的第五个前驱行。如果按照时间升序指定顺序，那么第一行为当前行五天前的行。UNBOUNDED PRECEDING 设置窗口中的第一行为分区中的第一行。

**BETWEEN**：BETWEEN 子句使用当前行作为参考点，定义了窗口的第一行和最后一行。第一行和最后一行依据当前行的前驱和后继的行的数目表达。例如，BETWEEN 3 PRECEDING AND 5 FOLLOWING 设置窗口开始于当前行前驱的第三个行，结束于当前行后面的第五行。使用 BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 设置窗口的第一行和最后一行为该分区中的一行和最后一行。这等效于在没有 ROW 或者 RANGE 子句指定是的默认行为。

**FOLLOWING**：FOLLOWING 子句定义了使用当前行作为参考点的窗口的最后一行。最后一行的表示依据跟在当前行后面的行的行号。例如，在 ROWS 框架中，5 FOLLOWING 设置窗口的结束为止在当前行后的第五个行。在 RANGE 框架中，它设置窗口的结束为按在给定顺序跟在当前行后面的5行。如果指定属性为按照日期的升序，那么最一行为当前行之后5天的行。使用 UNBOUNDED FOLLOWING 设置窗口中的最后一行为分区中的最后一行。

如果没有指定一个 ROW 或者 RANGE 子句，窗口的界会从分区的第一行开始（UNBOUNDED PRECEDING） 同时以当前行为结束（CURRENT ROW），如果使用了 ORDER BY ，ORDER BY 没有指定，那么窗口开始于分区（UNBOUNDED PRECEDING）的第一行同时结束语分区（UNBOUNDED FOLLOWING）的最后一行。

**HAVING 子句**
可选 HAVING 子句的形式：
```sql
HAVING condition
```
其中 condition 与 WHERE 子句中指定的条件相同。HAVING 消除不满足该条件的分组行。
HAVING 与 WHERE 不同：WHERE 会在应用 GROUP BY 之前过滤个体行，而 HAVING 过滤由 GROUP BY 创建的分组行。condition 中引用的每一个列必须无歧义地引用一个分组列（除非该引用出现在一个聚集函数）。

即使没有 GROUP BY 子句，HAVING 的存在也会把一个查询转变成一个分组查询。这和查询中包含聚集函数但没有 GROUP BY 子句时的情况相同。所有被选择的行都被认为是一个单一分组，并且 SELECT 列表和 HAVING 子句只能引用聚集函数中的表列。如果该 HAVING 条件为真，这样一个查询将会发出一个单一行；否则不返回行。

**UNION 子句**
UNION 子句具有下面的形式：
```sql
select_statement UNION [ALL] select_statement
```
select_statement 是任何没有 ORDER BY、LIMIT、 FOR UPDATE、 FOR SHARE 和 FOR KEY SHARE 子句的 SELECT 语句（如果子表达式被包围在圆括号内，ORDER BY 和 LIMIT 可以被附着到其上。如果没有圆括号，这些子句将被应用到 UNION 的结果而不是右手边的表达式上）。

UNION 操作符计算所涉及的 SELECT 语句所返回的行的并集。如果一行至少出现在两个结果集中的一个内，它就会在并集中。作为 UNION 两个操作数的 SELECT 语句必须产生相同数量的列并且对应位置上的列必须具有兼容的数据类型。

UNION 的结果不会包含重复行，除非指定了 ALL 选项。ALL 会阻止消除重复（因此，UNION ALL 通常显著地快于 UNION，尽量使用 ALL）。

除非用圆括号指定计算顺序，同一个 SELECT 语句中的多个 UNION 操作符会从左至右计算。

当前，FOR UPDATE 和 FOR SHARE 不能用于 UNION 结果或者 UNION 的任何输入。

**INTERSECT** **子句**

INTERSECT子句具有下面的形式：

```sql
select_statement INTERSECT [ALL] select_statement
```

select_statement 是任何没有 ORDER BY、LIMIT、FOR UPDATE 以及 FOR SHARE 子句的 SELECT 语句。

INTERSECT 操作符计算所涉及的 SELECT 语句返回的行的交集。如果一行同时出现在两个结果集中，它就在交集中。

INTERSECT 的结果不会包含重复行，除非指定了 ALL 选项。如果有 ALL，一个在左表中有m次重复并且在右表中有n次重复的行将会在结果中出现 min(m, n) 次。

除非用圆括号指定计算顺序， 同一个 SELECT 语句中的多个 INTERSECT 操作符会从左至右计算。INTERSECT 的优先级比 UNION 更高。也就是说，A UNION B INTERSECT C 被读成 A UNION (B INTERSECT C)。

当前， FOR UPDATE 和 FOR SHARE 不能用于 INTERSECT 结果或者 INTERSECT 的任何输入。

**EXCEPT 子句**

EXCEPT 子句具有如下形式：
```sql
select_statement EXCEPT [ALL] select_statement
```
select_statement 是任何没有 ORDER BY、LIMIT、FOR UPDATE 以及 FOR SHARE 子句的 SELECT 语句。

EXCEPT 操作符计算位于左 SELECT 语句的结果中但不在右 SELECT 语句结果中的行集合。

EXCEPT 的结果不会包含重复行，除非指定了 ALL 选项。如果有 ALL，一个在左表中有 m 次重复并且在右表中有 n 次重复的行将会在结果集中出现 max(m-n,0) 次。

除非用圆括号指定计算顺序，同一个 SELECT 语句中的多个 EXCEPT 操作符会从左至右计算。EXCEPT 的优先级与 UNION 相同。

当前，FOR UPDATE 和 FOR SHARE 不能用于 EXCEPT 结果或者 EXCEPT 的任何输入。

**ORDER BY 子句**

ORDER BY 子句可选的形式如下：
```sql
ORDER BY expression [ASC | DESC | USING operator] [NULLS { FIRST | LAST}] [, ...]
```
每一个 expression 可以是输出列（SELECT 列表项）的名称或者序号，它也可以是由输入列值构成的任意表达式。

ORDER BY 子句导致结果行被按照指定的表达式排序。 如果两行按照最左边的表达式是相等的，则会根据下一个表达式比较它们，以此类推。如果按照所有指定的表达式它们都是相等的，则它们被返回的顺序取决于实现。

序号指的是输出列的顺序（从左至右）位置。这种特性可以为不具有唯一名称的列定义一个顺序。这不是绝对必要的，因为总是可以使用 AS 子句为输出列赋予一个名称。

也可以在 ORDER BY 子句中使用任意表达式，包括没有出现在 SELECT 输出列表中的列。因此，下面的语句是合法的：

```sql
SELECT name FROM distributors ORDER BY code;
```

这种特性的一个限制是一个应用在 UNION、INTERSECT 或者 EXCEPT 子句结果上的 ORDER BY 只能指定输出列名称或序号，但不能指定表达式。

如果一个 ORDER BY 表达式是一个既匹配输出列名称又匹配输入列名称的简单名称，ORDER BY 将把它解读成输出列名称。这与在同样情况下 GROUP BY 会做出的选择相反。这种不一致是为了与 SQL 标准兼容。

可以为 ORDER BY 子句中的任何表达式之后增加关键词 ASC（上升）DESC（下降）。如果没有指定， ASC 被假定为默认值。或者可以在 USING 子句中指定一个特定的排序操作符名称。ASC 通常等价于 USING <，而 DESC 通常等价于USING >（但是一种用户定义数据类型的创建者可以准确地定义默认排序顺序是什么，并且它可能会对应于其他名称的操作符）。

如果指定 NULLS LAST，空值会排在非空值之后；如果指定 NULLS FIRST，空值会排在非空值之前。如果都没有指定， 在指定或者隐含 ASC 时的默认行为是 NULLS LAST， 而指定或者隐含 DESC 时的默认行为是 NULLS FIRST（因此，默认行为是空值大于非空值）。当指定 USING时，默认的空值顺序取决于该操作符是否为小于或者大于操作符。

注意顺序选项只应用到它们所跟随的表达式上。例如 ORDER BY x, y DESC 和 ORDER BY x DESC, y DESC 是不同的。

字符串数据被根据区域相关的排序规则顺序排序，该顺序在数据库系统被初始化时建立。

**DISTINCT 子句**

如果指定了 DISTINCT 子句，所有重复的行会被从结果 集中移除（为每一组重复的行保留一行）。ALL 则指定相反的行为，所有行都会被保留，这也是默认情况。

DISTINCT ON ( expression [, ...] )只保留在给定表达式上计算相等的行集合中的第一行。DISTINCT ON 表达式使用和 ORDER BY 相同的规则（见上文）解释。注意，除非用 ORDER BY 来确保所期望的行出现在第一位，每一个集合的"第一行"是不可预测的。例如：

```sql
SELECT DISTINCT ON (location) location, time, report FROM 
weather_reports ORDER BY location, time DESC;
```

为每个地点检索最近的天气报告。但是如果我们不使用 ORDER BY 来强制对每个地点的时间值进行降序排序，我们为每个地点得到的报告的时间可能是无法预测的。

DISTINCT ON 表达式必须匹配最左边的 ORDER BY 表达式。ORDER BY 子句通常将包含额外的表达式，这些额外的表达式用于决定在每一个 DISTINCT ON 分组内行的优先级。

当数据库处理包含有 DISTINCT 子句的查询时，查询将会转换为 GROUP BY 查询。在很多场景中，变换能够提供显著的性能提升。然而，当 distinct 值的数量与总的行数相近时，该转换可能会导致多个层次的分组计划的产生。在这种情况下，由于引入的低聚集度开销，预期性能会降低。

**LIMIT 子句**
LIMIT 子句两个独立的子句构成：
```sql
LIMIT {count | ALL}
OFFSET start
```
count 指定要返回 的最大行数，而 start 指定在返回行之前要跳过的行数。在两者都被指定时，在开始计算要返回的  count 行之前会跳过 start 行。

在使用 LIMIT 时，用一个 ORDER BY 子句把结果行约束到一个唯一顺序是个好办法。否则用户讲得到该查询结果行的 一个不可预测的子集，用户可能要求从第10到第20行，但是在什么顺序下的第10到第20，除非指定 ORDER BY，用户是不知道顺序的。

查询规划器在生成一个查询计划时会考虑 LIMIT，因此根据用户使用的 LIMIT 和 OFFSET，用户很可能得到不同的计划（得到不同的行序）。所以，使用不同的 LIMIT/OFFSET 值来选择一个查询结果的不同子集将会给出不一致的结果，除非用户用 ORDER BY 强制一种可预测的结果顺序。这不是一个缺陷，它是 SQL 不承诺以任何特定顺序（除非使用  ORDER BY 来约束顺序）给出一个查询结果这一事实造成的必然后果。

**FOR UPDATE/FOR SHARE 子句**
FOR UPDATE 子句的形式如下：

```sql
FOR UPDATE [OF table_name [, ...]] [NOWAIT]
```

非常接近的 FOR SHARE 子句的形式为：

```sql
FOR SHARE [OF table_name [, ...]] [NOWAIT]
```

FOR UPDATE 导致被 SELECT 语句访问的表被锁定，就好像在做更新一样。这可以防止表在当前事务结束之前被其他事务修改或者删除。也就是说在这个表上尝试 UPDATE、DELETE 或者 SELECT FOR UPDATE 的其他事务都将被阻塞，直至当前事务结束。还有，如果来自于另一个事务的 UPDATE、DELETE 或者 SELECT FOR UPDATE 已经锁住了选择的表，SELECT FOR UPDATE 将会等待该其他事务完成，并且接着锁住并且返回更新过的表。

为了防止该操作等待其他事务提交，可使用 NOWAIT。使用 NOWAIT 时，如果选中的行不能被立即锁定，该语句会报告错误而不是等待。
注意 NOWAIT 只适合行级锁，所要求的 ROW SHARE 表级锁仍然会以常规的方式取得。如果想要不等待的表级锁，用户可以先使用带 NOWAIT 的 LOCK（见**LOCK**）。

FOR SHARE 的行为相似，除了需要一个在表上的共享锁而不是排它锁。一个共享锁阻塞其它在表上执行 UPDATE、DELETE 或者 SELECT FOR UPDATE的事务，但是不禁止它们执行 SELECT FOR SHARE。

如果特定的表在 FOR UPDATE 或者 FOR SHARE 中，那么只有这些表被锁定；任何其它在 SELECT 中使用的表按照通常的方式进行读。一个不带表列表的 FOR UPDATE 或者 FOR SHARE 子句将会影响所有在命令中使用的表。如果 FOR UPDATE 或者 FOR SHARE 应用到了一个视图或者子查询上，那么它将影响所有在视图或者子查询中使用到的表。

FOR UPDATE 或者 FOR SHARE 不能应用到由一个基础查询引用的 with_query 上。如果需要行锁定在 with_query 上，可以在 with_query 中指定 FOR UPDATE 或者 FOR SHARE。

如果需要在不同的表上指定不同的锁行为，多个 FOR UPDATE 和 FOR SHARE 子句是可以写的。如果相同表同时由 FOR UPDATE 和 FOR SHARE子句中提及（或者是隐式的影响），那么该表将会按照 FOR UPDATE 进行处理。相似的，如果一个表任何一个子句都会对它有影响，那么将会按照 NOWAIT 进行处理。

## 示例
把表 films 与表 distributors 连接：

```sql
SELECT f.title, f.did, d.name, f.date_prod, f.kind FROM 
distributors d, films f WHERE f.did = d.did
```

要对所有电影的 length 列求和并且用 kind 对结果分组：

```sql
SELECT kind, sum(length) AS total FROM films GROUP BY kind;
```

要对所有电影的 length 列求和、对结果按照 kind 分组并且显示总长小于 5 小时的分组：

```sql
SELECT kind, sum(length) AS total FROM films GROUP BY kind 
HAVING sum(length) < interval '5 hours';
```

根据 kind 和 distributor 计算所有电影销售的部分和以及总和：

```sql
SELECT kind, distributor, sum(prc*qty) FROM sales
GROUP BY ROLLUP(kind, distributor)
ORDER BY 1,2,3;
```

基于总的销售对电影的发行商进行排名：

```sql
SELECT distributor, sum(prc*qty), 
       rank() OVER (ORDER BY sum(prc*qty) DESC) 
FROM sale
GROUP BY distributor ORDER BY 2 DESC;
```

下面的两个例子都是根据第二列（name）的内容排序结果：

```sql
SELECT * FROM distributors ORDER BY name;
SELECT * FROM distributors ORDER BY 2;
```

接下来的例子展示了如何得到表 distributors 和 actors的并集，把结果限制为那些在每个表中以字母 W 开始的行。只想要可区分的行，因此省略了关键词 ALL：

```sql
SELECT distributors.name FROM distributors WHERE 
distributors.name LIKE 'W%' UNION SELECT actors.name FROM 
actors WHERE actors.name LIKE 'W%';
```

这个例子展示了如何在 FROM 子句中使用函数， 分别使用和不使用列定义列表：

```sql
CREATE FUNCTION distributors(int) RETURNS SETOF distributors 
AS $$ SELECT * FROM distributors WHERE did = $1; $$ LANGUAGE 
SQL;
SELECT * FROM distributors(111);
 
CREATE FUNCTION distributors_2(int) RETURNS SETOF record AS 
$$ SELECT * FROM distributors WHERE did = $1; $$ LANGUAGE 
SQL;
SELECT * FROM distributors_2(111) AS (dist_id int, dist_name 
text);
```

这个例子展示了如何使用简单的 WITH 子句：

```sql
WITH test AS (
  SELECT random() as x FROM generate_series(1, 3)
  )
SELECT * FROM test
UNION ALL
SELECT * FROM test; 
```

这个例子使用 WITH 子句来展示每个产品只在最好销售区域的销售总额：

```sql
WITH regional_sales AS 
    SELECT region, SUM(amount) AS total_sales
    FROM orders
    GROUP BY region
  ), top_regions AS (
    SELECT region
    FROM regional_sales
    WHERE total_sales > (SELECT SUM(total_sales) FROM
       regional_sales)
  )
SELECT region, product, SUM(quantity) AS product_units,
   SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions) 
GROUP BY region, product;
```

该示例能够不用 WITH 子句进行重写，但是将需要两层的子-SELECT 语句。

## 兼容性
SELECT 语句是兼容 SQL 标准的。 但是也有一些扩展和缺失的特性。

**省略的 FROM 子句**
数据库允许我们省略 FROM子句。一种简单的使用是计算简单表达式 的结果，例如：
```sql
SELECT 2+2;
```
某些其他 SQL 数据库需要引入一个假的单行表放在该 SELECT 要选择的表上。

注意，如果没有指定一个 FROM 子句，该查询就不能引用任何数据库表。对于依赖这种行为的应用的兼容性，add_missing_from 配置参数能够可以启动。

**AS 关键词**
在 SQL 标准中，可选关键词 AS 只是一个噪声，能够直接被省略没有任何的语义影响。数据库解析器在重命名输出列时需要该关键词，因为没有它在类型扩展特性上回出现解析歧义。只要新列名是一个合法的列名（就是说与任何保留关键词不同）， 就可以省略输出列名之前的可选关键词 AS。 
PostgreSQL 要稍微严格些，只要新列名匹配任何关键词（保留或者非保留）就需要AS。推荐的习惯是使用 AS 或者带双引号的输出列名来防止与未来增加的关键词可能的冲突。然而在 FROM 中 AS 是可选的。

**GROUP BY 和 ORDER BY 可用的名字空间**
在 SQL-92 标准中，一个 ORDER BY 子句只能使用输出列名或者序号，而一个 GROUP BY 子句只能使用基于输入列名的表达式。数据库扩展了这两种子句以允许它们使用其他的选择（但如果有歧义时还是使用标准的解释）。数据库也允许两种子句指定任意表达式。注意出现在一个表达式中的名称将总是被当做输入列名而不是输出列名。

SQL:1999 及其后的标准使用了一种略微不同的定义，它并不完全向后兼容 SQL-92。不过在大部分的情况下，数据库会以与 SQL:1999 相同的方式解释 ORDER BY 或 GROUP BY 表达式。

**非标准子句**
DISTINCT ON、LIMIT 以及 OFFSET 子句并没有在 SQL 标准中有定义。

**STABLE 以及 VOLATILE 函数的限制使用**
为了防止数据在数据库的多个 segment 间不同步，任何一个定义为 STABLE 或者 VOLATILE 的函数不能在 Segment 级别执行（如果它包含了 SQL 或者修改了数据库）。

## 另见
EXPLAIN
