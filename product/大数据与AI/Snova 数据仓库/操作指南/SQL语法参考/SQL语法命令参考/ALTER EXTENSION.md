更改在数据库中注册的扩展的定义。

## 概要

```sql
ALTER EXTENSION name UPDATE [ TO new_version ]
ALTER EXTENSION name SET SCHEMA new_schema
ALTER EXTENSION name ADD member_object
ALTER EXTENSION name DROP member_object
 
其中 member_object是：
 
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

## 描述
ALTER EXTENSION 更改已安装扩展的定义。有几种子形式：

UPDATE
此形式将扩展更新到一个较新版本。该扩展必须提供一个合适的更新脚本（或一系列脚本），可以将当前安装的版本修改为所要求的版本。

SET SCHEMA
这种形式将扩展对象移动到另一个模式中。扩展名必须是“可重定位”。

ADD member_object
这种形式将一个现有对象添加到该扩展中。这在扩展更新脚本中很有用。该对象后续将被当作该扩展的一个成员。尤其是该对象只有通过删除扩展才能删除。

DROP member_object
这种形式从扩展中删除一个成员对象。这主要对扩展更新脚本有用。只有撤销该对象与其扩展之间的关联后才能删除该对象。

用户必须拥有扩展权限，且对被操作的扩展进行 ALTER EXTENSION.ADD 和 DROP 操作时，需要走对应扩展的所有权。

## 参数
name
一个已安装扩展的名称。

new_version
新版本的扩展。new_version 可以是标识符或字符串文字。如果未指定，该命令将尝试更新到扩展控制文件中的默认版本。

new_schema
扩展的新模式。

object_name

aggregate_name

function_name

operator_name
要从该扩展增加或者移除的对象的名称。表、聚集、域、外部表、函数、 操作符、操作符类、操作符族、序列、文本搜索对象、类型和视图的名称可以被方案限定。

source_type
该转换的源数据类型的名称。

target_type
cast的目标数据类型的名称。

argmode
函数或聚集参数的模式：IN、OUT、INOUT、VARIADIC。默认为 IN。
该命令忽略了 OUT 参数。 只需要输入参数来确定函数的身份。列出 IN、INOUT、VARIADIC 参数就足够。

argname
函数或聚集参数的名称。
该命令忽略参数名称，因为只需要参数数据类型来确定函数标识。

argtype
函数或聚集参数的数据类型。

left_type

right_type
操作符参数的数据类型（可以是方案限定）。指定 NONE 对于一个前缀或后缀操作符的缺失的参数。

PROCEDURAL
是一个噪声词。

type_name
该转换的数据类型的名称。

lang_name
该转换的语言的名称。

## 示例
要将 hstore 扩展更新为2.0版本：

```sql
ALTER EXTENSION hstore UPDATE TO '2.0';
```

更改 hstore 的扩展模式为 utils：

```sql
ALTER EXTENSION hstore SET SCHEMA utils;
```

要将现有函数添加到 hstore 扩展中：

```sql
ALTER EXTENSION hstore ADD FUNCTION populate_record(anyelement, hstore);
```

## 兼容性
ALTER EXTENSION 是一个数据库扩展。

## 参考
CREATE EXTENSION、DROP EXTENSION
