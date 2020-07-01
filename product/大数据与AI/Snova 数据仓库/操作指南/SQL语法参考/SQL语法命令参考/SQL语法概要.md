### 终止
终止当前事务。

```sql
ABORT [WORK | TRANSACTION]
```

### 修改聚集函数
改变聚集函数的定义。

```sql
ALTER AGGREGATE name ( type [ , ... ] ) RENAME TO new_name
 
ALTER AGGREGATE name ( type [ , ... ] ) OWNER TO new_owner
 
ALTER AGGREGATE name ( type [ , ... ] ) SET SCHEMA new_schema
```

### 修改转换
修改转换的定义。

```sql
ALTER CONVERSION name RENAME TO newname
 
ALTER CONVERSION name OWNER TO newowner
```

### 修改数据库
修改数据库属性。

```sql
ALTER DATABASE name [ WITH CONNECTION LIMIT connlimit ]
 
ALTER DATABASE name SET parameter { TO | = } { value | DEFAULT }
 
ALTER DATABASE name RESET parameter
 
ALTER DATABASE name RENAME TO newname
 
ALTER DATABASE name OWNER TO new_owner
```

### 修改域
改变域的定义。

```sql
ALTER DOMAIN name { SET DEFAULT expression | DROP DEFAULT }
 
ALTER DOMAIN name { SET | DROP } NOT NULL
 
ALTER DOMAIN name ADD domain_constraint
 
ALTER DOMAIN name DROP CONSTRAINT constraint_name [RESTRICT | CASCADE]
 
ALTER DOMAIN name OWNER TO new_owner
 
ALTER DOMAIN name SET SCHEMA new_schema
```

### 修改扩展
改变在数据库中注册的扩展的定义。

```sql
ALTER EXTENSION name UPDATE [ TO new_version ]
ALTER EXTENSION name SET SCHEMA new_schema
ALTER EXTENSION name ADD member_object
ALTER EXTENSION name DROP member_object
 
其中 member_object 是：
 
  ACCESS METHOD object_name |
  AGGREGATE aggregate_name ( aggregate_signature ) |
  CAST (source_type AS target_type) |
  COLLATION object_name |
  CONVERSION object_name |
  DOMAIN object_name |
  EVENT TRIGGER object_name |
  FOREIGN DATA WRAPPER object_name |
  FOREIGN TABLE object_name |
  FUNCTION function_name ( [ [ argmode ] [ argname ] argtype [, ...] ] ) |
  MATERIALIZED VIEW object_name |
  OPERATOR operator_name (left_type, right_type) |
  OPERATOR CLASS object_name USING index_method |
  OPERATOR FAMILY object_name USING index_method |
  [ PROCEDURAL ] LANGUAGE object_name |
  SCHEMA object_name |
  SEQUENCE object_name |
  SERVER object_name |
  TABLE object_name |
  TEXT SEARCH CONFIGURATION object_name |
  TEXT SEARCH DICTIONARY object_name |
  TEXT SEARCH PARSER object_name |
  TEXT SEARCH TEMPLATE object_name |
  TRANSFORM FOR type_name LANGUAGE lang_name |
  TYPE object_name |
  VIEW object_name
 
aggregate_signature 是：
 
* | [ argmode ] [ argname ] argtype [ , ... ] |
  [ [ argmode ] [ argname ] argtype [ , ... ] ] 
    ORDER BY [ argmode ] [ argname ] argtype [ , ... ]
```

### 修改外部表
改变外部表的定义。

```sql
ALTER EXTERNAL TABLE name RENAME [COLUMN] column TO new_column
 
ALTER EXTERNAL TABLE name RENAME TO new_name
 
ALTER EXTERNAL TABLE name SET SCHEMA new_schema
 
ALTER EXTERNAL TABLE name action [, ... ]
```

### 修改文件空间
改变文件空间的定义。

```sql
ALTER FILESPACE name RENAME TO newname
 
ALTER FILESPACE name OWNER TO newowner
```

### 修改函数
改变函数的定义。

```sql
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   action [, ... ] [RESTRICT]
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] )
   RENAME TO new_name
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   OWNER TO new_owner
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   SET SCHEMA new_schema
```

### 修改组
改变角色名字或者成员信息。

```sql
ALTER GROUP groupname ADD USER username [, ... ]
 
ALTER GROUP groupname DROP USER username [, ... ]
 
ALTER GROUP groupname RENAME TO newname
```

### 修改索引
改变索引的定义。

```sql
ALTER INDEX name RENAME TO new_name
 
ALTER INDEX name SET TABLESPACE tablespace_name
 
ALTER INDEX name SET ( FILLFACTOR = value )
 
ALTER INDEX name RESET ( FILLFACTOR )
```

