定义一个新函数。

## 概要

```sql
CREATE [OR REPLACE] FUNCTION name    
    ( [ [argmode] [argname] argtype [ { DEFAULT | = } defexpr ] [, ...] ] )
      [ RETURNS { [ SETOF ] rettype 
        | TABLE ([{ argname argtype | LIKE other table }
          [, ...]])
        } ]
    { LANGUAGE langname
    | IMMUTABLE | STABLE | VOLATILE
    | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
    | [EXTERNAL] SECURITY INVOKER | [EXTERNAL] SECURITY DEFINE
    | COST execution_cost
    | SET configuration_parameter { TO value | = value | FROM CURRENT }
    | AS 'definition'
    | AS 'obj_file', 'link_symbol' } ...
    [ WITH ({ DESCRIBE = describe_function
           } [, ...] ) ]
```

## 描述
CREATE FUNCTION 定义了一个新的函数。CREATE OR REPLACE FUNCTION 将会要么创建一个新的函数，要么替换一个存在的定义。

新函数的名称不能与同一模式中的具有相同参数的任何现有函数匹配。但是，不同参数类型的函数可能会共享一个名称（重载)。

为了更新一个已经存在函数的定义，可以使用 CREATE OR REPLACE FUNCTION 语句。不可能以这种方式更改函数的名称或参数类型（这实际上会创建一个新的，不同的函数）。此外，CREATE OR REPLACE FUNCTION 不会让用户更改现有函数的返回类型。为此，用户必须删除并重新创建该函数。如果用户删除然后重建一个函数，用户将不得不删除引用该旧函数的现有对象（如规则，视图，触发器等），用户可以使用 CREATE OR REPLACE FUNCTION 去改变一个函数的定义，而不会破坏引用该函数的对象。

**VOLATILE和STABLE函数的限制使用**

为了防止数据在数据库的各个段中变得不同步，任何分类为 STABLE 或 VOLATILE 的函数，如果它包含 SQL 或以任何方式修改数据库，都不能在段级别执行。例如 random() 或 timeofday() 函数不允许在数据库中的分布式数据上执行，因为他们可能会导致段实例之间的数据不一致。

为了确保数据的一致性，VOLATILE 和 STABLE 函数可以安全地用在主机上进行评估和执行的语句中。例如，接下来的语句总是在主机（master）上执行（没有 FROM 子句的语句）。

```sql
SELECT setval('myseq', 201);
SELECT foo();
```

在一个语句包含分布式表的 FROM 子句而且 FROM 子句中使用的函数只简单的返回一组行的情况下，该操作则可以在段上允许执行。

```sql
SELECT * FROM foo();
```

此规则的一个例外就是返回表引用（rangeFuncs）或使用 refCursor 数据类型的函数。请注意用户不能从数据库中的任何类型函数返回 refcursor。

## 参数

name
创建函数的名称（可选方案限定）。

argmode
参数的模式：IN、OUT、INOUT或VARIADIC。只有 OUT 参数可以遵循声明为 VARIADIC 的参数。如果省略，默认值为  IN。

argname
参数的名字。一些语言（目前只有 PL/pgSQL）能让用户在函数体中使用这个名字。对于其他语言输入参数的名称只是额外的文档。但是，输出参数的名称很重要，因为它定义了结果行类型中的列名。（如果用户省略了输出参数的名称，系统将选择默认列名称）

argtype
函数参数的数据类型（可选方案限定），如果有，该参数可以是 base、composite 或 domain 类型，或可以引用表列的类型。
根据实现的语言，也可以允许指定诸如 cstring 之类的假型。伪类型表示实际的参数类型是未完全指定的，或者在普通的 SQL 数据类型之外。
列的类型通过写入 tablename.columnname%TYPE 来引用。使用此功能有时可以帮助函数独立于表的定义的更改。

defexpr
如果没有指定参数，则用作默认值的表达式。表达式必须对参数类型是强制的。只有 IN 和 INOUT 参数可以有一个默认值。参数列表中具有默认值的参数后面的每个输入参数也必须具有默认值。

rettype
返回数据类型（可选方案限定）。该返回值可以是 base、composite 或 domain 类型，或引用表列的类型。根据实现语言，也可以允许它们指定诸如 cstring cstring 之类的伪类型。如果该函数不返回值，可以指定 void 作为其返回类型。
当有 OUT 和 INOUT 参数时， 该 RETURNS 子句可以被省略。如果存在，它必须与输出参数所暗示的结果类型一致： 如果存在多个输出参数或与单个输出参数相同的类型，则为 RECORD。
该 SETOF 修饰符表示该函数将返回一组条目，而不是单个条目。
列的类型通过写入 tablename.columnname%TYPE 来引用。

langname
该函数实现的语言名称可以是 SQL、C、internal 或用户自定义过程语言的名称。更多数据库支持过程语言请参见  CREATE LANGUAGE。为了向后兼容，该名称可以用括号括起来。

