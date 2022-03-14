从指定表中删除行。如果指定了 where 子句，则只删除匹配的行。否则，将删除表中的所有行。

## 语法
```
DELETE FROM table_name [ WHERE condition ]
```
## 参数
- [table_name]：表名。
- [where condition]：可选 where 条件，用于条件删除，如果不加则整张表删除。

## 示例
```
DELETE FROM lineitem WHERE shipmode = 'AIR';
```
```
DELETE FROM lineitem WHERE orderkey IN (SELECT orderkey FROM orders WHERE priority = 'LOW');
```
```
DELETE FROM orders;
```

## 限制
Spark 不支持该操作，需要使用其它方式替换，例如，可参考 [INSERT OVERWRITE STATEMENT](https://cloud.tencent.com/document/product/1342/61990) 方式去覆写表。
