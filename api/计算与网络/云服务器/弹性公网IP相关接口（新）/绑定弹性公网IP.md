## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[绑定弹性公网IP](https://www.qcloud.com/document/api/213/1377)。


本接口 (AssociateAddress) 用于将[弹性公网IP](https://www.qcloud.com/document/product/213/1941)绑定到实例或弹性网卡的指定内网IP上。
 
接口请求域名：<font style="color:red">eip.api.qcloud.com</font>


* 将弹性公网IP绑定到实例上，其本质是将弹性公网IP绑定到实例的主网卡的主内网IP上。
* 将弹性公网IP绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网IP自动解绑并释放。
* 如果指定网卡的内网IP已经绑定了弹性公网IP，则必须先解绑该弹性公网IP，才能再绑定新的。
* 弹性公网IP如果欠费或被封堵，则不能被绑定。
* 只有状态为 UNBIND 和 BIND_ENI 的弹性公网IP才能够被绑定。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/document/api/213/6976)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| AddressId | String| 是| 标识弹性公网IP的唯一ID。|
| InstanceId| String| 否| 要绑定的实例ID。可通过 [DescribeInstances](https://www.qcloud.com/document/api/213/9389) API返回值中的`InstanceId`获取。
| NetworkInterfaceId | String| 否| 要绑定的弹性网卡ID。 `NetworkInterfaceId` 与 `InstanceId` 不可同时指定。|
| PrivateIpAddress | String| 否| 要绑定的内网IP。如果指定了 `NetworkInterfaceId` 则也必须指定 `PrivateIpAddress` ，表示将弹性公网IP绑定到指定弹性网卡的指定内网IP上。同时要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一个内网IP。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId |String | 唯一请求ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](https://www.qcloud.com/document/api/213/10146)。

| 错误码 | 描述 |
|---------|---------|
|InvalidAddressId.NotFound|指定的弹性公网IP不存在。|
|InvalidAddressId.Blocked|指定弹性公网IP处于被封堵状态。当弹性公网IP处于封堵状态的时候是不能够镜像绑定操作的，需要先进行解封。|
|InvalidAddressIdState.InArrears|指定弹性公网IP处于欠费状态。|
|InvalidAddressIdStatus.NotPermit|指定弹性公网IP的状态不能允许进行绑定操作。只有弹性公网IP的状态处于 UNBIND 或 BIND_ENI 状态时才能进行绑定操作。|
|InvalidInstanceId.NotFound|指定实例ID不存在。|
|InvalidInstanceId.AlreadyBindEip|指定实例ID已经绑定了弹性公网IP。需先解绑当前的弹性公网IP才能再次进行绑定操作。|
|InvalidInstance.NotSupported|指定实例ID的当前状态不能进行绑定弹性公网IP操作。|
|InvalidNetworkInterfaceId.NotFound|指定 `NetworkInterfaceId` 不存在或指定的 `PrivateIpAddress` 不在 `NetworkInterfaceId` 上。|
|InvalidPrivateIpAddress.AlreadyBindEip|指定弹性网卡的指定内网IP已经绑定了弹性公网IP，不能重复绑定。|
|InvalidParameterConflict|指定的两个参数冲突，不能同时存在。弹性公网IP只能绑定在实例上或指定网卡的指定内网IP上。|
|MissingParameter|参数依赖缺少。`NetworkInterfaceId` 和 `PrivateIpAddress` 必须同时指定，表示将弹性公网IP绑定到指定弹性网卡的指定内网IP上|
|MissingResourceId|绑定的实体缺失。`InstanceId` 或 `NetworkInterfaceId`、 `PrivateIpAddress` 必须指定一个。|



## 5. 示例代码


### 示例1

> **绑定弹性公网IP到实例ID上：**<br>


#### 请求参数
```
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &InstanceId=ins-1bmpb9tu
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


### 示例2

> **绑定弹性公网IP到指定网卡的指定内网IP上：**<br>


#### 请求参数
```
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &NetworkInterfaceId=eni-8x55qvrh
  &PrivateIpAddress=10.0.0.2
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```
