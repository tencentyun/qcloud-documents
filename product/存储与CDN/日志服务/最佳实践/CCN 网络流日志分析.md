## 概述

[网络流日志（Flow Logs，FL）](https://cloud.tencent.com/document/product/682/18931) 为您提供全时、全流、非侵入的流量采集服务，可将采集的网络流量进行实时的存储、分析，适用于故障排查、合规审计、架构优化、安全检测等场景，让您的云上网络更加稳定、安全和智能。

您可以创建指定采集范围（例如弹性网卡、NAT 网关、云联网跨地域流量）的网络流日志，来采集该范围内传入/传出的流量。

## 前提条件

已将 [云联网（Cloud Connect Network，CCN）](https://cloud.tencent.com/document/product/877) 网络流日志采集至日志服务（Cloud Log Service，CLS），详见 [操作详情](https://cloud.tencent.com/document/product/682/18966)。

## 场景示例

### CLS 分析云联网流日志

流日志 FlowLog 与 CLS 实现打通， 用户可以将 云联网流日志 的数据实时投递至 CLS， 并进一步使用 CLS 的检索和 SQL 分析能力， 来满足不同场景下用户个性化的实时日志分析需求：

- 日志一键投递
- 百亿级日志， 秒级分析
- Dashboard 仪表盘实时日志可视化
- 一分钟实时告警


### 云联网流日志字段说明

| 字段        | 数据类型 | 说明                                                         |
| :---------- | :------- | :----------------------------------------------------------- |
| srcaddr     | text     | 源 IP。                                                      |
| dstregionid | text     | 流量目的地域。                                               |
| dstport     | long     | 流量的目标端口。该字段仅对 UDP/TCP 协议生效，当流量为其他协议时，该字段显示为“-”。 |
| start       | long     | 当前捕获窗口收到第一个报文的时间戳，如果在捕获窗口内没有报文，则显示为该捕获窗口的起始时间，采用 Unix 秒的格式。 |
| dstaddr     | text     | 目标 IP。                                                    |
| version     | text     | 流日志版本。                                                 |
| packets     | long     | 捕获窗口中传输的数据包的数量。当“log-status”为“NODATA”时，该字段显示为“-”。 |
| ccn-id      | text     | 云联网唯一标识，如需确定云联网的信息请 [联系我们](https://cloud.tencent.com/document/product/877/59695)。 |
| protocol    | long     | 流量的 IANA 协议编号。有关更多信息，请转到分配的 [Internet 协议](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml#protocol-numbers-1) 编号。 |
| srcregionid | text     | 流量源地域。                                                 |
| bytes       | long     | 捕获窗口中传输的字节数。当 “log-status” 为 “NODATA” 时，该字段显示为“-”。 |
| action      | text     | 与流量关联的操作：<ul  style="margin: 0;"><li> ACCEPT：通过云联网正常转发的跨地域流量。</li><li>REJECT：因限速被阻止转发的跨地域流量。</li></ul>  |
| region-id   | text     | 记录日志的地域。                                             |
| srcport     | text     | 流量的源端口。该字段仅对 UDP/TCP 协议生效，当流量为其他协议时，该字段显示为“-”。 |
| end         | long     | 当前捕获窗口收到最后一个报文的时间戳，如果在捕获窗口内没有报文，则显示为该捕获窗口的结束时间，采用 Unix 秒的格式。 |
| log-status  | text     | 流日志的日志记录状态： <ul  style="margin: 0;"><li> OK：表示数据正常记录到指定目标。</li><li> NODATA：表示捕获窗口中没有传入或传出网络流量，此时 “packets” 和 “bytes” 字段会显示为“-1”。</li></ul>  |



### 云联网访问分析

#### 场景概述

为了更好的管理业务，根据业务发展需求随时对各地域的带宽上限进行调整，需要对各地域间的带宽进行监控统计，设置带宽使用预警。

<dx-accordion>
::: 各线路带宽趋势
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(bytes)/60.00*8 as bandwidth, concat(concat('srcRegion : ',srcregionid, ' , dstRegion : '), dstregionid) as region_ip group by time, region_ip limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/abf58cc6c711774c77af3e81d940b529.png)
:::
::: 各线路 PPS 趋势
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(packets)/60.00 as pps, concat(concat('srcRegion : ',srcregionid, ' , dstRegion : '), dstregionid) as region_ip group by time, region_ip limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/3feed866d0d1ed4e143d5d99ffc6fd06.png)

:::
::: TOP20线路总流量分布
```sql
log-status:OK | select concat(concat('srcRegion : ',srcregionid, ' , dstRegion : '), dstregionid) as region, sum(bytes) as bytes group by region order by bytes desc limit 20
```

![](https://qcloudimg.tencent-cloud.cn/raw/9e6c04a93dbb2d134fc949e067592b81.png)

:::
::: Top10源 IP 流量带宽
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(bytes)/60.00*8 as pps  , srcaddr where srcaddr in (select srcaddr group by srcaddr order by sum(cast(bytes as double)) desc limit 10)  group by time, srcaddr limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/8e1e19ebaca4fa77ad5606f8d3829fa0.png)

:::
::: Top10源 IP 流量 PPS
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(packets)/60.00 as pps  , srcaddr where srcaddr in (select srcaddr group by srcaddr order by sum(cast(packets as double)) desc limit 10) group by time, srcaddr  limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/a3672cb2f7fd597dc0da51fea119e883.png)

:::
::: Top10协议流量带宽
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(bytes)/60*8 as bandwidth, cast(protocol as varchar) where protocol in ( select protocol group by protocol order by sum(cast(bytes as double)) desc limit 10) group by time, protocol  limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/8e6802c2b55f3fbd21e4631f0f8c110f.png)

