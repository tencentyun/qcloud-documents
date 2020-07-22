>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DescribeKeyPairs) 用于查询密钥对信息。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* [密钥对](/document/product/213/6092)是通过一种算法生成的一对密钥，在生成的密钥对中，一个向外界公开，称为公钥；另一个用户自己保留，称为私钥。密钥对的公钥内容可以通过这个接口查询，但私钥内容系统不保留。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| KeyIds.N  | array of Strings | 否 | 密钥对ID，密钥对ID形如：`skey-11112222`（此接口支持同时传入多个ID进行过滤。此参数的具体格式可参考 API [简介](/document/api/213/11646)的 `id.N` 一节）。参数不支持同时指定 `KeyIds` 和 `Filters`。<br> 密钥对ID可以通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询。|
| Filters.N| array of [Filter](/document/api/213/9451#filter) objects| 否| 过滤条件，详见密钥对过滤条件表。参数不支持同时指定 `KeyIds` 和 `Filters`。|
| Offset| Integer| 否| 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](/document/api/213/11646#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)中的相关小节。|
| Limit| Integer| 否| 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)中的相关小节。|

密钥对过滤条件表

| 参数名称| 类型| 是否必选| 描述|
|---------|---------|---------|---------|
| project-id| Integer| 否| （过滤条件）按照项目ID过滤。<br><br>可以通过以下方式获取项目ID：<br><li>通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID。<br><li>通过调用接口 [DescribeProject](/document/api/378/4400) ，取返回信息中的`projectId `获取项目ID。|
| key-name| String| 否| （过滤条件）按照密钥对名称过滤。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 `ID`。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|
| TotalCount | Integer | 符合条件的密钥对数量。 |
| KeyPairSet| array of [KeyPair](/document/api/213/9451#keypair) objects| 密钥对详细信息列表。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|InvalidParameter| 无效参数。参数不合要求或者参数不被支持等。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidParameterValueLimit|参数值数量超过限制。|
|InvalidParameterValueOffset| 无效参数值。指定的 `Offset` 无效。
|InvalidFilterValue.LimitExceeded|[`Filter`](/document/api/213/9451#filter)参数值数量超过限制。|
|InvalidFilter|指定的[`Filter`](/document/api/213/9451#filter)不被支持。|
|InvalidKeyPairId.Malformed|无效密钥对ID。指定的密钥对ID格式错误，例如 `ID` 长度错误`skey-1122`。|
|InvalidKeyPair.LimitExceeded|密钥对数量超过限制。|
|InternalServerError|操作内部错误。|


## 5. 示例

输入
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeKeyPairs
&Version=2017-03-12
&Filters.1.Name=key-name
&Filters.1.Values.1=Tencent
&Offset=0
&Limit=20
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出
<pre>
{
    "Response": {
        "TotalCount": 1,
        "KeyPairSet": [
            {
                "KeyId": "skey-mv9yzyjj",
                "KeyName": "Tencent",
                "Description": "",
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
                "AssociatedInstanceIds": [
                ],
                "CreateTime": "2016-12-02T00:22:40Z"
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
