移除这个表中所有存在的列并用一个这个集合的列去替换原表中的列，可使用 REPLACE 语法来删除列并保留一些列。
## 语法
```
ALTER TABLE table_name 
 [PARTITION 
   (partition_col1_name = partition_col1_value
   [,partition_col2_name = partition_col2_value][,...])]
 REPLACE COLUMNS (col_spec[, col_spec ...])
```
## 参数
- table_name：表名。
- PARTITION：指定分区，分区列和值相对应。
- `(col_spec[, col_spec ...])`：用指定的列名和数据类型替换现有列。

## 示例
表：
```
ALTER TABLE orders REPLACE COLUMNS 
(
    eid INT, 
    empid Int,
    ename STRING 
    name String
);
```
分区表：
```
ALTER TABLE orders PARTITION (year='2021') REPLACE COLUMNS 
(
    eid INT, 
    empid Int,
    ename STRING 
    name String
);
```