IMMUTABLE
STABLE
VOLATILE
这些属性通知查询优化器有关该函数的行为。最多可以指定一个选择。如果这些都不出现，则 VOLATILE 是默认的假设。由于数据库目前有使用 VOLATILE 函数的性质，因此如果一个函数是真正的 IMMUTABLE，那么用户必须显式声明以能够使用该限制。

IMMUTABLE 表示该函数不能修改数据库，并且在给定相同的参数值时始终返回相同的结果。它不会进行数据库查找或以其他方式使用参数列表中不直接显示的信息。如果给出这个选项。则可以使用函数值替换具有全常量参数的函数的任何调用。

STABLE 表示该数据库不能修改数据库，并且在单个表扫描中，对于相同的参数值，它将返回相同的结果。但是其结果可能会随 SQL 语句更改。这是对结果取决于数据库查询，参数值 （例如当前时区），等等的函数的适当选择。还是要注意  current_timestamp 系列的函数符合稳定状态，因为他们的值在事务中不会改变。

VOLATILE 表示即使在单个表扫描中函数值可能发生变化，因此不能进行优化。在这个意义上来说，相对较少的数据库函数是不稳定的。例如 random()，currval()，timeofday()。 但是请注意，任何具有副作用的函数必须归类为 volatile， 即使它的结果相当可预测，以此来防止调用被优化，一个例子是 setval()。

CALLED ON NULL INPUT
RETURNS NULL ON NULL INPUT
STRICT
CALLED ON NULL INPUT（默认值）表示当其某些参数为 NULL 时，该函数仍能被正常调用。那么该函数的作者有责任在必要时检查空值，并作出适当的响应。RETURNS NULL ON NULL INPUT or STRICT 被指明时，表示当输入参数为空时，该函数不会执行，直接返回 NULL 结果。

[EXTERNAL] SECURITY INVOKER
[EXTERNAL] SECURITY DEFINER
SECURITY INVOKER（默认值）表示该函数将以调用者的权限执行。SECURITY DEFINER 表示该函数以创建者的权限执行。

COST execution_cost
确定估计成本的整数，以 cpu_operator_cost 为单位。 如果函数返回一个集合，execution_cost 会标识每个返回行的成本。如果没有指定成本，C 语言和内部函数 默认为1个单位，然而其他语言的函数默认100个单位，当用户指定较大的 execution_cost 值时，计划程序会尝试较少的函数评估。

configuration_parameter
value
当输入该功能时，该 SET 子句将一个值应用于会话配置参数。当函数退出时，配置参数恢复到先前的值。当进入函数时，SET FROM CURRENT 应用会话的当前值。

definition
定义函数的字符串常量；意思取决于语言。它可能是内部函数名称，对象文件的路径，过程化语言文本中的 SQL 命令。

obj_file，link_symbol
当C语言源代码中的函数名称和 SQL 函数的名称不同时，这种形式的 AS 子句用于动态加载 C 语言函数。字符串 obj_file 是包含动态可加载对象文件的名称，link_symbol 是 C 语言源代码中的函数名称。如果省略了连接符号，则假定与正在定义的 SQL 函数的名称相同。建议相对于 $libdir（位于 $GPHOME/lib）或通过动态库路径（由 dynamic_library_path 服务器配置参数所设置）来定位共享库。如果新安装的版本位于不同的位置，则可以简化升级。

describe_function
当调用此函数的查询被解析时要执行回调函数的名称。回调函数返回一个指示结果类型的元组描述符。

## 注意
必须将自定义函数的任何编译的代码（共享库文件）放置在数据库的数组的（主机和段主机） 的每个主机上的相同位置。该位置必须位于 LD_LIBRARY_PATH 中，以便服务器找到文件。建议相对于 $libdir（位于 $GPHOME/lib）或者主机的动态库路径（dynamic_library_path）来配置参数，以定位共享库。

对于输入参数和返回值，允许使用完整的 SQL 类型语法，但是该类型的规范是由底层函数实现的，不能被 CREATE FUNCION 命令识别或强制执行。

数据库允许函数重载。只要具有不同的参数类型，相同的名字可以用于几个不同的函数。但是，所有函数的 C 名称必须不同，所以用户必须给重载 C 函数不同 C 名称（例如使用参数类型作为 C 名称的一部分）。

两个函数如果他们具有相同的名字和输入的参数类型，那他们就被认为是相同的，而不用考虑任何 OUT 参数。因此例如以下声明会产生冲突：

```sql
CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, out text) ...
```

具有不同参数类型列表的函数在创建的时候不会产生冲突，但是如果提供了参数的默认值，它们在使用中可能会产生冲突。例如，考虑：

```sql
CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, int default 42) ...
```

