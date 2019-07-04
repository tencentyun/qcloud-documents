>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](/document/product/213/1941)（简称 EIP）的详细信息。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

* 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version | String | 是 | 表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
| AddressIds.N | array of String | 否 | 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`AddressIds`和`Filters`。|
| Filters.N | array of [Filter](/document/api/213/9451#filter) objects | 否 | 过滤条件，详见下表： EIP 过滤条件表。每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。|
| Offset| Integer| 否| 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](/document/api/213/11646)中的相关小节。|
| Limit| Integer| 否| 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/api/213/11646)中的相关小节。|


EIP 过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| address-id | String| 否| （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：`eip-11112222`。|
| address-name | String | 否| （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。|
| address-ip| String| 否| （过滤条件）按照 EIP 的 IP 地址过滤。|
| address-status| String| 否| （过滤条件）按照 EIP 的状态过滤。取值范围：详见 [EIP 状态列表](/document/api/213/9452#eip_state)。|
| instance-id| String| 否| （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：`ins-11112222`。|
| private-ip-address| String| 否|（过滤条件）按照 EIP 绑定的内网 IP 过滤。|
| network-interface-id| String| 否|（过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：`eni-11112222`。|
| is-arrears| String| 否|（过滤条件）按照 EIP 是否欠费进行过滤。取值范围：<br><li>TRUE：EIP 处于欠费状态<br><li>FALSE：EIP 费用状态正常。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String|唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| TotalCount| Integer | 符合条件的 EIP 数量。|
| AddressSet| array of [Address](/document/api/213/9451#address) objects | EIP 详细信息列表。|


## 4. 示例代码
### 示例1

> **使用`AddressIds`查询 EIP：**<br>

#### 请求参数
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&Version=2017-03-12
&AddressIds.1=eip-hxlqja90
&<<a href="/document/api/213/11650">公共请求参数</a>>
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
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
</pre>

### 示例2

> **使用`Filters`查询 EIP：**<br>

#### 请求参数
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&Version=2017-03-12
&Filters.1.Name=address-id
&Filters.1.Values.1=eip-hxlqja90
&<<a href="/document/api/213/11650">公共请求参数</a>>
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
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
</pre>