### 修改语言
改变程序语言的名字。

```sql
ALTER LANGUAGE name RENAME TO newname
ALTER LANGUAGE name OWNER TO new_owner
```

### 修改操作符
改变操作符的定义。

```sql
ALTER OPERATOR name ( {lefttype | NONE} , {righttype | NONE} ) 
   OWNER TO newowner
```

### 修改操作符类
改变操作符类的定义。

```sql
ALTER OPERATOR CLASS name USING index_method RENAME TO newname
 
ALTER OPERATOR CLASS name USING index_method OWNER TO newowner
```

### 修改操作符族
修改操作符族的定义。

```sql
ALTER OPERATOR FAMILY name USING index_method ADD
  {  OPERATOR strategy_number operator_name ( op_type, op_type ) [ RECHECK ]
    | FUNCTION support_number [ ( op_type [ , op_type ] ) ] funcname ( argument_type [, ...] )
  } [, ... ]
ALTER OPERATOR FAMILY name USING index_method DROP
  {  OPERATOR strategy_number ( op_type, op_type ) 
    | FUNCTION support_number [ ( op_type [ , op_type ] ) 
  } [, ... ]
 
ALTER OPERATOR FAMILY name USING index_method RENAME TO newname
 
ALTER OPERATOR FAMILY name USING index_method OWNER TO newowner
```

### 修改协议
修改协议的定义。

```sql
ALTER PROTOCOL name RENAME TO newname
 
ALTER PROTOCOL name OWNER TO newowner
```

### 修改资源队列
修改资源队列的限制。

```sql
ALTER RESOURCE QUEUE name WITH ( queue_attribute=value [, ... ] ) 
```

### 修改角色
修改数据库角色（用户或组）。

```sql
ALTER ROLE name RENAME TO newname
 
ALTER ROLE name SET config_parameter {TO | =} {value | DEFAULT}
 
ALTER ROLE name RESET config_parameter
 
ALTER ROLE name RESOURCE QUEUE {queue_name | NONE}
 
ALTER ROLE name [ [WITH] option [ ... ] ]
```

### 修改模式
改变模式的定义。

```sql
ALTER SCHEMA name RENAME TO newname
 
ALTER SCHEMA name OWNER TO newowner
```

### 修改序列
改变序列生成器的定义。

```sql
ALTER SEQUENCE name [INCREMENT [ BY ] increment] 
     [MINVALUE minvalue | NO MINVALUE] 
     [MAXVALUE maxvalue | NO MAXVALUE] 
     [RESTART [ WITH ] start] 
     [CACHE cache] [[ NO ] CYCLE] 
     [OWNED BY {table.column | NONE}]
 
ALTER SEQUENCE name RENAME TO new_name
 
ALTER SEQUENCE name SET SCHEMA new_schema
```

### 修改表
改变的表的定义。

```sql
ALTER TABLE [ONLY] name RENAME [COLUMN] column TO new_column
 
ALTER TABLE name RENAME TO new_name
 
ALTER TABLE name SET SCHEMA new_schema
 
ALTER TABLE [ONLY] name SET 
     DISTRIBUTED BY (column, [ ... ] ) 
   | DISTRIBUTED RANDOMLY 
   | WITH (REORGANIZE=true|false)
 
ALTER TABLE [ONLY] name action [, ... ]
 
ALTER TABLE name
   [ ALTER PARTITION { partition_name | FOR (RANK(number)) 
   | FOR (value) } partition_action [...] ] 
   partition_action
```

### 修改表空间
改变表空间的定义。

```sql
ALTER TABLESPACE name RENAME TO newname
 
ALTER TABLESPACE name OWNER TO newowner
```

### 修改类型
改变数据类型的定义。

```sql
ALTER TYPE name
   OWNER TO new_owner | SET SCHEMA new_schema
```

### 修改用户
修改数据库角色（用户）的定义。

```sql
ALTER USER name RENAME TO newname
 
ALTER USER name SET config_parameter {TO | =} {value | DEFAULT}
 
ALTER USER name RESET config_parameter
 
ALTER USER name [ [WITH] option [ ... ] ]
```

### 修改视图
改变视图的定义。

```sql
ALTER VIEW name RENAME TO newname
```

### 分析
收集关于数据库的数据。

```sql
ANALYZE [VERBOSE] [ROOTPARTITION [ALL] ] 
   [table [ (column [, ...] ) ]]
```

### 开始
启动事务块。

```sql
BEGIN [WORK | TRANSACTION] [transaction_mode]
      [READ ONLY | READ WRITE]
```

### 检查点
强制事务记录检查点。

