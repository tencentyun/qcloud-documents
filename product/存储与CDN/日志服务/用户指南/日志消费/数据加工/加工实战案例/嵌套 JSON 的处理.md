## 场景描述

小王将日志以 JSON 格式采集到日志服务（Cloud Log Service，CLS）。JSON 是多层嵌套，小王想提取 **user** 和 **App** 字段。其中 **user** 是二级嵌套字段。

## 原始日志

``` 
[
    {
        "content": {
            "App": "App-1",
            "start_time": "2021-10-14T02:15:08.221",
            "resonsebody": {
                "method": "GET",
                "user": "Tom"
            },
            "response_code_details": "3000",
            "bytes_sent": 69
        }
    },
    {
        "content": {
            "App": "App-2",
            "start_time": "2222-10-14T02:15:08.221",
            "resonsebody": {
                "method": "POST",
                "user": "Jerry"
            },
            "response_code_details": "2222",
            "bytes_sent": 1
        }
    }
]
```

## DSL 加工函数

- 方法一：不展开所有的 KV，使用 **jmes** 公式直接提取字段。
```
ext_json_jmes("content", jmes="resonsebody.user", output="user")
ext_json_jmes("content", jmes="App", output="App")
```
- 方法二：平铺所有的 KV，丢弃不需要的字段。
```
ext_json("content")
fields_drop("content")
fields_drop("bytes_sent","method","response_code_details","start_time")
```

## DSL 加工函数详解 

- 方法一： 
 1. 使用 jmes 公式 **resonsebody.user**，直接指定二级嵌套的 **user** 字段。
```
ext_json_jmes("content", jmes="resonsebody.user", output="user")
```
 2. 使用 jmes 公式 **App**，直接指定 **App** 字段。
```
ext_json_jmes("content", jmes="App", output="App")
```
- 方法二：  
 1. 使用 **ext_json** 函数从 JSON 数据中提取结构化数据，默认会平铺所有的字段。
```
ext_json("content")
```
 2. 丢弃 **content** 字段。
```
fields_drop("content")
```
 3. 丢弃不需要的字段 **bytes_sent,method,response_code_details,start_time**
```
fields_drop("bytes_sent","method","response_code_details","start_time")
```

## 加工结果

```
[{"App":"App-1","user":"Tom"},
{"App":"App-2","user":"Jerry"}]
```
