
## 场景描述

小王将日志采集到日志服务（Cloud Log Service，CLS），但是没有固定的分割符号，是单行文本格式。现在小王想将日志结构化，从文本中**提取日志时间、日志级别、操作、URL 信息**，便于后续的检索分析。   

## 场景分析

梳理一下小王的加工需求，加工思路如下：  
1. {...}中的内容是**操作**的详情，可以通过正则提取。  
2. 使用正则提取**日志时间、日志级别、URL**。  

## 原始日志

``` 
{
    "content": "[2021-11-24 11:11:08,232][328495eb-b562-478f-9d5d-3bf7e][INFO] curl -H 'Host: ' http://abc.com:8080/pc/api -d {\"version\": \"1.0\",\"user\": \"CGW\",\"password\": \"123\",\"interface\": {\"Name\": \"ListDetail\",\"para\": {\"owner\": \"1253\",\"orderField\": \"createTime\"}}}"
}
```

## DSL 加工函数

```
fields_set("Action",regex_select(v("content"),regex="\{[^\}]+\}",index=0,group=0)) 
fields_set("loglevel",regex_select(v("content"),regex="\[[A-Z]{4}\]",index=0,group=0))。 
fields_set("logtime",regex_select(v("content"),regex="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}",index=0,group=0))
fields_set("Url",regex_select(v("content"),regex="([a-z]{3}).([a-z]{3}):([0-9]{4})",index=0,group=0))
fields_drop("content")
```

## DSL 加工函数详解 

1. 新建一个字段 **Action**，使用正则\{[^\}]+\}，匹配**{...}**。  
```
fields_set("Action",regex_select(v("content"),regex="\{[^\}]+\}",index=0,group=0)) 
``` 
2. 新建一个字段 **loglevel**，使用正则[A-Z]{4}可以匹配 **INFO**。
```
fields_set("loglevel",regex_select(v("content"),regex="\[[A-Z]{4}\]",index=0,group=0))。
```
3. 新建一个字段 **logtime**，使用正则d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}匹配**2021-11-24 11:11:08**。
```  
fields_set("logtime",regex_select(v("content"),regex="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}",index=0,group=0))
```
4. 新建一个字段 **Url**，使用正则[a-z]{3}.[a-z]{3}匹配 **abc.com**，[0-9]{4}匹配**8080**。  
```
fields_set("Url",regex_select(v("content"),regex="([a-z]{3}).([a-z]{3}):([0-9]{4})",index=0,group=0))
```
5. 丢弃 **content** 字段。 
```
fields_drop("content")
```

## 加工结果

```
{"Action":"{\"version\": \"1.0\",\"user\": \"CGW\",\"password\": \"123\",\"interface\": {\"Name\": \"ListDetail\",\"para\": {\"owner\": \"1253\",\"orderField\": \"createTime\"}","Url":"abc.com:8080","loglevel":"[INFO]","logtime":"2021-11-24 11:11:08,232"}
 
```