```sql
CHECKPOINT
```

### 关闭
关闭游标。

```sql
CLOSE cursor_name
```

### 集簇
根据索引对磁盘上的堆存储表进行物理重新排序。不是数据库的推荐操作。

```sql
CLUSTER indexname ON tablename
 
CLUSTER tablename
 
CLUSTER
```

### 注释
定义或者修改对一个对象的注释。

```sql
COMMENT ON
{ TABLE object_name |
  COLUMN table_name.column_name |
  AGGREGATE agg_name (agg_type [, ...]) |
  CAST (sourcetype AS targettype) |
  CONSTRAINT constraint_name ON table_name |
  CONVERSION object_name |
  DATABASE object_name |
  DOMAIN object_name |
  FILESPACE object_name |
  FUNCTION func_name ([[argmode] [argname] argtype [, ...]]) |
  INDEX object_name |
  LARGE OBJECT large_object_oid |
  OPERATOR op (leftoperand_type, rightoperand_type) |
  OPERATOR CLASS object_name USING index_method |
  [PROCEDURAL] LANGUAGE object_name |
  RESOURCE QUEUE object_name |
  ROLE object_name |
  RULE rule_name ON table_name |
  SCHEMA object_name |
  SEQUENCE object_name |
  TABLESPACE object_name |
  TRIGGER trigger_name ON table_name |
  TYPE object_name |
  VIEW object_name } 
IS 'text'
```

### 提交
提交当前事务。

```sql
COMMIT [WORK | TRANSACTION]
```

### 复制
在文件和表之间拷贝数据。

```sql
COPY table [(column [, ...])] FROM {'file' | STDIN}
     [ [WITH] 
       [BINARY]
       [OIDS]
       [HEADER]
       [DELIMITER [ AS ] 'delimiter']
       [NULL [ AS ] 'null string']
       [ESCAPE [ AS ] 'escape' | 'OFF']
       [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
       [CSV [QUOTE [ AS ] 'quote'] 
            [FORCE NOT NULL column [, ...]]
       [FILL MISSING FIELDS]
       [[LOG ERRORS]  
       SEGMENT REJECT LIMIT count [ROWS | PERCENT] ]
 
COPY {table [(column [, ...])] | (query)} TO {'file' | STDOUT}
      [ [WITH] 
        [ON SEGMENT]
        [BINARY]
        [OIDS]
        [HEADER]
        [DELIMITER [ AS ] 'delimiter']
        [NULL [ AS ] 'null string']
        [ESCAPE [ AS ] 'escape' | 'OFF']
        [CSV [QUOTE [ AS ] 'quote'] 
             [FORCE QUOTE column [, ...]] ]
      [IGNORE EXTERNAL PARTITIONS ]
```

### 创建聚集函数
定义一个新的聚集函数。

```sql
CREATE [ORDERED] AGGREGATE name (input_data_type [ , ... ]) 
      ( SFUNC = sfunc,
        STYPE = state_data_type
        [, PREFUNC = prefunc]
        [, FINALFUNC = ffunc]
        [, INITCOND = initial_condition]
        [, SORTOP = sort_operator] )
```

### 创建投影
定义一个新的投影。

```sql
CREATE CAST (sourcetype AS targettype) 
       WITH FUNCTION funcname (argtypes) 
       [AS ASSIGNMENT | AS IMPLICIT]
 
CREATE CAST (sourcetype AS targettype) WITHOUT FUNCTION 
       [AS ASSIGNMENT | AS IMPLICIT]
```

### 创建转换
定义一个新的编码转换。

```sql
CREATE [DEFAULT] CONVERSION name FOR source_encoding TO 
     dest_encoding FROM funcname
```

### 创建数据库
创建一个信息的数据库。

```sql
CREATE DATABASE name [ [WITH] [OWNER [=] dbowner]
                     [TEMPLATE [=] template]
                     [ENCODING [=] encoding]
                     [TABLESPACE [=] tablespace]
                     [CONNECTION LIMIT [=] connlimit ] ]
```

### 创建域
定义一个新的域。

```sql
CREATE DOMAIN name [AS] data_type [DEFAULT expression] 
       [CONSTRAINT constraint_name
       | NOT NULL | NULL 
       | CHECK (expression) [...]]
```

### 创建扩展
在数据库中注册一个扩展。

```sql
CREATE EXTENSION [ IF NOT EXISTS ] extension_name
  [ WITH ] [ SCHEMA schema_name ]
           [ VERSION version ]
           [ FROM old_version ]
           [ CASCADE ]
```

### 创建外部表
定义一张外部表。

