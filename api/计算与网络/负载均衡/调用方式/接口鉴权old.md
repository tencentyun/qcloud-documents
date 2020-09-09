腾讯云 API 使用签名方法（Signature）对接口进行鉴权。每一次请求都需要在请求中包含签名信息，以验证用户身份。

在第一次使用云 API 之前，用户首先需要在腾讯云 CVM 控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey， SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。已有安全凭证的用户请从生成签名串开始操作。

## 申请安全凭证
第一次使用云 API 的用户必须先申请安全凭证才可使用。
1. 登录 [API 密钥管理](https://console.cloud.tencent.com/capi) 控制台。
2. 单击【新建密钥】即可以创建一对 SecretId/SecretKey， 每个帐号最多可以创建两对 SecretId/SecretKey。

## 生成签名串
假设上一步申请的 SecretId 和 SecretKey 分别是：
 - SecretId：AKID****J5yKBZQpn74WFkmLPx3gnPhESA。
 - SecretKey：Gu5t****pq86cd98joQYCN3Cozk1qA。

以查询 CVM 实例列表请求为例，请求参数为：

| 参数 | 参数写法 | 
|---------|---------|
| 方法名 | Action=DescribeInstances | 
| SecretId | SecretId= AKID****J5yKBZQpn74WFkmLPx3gnPhESA | 
| 当前时间戳 | Timestamp=1408704141 | 
| 随机正整数 | Nonce=345122 | 
| 区域 | Region=gz | 
| 待查询的第一台机器的实例 ID | instanceIds.0=qcvm12345 | 
| 待查询的第二台机器的实例 ID | instanceIds.1=qcvm56789 | 

接口签名的详细步骤如下：
###  对参数排序
对请求参数按参数名做字典序升序排列（例如 PHP 中可使用 ksort 函数排序） , 结果如下：

```
{
  'Action' : 'DescribeInstances',
  'Nonce' : 345122,
  'Region' : 'gz',
  'SecretId' : 'AKID****J5yKBZQpn74WFkmLPx3gnPhESA',
  'Timestamp' : 1408704141
  'instanceIds.0' : 'qcvm12345',
  'instanceIds.1' : 'qcvm56789',
}
```

### 拼接请求字符串
把上一步排序好的请求参数，格式化成 k=v，然后用"&"拼接在一起，注意 v 为原始值而非 url 编码后的值。结果为：

```
Action=DescribeInstances&Nonce=345122&Region=gz&SecretId=AKID****J5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141& instanceIds.0=qcvm12345&instanceIds.1=qcvm56789
```

### 拼接签名原文字符串
拼接签名原文时需要如下参数：

- 请求方法： 支持 POST 和 GET 方式，这里使用 GET 请求，注意方法为全大写。
- 请求主机： cvm.api.qcloud.com，根据接口所属模块不同域名也不同，详见各接口详细说明。
- 请求路径： `/v2/index.php`。
- 请求字符串： 即前 2 步生成的请求字符串。

签名原文的拼接规则为：
请求方法 + 请求主机 +请求路径 + ? + 请求字符串。

示例拼接结果为：

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce= 345122&Region=gz&SecretId=AKID****J5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141
```

### 生成签名串
1. 使用 HMAC-SHA1 算法对上面步骤中获得的 **签名原文字符串** 进行签名。
2. 将生成的签名串使用 Base64 进行编码，获得最终的签名串。

以 PHP 语言为例：

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=345122&Region=gz&SecretId=AKID****J5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

得到的签名串为：

```
HgIYOPcx5lN6gz8JsCFBNAWp2oQ=
```

使用其它程序设计语言开发时，可用上面示例中的原文进行签名验证，得到的签名串与例子中的一致即可。

### 添加签名, 发送请求
- 请求参数中添加 Signature 参数， 参数值为上一步生成的 **签名串**，并且对签名进行 url 编码。上面生成的签名 `HgIYOPcx5lN6gz8JsCFBNAWp2oQ=` 编码后为 `HgIYOPcx5lN6gz8JsCFBNAWp2oQ%3D`。

- 如果是使用GET方法，则对所有请求参数的参数值做 URL 编码；例如若使用 POST 方法则除 Signature 参数外无需URL 编码。
  
- 发送 HTTPS 协议请求即可得到 JSON 字符串格式的接口返回值。

示例最终的请求 URL 为：

```
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&Nonce=345122
&Region=gz
&SecretId=AKID****J5yKBZQpn74WFkmLPx3gnPhESA
&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ%3D
&Timestamp=1408704141
&instanceIds.0=qcvm12345
&instanceIds.1=qcvm56789 
```

