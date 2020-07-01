>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 接口描述
本接口（CreateIngress）用于创建 Ingress。

接口请求域名：
```
ccs.api.qcloud.com
```

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称   | 描述                               | 类型     | 必选 |
|------------|------------------------------------|----------|------|
| clusterId   | 集群 ID，请填写 [查询集群列表](/doc/api/457/9448) 接口中返回的 clusterId 字段 |String | 是    |
| ingressName| Ingress 名称 | String | 是 |
| ingressDesc | Ingress 描述 | String | 否 |
| certId | SSL 证书 ID | String | 否 |
| rules| 转发规则 | Object Array | 否 |
| namespace | 命名空间，请填写 [查询集群命名空间](/doc/api/457/9430) 接口中返回的 namespaces 字段，默认为 default |String  |否 |
| unSubnetId | 内网 Ingress 所属的 Subnet ID | String | 否 |
| internetChargeType | TRAFFIC_POSTPAID_BY_HOUR 或者 BANDWIDTH_POSTPAID_BY_HOUR | String | 否 |
| internetMaxBandwidthOut | 带宽上限，必须大于 0 | Int | 否 |

rules 参数详细说明：

| 字段 | 描述 | 类型 | 必选 | 
|---------|---------|---------|---------|
|url|应用型负载均衡监听器转发规则的路径。长度限制为：1 ~ 80。使用格式有两种：无修饰符格式，有修饰符格式。修饰符可以使用的有：`~`、` ~\*` 、` ^~` 、 `=` ，其中：<br><li> `~`表示接下来的表达式为大小写敏感的正则表达式<li>`~*`修饰符表示大小写不敏感的正则表达式<li>`^~` 修饰符表示如果该表达式被认定为最佳匹配，那么不再进行以下的搜索匹配<li>`=`表示精确匹配，只有请求与该表达式完全相同才满足该转发<br>非正则表达式可用的字符包括字母、数字、`_`、`-`、`.`、`=`、`?`、`/`|String|是|
|domain|应用型负载均衡监听器转发规则的域名。长度限制为：1 ~ 80。有三种使用格式：非正则表达式格式，通配符格式，正则表达式格式。<li>非正则表达式格式只能使用字母、数字、`-`、`.`。<li>通配符格式的使用，`*`只能在开头或者结尾。<li>正则表达式以`~`开头，支持 Nginx 原生的正则表达式。|String|是|
|protocol|应用型负载均衡监听器转发规则的协议类型|String|是|
|serviceName|后端服务名称|String|是|
|servicePort|后端服务端口|Int|是|
|LoadBalancePort|应用型负载均衡开放端口|Int|是|

## 输出参数
| 参数名称 | 描述 |类型 |
|----------|------|-----|
| code |公共错误码。0 表示成功，其他值表示失败| Int |
| codeDesc | 业务错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message | 模块错误信息描述，与接口相关|String |

## 示例
### 输入
```
 https://domain/v2/index.php?Action=CreateIngress
  &clusterId=cls-xxxxx
  &namespace=default
  &ingressName=test
  &ingressDesc=test
  &其它公共参数
```
### 输出
```
{
    "data":{
        "code":0,
        "message":"",
        "codeDesc":"Success",
        "data":[

        ]
    },
    "message":"",
    "code":0
}
```
