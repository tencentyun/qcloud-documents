## 说明
- 支持内核：SparkSQL。
- 适用表类型：外部 Iceberg 表、原生 Iceberg 表。
- 用途：删除 identifier fields 属性。

## 语法
```
ALTER TABLE dempts DROP IDENTIFIER FIELD empno, name
```


## 示例
```
ALTER TABLE tb1 DROP IDENTIFIER FIELDS id, location.lon
```



