## 简介

日志中的时间处理函数，包括将 Date 类型转为 String 类型、时间类字段值和 UTC 时间互转以及获取当前时间。

## dt_str 函数

#### 函数定义

将时间类的字段值（特定格式的日期字符串或者时间戳），转换为指定时区、格式的目标日期字符串。

#### 语法描述

```sql
dt_str(值, format="格式化字符串", zone="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值，可支持的解析格式可参考 [dateparser](https://github.com/sisyphsu/dateparser)  | string | 是 | -  | -  |
|format |格式化日期格式可参考 [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) | string | 否 | -  | -  |
|zone|默认 UTC 时间，不指定时区。时区定义可参考 [ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html) |string| 否 |UTC+00:00| -  |

#### 示例

原始日志：
```
{"date":"2014-04-26 13:13:44 +09:00"}
```
加工规则：
```
fields_set("result", dt_str(v("date"), format="yyyy-MM-dd HH:mm:ss", zone="UTC+8"))
```
加工结果：
```
{"date":"2014-04-26 13:13:44 +09:00","result":"2014-04-26 12:13:44"}
```


## dt_to_timestamp 函数

#### 函数定义

将时间类的字段值（特定格式的日期字符串），同时指定字段对应的时区，转换为 UTC 时间戳。

#### 语法描述

```sql
dt_to_timestamp(值, zone="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值，可支持的解析格式可参考 [dateparser](https://github.com/sisyphsu/dateparser)|string|是| -  | -  |
|zone|默认 UTC 时间，不指定时区。如果指定此值，则必须和时间字段值对应，否则会出现时区错误问题。时区定义可参考 [ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html) |string| 否 |UTC+00:00| -  |

#### 示例 

原始日志：
```
{"date":"2021-10-26 15:48:15"}
```
加工规则：
```
fields_set("result", dt_to_timestamp(v("date"), zone="UTC+8"))
```
加工结果：
```
{"date":"2021-10-26 15:48:15","result":"1635234495000"}
```


## dt_from_timestamp 函数

#### 函数定义

将时间类的时间戳字段，指定目标时区后，转换为时间字符串。

#### 语法描述

```sql
dt_from_timestamp(值, zone="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值，可支持的解析格式可参考 [dateparser](https://github.com/sisyphsu/dateparser)|string|是| -  | -  |
|zone|默认 UTC 时间，不指定时区。时区定义可参考 [ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html)|string|否|UTC+00:00| -  |


#### 示例
原始日志：
```
{"date":"1635234495000"}
```
加工规则：
```
fields_set("result", dt_from_timestamp(v("date"), zone="UTC+8"))
```
加工结果：
```
{"date":"1635234495000","result":"2021-10-26 15:48:15"}
```

## dt_now 函数

#### 函数定义

获取加工计算时的本地时间。

#### 语法描述

```
dt_now(format="格式化字符串", zone="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|format|格式化日期格式，可参考[DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html)|string|否| -  | -  |
|zone|默认 UTC 时间，不指定时区。时区定义可参考 [ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html) |string|否|UTC+00:00| -  |

#### 示例
原始日志：
```
{"date":"1635234495000"}
```
加工规则：
```
fields_set("now", dt_now(format="yyyy-MM-dd HH:mm:ss", zone="UTC+8"))
```
加工结果，仅参考，具体结果和系统时间相关：
```
{"date":"1635234495000","now":"2021-MM-dd HH:mm:ss"}
```
