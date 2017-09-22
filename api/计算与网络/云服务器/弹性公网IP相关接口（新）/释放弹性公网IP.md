## 1. 接口描述

注：本接口为改版后的 API 接口。如需了解旧接口相关信息，请参考：[释放弹性公网IP](/document/api/213/1380)。

本接口 (ReleaseAddresses) 用于释放[弹性公网IP](/document/product/213/1941)（简称 EIP）。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
| AddressIds | array of String| 是| 标识 EIP 的唯一 ID 列表。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 示例代码

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
