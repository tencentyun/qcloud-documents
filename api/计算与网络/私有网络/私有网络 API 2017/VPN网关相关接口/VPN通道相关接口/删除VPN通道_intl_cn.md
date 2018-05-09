## 1. 接口描述

本接口(DeleteVpnConn)用于删除VPN通道。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DeleteVpnConn。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 私有网络ID，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-03vihbk9,可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 | 
| vpnGwId | 是 | String | 系统分配的VPN网关ID，可使用vpnGwId或unVpnGwId，建议unVpnGwId，例如：vpngw-dystbrkv。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>接口查询。 |
| vpnConnId | 是 | String | 系统分配的VPN通道ID，可使用vpnConnId或unVpnConnId，建议使用unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>接口查询。 | 


## 3. 输出参数

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
| data.taskId | Int  | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidVpnGw.NotFound | 无效的vpn网关。vpn网关资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>接口查询vpn网关。 |
| InvalidVpnConnState | vpn通道状态不对 |
| InvalidVpnConn.NotFound | 无效的vpn通道。vpn通道资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>接口查询vpn通道。 |

## 5. 示例
 
输入
<pre>
  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteVpnConn
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-03vihbk9
  &vpnGwId=vpngw-kfldykuz
  &vpnConnId=vpnx-ol6bcqp0

</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "vpnGwId": "vpngw-kfldykuz",
        "vpcConnId": "vpnx-ol6bcqp0",
        "taskId": 12615,
        "state": 4
    }
}

```

