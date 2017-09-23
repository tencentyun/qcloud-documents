## 1. 接口描述

注：本接口为改版后的 API 接口。如需了解旧接口相关信息，请参考：[查询弹性公网IP配额](/document/api/213/1378)。

本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](/document/product/213/1941)（简称 EIP）配额信息。配额详情可参见 [EIP 产品简介](/document/product/213/5733)。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


## 2. 输入参数

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| QuotaSet | array of [Quota](/document/api/213/9451#quota) objects| 账户 EIP 配额信息|




## 4. 示例代码

#### 请求参数
```
  https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddressQuota
  &<<a href="/doc/api/229/6976">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        {
            'QuotaSet': [
            {'QuotaId': 'TOTAL_EIP_QUOTA', 'QuotaCurrent': 0, 'QuotaLimit': 20},
            {'QuotaId': 'DAILY_EIP_APPLY', 'QuotaCurrent': 0, 'QuotaLimit': 40},
            {'QuotaId': 'DAILY_EIP_ASSIGN','QuotaCurrent': 0, 'QuotaLimit': 40},
             ]
        }
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```
