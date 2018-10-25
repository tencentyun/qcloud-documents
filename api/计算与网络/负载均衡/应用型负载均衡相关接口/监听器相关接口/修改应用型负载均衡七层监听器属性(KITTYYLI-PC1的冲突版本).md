## 1. 接口描述
 ModifyForwardLBSeventhListener 接口用来修改应用型负载均衡七层监听器的属性。
 
接口访问域名：lb.api.qcloud.com


## 2. 请求参数

   以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](/doc/api/244/4183)页面。其中，此接口的Action字段为 ModifyForwardLBSeventhListener。
 
|参数名称|必选|类型|描述|
|-----|------|--------|-----------|
|loadBalancerId|是|String|负载均衡实例统一ID，即 unLoadBalancerId，可通过<a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>接口同时入参forward字段为1或者-1来查询。|
|listenerId|是|String|应用型负载均衡监听器ID，可通过 DescribeForwardLBListeners 接口查询。|
|listenerName|否|String|应用型负载均衡监听器名称。|
|SSLMode|否|String|HTTPS协议监听器的认证类型, unidirectional:单向认证，mutual:双向认证。|
|certId|否|String|HTTPS协议监听器新的服务端证书ID。|
|certCaId|否|String|HTTPS协议监听器新的客户端证书ID。|
|certCaContent|否|String|HTTPS协议监听器新的客户端证书内容。|
|certCaName|否|String|HTTPS协议监听器新的客户端证书名称。|
|certContent|否|String|HTTPS协议监听器新的服务端证书内容。|
|certKey|否|String|HTTPS协议监听器新的服务端证书的密钥。|
|certName|否|String|HTTPS协议监听器新的服务端证书的名称。|

## 3. 返回参数
 
 
|参数名称|类型|描述|
|-------|---|---------------|
|code|Int|公共错误码, 0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/doc/api/244/1530)。|
|message|String|模块错误信息描述，与接口相关。|
|codeDesc|String|英文错误码，成功返回 Success，失败有相应的英文说明。|
|requestId|Int|请求任务ID，可根据[DescribeLoadBalancersTaskResult](/doc/api/244/4007)接口查询操作状态。|

## 4. 示例
 
输入
```
https://lb.api.qcloud.com/v2/index.php?Action=ModifyForwardLBSeventhListener
&<公共请求参数>
&loadBalancerId=lb-ltkip4do
&listenerId=lbl-6hkiqc6c
&SSLMode=unidirectional
```
输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 18642
}

```


