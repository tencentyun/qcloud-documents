[负载均衡（Cloud Load Balancer，CLB）](https://console.cloud.tencent.com/clb/overview) 作为千亿 QPS 的网关产品，精细化运营十分重要，而日志服务（Cloud Log Service，CLS）访问日志则是其中的利器。通过 [CLB > 访问日志](https://console.cloud.tencent.com/clb/log)，我们可以挖掘海量的数据价值，不仅可以从访问日志中监控客户端请求、辅助排查问题、也可以分析梳理用户行为，为运营角色提供数据支持。本文主要介绍如何使用 CLS 分析 CLB 访问日志。

## 运维监控场景示例

小秦负责某互联网业务广告平台的运维，遇到广告合作方的反馈：用户在平台点击广告时，打开很慢。由于广告合作方对时效性和稳定性要求比较高，提出如果服务出现异常，需要1min内告警，5min内解决。此时，可利用 CLB 日志达到以下能力：
- 对客户端的访问时延，异常请求监控，高于一定阈值告警。
- 出现告警，有额外信息帮助判断故障原因。
  - 延时高于阈值的请求都是访问哪些网站，哪些 LB 实例和后端 RS 服务器。
  - LB 实例和后端 RS 服务器的延时情况统计。

## 运维监控解决方案

基于 CLS 的1min实时告警及多维分析能力，用户可以快速针对 CLB 访问日志进行运维监控，快速定位异常问题修复故障。

### 步骤1：开启 CLB 访问日志投递 CLS

1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/overview)。
2. 在左侧导航栏中，选择**实例管理**，进入实例管理页面。
3. 单击**负载均衡 ID/名称**，进入该负载均衡管理页面。
4. 找到并开启**日志服务CLS**。如下图所示：
详情请参考 [配置访问日志](https://cloud.tencent.com/document/product/214/41379) 文档。
![img](https://main.qcloudimg.com/raw/5c6ff27e1e5f4d839ea61def06457ae3.png)


### 步骤2：配置客户端访问时延及告警策略

- 客户端访问时延统计：
```
* | select time_series(__TIMESTAMP__, '1m', '%Y-%m-%d %H:%i:%s', '0')  as time, round(avg(request_time)*1000,2) as "平均访问延时" group by time order by time limit 1000
```
- 异常请求统计：
```
status:>200 | select time_series(__TIMESTAMP__, '1m', '%Y-%m-%d %H:%i:%s', '0')  as time, status, count(1) group by time,status order by time limit 1000
```

![](https://main.qcloudimg.com/raw/da511215e81a37a44f2eadb96eb2fcef.png)

- 配置告警策略，检测每分钟平均延时，高于阈值告警。
![](https://main.qcloudimg.com/raw/933580f29cb6b237fd1fa30b05746ba6.png)
- 告警策略中配置多维分析，出现告警时，附带额外信息。
  - LB 实例和后端 RS 服务器的延时情况统计。
  - 延时高于阈值的请求都是访问哪些网站，哪些 LB 实例和后端 RS 服务器。

![](https://main.qcloudimg.com/raw/264e5e77a1b838f785a79426da06ec2e.png)

- 配置通知渠道，可支持如下渠道：
 - 邮件
 - 短信
 - 微信
 - 企业微信
 - 电话
 - 自定义接口回调


### 步骤3：接收告警和快速定位

一旦触发告警，微信、企业微信、短信、电话等多端接收告警信息及详情内容：
![](https://main.qcloudimg.com/raw/81d6b2bc4508dcf1d5263eed7299f012.jpg)
告警详情中，可以看到受影响的 RS 实例，LB 实例等信息。
<img src="https://main.qcloudimg.com/raw/8c2fbdb17aa87c3269d416573e3537f2.jpg" style="zoom:33%;" />

由此可得知，LB 实例平均延时较高，受影响的 LB 实例主要是`9.*****.1`。小秦即可快速定位出异常 LB 实例并修复，整体耗时仅用1分钟。

## 运营统计场景示例

某科技内容 App 希望下个月策划一次线下沙龙会，一方面增加存量用户的粘性，另一方面借此机会宣传产品，拉动新用户。由于准备时间较短，经费有限，为了完成 KPI 目标，运营小婷列了如下需要获知的信息。
- 线下沙龙在哪里举办：需要了解访问客户地理来源，了解重点客户群体地理位置。
- 沙龙主题是什么：统计热点网站 TOP 排序，了解用户关注较多的内容版块是哪些。
- 当前用户主要用哪些客户端访问：针对当前客户端分布，重点设计落地页。
- 宣传落地页投放在哪些渠道：统计当前网站请求来源，寻找流量高的导流入口重点投放广告。

## 运营统计解决方案

使用 CLB 访问日志，用户可以轻松解决运营统计问题。

### 步骤1：了解访问客户地理来源

利用 CLS 提供 IP 函数，将客户端 IP 转换为对应的省份或国家。
- 中国分布：
```
* | select count(1) as c, ip_to_province(remote_addr) as address group by address limit 100
```
- 全球分布：
```
* | select count(1) as c, ip_to_country(remote_addr) as address group by address limit 100
```

![](https://main.qcloudimg.com/raw/7ce2b13d088fcf573d74ecbe1df19439.png)

### 步骤2：统计热点网站 TOP 排序

http_host 记录了访问的请求域名，通过统计请求域名的 pv，uv，可以统计 top host 排序。
```
* | select http_host, count(*) as pv, count(distinct(remote_addr)) as uv group by http_host order by pv desc limit 100
```
![image-20210827111351091](https://main.qcloudimg.com/raw/56a8a27c7b8c4c46c5cd6418f8b13bb5.png)

### 步骤3：统计客户端分布情况

```
* | select http_user_agent, count(*) group by http_user_agent
```
![](https://main.qcloudimg.com/raw/d26d73fab5391de78b1db5b8fae5e6da.png)

### 步骤4：统计当前网站请求来源

http_referer 字段记录了网站的请求来源。
```
* | select http_referer, count(*) as count group by http_referer order by count desc limit 100
```
![](https://main.qcloudimg.com/raw/54eba44020f70c3df070ec8159ef2290.png)


## 总结

CLB 的访问日志挖掘出很多价值，例如 pv、uv 趋势统计，客户端报文流量统计，状态码分布，P99，P95 访问延时等。为了帮助用户快速分析 CLB 访问日志，CLS 和 CLB 联合打造了开箱即用的可视化分析方案，用户只需开启 CLB 访问日志投递 CLS，即可马上享用。









