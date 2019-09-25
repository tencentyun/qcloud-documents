>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (InquiryPriceResizeInstanceDisks) 用于扩容实例的数据盘询价。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 目前只支持扩容随实例购买的数据盘询价，且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。
* 目前不支持[CDH](/document/product/416)实例使用该接口扩容数据盘询价。
* 仅支持包年包月实例随机器购买的数据盘。
* 目前只支持扩容一块数据盘询价。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 名称      |    类型 |  是否必选 | 描述|
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|InstanceId|String|是|待操作的实例ID。可通过[`DescribeInstances`](/document/api/213/9388)接口返回值中的`InstanceId`获取。|
|DataDisks.N|array of [DataDisk](/document/api/213/9451#datadisk) objects|是|待扩容的数据盘配置信息。只支持扩容随实例购买的数据盘，且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考硬盘产品简介。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。|
|ForceStop| Boolean| 否 |是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|Price|[Price](/document/api/213/9451#price)|该参数表示磁盘扩容成对应配置的价格。|
|RequestId|String| 唯一请求ID。每次请求都会返回一个唯一的requestId，当客户调用接口失败找后台研发人员处理时需提供该requestId具体值。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidInstanceId.NotFound|无效实例`ID`。指定的实例`ID`不存在。|
|InvalidInstanceId.Malformed|无效实例`ID`。指定的实例`ID`格式错误。例如`ID`长度错误`ins-1122`。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidInstance.NotSupported|实例不支持该操作。|
|InvalidAccount.InsufficientBalance|账户余额不足。|
|InvalidAccount.UnpaidOrder|账户有未支付订单。|
|InternalServerError|操作内部错误。|


## 5. 示例

### 示例1

> **包年包月实例扩容磁盘询价：**<br>


#### 请求参数
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResizeInstanceDisks
&Version=2017-03-12
&InstanceId=ins-r8hr2upy
&DataDisks.0.DiskSize=100
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "15.78",
                "DiscountPrice": "15.78"
            }
        },
        "RequestId": "0b30b426-c4fa-4f48-819b-7dd5529f7e05"
    }
}
</pre>

### 示例2

> **按量付费实例扩容磁盘询价：**<br>


#### 请求参数
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResizeInstanceDisks
&InstanceId=ins-fd8spnmq
&DataDisks.0.DiskSize=100
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

#### 返回参数
<pre>
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.46,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "d63b4f53-335b-49fb-9aa1-1716bb9276f6"
    }
}
</pre>
