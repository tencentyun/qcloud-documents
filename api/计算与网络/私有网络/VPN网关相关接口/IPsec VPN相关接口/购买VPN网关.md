## 1. 接口描述

本接口（RunVpnGw）用于购买 VPN 网关。
接口请求域名：vpc.api.qcloud.com


## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 <a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 RunVpnGw。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| name | 是 | String | IPsec VPN 网关名称，可任意命名，但不得超过60个字符。 |
| vpcId | 是 | String | 网络 ID 或者统一 ID，建议使用统一 ID，可通过 <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> 接口查询。 |
| bandwidth | 是 | Int | 带宽，只支持：5、10、20、50、100，单位 Mb。 |
| chargeType	| 是	| String | PREPAID：预付费，即包年包月， POSTPAID_BY_HOUR：按小时后付费。 |
| chargePrepaid	| 否	| ChargePrepaidObject |	预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。|


包年包月（ChargePrepaidObject）相关参数如下：

| 名称      |   必选 |  类型  | 描述|
|---------|---------|---------|---------|
|period|是| Int| 购买实例的时长，单位：月。取值范围：1、2、3、4、5、6、7、8、9、10、11、12、24、36。 |
|isAutoRenewals|否| String | 自动续费标识。取值范围：是否开启自动续费， {1：开启自动续费, 0：不自动续费} 自动续费是指在账户余额充足的情况下，实例到期后将按月自动续费。|


 

## 3. 输出参数

| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code | Int | 错误码，0：成功，其他值：失败。 |
| message | String | 错误信息。 |
| data | Array | 返回 VPN 网关的实例 ID 列表，返回实例 ID 列表并不代表实例创建成功，可根据 DescribeVpnGw 接口查询返回的 VPN 实例的 vpnGwStatus 状态来判断是否创建成功。 |


 ## 4. 错误码表
 该接口没有业务错误码，公共错误码详见 <a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">VPC 错误码</a>。

## 5. 示例
 
输入
<pre>
  https://domain/v2/index.php?Action=CreateVpn
  &<公共请求参数>
  &name=test-name
  &bandwidth=5
  &vpcId=vpc-4gzrxtwj
  &chargePrepaid.period=1
  &chargePrepaid.isAutoRenewals=1
  &chargeType=PREPAID
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vpnGwId": "vpngw-********"
    }
}
```

