## 概述

[内容分发网络（Content Delivery Network，CDN）](https://console.cloud.tencent.com/cdn) 是非常重要的互联网基础设施，用户可以通过 CDN，快速的访问网络中各种图片，视频等资源。在访问过程中，CDN 会产生大量的日志数据，通过对 CDN 访问日志的分析，用户可以挖掘出大量有用的信息用于 CDN 质量和性能的分析，错误诊断，客户端分布， 以及用户行为分析。

## 前提条件

已将 CDN 日志采集至日志服务（Cloud Log Service，CLS），详见 [操作详情](https://cloud.tencent.com/document/product/228/42137)。


## 场景示例

### 传统 CDN 日志分析

当前， 各 CDN 服务提供厂商， 通常会实时提供基础的监控指标，例如请求次数，宽带等信息。 但是，在许多特定的分析场景下， 这些默认的实时指标可能并不能满足用户定制化的分析需求。 因此，通常用户会进一步将 CDN 的原始日志下载下来， 进行离线的深入分析与挖掘。

这种情况用户自行搭建离线分析集群，不仅需要大量的运维开发成本和人力成本；同时在一些基于 CDN 日志的告警，排障等分析场景下，离线日志的实时性难以保证。

### CDN to CLS 方案

腾讯云 CDN 与 CLS 实现打通， 用户可以将 CDN 的数据实时投递至 CLS， 并进一步使用 CLS 的检索和 SQL 分析能力， 来满足不同场景下用户个性化的实时日志分析需求：
- 日志一键投递
- 百亿级日志， 秒级分析
- Dashboard 仪表盘实时日志可视化
- 一分钟实时告警

#### CDN 日志介绍

CDN 日志字段说明：

| 字段名        | 原始日志类型 | 日志服务类型 | 说明                                                         |
| ------------- | ------------ | ------------ | ------------------------------------------------------------ |
| app_id        | Integer      | long         | 腾讯云账号 APPID                                             |
| client_ip     | String       | text         | 客户端 IP                                                    |
| file_size     | Integer      | long         | 文件大小                                                     |
| hit           | String       | text         | 缓存 HIT / MISS，在 CDN 边缘节点命中、父节点命中均标记为 HIT |
| host          | String       | text         | 域名                                                         |
| http_code     | Integer      | long         | HTTP 状态码                                                  |
| isp           | String       | text         | 运营商                                                       |
| method        | String       | text         | HTTP Method                                                  |
| param         | String       | text         | URL 携带的参数                                               |
| proto         | String       | text         | HTTP 协议标识                                                |
| prov          | String       | text         | 运营商省份                                                   |
| referer       | String       | text         | Referer 信息，HTTP 来源地址                                  |
| request_range | String       | text         | Range 参数，请求范围                                         |
| request_time  | Integer      | long         | 响应时间（毫秒），指节点从收到请求后响应所有回包再到客户端所花费的时间 |
| request_port  | String       | long         | 客户端与 CDN 节点建立连接的端口。若无，则为 -                  |
| rsp_size      | Integer      | long         | 返回字节数                                                   |
| time          | Integer      | long         | 请求时间，UNIX 时间戳，单位为：秒                          |
| ua            | String       | text         | User-Agent 信息                                              |
| url           | String       | text         | 请求路径                                                     |
| uuid          | String       | text         | 请求的唯一标识                                               |
| version       | Integer      | long         | CDN 实时日志版本                                             |

#### CDN 质量监控

##### 场景1：监控 CDN 访问延时高于一定阈值告警

使用数学统计中的百分数（例如99%最大延迟）来作为告警触发条件较为准确， 使用平均值， 个体值触发告警会造成一些个体请求延时被平均， 无法反映真实情况。 例如使用如下查询分析语句计算一天窗口（1440分钟）内各分钟的平均延时大小，50%分位的延时大小，和90%分位的延时大小。
```sql
* | select avg(request_time) as l, approx_percentile(request_time, 0.5) as p50, approx_percentile(request_time, 0.99) as p99, time_series(__TIMESTAMP__, '5m', '%Y-%m-%d %H:%i:%s', '0') as time group by time order by time desc limit 1440
```
![](https://main.qcloudimg.com/raw/b0e6442999c2ea4a95501a6986c026d6/15.png)
针对99%的延时大于100ms进行告警，并且在告警信息中之间展示受影响域名、url、client_ip，以便快速判断错误情况。告警设置如下语句。
```sql
* | select approx_percentile(request_time, 0.99) as p99
```
![](https://main.qcloudimg.com/raw/ba7282a1854fc485715eb544b597c69b/16.png)
通过配置多维度分析，在告警信息中展示受影响的域名，客户端 IP，url，帮助开发人员快速定位问题。
![](https://main.qcloudimg.com/raw/d82d1a9aedf74a97567a371a30b66d05/17.png)
一旦告警触发后，通过微信，企业微信，短信第一时间获取关键信息。

<img src="https://main.qcloudimg.com/raw/bf0cd29a79e8a41894a7a8c12cd5b08f.png" style="zoom:50%;" />

##### 场景2: 资源访问错误激增告警，当同比增数超过一定阈值时， 告警通知用户

当页面访问错误的数量出现激增时，可能说明 CDN 后端服务器出现故障，或者请求过载。 我们可以通过设置告警来对一定时间范围内（eg.一分钟）请求错误数量的同比增数进行监控， 当同比增数超过一定阈值时， 告警通知用户。

**最近一分钟内的错误数量**
```sql
* | select * from (select * from (select * from (select date_trunc('minute', __TIMESTAMP__) as time,count(*) as errct where http_code>=400 group by time order by time desc limit 2)) order by time desc limit 1)
```

**上一分钟内的错误数量**
```sql
* | select *  from (select * from (select * from (select date_trunc('minute', __TIMESTAMP__) as time,count(*) as errct where http_code>=400 group by time order by time desc limit 2)) order by time asc limit 1)
```

告警策略配置触发条件为【最近一分钟内的错误数量】-【上一分钟内的错误数量】 > 指定阈值
```
$2.errct-$1.errct >100
```

![](https://main.qcloudimg.com/raw/9171b4610883c7a5a1396926e90cf6b5/18.png)


#### CDN 质量和性能分析

CDN 提供日志中，包含了丰富的内容，我们可以从多个维度对 CDN 的整体质量和性能进行全方位的统计和分析。
- 健康度
- 缓存命中率
- 平均下载速度
- 运营商的下载次数、下载流量、速度
- 请求延时响应

##### 健康度

统计 http_code 小于500的请求占所有请求的百分比。
```sql
* | select round(sum(case when http_code<500 then 1.00 else 0.00 end) / cast(count(*) as double) * 100,1) as "健康度"
```
![](https://main.qcloudimg.com/raw/26a77c33b0d8ac5abe518152ab974309/1.png)

##### 缓存命中率

统计 return_code 小于400的请求中， hit 为 “hit” 的请求百分比。
```sql
http_code<400 | select round(sum(case when hit='hit' then 1.00 else 0.00 end) / cast(count(*) as double) * 100,1) as "缓存命中率"
```
![](https://main.qcloudimg.com/raw/d9cd86776fdc4abea0c9dd55335e523a/2.png)

##### 平均下载速度

统计一段时间内，总体下载量除以整体耗时获得平均下载速度。
```sql
* | select sum(rsp_size/1024.0) / sum(request_time/1000.0) as "平均下载速度(kb/s)"
```

![](https://main.qcloudimg.com/raw/675c5270e2ee511bdd691cf637eb40bb/3.png)

##### 运营商的下载次数、下载流量、速度

原理同上，使用 ip_to_provider 函数，将 client_ip 转化成对应的运营商。
```sql
* | select ip_to_provider(client_ip) as isp , sum(rsp_size)* 1.0 /(sum(request_time)+1) as "下载速度(KB/s)" , sum(rsp_size/1024.0/1024.0) as  "下载总量(MB)",  count(*) as c   group by  isp  order by c desc  limit 10
```
![](https://main.qcloudimg.com/raw/c4e2f9c4ca11c2ae4e23933825cf473f/7.png)

##### 请求延时响应

将访问延时按照各窗口进行统计，可根据应用实际的情况来划分合适的延时时间窗口。
```sql
* | select case when request_time < 5000 then  '~5s'  when request_time < 6000 then '5s~6s'  when request_time < 7000 then '6s~7s' when request_time < 8000 then '7~8s' when request_time < 10000 then '8~10s' when request_time < 15000 then '10~15s' else '15s~' end as  latency , count(*) as count group by latency
```
![](https://main.qcloudimg.com/raw/5d30ded533d76852dd0d0f6182ded224/8.png)

#### CDN 质量和性能分析

访问错误一直是影响服务体验的重要一环，当出现错误的时候，需要快速定位当前错误 QPS 和比例是多少，哪些域名和 URI 影响最大，是否和地域、运营商有关，是不是发布的新版本导致。

**解决方案**

查看4xx，5xx错误码分布。
```
* |  select  http_code , count(*) as c where http_code >= 400 group by http_code order by c  desc 
```

从下面的错误分布图来看，主要的错误都是发生了404错误，说明被被访问文件或内容不存在，这个时候就需要检查是不是资源已经被删除或者销毁
![](https://main.qcloudimg.com/raw/8900ee8826c76d742985a64d2f3be2b2/10.png)

对于 http_code > 400的请求，我们对其进行多维度分析，如按照域名和 uri 的维度进行 top 排序；省份，运营商角度查看错误次数；查看客户端分布。
**域名**
```sql
* |  select  host , count(*) as count where http_code > 400   group by host  order by count desc limit 10 
```

**url**
```sql
* |  select  url , count(*) as count where http_code > 400   group by url  order by count desc limit 10 
```

**省份，运营商分析**
```sql
* | select client_ip, ip_to_province(client_ip) as "province", ip_to_provider(client_ip) as  "运营商" , count(*) as "错误次数"  where http_code >= 400 group by client_ip   order by "错误次数" DESC limit 100
```

**客户端分布**
```sql
鹅湖单xxxxxxxxxx *  | select ua as "客户端版本", count(*) as "错误次数"  where http_code > 400 group by ua order by "错误次数" desc limit 10sql
```

![](https://main.qcloudimg.com/raw/06582e8e14a4f5d44537e3317240312c.png)

由图可看出，错误集中 Safari 客户端，定位问题后发现，是新版本 bug 导致在 Safari 浏览器窗口下，访问资源频繁失败。


#### 用户行为分析

**需求**
- 大部分用户是从哪里过来，是内部还是外部
- 哪些资源用户是热门资源
- 是否有用户在疯狂下载资源，行为是否符合预期

**解决方案**
- 访问来源分析
```sql
* | select ip_to_province(client_ip) as province ,  count(*) as c group by province order by c desc limit 50
```
![](https://main.qcloudimg.com/raw/84564c14877fbfff31624286c9b76a5f.png)
- 访问 TopUrl
```sql
http_code < 400 | select url ,count(*) as  "访问次数", round(sum(rsp_size)/1024.0/1024.0/1024.0, 2) as "下载总量(GB)" group by url order by "访问次数" desc limit 100
```
![](https://main.qcloudimg.com/raw/10b6050874e2eefe069ecdbe5a17de19/12.png)
- 下载流量 Top 域名，按照各个域名下载数据量大小进行 Top 排序
```sql
* | select host, sum(rsp_size/1024) as  "下载总量" group by host order by  "下载总量"  desc  limit 100
```
![](https://main.qcloudimg.com/raw/a18004b86c9b2c6e889e5c6fbbe3fc1e/5.png)
- 下载量 Top 用户统计
```sql
* | SELECT CASE WHEN ip_to_country(client_ip)='香港' THEN concat(client_ip, ' ( Hong Kong )') WHEN ip_to_province(client_ip)='' THEN concat(client_ip, ' ( Unknown IP )') WHEN ip_to_provider(client_ip)='内网IP' THEN concat(client_ip, ' (Private IP )') ELSE concat(client_ip, ' ( ', ip_to_country(client_ip), '/', ip_to_province(client_ip), '/', if(ip_to_city(client_ip)='-1', 'Unknown city', ip_to_city(client_ip)), ' ',ip_to_provider(client_ip), ' )') END AS client, pv as "总访问数", error_count as "错误访问数" , throughput as "下载总量(GB)"  from  (select  client_ip , count(*) as pv, round(sum(rsp_size)/1024.0/1024/1024.0, 1) AS throughput , sum(if(http_code  > 400, 1, 0)) AS error_count from log   group by client_ip order by throughput desc limit 100)
```
![](https://main.qcloudimg.com/raw/48c4585418033757809449ed53c61bb8/13.png)
- 有效访问 Top 用户统计
```sql
* | SELECT CASE WHEN ip_to_country(client_ip)='香港' THEN concat(client_ip, ' ( Hong Kong )') WHEN ip_to_province(client_ip)='' THEN concat(client_ip, ' ( Unknown IP )') WHEN ip_to_provider(client_ip)='内网IP' THEN concat(client_ip, ' (Private IP )') ELSE concat(client_ip, ' ( ', ip_to_country(client_ip), '/', ip_to_province(client_ip), '/', if(ip_to_city(client_ip)='-1', 'Unknown city', ip_to_city(client_ip)), ' ',ip_to_provider(client_ip), ' )') END AS client, pv as  "总访问数", (pv - success_count)  as "错误访问数" , throughput as "下载总量(GB)"  from  (select  client_ip , count(*) as pv, round(sum(rsp_size)/1024.0/1024/1024.0, 1) AS throughput , sum(if(http_code  < 400, 1, 0)) AS success_count from log   group by client_ip order by success_count desc limit 100)
```
![](https://main.qcloudimg.com/raw/ed3d50ce8310e69ab72e50309ccc31b4/14.png)
- 访问 PV、UV 统计，统计某一时间段内的访问次数和独立的 client ip 的变化趋势
```sql
* | select date_trunc('minute', __TIMESTAMP__) as time, count(*) as pv,count( distinct client_ip) as uv group by time order by time limit 1000 
```
![](https://main.qcloudimg.com/raw/1932a986b7754f2749651fce12f844da/9.png)

