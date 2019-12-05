>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (ModifyInstancesProject) 用于修改实例所属项目。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源；将多个不同实例分属到不同项目中，后续使用 [`DescribeInstances`](/document/api/213/9388)接口查询实例，项目ID可用于过滤结果。
* 绑定负载均衡的实例不支持修改实例所属项目，请先使用[`DeregisterInstancesFromLoadBalancer`](/document/api/214/1258)接口解绑负载均衡。
* 修改实例所属项目会自动解关联实例原来关联的安全组，修改完成后可能使用[`ModifySecurityGroupsOfInstance`](/document/api/213/1367)接口关联安全组。
* 支持批量操作。每次请求批量实例的上限为100。如果批量实例存在不允许操作的实例，操作会以特定[错误码](#4.-.E9.94.99.E8.AF.AF.E7.A0.81)返回。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型  | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceIds.N| array of Strings|是|一个或多个待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
| ProjectId|Integer |是 | 项目ID。项目可以使用[AddProject](/doc/api/403/4398)接口创建。后续使用[DescribeInstances](/document/api/213/9388)接口查询实例时，项目ID可用于过滤结果。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId |String | 唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidParameterValue.LimitExceeded|参数值数量超过限制。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InternalServerError|操作内部错误。|


## 5. 示例

输入
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyInstancesProject
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&ProjectId=1045
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出
<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
