本文将为您介绍如何使用 ECC 签名验签算法。
## 操作步骤

### 步骤1：创建非对称签名密钥
>!在密钥管理系统（KMS）中调用 [创建主密钥](https://cloud.tencent.com/document/product/573/34430) 接口创建用户主密钥时，必须传入正确的密钥用途 ASYMMETRIC_SIGN_VERIFY_ECC，这样才可以使用签名功能。
>
-  **请求**：
```
tccli kms CreateKey --Alias test_ecc --KeyUsage ASYMMETRIC_SIGN_VERIFY_ECC
```
- **返回结果**：
```
{
"Response": {
  "KeyId": "22d79428-61d9-11ea-a3c8-525400******",
  "Alias": "test_ecc",
  "CreateTime": 1583739580,
  "Description": "",
  "KeyState": "Enabled",
  "KeyUsage": "ASYMMETRIC_SIGN_VERIFY_ECC",
  "TagCode": 0,
  "TagMsg": "",
  "RequestId": "0e3c62db-a408-406a-af27-dd5ced******"
}
}
```

### 步骤2：下载公钥
-  **请求**：
```
tccli kms GetPublicKey  --KeyId 22d79428-61d9-11ea-a3c8-525400******
```
- **返回结果**：
```
{
"Response": {
  "RequestId": "408fa858-cd6d-4011-b8a0-653805******",
  "KeyId": "22d79428-61d9-11ea-a3c8-525400******",
  "PublicKey":  "MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEFLlge0vtct949CwtadHODzisgXJahujq+PvM***************bBs/f3axWbvgvHx8Jmqw==",
  "PublicKeyPem": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEFLlge0vtct949CwtadHODzisgXJa\nhujq+PvM***************bBs/f3axWbvgvHx8Jmqw==\n-----END PUBLIC KEY-----\n"
}
}
```

- **将公钥 PublicKeyPem 转成pem格式，并存入文件 public_key.pem**：
```
echo "-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEFLlge0vtct949CwtadHODzisgXJa
hujq+PvM***************bBs/f3axWbvgvHx8Jmqw==
-----END PUBLIC KEY-----" > public_key.pem
```

>!您也可以登录 [KMS 控制台](https://console.cloud.tencent.com/kms2/index) ，单击【用户密钥】>【密钥 ID/密钥名称】进入密钥信息页面，直接下载非对称密钥公钥。

### 步骤3：创建信息的明文文件

创建测试明文文件。
```
echo "test" > test_verify.txt
```
>!当生成的文件内容中，存在不可见的字符情况下（如换行符等），需对文件进行 truncate 操作（如 truncate -s -1 test_verify.txt），从而保证签名准确。


### 步骤4：计算消息摘要
>!
- 如果待签名的消息的长度不超过4096字节，可以跳过本步骤，直接进入 [步骤5](#step5)。
- 如果待签名的消息的长度超过4096字节，则需先在用户端本地计算消息摘要。


使用 openssl 对 test_verity.txt 文件内容进行摘要计算。
```
openssl dgst -sha256 -binary -out digest.bin test_verify.txt
```

[](id:step5)
### 步骤5：通过 KMS 签名接口生成签名

调用 KMS 的 [签名](https://cloud.tencent.com/document/product/573/52065) 接口计算信息的签名。
1. 消息原文或消息摘要进行计算签名之前，需先进行 base64 编码。
```
//消息摘要进行base64编码。
openssl enc -e -base64 -A -in digest.bin -out encoded.base64
//消息原文进行base64编码。
openssl enc -e -base64 -A -in test_verify.txt -out encoded.base64
```
2. 进行签名的计算。
	- **请求**：
```
// 将上述 encoded.base64 的文件内容作为 SignByAsymmetricKey 的 Message 参数，以消息摘要的形式进行签名。
tccli kms SignByAsymmetricKey --KeyId 22d79428-61d9-11ea-a3c8-525400****** --Algorithm ECC_P256_R1 --Message "qJQj83hSyOuU7Tn0SRReGCk4yuuVWaeZ44BP******==" --MessageType DIGEST
// 以消息原文的形式进行签名（原文要进行 Base64 编码）。
tccli kms SignByAsymmetricKey --KeyId 22d79428-61d9-11ea-a3c8-525400****** --Algorithm ECC_P256_R1 --Message "dG***Ao=" --MessageType RAW
```
	- **返回结果**：
```
{
"Response": {
  "Signature": "U7Tn0SRReGCk4yuuVWaeZ4******",
  "RequestId": "408fa858-cd6d-4011-b8a0-653805******"
}
}
```
	- **将签名内容 Signature 存入文件 signContent.sign：**
```
echo "U7Tn0SRReGCk4yuuVWaeZ4******" | base64 -d > signContent.bin
```

### 步骤6：验证签名

1. 通过 KMS 验证签名接口校验。( 建议使用该方法进行验证签名)
	- **请求**：
```
// 对消息摘要进行验证(将步骤4 encoded.base64 文件内容作为 VerifyByAsymmetricKey 的 Message 参数，以消息摘要的形式进行验签)。
tccli kms VerifyByAsymmetricKey --KeyId 22d79428-61d9-11ea-a3c8-525400****** --SignatureValue "U7Tn0SRReGCk4yuuVWaeZ4******" --Message "QUuAcNFr1Jl5+3GDbCxU7te7Uekq+oTxZ**********=" --Algorithm ECC_P256_R1 --MessageType DIGEST
// 对消息原文进行验证（原文要进行Base64编码）。
tccli kms VerifyByAsymmetricKey --KeyId 22d79428-61d9-11ea-a3c8-525400****** --SignatureValue "U7Tn0SRReGCk4yuuVWaeZ4******" --Message "dG***Ao=" --Algorithm ECC_P256_R1 --MessageType RAW
```
	- **返回结果**：
```
{
"Response": {
  "SignatureValid": true,
  "RequestId": "6758cbf5-5e21-4c37-a2cf-8d47f5******"
}
}
```

>!签名接口和验签接口中使用的参数 Message 和 MessageType 的取值要保持一致。

2. 通过 KMS 公钥和签名内容在本地进行验证。
	-  **请求**：
```
openssl dgst -verify public_key.pem -sha256 -signature ./signContent.bin ./test_verify.txt
```
	- **返回结果**：
```
Verified OK
```
