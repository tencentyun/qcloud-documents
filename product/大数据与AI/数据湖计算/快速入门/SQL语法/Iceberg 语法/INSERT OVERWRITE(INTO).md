行级数据插入操作。
## 语法
```
INSERT { OVERWRITE | INTO } [ TABLE ] table_name
    [ PARTITION clause ]
    { VALUES (column_values,...), (column_values,...)...
    | SELECT select_expr}
```


## 示例
```
CREATE TABLE IF NOT EXISTS `table_01` (
  `id` INTEGER,
  `num` int,
  `name` STRING
) USING `iceberg`

INSERT INTO table_01 PARTITION(name='21') VALUES (1,2), (2,3);
INSERT INTO TABLE table_01 VALUES (3,2,'abc'), (4,3,'abd');

```


