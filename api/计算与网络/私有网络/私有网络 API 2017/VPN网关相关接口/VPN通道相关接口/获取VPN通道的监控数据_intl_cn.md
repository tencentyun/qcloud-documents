## 1. 接口描述

本接口(DescribeVpnConnMonitor)用于获取VPN通道的监控数据。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeVpnConnMonitor。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 私有网络ID，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-03vihbk9,可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 | 
| vpnGwId | 是 | String | 系统分配的VPN网关ID，可使用vpnGwId或unVpnGwId，建议unVpnGwId，例如：vpngw-dystbrkv。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>接口查询。 |
| vpnConnId | 是 | String | 系统分配的VPN通道ID，可使用vpnConnId或unVpnConnId，建议使用unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E9%80%9A%E9%81%93%E5%88%97%E8%A1%A8" title="DescribeVpnConn">DescribeVpnConn</a>接口查询。 |  
| metricName | 是 | String | 监控指标名称（目前只支持两个指标：“outtraffic”公网出流量；"intraffic" 公网入流量） |
| starttime | 否 | datetime | 开始时间，开始时间不填写默认为昨天此时。时间跨度不能超过2天。超过2天时，开始时间将被设置为结束时间减2天，例如：2016-07-06 12:00:00 |
| endtime | 否 | datetime | 结束时间，结束时间不填写默认是当前时间，例如：2016-07-07 12:00:00 |
 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
| data.data | Array  | 通道指标流量带宽，单位bps，每5min记录。 示例：data[1] 表示 (starttime+5) ~ (starttime+10)  min的通道指标流量带宽，metricName为outtraffic表示返回出流量，intraffic时表示返回为入流量 |

## 4. 错误码表
 该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc错误码</a>

## 5. 示例
 
输入
<pre>
https://domain/v2/index.php?Action=DescribeVpnConnMonitor
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=7
&vpnGwId=8
&vpnConnId=5
&metricName=outtraffic
&starttime=2015-07-14 00:00:00
&endtime=2015-07-14 23:00:00
</pre>

输出
```

{
    "code" : 0,
    "message" : "ok",
    "data" : [
		1221,
		1212,
		787
	],
}


