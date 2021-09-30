`SELECT` 语句：从零个或多个表中检索数据行。

### 语法

```
[ WITH with_query [ , ... ] ]
select_statement [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select_statement, ... ]
    [ ORDER BY { expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [ , ... ] } ]
    [ DISTRIBUTE BY { expression [, ... ] } ]
    [ LIMIT { ALL | expression } ]
```

`select_statement` 包含下列查询：

```
SELECT [ ALL | DISTINCT ] { [ [ named_expression | regex_column_names ] [ , ... ] | TRANSFORM (...) ] }
    FROM { from_item [ , ... ] }
    [ WHERE boolean_expression ]
    [ GROUP BY expression [ , ... ] ]
    [ HAVING boolean_expression ]
```
### 参数
大部分语句的解释可以参考 Select Statement 中。

特殊子句比如像：

`[ DISTRIBUTE BY { expression [, ... ] } ]`

指定一组表达式，通过这些表达式对结果行进行重新分区。

### 示例
Spark distribute by 语句：

```
select * from test_table distribute by f1
```
