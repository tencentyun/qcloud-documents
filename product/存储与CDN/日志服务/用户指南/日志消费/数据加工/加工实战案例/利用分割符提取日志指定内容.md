## 场景描述

小王将 **Flink 任务运行的日志**，以单行文本采集到日志服务（Cloud Log Service，CLS）。日志内容里面包含了**逗号","** ,**冒号"："**，这些分割符将日志分割成了几小段。其中有一段是转义 JSON，它里面是 Flink 任务执行的详情，小王想将任务详情提取出来，然后对其进行结构化。  

## 场景分析

梳理一下小王的加工需求，加工思路如下：  
1. 将转义 JSON 提取出来。  
2. 从 JSON 中提取结构化数据。


## 原始日志

``` 
{
    "regex": "2021-12-02 14:33:35.022 [1] INFO  org.apache.Load - Response:status: 200, resp msg: OK, resp content: {    \"TxnId\": 58322,    \"Label\": \"flink_connector_20211202_1de749d8c80015a8\",    \"Status\": \"Success\",    \"Message\": \"OK\",    \"TotalRows\": 1,    \"LoadedRows\": 1,    \"FilteredRows\": 0,  \"CommitAndPublishTimeMs\": 16}"
}
```

## DSL 加工函数

```
ext_sepstr("regex", "f1, f2, f3", sep=",")
fields_drop("regex")
fields_drop("f1")
fields_drop("f2")
ext_sepstr("f3", "f1,resp_content", sep=":")
fields_drop("f1")
fields_drop("f3")
ext_json("resp_content", prefix="")
fields_drop("resp_content")
```

## DSL 加工函数详解 

1. 使用逗号将该条日志截成3段，第三段**f3**是 **resp content:{JSON}**。
```
ext_sepstr("regex", "f1, f2, f3", sep=",")
```
2. 将不需要的字段丢弃。
```
fields_drop("regex")
fields_drop("f1")
fields_drop("f2")
```
3. 使用冒号将**f3**字段截成两段。
```
ext_sepstr("f3", "f1,resp_content", sep=":")
```
4. 丢弃无用的字段。
```
fields_drop("f1")
fields_drop("f3")
```
5. 使用 **ext_json** 函数，从 **resp_content** 字段中，提取结构化数据。
```
ext_json("resp_content", prefix="")
```
6. 丢弃 **resp_content** 字段。
```
fields_drop("resp_content")
```

## 加工结果

```
{"CommitAndPublishTimeMs":"16","FilteredRows":"0","Label":"flink_connector_20211202_1de749d8c80015a8","LoadedRows":"1","Message":"OK","Status":"Success","TotalRows":"1","TxnId":"58322"}
```

