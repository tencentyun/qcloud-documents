## 简介

对一行日志进行处理，包括过滤、分发、分裂等函数。
![](https://qcloudimg.tencent-cloud.cn/raw/f34421c534c3aa04aa79240584846983.jpg)

## log_output 函数

#### 函数定义

输出到指定的目标主题。可以配合分支条件使用，也可以单独使用。

#### 语法描述

log_output(别名)，别名在配置加工任务时定义。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0c4e3f2d99257c6f8e607b56798e04db.jpg)

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
| alias | 目标主题的别名 | string | 是 | -   | -   |

#### 示例

按照 loglevel 字段值为 waring/info/error 的情况，分发到三个不同的日志主题中。

原始日志：
```
[
  {
    "loglevel": "warning"
  },
  {
    "loglevel": "info"
  },
  {
    "loglevel": "error"
  }
]
```
加工规则：
```
//按照loglevel字段值为waring/info/error的情况，分发到三个不同的日志主题中。
t_switch(regex_match(v("loglevel"),regex="info"),log_output("info_log"),regex_match(v("loglevel"),regex="warning"),log_output("warning_log"),regex_match(v("loglevel"),regex="error"),log_output("error_log"))
```
加工结果：如下图所示
![](https://qcloudimg.tencent-cloud.cn/raw/0e99dd62ca4f13f4d5260310ad4a2648.jpg)


## log_split 函数

#### 函数定义

使用分隔符结合 jmes 表达式，对特定字段进行拆分，拆分结果分裂为多行日志。

#### 语法描述

```sql
log_split(字段名, sep=",", quote="\"", jmes="", output="")
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
| field  | 待提取的字段名 | string | 是  | - | -  |
| sep  | 分隔符 | string | 否 | , | 任意单字符  |
| quote  |将值包括起来的字符  | string | 否 | -  | -  |
| jmes  | jmes 表达式，详情请参考 [JMESPath](https://jmespath.org/) | string  | 否 | -  | -  |
| output  |单个字段名  |string  | 是  | -  | -  |

#### 示例

- 示例1：字段中有多个值的日志分裂
```
{"field": "hello Go,hello Java,hello python","status":"500"}
```
加工规则：
```
//使用分割符“，”，将日志分隔成三条。
log_split("field", sep=",",  output="new_field")
```
加工结果：
```
{"new_field":"hello Go","status":"500"}
{"new_field":"hello Java","status":"500"}
{"new_field":"hello python","status":"500"}
```
- 示例2：利用 JMES 对日志进行分裂。
```
{"field": "{\"a\":{\"b\":{\"c\":{\"d\":\"a,b,c\"}}}}", "status": "500"}
```
加工规则：
```
//a.b.c.d节点的值为“a,b,c”
log_split("field", jmes="a.b.c.d",  output="new_field")
```
加工结果：
```
{"new_field":"a","status":"500"}
{"new_field":"b","status":"500"}
{"new_field":"c","status":"500"}
```
- 示例3：包含有 JSON 数组的日志分裂。
```
{"field": "{\"a\":{\"b\":{\"c\":{\"d\":[\"a\",\"b\",\"c\"]}}}}", "status": "500"}
```
加工规则：
```
log_split("field", jmes="a.b.c.d",  output="new_field")
```
加工结果：
```
{"new_field":"a","status":"500"}
{"new_field":"b","status":"500"}
{"new_field":"c","status":"500"}
```


## log_drop 函数
 
#### 函数定义

丢弃符合条件的日志。

#### 语法描述

```sql
log_drop(条件1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
| condition | 返回值为 bool 类型的函数表达式 | bool | 是  | -  | -  |


#### 示例

丢弃 status=200的日志，其余保留。

原始日志：
```
{"field": "a,b,c", "status": "500"}
{"field": "a,b,c", "status": "200"}
```
加工规则：
```
log_drop(op_eq(v("status"), 200))
```
加工结果：
```
{"field":"a,b,c","status":"500"}
```


## log_keep 函数

#### 函数定义

保留符合条件的日志。

#### 语法描述

```sql
log_keep(条件1)
```

#### 参数说明

| 参数名称 | 参数描述 | 参数类型 | 是否必须 | 参数默认值 | 参数取值范围 |
|----------- | ----------- | ----------- | ----------- | -------------- | -------------- |
| condition | 返回值为 bool 类型的函数表达式 | bool | 是 | -  | -  |


#### 示例

保留 status=500的日志，其余丢弃。

原始日志：
```
{"field": "a,b,c", "status": "500"}
{"field": "a,b,c", "status": "200"}
```
加工规则：
```
log_keep(op_eq(v("status"), 500))
```
加工结果：
```
{"field":"a,b,c","status":"500"}
```