```sql
CREATE [READABLE] EXTERNAL TABLE table_name     
    ( column_name data_type [, ...] | LIKE other_table )
     LOCATION ('file://seghost[:port]/path/file' [, ...])
       | ('gpfdist://filehost[:port]/file_pattern[#transform=trans_name]'
           [, ...]
       | ('gpfdists://filehost[:port]/file_pattern[#transform=trans_name]'
           [, ...])
       | ('gphdfs://hdfs_host[:port]/path/file')
       | ('s3://S3_endpoint[:port]/bucket_name/[S3_prefix]
             [region=S3-region]
            [config=config_file]')
     [ON MASTER]
     FORMAT 'TEXT' 
           [( [HEADER]
              [DELIMITER [AS] 'delimiter' | 'OFF']
              [NULL [AS] 'null string']
              [ESCAPE [AS] 'escape' | 'OFF']
              [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
              [FILL MISSING FIELDS] )]
          | 'CSV'
           [( [HEADER]
              [QUOTE [AS] 'quote'] 
              [DELIMITER [AS] 'delimiter']
              [NULL [AS] 'null string']
              [FORCE NOT NULL column [, ...]]
              [ESCAPE [AS] 'escape']
              [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
              [FILL MISSING FIELDS] )]
          | 'AVRO' 
          | 'PARQUET'
          | 'CUSTOM' (Formatter=<formatter_specifications>)
    [ ENCODING 'encoding' ]
      [ [LOG ERRORS] SEGMENT REJECT LIMIT count
      [ROWS | PERCENT] ]
 
CREATE [READABLE] EXTERNAL WEB TABLE table_name     
   ( column_name data_type [, ...] | LIKE other_table )
      LOCATION ('http://webhost[:port]/path/file' [, ...])
    | EXECUTE 'command' [ON ALL 
                          | MASTER
                          | number_of_segments
                          | HOST ['segment_hostname'] 
                          | SEGMENT segment_id ]
      FORMAT 'TEXT' 
            [( [HEADER]
               [DELIMITER [AS] 'delimiter' | 'OFF']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CSV'
            [( [HEADER]
               [QUOTE [AS] 'quote'] 
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE NOT NULL column [, ...]]
               [ESCAPE [AS] 'escape']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CUSTOM' (Formatter=<formatter specifications>)
     [ ENCODING 'encoding' ]
     [ [LOG ERRORS] SEGMENT REJECT LIMIT count
       [ROWS | PERCENT] ]
 
CREATE WRITABLE EXTERNAL TABLE table_name
    ( column_name data_type [, ...] | LIKE other_table )
     LOCATION('gpfdist://outputhost[:port]/filename[#transform=trans_name]'
          [, ...])
      | ('gpfdists://outputhost[:port]/file_pattern[#transform=trans_name]'
          [, ...])
      | ('gphdfs://hdfs_host[:port]/path')
      FORMAT 'TEXT' 
               [( [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] 'quote'] 
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE QUOTE column [, ...]] ]
               [ESCAPE [AS] 'escape'] )]
           | 'AVRO' 
           | 'PARQUET'
 
           | 'CUSTOM' (Formatter=<formatter specifications>)
    [ ENCODING 'write_encoding' ]
    [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
 
CREATE WRITABLE EXTERNAL TABLE table_name
    ( column_name data_type [, ...] | LIKE other_table )
     LOCATION('s3://S3_endpoint[:port]/bucket_name/[S3_prefix]
            [region=S3-region]
            [config=config_file]')
      [ON MASTER]
      FORMAT 'TEXT' 
               [( [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] 'quote'] 
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE QUOTE column [, ...]] ]
               [ESCAPE [AS] 'escape'] )]
 
CREATE WRITABLE EXTERNAL WEB TABLE table_name
    ( column_name data_type [, ...] | LIKE other_table )
    EXECUTE 'command' [ON ALL]
    FORMAT 'TEXT' 
               [( [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] 'quote'] 
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE QUOTE column [, ...]] ]
               [ESCAPE [AS] 'escape'] )]
           | 'CUSTOM' (Formatter=<formatter specifications>)
    [ ENCODING 'write_encoding' ]
    [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
```

### 创建函数
定义一个新的函数。

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

### 创建组
定义一个新的数据库角色。

```sql
CREATE GROUP name [ [WITH] option [ ... ] ]
```

### 创建索引
定义一个新的索引。

```sql
CREATE [UNIQUE] INDEX name ON table
       [USING btree|bitmap|gist]
       ( {column | (expression)} [opclass] [, ...] )
       [ WITH ( FILLFACTOR = value ) ]
       [TABLESPACE tablespace]
       [WHERE predicate]
```

