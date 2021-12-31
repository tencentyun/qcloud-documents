## 概述

Nginx 是一个高性能的 HTTP 和反向代理 Web 服务器，透过 Nginx 日志可以挖掘非常大的价值，例如诊断调优网站，监控网站稳定性，运营数据统计等。本文介绍如何通过日志服务（Cloud Log Service，CLS）对 Nginx 进行全方位日志数据挖掘。


## 前提条件

- 已将 Nginx 日志采集至 CLS，详见 [操作指南](https://cloud.tencent.com/document/product/614/37735)。
- 本文采取标准 Nginx 日志配置：
```
log_format  main  '$server_name $remote_addr - $remote_user [$time_local] "$request" '
                        '$status $uptream_status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for" ';
```

## 场景示例

### 诊断调优

#### 需求场景

针对访问延时大的页面进行调优，优化用户体验。

#### 解决方案

- 计算每5分钟请求的平均延时和最大延时，从整体了解延时情况。
```
* | select time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0')  as time, avg(request_time) as avg_latency ,max(request_time) as max_latency group by time order by time limit 1000
```
![image-20210823201855487](https://main.qcloudimg.com/raw/2421a0fb81c5e58d1a073fad3ddfa1ff.png)
- 统计最大延时对应的请求页面，进一步优化页面响应。
```
* | select time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0')  as time, max_by(request_uri,request_time) group by time order by time limit 1000
```
![image-20210823202154190](https://main.qcloudimg.com/raw/854d6dc6900d8f4a2c35146303178987.png)
- 对延时最大的页面进行调优。
例如**/4nm8c.html**页面的访问延时最大，需要对**\/4nm8c.html**页面进行调优，则需计算**\/4nm8c.html**页面的访问 PV、UV、各种请求方法次数、各种请求状态次数、各种浏览器次数、平均延时和最大延时。
```
request_uri:"/4nm8c.html*" | select count(1) as pv,
        approx_distinct(remote_addr) as uv,
        histogram(method) as method_pv,
        histogram(status) as status_pv,
        histogram(user_agent) as user_agent_pv,
        avg(request_time) as avg_latency,
        max(request_time) as max_latency
```
![image-20210823203326333](https://main.qcloudimg.com/raw/d3a9a203135975252e917d922cd5c6d0.png)

### 监控网站稳定性问题

#### 需求场景

针对性能问题、网站错误、流量急跌或暴涨等情况，根据日志监控阈值，一旦触发阈值告警，先于用户发现问题。

#### 解决方案

使用数学统计中的百分数（例如99%最大延时）来作为告警触发条件较为准确，使用平均值，个体值触发告警会造成一些个体请求延时被平均，无法反映真实情况。例如使用如下查询分析语句计算一天窗口（1440分钟）内各分钟的平均延时大小、50%分位的延时大小和90%分位的延时大小。
```
* | select avg(request_time) as l, approx_percentile(request_time, 0.5) as p50, approx_percentile(request_time, 0.99) as p99, time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0') as time group by time order by time desc limit 1440
```
![image-20210823204601224](https://main.qcloudimg.com/raw/473a592c93fb7994623d6c265dd9e50a.png)
针对99%分位的延时大于100ms告警，并且在告警信息中直接展示受影响的 url，用户，快速判断出错情况。
```
* | select approx_percentile(request_time, 0.99) as p99
```
![image-20210823205326591](https://main.qcloudimg.com/raw/afa64d65eac65dc399d84d0a1d61dda4.png)
接收告警信息，根据受影响的 top url 及用户信息，进行针对性的告警恢复决策。
![](https://main.qcloudimg.com/raw/82e80b787485880d124f28d940e06182.jpg)

### 分析网站访问情况

利用 CLS，用户可以搭建运营数据大盘，全方位展示网站访问情况。访问 PV/UV 统计、访问地理信息统计，前十访问来源、访问前十地址和等信息均可快速分析。

- 统计最近一天访问 IP 地址的来源情况。
```
* | select count(1) as c, ip_to_province(remote_addr) as address group by address limit 100
```
![image-20210823212009497](https://main.qcloudimg.com/raw/d87f3fd58339856867afc7766c5a3236.png)
- 展示最近一天 PV 数最多的前十个访问来源页面，获取热门页面。
```
* | select count(1) as pv , http_referer  group by http_referer order by pv desc limit 10
```
![image-20210823212306355](https://main.qcloudimg.com/raw/4a73e9cda0bedfa8c8454f10827326b3.png)
- 展示最近一天内的 PV 数和 UV 数。
```
*| select approx_distinct(remote_addr) as uv ,count(1) as pv , time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0')  as time group by time order by time limit 1000
```
![image-20210823212539291](https://main.qcloudimg.com/raw/01bd568b51de6b6c3351284666647113.png)



