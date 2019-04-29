## 1. 接口描述

本接口(AssignPrivateIpAddresses)用于弹性网卡申请内网 IP。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

1) 一个弹性网卡支持绑定的IP地址是有限制的，更多vpc资源限制信息详见<a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>。
2) 可以指定内网IP地址申请，内网IP地址类型不能为主IP，主IP已存在，不能修改，内网IP必须要弹性网卡所在子网内，而且不能被占用。
3) 在弹性网卡上申请一个到多个辅助内网IP，接口会在弹性网卡所在子网网段内返回指定数量的辅助内网IP。


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/245/4772" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为AssignPrivateIpAddresses。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 弹性网卡对应的私用网络ID，例如：vpc-7t9nf3pu |
| networkInterfaceId | 是 | String | 弹性网卡ID，例如：eni-m6dyj72l |
| privateIpAddressSet.n | 否 | Array | 申请内网ip时，指定IP地址申请，可以指定主IP，是个可选项。 |
| privateIpAddressSet.n.primary | 是 | Bool | 是否为主IP，只能设置一个主IP。 |
| privateIpAddressSet.n.privateIpAddress | 是 | String | 指定的内网IP地址。 |
| secondaryPrivateIpAddressCount | 否 | Int | 申请内网ip时，只指定数量，由系统自动生成IP，可选项。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功, 其他值：失败|
| message | String | 错误信息|
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC，VPC资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC |
| InvalidNetworkInterface.NotFound | 无效的弹性网卡，弹性网卡资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e5%bc%b9%e6%80%a7%e7%bd%91%e5%8d%a1%e4%bf%a1%e6%81%af?viewType=preview" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a>接口查询弹性网卡 |
| InvalidPrivateIpAddress.InUse | 内网IP已经被占用 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=AssignPrivateIpAddresses
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-7t9nf3pu
&networkInterfaceId=eni-m6dyj72l
&secondaryPrivateIpAddressCount=1
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

