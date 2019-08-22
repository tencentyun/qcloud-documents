>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (AllocateAddresses) 用于申请一个或多个[弹性公网IP](/document/product/213/1941)（简称 EIP）。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

* EIP 是专为动态云计算设计的静态 IP 地址。借助 EIP，您可以快速将 EIP 重新映射到您的另一个实例上，从而屏蔽实例故障。
* 您的 EIP 与腾讯云账户相关联，而不是与某个实例相关联。在您选择显式释放该地址，或欠费超过七天之前，它会一直与您的腾讯云账户保持关联。
* 平台对用户每地域能申请的 EIP 最大配额有所限制，可参见 [EIP 产品简介](/document/product/213/5733)，上述配额可通过 [DescribeAddressQuota](/document/api/213/1378) 接口获取。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
|AddressCount | Integer| 否| 申请 EIP 数量。取值范围：[1，5]，默认值为1。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| AddressSet | array of Strings | 申请到的 EIP 的唯一 ID 列表。 |

## 4. 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|AddressQuotaLimitExceeded|账户配额不足，每个腾讯云账户每个地域下最多可创建 20 个 EIP。|
|AddressQuotaLimitExceeded.DailyAllocate|申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数*2 次。|

## 5. 示例代码

#### 请求参数

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=AllocateAddresses
&Version=2017-03-12
&AddressCount=1
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "AddressSet": [
            "eip-m44ku5d2"
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
