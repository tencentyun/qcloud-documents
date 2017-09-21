## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[查询弹性公网IP列表](https://www.qcloud.com/document/api/213/1379)。


本接口 (DescribeAddresses) 用于查询弹性公网IP列表。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/document/api/213/6976)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| AddressIds | array of String| 是| 标识弹性公网IP的唯一ID列表。|
| Filters.N|[array of Filter objects](https://www.qcloud.com/document/api/213/9451#filter15)| 否| 过滤条件，详见[实例过滤条件表]()。每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。|
| Offset| Integer| 否| 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)中的相关小节。|
| Limit| Integer| 否| 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)中的相关小节。|


实例过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| address-id | String| 否| （过滤条件）按照弹性公网IP的唯一ID过滤。|
| address-name | String | 否| （过滤条件）按照弹性公网IP名称过滤。不支持模糊过滤。|
| address-ip| String| 否| （过滤条件）按照弹性公网IP的IP来过滤。|
| address-status| String| 否| （过滤条件）按照弹性公网IP的状态过滤。取值范围：详见EIP状态列表。|
| instance-id| String| 否| （过滤条件）按照弹性公网IP帮定的实例ID过滤。|
| private-ip-address| String| 否|（过滤条件）按照弹性公网IP帮定的内网IP过滤。|
| network-interface-id| String| 否|（过滤条件）按照弹性公网IP帮定的网卡ID过滤。|
| is-arrears| String| 否|（过滤条件）按照弹性公网IP是否欠费进行过滤。取值范围：<br><li>TRUE：弹性公网IP处于欠费状态<br><li>FALSE：弹性公网IP费用状态正常。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| TotalCount| Integer | 符合条件的EIP数量。|
| AddressSet| array of [Address](https://www.qcloud.com/document/api/213/9451#address) objects | EIP详细信息列表。|


## 4. 示例代码

#### 请求参数
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&AddressIds.0=eip-hxlqja90
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
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
</pre>