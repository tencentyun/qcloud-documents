## 简介

字符串处理函数，支持字符串长度计算、大小写转换、拼接字符串、替换、剔除、查找字符所在位置、前后缀匹配等。
需要注意的是，正则和字符串函数使用的场景并不相同。**正则更加适合于**在非结构化的日志中提取字段和字段值。例如，在如下的日志中提取 log_time、log_level，正则更为合适。  
```
{
    “日志内容”: "2021-12-02 14:33:35.022 [1] INFO  org.apache.Load - Response:status: 200, resp msg: OK, resp content: {    \"TxnId\": 58322,    \"Label\": \"flink_connector_20211202_1de749d8c80015a8\",    \"Status\": \"Success\",    \"Message\": \"OK\",    \"TotalRows\": 1,    \"LoadedRows\": 1,    \"FilteredRows\": 0,  \"CommitAndPublishTimeMs\": 16}"
}  
```
而**字符串函数更加适用于**在结构化日志数据中，对某个字段值进行处理。例如：
```
"resonsebody": {"method": "GET","user": "Tom"}
```

## str_count 函数

#### 函数定义

在值中指定范围内查找子串，返回子串出现的次数。

#### 语法描述

```sql
str_count(值, sub="", start=0, end=-1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|sub|准备查找的子字符串|string|是| -  | -  |
|start|查找的起始位置|number|否|默认为0| -  |
|end|查找的结束位置|number|否|默认为-1| -  |

#### 示例
原始日志：
```
{"data": "warn,error,error"}
```
加工规则：
```
fields_set("result", str_count(v("data"), sub="err"))
```
加工结果：
```
{"result":"2","data":"warn,error,error"}
```

## str_len 函数

#### 函数定义

返回字符串长度。

#### 语法描述

```sql
str_len(值)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |

#### 示例

原始日志：
```
{"data": "warn,error,error"}
```
加工规则：
```
fields_set("result", str_len(v("data")))
```
加工结果：
```
{"result":"16","data":"warn,error,error"}
```

## str_uppercase 函数

#### 函数定义

返回大写字符串。

#### 语法描述

```sql
str_uppercase(值)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |

#### 示例
原始日志：
```
{"data": "warn,error,error"}
```
加工规则：
```
fields_set("result", str_uppercase(v("data")))
```
加工结果：
```
{"result":"WARN,ERROR,ERROR","data":"warn,error,error"}
```

## str_lowercase 函数

#### 函数定义

返回小写字符串。

#### 语法描述

```sql
str_lowercase(值)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |

#### 示例

原始日志：
```
fields_set("result", str_lowercase(v("data")))
```
加工规则：
```
{"data": "WARN,ERROR,ERROR"}
```
加工结果：
```
{"result":"warn,error,error","data":"WARN,ERROR,ERROR"}
```

## str_join 函数

#### 函数定义

使用拼接字符串，拼接多值。

#### 语法描述

```
str_join(拼接字符串1, 值1, 值2, ...)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|join|字符串类型的值|string|是| -  | -  |
|值参数，可变参数列表|字符串类型的值|string|是| -  | -  |

#### 示例
原始日志：
```
{"data": "WARN,ERROR,ERROR"}
```
加工规则：
```
fields_set("result", str_join(",", v("data"), "INFO"))
```
加工结果：
```
{"result":"WARN,ERROR,ERROR,INFO","data":"WARN,ERROR,ERROR"}
```

## str_replace 函数

#### 函数定义

替换字符串，返回替换结果字符串。

#### 语法描述

```sql
str_replace(值, old="", new="", count=0)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| - | - |
|old|将要被替换的字符串|string|是| - | - |
|new|替换的目标字符串|string|是| - | - |
|count|最大替换次数，默认全部替换|number|否|默认为0| - |

#### 示例

将字段 data 的值中的 "WARN" 替换为 "ERROR"。

原始日志：
```
{"data": "WARN,ERROR,ERROR"}
```
加工规则：
```
fields_set("result", str_replace( v("data"), old="WARN", new="ERROR"))
```
将替换的结果保存到新字段 "result" 中。
加工结果：
```
{"result":"ERROR,ERROR,ERROR","data":"WARN,ERROR,ERROR"}
```

## str_format 函数

#### 函数定义

格式化字符串，返回格式化结果。

#### 语法描述

