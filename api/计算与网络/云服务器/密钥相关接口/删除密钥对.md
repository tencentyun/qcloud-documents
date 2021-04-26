>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (DeleteKeyPairs) 用于删除已在腾讯云托管的密钥对。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 可以同时删除多个密钥对。
* 不能删除已被实例或镜像引用的密钥对，所以需要独立判断是否所有密钥对都被成功删除。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|KeyIds.N | array of Strings | 是| 一个或多个待操作的密钥对ID。每次请求批量密钥对的上限为100。<br><br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](/document/api/213/9403) ，取返回信息中的 `KeyId` 获取密钥对ID。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 `ID`。每次请求都会返回 `RequestId`。当用户调用接口失败找后台研发人员处理时需提供该 `RequestId`。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidParameterValue.LimitExceeded|参数值数量超过限制。|
|InvalidKeyPairId.Malformed|无效密钥对ID。指定的密钥对ID格式错误。例如ID长度错误`skey-1122`。|
|InvalidKeyPair.LimitExceeded|密钥对数量超过限制。|
|InternalServerError|操作内部错误。|


## 5. 示例

输入

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DeleteKeyPairs
&Version=2017-03-12
&KeyIds.1=skey-mv9yzyjj
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
