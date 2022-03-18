支持对数据表进行统计。
### 语法
```
ANALYZE TABLES [ { FROM | IN } database_name ] COMPUTE STATISTICS [ NOSCAN ]

ANALYZE TABLE table_identifier
[ PARTITION ( partition_col_name [ = partition_col_val ] [ , ... ] ) ]
COMPUTE STATISTICS [ NOSCAN | FOR COLUMNS col [ , ... ] | FOR ALL COLUMNS ]
```

### 参数
- `database_name`：需要计算统计信息的表所在的数据库。
- `table_identifier`：需要计算统计信息的表名。
- `partition_col_name`：需要计算统计信息的分区列名。
- `partition_col_value`：需要计算统计信息的分区列的值。

### 示例
```
ANALYZE TABLE students COMPUTE STATISTICS
ANALYZE TABLE students COMPUTE STATISTICS FOR COLUMNS name
ANALYZE TABLE db.students COMPUTE STATISTICS FOR COLUMNS name
ANALYZE TABLE students COMPUTE STATISTICS NOSCAN
ANALYZE TABLE students COMPUTE STATISTICS FOR all COLUMNS
ANALYZE TABLE db.students COMPUTE STATISTICS FOR all COLUMNS
ANALYZE TABLE students PARTITION (student_id) COMPUTE STATISTICS
ANALYZE TABLE students PARTITION (student_id = 111111) COMPUTE STATISTICS
ANALYZE TABLE db.students PARTITION (student_id = 111111, name = 'test') COMPUTE STATISTICS FOR all COLUMNS

ANALYZE TABLES COMPUTE STATISTICS
ANALYZE TABLES COMPUTE STATISTICS NOSCAN
ANALYZE TABLES from school_db COMPUTE STATISTICS NOSCAN
ANALYZE TABLES IN school_db COMPUTE STATISTICS NOSCAN
```



