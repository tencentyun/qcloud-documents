>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为 [弹性公网 IP](https://cloud.tencent.com/document/product/213/5733)（简称 EIP）。
接口请求域名：eip.api.qcloud.com
平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/11650) 页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
|InstanceId|String|是|待操作有普通公网 IP 的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录 [控制台](https://console.cloud.tencent.com/cvm) 查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 接口返回值中的`InstanceId`获取。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|AddressQuotaLimitExceeded|账户配额不足，每个腾讯云账户每个地域下最多可创建20个 EIP。|
|AddressQuotaLimitExceeded.DailyAllocate|申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数 \* 2次。|
|InvalidInstanceId.NotFound|实例 ID 不存在。|
|InvalidInstanceState|指定实例当前状态不能进行普通公网 IP 转换 EIP 操作。|
|InvalidInstance.NotSupported|指定实例不支持将普通公网 IP 转换为 EIP。|

## 5. 示例代码

#### 请求参数

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=TransformAddress
&Version=2017-03-12
&InstanceId=ins-3ea0qeu6
&<<a href="https://cloud.tencent.com/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
