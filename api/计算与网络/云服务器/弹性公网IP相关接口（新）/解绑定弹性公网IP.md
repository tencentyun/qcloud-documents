## 1. 接口描述

注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[解绑定弹性公网IP](https://www.qcloud.com/document/api/213/1376)。


本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://www.qcloud.com/document/product/213/1941)。

接口请求域名：<font style="color:red">eip.api.qcloud.com</font>

* 只有状态为 BIND 和 BIND_ENI 的弹性公网IP才能进行解绑定操作。
* 弹性公网IP如果被封堵，则不能被解绑定。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/document/api/213/6976)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
| Version |String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| AddressId | String| 是| 标识弹性公网IP的唯一ID。|
| ReallocateNormalPublicIp | String| 否| 表示解绑弹性公网IP之后是否分配普通公网IP。取值范围：<br><li>TRUE：表示解绑弹性公网IP之后分配普通公网IP。<br><li>FALSE：表示解绑弹性公网IP之后不分配普通公网IP。<br>默认取值：FALSE。<br><br>只有满足以下条件时才能指定该参数：<br><li> 只有在解绑主网卡的主内网IP上的弹性公网IP时才能指定该参数。<br><li>解绑弹性公网IP后重新分配普通公网IP操作一个账号每天最多操作10次；详情可以通过查询弹性公网IP配额接口获取。 |


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
|InvalidAddressIdStatus.NotPermit|指定弹性公网IP的状态不能允许进行绑定操作。只有弹性公网IP的状态处于 BIND 或 BIND_ENI 状态时才能进行绑定操作。|
|InvalidInstanceId.NotFound|指定实例ID不存在。|
|InvalidInstance.NotSupported|指定实例ID的当前状态不能镜像绑定弹性公网IP操作。|
|InvalidParameter|参数取值不合法。|
|AddressQuotaLimitExceeded.DailyAllocate| 重新分配普通公网IP配额已经到达当日配额上线。详情可以通过查询弹性公网IP配额接口获取。|


## 5. 示例代码


### 示例1

> **解绑弹性公网IP：**<br>


#### 请求参数
```
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
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

> **解绑弹性公网IP同时在解绑之后分配普通公网IP：**<br>
> 只有在该弹性公网IP绑定在主网卡的主内网IP上时才支持。


#### 请求参数
```
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &ReallocateNormalPublicIp=TRUE
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