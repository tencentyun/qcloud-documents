## 场景描述

小王将日志采集到了日志服务（Cloud Log Service，CLS），日志通过双竖线`||`分割，有日志的时间、日志级别、日志内容、任务 ID、进程名称、主机 IP 等。现在小王想将日志结构化，便于后续索引、仪表盘展示。并按照 **ERROR、WARNING、INFO** 三个级别，把日志**分发**到三个不同的目标日志主题中，便于后续的分析。最后，当日志内容中有 “**team B is working**” 字样时，将该条**日志过滤（丢弃）**。

## 场景分析

梳理一下小王的加工需求，加工思路如下：  
1. 日志中如有 **team B is working** 字符，将该条日志过滤（丢弃）；并把丢弃日志放在前面，可以减少后续的运算量。  
2. 日志结构化：按照**双竖线**`||`分割符，对日志进行结构化。  
3. 日志分发：按照按照 **ERROR、WARNING、INFO** 三个级别，把日志分发到三个不同的目标日志主题。  

>! 分发到多个目标日志主题，需要在新建数据加工任务时，定义好日志主题的目标名称。该名称将用在 **log_output("目标名称")** 函数中。
>

![](https://qcloudimg.tencent-cloud.cn/raw/61bd11b23c04cff091d326cd6ad3d5ec.png)

## 原始日志

``` 
[
    {
        "message": "2021-12-09 11:34:28.279||team A is working||INFO||605c643e29e4||BIN--COMPILE||192.168.1.1"
    },
    {
        "message": "2021-12-09 11:35:28.279||team A is working ||WARNING||615c643e22e4||BIN--Java||192.168.1.1"
    },
    {
        "message": "2021-12-09 11:36:28.279||team A is working ||ERROR||635c643e22e4||BIN--Go||192.168.1.1"
    },
    {
        "message": "2021-12-09 11:37:28.279||team B is working||WARNING||665c643e22e4||BIN--Python||192.168.1.1"
    }
]
``` 

## DSL 加工函数

``` 
log_drop(regex_match(v("message"),regex="team B is working",full=False))
ext_sepstr("message","time,log,loglevel,taskId,ProcessName,ip",sep="\|\|")
fields_drop("message")
t_switch(regex_match(v("loglevel"),regex="INFO",full=True),log_output("info_log"),regex_match(v("loglevel"),regex="WARNING",full=True),log_output("warning_log"),regex_match(v("loglevel"),regex="ERROR",full=True),log_output("error_log"))
``` 

## DSL 加工函数详解 

1. 当日志中含有 **team B is working** 关键字时，丢弃该条日志。因为第四条日志中包含有 **team B is working**，所以第四条日志会被丢弃。
``` 
log_drop(regex_match(v("message"),regex="team B is working",full=False))
``` 
2. 根据**双竖线**||分隔符来提取结构化数据。
``` 
ext_sepstr("message","time,log,loglevel,taskId,ProcessName,ip",sep="\|\|")
``` 
3. 丢弃 **message** 字段。
``` 
fields_drop("message")
``` 
4. 按照 **loglevel** 的字段值，**INFO/WARNING/ERROR**，将日志分发到不同的目标日志主题。
``` 
t_switch(regex_match(v("loglevel"),regex="INFO",full=True),log_output("info_log"),regex_match(v("loglevel"),regex="WARNING",full=True),log_output("warning_log"),regex_match(v("loglevel"),regex="ERROR",full=True),log_output("error_log"))
``` 

## 加工结果

>! 必须要提前配置好目标日志主题和目标名称。
>

该日志分发到 **info_log**，即数据加工-目标3，可参看上图中的目标名称和日志主题的对应关系。
``` 
{"ProcessName":"BIN--COMPILE","ip":"192.168.1.1","log":"team A is working","loglevel":"INFO","taskId":"605c643e29e4","time":"2021-12-09 11:34:28.279"}
``` 
该日志分发到 **warning_log**，即数据加工-目标2。
``` 
{"ProcessName":"BIN--COMPILE","ip":"192.168.1.1","log":"team A is working","loglevel":"INFO","taskId":"605c643e29e4","time":"2021-12-09 11:34:28.279"}
``` 
该日志分发到 **error_log**，即数据加工-目标1。
``` 
{"ProcessName":"BIN--Go","ip":"192.168.1.1","log":"team A is working ","loglevel":"ERROR","taskId":"635c643e22e4","time":"2021-12-09 11:36:28.279"}
``` 
