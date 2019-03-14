#### SET

更改一个数据库配置参数的值。

##### 概要

```sql
SET [SESSION | LOCAL] configuration_parameter {TO | =} value | 
    'value' | DEFAULT}
 
SET [SESSION | LOCAL] TIME ZONE {timezone | LOCAL | DEFAULT}
```

##### 描述

SET命令更改运行时配置参数。任何被分类到session的参数可以用SET即时更改。SET只影响当前会话所使用的值。

如果在一个事务内发出SET（或者等效的SET SESSION）而该事务后来 中止，在该事务被回滚时SET命令的效果会 消失。一旦所在的事务被提交，这些效果将会持续到会话结束（除非被另 一个SET所覆盖）。

SET LOCAL的效果只持续到当前事务结束， 不管事务是否被提交。一种特殊情况是在一个事务内SET后面跟着SET LOCAL：SET LOCAL值将会在该事务结束前一直可见， 但是之后（如果该事务被提交）SET值将会生效。

如果在一个函数内使用SET LOCAL并且该函数 还有对同一变量的SET选项（见**CREATE FUNCTION**），在函数退出时SET LOCAL命令的效果会消失。也就是说，该函数被调用时的值会被恢复。这允许用SET LOCAL在函数内动态地或者重复地更改一个参数，同时仍然能便利地使用SET选项来保存以及恢复调用 者的值。不过，一个常规的SET命令会覆盖它所在的任何函数的SET选项，除非回滚，它的效果将一直保持。

如果在一个事务中，使用 DECLARE创建了一个游标，那么久不能在该事务中使用SET命令，直到使用CLOSE命令关闭游标。

##### 参数

SESSION

指定该命令对当前会话有效（这是默认值）。

LOCAL

指定该命令只对当前事务有效。在COMMIT或者ROLLBACK之后，会话级别的设置会再次生效。注意SET LOCAL出现在事务块外部执行，不会有效果。

configuration_parameter

一个可设置运行时参数的名称。只有被分类为*session*类别的参数能够通过SET命令就行修改。 

value

参数的新值。根据特定的参数，值可以被指定为字符串常量、标识符、 数字或者以上构成的逗号分隔列表。写DEFAULT可以指定把该参数重置成它的默认值。如果指定内存大小伙子时间单位，则值包含在单引号中。

TIME ZONE

SET TIME ZONE value是 SET timezone TO value的一个别 名。语法SET TIME ZONE允许用于时区指定的特 殊语法。这里是合法值的例子：

'PST8PDT'

'Europe/Rome'

-7 (UTC 以西 7 小时的时区)

INTERVAL '-08:00' HOUR TO MINUTE (UTC 以西 8 小时的时区)。

LOCAL

DEFAULT

把时区设置为用户的本地时区（也就是说服务器的timezone默认值）。

##### 示例

设置模式搜索路径：

```sql
SET search_path TO my_schema, public;
```

增加每个查询的段主机内存到200MB：

```sql
SET statement_mem TO '200MB';
```

把日期风格设置为传统 POSTGRES的 "日在月之前"的输入习惯：

```sql
SET datestyle TO postgres, dmy;
```

设置时区为加州伯克利：

```sql
SET TIME ZONE 'PST8PDT';
```

设置时区为意大利：

```sql
SET TIME ZONE 'Europe/Rome'; 
```

##### 兼容性

SET TIME ZONE扩展了SQL标准定义的语法。

##### 另见

RESET, SHOW