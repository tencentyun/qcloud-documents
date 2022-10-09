支持四段式的 Iceberg 表元数据查询，包括：history、snapshots、files、manifests。
## 语法
```
SELECT select_expr (, select_expr)*
FROM `Catalog`.`db`.`tableName${history|snapshots|files|manifests|partitions|all_data_files|all_manifests}`
[WHERE where_condition]
[LIMIT [offset,] rows]
```


## 示例
```
SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$history` ORDER BY snapshot_id DESC LIMIT 1;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$snapshots` ORDER BY snapshot_id LIMIT 1;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$files` ORDER BY file_size_in_bytes LIMIT 1;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$manifests` ORDER BY length LIMIT 1;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$partitions` LIMIT 10;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$all_data_files` LIMIT 10;

SELECT * FROM `DataLakeCatalog`.`validation`.`dempts$all_manifests` LIMIT 10;
```



