>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (InquiryPriceResetInstancesType) 用于调整实例的机型询价。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 目前只支持[系统盘类型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口进行调整机型询价。
* 目前不支持[CDH](/document/product/416)实例使用该接口调整机型询价。
* 目前不支持跨机型系统来调整机型，即使用该接口时指定的`InstanceType`和实例原来的机型需要属于同一系列。
* 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](/document/product/378/4397)接口查询账户余额。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceIds.N| array of Strings|是 |一个或多个待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为1。|
|InstanceType|String|是|实例机型。不同实例机型指定了不同的资源规格，具体取值可参见附表实例资源规格对照表，也可以调用查询实例资源规格列表接口获得最新的规格表。|
|ForceStop| Boolean| 否 |是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|Price|[Price](/document/api/213/9451#price) object|该参数表示调整成对应机型实例的价格。|
|RequestId|String| 唯一请求ID。每次请求都会返回一个唯一的requestId，当客户调用接口失败找后台研发人员处理时需提供该requestId具体值。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。

| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidParameter| 无效参数。参数不合要求或者参数不被支持等。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InvalidPermission|账户不支持该操作。|
|InvalidAccount.InsufficientBalance|账户余额不足。|
|InvalidAccount.UnpaidOrder|账户有未支付订单。|
|InternalServerError|内部服务错误。|


## 5. 示例

### 示例1

> **包年包月实例调整配置询价：**<br>


#### 请求参数
```
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstancesType
&Version=2017-03-12
&InstanceIds.1=ins-2zvpghhc
&InstanceType=S1.SMALL4
&<<a href="/document/api/213/11650">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "67.33",
                "DiscountPrice": "67.33"
            }
        },
        "RequestId": "d9f36a23-7bc4-4f02-99c5-00b4a77431df"
    }
}
```

### 示例2

> **按量付费实例调整配置询价：**<br>


#### 请求参数
```
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstancesType
&InstanceId=ins-fd8spnmq
InternetAccessible.InternetMaxBandwidthOut=20
&DryRun=FALSE
&<<a href="/document/api/213/11650">公共请求参数</a>>
```

#### 返回参数
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.66,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "56d68b92-7004-4716-b3bf-3c2c231035c9"
    }
}
```
