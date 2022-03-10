## 简介

值结构化处理函数，包括 JSON 指定节点的值选取，XML 和 JSON 互转，判断值是否是 JSON。

## json_select 函数

#### 函数定义

通过 jmes 表达式，提取 JSON 字段值，并返回 jmes 提取结果的 JSON 字符串。

#### 语法描述

```sql
json_select(v(字段名), jmes="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值，可以通过其他函数提取字段值|string|是| -  | -  |
|jmes|jmes 表达式|string|是| -  | -  |

#### 示例

原始日志：
```
{"field": "{\"a\":{\"b\":{\"c\":{\"d\":\"success\"}}}}", "status": "500"}
```
加工规则：
```
fields_set("message", json_select(v("field"), jmes="a.b.c.d"))
```
加工结果：
```
{"field":"{\"a\":{\"b\":{\"c\":{\"d\":\"success\"}}}}","message":"success","status":"500"}
```


## xml_to_json 函数

#### 函数定义

解析 XML 值并转换为 JSON 字符串，输入值必须为 XML 字符串结构，否则会导致转换异常。

#### 语法描述

```sql
xml_to_json(字段值)
```

#### 参数说明
| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值|string|是| -  | -  |


#### 示例

原始日志：
```
{"xml_field": "<note><to>B</to><from>A</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>", "status": "500"}
```
加工规则：
```
fields_set("json_field", xml_to_json(v("xml_field")))
```
加工结果：
```
{"xml_field":"<note><to>B</to><from>A</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>","json_field":"{\"to\":\"B\",\"from\":\"A\",\"heading\":\"Reminder\",\"body\":\"Don't forget me this weekend!\"}","status":"500"}
```


## json_to_xml 函数 

#### 函数定义

解析 JSON 字符串值并转换为 XML 字符串。

#### 语法描述

```sql
json_to_xml(字段值)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值|string|是| -  | -  |

#### 示例

原始日志：
```
{"json_field":"{\"to\":\"B\",\"from\":\"A\",\"heading\":\"Reminder\",\"body\":\"Don't forget me this weekend!\"}", "status": "200"}
```
加工规则：
```
fields_set("xml_field", json_to_xml(v("json_field")))
```
加工结果：
```
{"json_field":"{\"to\":\"B\",\"from\":\"A\",\"heading\":\"Reminder\",\"body\":\"Don't forget me this weekend!\"}","xml_field":"<ObjectNode><to>B</to><from>A</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></ObjectNode>","status":"200"}
```


## if_json 函数

#### 函数定义

判断是否为 JSON 字符串。

#### 语法描述

```sql
if_json(字段值)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
|data|字段值|string|是| -  | -  |

#### 示例
- 示例1
原始日志：
```
{"condition":"{\"a\":\"b\"}","status":"500"}
```
加工语句：
```
t_if(if_json(v("condition")), fields_set("new", 1))
```
加工结果：
```
{"new":"1","condition":"{\"a\":\"b\"}","status":"500"}
```
- 示例2
原始日志：
```
{"condition":"haha","status":"500"}
```
加工语句：
```
t_if(if_json(v("condition")), fields_set("new", 1))
```
加工结果：
```
{"condition":"haha","status":"500"}
```
