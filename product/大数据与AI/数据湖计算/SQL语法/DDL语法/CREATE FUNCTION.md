该语句允许创建一个由类名实现的函数。
## 语法
```
CREATE FUNCTION [db_name.]function_name AS class_name
  [USING JAR|FILE 'file_uri' [, JAR|FILE 'file_uri'] ]
```
## 参数
- `[db_name.]function_name`：函数名，创建函数的时候后指定命名空间在`db_name`下。
- class_name：类名。
- `[USING JAR|FILE 'file_uri' [, JAR|FILE 'file_uri'] ]`：使用 jar 包或者 File 创建函数，这里要指明远程文件系统 Tencent  COS 的路径。

## 示例
```
CREATE FUNCTION udf_add2 AS 'udf_add2'
USING JAR 'cosn://xxxxx/udf/hive-test-udfs.jar.
```
