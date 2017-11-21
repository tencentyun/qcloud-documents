使用 MQTT 收发消息，服务端需要对客户端的身份进行权限校验，因此客户端请求中都需要带上签名以便比对身份。
腾讯云 IoT MQ 服务端会对每个客户端的访问请求进行身份验证，即客户端的每个请求中都需包含签名信息（Signature），以验证用户身份。

## 1. MQTT SDK 访问服务器
MQTT 客户端连接 IoT MQ 服务器时，须发送 CONNECT 报文，且在 Connect 报文中需上传 username 和 password。其中 username 是 SecretId，password 是将 Appid、Instanceid 等作为待签名字符串，用 SecretKey 作为秘钥计算得到的签名。

## 2. 申请安全凭证
在第一次使用客户端之前，用户需要在【腾讯云控制台】> 【[API 密钥管理](https://console.cloud.tencent.com/cam/capi) 】上申请安全凭证。安全凭证包括 SecretId 和 SecretKey，其中：

- **SecretId：**用于标识 API 调用者身份；
- **SecretKey：**用于加密签名字符串和服务器端验证签名字符串的密钥。

>**注意：**
> SecretKey 是构建腾讯云 MQTT 请求的重要凭证，使用腾讯云 MQTT 请求 可以操作您名下的消息队列 IoT MQ 资源，为了您的财产和服务安全，请妥善保存并定期更换密钥，当您更换密钥后，请及时删除旧密钥。


### 2.1 申请安全凭证步骤：

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)。
2. 单击【云产品】，选择【管理工具】栏下的【云 API 密钥】，进入云 API 密钥管理页面。
![](//mc.qcloudimg.com/static/img/a771465c47830d54730f8f431d586991/image.png)
3. 在 [ API 密钥管理](https://console.cloud.tencent.com/capi) 页面，单击【新建密钥】即可以创建一对 SecretId/SecretKey。
>**注意：**
> - 开发商帐号最多可以拥有两对 SecretId / SecretKey。
> - 被开发商添加为子用户的 QQ 帐号，在不同开发商控制台，可以申请不同的安全凭证。
> - 子用户的安全凭证，目前仅可调用部分接口的云 API。

##  3. 生成签名串
有了安全凭证 SecretId 和 SecretKey 后，就可以生成签名串了。生成签名串的详细过程如下
### 3.1 拼接原串
假设用户的 Appid、Instanceid分别是：
Appid：1251762227
Instanceid：mqtt-fludu2t6

则拼接后的原串为：Appid=1251762227&Instanceid=mqtt-fludu2t6&Action=Connect

>**注意：**
>这里只是示例，请用户根据自己实际的 Appid 和 Instanceid 和请求参数进行后续操作。

### 3.2 使用签名算法生成签名串
假设用户的 SecretId 、SecretKey 分别是：
SecretId： AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
SecretKey： Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

>**注意：**
>这里只是示例，请用户根据自己实际的 SecretId 和 SecretKey 和请求参数进行后续操作。

然后用 SecretKey 作为秘钥，使用 HmacSHA256 签名算法对上一步中获得的 签名原文字符串 进行签名，然后将生成的签名串使用 Base64 进行编码，即可获得最终的签名串。

HmacSHA256 的算法实现，各个语言都有现成的函数库，下面以 PHP 语言为例（使用其它程序设计语言开发时，可用上述示例中的原文字符串进行签名验证，得到的签名串与例子中的一致即可）：

```php
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'Appid=1251762227&Instanceid=mqtt-fludu2t6&Action=Connect';
$signStr = base64_encode(hash_hmac('sha256', $srcStr, $secretKey, true));
echo $signStr;
```

最终得到的签名串为:

```
anoZcbvEjytpjOWQE61+DO5XOU61XyXBKioOE5WCI8s=
```

## 4. 客户端 CONNECT
使用客户端 SDK 连接 IoT MQ 服务器时，在 Connect 报文中的用户名为 SecretId，密码为签名串。根据上述示例，详情如下
username：AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
password：anoZcbvEjytpjOWQE61+DO5XOU61XyXBKioOE5WCI8s=
