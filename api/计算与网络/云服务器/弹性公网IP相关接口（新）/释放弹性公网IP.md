## 1. 接口描述

注：本接口为改版后的 API 接口。如需了解旧接口相关信息，请参考：[释放弹性公网IP](/document/api/213/1380)。

本接口 (ReleaseAddresses) 用于释放一个或多个[弹性公网IP](/document/product/213/1941)（简称 EIP）。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

* 该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
* 只有状态为 UNBIND 的 EIP 才能进行释放操作。

## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
| AddressIds | array of String| 是| 标识 EIP 的唯一 ID 列表。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 | 描述 |
|---------|---------|
|InvalidAddressId.NotFound|指定的 EIP 不存在。|
|InvalidAddressState|指定 EIP 当前状态不允许进行释放操作。只有 EIP 的状态是 UNBIND 时才能进行释放操作。|

## 5. 示例代码

#### 请求参数
```
https://eip.api.qcloud.com/v2/index.php?Action=ReleaseAddresses
&AddressId.0=eip-gzc5rgr2
&<<a href="/doc/api/229/6976">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```
