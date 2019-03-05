## 1. 接口描述

本接口(CreateNetworkInterface)用于创建弹性网卡。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
2) 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
3) 创建弹性网卡同时可以绑定已有安全组。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/245/4772" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateNetworkInterface。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 弹性网卡所在的私有网络ID，推荐使用新ID，例如：vpc-7t9nf3pu。 |
| subnetId | 是 | String | 弹性网卡所在的子网ID，推荐使用新ID，例如：subnet-0ap8nwca。 |
| eniName | 是 | String | 弹性网卡名称，可任意命名，但不得超过60个字符。 |
| eniDescription | 否 | String | 弹性网卡描述，可任意命名，但不得超过60个字符。 |
| privateIpAddressSet.n | 否 | Array | 指定的内网IP地址数组。 |
| privateIpAddressSet.n.primary | 是 | Bool | 是否为主IP，只能设置一个主IP。 |
| privateIpAddressSet.n.privateIpAddress | 是 | String | 指定的内网IP地址。 |
| secondaryPrivateIpAddressCount | 否 | Int | 需要新申请的内网IP地址个数。|
| sgIds.n | 否 | Array | 指定绑定的安全组，例如:['sg-1dd51d']。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC |
| InvalidSubnet.NotFound | 无效的子网，子网资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8" title="DescribeSubnetEx">DescribeSubnetEx</a>接口查询子网 |
| InvalidNetworkInterfaceName | 弹性网卡名称不合法。可任意命名，但不得超过60个字符。 |
| NetworkInterfaceLimitExceeded | 创建的弹性网卡数量超过上限。如果需要更多资源，请联系客服申请。更多VPC资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a> |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=CreateNetworkInterface
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-7t9nf3pu
&subnetId=subnet-0ap8nwca
&eniName=eni
&secondaryPrivateIpAddressCount=1
&sgIds.0=sg-1dd51d
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data":
        {
            "taskId": 16284
        }
}
```

