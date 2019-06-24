>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
ApplyIps 用于申请黑石私有网络子网 IP。

为了避免出现 IP 冲突导致网络异常的情况，当您需要使用某些子网下的 IP 资源时（物理机 IP 除外），需要调用此接口进行 IP 申请。该接口会从子网未分配的 IP 列表中，按从小到大的规则随机进行 IP 分配（分配出来后才知道具体分配了哪些 IP）。
- 当子网中可用的 IP 个数为 0 时，调用此接口进行 IP 资源申请，会返回没有可用的 IP 资源。
- 已申请分配出来的 IP 资源，黑石侧不会再次分配出来，除非您把 IP 资源退还了。
- 已经申请出来的 IP 资源，可用 IP 资源列表中将不再返回此 IP。

接口请求域名：bmvpc.api.qcloud.com


## 请求

### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?Action=ApplyIps
    &<公共请求参数>
    &unVpcId=<VPC网络唯一ID>
	&unSubnetId=<子网唯一ID>
	&count=<申请IP个数>
```
### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的 Action 字段为 ApplyIps。

| 参数名称 |描述 | 类型 | 必选  | 
|---------|---------|---------|---------|
| unVpcId |系统分配的私有网络 ID，例如：vpc-kd7d06of。可通过 DescribeBmVpcEx 接口查询返回的 unVpcId 值。 | String |  是 |
| unSubnetId |  系统分配的私有网络子网 ID，例如：subnet-k20jbhp0。可通过DescribeBmSubnetEx接口查询返回的unSubnetId值。 |String | 是 |
| count |申请 IP 个数，默认为1，取值范围 1-20。 | Int |  否 |


## 响应

### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.6.100.40"
    ],
    "count": 1
}
```
### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| count |申请成功的 IP 个数。| Int | 
| data.n | 申请成功的 IP 数组。| Array |

## 错误码

| 错误代码 |英文提示| 描述 |
|---------|---------|---------|
| -3047 |InvalidBmVpc.NotFound| 无效的 VPC,VPC 资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3030  |InvalidBmSubnet.NotFound| 无效的子网,子网资源不存在，请再次核实您输入的资源信息是否正确。 |
| -3031 |AvailableIpUseUp| 没有可用的 IP 可以分配。 |
| -3001| InvalidInputParams|参数不合法


## 实际案例
### 输入
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
	Action=ApplyIps
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
	&unVpcId=vpc-2ari9m7h
	&unSubnetId=subnet-keqt3oty
	&count=1
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.6.100.40"
    ],
    "count": 1
}
```
