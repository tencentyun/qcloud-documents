>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>。

* 为了您的数据安全，请关闭实例后创建镜像。
* 单个帐号在每个地域最多支持创建10个自定义镜像。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| InstanceId |  String |是 | 用于制作镜像的实例ID 。实例ID可以通过以下方式获取:<br><li>通过[DescribeInstances](/document/api/213/9388)接口返回的`InstanceId`获取。<br><li>通过[实例控制台](https://console.cloud.tencent.com/cvm/index)获取。
| ImageName |  String |是 | 镜像名称；需要满足下列要求：<br><li>不得超过20个字符。<br><li>镜像名称不得重复。
| ImageDescription |  String |否 | 镜像描述；需要满足下列要求：<br><li>不得超过60个字符。<br>不指定该参数时镜像描述为空。
| Sysprep |  Boolean |否 | 创建镜像时是否启用 SysPrep( Windows only) 。其默认值为 `False`。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 |  描述 |
|---------|---------|
|InvalidParameter.ValueTooLarge | 参数长度超过限制。|
|InvalidImageName.Duplicate |镜像名称与原有镜像重复。|
|MutexOperation.TaskRunning|同样的任务正在运行。|
|InvalidInstanceId.NotFound| 没有找到相应实例。|
|ImageQuotaLimitExceeded| 镜像配额超过了限制。|
|InvalidInstance.NotSupported| 不被支持的实例。|

## 5. 示例 

请求参数
<pre>
https://image.api.qcloud.com/v2/index.php?Action=CreateImage
&Version=2017-03-12
&InstanceId=ins-6pb6lrmy
&<<a href="/doc/api/229/6976">公共请求参数</a>>
</pre>

返回参数
<pre>
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>


