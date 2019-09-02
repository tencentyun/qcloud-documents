>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DescribeInstanceTypeConfigs) 用于查询实例机型配置。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 可以根据`zone`、`instance-family`来查询实例机型配置。过滤条件详见过滤器`Filter`。
* 如果参数为空，返回指定地域的所有实例机型配置。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|Filters.N|array of [Filter](/document/api/213/9451#filter) objects| 否| 过滤条件，详见下表：实例过滤条件表。每次请求的`Filters`的上限为10，`Filter.Values`的上限为1。|

实例过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| zone| String| 否| （过滤条件）按照[可用区](/document/product/213/9452#zone)过滤。|
| instance-family| String| 否| （过滤条件）按照实例机型系列过滤。实例机型系列形如：`S1`、`I1`、`M1`等。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
|InstanceTypeConfigSet|array of [InstanceTypeConfig](/document/api/213/9451#instancetypeconfig) objects| 实例机型配置列表。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidFilter|[指定的`Filter`不被支持。](/document/api/213/9451#filter)|
|InvalidFilterValue.LimitExceeded|[`Filter`参数值数量超过限制。](/document/api/213/9451#filter)|
|InvalidZone.MismatchRegion|指定的`zone`不存在。|
|InternalServerError|内部服务错误。|


## 5. 示例

输入

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceTypeConfigs
&Version=2017-03-12
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.1=I1
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出

<pre>
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM4",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 4
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM8",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 8
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM16",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 16
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.LARGE8",
                "CPU": 4,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 8
            },
			......
        ],
        "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
    }
}
</pre>
