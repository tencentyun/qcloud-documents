>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (ModifyBmForwardListener) 提供了修改黑石负载均衡七层监听器功能。

接口请求域名：<font style="color:red">bmlb.api.qcloud.com</font>


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/product/386/6718)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| loadBalancerId | 是 | String |   负载均衡实例ID，可通过接口[DescribeBmLoadBalancers](/document/product/386/9306)查询。|
| listenerId | 是 | String | 七层监听器ID，可通过接口[DescribeBmForwardListeners](/document/product/386/9283)查询。|
| listenerName|否|String|更新为的负载均衡七层监听器名称。|
| sslMode|否|Int|负载均衡七层监听器的认证方式：0（不认证，用于http），1（单向认证，用于https），2（双向认证，用于https）。|
| certId|否|String|更新为的负载均衡七层监听器的服务端证书ID。|
| certName|否|String|更新为的负载均衡七层监听器的服务端证书名称。|
| certContent|否|String|更新为的负载均衡七层监听器的服务端证书内容。|
| certKey|否|String|更新为的负载均衡七层监听器的服务端证书密钥。|
| certCaId|否|String|更新为的负载均衡七层监听器的客户端证书ID。|
| certCaName|否|String|更新为的负载均衡七层监听器的客户端证书名称。|
| certCaContent|否|String|更新为的负载均衡七层监听器的客户端证书内容。|
| bandwidth|否|Int|更新为的监听器最大带宽值，可选值：0-1000，单位：Mbps。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 返回码信息描述。|
| requestId | Int | 任务ID。该接口为异步任务，可根据本参数调用[DescribeBmLoadBalancersTaskResult](/document/product/386/9308)接口来查询任务操作结果|


模块错误码

| 错误代码 | 英文提示 | 错误描述 |
|------|------|------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError.CCDBAbnormal | CCDB 服务异常 |
| 11041 | InvalidParameter.CCDBLBNotExist | CCDB中不存在该负载均衡记录信息 |
| 12003 | IncorrectStatus.LBWrongStatus | 该负载均衡状态不正确,无法执行当前操作 |
| -12000 | InvalidL7Listener.NotExist | CCDB中不存在该七层监听器 |
| -12010 | IncorrectStatus.ListenerWrongStatus | 该负载均衡监听器状态不正确 |
| -20002 | InvalidParameter.InvalidCertContent | 证书内容不合法 |
| -20000 | InvalidResource.CertPlatformErr | 访问证书平台异常 |
| -12020 | InvalidParameter.certNotInValidTime | 证书不在合法使用时段 |


## 4. 示例
 
输入

<pre>
https://domain/v2/index.php?Action=ModifyBmForwardListener
&<<a href="https://www.qcloud.com/document/product/386/6718">公共请求参数</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&listenerName=https-listener
&SSLMode=1
&certId=abcdefgh
</pre>

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId" : 1234
}

```