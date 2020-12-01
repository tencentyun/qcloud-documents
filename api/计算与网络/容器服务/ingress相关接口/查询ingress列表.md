>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>

## 接口描述
本接口（DescribeIngress）用于查询 Ingress 列表。

接口请求域名：
```
ccs.api.qcloud.com
```


## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称   | 描述                               | 类型     | 必选 |
|------------|------------------------------------|----------|------|
| clusterId   | 集群 ID，请填写 [查询集群列表](/doc/api/457/9448) 接口中返回的 clusterId 字段 |String | 是    |
| namespace | 命名空间，请填写 [查询集群命名空间](/doc/api/457/9430) 接口中返回的 namespaces 字段，默认为 default|String |否|
| allnamespace| 是否使用所有的命名空间。1：是，0 或不传：否| Uint/Float | 否 |

## 输出参数

| 参数名称 | 描述 |类型 |
|----------|------|-----|
| code |公共错误码。0 表示成功，其他值表示失败| Int |
| codeDesc | 业务错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message | 模块错误信息描述，与接口相关| String |
| data | Ingress 列表相关数据 |Object |

data 字段的结构如下：

| 参数名称 | 描述 |类型 |
|---------|---------|---------|
| ingressList | 日志收集规则 | Object |


ingressList 字段中 Object 的结构如下：

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| ingressList | Ingress 列表信息 | Object Array |
| ingressName | Ingress 名称 | String |
| ingressDesc | Ingress 描述 | String |
| lbId | 应用型负载均衡 ID | String |
| ingressIp | Ingress 的虚拟 IP | String |
| rules | 转发规则，详情见 [创建 Ingress](/document/product/457/17544) 接口 | Array |
| createAt | Ingress 创建时间 | String |
| namespace | 命名空间 | String |
| unSubnetId | 内网 Ingress 所属的 Subnet ID | String |

## 示例
### 输入
```
 https://domain/v2/index.php?Action=DescribeIngress
  &clusterId=cls-xxxxx
  &namespace=default
  &其它公共参数
```

### 输出
```
{
    "data":{
        "code":0,
        "message":"",
        "codeDesc":"Success",
        "data":{
            "ingressList":[
                {
                    "ingressName":"test",
                    "ingressDesc":"test",
                    "lbId":"lb-xxxxx",
                    "ingressIp":"193.112.230.126",
                    "rules":[

                    ],
                    "createdAt":"2018-04-25 12:31:58",
                    "namespace":"default",
                    "unSubnetId":""
                }
            ]
        }
    },
    "message":"",
    "code":0
}
```