```
str_format(格式化字符串, 值1, 值2, ...)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|format|目标格式，占位符使用{}，例如："The disk \"{1}\" contains {0} file(s)."。其中{}中的数字，对应后面参数值的序号，从0开始。具体使用可参考 [MessageFormat.format](https://docs.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) 函数的使用 |string|是| -  | -  |
|值参数，可变参数列表|字符串类型的值|string|是| -  | -  |


#### 示例

原始日志：
```
{"status": 200, "message":"OK"}
```
加工规则：
```
fields_set("result", str_format("status:{0}, message:{1}", v("status"), v("message")))
```
加工结果：
```
{"result":"status:200, message:OK","message":"OK","status":"200"}
```

## str_strip 函数

#### 函数定义

剔除用户指定的字符序列中的字符，从字符串开头和结尾同时剔除，返回剔除后的结果。

#### 语法描述

```
str_strip(值, chars="\t\r\n")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|chars|将要被剔除的字符序串|string|否|\t\r\n| -  |


#### 示例
- 示例1
原始日志：
```
{"data": " abc  "}
```
加工规则：
```
fields_set("result", str_strip(v("data"), chars=" "))
```
加工结果：
```
{"result":"abc","data":" abc  "}
```
- 示例2
原始日志：
```
{"data": " **abc**  "}
```
加工规则：
```
fields_set("result", str_strip(v("data"), chars=" *"))
```
加工结果：
```
{"result":"abc","data":" **abc**  "}
```

## str_lstrip 函数

#### 函数定义

剔除用户指定的字符序列中的字符，从字符串左侧开头剔除，返回剔除后的结果。

#### 语法描述

```sql
str_strip(值, chars="\t\r\n")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|chars|将要被剔除的字符序串|string|否|\t\r\n| -  |


#### 示例
原始日志：
```
{"data": " abc  "}
```
加工规则：
```
fields_set("result", str_lstrip(v("data"), chars=" "))
```
加工结果：
```
{"result":"abc  ","data":" abc  "}
```

## str_rstrip 函数

#### 函数定义

剔除用户指定的字符序列中的字符，从字符串右侧结尾部分剔除，返回剔除后的结果。

#### 语法描述

```sql
str_strip(值, chars="\t\r\n")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|chars|将要被剔除的字符序串|string| 否  |\t\r\n| -  |

#### 示例

原始日志：
```
{"data": " abc  "}
```
加工规则：
```
fields_set("result", str_rstrip(v("data"), chars=" "))
```
加工结果：
```
{"result":" abc","data":" abc  "}
```

## str_find 函数

#### 函数定义

在值中查找子串，并返回子串出现的位置。

#### 语法描述

```sql
str_find(值, sub="", start=0, end=-1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|sub|准备查找的子字符串|string|是| -  | -  |
|start|查找的起始位置|number|否|默认为0| -  |
|end|查找的结束位置|number|否 |默认为-1| -  |


#### 示例
原始日志：
```
{"data": "warn,error,error"}
```
加工规则：
```
fields_set("result", str_find(v("data"), sub="err"))
```
加工结果：
```
{"result":"5","data":"warn,error,error"}
```

## str_start_with 函数

#### 函数定义

判断字符串是否以指定前缀开头。

#### 语法描述

```sql
str_start_with(值, sub="", start=0, end=-1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|sub|前缀字符串或字符|string|是| -  | -  |
|start|查找的起始位置|number|否|默认为0| -  |
|end|查找的结束位置|number|否 |默认为-1| -  |


#### 示例
- 示例1
原始日志：
```
{"data": "something"}
```
加工规则：
```
fields_set("result", str_start_with(v("data"), sub="some"))
```
加工结果：
```
{"result":"true","data":"something"}
```
- 示例2
原始日志：
```
{"data": "something"}
```
加工规则：
```
fields_set("result", str_start_with(v("data"), sub="*"))
```
加工结果：
```
{"result":"false","data":"something"}
```

## str_end_with 函数

#### 函数定义

判断字符串是否以指定前缀开头。

#### 语法描述

```
str_end_with(值, sub="", start=0, end=-1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字符串类型的值|string|是| -  | -  |
|sub|前缀字符串或字符|string|是| -  | -  |
|start|查找的起始位置|number|否|默认为0| -  |
|end|查找的结束位置|number|否|默认为-1| -  |

#### 示例

原始日志：
```
{"data": "endwith something"}
```
加工规则：
```
fields_set("result", str_end_with(v("data"), sub="ing"))
```
加工结果：
```
{"result":"true","data":"endwith something"}
```