:::
::: Top10各协议流量 PPS
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(packets)/60.00 as pps, cast(protocol as varchar) where protocol in ( select protocol group by protocol order by sum(cast(bytes as double)) desc limit 10) group by time, protocol  limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/880fedda6d9b1418625c3c790b89bc57.png)

:::
::: 拒绝访问占比
```sql
log-status:OK | select round(sum(case when action = 'REJECT' then 1.00 else 0.00 end) / cast(count(*) as double) * 100,2) as "拒绝访问占比(%)"
```

![](https://qcloudimg.tencent-cloud.cn/raw/e177cbfa10485af3ba0918c57fe24284.png)

:::
::: ACCEPT 与 REJECT 的带宽趋势
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(bytes)/60.00*8 as bandwidth, action group by time, action limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/4fbb33da3f04893a1f4129b27bb8d844.png)

:::
::: ACCEPT 与 REJECT 的 PPS
```sql
log-status:OK | select histogram(cast(__TIMESTAMP__ as timestamp), interval 1 MINUTE) as time, sum(packets)/60.00 as pps, action group by time, action limit 10000
```

![](https://qcloudimg.tencent-cloud.cn/raw/8b7480cb468ecfe1d1b037f4d31c85e4.png)

:::
::: 某线路带宽的阈值告警
使用中给某线路配置了带宽上限，需要监控配置的合理性，随时对某地域的带宽上限进行调整，轻松掌控网络。例如，初次配置了中国香港-硅谷线路的带宽上限为100Mbps，当该线路的带宽使用，连续10min带宽都大于等于95Mbps时，即进行告警，以便于及时调整带宽上限。

根据以上场景，配置 CLS 告警。

1. 新建监控任务，输入以下执行语句，时间范围选择1分钟，统计近1分钟内的中国香港-硅谷线路带宽使用情况，每分钟执行1次。
```sql
log-status:OK AND srcregionid:ap-hongkong AND dstregionid:na-siliconvalley | select sum(bytes)/60.00*8/1000 as bandwidth
```
![](https://qcloudimg.tencent-cloud.cn/raw/76fbcc7cfab5b0e46b9b7daef496d400.png)
2. 配置告警策略，当连续10次（即10分钟）的监控任务结果都大于等于95Mbps时，则触发告警。
![](https://qcloudimg.tencent-cloud.cn/raw/404fb206909a0278fe307284da4fe492.png)

:::
</dx-accordion>
