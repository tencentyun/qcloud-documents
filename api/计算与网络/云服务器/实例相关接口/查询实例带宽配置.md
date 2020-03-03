>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DescribeInstanceInternetBandwidthConfigs) 用于查询实例带宽配置。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 只支持查询`BANDWIDTH_PREPAID`计费模式的带宽配置。
* 接口返回实例的所有带宽配置信息（包含历史的带宽配置信息）。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型  | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceId| String| 是| 待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388)接口返回值中的`InstanceId`获取。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
 |InternetBandwidthConfigSet|array of [InternetBandwidthConfig](/document/api/213/9451#internetbandwidthconfig) objects| 带宽配置信息列表。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InternalServerError|内部服务错误。|


## 5. 示例

输入
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceInternetBandwidthConfigs
&Version=2017-03-12
&InstanceId=ins-6lafsaz0
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出
<pre>
{
    "Response": {
        "InternetBandwidthConfigSet": [
            {
                "StartTime": "2017-03-12T16:00:00Z",
                "EndTime": "2017-04-12T16:00:00Z",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 50,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                }
            }
        ],
        "RequestId": "314161cd-ee40-4c37-921e-b10c4ed5607c"
    }
}
</pre>