调用 foo(10)，由于不知道该调用那个函数，所以会产生函数调用失败（缺失可用默认值代替）。
当重复 CREATE FUNCTION 函数调用时，引用同一个对象文件，该文件只被加载一次。当卸载并重新加载文件时，请使用 LOAD 命令。

用户必须对具有语言的 USAGE 权限才能使用该语言定义函数。

使用美元引用来编写定义字符串，而不是普通单引号语法，这是有帮助的。没有美元引用，函数定义中的任何单引号或反斜杠必须通过双写来实现转义。
引用字符串由七个部分组成，第一个部分为美元符号（后续称$），第二部分由零个或多个字符组成的可选标记，第三部分为$，第四部分为任意字符串序列，第五部分为$，第六部分与第二部分相同，作为标签结束，第七部分同样为$。在引用字符串中，可以使用单引号，反斜杠，并且不需要任何转移字符，字符串始终以字面形式写入。例如，这里有两种不同方法来表示字符串“Dinaner’s horse”。

```sql
$$Dianne's horse$$
$SomeTag$Dianne's horse$SomeTag$
```

如果一个 SET 字句被附加到一个函数上，则在同一个变量的函数内部执行 SET LOCAL 命令的作用仅限于该函数；当函数退出时，配置参数的先前值仍然被恢复。但是，普通的SET命令（不带 LOCAL）将覆盖 CREATE FUNCTION SET 字句，与之前的 SET LOCAL 命令一样。这样命令的效果将在函数退出后持续，除非当前的事务被回滚。

如果具有 VARIADIC 参数的函数声明为 STRICT，则严格性检查将测试作为整体的可变数组是非空值。如果数组有空元素，PL/pgSQL 仍然会调用该函数。

**使用分布式数据查询功能**

一些情况下，数据库不支持在查询中使用函数，如果该查询的 FROM 子句指定表中的数据分布在数据库段上的话。例如， 该 SQL 查询包含函数 func()：

```sql
SELECT func(a) FROM table1;
```

如果遇到以下所有情况的话，则该函数不支持在查询中使用：
- 该 table1 表的数据分布在数据库段主机上。
- 函数 func() 从分布式表上读或修改数据。
- 函数 func() 返回多个行，或者使用来自 table1 的参数（a）。

如果任何以下的条件没有满足，则支持该函数，具体来说，如果满足以下任一条件，则支持该函数：
- 函数 func() 不能访问来自分布表的数据，也不能访问仅存在数据库主机上的数据。
- 表 table1 仅仅是主机上的表。
- 函数 func() 仅返回一行并且仅接受常量值的输入参数。如果可以将该函数改为不需要输入参数，则支持此功能。

## 示例
一个简单的加法函数：

```sql
CREATE FUNCTION add(integer, integer) RETURNS integer
    AS 'select $1 + $2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;
```

在 PL/pgSQL 中增加使用参数名称的整数：

```sql
CREATE OR REPLACE FUNCTION increment(i integer) RETURNS 
integer AS $$
        BEGIN
                RETURN i + 1;
        END;
$$ LANGUAGE plpgsql;
```

为 PL/pgSQL 函数增加每个查询的默认段主机内存：

```sql
CREATE OR REPLACE FUNCTION function_with_query() RETURNS 
SETOF text AS $$
        BEGIN
                RETURN QUERY
                EXPLAIN ANALYZE SELECT * FROM large_table;
        END;
$$ LANGUAGE plpgsql
SET statement_mem='256MB';
```

使用多态返回 ENUM 数组：

```sql
CREATE TYPE rainbow AS ENUM('red','orange','yellow','green','blue','indigo','violet');
CREATE FUNCTION return_enum_as_array( anyenum, anyelement, anyelement ) 
    RETURNS TABLE (ae anyenum, aa anyarray) AS $$
    SELECT $1, array[$2, $3] 
$$ LANGUAGE SQL STABLE;
SELECT * FROM return_enum_as_array('red'::rainbow, 'green'::rainbow, 'blue'::rainbow);
```

返回多个输出参数的记录：

```sql
CREATE FUNCTION dup(in int, out f1 int, out f2 text)
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;
SELECT * FROM dup(42);
```

用户可以使用明确命名的复合类型更详细地做同样的事情：

```sql
CREATE TYPE dup_result AS (f1 int, f2 text);
CREATE FUNCTION dup(int) RETURNS dup_result
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;
SELECT * FROM dup(42);
```

## 兼容性
CREATE FUNCTION 被定义在 SQL:1999 和之后。该数据库版本是相似的，但是不完全兼容。属性不可移植，不同可用语言也不可移植。
为了和其他数据库系统的兼容，argmode 可以写在 argname 之前或者之后。但是只有第一种是复合标准的。
SQL 标准没有指明参数的默认值。

## 另见
ALTER FUNCTION、DROP FUNCTION、LOAD
