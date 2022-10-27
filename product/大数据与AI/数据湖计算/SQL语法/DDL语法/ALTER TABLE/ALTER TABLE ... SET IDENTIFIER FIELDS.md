## 说明
- 支持内核：SparkSQL。
- 适用表类型：外部 Iceberg 表、原生 Iceberg 表。
- 用途：添加 identifier fields 属性。

## 语法
```
ALTER TABLE dempts SET IDENTIFIER FIELD empno, name
```


## 示例
```
ALTER TABLE tb1 SET IDENTIFIER FIELDS id, location.lon
```