### 创建语言
定义一个新的程序语言。

```sql
CREATE [PROCEDURAL] LANGUAGE name
 
CREATE [TRUSTED] [PROCEDURAL] LANGUAGE name
       HANDLER call_handler [ INLINE inline_handler ] [VALIDATOR valfunction]
```

### 创建操作符
定义一个新的操作符。

```sql
CREATE OPERATOR name ( 
       PROCEDURE = funcname
       [, LEFTARG = lefttype] [, RIGHTARG = righttype]
       [, COMMUTATOR = com_op] [, NEGATOR = neg_op]
       [, RESTRICT = res_proc] [, JOIN = join_proc]
       [, HASHES] [, MERGES]
       [, SORT1 = left_sort_op] [, SORT2 = right_sort_op]
       [, LTCMP = less_than_op] [, GTCMP = greater_than_op] )
```

### 创建操作符类
定义一个新的操作符类。

```sql
CREATE OPERATOR CLASS name [DEFAULT] FOR TYPE data_type  
  USING index_method AS 
  { 
  OPERATOR strategy_number op_name [(op_type, op_type)] [RECHECK]
  | FUNCTION support_number funcname (argument_type [, ...] )
  | STORAGE storage_type
  } [, ... ]
```

### 创建操作符族
定义一个新的操作符族。

```sql
CREATE OPERATOR FAMILY name  USING index_method  
```

### 创建协议
注册自定义数据访问协议，当定义数据库外部表时可以指定。

```sql
CREATE [TRUSTED] PROTOCOL name (
   [readfunc='read_call_handler'] [, writefunc='write_call_handler']
   [, validatorfunc='validate_handler' ])
```

### 创建资源队列
定义一个新的资源队列。

```sql
CREATE RESOURCE QUEUE name WITH (queue_attribute=value [, ... ])
```

### 创建角色
定义一个新的数据库角色（用户或组）。

```sql
CREATE ROLE name [[WITH] option [ ... ]]
```

### 创建规则
定义一个新的重写规则。

```sql
CREATE [OR REPLACE] RULE name AS ON event
  TO table [WHERE condition] 
  DO [ALSO | INSTEAD] { NOTHING | command | (command; command 
  ...) }
```

### 创建模式
定义一个新的模式。

```sql
CREATE SCHEMA schema_name [AUTHORIZATION username] 
   [schema_element [ ... ]]
 
CREATE SCHEMA AUTHORIZATION rolename [schema_element [ ... ]]
```

### 创建序列
定义一个新的序列生成器。

```sql
CREATE [TEMPORARY | TEMP] SEQUENCE name
       [INCREMENT [BY] value] 
       [MINVALUE minvalue | NO MINVALUE] 
       [MAXVALUE maxvalue | NO MAXVALUE] 
       [START [ WITH ] start] 
       [CACHE cache] 
       [[NO] CYCLE] 
       [OWNED BY { table.column | NONE }]
```

### 创建表
定义一个新的表。

```sql
CREATE [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name ( 
[ { column_name data_type [ DEFAULT default_expr ] 
   [column_constraint [ ... ]
[ ENCODING ( storage_directive [,...] ) ]
] 
   | table_constraint
   | LIKE other_table [{INCLUDING | EXCLUDING} 
                      {DEFAULTS | CONSTRAINTS}] ...}
   [, ... ] ]
   )
   [ INHERITS ( parent_table [, ... ] ) ]
   [ WITH ( storage_parameter=value [, ... ] )
   [ ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP} ]
   [ TABLESPACE tablespace ]
   [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
   [ PARTITION BY partition_type (column)
       [ SUBPARTITION BY partition_type (column) ] 
          [ SUBPARTITION TEMPLATE ( template_spec ) ]
       [...]
    ( partition_spec ) 
        | [ SUBPARTITION BY partition_type (column) ]
          [...]
    ( partition_spec
      [ ( subpartition_spec
           [(...)] 
         ) ] 
    )
```

### 创建表如（AS）
从查询的结果中定义一个新的表。

```sql
CREATE [ [GLOBAL | LOCAL] {TEMPORARY | TEMP} ] TABLE table_name
   [(column_name [, ...] )]
   [ WITH ( storage_parameter=value [, ... ] ) ]
   [ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP}]
   [TABLESPACE tablespace]
   AS query
   [DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY]
```

### 创建表空间
定义一个新的表空间。

```sql
CREATE TABLESPACE tablespace_name [OWNER username] 
       FILESPACE filespace_name
```

### 创建类型
定义一个新的类型。

