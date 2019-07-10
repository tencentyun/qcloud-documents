>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
 
DescribeBmBindInfo 提供了查询黑石物理机ID和虚机IP绑定的黑石负载均衡详情功能。

接口请求域名：bmlb.api.qcloud.com


## 请求
### 请求示例

```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=DescribeBmBindInfo
	&<公共请求参数>
	&vpcId=<黑石私有网络整形ID>
	&instanceIds.0=<主机ID>
	&instanceIds.1=<虚机IP>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 DescribeBmBindInfo。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 否 | Int | 黑石私有网络整形ID。|
| unVpcId | 否 | String | 黑石私有网络唯一ID。|
| instanceIds.n | 是 | Array | 主机ID或虚机IP列表，可用于获取绑定了该主机的负载均衡列表。|


## 响应
### 响应示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-abcdefgh",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "unVpcId": "vpc-abcdefgh",
            "vip": "100.100.100.100",
            "tgwSetType": "fullnat",
            "exclusive": 0,
            "L4ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgh",
                    "protocol": "tcp",
                    "loadBalancerPort": 1234,
                    "rsList": [
                        {
                            "instanceId": "1.1.1.1",
                            "rsPort": 1234
                        }
                    ]
                }
            ],
            "L7ListenerSet": [
                {
                    "listenerId": "lbl-abcdefge",
                    "protocol": "http",
                    "loadBalancerPort": 80,
                    "ruleSet": [
                        {
                            "domain": "a.com",
                            "domainId": "dm-abcdefgh",
                            "locations": [
                                {
                                    "url": "/",
                                    "locationId": "loc-abcdefgh",
                                    "rsList": [
                                        {
                                            "instanceId": "1.1.1.1",
                                            "rsPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "totalCount": 1
}
```

### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。|
| message | String | 错误信息描述，与接口相关。|
| codeDesc | String | 返回码信息描述。|
| loadBalancerSet | Array | 返回的负载均衡列表。|

loadBalancerSet每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| loadBalancerId | String | 负载均衡实例ID。|
| appId | Int | 开发商AppId。|
| projectId | Int | 负载均衡所属的项目ID。|
| vpcId | Int | 黑石私有网络整形ID。|
| unVpcId | String | 黑石私有网络唯一ID。|
| vip | String | 负载均衡的IP地址。|
| tgwSetType | String | 负载均衡对应的TGW集群类别，取值为tunnel或fullnat。tunnel表示隧道集群，fullnat表示FULLNAT集群。|
| exclusive | Int | 是否独占TGW集群。|
| L4ListenerSet | Array | 具有该绑定关系的四层监听器列表。|
| L7ListenerSet | Array | 具有该绑定关系的七层监听器列表。|

L4ListenerSet每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| listenerId | String | 负载均衡七层监听器ID。|
| listenerName | String | 负载均衡七层监听器名称。|
| protocol | String | 负载均衡七层监听器协议类型，可选值：http,https。|
| loadBalancerPort | Int | 负载均衡七层监听器的监听接口。|
| rsList | Array | 该转发路径所绑定的主机列表。|

rsList每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| instanceId | String | 黑石物理机的主机ID或虚机IP。|
| rsPort | Int | 主机端口。|


L7ListenerSet每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| listenerId | String | 七层监听器实例ID。|
| listenerName | String | 七层监听器名称。|
| protocol | String | 七层监听器协议类型，可选值：http,https。|
| loadBalancerPort | Int | 七层监听器的监听端口。|
| ruleSet | Array | 返回的转发规则列表。|

ruleSet每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| domain | String | 转发域名。|
| domainId | String | 转发域名ID。|
| locations | Array | 转发路径列表。|

locations每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| url | String | 转发路径。|
| locationId | String | 转发路径实例ID。|
| rsList | Array | 该转发路径所绑定的主机列表。|

rsList每一个子项目包含字段如下

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| instanceId | String | 黑石物理机的主机ID或虚机IP。|
| rsPort | Int | 主机端口。|


## 错误码

| 错误代码 | 英文提示 | 错误描述 |
|------|------|------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError.CCDBAbnormal | CCDB 服务异常 |


## 实际案例
 
### 输入

```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=DescribeBmBindInfo
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=24763
	&Timestamp=1507714922
	&Region=bj
	&vpcId=XXX
	&instanceIds.0=1.1.1.1
	&instanceIds.1=cpm-abcdefgh
	&Signature=AySJsE6Zq3knXwPSzxlYUl%2FrM90%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-abcdefgh",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "unVpcId": "vpc-abcdefgh",
            "vip": "100.100.100.100",
            "tgwSetType": "fullnat",
            "exclusive": 0,
            "L4ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgh",
                    "protocol": "tcp",
                    "loadBalancerPort": 1234,
                    "rsList": [
                        {
                            "instanceId": "1.1.1.1",
                            "rsPort": 1234
                        }
                    ]
                }
            ],
            "L7ListenerSet": [
                {
                    "listenerId": "lbl-abcdefge",
                    "protocol": "http",
                    "loadBalancerPort": 80,
                    "ruleSet": [
                        {
                            "domain": "a.com",
                            "domainId": "dm-abcdefgh",
                            "locations": [
                                {
                                    "url": "/",
                                    "locationId": "loc-abcdefgh",
                                    "rsList": [
                                        {
                                            "instanceId": "1.1.1.1",
                                            "rsPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "loadBalancerId": "lb-abcdefge",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "unVpcId": "vpc-abcdefgh",
            "vip": "115.115.115.115",
            "tgwSetType": "fullnat",
            "exclusive": 0,
            "L4ListenerSet": [],
            "L7ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgi",
                    "protocol": "http",
                    "loadBalancerPort": 80,
                    "ruleSet": [
                        {
                            "domain": "a.com",
                            "domainId": "dm-abcdefge",
                            "locations": [
                                {
                                    "url": "/",
                                    "locationId": "loc-abcdefgi",
                                    "rsList": [
                                        {
                                            "instanceId": "cpm-abcdefgh",
                                            "rsPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "loadBalancerId": "lb-abcdefgi",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "unVpcId": "vpc-abcdefgh",
            "vip": "115.115.115.116",
            "tgwSetType": "tunnel",
            "exclusive": 0,
            "L4ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgg",
                    "protocol": "tcp",
                    "loadBalancerPort": 1234,
                    "rsList": [
                        {
                            "instanceId": "cpm-abcdefgh",
                            "rsPort": 1234
                        }
                    ]
                }
            ],
            "L7ListenerSet": []
        }
    ],
    "totalCount": 3
}

```