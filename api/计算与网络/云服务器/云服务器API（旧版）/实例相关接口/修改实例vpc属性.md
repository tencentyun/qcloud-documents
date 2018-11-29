## 1. 接口描述

本接口(UpdateInstanceVpcConfig)用于修改实例vpc属性，如私有网络ip。
 
接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


* 此操作默认会关闭实例，完成后再启动。
* 不支持跨vpcId操作。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 名称      |  是否必选|    类型  | 描述|
|---------|---------|---------|---------|
|instanceId |是|String|待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API返回值中的 unInstanceId 获取|
|vpcId | 是 |String| 私有网络ID。|
|subnetId| 是|String|私有网络子网ID。|
|privateIpAddresses.n| 是|array of Strings|私有子网ip数组，目前只支持一个ip。|
|autoPowerOffFlag| 否 |int| 1表示自动关机，0表示不自动关机，默认为1|

## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|


## 4. 错误码
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见[CVM错误码](/document/product/213/6982)页面。

|错误码|描述|
|---|---|
|InvalidParameter.InvalidIpFormat|ip格式不正确|
|InvalidParameter.NotSupportReservedIp|保留ip不可使用|
|InvalidParameter.IpNotInCidrRange|ip不在子网内|
|InvalidParameter.IpInUse|ip已经被使用|

## 5. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=UpdateInstanceVpcConfig
  &instanceId=qcvm12345
  &vpcId=gz_vpc_1
  &subnetId=gz_subnet_1
  &privateIpAddresses.0=10.0.0.20
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
  {
      "code" : 0,
      "message" : ""
  }

```