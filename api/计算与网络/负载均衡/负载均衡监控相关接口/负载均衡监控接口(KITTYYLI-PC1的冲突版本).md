## 1. 接口描述

GetMonitorData 接口提供了获取负载均衡的监控数据。可以根据用户传入的负载均衡命名空间、对象纬度描述和监控指标即可获得相应的监控数据。

接口访问域名：monitor.api.qcloud.com

## 2. 请求参数
   以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](/doc/api/244/4183)页面。其中，此接口的Action字段为 GetMonitorData。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> namespace
<td> 是
<td> String
<td> 命名空间，每个云产品会有一个命名空间。负载均衡共有三个命名空间：qce/lb_public、qce/lb_rs_private，其中qce/lb_public是公网负载均衡命名空间，包括负载均衡维度和后端机器维度；qce/lb_rs_private是内网负载均衡命名空间，包括内网负载均衡维度和后端机器维度
<tr>
<td> metricName
<td> 是
<td> String
<td> 指标名称，想要获取的具体监控指标，如当前连接数是connum，入流量是intraffic等。
<tr>
<td> dimensions.n.name
<td> 是
<td> String
<td> 纬度的名称，多个维度组合起来得到具体的监控数据。每个命名空间的纬度结构不同。具体纬度接口可见下面的表格，与dimensions.n.value配合使用。
<tr>
<td> dimensions.n.value
<td> 是
<td> String
<td> 相应纬度名称对应的值。
<tr>
<td> startTime
<td> 否
<td> Datetime
<td> 起始时间，如”2017-01-01 00:00:00”。默认时间为当天的”00:00:00”。
<tr>
<td> endTime
<td> 否
<td> Datetime
<td> 结束时间，如”2017-01-01 10:00:00”。默认为当前时间。注意：endTime不能小于startTime，且endTime与startTime最好为同一天。
<tr>
<td> period
<td> 否
<td> Int
<td> 监控统计周期。当前支持60s和300s两种粒度，如不传，默认使用300s粒度。
</tbody></table>

当前负载均衡可展示的指标（metricName）列表如下：

| 指标名称 | 含义 | 单位 |
|---------|---------|---------|
| connum | 当前连接数 | 个 |
| new_conn | 新增连接数 | 个 |
| intraffic | 入流量 | Mbps |
| outtraffic | 出流量 | Mbps |
| inpkg | 入包量 | 个/s |
| outpkg | 出包量 | 个/s |

当前负载均衡支持的三种命名空间以及各自的监控维度说明如下：

### 2.1 公网负载均衡命名空间qce/lb_public
qce/lb_public是公网负载均衡对应的命名空间，您可以在此空间查询到公网负载均衡的所有监控数据。
qce/lb_public支持以下4种维度组合：

1）、公网负载均衡维度

此维度体现的是一个公网负载均衡器的整体监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
</pre>

2）、公网负载均衡端口维度

此维度体现的是一个公网负载均衡器端口的监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
</pre>

3）、公网负载均衡后端服务器维度

此维度体现的是一个公网负载均衡所绑定的后端服务器的监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
|  loadBalancerPort | 负载均衡端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
|  lanIp | 负载均衡绑定机器的Ip | ip地址类型，如111.111.111.11|

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
&dimensions.3.name=vpcId
&dimensions.3.value=1111
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
</pre>

4）、公网负载均衡后端服务器端口维度
此维度体现的是一个公网负载均衡所绑定的后端服务器某个端口的监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
|  loadBalancerPort | 负载均衡端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
|  lanIp | 负载均衡绑定机器的Ip | ip地址类型，如111.111.111.11|
|  port | 负载均衡绑定机器的端口号 | int类型，如80 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
&dimensions.3.name=vpcId
&dimensions.3.value=1111
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.5.name=port
&dimensions.5.value=80
</pre>

### 2.2 内网负载均衡负载均衡维度命名空间qce/lb_rs_private
qce/lb_rs_private，您可以在此空间查询到内网负载均衡维度相关监控数据。
qce/lb_rs_private 支持以下4种维度组合：

1）、内网负载均衡维度

此维度体现的是一个内网负载均衡器的整体监控指标，需要传入的维度（dimensions.n.name）如下，由于内网vip有可能重复，所以还需要传入vpcId才能唯一指定一个lb：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
</pre>

2）、内网负载均衡端口维度

此维度体现的是一个内网负载均衡器端口的监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
|  loadBalancerPort | 负载均衡端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
</pre>



3）、内网负载均衡后端机器维度

此维度体现的是一个内网负载均衡绑定的后端机器的监控指标，需要传入的维度（dimensions.n.name）如下，由于内网vip有可能重复，所以还需要传入vpcId才能唯一指定一个lb：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
| vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
| vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
| loadBalancerPort | 负载均衡端口 | int类型，如80 |
| protocol | 协议 | string类型，如http |
| lanIp | 负载均衡绑定机器ip | ip地址类型，如111.111.111.11 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
</pre>

4）、内网负载均衡后端机器端口维度

此维度体现的是内网负载均衡绑定的后端机器的某个端口监控指标，需要传入的维度（dimensions.n.name）如下：

| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
| vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |
| vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
| loadBalancerPort | 负载均衡端口 | int类型，如80 |
| protocol | 协议 | string类型，如http |
| lanIp | 负载均衡绑定机器ip | ip地址类型，如111.111.111.11 |
| port | 负载均衡绑定机器port | int类型，如80 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.5.name=port
&dimensions.5.value=80
</pre>

### 2.3 负载均衡维度命名空间qce/loadbalance（新）
qce/loadbalance是负载均衡对应的命名空间，您可以在此空间查询到负载均衡的相关监控数据。 

当前命名空间负载均衡可展示的指标（metricName）列表如下：

| 指标名称 | 含义 | 单位 |
|---------|---------|---------|
| connum | 当前（活跃）连接数 | 个/分钟 |
| new_conn | 新增连接数 | 个/分钟 |
| intraffic | 入流量 | Mbps |
| outtraffic | 出流量 | Mbps |
| inpkg | 入包量 | 个/秒 |
| outpkg | 出包量 | 个/秒 |
| httpCode_2XX| 2xx 状态码 | 个/分钟 |
| httpCode_3XX| 3xx 状态码 | 个/分钟 |
| httpCode_4XX| 4xx 状态码 | 个/分钟 |
| httpCode_5XX| 5xx 状态码 | 个/分钟 |
| httpCode_404| 404 状态码 | 个/分钟 |
| httpCode_502| 502 状态码 | 个/分钟 |
| response_time_max| 最大响应时间 | ms |
|response_time_average| 平均响应时间 | ms |
| response_timeout_num| 响应超时个数 | 个/分钟 |
| QPS| 每秒钟请求数 | 个 |

qce/loadbalance支持以下6种维度组合：

1）、负载均衡vip维度
此维度体现的是一个负载均衡器的整体监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11 |


此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
</pre>


2）、负载均衡监听器端口维度
此维度体现的是一个负载均衡器端口的监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
</pre>


3）、负载均衡转发域名维度
此维度体现的是一个负载均衡器转发域名的监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  domain| 转发域名| string类型，如www.domain.com|

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=domain
&dimensions.1.value=www.domian.com
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
</pre>

4）、负载均衡转发路径维度
此维度体现的是一个负载均衡器转发路径的监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  domain| 转发域名| string类型，如www.domain.com|
|  url| 转发路径| string类型，如/url|

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=domain
&dimensions.1.value=www.domian.com
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.3.name=url
&dimensions.3.value=/url
</pre>

5）、负载均衡后端ip维度
此维度体现的是一个负载均衡器后端ip的监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  domain| 转发域名| string类型，如www.domain.com|
|  url| 转发路径| string类型，如/url|
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
|  lanIp | 负载均衡绑定机器的Ip | ip地址类型，如111.111.111.11|

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.1.name=domain
&dimensions.1.value=www.domian.com
&dimensions.3.name=url
&dimensions.3.value=/url
</pre>

6）、负载均衡后端端口维度
此维度体现的是一个负载均衡器后端端口的监控指标，需要传入的维度（dimensions.n.name）如下：
| 维度 | 维度解释 | 格式 |
|---------|---------|---------|
|  vip | 负载均衡VIP | ip地址类型，如111.111.111.11|
|  loadBalancerPort | 端口 | int类型，如80 |
|  protocol | 协议 | string类型，如http |
|  domain| 转发域名| string类型，如www.domain.com|
|  url| 转发路径| string类型，如/url|
|  vpcId | 负载均衡所在私有网络的Id | int类型，如1111 |
|  lanIp | 负载均衡绑定机器的Ip | ip地址类型，如111.111.111.11|
|  port | 负载均衡绑定机器的端口号 | int类型，如80 |

此维度调用方式示例：
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/loadbalance
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.5.name=port
&dimensions.5.value=80
&dimensions.1.name=domain
&dimensions.1.value=www.domian.com
&dimensions.3.name=url
&dimensions.3.value=/url
</pre>

## 3. 返回参数

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码" target="_blank">公共错误码</a>。
<tr>
<td> codeDesc
<td> String
<td> 英文错误码。
<tr>
<td> message
<td> String
<td> 错误信息详细描述。
<tr>
<td> startTime
<td> Datetime
<td> 起始时间。
<tr>
<td> endTime
<td> Datetime
<td> 结束时间。
<tr>
<td> metricName
<td> String
<td> 指标名称。
<tr>
<td> period
<td> Int
<td> 监控统计周期。
<tr>
<td> dataPoints
<td> Object
<td> 监控数据列表。数组每个元素是监控点数据。
</tbody></table>

## 4. 示例
输入
<pre>
 
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&&lt;<a href="https://cloud.tencent.com/doc/api/229/6976" target="_blank">公共请求参数</a>&gt;
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=protocol
&dimensions.0.value=HTTP
&dimensions.1.name=vip
&dimensions.1.value=111.111.111.111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&startTime=2015-12-28 14:00:00
&endTime=2015-12-28 14:05:00
&period=300
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "metricName": "connum",
    "startTime": "2015-12-28 14:00:00",
    "endTime": "2015-12-28 14:05:00",
    "period": 300,
    "dataPoints":  [
           0
        ]
}
```
