## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[普通IP转弹性公网IP](https://www.qcloud.com/document/api/213/1374)。

本接口 (TransformAddress) 用于将实例普通IP转换为弹性公网IP。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

>注：
平台对用户每地域每日解绑EIP重新分配普通公网IP次数有所限制（可参见<a href="/doc/product/213/1941" title="/doc/product/213/1941">EIP产品简介</a>）。上述配额可通过 <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D" title="DescribeAddressQuota">DescribeAddressQuota</a>接口获取。


## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|InstanceId|String|是|待操作有普通公网IP的服务器实例ID，可通过[DescribeInstances](https://www.qcloud.com/document/api/213/9388)接口返回字段中的InstanceId获取。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
 

## 4. 错误码
| 错误码 | 描述 |
|---------|---------|
|AddressQuotaLimitExceeded|账户配额不足，每个腾讯云账户每个地域下最多可创建 20 个弹性公网 IP。|
|AddressQuotaLimitExceeded.DailyAllocate|申购次数不足，每个腾讯云账户每个地域每天申购次数为配额数*2 次。|
|InvalidInstanceId.NotFound|实例ID不存在。|
|InvalidInstanceState|实例处于无效的状态。|
|InvalidInstance.NotSupported|该实例不支持将普通公网IP转换为弹性公网IP。|

## 5. 示例代码

#### 请求参数

<pre>
https://eip.api.qcloud.com/v2/index.php?Action=TransformAddress
&InstanceId=ins-3ea0qeu6
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
</pre>

#### 返回参数

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre> 
 
