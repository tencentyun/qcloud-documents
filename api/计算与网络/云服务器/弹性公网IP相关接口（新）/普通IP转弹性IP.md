## 1. 接口描述

注：本接口为改版后的 API 接口。如需了解旧接口相关信息，请参考：[普通IP转弹性公网IP](/document/api/213/1374)。

本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](/document/product/213/1941)（简称 EIP）。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


* 平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](/document/api/213/1378) 接口获取。


## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
|InstanceId|String|是|待操作有普通公网 IP 的服务器实例 ID，可通过 [DescribeInstances](/document/api/213/9388) 接口返回字段中的`InstanceId`获取。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码
| 错误码 | 描述 |
|---------|---------|
|AddressQuotaLimitExceeded|账户配额不足，每个腾讯云账户每个地域下最多可创建 20 个 EIP。|
|AddressQuotaLimitExceeded.DailyAllocate|申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数*2 次。|
|InvalidInstanceId.NotFound|实例 ID 不存在。|
|InvalidInstanceState|指定实例当前状态不能进行普通公网 IP 转换 EIP 操作。|
|InvalidInstance.NotSupported|指定实例不支持将普通公网 IP 转换为 EIP。|

## 5. 示例代码

#### 请求参数

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=TransformAddress
&InstanceId=ins-3ea0qeu6
&<<a href="/doc/api/229/6976">公共请求参数</a>>
</pre>

#### 返回参数

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
