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
|url|应用型负载均衡监听器转发规则的路径。长度限制为：1 ~ 80。使用格式有两种：无修饰符格式，有修饰符格式。<br>修饰符可以使用的有：`~`、 `~\*` 、` ^~` 、`=`， 其中：<br>`~`表示接下来的表达式为大小写敏感的正则表达式<br>`~*`修饰符表示大小写不敏感的正则表达式<br>`^~`修饰符表示如果该表达式被认定为最佳匹配，那么不再进行以下的搜索匹配<br>`=`表示精确匹配，只有请求与该表达式完全相同才满足该转发。<br>非正则表达式可用的字符包括字母、数字、`_`、`-`、`.`、`=`、`？`、`/`|String|是|
|sessionExpire|应用型负载均衡监听器转发规则的会话保持时间，0 表示关闭，可选值：30 ~ 3600|Int|否|
|healthSwitch|应用型负载均衡监听器转发规则健康检查，默认值 1；1 表示开启，0 表示关闭|Int|否|
|intervalTime|应用型负载均衡监听器转发规则健康检查的检查间隔时间，默认值 5，可选值：5 ~ 300，单位：秒|Int|否|
|healthNum|应用型负载均衡监听器转发规则健康阀值，默认值 3，表示当连续探测三次健康则表示该转发正常，可选值：2 ~ 10，单位：次|Int|否|
|unhealthNum|应用型负载均衡监听器转发规则不健康阀值，默认值 3，表示当连续探测三次不健康则表示该转发不正常，可选值：2 ~ 10，单位：次|Int|否|
|httpHash|应用型负载均衡监听器转发规则的转发方式。可选值：wrr、ip_hash，least_conn<br>分别表示按权重轮询、根据源 IP 进行哈希到后端机器，最小连接数的调度方式，默认为 wrr。|Int|否|
|httpCode|应用型负载均衡监听器转发规则的健康状态码。可选值：1 ~ 31，默认 31。<br>1 表示探测后返回值 1xx 表示健康，<br>2 表示返回  2xx 表示健康，<br>4 表示返回 3xx 表示健康，<br>8 表示返回 4xx 表示健康，<br>16 表示返回 5xx 表示健康。<br>若希望多种码都表示健康，则将相应的值相加|Int|否|
|httpCheckPath|应用型负载均衡监听器转发规则的探测路径，默认`/`，必须以`/`开头。长度限制为：1 ~ 80，可用的字符包括字母、数字、`_`、`-`、`.`、`=`、`？`、`/`|String|否|

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
