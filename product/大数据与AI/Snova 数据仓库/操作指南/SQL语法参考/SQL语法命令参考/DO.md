执行匿名的代码块作为暂时匿名函数。

## 概要

```sql
DO [ LANGUAGE lang_name ] code
```

## 描述

DO 执行了一个匿名代码块，或换而言之为一个程序化语言的暂时的匿名函数。

该代码块被认为似乎是一个没有参数的函数体，返回空值。它被解析被执行了一次。

可选参数 LANGUAGE 子句可以出现在代码块的前或者后。

匿名块是程序化语言结构，该结构提供在运行时创建和执行程序代码的能力，而不用将代码作为数据库对象持久的存储在系统目录中。匿名代码块的概念和 UNIX shell 脚本相似，能允许将多个手动输入命令分组并作为一步骤执行。顾名思义，匿名块没有名字，因此不能被其他对象引用。虽然动态创建，匿名块可以轻松的作为脚本存储在操作系统文件中以便重复执行。

匿名块是标准程序语言块。他们携带语法并且遵循适用于该程序语言的规则，包括变量的声明和作用于执行异常处理和语言使用。

匿名块的编译和执行结合在一个步骤中，而用户定义的函数需要在每次定义变更之前重新定义。

## 参数
code
需要执行的程序化语言代码。这必须指定为字符串文本。正如使用 CREATE FUNCTION 命令。建议使用$引用文字。可选关键字无效。支持这些程序语言：PL/pgSQL（plpgsql）、PL/Python（plpythonu）和 PL/Perl（plperl 和plperlu）。

lang_name
代码所用程序语言的名字。该语言默认是 plpgsql。该语言必须在数据库中安装并且在用户数据库中注册。

## 注意
PL/pgSQL 语言安装在数据库系统中并且注册在用户创建的数据库中。PL/Python 语言是默认安装的，但是没有注册。其他语言没有安装也没有注册。系统目录 pg_language 包含了在数据库中注册语言的信息。

如果语言不可信，则用户必须有对程序语言有 USAGE 权限，或者必须是超级用户。这和使用该语言创建函数的权限要求一样。

## 示例

该 PL/pgSQL 示例对 webuser 用户赋予在 *public* 模式中所有视图的所有权限：

```sql
DO $$DECLARE r record;
BEGIN
    FOR r IN SELECT table_schema, table_name FROM information_schema.tables
             WHERE table_type = 'VIEW' AND table_schema = 'public'
    LOOP
        EXECUTE 'GRANT ALL ON ' || quote_ident(r.table_schema) || '.' || quote_ident(r.table_name) || ' TO webuser';
    END LOOP;
END$$;
```

该 PL/pgSQL 示例决定是否数据库用户是超级用户。在示例中，匿名块检索从临时表的输入值：

```sql
CREATE TEMP TABLE list AS VALUES ('gpadmin') DISTRIBUTED RANDOMLY;
 
DO $$ 
DECLARE
  name TEXT := 'gpadmin' ;
  superuser TEXT := '' ;
  t1_row   pg_authid%ROWTYPE;
BEGIN
  SELECT * INTO t1_row FROM pg_authid, list 
     WHERE pg_authid.rolname = name ;
  IF t1_row.rolsuper = 'f' THEN
    superuser := 'not ';
  END IF ;
  RAISE NOTICE 'user % is %a superuser', t1_row.rolname, superuser ;
END $$ LANGUAGE plpgsql ;
```

注意：示例 PL/pgSQL 使用 SELECT 和 INTO 子句。它和 SQL 命令的 SELECT INTO 语句不同。

## 兼容性
SQL 标准中没有 DO 语句。

## 另见
CREATE LANGUAGE 
