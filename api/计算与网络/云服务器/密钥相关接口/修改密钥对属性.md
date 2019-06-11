>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (ModifyKeyPairAttribute) 用于修改密钥对属性。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 修改密钥对ID所指定的密钥对的名称和描述信息。
* 密钥对名称不能和已经存在的密钥对的名称重复。
* 密钥对ID是密钥对的唯一标识，不可修改。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称        | 类型     | 是否必选 | 描述                                       |
| ----------- | ------ | ---- | ---------------------------------------- |
| Version     | String | 是    | 表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。 |
| KeyId       | String | 是    | 密钥对ID，密钥对ID形如：`skey-11112222`。<br><br>可以通过以下方式获取可用的密钥 ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥 ID。<br><li>通过调用接口 [DescribeKeyPairs](/document/api/213/9403) ，取返回信息中的 `KeyId` 获取密钥对 ID。 |
| KeyName     | String | 否    | 修改后的密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。      |
| Description | String | 否    | 修改后的密钥对描述信息。可任意命名，但不得超过60个字符。            |


## 3. 输出参数

| 参数名称      | 类型     | 描述                                       |
| --------- | ------ | ---------------------------------------- |
| RequestId | String | 唯一请求 `ID`。每次请求都会返回 `RequestId`。当用户调用接口失败找后台研发人员处理时需提供该 `RequestId`。 |


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码                              | 描述                                       |
| -------------------------------- | ---------------------------------------- |
| MissingParameter                 | 参数缺失。请求没有带必选参数。                          |
| InvalidParameter                 | 无效参数。参数不合要求或者参数不被支持等。                    |
| InvalidParameterValue            | 无效参数值。参数值格式错误或者参数值不被支持等。                 |
| InvalidKeyPairId.Malformed       | 无效密钥对ID。指定的密钥对ID格式错误。例如ID长度错误`skey-1122`。 |
| InvalidKeyPairId.NotFound        | 无效密钥对ID。指定的密钥对ID不存在。                     |
| InvalidKeyPairName.Duplicate     | 密钥对名称重复。                                 |
| InvalidKeyPairDescriptionTooLong | 密钥名称超过60个字符。                             |
| InternalServerError              | 操作内部错误。                                  |


## 5. 示例

输入

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyKeyPairAttribute
&Version=2017-03-12
&KeyId=skey-mv9yzyjj
&KeyName=Tencent
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
