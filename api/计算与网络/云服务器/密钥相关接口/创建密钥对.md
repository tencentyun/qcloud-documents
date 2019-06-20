>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述

本接口 (CreateKeyPair) 用于创建一个 `OpenSSH RSA` 密钥对，可以用于登录 `Linux` 实例。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 开发者只需指定密钥对名称，即可由系统自动创建密钥对，并返回所生成的密钥对的 `ID` 及其公钥、私钥的内容。
* 密钥对名称不能和已经存在的密钥对的名称重复。
* 私钥的内容可以保存到文件中作为 `SSH` 的一种认证方式。
* 腾讯云不会保存用户的私钥，请妥善保管。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/11650)页面。

| 参数名称 | 类型 | 是否必选 | 描述 |
|---------|---------|---------|---------|
|Version|String|是|表示API版本号，主要用于标识请求的不同API版本。 本接口第一版本可传：2017-03-12。|
|KeyName  | String | 是 |密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
|ProjectId| Integer| 是| 密钥对创建后所属的[项目](/document/product/378/10863)ID。<br><br>可以通过以下方式获取项目ID：<br><li>通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID。<br><li>通过调用接口 [DescribeProject](/document/api/378/4400) ，取返回信息中的`projectId `获取项目ID。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId| String| 唯一请求 `ID` 。每次请求都会返回 `RequestId`。当用户调用接口失败找后台研发人员处理时需提供该 `RequestId`。|
| KeyPair| [KeyPair](/document/api/213/9451#keypair) object| 密钥对信息。|


## 4. 错误码

以下错误码表仅列出了该接口的业务逻辑错误码，更多错误码详见[公共错误码](/document/api/213/11657)。


| 错误码 | 描述 |
|---------|---------|
|MissingParameter| 参数缺失。请求没有带必选参数。|
|InvalidParameterValue| 无效参数值。参数值格式错误或者参数值不被支持等。|
|InvalidKeyPairName.Duplicate|密钥对名称重复。|
|InvalidKeyPair.LimitExceeded|密钥对数量超过限制。|
|InvalidKeyPairNameEmpty|密钥名称为空。|
|InvalidKeyPairNameTooLong|密钥名称超过25个字符。|
|InvalidKeyPairNameIncludeIllegalChar|密钥名称包含非法字符。密钥名称只支持英文、数字和下划线。|
|InvalidProjectId.NotFound|无效的项目ID，指定的项目ID不存在。|
|InternalServerError|操作内部错误。|


## 5. 示例

输入

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=CreateKeyPair
&Version=2017-03-12
&KeyName=Tencent
&ProjectId=0
&<<a href="/document/api/213/11650">公共请求参数</a>>
</pre>

输出

<pre>
{
    "Response": {
        "KeyPair": {
            "KeyId": "skey-mv9yzyjj",
            "KeyName": "Tencent",
            "ProjectId": 0,
            "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZK\nAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/X\nUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCwIDAQAB\nAoGBAJEvSu5SaCD02hs0F2C4Aln2E2/qjMoDEa7spcEVfUhdaNX8ZLvk5pUvnikm\nwfSb7a71QUIcFu66zKxBK4kVcirBRCR8nTAQbQ6AhXQYP+y6ihZ9Z/g6BBEeqCpV\nuGPmKnhdxdJ8Al2huEZKJFUQhKM8XdP7dqn6yFDm0L2sTK6RAkEA9IbhP4/2CVSC\n6d8j5nj3ejPx25R3wc4G+st1tZn1O/TRqUknbVEvsxZC63bRjHiw086QIWr61L8f\nqQBLZ58DMwJBANmRv3aHVxv5sMlV0F3hD5ZgWEDIIjxD7oiBzU1rqvF6OpTQc1cF\nrnwxAXDtYYJ75B8qQEL1ph/zIE5YW0hlfckCQQCyVTwpUyCopU3kqqxQBaDXKtMU\nxS6h1VQZzBDIpMPJOj8+Ku/qNe+HuJCNkVY6EDtF/bv340GTrt+0LVbQ95MpAkEA\nxcvwUdTXB9LnuxKuHTsoDaFHepW4MivcJvRC7njM7z4dFf+wbFP4/mUbF0xoUtVJ\nXl/uDjH/tpo1K6S+UEIcqQJAfLQywCQdZ/qOJn0PwxiOhwniikSnZuZPNSw8T+kg\n/oxijESOLAJBnt3S/g+D530Enjitvfc9mEB7mh0VmwWvPg==\n-----END RSA PRIVATE KEY-----\n"
        },
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>
