## 1. 接口描述

注：本接口为改版后的 API 接口。如需了解旧接口相关信息，请参考：[查询弹性公网IP列表](/document/api/213/1379)。


本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](/document/product/213/1941)（简称 EIP）的详细信息。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version | String | 是 | 表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
| AddressIds | array of String | 是 | 标识 EIP 的唯一 ID 列表。|
| Filters.N | array of [Filter](/document/api/213/9451#filter) objects | 否 | 过滤条件，详见下表： EIP 过滤条件表。每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。|
| Offset| Integer| 否| 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](/document/api/213/568)中的相关小节。|
| Limit| Integer| 否| 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/api/213/568)中的相关小节。|


EIP 过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| address-id | String| 否| （过滤条件）按照 EIP 的唯一 ID 过滤。|
| address-name | String | 否| （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。|
| address-ip| String| 否| （过滤条件）按照 EIP 的 IP 地址过滤。|
| address-status| String| 否| （过滤条件）按照 EIP 的状态过滤。取值范围：详见 [EIP 状态列表](/document/api/213/9452#eip_status)。|
| instance-id| String| 否| （过滤条件）按照 EIP 绑定的实例 ID 过滤。|
| private-ip-address| String| 否|（过滤条件）按照 EIP 绑定的内网 IP 过滤。|
| network-interface-id| String| 否|（过滤条件）按照 EIP 绑定的网卡 ID 过滤。|
| is-arrears| String| 否|（过滤条件）按照 EIP 是否欠费进行过滤。取值范围：<br><li>TRUE：EIP 处于欠费状态<br><li>FALSE：EIP 费用状态正常。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| TotalCount| Integer | 符合条件的 EIP 数量。|
| AddressSet| array of [Address](/document/api/213/9451#address) objects | EIP 详细信息列表。|


## 4. 示例代码

#### 请求参数
```
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&AddressIds.0=eip-hxlqja90
&<<a href="/doc/api/229/6976">公共请求参数</a>>
```

#### 返回参数
```
{
  "Response": {
    "TotalCount": 1,
    "AddressSet": [
      {
        "AddressId": "eip-hxlqja90",
        "AddressName": "test",
        "AddressIp": "123.121.34.33",
        "AddressStatus": "BINDED",
        "InstanceId": "ins-m2j0thu6",
        "NetworkInterfaceId": null,
        "PrivateAddressIp": null,
        "IsArrears": False,
        "IsBlocked": False,
        "CreatedTime": "2017-09-12T07:52:00Z"
      }
    ]
  }
}
```
