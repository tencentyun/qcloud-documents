
DBMS_SQL 可以在应用的运行时间构建查询和其它的命令。DBMS_SQL 中可以使用的存储过程及函数如下表所示：

| 存储过程/函数                                                | 描述                                         |
| ------------------------------------------------------------ | -------------------------------------------- |
| BIND_VARIABLE(c, name, value [, out_value_size ])            | Bind a value to a variable                   |
| BIND_VARIABLE_CHAR(c, name, value [, out_value_size ])       | Bind a CHAR value to a variable              |
| BIND_VARIABLE_RAW(c, name, value [, out_value_size ])        | Bind a RAW value to a variable               |
| CLOSE_CURSOR(c IN OUT)                                       | Close a cursor                               |
| COLUMN_VALUE(c, position, value OUT [, column_error OUT [, actual_length OUT ]]) | Return a column value into a variable.       |
| COLUMN_VALUE_CHAR(c, position, value OUT [, column_error OUT [, actual_length OUT ]]) | Return a CHAR column value into a variable.  |
| COLUMN_VALUE_RAW(c, position, value OUT [, column_error OUT [, actual_length OUT ]]) | Return a RAW column value into a variable.   |
| DEFINE_COLUMN(c, position, column [, column_size ])          | Define a column in the SELECT list.          |
| DEFINE_COLUMN_CHAR(c, position, column, column_size)         | Define a CHAR column in the SELECT list.     |
| DEFINE_COLUMN_RAW(c, position, column, column_size)          | Define a RAW column in the SELECT list.      |
| DESCRIBE_COLUMNS                                             | Defines columns to hold a cursor result set. |
| EXECUTE(c)                                                   | Execute a cursor.                            |
| EXECUTE_AND_FETCH(c [, exact ])                              | Execute a cursor and fetch a single row.     |
| FETCH_ROWS(c)                                                | Fetch rows from the cursor.                  |
| IS_OPEN(c)                                                   | Check if a cursor is open.                   |
| LAST_ROW_COUNT                                               | Return cumulative number of rows fetched.    |
| OPEN_CURSOR                                                  | Open a cursor.                               |
| PARSE(c, statement, language_flag)                           | Parse a statement.                           |

示例：
```
set client_min_messages TO error;
CREATE EXTENSION IF NOT EXISTS dbms_sql;
set client_min_messages TO default;
    
do
$$
declare
c  int;
strval varchar;
intval int;
nrows  int default 30;
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'select ''ahoj'' || i, i from generate_series(1, :nrows) g(i)');
call dbms_sql.bind_variable(c, 'nrows', nrows);
call dbms_sql.define_column(c, 1, strval);
call dbms_sql.define_column(c, 2, intval);
perform dbms_sql.execute(c);
while dbms_sql.fetch_rows(c) > 0
loop
call dbms_sql.column_value(c, 1, strval);
call dbms_sql.column_value(c, 2, intval);
raise notice 'c1: %, c2: %', strval, intval;
end loop;
call dbms_sql.close_cursor(c);
end;
$$;
    
do
$$
declare
c  int;
strval varchar;
intval int;
nrows  int default 30;
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'select ''ahoj'' || i, i from generate_series(1, :nrows) g(i)');
call dbms_sql.bind_variable(c, 'nrows', nrows);
call dbms_sql.define_column(c, 1, strval);
call dbms_sql.define_column(c, 2, intval);
perform dbms_sql.execute(c);
while dbms_sql.fetch_rows(c) > 0
loop
strval := dbms_sql.column_value_f(c, 1, strval);
intval := dbms_sql.column_value_f(c, 2, intval);
raise notice 'c1: %, c2: %', strval, intval;
end loop;
call dbms_sql.close_cursor(c);
end;
$$;
    
create table foo
(
a int,
b varchar,
c numeric
);
    
do
$$
declare
c int;
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'insert into foo values(:a, :b, :c)');
for i in 1..100
loop
call dbms_sql.bind_variable(c, 'a', i);
call dbms_sql.bind_variable(c, 'b', 'Ahoj ' || i);
call dbms_sql.bind_variable(c, 'c', i + 0.033);
perform dbms_sql.execute(c);
end loop;
end;
$$;
    
select *
from foo
order by a;
truncate foo;
    
do
$$
declare
c int;
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'insert into foo values(:a, :b, :c)');
for i in 1..100
loop
perform dbms_sql.bind_variable_f(c, 'a', i);
perform dbms_sql.bind_variable_f(c, 'b', 'Ahoj ' || i);
perform dbms_sql.bind_variable_f(c, 'c', i + 0.033);
perform dbms_sql.execute(c);
end loop;
end;
$$;
    
select *
from foo
order by a;
truncate foo;

do
$$
declare
c  int;
a  int[];
b  varchar[];
ca numeric[];
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'insert into foo values(:a, :b, :c)');
a := ARRAY [1, 2, 3, 4, 5];
b := ARRAY ['Ahoj', 'Nazdar', 'Bazar'];
ca := ARRAY [3.14, 2.22, 3.8, 4];
    
call dbms_sql.bind_array(c, 'a', a);
call dbms_sql.bind_array(c, 'b', b);
call dbms_sql.bind_array(c, 'c', ca);
raise notice 'inserted rows %', dbms_sql.execute(c);
end;
$$;
    
select *
from foo
order by a;
truncate foo;
    
do
$$
declare
c  int;
a  int[];
b  varchar[];
ca numeric[];
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'insert into foo values(:a, :b, :c)');
a := ARRAY [1, 2, 3, 4, 5];
b := ARRAY ['Ahoj', 'Nazdar', 'Bazar'];
ca := ARRAY [3.14, 2.22, 3.8, 4];
    
call dbms_sql.bind_array(c, 'a', a, 2, 3);
call dbms_sql.bind_array(c, 'b', b, 3, 4);
call dbms_sql.bind_array(c, 'c', ca);
raise notice 'inserted rows %', dbms_sql.execute(c);
end;
$$;
    
select *
from foo
order by a;
truncate foo;
    
do
$$
declare
c  int;
a  int[];
b  varchar[];
ca numeric[];
begin
c := dbms_sql.open_cursor();
call dbms_sql.parse(c, 'select i, ''Ahoj'' || i, i + 0.003 from generate_series(1, 35) g(i)');
call dbms_sql.define_array(c, 1, a, 10, 1);
call dbms_sql.define_array(c, 2, b, 10, 1);
call dbms_sql.define_array(c, 3, ca, 10, 1);
    
perform dbms_sql.execute(c);
while dbms_sql.fetch_rows(c) > 0
loop
call dbms_sql.column_value(c, 1, a);
call dbms_sql.column_value(c, 2, b);
call dbms_sql.column_value(c, 3, ca);
raise notice 'a = %', a;
raise notice 'b = %', b;
raise notice 'c = %', ca;
end loop;
call dbms_sql.close_cursor(c);
end;
$$;
```

    
