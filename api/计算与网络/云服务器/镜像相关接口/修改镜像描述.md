>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口（ModifyImageAttribute）用于修改镜像属性。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>。

* 已分享的镜像无法修改属性。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| ImageId |  String |是 | 镜像ID，形如`img-gvbnzy6f`。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](/document/api/213/9418)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。|
| ImageName |  String |否 | 设置新的镜像名称；必须满足下列限制：<br> <li> 不得超过20个字符。<br> <li> 镜像名称不能与已有镜像重复。|
| ImageDescription |  String |否 | 设置新的镜像描述；必须满足下列限制：<br> <li> 不得超过60个字符。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 |  描述 |
|---------|---------|
|InvalidImageId.IncorrectState|镜像状态不合法。|
|InvalidImageId.NotFound|未找到该镜像。|
|InvalidImageId.Malformed|设置的镜像名称不合法。|
|InvalidImageName.Duplicate|设置的镜像名称与现有镜像重复。|
|InvalidParameter.ValueTooLarge|参数长度超过限制。|


## 5. 示例

输入
<pre>
https://image.api.qcloud.com/v2/index.php?Action=ModifyImageAttribute
&Version=2017-03-12
&ImageId=img-6pb6lrmy
&ImageName=sample
&<<a href="/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
<pre>
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
</pre>


