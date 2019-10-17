把一个运行时参数的值恢复到默认值。

## 概要

```sql
RESET configuration_parameter
 
RESET ALL
```

## 描述
RESET 把运行时参数恢复到它们的默认值。RESET 是 SET *configuration_parameter* TO DEFAULT 的另外一种写法。

默认值被定义为如果在当前会话中没有发出过 SET，参数必须具有的值。这个值的实际来源可能是一个编译在内部的默认值、 配置文件（postgresql.conf）、命令行选项、或者针对每个数据库或者每个用户的默认设置。

## 参数
configuration_parameter
一个可设置的运行时参数名称。 

ALL
把所有可设置的运行时参数重置为默认值。

## 示例
将 statement_mem 设置为其默认值：
```sql
RESET statement_mem; 
```

## 兼容性
RESET 是数据库的扩展。

## 另见
SET
