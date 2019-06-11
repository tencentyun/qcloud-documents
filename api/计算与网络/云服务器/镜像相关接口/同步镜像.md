>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口（SyncImages）用于将自定义镜像同步到其它地区。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>。

* 该接口每次调用只支持同步一个镜像。
* 该接口支持多个同步地域。
* 单个帐号在每个地域最多支持存在10个自定义镜像。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| ImageIds.N |  array of Strings |是 | 镜像ID列表 ，镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](/document/api/213/9418)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。<br>镜像ID必须满足限制：<br><li>镜像ID对应的镜像状态必须为`NORMAL`。<br><li>镜像大小小于50GB。<br>镜像状态请参考[镜像数据表](/document/api/213/9452#image_state)。
| DestinationRegions.N |  array of String |是 | 目的同步地域列表；必须满足限制：<br><li>不能为源地域，<br><li>必须是一个合法的Region。<br><li>暂不支持部分地域同步。<br>具体地域参数请参考[Region](/document/product/213/6091)。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 |  描述 |
|---------|---------|
|InvalidImageId.IncorrectState|镜像状态不合法。|
|InvalidImageId.NotFound| 未找到该镜像。|
|InvalidImageId.Malformed| 镜像ID格式错误。|
|InvalidImageId.TooLarge|镜像大小超过限制。|
|InvalidRegion.NotFound|未找到该区域。|
|InvalidRegion.Unavailable|该区域目前不支持同步镜像。|


## 5. 示例 

请求参数
<pre>
https://image.api.qcloud.com/v2/index.php?Action=SyncImages
&Version=2017-03-12
&ImageIds.0=img-o3ycss2p
&DestinationRegions.0=ap-guangzhou
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



