>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (AssociateAddress) 用于将 [弹性公网IP](https://cloud.tencent.com/document/product/213/5733)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
接口请求域名：eip.api.qcloud.com
* 将 EIP 绑定到实例上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
* 将 EIP 绑定到主网卡的主内网 IP 上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。
* 如果指定网卡的内网 IP 已经绑定了 EIP，则必须先解绑该 EIP，才能再绑定新的。
* EIP 如果欠费或被封堵，则不能被绑定。
* 只有状态为 UNBIND 的 EIP 才能够被绑定。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/213/11650) 页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示 API 版本号，主要用于标识请求的不同 API 版本。 本接口第一版本可传：2017-03-12。|
| AddressId | String| 是| 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。|
| InstanceId| String| 否| 要绑定的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录 [控制台](https://console.cloud.tencent.com/cvm) 查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 接口返回值中的`InstanceId`获取。
| NetworkInterfaceId | String| 否| 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：`eni-11112222`。`NetworkInterfaceId` 与 `InstanceId` 不可同时指定。弹性网卡 ID 可通过登录 [控制台](https://console.cloud.tencent.com/vpc/eni) 查询，也可通过 [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/4814) 接口返回值中的`networkInterfaceId`获取。|
| PrivateIpAddress | String| 否| 要绑定的内网 IP。如果指定了 `NetworkInterfaceId` 则也必须指定 `PrivateIpAddress` ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一个内网 IP。指定弹性网卡的内网 IP 可通过登录 [控制台](https://console.cloud.tencent.com/vpc/eni) 查询，也可通过 [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/4814) 接口返回值中的`privateIpAddress`获取。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|RequestId |String | 唯一请求 ID。每次请求都会返回`RequestId`。当用户调用接口失败找后台研发人员处理时需提供该`RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|InvalidAddressId.NotFound|指定的 EIP 不存在。|
|InvalidAddressId.Blocked|指定 EIP 处于被封堵状态。当 EIP 处于封堵状态的时候是不能够进行绑定操作的，需要先进行解封。|
|InvalidAddressIdState.InArrears|指定 EIP 处于欠费状态。|
|InvalidAddressIdStatus.NotPermit|指定 EIP 当前状态不能进行绑定操作。只有 EIP 的状态是 UNBIND 时才能进行绑定操作。|
|InvalidInstanceId.NotFound|指定实例 ID 不存在。|
|InvalidInstanceId.AlreadyBindEip|指定实例已经绑定了 EIP。需先解绑当前的 EIP 才能再次进行绑定操作。|
|InvalidInstance.NotSupported|指定实例当前状态不能进行绑定 EIP 操作。|
|InvalidNetworkInterfaceId.NotFound|指定 `NetworkInterfaceId` 不存在或指定的 `PrivateIpAddress` 不在 `NetworkInterfaceId` 上。|
|InvalidPrivateIpAddress.AlreadyBindEip|指定弹性网卡的指定内网 IP 已经绑定了 EIP，不能重复绑定。|
|InvalidParameterConflict|指定的两个参数冲突，不能同时存在。 EIP 只能绑定在实例上或指定网卡的指定内网 IP 上。|
|MissingParameter|参数依赖缺少。`NetworkInterfaceId` 和 `PrivateIpAddress` 必须同时指定，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。|
|MissingResourceId|绑定的实体缺失。`InstanceId` 或 `NetworkInterfaceId`、 `PrivateIpAddress` 必须指定一个。|



## 5. 示例代码


### 示例1

**绑定 EIP 到实例上：**


#### 请求参数
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &InstanceId=ins-1bmpb9tu
  &<<a href="https://cloud.tencent.com/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


### 示例2

**绑定 EIP 到指定网卡的指定内网 IP 上：**


#### 请求参数
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &NetworkInterfaceId=eni-8x55qvrh
  &PrivateIpAddress=10.0.0.2
  &<<a href="https://cloud.tencent.com/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>