```sql
CREATE TYPE name AS ( attribute_name data_type [, ... ] )
 
CREATE TYPE name AS ENUM ( 'label' [, ... ] )
 
CREATE TYPE name (
    INPUT = input_function,
    OUTPUT = output_function
    [, RECEIVE = receive_function]
    [, SEND = send_function]
    [, TYPMOD_IN = type_modifier_input_function ]
    [, TYPMOD_OUT = type_modifier_output_function ]
    [, INTERNALLENGTH = {internallength | VARIABLE}]
    [, PASSEDBYVALUE]
    [, ALIGNMENT = alignment]
    [, STORAGE = storage]
    [, DEFAULT = default]
    [, ELEMENT = element]
    [, DELIMITER = delimiter] )
 
CREATE TYPE name
```

### 创建用户
定义一个默认带有 LOGIN 权限的数据库角色。

```sql
CREATE USER name [ [WITH] option [ ... ] ]
```

### 创建视图
定义一个新的视图。

```sql
CREATE [OR REPLACE] [TEMP | TEMPORARY] VIEW name
       [ ( column_name [, ...] ) ]
       AS query
```

### 取消分配
取消分配一个已经准备（预编译）的语句。

```sql
DEALLOCATE [PREPARE] name
```

##### 声明
定义一个游标。

```sql
DECLARE name [BINARY] [INSENSITIVE] [NO SCROLL] CURSOR 
     [{WITH | WITHOUT} HOLD] 
     FOR query [FOR READ ONLY]
```

### 函数
从表中删除行。

```sql
DELETE FROM [ONLY] table [[AS] alias]
      [USING usinglist]
      [WHERE condition | WHERE CURRENT OF cursor_name ]
```

### 丢弃
丢弃会话的状态。

```sql
DISCARD { ALL | PLANS | TEMPORARY | TEMP }
```

### 删除聚集函数
删除聚集函数。

```sql
DROP AGGREGATE [IF EXISTS] name ( type [, ...] ) [CASCADE | RESTRICT]
```

### （做）DO
执行匿名代码块作为暂时匿名函数。

```sql
DO [ LANGUAGE lang_name ] code
```

### 删除投影
删除一个投影。

```sql
DROP CAST [IF EXISTS] (sourcetype AS targettype) [CASCADE | RESTRICT]
```

### 删除转换
删除一个转换。

```sql
DROP CONVERSION [IF EXISTS] name [CASCADE | RESTRICT]
```

### 删除数据库
删除一个数据库。

```sql
DROP DATABASE [IF EXISTS] name
```

### 删除域
删除一个域。

```sql
DROP DOMAIN [IF EXISTS] name [, ...]  [CASCADE | RESTRICT]
```

### 删除扩展
从数据库中删除一个扩展。

```sql
DROP EXTENSION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

### 删除外部表
删除一个外部表定义。

```sql
DROP EXTERNAL [WEB] TABLE [IF EXISTS] name [CASCADE | RESTRICT]
```

### 删除文件空间
删除一个文件空间。

```sql
DROP FILESPACE [IF EXISTS] filespacename
```

### 删除函数
删除一个函数。

```sql
DROP FUNCTION [IF EXISTS] name ( [ [argmode] [argname] argtype 
    [, ...] ] ) [CASCADE | RESTRICT]
