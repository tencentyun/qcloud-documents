在简单的运维场景下，日志通常先直接输出到服务器本地文件中，再使用 Linux 系统下常用的 grep 命令查找符合要求的日志。此方式在业务系统较为复杂时，会由于日志分散在不同的服务器、命令行操作不直观、服务器权限管理限制等原因导致日志查找困难，严重影响运维效率。或者当用户需要基于日志做一些统计分析或监控告警，更是难上加难。

本文将介绍如何快速将通过 grep 命令查找的本地日志迁移至日志服务（Cloud Log Service，CLS），以获取如下优势：

- 数据集中存储及检索，无需登录多台服务器分别进行查询，在负载均衡、微服务等架构下尤为关键。
- 简单单击即可快速检索日志，告别命令行及繁琐的服务器权限管理。
- 基于日志进行统计分析，获取关键业务指标，例如 PV、接口响应时间、接口错误率等。
- 实时检测异常日志，通过短信、邮件和微信等多种方式获取通知。

>? 如果您的日志已经采集到了 CLS，可跳过日志采集和配置索引步骤，直接执行 [步骤3：检索日志](#RetrievalLog)。
>

## 步骤1：日志采集

针对服务器本地日志，可使用 LogListener 将原始日志采集至 CLS，LogListener 安装详情请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。
如果您的服务器为腾讯云云服务器（Cloud Virtual Machine，CVM），还可以通过控制台自动安装 LogListener，详情请参见 [CVM 批量部署 LogListener](https://cloud.tencent.com/document/product/614/60593)。

与服务器本地日志不同，为了后续对日志进行更方便的检索和统计分析，在采集时可将非格式化的原始日志转换为格式化的数据。例如原始日志为：
```
10.20.20.10 ::: [Tue Jan 22 14:49:45 CST 2019 +0800] ::: GET /online/sample HTTP/1.1 ::: 127.0.0.1 ::: 200 ::: 647 ::: 35 ::: http://127.0.0.1/
```
可使用分割符`:::`切分为八个字段，并为每个字段定义名称：
```
IP: 10.20.20.10
bytes: 35
host: 127.0.0.1
length: 647
referer: http://127.0.0.1/
request: GET /online/sample HTTP/1.1
status: 200
time: [Tue Jan 22 14:49:45 CST 2019 +0800]
```
具体操作请参见 [分隔符格式](https://cloud.tencent.com/document/product/614/17420)。除了使用分隔符切分日志，CLS 还支持正则、JSON、全文等多种日志切分方式，详情请参见 [采集文本日志](https://cloud.tencent.com/document/product/614/17418)。

## 步骤2：配置索引

配置索引的目的在于定义哪些字段需要检索，字段的类型是什么，以便于后续检索日志。对于大多数使用场景，可使用自动配置索引功能，一键完成配置，详情请参见 [配置索引](https://cloud.tencent.com/document/product/614/50922#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)。


<span id="RetrievalLog"></span>
## 步骤3：检索日志

本文以常用的 grep 命令为例，介绍如何通过 CLS 实现类似的日志检索效果。

示例原始日志为：
```
10.20.20.10 ::: [Tue Jan 22 14:49:45 CST 2019 +0800] ::: GET /online/sample HTTP/1.1 ::: 127.0.0.1 ::: 200 ::: 647 ::: 35 ::: http://127.0.0.1/
```

在 CLS 对应的格式化后日志为：
```
IP: 10.20.20.10
bytes: 35
host: 127.0.0.1
length: 647
referer: http://127.0.0.1/
request: GET /online/sample HTTP/1.1
status: 200
time: [Tue Jan 22 14:49:45 CST 2019 +0800]
```

#### 案例1

检索 request为/online/sample 的日志。
- 使用 grep 命令：
```
# grep "/online/sample" test.log
```
- 使用 CLS 检索方式：
```
request:"/online/sample"
```


#### 案例2

检索状态码 status 不为200的日志。
- 使用 grep 命令：
```
# grep -v "200" test.log
```
实际上，此方式可能会把一些日志也排除掉（出现了200，但 status 不是200的字段）。如需准确检索，则需要编写正则表达式。
- 使用 CLS 检索方式：
```
NOT status:200
```
CLS 还支持更加灵活的检索方式，例如检索状态码 status 大于等于500的日志。
```
status:>=500
```


#### 案例3

统计 status 不为200的日志条数。
- 使用 grep 命令：
```
# grep -c -v "200" test.log
```
- 使用 CLS 检索方式：
```
NOT status:200 | select count(*) as errorLogCounts
```


#### 案例4

检索状态码 status 为200，且 request 为 /online/sample 的日志。
- 使用 grep 命令：
```
# grep "200" test.log | grep "/online/sample"
```
- 使用 CLS 检索方式：
```
status:200 AND request:"/online/sample"
```

#### 案例5

检索 request 为 /online/sample 或 /offline/sample 的日志。
- 使用 grep 命令：
```
# grep -E "/online/sample|/offline/sample" test.log
```
- 使用 CLS 检索方式：
```
request:"/online/sample" OR request:"/offline/sample"
```

#### 案例6

检索 request 为 /online/sample，但日志文件不是 test.log 的日志。
- 使用 grep 命令：
```
# grep -rn "/online/sample" --exclude=test.log
```
- 使用 CLS 检索方式：
```
request:"/online/sample" AND NOT __FILENAME__:"test.log"
```

#### 案例7

检索 time 为 [Tue Jan 22 14:49:45 CST 2019 +0800] 的日志的前10行日志。
- 使用 grep 命令：
```
# grep "[Tue Jan 22 14:49:45 CST 2019 +0800]" -B 10 test.log
```
- 使用 CLS 检索方式：
```
time:"[Tue Jan 22 14:49:45 CST 2019 +0800]"
```
检索到匹配的日志后，在控制台单击**上下文检索**，即可查看该条日志附近的日志。



