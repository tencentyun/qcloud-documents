>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DescribeAddressQuota) 用于查询您账户的 [弹性公网 IP](https://cloud.tencent.com/document/product/213/5733)（简称 EIP）在当前地域的配额信息。
接口请求域名：eip.api.qcloud.com


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/11650) 页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| QuotaSet | array of [Quota](https://cloud.tencent.com/document/api/213/9451#quota) objects| 账户 EIP 配额信息|




## 4. 示例代码

#### 请求参数
<pre>
  https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddressQuota
  &Version=2017-03-12
  &<<a href="https://cloud.tencent.com/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
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
</pre>
