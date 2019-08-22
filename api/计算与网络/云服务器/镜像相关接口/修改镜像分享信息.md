>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口（ModifyImageSharePermission）用于修改镜像分享信息。

接口请求域名：<font style="color:red">image.api.qcloud.com</font>。

* 分享镜像后，被分享账户可以通过该镜像创建实例。
* 每个自定义镜像最多可共享给50个账户。
* 分享镜像无法更改名称，描述，仅可用于创建实例。
* 只支持分享到对方账户相同地域。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
| ImageId |  String |是 | 镜像ID，形如`img-gvbnzy6f`。镜像Id可以通过如下方式获取：<br><li>通过[DescribeImages](/document/api/213/9418)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。 <br>镜像ID必须指定为状态为`NORMAL`的镜像。镜像状态请参考[镜像数据表](/document/api/213/9452#image_state)。|
| AccountIds |  array of Strings |是 | 接收分享镜像的账号Id列表，array型参数的格式可以参考[API简介](/document/api/213/568)。帐号ID不同于QQ号，查询用户帐号ID请查看[帐号信息](https://console.cloud.tencent.com/developer)中的帐号ID栏。|
| Permission |  String |是 | 操作，包括 `SHARE`，`CANCEL`。其中`SHARE`代表分享操作，`CANCEL`代表取消分享操作。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|

## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/10146)。

| 错误码 |  描述 |
|---------|---------|
|InvalidAccountId.NotFound | 无效的帐号ID。 |
|InvalidAccountIs.YourSelf|帐号ID不能指定自己的帐号ID。|
|OverQuota|镜像分享次数超过限制。|

## 5. 示例 

输入
<pre>
https://image.api.qcloud.com/v2/index.php?Action=ModifyImageSharePermission
&Version=2017-03-12
&ImageId=img-6pb6lrmy
&AccountIds.1=1038493875
&Permission=SHARE
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