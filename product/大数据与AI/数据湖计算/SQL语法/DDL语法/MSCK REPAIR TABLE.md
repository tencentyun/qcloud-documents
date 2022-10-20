## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：更新数据表的分区信息。

## 标准语法 
```
MSCK REPAIR TABLE table_identifier
```
## 参数
`table_identifier`：表的名称。

## 示例
```
MSCK REPAIR TABLE t1
```
