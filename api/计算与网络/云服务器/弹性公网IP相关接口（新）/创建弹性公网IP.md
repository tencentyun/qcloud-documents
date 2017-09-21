## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[创建弹性公网IP](https://www.qcloud.com/document/api/213/1381)。

本接口 (AllocateAddresses) 用于申请[弹性公网IP](https://www.qcloud.com/document/product/213/1941)。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

* EIP是专为动态云计算设计的静态IP地址。借助EIP，您可以快速将EIP重新映射到您的另一个实例上，从而屏蔽实例故障。
您的EIP与腾讯云账户相关联，而不是与某个实例相关联，而且在您选择显式释放该地址，或欠费超过7天之前，它会一直与您的腾讯云账户保持关联。
* 平台对用户每地域能申请的EIP最大配额有所限制，可参见[EIP产品简介](https://www.qcloud.com/document/product/213/5733)，上述配额可通过 [DescribeAddressQuota](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) API 获取。


## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|AddressCount | Integer| 否| 申请弹性公网IP数量。取值范围：[1，5]，默认值为1。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| AddressSet | array of Strings | 申请到的弹性公网IP ID列表 |

## 4. 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](https://www.qcloud.com/document/api/213/10146)。

| 错误码 | 描述 |
|---------|---------|
|AddressQuotaLimitExceeded|账户配额不足，每个腾讯云账户每个地域下最多可创建 20 个弹性公网 IP。|
|AddressQuotaLimitExceeded.DailyAllocate|申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数*2 次。|

## 5. 示例代码

#### 请求参数

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=AllocateAddresses
&Version=2017-03-12
&AddressCount=1
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
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