## enrich_table 函数

#### 函数定义

使用 CSV 结构数据对日志中的字段进行匹配，当值相同时，可以将 CSV 中的其他字段和值添加到源日志中。

#### 语法描述

```sql
enrich_table(csv数据字符串, csv列名字符串, output=目标字段名或列表, mode="overwrite")
```

#### 参数说明

| 参数名称  | 参数描述  | 参数类型  | 是否必须  | 参数默认值 | 参数取值范围 |
|-----------  |  ----------- |  ----------- | ----------- | -------------- |  --------------  |
|data  | 输入的 CSV 数据，第一行为列名，其余行对应值。例如：region,count\nbj, 200\ngz, 300    |string    | 是    | -   | -   |
|fields  |待匹配列名称。CSV 中的字段名称，与实际日志中同名的字段进行匹配。单个字段名或以英文半角逗号拼接的多个新字段名   |string   | 是   | -   | -   |
|output  |输出字段列表，单个字段名或以英文半角逗号拼接的多个新字段名    |string        | 是      | -       |      -          |
|mode  |新字段的写入模式。默认强制覆盖|string  | 否   |  overwrite  | -     |


#### 示例

原始日志：
```
{"region": "gz"}
```
加工规则：
```
enrich_table("region,count\nbj,200\ngz,300", "region", output="count")
```
加工结果：
```
{"count":"300","region":"gz"}
```

## enrich_dict 函数 

#### 函数定义

使用 dict 结构对日志中的字段值进行匹配，当指定的字段的值和 dict 中的 key 相同时，将此 key 对应的 value 赋值给日志中的另一字段。

#### 语法描述

```sql
enrich_dict(dict数据字符串, 源字段名, output=目标字段, mode="overwrite")
```

#### 参数说明

| 参数名称  | 参数描述  | 参数类型  | 是否必须  | 参数默认值 | 参数取值范围 |
|-----------  |  ----------- |  ----------- | ----------- | -------------- |  --------------  |
| data  | 输入的 dict 数据，这里必须是 JSON 对象的转义字符串，例如：enrich_dict("{\"200\":\"SUCCESS\",\"500\":\"FAILED\"}", "status", output="message")  | string | 是 | -  | -  |
| fields | 待匹配字段名称。当 dict 中的 key 和指定字段对应的值相同时，匹配成功。单个字段名或以英文半角逗号拼接的多个新字段名  | string | 是   | -   | -  |
|output | 目标字段列表。匹配成功后，将 dict 中对应的 value 写入到目标字段列表。单个字段名或以英文半角逗号拼接的多个新字段名 | string  |  是  | -   | -   |
| mode  |新字段的写入模式。默认强制覆盖    | string  | 否  |overwrite  | -   |

#### 示例

原始日志：
```
{"status": "500"}
```
加工规则：
```
enrich_dict("{\"200\":\"SUCCESS\",\"500\":\"FAILED\"}", "status", output="message")
```
加工结果：
```
{"message":"FAILED","status":"500"}
```