```

### 删除组
删除一个数据库角色。

```sql
DROP GROUP [IF EXISTS] name [, ...]
```

### 删除索引
删除一个索引。

```sql
DROP INDEX [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 删除语言
删除一个程序语言。

```sql
DROP [PROCEDURAL] LANGUAGE [IF EXISTS] name [CASCADE | RESTRICT]
```

### 删除操作符
删除一个操作符。

```sql
DROP OPERATOR [IF EXISTS] name ( {lefttype | NONE} , 
    {righttype | NONE} ) [CASCADE | RESTRICT]
```

### 删除操作符类
删除一个操作符类。

```sql
DROP OPERATOR CLASS [IF EXISTS] name USING index_method [CASCADE | RESTRICT]
```

### 删除操作符族
删除一个操作符族。

```sql
DROP OPERATOR FAMILY [IF EXISTS] name USING index_method [CASCADE | RESTRICT]
```

### 删除拥有（owned）
删除数据库角色所拥有的数据库对象。

```sql
DROP OWNED BY name [, ...] [CASCADE | RESTRICT]
```

### 删除协议
从数据库中删除外部表的访问协议。

```sql
DROP PROTOCOL [IF EXISTS] name
```

### 删除资源队列
删除一个资源队列。

```sql
DROP RESOURCE QUEUE queue_name
```

### 删除角色
删除一个数据库角色。

```sql
DROP ROLE [IF EXISTS] name [, ...]
```

### 删除规则
删除一个重写规则。

```sql
DROP RULE [IF EXISTS] name ON relation [CASCADE | RESTRICT]
```

### 删除模式
删除一个模式。

```sql
DROP SCHEMA [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 删除序列
删除一个序列。

```sql
DROP SEQUENCE [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 删除表
删除一个表。

```sql
DROP TABLE [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 删除表空间
删除一个表空间。

```sql
DROP TABLESPACE [IF EXISTS] tablespacename
```

### 删除类型
删除一个数据类型。

```sql
DROP TYPE [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 删除用户
删除一个数据库角色。

```sql
DROP USER [IF EXISTS] name [, ...]
```

### 删除视图
删除一个视图。

```sql
DROP VIEW [IF EXISTS] name [, ...] [CASCADE | RESTRICT]
```

### 结束（END）
提交当前事务。

```sql
END [WORK | TRANSACTION]
```

### 执行
执行一个已经准备好的 SQL 语句。

```sql
EXECUTE name [ (parameter [, ...] ) ]
```

### 解释
展示语句的查询计划。

```sql
EXPLAIN [ANALYZE] [VERBOSE] statement
```

### 提取
使用游标获取查询结果的行。

```sql
FETCH [ forward_direction { FROM | IN } ] cursorname
```

### 授权
定义一个访问权限。

```sql
GRANT { {SELECT | INSERT | UPDATE | DELETE | REFERENCES | 
TRIGGER | TRUNCATE } [,...] | ALL [PRIVILEGES] }
    ON [TABLE] tablename [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { {USAGE | SELECT | UPDATE} [,...] | ALL [PRIVILEGES] }
    ON SEQUENCE sequencename [, ...]
    TO { rolename | PUBLIC } [, ...] [WITH GRANT OPTION]
 
GRANT { {CREATE | CONNECT | TEMPORARY | TEMP} [,...] | ALL 
[PRIVILEGES] }
    ON DATABASE dbname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { EXECUTE | ALL [PRIVILEGES] }
    ON FUNCTION funcname ( [ [argmode] [argname] argtype [, ...] 
] ) [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { USAGE | ALL [PRIVILEGES] }
    ON LANGUAGE langname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { {CREATE | USAGE} [,...] | ALL [PRIVILEGES] }
    ON SCHEMA schemaname [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT { CREATE | ALL [PRIVILEGES] }
    ON TABLESPACE tablespacename [, ...]
    TO {rolename | PUBLIC} [, ...] [WITH GRANT OPTION]
 
GRANT parent_role [, ...] 
    TO member_role [, ...] [WITH ADMIN OPTION]
 
GRANT { SELECT | INSERT | ALL [PRIVILEGES] } 
    ON PROTOCOL protocolname
    TO username
```

### 插入
在表中创建新的行。

```sql
INSERT INTO table [( column [, ...] )]
   {DEFAULT VALUES | VALUES ( {expression | DEFAULT} [, ...] ) 
   [, ...] | query}
```

### 加载
加载或重新加载共享库文件。

```sql
LOAD 'filename'
```

### 锁
锁住一张表。

```sql
LOCK [TABLE] name [, ...] [IN lockmode MODE] [NOWAIT]
```

### 移动
放置一个游标。

```sql
MOVE [ forward_direction {FROM | IN} ] cursorname
```

### 准备
准备一个执行的语句。

```sql
PREPARE name [ (datatype [, ...] ) ] AS statement
```

### 重新分配拥有
改变数据库角色所拥有的数据库对象的所有权。

```sql
REASSIGN OWNED BY old_role [, ...] TO new_role
```

### 重新索引
重新构建索引。

```sql
REINDEX {INDEX | TABLE | DATABASE | SYSTEM} name
```

### 释放SAVEPOINT
销毁一个之前定义过的 savepoint。

```sql
RELEASE [SAVEPOINT] savepoint_name
```

### 重置
恢复系统配置参数的值为默认值。

```sql
RESET configuration_parameter
 
RESET ALL
```

### 撤销
撤销访问权限。

```sql
REVOKE [GRANT OPTION FOR] { {SELECT | INSERT | UPDATE | DELETE 
       | REFERENCES | TRIGGER | TRUNCATE } [,...] | ALL [PRIVILEGES] }
       ON [TABLE] tablename [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { {USAGE | SELECT | UPDATE} [,...] 
       | ALL [PRIVILEGES] }
       ON SEQUENCE sequencename [, ...]
       FROM { rolename | PUBLIC } [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { {CREATE | CONNECT 
       | TEMPORARY | TEMP} [,...] | ALL [PRIVILEGES] }
       ON DATABASE dbname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] {EXECUTE | ALL [PRIVILEGES]}
       ON FUNCTION funcname ( [[argmode] [argname] argtype
                              [, ...]] ) [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] {USAGE | ALL [PRIVILEGES]}
       ON LANGUAGE langname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [ CASCADE | RESTRICT ]
 
REVOKE [GRANT OPTION FOR] { {CREATE | USAGE} [,...] 
       | ALL [PRIVILEGES] }
       ON SCHEMA schemaname [, ...]
       FROM {rolename | PUBLIC} [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [GRANT OPTION FOR] { CREATE | ALL [PRIVILEGES] }
       ON TABLESPACE tablespacename [, ...]
       FROM { rolename | PUBLIC } [, ...]
       [CASCADE | RESTRICT]
 
REVOKE [ADMIN OPTION FOR] parent_role [, ...] 
       FROM member_role [, ...]
       [CASCADE | RESTRICT]
```

### 回滚
中止当前事务。

```sql
ROLLBACK [WORK | TRANSACTION]
```

### 回滚到SAVEPOINT
将当前事务回滚到某个 savepoint。

```sql
ROLLBACK [WORK | TRANSACTION] TO [SAVEPOINT] savepoint_name
```

### SAVEPOINT
在当前事务定义一个新的 savepoint。

```sql
SAVEPOINT savepoint_name
```

### 选择（SELECT）
从表或者视图中检索行。

```sql
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

### 选择到（SELECT INTO）
从查询结果中定义一个新的表。

```sql
[ WITH with_query [, ...] ]
SELECT [ALL | DISTINCT [ON ( expression [, ...] )]]
    * | expression [AS output_name] [, ...]
    INTO [TEMPORARY | TEMP] [TABLE] new_table
    [FROM from_item [, ...]]
    [WHERE condition]
    [GROUP BY expression [, ...]]
    [HAVING condition [, ...]]
    [{UNION | INTERSECT | EXCEPT} [ALL] select]
    [ORDER BY expression [ASC | DESC | USING operator] [NULLS {FIRST | LAST}] [, ...]]
    [LIMIT {count | ALL}]
    [OFFSET start]
    [FOR {UPDATE | SHARE} [OF table_name [, ...]] [NOWAIT] 
    [...]]
```

### 设置
改变数据库配置参数的值。

```sql
SET [SESSION | LOCAL] configuration_parameter {TO | =} value | 
    'value' | DEFAULT}
 
SET [SESSION | LOCAL] TIME ZONE {timezone | LOCAL | DEFAULT}
```

### 设置角色
设置当前会话当前角色的标识符。

```sql
SET [SESSION | LOCAL] ROLE rolename
 
SET [SESSION | LOCAL] ROLE NONE
 
RESET ROLE
```

### 设置会话授权
设置会话角色标识符和当前会话当前角色的标识符。

```sql
SET [SESSION | LOCAL] SESSION AUTHORIZATION rolename
 
SET [SESSION | LOCAL] SESSION AUTHORIZATION DEFAULT
 
RESET SESSION AUTHORIZATION
```

### 设置事务（SET TRANSACTION）
设置当前事务的特征。

```sql
SET TRANSACTION [transaction_mode] [READ ONLY | READ WRITE]
 
SET SESSION CHARACTERISTICS AS TRANSACTION transaction_mode 
     [READ ONLY | READ WRITE]
```

### 显示（SHOW）
显示当前系统配置参数的值。

```sql
SHOW configuration_parameter
 
SHOW ALL
```

### 开始事务
开始一个事务块。

```sql
START TRANSACTION [SERIALIZABLE | READ COMMITTED | READ UNCOMMITTED]
                  [READ WRITE | READ ONLY]
```

### 截断（TRUNCATE）
清空表的所有行。

```sql
TRUNCATE [TABLE] name [, ...] [CASCADE | RESTRICT]
```

### 更新
更新表的行。

```sql
UPDATE [ONLY] table [[AS] alias]
   SET {column = {expression | DEFAULT} |
   (column [, ...]) = ({expression | DEFAULT} [, ...])} [, ...]
   [FROM fromlist]
   [WHERE condition | WHERE CURRENT OF cursor_name ]
```

### 清理
垃圾收集和选择性分析数据库。

```sql
VACUUM [FULL] [FREEZE] [VERBOSE] [table]
 
VACUUM [FULL] [FREEZE] [VERBOSE] ANALYZE
              [table [(column [, ...] )]]
```

### 值
计算一组行。

```sql
VALUES ( expression [, ...] ) [, ...]
   [ORDER BY sort_expression [ASC | DESC | USING operator] [, ...]]
   [LIMIT {count | ALL}] [OFFSET start]
```

