Python3 语言 SDK，底层使用 C 语言实现，上层通过 ctypes 封装后，提供接口供 Python3 语言调用。

## 错误码
| 错误码               | 说明                             |
| -------------------- | -------------------------------- |
| 0                    | 正常返回                         |
| -1                   | 一般错误                         |
| -2                   | 加密的原文为空                   |
| -3                   | 未设置主密钥                     |
| -4                   | 算法不支持                       |
| -5                   | 产生 DataKey 错误                |
| -6                   | 加密 DataKey 错误                |
| -7                   | 序列化 ProtoBuf 出错             |
| -8                   | 密文数据太短                     |
| -9                   | 获取 ProtoBuf 报文出错           |
| -10                  | 解析 ProtoBuf 报文出错           |
| -11                  | 解密 DataKey 错误                |
| -12                  | 设置 DataKey 错误                |
| -13                  | 签名不合法，导致校验不通过       |
| -14                  | 内存错误                         |
| -15                  | KMS 服务未开通                   |
| -16                  | 未升级为 KMS 旗舰版              |

## 初始化 SDK 接口

### InitSdk

- **功能描述**：检验用户是否开通 KMS 旗舰版服务。
- **输入参数**：

| 参数名称  | 必选 | 类型   | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| region    | 是   | str | CMK 地域信息字符串，详见产品支持的 [**地域列表**](https://cloud.tencent.com/document/api/573/34406#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) |
| secretId  | 是   | str | 云账户 API 密钥 ID 值                                            |
| secretKey | 是   | str | 云账号 API 密钥 Key 值                                           |
| domainName | 是   | str | 域名信息字符串                                           |

- **返回值**：接口返回一个整数。
  - 当接口返回值为0，表示初始化成功。
  - 当接口返回值为非0，代表初始化失败。

> !
>  - SecretId 和 SecretKey 需保密存储：腾讯云接口认证主要依靠 SecretID 和 SecretKey，SecretID 和 SecretKey 是用户的唯一认证凭证。业务系统需要该凭证调用腾讯云接口。
>  - SecretID 和 SecretKey 的权限控制：建议使用子账号，根据业务需要进行接口授权的方式管控风险。
>  - 在设置 domainName 时：如果 domainName 入参为""，则从环境变量 TENCENT_SDK_DOMAIN 中读取值，反之，则以入参为准。

## KMS加密方式的接口说明

### NewMasterKey

- **功能描述**：将用户首个主密钥加入主密钥信息列表。
- **参数说明**：

| 参数名称   | 必选 | 类型   | 描述                                                         |
| ---------- | ---- | ------ | ------------------------------------------------------------ |
| cmkRegion  | 是   | str | 主密钥（CMK）地域信息                                        |
| cmkKeyId   | 是   | str | 主密钥（CMK）的 ID，从 KMS 控制台中查询                         |

- **返回值**：接口返回整数、主密钥信息列表。
  - 当接口返回整数值为0，表示添加成功。
  - 当接口返回整数值为非0，代表添加失败。

>!请确保用于加密的首个主密钥，在 KMS 平台中是处于**生效**的状态。

### AddMasterKey

- **功能描述**：加入备用的用户主密钥，目的是为了灾备，当首个主密钥无法使用时，会使用的备用密钥，最多支持加入4个备用密钥。
- **参数说明**：

| 参数名称   | 必选 | 类型   | 描述                                                         |
| ---------- | ---- | ------ | ------------------------------------------------------------ |
| masterKeys | 是   | list | 主密钥信息列表，长度根据用户加入的密钥数量来确定 |
| cmkRegion  | 是   | str | 主密钥（CMK）地域信息                                        |
| cmkKeyId   | 是   | str | 主密钥（CMK）的 ID，从 KMS 控制台中查询                         |

- **返回值**：接口返回整数、主密钥信息列表。
  - 当接口返回值为0，表示添加成功。
  - 当接口返回值为非0，代表添加失败。


### InitKeyManager

- **功能描述**：初始化用户的主密钥，包含主密钥信息、密钥加密次数、密钥生效时间等，具体参见下方参数说明。
- **参数说明**：

| 参数名称     | 必选 | 类型                  | 描述                                                         |
| ------------ | ---- | --------------------- | ------------------------------------------------------------ |
| masterKey    | 是   | list                  | 主密钥（CMK）信息列表                                        |
| msgCount     | 是   | int                   | 每个缓存 DataKey 可加密的消息数量，加密的数量达到后，会重新向KMS后台请求，生成新的DataKey，设置为0表示没有限制使用次数。 |
| enExpiretime | 是   | int                   | 加密使用的 DataKey 在缓存中的有效期，单位为秒，和消息数量一起生效，消息数量超过或者超时时间达到，都会触发 DataKey 的替换，0表示不过期 |
| deExpiretime | 是   | int                   | 解密使用的 DataKey 缓存的有效期，单位为秒，0表示不过期      |
| secretId     | 是   | str                   | 云账户 API 密钥 ID 值                                            |
| secretKey    | 是   | str                   | 云账号 API 密钥 Key 值                                           |

- **返回值**：接口返回 KeyManager 对象。
  - 当接口返回值不为 None，表示初始化成功。
  - 当接口返回值为None，代表初始化失败。

### Encrypt

- **功能描述**：使用 KMS 平台创建的 DataKey，进行本地数据加密。
- **输入参数**：

| 参数名称          | 必选 | 类型                  | 描述                                                         |
| ----------------- | ---- | --------------------- | ------------------------------------------------------------ |
| source            | 是   | bytes                 | 待加密的明文数据                                             |
| keyManager        | 是   | kms_enc_sdk.KeyManager | 已经初始化的 KeyManager 结构体指针                             |
| masterKeys        | 是   | list                  | 主密钥（CMK）信息列表                                        |
| algorithm         | 是   | Algorithm             | 算法枚举值，参照后面算法列表                                 |
| encryptionContext | 是   | str                   | 用于标识 DataKey 的辅助字段，key/value 对的 json 字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"} |
| blockSize         | 是   | int                   | 0 表示加密时不分块加密，非0表示分块加密以及分块大小，单位 byte |

- **返回值**：接口返回三个内容，一个整数、一个 MsgHead 对象、一个字节类型的加密后的密文。
  - 当接口返回的整数信息为0，代表加密成功。
  - 当接口返回的整数信息为非0，代表加密失败。

> !加密后的数据，会加入 DataKey 相关信息，只能使用 KMS 密钥保护方式的接口进行解密。

### Decrypt

- **功能描述**：方法用于解密密文，得到明文数据。
- **输入参数**：

| 参数名称   | 必选 | 类型                  | 描述                                                         |
| ---------- | ---- | --------------------- | ------------------------------------------------------------ |
| source     | 是   | bytes                 | 加密后的数据                                                 |
| keyManager | 是   | kms_enc_sdk.KeyManager | 已经初始化的 KeyManager 对象                             |

- **返回值**：接口返回三个内容，一个整数、一个 MsgHead 结构体、一个字节类型的解密后的明文。
  - 当接口返回的整数信息为0，代表解密成功。
  - 当接口返回的整数信息为非0，代表解密失败。

### Algorithm 支持的加密算法列表

| 枚举值                       | 数值 | 说明                            |
| ---------------------------- | ---- | ------------------------------- |
| SM4_CBC_128_WITH_SIGNATURE | 1    | 使用 SM3HAC 签名的 SM4 CBC 模式     |
| SM4_CBC_128                | 2    | 不使用签名的 SM4 CBC 模式加密     |
| SM4_GCM_128_WITH_SIGNATURE | 3    | 使用 SM3HAC 签名的 SM4 GCM 模式     |
| SM4_GCM_128                | 4    | 不使用签名的 SM4 GCM 模式加密算法 |
| SM4_CTR_128_WITH_SIGNATURE | 5    | 使用 SM3HAC 签名的 SM4 CTR 模式     |
| SM4_CTR_128                | 6    | 不使用签名的 SM4 CTR 模式         |
| SM4_ECB_128_WITH_SIGNATURE | 7    | 使用 SM3HAC 签名的 SM4 ECB 模式     |
| SM4_ECB_128                | 8    | 不使用签名的 SM4 ECB 模式         |

### KMS加密方式接口调用示例

```
#coding=utf-8
import sys
import os
import time

from kms_enc_sdk import *

region1 = 'replace-with-real-region1'
keyId1 = 'replace-with-realkeyid1'
region2 = 'replace-with-real-region2'
keyId2 = 'replace-with-realkeyid2'
secretId = 'replace-with-real-secretId'
secretKey = 'replace-with-real-secretKey'
domainName = 'kms.tencentcloudapi.com'

def ECBEnAndDeWithSignTest():
	   ret,masterKey = NewMasterKey(region1,keyId1)
	   if ret != 0:
		   print('NewMasterKey error:',ret)
		   return
	   ret,masterKey = AddMasterKey(masterKey,region2,keyId2)
	   if ret != 0:
		   print('AddMasterKey error:',ret)
		   return
	
	   keymanager = InitKeyManager(masterKey,0,0,0,secretId,secretKey)
	   if keymanager == None:
		   print('KeyManager error')
		   return
	
	   ret,enheader,endata = Encrypt(b'hello',keymanager,masterKey,Algorithm.SM4_ECB_128_WITH_SIGNATURE,'{}',0)
	   if ret == 0:
		   print('Encrypt ok')
	   else:
		   print('Encrypt error:',ret)
		   return

	   ret,deheader,dedata = Decrypt(endata,keymanager)
	   if ret == 0:
		   print ('dedata:',)
		   print (dedata)
	   else:
		   print('Decrypt error:',ret)

ret = InitSdk(region1,secretId,secretKey,domainName)
if ret != 0:
	   print('InitSdk error:',ret)
	   sys.exit(1)

ECBEnAndDeWithSignTest()

```

## 原生加密方式的接口说明

原生加密方式对应的服务也需要升级为 [旗舰版](https://cloud.tencent.com/document/product/573/18809)，与 KMS 密钥保护方式相比，原生加密方式需要用户自己生成加密密钥进行加解密，由用户保证密钥的安全性。出于安全与合规的考虑，建议用户使用 KMS 密钥保护方式。
>?其中 CTR 模式加密没有填充，其他的模式加密采用 PKCS#7 标准进行填充。

### Sm2GetKey

- **功能描述**：使用 SM2 算法生成密钥对。
- **输入参数**：无需填充输入参数。
- **返回值**：接口返回三个内容，一个整数和两个字节列表（分别是生成的公钥值、私钥值）。
  - 当接口返回的整数信息为0，表示获取密钥对成功。
  - 当接口返回的整数信息为非0，代表获取失败。

### Sm2Sign

- **功能描述**：使用 SM2 算法进行签名。
- **输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubKey   | 是   | bytes | 公钥内容，数据长度固定为64字节 |
| priKey   | 是   | bytes | 私钥内容，数据长度固定为32字节 |
| source   | 是   | bytes | 原文数据                               |

- **返回值**：接口返回两个内容，一个整数和一个包含签名内容的字节列表。
  - 当接口返回的整数信息为0，代表签名成功。
  - 当接口返回的整数信息为非0，代表签名失败。

>!公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2Verify

- **功能描述**：使用 SM2 算法进行验签。
- **输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubkey   | 是   | bytes | 公钥内容，数据长度固定为64字节 |
| sign     | 是   | bytes | 签名后的数据                           |
| source   | 是   | bytes | 原文数据                               |

- **返回值**：接口返回一个整数。
  - 当接口返回的整数信息为0，表示验签成功。
  - 当接口返回的整数信息为非0，代表验签失败。

>!公钥长度为固定长度64字节，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2Encrypt

- **功能描述**：使用 SM2 算法进行加密。
- **输入参数**：

| 参数名称 | 必选 | 类型   | 描述                               |
| -------- | ---- | ------ | ---------------------------------- |
| pubkey   | 是   | bytes | 公钥内容，数据长度为64字节 |
| source   | 是   | bytes | 源数据                             |

- **返回值**：接口返回两个内容，一个整数和一个包含加密后的密文内容的字节列表。
  - 当接口返回的整数信息为0，代表加密成功。
  - 当接口返回的整数信息为非0，代表加密失败。

>!SM2 加密适用于小数据的场景，不建议加密超过256k的数据。

### Sm2Decrypt

-	**功能描述**：使用 SM2 算法进行解密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| prikey   | 是   | bytes | 私钥内容，数据长度固定为32字节 |
| source   | 是   | bytes | 加密后的数据                           |

- **返回值**：接口返回两个内容，一个整数和一个包含解密后的明文内容的字节列表。
  - 当接口返回的整数信息为0，代表解密成功。
  - 当接口返回的整数信息为非0，代表解密失败。

### Sm2PemChangeToPubkey

- **功能描述**：对 pem 格式的公钥内容进行转换。
- **输入参数**：

| 参数名称      | 必选 | 类型   | 描述              |
| ------------- | ---- | ------ | ----------------- |
| pemPubKeyInfo | 是   | bytes | pem 格式的公钥信息 |

- **返回值**：接口返回两个内容，一个整数和一个包含转换后的公钥内容的字节列表。
  - 当接口返回的整数信息为0，代表转换成功。
  - 当接口返回的整数信息为非0，代表转换失败。

### HashForSM3WithSM2

- 功能描述：使用 **Sm2GetKey** 接口生成的公钥，并基于SM3算法生成信息摘要。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| msg      | 是   | bytes | 原文数据                               |
| pubKey   | 是   | bytes | 公钥内容，数据长度固定为64字节 |
| id       | 是   | bytes | ID 值                                   |

- 返回值：接口返回两个内容，一个整数和一个包含生成的摘要内容的字节列表。
  - 当接口返回的整数信息为0，代表摘要生成成功。
  - 当接口返回的整数信息为非0，代表摘要生成失败。

### Sm2SignWithDigest

- **功能描述**：使用本地生成的消息摘要生成签名。
- **输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                     |
| -------- | ---- | ------ | ---------------------------------------- |
| pubKey   | 是   | bytes | 公钥内容，数据长度固定为64字节   |
| priKey   | 是   | bytes | 私钥内容，数据长度固定为32字节   |
| digest   | 是   | bytes | **HashForSM3WithSM2** 生成的摘要信息内容 |

- **返回值**：接口返回两个内容，一个整数和一个包含生成的签名内容的字节列表。
  - 当接口返回的整数信息为0，代表签名成功。
  - 当接口返回的整数信息为非0，代表摘要签名失败。

### Sm2VerifyWithDigest

- **功能描述**：通过生成的摘要内容进行验签。
- **输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                     |
| -------- | ---- | ------ | ---------------------------------------- |
| pubKey   | 是   | bytes | 公钥内容，数据长度固定为64字节   |
| sig      | 是   | bytes | **Sm2SignWithDigest** 生成的签名内容                               |
| digest   | 是   | bytes | **HashForSM3WithSM2** 生成的摘要信息内容 |

- **返回值**：接口返回一个整数。
  - 当接口返回的整数信息为0，代表验签成功。
  - 当接口返回的整数信息为非0，代表摘要验签失败。

### Sm3Hmac

-	**功能描述**：使用 SM3 哈希运算 Hmac 计算。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述               |
| -------- | ---- | ------ | ------------------ |
| source     | 是   | bytes | 原文数据           |
| hmacKey  | 是   | bytes | 计算 Hmac 的密钥内容 |

- **返回值**：接口返回两个内容，一个整数和一个包含 Hmac 内容的字节列表。
  - 当接口返回的整数信息为0，代表 Hmac 计算成功。
  - 当接口返回的整数信息为非0，代表 Hmac 计算失败。

### Sm3Digest

-	**功能描述**：使用 SM3 生成摘要。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述               |
| -------- | ---- | ------ | ------------------ |
| source     | 是   | bytes | 原文数据           |

- **返回值**：接口返回两个内容，一个整数和一个包含摘要内容的字节列表。
  - 当接口返回的整数信息为0，代表生成摘要成功。
  - 当接口返回的整数信息为非0，代表生成摘要失败。

### Sm4CbcEncrypt/Sm4CtrEncrypt

-	功能描述：方法适用于 SM4 加密算法 CBC、CTR 模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 原文数据                                     |
| Key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | bytes | 初始化向量，固定为128位(16字节)，不能设置为空       |

- 返回值：接口返回两个内容，一个整数和一个包含加密后的密文内容的字节列表。
  - 当接口返回的整数信息为0，代表加密成功。
  - 当接口返回的整数信息为非0，代表加密失败。

### Sm4CbcDecrypt/Sm4CtrDecrypt

-	**功能描述**：方法是用于 SM4 加密算法 CBC、CTR 模式下的解密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 加密后的数据                                 |
| Key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | bytes | 初始化向量，固定为128位(16字节)，不能设置为空       |

- **返回值**：接口返回两个内容，一个整数和一个包含解密后的明文内容的字节列表。
  - 当接口返回的整数信息为0，代表解密成功。
  - 当接口返回的整数信息为非0，代表解密失败。

### Sm4EcbEncrypt

-	**功能描述**：方法是用于 SM4 加密算法 ECB 模式下的加密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 原文数据                                     |
| Key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |

- **返回值**：接口返回两个内容，一个整数和一个包含加密后的密文内容的字节列表。
  - 当接口返回的整数信息为0，代表加密成功。
  - 当接口返回的整数信息为非0，代表加密失败。

### Sm4EcbDecrypt

-	**功能描述**：方法是用于 SM4 加密算法 ECB 模式下的解密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 加密后的数据                                 |
| Key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |

- **返回值**：接口返回两个内容，一个整数和一个包含解密后的明文内容的字节列表。
  - 当接口返回的整数信息为0，代表解密成功。
  - 当接口返回的整数信息为非0，代表解密失败。

### Sm4GcmEncrypt

-	**功能描述**：方法是用于 SM4 加密算法 GCM 模式下的加密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 原文数据                                     |
| key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | bytes | 初始化向量，不能设置为空       |
| aad      | 是   | bytes | 附加校验信息                                 |

- **返回值**：接口返回三个内容，一个整数、一个包含加密后的密文内容的字节列表、一个包含加密后的 tag 内容的字节列表。
  - 当接口返回的整数信息为0，代表加密成功。
  - 当接口返回的整数信息为非0，代表加密失败。

### Sm4GcmDecrypt

-	**功能描述**：方法是用于 SM4 加密算法 GCM 模式下的解密。
-	**输入参数**：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | bytes | 加密后的数据                                 |
| key      | 是   | bytes | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | bytes | 初始化向量，不能设置为空                            |
| aad      | 是   | bytes | 附加校验信息                                 |
| tag      | 是   | bytes | tag 值，即校验码                              |

- **返回值**：接口返回两个内容，一个整数和一个包含解密后的明文内容的字节列表。
  - 当接口返回的整数信息为0，代表解密成功。
  - 当接口返回的整数信息为非0，代表解密失败。

### 原生加密方式的接口调用示例

```
#coding=utf-8
import sys
import os
import time

from kms_enc_sdk import *

key = b'1234567890abcdef'
iv = b'1234567890abcdef'
aad = b'1234567890abcdef'

region = 'replace-with-real-region'
secretId = 'replace-with-real-secretId'
secretKey = 'replace-with-real-secretKey'
domainName = 'kms.tencentcloudapi.com'

ret = InitSdk(region,secretId,secretKey,domainName)
if ret != 0:
	   print('InitSdk error:',ret)
	   sys.exit(1)

ret,pubKey,priKey = Sm2GetKey()
if ret == 0:
	   print ('Sm2GetKey ok')
	
	   ret,sm2endata = Sm2Encrypt(pubKey,b'this Sm2Test')
	   if ret == 0:
		   print ('Sm2Encrypt:',sm2endata)
		   ret,sm2dedata = Sm2Decrypt(priKey,sm2endata)
		   if ret == 0:
			   print ('Sm2Decrypt:',sm2dedata)
		   else:
			   print ('Sm2Decrypt is error',ret)
	   else:
		   print ('Sm2Encrypt is error',ret)
	
	
	   ret,sign = Sm2Sign(pubKey,priKey,b'hello world')
	   if ret == 0:
		   print ('Sm2Sign is ok',sign)
		   ret = Sm2Verify(pubKey,sign,b'hello world')
		   if ret == 0:
			   print ('Sm2Verify is ok')
		   else:
			   print ('Sm2Verify is error',ret)
	   else:
		   print ('Sm2Sign is error',ret)
else:
	   print ('Sm2GetKey is error',ret)



pemInfo = "-----BEGIN PUBLIC KEY-----\n"
pemInfo += "MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE5rwEIw9e5fX87uSN7C/vy6lyEZ2R\n"
pemInfo += "gzLqWLnY8EPN1C+nJP2v4rLgaQCbHV38+vBVLimbLmdccLM69R83JxpxuQ==\n"
pemInfo += "-----END PUBLIC KEY-----\n"

ret,pubKey = Sm2PemChangeToPubkey(pemInfo.encode())
if ret == 0:
	   print('Sm2PemChangeToPubkey ok')
else:
	   print('Sm2PemChangeToPubkey error')

priKey = base64.b16decode("B8F66F0097488D8FA91FE857DFC9886356BA26A48C23F44271DD702F374174F0")

ret,digest = HashForSM3WithSM2(b'hello',pubKey,b'1234567812345678')
if ret == 0:
	   print('HashForSM3WithSM2 ok')
else:
	   print('HashForSM3WithSM2 error')

ret,sign = Sm2SignWithDigest(pubKey,priKey,digest)
if ret == 0:
	   print('Sm2SignWithDigest ok')
else:
	   print('Sm2SignWithDigest error')

ret = Sm2VerifyWithDigest(pubKey,sign,digest)
if ret == 0:
	   print('Sm2VerifyWithDigest ok')
else:
	   print('Sm2VerifyWithDigest error')


ret,hmac = Sm3Hmac(b'hello',key)
if ret == 0:
	   print ('Sm3Hmac is ok:',hmac)
else:
	   print ('Sm3Hmac is error',ret)

ret,digest = Sm3Digest(b'hello')
if ret == 0:
	   print ('Sm3Digest is ok:',digest)
else:
	   print ('Sm3Digest is error',ret)

ret,en_data = Sm4CbcEncrypt(b'this Sm4CbcTest',key,iv)
if ret == 0:
	   ret,de_data = Sm4CbcDecrypt(en_data,key,iv)
	   if ret == 0:
		   print (de_data)
	   else:
		   print ('Sm4CbcDecrypt is error',ret)
else:
	   print ('Sm4CbcEncrypt is error',ret)



ret,en_data = Sm4CtrEncrypt(b'this Sm4CtrTest',key,iv)
if ret == 0:
	   ret,de_data = Sm4CtrDecrypt(en_data,key,iv)
	   if ret == 0:
		   print (de_data)
	   else:
		   print ('Sm4CtrDecrypt is error',ret)
else:
	   print ('Sm4CtrEncrypt is error',ret)



ret,en_data = Sm4EcbEncrypt(b'this Sm4EcbTest',key)
if ret == 0:
	   ret,de_data = Sm4EcbDecrypt(en_data,key)
	   if ret == 0:
		   print (de_data)
	   else:
		   print ('Sm4EcbDecrypt is error',ret)
else:
	   print ('Sm4EcbEncrypt is error',ret)

ret,en_data,tag = Sm4GcmEncrypt(b'this Sm4GcmTest',key,iv,aad)
if ret == 0:
	   ret,de_data = Sm4GcmDecrypt(en_data,key,iv,aad,tag)
	   if ret == 0:
		   print (de_data)
	   else:
		   print ('Sm4GcmDecrypt is error',ret)
else:
	   print ('Sm4GcmEncrypt is error',ret)

```
