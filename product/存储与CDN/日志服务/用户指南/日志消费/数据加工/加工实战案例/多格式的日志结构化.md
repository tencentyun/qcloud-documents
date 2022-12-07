## 场景描述

小王把**用户操作和结果**的日志，以单行文本的格式采集到日志服务（Cloud Log Service，CLS），日志的格式和内容**不完全相同**。小王想编写一套语句，对不同格式的日志进行结构化。 
经过梳理查看，日志基本分为三种格式：第一种包含有 **uin、requestid、action、Reqbody** 四个字段、第二种包含 **uin、requestid、action** 三个字段、第三种包含 **requestid、action、TaskId** 三个字段。

## 场景分析

梳理一下小王的加工需求，加工思路如下：  
1. 由于三种格式的日志都包含 **requestid、action** 字段，因此使用正则提取 **requestid** 和 **action** 字段。  
2. 对 **uin、reqbody、TaskId** 字段进行特殊处理，先判断这个字段是否存在，如果存在，再进行提取。

## 原始日志

``` 
[
    {
        "__CONTENT__": "2021-11-29 15:51:33.201 INFO request 7143a51d-caa4-4a6d-bbf3-771b4ac9e135 action: Describe uin: 15432829 reqbody {\"Key\": \"config\",\"Values\": \"appisrunnning\",\"Action\": \"Describe\",\"RequestId\": \"7143a51d-caa4-4a6d-bbf3-771b4ac9e135\",\"AppId\": 1302953499,\"Uin\": \"100015432829\"}"
    },
    {
        "__CONTENT__": "2021-11-2915: 51: 33.272 ERROR request 2ade9fc4-2db2-49d8-b3e0-a6ea78ce8d96 has error action DataETL uin 15432829"
    },
    {
        "__CONTENT__": "2021-11-2915: 51: 33.200 INFO request 6059b946-25b3-4164-ae93-9178c9e73d75 action: UploadData hUWZSs69yGc5HxgQ TaskId 51d-caa-a6d-bf3-7ac9e"
    }
]
```

## DSL 加工函数

```
fields_set("requestid",regex_select(v("__CONTENT__"),regex="request [A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+",index=0,group=0))
fields_set("action",regex_select(v("__CONTENT__"),regex="action: \S+|action \S+",index=0,group=0))
t_if(regex_match(v("__CONTENT__"),regex="uin", full=False),fields_set("uin",regex_select(v("__CONTENT__"),regex="uin: \d+|uin \d+",index=0,group=0)))
t_if(regex_match(v("__CONTENT__"),regex="TaskId", full=False),fields_set("TaskId",regex_select(v("__CONTENT__"),regex="TaskId [A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+",index=0,group=0)))
t_if(regex_match(v("__CONTENT__"),regex="reqbody", full=False),fields_set("requestbody",regex_select(v("__CONTENT__"),regex="reqbody \{[^\}]+\}")))
t_if(has_field("requestbody"),fields_set("requestbody",str_replace(v("requestbody"),old="reqbody",new="")))
fields_drop("__CONTENT__")
fields_set("requestid",str_replace(v("requestid"),old="request",new=""))
t_if(has_field("action"),fields_set("action",str_replace(v("action"),old="action:|action",new="")))
t_if(has_field("uin"),fields_set("uin",str_replace(v("uin"),old="uin:|uin",new="")))
t_if(has_field("TaskId"),fields_set("TaskId",str_replace(v("TaskId"),old="TaskId",new="")))
```

## DSL 加工函数详解 

1. 新建一个字段 **requestid**，使用正则公式匹配 “**request 7143a51d-caa4-4a6d-bbf3-771b4ac9e135**”。
```
fields_set("requestid",regex_select(v("__CONTENT__"),regex="request [A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+",index=0,group=0))
```
2. 新建一个字段 **action**，使用正则公式匹配 “**action: UploadData**” 或者 “**action DataETL**”。因为原始日志中两种格式都有。
```
fields_set("action",regex_select(v("__CONTENT__"),regex="action: \S+|action \S+",index=0,group=0))
```
 - 如果 **\_\_CONTENT\_\_** 字段中有 **uin** 这个字符，新建 **uin** 字段，使用正则"**uin: \d+|uin \d+**"来匹配**uin: 15432829**或者**uin 15432829**。
```
t_if(regex_match(v("__CONTENT__"),regex="uin", full=False),fields_set("uin",regex_select(v("__CONTENT__"),regex="uin: \d+|uin \d+",index=0,group=0)))
```
 - 如果有 **TaskId** 这个字符，新建 **TaskId** 字段，使用正则来匹配 “**TaskId 51d-caa-a6d-bf3-7ac9e**”。
```
t_if(regex_match(v("__CONTENT__"),regex="TaskId", full=False),fields_set("TaskId",regex_select(v("__CONTENT__"),regex="TaskId [A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+",index=0,group=0)))
```
 - 如果有 **reqbody** 这个字符，新建 **requestbody** 字段，使用正则来匹配 **reqbody{...}**。
```
t_if(regex_match(v("__CONTENT__"),regex="reqbody", full=False),fields_set("requestbody",regex_select(v("__CONTENT__"),regex="reqbody \{[^\}]+\}")))
```
3. 丢弃**\_\_CONTENT\_\_**字段。
```
fields_drop("__CONTENT__")
```

以上我们已经提取出了我们需要的字段，但是由于在正则匹配过程中，产生了多余的字符 action、uin、requestbody、requestid、TaskId。所以需要使用 **str_replace()** 函数将多余的字符去掉，并且使用 **fields_set()** 函数对字段值进行重置。

1. 如果有 **requestbody** 字段，将字段值中多余的 **reqbody** 字符去掉。
```
t_if(has_field("requestbody"),fields_set("requestbody",str_replace(v("requestbody"),old="reqbody",new="")))
```
2. 将字段值v("**requestid**")中多余的 **requestid** 去掉。因为每条日志中都有 **requestid**，所以没有判断这个字段是否存在。
```
fields_set("requestid",str_replace(v("requestid"),old="request",new=""))
```
3. 如果有 **action** 字段，那么字段值中多余的 **action:** 或 **action** 字符去掉。
```
t_if(has_field("action"),fields_set("action",str_replace(v("action"),old="action:|action",new="")))
```
4. 如果有 **uin** 字段，那么字段值中多余的 **uin:** 或者 **uin** 去掉。
```
t_if(has_field("uin"),fields_set("uin",str_replace(v("uin"),old="uin:|uin",new="")))
```
5. 如果有 **TaskId** 字段，那么字段值中多余的 **TaskId** 字符去掉。
```
t_if(has_field("tTaskId"),fields_set("TaskId",str_replace(v("TaskId"),old="TaskId",new="")))
```

## 加工结果

```
[
{"action":" Describe","requestid":" 7143a51d-caa4-4a6d-bbf3-771b4ac9e135","requestbody":" {\"Key\": \"config\",\"Values\": \"appisrunnning\",\"Action\": \"Describe\",\"RequestId\": \"7143a51d-caa4-4a6d-bbf3-771b4ac9e135\",\"AppId\": 1302953499,\"Uin\": \"100015432829\"}","uin":" 15432829"},
{"action":" DataETL","requestid":" 2ade9fc4-2db2-49d8-b3e0-a6ea78ce8d96","uin":" 15432829"},
{"action":" UploadData","requestid":" 6059b946-25b3-4164-ae93-9178c9e73d75","TaskId":" 51d-caa-a6d-bf3-7ac9e"}
]
```
