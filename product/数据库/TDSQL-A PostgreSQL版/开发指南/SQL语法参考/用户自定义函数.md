用户可以通过语句 CREATE FUNCTION 定义一个新函数。CREATE OR REPLACE FUNCTION 将创建一个新函数或者替换一个现有的函数。要定义一个函数，用户必须具有该语言上的 USAGE 权限。新函数的名称不能匹配同一个模式中具有相同输入参数类型的任何现有函数，支持重载。

## PL/pgSQL 语言函数
PL/pgSQL 类似于 Oracle 的 PL/SQL，是一种可载入的过程语言。
用 PL/pgSQL 创建的函数可以被用在任何可以使用内建函数的地方。SQL 被大多数数据库用作查询语言。它是可移植的并且容易学习。但是每一个 SQL 语句必须由数据库服务器单独执行。这意味着客户端应用必须发送每一个查询到数据库服务器、等待它被处理、接收并处理结果、做一些计算，然后发送更多查询给服务器。如果客户端和数据库服务器不在同一台机器上，所有这些会引起进程间通信并且将带来网络负担。

通过 PL/pgSQL，可以将一整块计算和一系列查询分组在数据库服务器内部，这样就有了一种过程语言的能力，并且使 SQL 更易用，同时能节省的客户端/服务器通信开销。
- 客户端和服务器之间的额外往返通信被消除。
- 客户端不需要的中间结果不必被整理或者在服务器和客户端之间传送。
- 多轮的查询解析可以被避免。

PL/pgSQL 可以使用 SQL 中所有的数据类型、操作符和函数。其应用方法与存储过程相似，只是存储过程无返回值，函数有返回值。
示例：
```
CREATE FUNCTION one() RETURNS integer AS $$
SELECT 1 AS result;
$$ LANGUAGE SQL;
直接 select 进行调用
SELECT one();
```

## C/C++ 语言函数
用户定义的函数可以用 C\C++ 编写， 这类函数被编译成共享库（即 so 库文件），在创建之前上传到服务器上。动态载入是把“C 语言”函数和 “内部”函数区分开的特性，两者真正的编码习惯实际上是一样的。

### 编写代码
编写和编译 C 函数的基本规则如下：
在分配内存时，使用函数 palloc 和 pfree，而不是使用对应的 C 库函数 malloc 和 free。在每个事务结束时会自动释放通过palloc 分配的内存，以免内存泄露。
大部分的内部 TDSQL-A PostgreSQL版 的类型都声明在 postgres.h 中，不过函数管理器接口在 fmgr.h中，为了移植性，最好在其他系统或者用户头文件之前，先包括 postgres.h 和 fmgr.h。

创建的对象文件中定义的符号名不能和原库中的定义的符号名、操作系统的可执行程序中定义的符号互相冲突。
如：
```
extern "C"{
#include "postgres.h"
#include "fmgr.h"
 
PG_MODULE_MAGIC;
}
//加法
extern "C"{
PG_FUNCTION_INFO_V1(my_add_func);
Datum my_add_func(PG_FUNCTION_ARGS)
 {
 int32 a = PG_GETARG_INT32(0);
 int32 b = PG_GETARG_INT32(1);
 int64 result = a + b;
 PG_RETURN_INT64(result);
 }
}
```

### 编译和载入自定义函数
1、编译。
```
gcc -Wall -Werror -g3 -o my_func.o -fPIC -c my_func.cpp -I/data/tbase/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/include/postgresql/server/
```
2、生成 so 库文件。
```
gcc -shared -o my_func.so my_func.o
```
3、将库文件发送到每个 DN、CN 节点上，并赋予数据库用户角色权限，进行函数创建。
```
create function my_add_func(a integer,b integer) RETURNS integer
as '/data/tbase/my_func.so' ,'my_add_func' language c strict;
CREATE FUNCTION
进行函数查询
v3=# select my_add_func(1,2);
 my_add_func
\-------------
 3
(1 row)
```

## PL/Python 函数
在 TDSQL-A PostgreSQL版 使用 PL/Python 函数之前需要提前的创建拓展 plpythonu：
```
create extension plpythonu;
```

### 语法声明
PL/Python 中的函数通过标准的 [CREATE FUNCTION](http://postgres.cn/docs/10/sql-createfunction.html) 语法声明：
```
CREATE FUNCTION funcname (argument-list)
 RETURNS return-type
AS $$
 \# PL/Python 函数体
$$ LANGUAGE plpythonu;
```
函数体就是一个 Python 脚本。当函数被调用时，它的参数被当做列表 args 的元素传递，命名参数也被作为普通变量传递给 Python 脚本。使用命名参数通常可读性更好。Python 代码会以通常的方式返回结果，即使用 return 或者 yield（在结果集合语句的情况中）。如果没有提供一个返回值，Python 会返回默认的None。PL/Python 会把 Python 的 None 翻译成 SQL 空值。
例如，一个返回两个整数中较大的整数的函数可以定义为：
```
CREATE FUNCTION pymax (a integer, b integer)
 RETURNS integer
AS $$
 if a > b:
  return a
 return b
$$ LANGUAGE plpythonu;
```

作为该函数定义给出的 Python 代码会被转换成一个 Python 函数。例如上面的代码会得到：
```
def __plpython_procedure_pymax_23456():
 if a > b:
  return a
 return b
```

### 变量范围
参数被设置为全局变量。由于 Python 的可见范围规则，这会导致一种后果：在函数内不能把一个参数变量重新赋予给一个涉及该变量名称本身的表达式的值，除非在该代码块中重新声明该变量为全局的。例如，下面的代码无法工作：
```
CREATE FUNCTION pystrip(x text)
 RETURNS text
AS $$
 x = x.strip() # 错误
 return x
$$ LANGUAGE plpythonu;
```

因为对 x 的赋值让 x 成为了整个代码块的一个局部变量，并且因此该赋值操作右边的 x 引用的是一个还未赋值的局部变量x，而不是 PL/Python 函数的参数。通过使用 global 语句，可以让上面的代码正常工作：
```
CREATE FUNCTION pystrip(x text)
 RETURNS text
AS $$
 global x
 x = x.strip() # 现在好了
 return x
$$ LANGUAGE plpythonu;
```
但是不建议依赖于这类 PL/Python 的实现细节，最好把函数参数当作是只读。
