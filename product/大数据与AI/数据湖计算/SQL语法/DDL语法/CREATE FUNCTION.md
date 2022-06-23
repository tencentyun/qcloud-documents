该创建一个由类名实现的函数。
## 语法
```
CREATE  FUNCTION [db_name.]function_name AS class_name
 [USING JAR|FILE|ARCHIVE 'file_uri' [, JAR|FILE|ARCHIVE 'file_uri'] ];
```
## 参数
- `[db_name.]function_name`：函数名称，创建函数的时候后指定命名空间在 `db_name` 下。
- `class_name`：函数的实现类。
- `USING JAR|FILE|ARCHIVE 'file_uri'` ：函数资源的路径。

## 示例
```
CREATE FUNCTION `MYFUNC` AS 'myclass' USING JAR 'hdfs:///path/to/jar'
```

```
CREATE FUNCTION `MYFUNC` AS 'myclass' USING "JAR 'hdfs:///path/to/jar', FILE 'file:///usr/local/'
```
