>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (CreateKeyPair) 用于创建一个 OpenSSH RSA 密钥，可以用于登录 Linux 实例。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 开发者只需指定密钥名称，即可由系统自动创建密钥，并返回所生成的密钥的 ID 及其公钥、私钥的内容。
* 密钥名称不可重复。
* 私钥的内容可以保存到文件中作为 SSH 的一种认证方式。
* 腾讯云不会保存用户的私钥，请妥善保管。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|keyName  | 是 | String | 用于定义即将生成的密钥的名称。只能包含数字，字母和下划线。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| keyId |  String |  所生成密钥的ID，是密钥的唯一标识。 |
| keyName |   String | 用户定义的名称。 |
|  pubkey  |  String | 所生成密钥的纯文本公钥。  |
| secretkey | String | 所生成的密钥的纯文本私钥，腾讯云不会保管，请妥善保存。 |


## 4. 示例
 
输入

```
  https://cvm.api.qcloud.com/v2/index.php?Action=CreateKeyPair
  &keyName=Tencent
  &<公共请求参数>
```

输出

```

{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "data": {
        "secretkey": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZK\nAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/X\nUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCwIDAQAB\nAoGBAJEvSu5SaCD02hs0F2C4Aln2E2/qjMoDEa7spcEVfUhdaNX8ZLvk5pUvnikm\nwfSb7a71QUIcFu66zKxBK4kVcirBRCR8nTAQbQ6AhXQYP+y6ihZ9Z/g6BBEeqCpV\nuGPmKnhdxdJ8Al2huEZKJFUQhKM8XdP7dqn6yFDm0L2sTK6RAkEA9IbhP4/2CVSC\n6d8j5nj3ejPx25R3wc4G+st1tZn1O/TRqUknbVEvsxZC63bRjHiw086QIWr61L8f\nqQBLZ58DMwJBANmRv3aHVxv5sMlV0F3hD5ZgWEDIIjxD7oiBzU1rqvF6OpTQc1cF\nrnwxAXDtYYJ75B8qQEL1ph/zIE5YW0hlfckCQQCyVTwpUyCopU3kqqxQBaDXKtMU\nxS6h1VQZzBDIpMPJOj8+Ku/qNe+HuJCNkVY6EDtF/bv340GTrt+0LVbQ95MpAkEA\nxcvwUdTXB9LnuxKuHTsoDaFHepW4MivcJvRC7njM7z4dFf+wbFP4/mUbF0xoUtVJ\nXl/uDjH/tpo1K6S+UEIcqQJAfLQywCQdZ/qOJn0PwxiOhwniikSnZuZPNSw8T+kg\n/oxijESOLAJBnt3S/g+D530Enjitvfc9mEB7mh0VmwWvPg==\n-----END RSA PRIVATE KEY-----\n",
        "pubkey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
        "keyId": "skey-mv9yzyjj",
        "keyName": "Tencent"
    }
}

```



