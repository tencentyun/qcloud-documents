## 1. 接口描述

本接口(UpdateInstanceVpcConfig)用于修改实例vpc属性，如私有网络ip。
 
接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


* 此操作默认会关闭实例，完成后再启动。
* 不支持跨VpcId操作。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|InstanceId |String|是|待操作的实例ID。可通过[`DescribeInstances`](https://www.qcloud.com/doc/api/229/831)接口返回值中的`InstanceId`获取。|
VirtualPrivateCloud |[ VirtualPrivateCloud object](https://www.qcloud.com/document/api/213/9451#virtualprivatecloud5)| 是 |私有网络相关信息配置。通过该参数指定私有网络的ID，子网ID，私有网络ip等信息。|
|ForceStop| Boolean| 否 |是否对运行中的实例选择强制关机。默认为TRUE。|

## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId|String| 唯一请求ID。每次请求都会返回一个唯一的requestId，当客户调用接口失败找后台研发人员处理时需提供该requestId具体值。|


### 接口执行正常返回参数示例
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```
## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见公共错误码。

| 错误码 | 描述 |
|---------|---------|
|InvalidParameterValue|无效参数值。参数值格式错误或者参数值不被支持等。|
|VpcAddrNotInSubNet|私有网络ip不在子网内。|
|VpcIpIsUsed|私有网络ip已经被使用。|
|VpcIdNotMatch|VpcId与实例所在VpcId不匹配。|
|EniNotAllowedChangeSubnet|弹性网卡不允许跨子网操作。|
