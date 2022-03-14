对于 SQL 作业，用户可以上传 [自定义程序包](https://console.cloud.tencent.com/oceanus/resource)，然后在作业分析开发页的参数设置中，引用该程序包。目前支持从本地上传，也可以引用账户下现有 COS 存储中的资源（仅限相同地域）。

这里的程序包既可以用来扩展 Connector 的功能，也可以创建自定义函数（UDF）。

## 语法
目前流计算 Oceanus 支持 Java 和 Scala 两种语言编写的程序包。当用户上传了自定义程序包后，在界面上关联后即可用下面的 CREATE FUNCTION 语句来声明：
```sql
CREATE TEMPORARY SYSTEM FUNCTION 函数名
  AS '函数类全名' [LANGUAGE JAVA|SCALA]
```
其中的**函数名**可以自行定义，但不要与现有的冲突。**函数类全名**为 Java 或 Scala 类的类全名（例如 `'com.example.flink.MyCustomFunction'`）。

## 命名覆盖
如果存在系统内置的同名函数时，用户使用上述语法创建的 UDF 会覆盖系统内置的函数。因此除非有意改变系统函数的功能，请不要创建与系统内置函数同名的自定义函数。

## 函数类型
目前 Flink 支持下面多种函数定义。

### 标量函数（Scalar Function）
标量函数简称 UDF，作用是将一个值转换为另一个值（一对一），例如系统内置的 `SUBSTRING`、`REPLACE` 等字符串操作函数，都属于标量函数。

### 表函数（Table Function）
表函数简称 UDTF，作用是将一个值转为表中的一行数据（一变多），这样可以在后续 JOIN 操作中作为右表。

### 聚合函数（Aggregate Function）
聚合函数简称 UDAGG，作用是将多行数据的一组值，聚合为一个最终值（多变一），例如系统内置的 `MAX`、`MIN`、`AVG` 等都属于聚合函数。

### 表聚合函数（Table Aggregate Function）
表聚合函数的作用是将多行数据的一组值，聚合为新的多行数据（多对多）。

### 异步表函数（Async Table Function）
异步表函数可作为一种特殊的数据源，例如可以通过它来对接外部的数据库、数据存储。

## UDF 开发指南
由于 Flink 不同版本间 API 和文档迭代频繁，可参考 Flink 官方文档中的 [UDF 开发指南](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/functions/udfs.html#%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)。目前流计算 Oceanus 兼容开源版的 Flink 1.11 版本 API。
