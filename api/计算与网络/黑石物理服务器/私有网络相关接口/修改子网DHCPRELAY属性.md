## 1. 接口描述
 
本接口（ModifySubnetDhcpRelayFlag）用于修改子网的DHCP RELAY属性。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>



## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifySubnetDhcpRelayFlag。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络ID，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-kd7d06of。可通过DescribeBmVpcEx接口查询。 |
| subnetId | 是 | String | 子网ID值，可使用subnetId或unSubnetId，建议使用unsubnetId，例如：subnet-k20jbhp0。可通过DescribeBmSubnetEx接口查询。 |
| dhcpEnable | 否 | Int | 是否开启dhcp relay ，关闭为0，开启为1。默认为0 |
| dhcpServerIp | 否 | Array | DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。 dhcpEnable为1时为必选值。|
| ipReserve | 否 | Int | 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。dhcpEnable为1时为必选值。 |

 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| subnetSet.n | Array | 子网信息，同时添加了子网时才会返回。|
| subnetSet.n.subnetId | String | 系统分配的子网ID，示例:subnetId_GZ_23。|
| subnetSet.n.unSubnetId | String | 系统分配的子网统一ID，由子网ID升级而来，为了兼容这两种ID系统都支持，示例:subnet-5gu2jxf4。|
| subnetSet.n.dhcpEnable | Int | 是否开启dhcp relay ，关闭为0，开启为1。默认为0 |
| subnetSet.n.dhcpServerIp | Array |  DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。|
| subnetSet.n.ipReserve | Int | 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。dhcpEnable为1时为必选值。|

  ## 4. 错误码表
 
| 错误代码 |英文提示| 描述 |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | 无效的VPC,VPC资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3246  | BmVpc.InvalidDhcpServer | DHCP SERVER IP地址不合法或者IP地址个数超过限制。 |
| -3247  | BmVpc.DhcpReserveIpLimit | 没有足够的IP地址可分配用于DHCP动态使用。 |




## 5. 示例
 
输入
```

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifySubnetDhcpRelayFlag
	&<公共请求参数>
	&vpcId=vpc-kd7d06of
    &subnetId=subnet-kd7d06of
    &dhcpEnable=1
    &dhcpServerIp.0=10.0.200.0
    &ipReserve=5
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "subnetSet": [
        {
            "subnetId": "gz_subnet_8949",
            "unSubnetId": "subnet-gvt14y8u",
            "subnetName": "tttt",
            "cidrBlock": "10.10.30.0/24",
            "zoneId": 1000800001
        }
    ]
}

```

