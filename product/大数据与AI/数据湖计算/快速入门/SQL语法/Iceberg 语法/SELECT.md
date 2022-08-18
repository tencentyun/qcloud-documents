查询数据。
## 语法

```
SELECT [ hints ] [ ALL | DISTINCT ] { named_expression | star_clause } [, ...]
  FROM from_item [, ...]
  [ LATERAL VIEW clause ]
  [ PIVOT clause ]
  [ WHERE clause ]
  [ GROUP BY clause ]
  [ HAVING clause]
  [ QUALIFY clause ]

from_item
{ table_name [ TABLESAMPLE clause ] [ table_alias ] |
  JOIN clause |
  [ LATERAL ] table_valued_function [ table_alias ] |
  VALUES clause |
  [ LATERAL ] ( query ) [ TABLESAMPLE clause ] [ table_alias ] }

named_expression
   expression [ column_alias ]

star_clause
   [ { table_name | view_name } . ] *
```



