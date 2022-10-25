## 说明
- 支持内核：SparkSQL。
- 适用表类型：外部 Iceberg 表、原生 Iceberg 表。
- 用途：修改分区表的数据分配策略。

## 语法
```
ALTER TABLE table_identifier 
WRITE DISTRIBUTED BY PARTITION  
[ LOCALLY ORDERED BY 
{col_name [ASC|DESC] [NULLS FIRST|LAST]}[, ...]] 
```


## 示例
```
ALTER TABLE dempts WRITE DISTRIBUTED BY PARTITION;
ALTER TABLE dempts WRITE DISTRIBUTED BY PARTITION LOCALLY ORDERED BY id;
```



