>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (ResetInstancesInternetMaxBandwidth) 用于调整实例公网带宽上限。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](/document/product/213/509)。
* 对于 `BANDWIDTH_PREPAID` 计费方式的带宽，需要输入参数 `StartTime` 和 `EndTime` ，指定调整后的带宽的生效时间段。在这种场景下目前不支持调小带宽，会涉及扣费，请确保账户余额充足。可通过 [`DescribeAccountBalance`](/document/product/378/4397) 接口查询账户余额。
* 对于 `TRAFFIC_POSTPAID_BY_HOUR` 、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽，使用该接口调整带宽上限是实时生效的，可以在带宽允许的范围内调大或者调小带宽，不支持输入参数 `StartTime` 和 `EndTime` 。
* 接口不支持调整 `BANDWIDTH_POSTPAID_BY_MONTH` 计费方式的带宽。
* 接口不支持批量调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽。
* 接口不支持批量调整混合计费方式的带宽。例如不支持同时调整 `TRAFFIC_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型  | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceIds.N| array of Strings|是 |一个或多个待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388)接口返回值中的 `InstanceId` 获取。 每次请求批量实例的上限为100。|
|InternetAccessible|[InternetAccessible](/document/api/213/9451#internetaccessible) object|是|公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持 `InternetMaxBandwidthOut` 参数。|
|StartTime| String| 否| 带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。|
|EndTime| String| 否| 带宽生效的终止时间。格式： `YYYY-MM-DD` ，例如：`2016-10-30` 。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过 [`DescribeInstances`](/document/api/213/9388)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId|String| 唯一请求ID。每次请求都会返回一个唯一的requestId，当客户调用接口失败找后台研发人员处理时需提供该requestId具体值。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidParameter| 无效参数。参数不合要求或者参数不被支持等。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidParameterValue.Range| 无效参数值。参数值取值范围不合法。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InvalidPermission|账户不支持该操作。|
|InvalidAccount.InsufficientBalance|账户余额不足。|
|InvalidAccount.UnpaidOrder|账户有未支付订单。|
|InternalServerError|内部服务错误。|


## 5. 示例

输入
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ResetInstancesInternetMaxBandwidth
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InternetAccessible.InternetMaxBandwidthOut=10
&StartTime=2017-03-15
&EndTime=2017-03-16
&DryRun=FALSE
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出
<pre>
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
</pre>
