>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口（UpdateInstanceVpcConfig）用于修改实例 VPC 属性，如私有网络 IP。

接口请求域名：cvm.api.qcloud.com
* 此操作默认会关闭实例，完成后再启动。
* 不支持跨 VpcId 操作。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/11650) 页面。

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|Version|String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
|InstanceId |String|是|待操作的实例 ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/831) 接口返回值中的 `InstanceId` 获取。|
|VirtualPrivateCloud|[VirtualPrivateCloud](https://cloud.tencent.com/document/api/213/9451#virtualprivatecloud) object| 是 |私有网络相关信息配置。通过该参数指定私有网络的 ID，子网 ID，私有网络 IP 等信息。|
|ForceStop| Boolean| 否 |是否对运行中的实例选择强制关机。默认为 TRUE。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId|String| 唯一请求 ID。每次请求都会返回一个唯一的 requestId，当客户调用接口失败找后台研发人员处理时需提供该 requestId 具体值。|


### 接口执行正常返回参数示例
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```
## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|InvalidParameterValue|无效参数值。参数值格式错误或者参数值不被支持等。|
|VpcAddrNotInSubNet|私有网络 IP 不在子网内。|
|VpcIpIsUsed|私有网络 IP 已经被使用。|
|VpcIdNotMatch|VpcId 与实例所在 VpcId 不匹配。|
|EniNotAllowedChangeSubnet|弹性网卡不允许跨子网操作。|
