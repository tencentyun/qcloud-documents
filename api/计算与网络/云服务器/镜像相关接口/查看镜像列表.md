>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口(DescribeImages) 用于查看镜像列表。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>。

*可以通过指定镜像ID来查询指定镜像的详细信息，或通过设定过滤器来查询满足过滤条件的镜像的详细信息。
*指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个镜像信息。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| ImageIds.N |  array of Strings |否 | 镜像ID列表 。镜像ID如：`img-gvbnzy6f`。array型参数的格式可以参考[API简介](/document/api/213/11646)。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](/document/api/213/9418)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。|
| Filters.N |array of [Filter](/document/api/213/9451#filter) objects|否 | 过滤条件，详见下表-镜像过滤条件表。其中Filters的上限为10，Filters.Values的上限为5。 注意：不可以同时指定ImageIds和Filters。可选值包括 `image-id`, `image-type`。|
| Offset |  Integer |否 | 偏移量，默认为0。关于Offset详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。|
| Limit |  Integer |否 | 数量限制，默认为20，最大值为100。关于Limit详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。|

镜像过滤条件表

|参数名称|类型|描述|
|---------|--------|---------|
|image-id|String|(过滤条件)，按镜像ID过滤，形如`img-gvbnzy6f`。|
|image-type|String|(过滤条件)，按[镜像类型](/document/api/213/9452#image_type)过滤。|
|image-name|String|(过滤条件)，按镜像名称过滤。|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|
| ImageSet |array of [Images](/document/api/213/9451#image)。| 一个关于镜像详细信息的结构体，主要包括镜像的主要状态与属性。|
| TotalCount |  Integer | 符合要求的镜像数量。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 |  描述 |
|---------|---------|
|InvalidFilter | 无效的过滤器。|
|InvalidParameter.InvalidParameterCoexistImageIdsFilters|不能同时指定ImageIds和Filters。|
|InvalidParameterValue.InvalidParameterValueLimit|参数值错误。|

## 5. 示例
示例1.
>**按镜像ID查询镜像**：<br>
> 已经知道镜像ID，查询镜像相关信息

请求参数
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DescribeImages
&Version=2017-03-12
&ImageIds.0=img-pmqg1cw7
&<<a href="/doc/api/229/6976">公共请求参数</a>>
</pre>

返回参数
<pre>
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "CentOS 6.6 32位",
                "ImageDescription": "CentOS 6.6 32位",
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestID": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
</pre>

示例2.
>**按镜像类型查询镜像**：<br>
> 查询账户下所有私有镜像。

请求参数
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DescribeImages
&Version=2017-03-12
&Filters.1.Name=image-type
&Filters.1.Values.1=PRIVATE_IMAGE
&<<a href="/doc/api/229/6976">公共请求参数</a>>
</pre>

返回参数
<pre>
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "CentOS 6.6 32位",
                "ImageDescription": "CentOS 6.6 32位",
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestID": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
</pre>
