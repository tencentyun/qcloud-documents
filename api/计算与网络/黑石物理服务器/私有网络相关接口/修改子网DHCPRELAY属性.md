>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
ModifySubnetDhcpRelayFlag 用于修改子网的DHCP RELAY属性。

接口请求域名：bmvpc.api.qcloud.com


## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=ModifySubnetDhcpRelayFlag
    &<公共请求参数>
    &unVpcId=<VPC网络唯一ID>
	&unSubnetId=<子网唯一ID>
    &dhcpEnable=<是否开启dhcp relay>
	&dhcpServerIp=<DHCP SERVER 的IP地址数组>
	&ipReserve =<预留的IP个数>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifySubnetDhcpRelayFlag。

| 参数名称 |  描述 | 类型 |必选  |
|---------|---------|---------|---------|
| unVpcId | 系统分配的私有网络ID，例如：vpc-kd7d06of。可通过DescribeBmVpcEx接口查询。 |String | 是 | 
| unSubnetId | 子网ID值，例如：subnet-k20jbhp0。可通过DescribeBmSubnetEx接口查询。 |String | 是 | 
| dhcpEnable | 是否开启dhcp relay ，关闭为0，开启为1。默认为0 | Int | 否 |
| dhcpServerIp | DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。 dhcpEnable为1时为必选值。| Array |否 |
| ipReserve | 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。dhcpEnable为1时为必选值。 | Int | 否 |


## 响应

### 响应示例
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
### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。| Int |
| message |  模块错误信息描述，与接口相关。| String |
| subnetSet.n |子网信息，同时添加了子网时才会返回。| Array | 
| subnetSet.n.subnetId | 系统分配的子网ID，示例:gz_subnet_8949。| String |
| subnetSet.n.unSubnetId | 系统分配的子网统一ID，由子网ID升级而来，为了兼容这两种ID系统都支持，示例:subnet-5gu2jxf4。| String |
| subnetSet.n.dhcpEnable | 是否开启dhcp relay ，关闭为0，开启为1。默认为0 | Int |
| subnetSet.n.dhcpServerIp | DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。| Array | 
| subnetSet.n.ipReserve | 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。dhcpEnable为1时为必选值。| Int |

## 错误码

| 错误代码 |英文提示| 描述 |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | 无效的VPC,VPC资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3246  | BmVpc.InvalidDhcpServer | DHCP SERVER IP地址不合法或者IP地址个数超过限制。 |
| -3247  | BmVpc.DhcpReserveIpLimit | 没有足够的IP地址可分配用于DHCP动态使用。 |


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=ModifySubnetDhcpRelayFlag
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
	&unVpcId=vpc-kd7d06of
    &unSubnetId=subnet-kd7d06of
    &dhcpEnable=1
    &dhcpServerIp.0=10.0.200.0
    &ipReserve=5
```

### 输出
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