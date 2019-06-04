>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (InquiryPriceRenewInstances) 用于续费包年包月实例询价。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


* 本接口仅支持查询包年包月实例的续费价格。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceIds.N| array of Strings|是 |一个或多个待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。|
|InstanceChargePrepaid|[InstanceChargePrepaid](/document/api/213/9451#instancechargeprepaid) object| 是 |预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|Price|[Price](/document/api/213/9451#price) object|该参数表示对应配置实例的价格。|
|RequestId|String| 唯一请求ID。每次请求都会返回一个唯一的requestId，当客户调用接口失败找后台研发人员处理时需提供该requestId具体值。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidPeriod|无效时长。目前只支持时长：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]，单位：月。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InvalidAccount.InsufficientBalance|账户余额不足。|
|InvalidAccount.UnpaidOrder|账户有未支付订单。|
|InternalServerError|内部服务错误。|


## 5. 示例

### 示例1

> **包年包月实例续费询价：**<br>

#### 请求参数
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceRenewInstances
&Version=2017-03-12
&InstanceIds.1=ins-2zvpghhc
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "120.00",
                "DiscountPrice": "1.20"
            }
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
</pre>
