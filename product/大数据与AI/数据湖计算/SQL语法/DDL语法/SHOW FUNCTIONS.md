## 说明
- 支持内核：Presto、SparkSQL。
- 用途：显示函数创建语法。

## 语法
```
SHOW FUNCTIONS [ [ LIKE ] { function_name | regex_pattern } 
```


## 参数
- `function_name`：函数名称。
- `regex_pattern`：需要过滤出函数名称的正则表达式。

## 示例
```
SHOW FUNCTIONS

SHOW FUNCTIONS trim;

SHOW FUNCTIONS LIKE 't*'
SHOW FUNCTIONS LIKE 'yea*|windo*'
SHOW FUNCTIONS LIKE 't[a-z][a-z][a-z]'
```
