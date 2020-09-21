>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (ModifyAddressAttribute) 用于修改 [弹性公网 IP](https://cloud.tencent.com/document/product/213/5733)（简称 EIP）的名称。
接口请求域名：eip.api.qcloud.com

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/11650) 页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
|AddressId | String| 是|标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。|
|AddressName | String| 是|修改后的 EIP 名称。长度上限为20个字符。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|InvalidAddressId.NotFound|指定的 EIP 不存在。|
|InvalidParameterValue.TooLong| EIP 设置的名称过长， EIP 的名称不应超过20个字符。|
|InvalidParameterValue|参数取值不合法|



## 5. 示例代码

#### 请求参数
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=ModifyAddressAttribute
&Version=2017-03-12
&AddressId=eip-p2x6wxc0
&AddressName=test_eip
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
