
Go 语言 SDK，底层使用 C 语言实现，上层通过 cgo 封装后，提供接口供 Go 语言调用。

<span id="test"></span>
## 接口返回错误码格式

大部分接口的返回值为 EncryptSDKError 类型结构体（Code：错误码，Message：错误消息）。详情如下：


| 错误码               | 错误消息                 |
| -------------------- | -------------------- |
| InvalidParameter     | 参数错误             |
| KmsAccessError       | 访问KMS出错          |
| GenerateDataKeyError | 产生DataKey错误      |
| EncryptDataKeyError  | 加密DataKey错误      |
| LocalEncryptError    | 本地加密出错         |
| UnknownError         | 未知错误             |
| CheckAlgorithmError  | 加密算法出错         |
| InvalidMessage       | 获取ProtoBuf报文出错 |
| DecryptDataKeyError  | 解密DataKey出错      |
| SignCheckFail        | 签名校验失败         |
| LocalDecryptError    | 本地解密出错         |
| KmsServiceError      | KMS服务未开通        |
| UserEditionError     | KMS未升级为旗舰版    |

### 初始化SDK接口：

#### InitSdk
- 功能描述：检验用户是否开通KMS旗舰版服务。
- 输入参数：

| 参数名称  | 必选 | 类型   | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| region    | 是   | string | CMK地域信息字符串，详见产品支持的 [**地域列表**](https://cloud.tencent.com/document/api/573/34406#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) |
| secretId  | 是   | string | 云账户API密钥ID值                                            |
| secretKey | 是   | string | 云账号API密钥Key值                                           |

- 返回值：接口返回EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回值为nil，表示初始化成功；
  - 非nil，代表初始化失败，具体查看错误码Code和错误信息Message。

> 注意:
>
>  - 需注意 SecretId 和 SecretKey 的保密存储：
>    腾讯云接口认证主要依靠 SecretID 和 SecretKey，SecretID 和 SecretKey 是用户的唯一认证凭证。业务系统需要该凭证调用腾讯云接口. 
>  - 需注意 SecretID 和 SecretKey 的权限控制：
>    建议使用子账号，根据业务需要进行接口授权的方式管控风险。

### KMS加密方式的接口说明：

#### NewMasterKey

- 功能描述：将用户首个主密钥加入主密钥信息列表。
- 参数说明：

| 参数名称   | 必选 | 类型   | 描述                                                         |
| ---------- | ---- | ------ | ------------------------------------------------------------ |
| masterKeys | 是   | []byte | 主密钥信息列表，长度根据用户加入的密钥数量来确定，每个CMK占用的空间为Region和KeyId长度。 |
| cmkRegion  | 是   | string | 主密钥（CMK）地域信息                                        |
| cmkKeyId   | 是   | string | 主密钥（CMK）的ID，从KMS控制台中查询                         |

- 返回值：接口返回EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回值为nil，表示添加成功；
  - 非nil，代表添加失败，具体查看结构体中的错误码Code和错误信息Message。

> 注意：请确保用于加密的首个主密钥，在KMS平台中是处于 **生效** 的状态。

#### AddMasterKey

- 功能描述：加入备用的用户主密钥，目的是为了灾备，当首个主密钥无法使用时，会使用的备用密钥，最多支持加入4个。
- 参数说明：

| 参数名称   | 必选 | 类型   | 描述                                                         |
| ---------- | ---- | ------ | ------------------------------------------------------------ |
| masterKeys | 是   | []byte | 主密钥信息列表，长度根据用户加入的密钥数量来确定，每个CMK占用的空间为Region和KeyId长度。 |
| cmkRegion  | 是   | string | 主密钥（CMK）地域信息                                        |
| cmkKeyId   | 是   | string | 主密钥（CMK）的ID，从KMS控制台中查询                         |

- 返回值：接口返回EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回值为nil，表示添加成功；
  - 非nil，代表添加失败，具体查看结构体中的错误码Code和错误信息Message。


#### InitKeyManager

- 功能描述：初始化KeyManager的结构体，KeyManager用来保存密钥管理相关参数，包含主密钥信息、密钥加密次数、密钥生效时间等，具体看后续参数。
- 参数说明：

| 参数名称     | 必选 | 类型                  | 描述                                                         |
| ------------ | ---- | --------------------- | ------------------------------------------------------------ |
| keyManager   | 是   | * C.struct_KeyManager | KeyManager 结构体指针，使用C语言中的KeyManager 结构体进行创建 |
| masterKeys   | 是   | string                | 主密钥（CMK）信息列表                                        |
| msgCount     | 是   | int                   | 每个缓存DataKey可加密的消息数量，加密的数量达到后，会重新向KMS后台请求，生成新的DataKey，设置为0表示没有限制使用次数。 |
| enExpiretime | 是   | int                   | 加密使用的DataKey在缓存中的有效期，单位为秒。和消息数量一起生效，消息数量超过或者超时时间达到，都会触发DataKey的替换，0表示不过期。 |
| deExpiretime | 是   | int                   | 解密使用的DataKey缓存的有效期，单位为秒，0表示不过期。       |
| secretId     | 是   | string                | 云账户API密钥ID值                                            |
| secretKey    | 是   | string                | 云账号API密钥Key值                                           |

- 返回值：接口返回EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回值为nil，表示初始化成功；
  - 非nil，代表初始化失败，具体查看结构体中的错误码Code和错误信息Message。

#### Encrypt

- 功能描述：使用kms平台创建的DataKey，进行本地数据加密。
- 输入参数：

| 参数名称          | 必选 | 类型                  | 描述                                                         |
| ----------------- | ---- | --------------------- | ------------------------------------------------------------ |
| source            | 是   | []byte                | 待加密的明文数据                                             |
| keyManager        | 是   | * C.struct_KeyManager | 已经初始化的KeyManager结构体指针                             |
| masterKeys        | 是   | string                | 主密钥（CMK）信息列表                                        |
| algorithm         | 是   | C.enum_Algorithm      | 算法枚举值，参照后面算法列表                                 |
| encryptionContext | 是   | string                | 用于标识DataKey的辅助字段，key/value对的json字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"} |
| blockSize         | 是   | int                   | 0 表示加密时不分块加密，非0表示分块加密以及分块大小，单位 byte |
| header            | 是   | * C.struct_MsgHead    | 头部数据结构体，用于返回本次加密的一些基本信息，具体请看关于结构体的描述 |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表加密成功，加密后的密文内容在返回的字符数组中；
  - 非nil，代表加密失败，具体查看结构体中的错误码Code和错误信息Message。

> 注意：加密后的数据，会加入DataKey相关信息，只能使用KMS密钥保护方式的接口进行解密。

#### Decrypt

- 功能描述：方法用于解密密文，得到明文数据。
- 输入参数：

| 参数名称   | 必选 | 类型                  | 描述                                                         |
| ---------- | ---- | --------------------- | ------------------------------------------------------------ |
| source     | 是   | []byte                | 加密后的数据                                                 |
| keyManager | 是   | * C.struct_KeyManager | 已经初始化的KeyManager结构体指针                             |
| header     | 是   | * C.struct_MsgHead    | 头部数据结构体，用于返回本次解密的一些基本信息，具体请看关于结构体的描述 |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表解密成功，解密后的明文内容在返回的字符数组中；
  - 非nil，代表解密失败，具体查看结构体中的错误码Code和错误信息Message。

#### C.enum_Algorithm 支持的加密算法列表：

| 枚举值                       | 数值 | 说明                            |
| ---------------------------- | ---- | ------------------------------- |
| C.SM4_CBC_128_WITH_SIGNATURE | 1    | 使用SM3HAC签名的SM4 CBC模式     |
| C.SM4_CBC_128                | 2    | 不使用签名的SM4 CBC模式加密     |
| C.SM4_GCM_128_WITH_SIGNATURE | 3    | 使用SM3HAC签名的SM4 GCM模式     |
| C.SM4_GCM_128                | 4    | 不使用签名的SM4 GCM模式加密算法 |
| C.SM4_CTR_128_WITH_SIGNATURE | 5    | 使用SM3HAC签名的SM4 CTR模式     |
| C.SM4_CTR_128                | 6    | 不使用签名的SM4 CTR模式         |
| C.SM4_ECB_128_WITH_SIGNATURE | 7    | 使用SM3HAC签名的SM4 ECB模式     |
| C.SM4_ECB_128                | 8    | 不使用签名的SM4 ECB模式         |

#### C.EncryptedDataKey结构体说明：

| 参数名称  | 类型     | 说明                                 |
| --------- | -------- | ------------------------------------ |
| cmkRegion | C.char * | 主密钥（CMK）地域信息                |
| cmkKeyId  | C.char * | 主密钥（CMK）的ID，从KMS控制台中查询 |
| dataKey   | C.char * | 存储的datakey对应的密文              |

#### C.struct_MsgHead结构体说明：

| 参数名称          | 类型                        | 说明                                                         |
| ----------------- | --------------------------- | ------------------------------------------------------------ |
| algorithm         | C.enum_Algorithm            | 算法枚举值，参照上面的加密算法列表                           |
| encryptionContext | C.char *                    | 用于标识DataKey的辅助字段，key/value对的json字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"} |
| dataKeyNum        | C.int                       | 使用的加密后DataKey数量，和有效的主密钥(CMK)数量相关，由各个地域的主密钥加密产生 |
| dataKey           | Array of C.EncryptedDataKey | DataKey的信息列表，包含的字段参照上面的EncryptedDataKey结构体说明 |
| blockType         | C.enum_BlockType            | 密文加密分块的枚举值，用于标识该密文是否被分块，参照下面的BlockType枚举值说明 |
| blockLength       | C.int                       | 分块的长度                                                   |

#### KMS加密方式接口调用示例：

```
package main

/*
#include "kms_enc_sdk.h"
*/
import "C"

import (
    "fmt"
//    "time"
//    "encoding/hex"
)

func ECBEnAndDeWithSignTest(){
    masterKeys := make([]byte, 1024)
	NewMasterKey(masterKeys,"ap-guangzhou","replace-with-realkeyid")
	AddMasterKey(masterKeys,"ap-shanghai","replace-with-realkeyid")
	
	f := &C.struct_KeyManager{}
	header_en := &C.struct_MsgHead{}
	header_de := &C.struct_MsgHead{}

	error := InitKeyManager(f,string(masterKeys),0,0,0,"replace-with-real-secretId"," replace-with-real-secretKey ")
	if ( nil != error ){
		fmt.Println(error.Error())
		return 
	}
	
	source := []byte("hello world!")
	encryptionContext := "{\"test\":\"nihao\"}"
	
	var algorithm C.enum_Algorithm = C.SM4_CBC_128_WITH_SIGNATURE
	cipher,err_en := Encrypt(source,f,string(masterKeys),algorithm,encryptionContext,0,header_en)
	if err_en != nil {
		fmt.Println(err_en.Error())
		return
	}
	plainTexttest,err_de := Decrypt(cipher,f,header_de)
	if err_de != nil {
		fmt.Println(err_de.Error())
		return
	}
	fmt.Println(string(plainTexttest))
}

func main() {
    error := InitSdk("ap-guangzhou","replace-with-real-secretId","replace-with-real-secretKey ")
    if(nil != error){
        fmt.Println(error.Eoor())
        return
    }

	ECBEnAndDeWithSignTest()

}

```

### 原生加密方式的接口说明：

原生加密方式对应的服务也需要升级为旗舰版，与KMS密钥保护方式相比，原生加密方式需要用户自己生成加密密钥进行加解密，由用户保证密钥的安全性。出于安全与合规的考虑，建议用户使用KMS密钥保护方式。
其中CTR模式加密没有填充，其他的模式加密采用PKCS#7标准进行填充。

#### Sm2Sign

- 功能描述：使用SM2算法进行签名。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubKey   | 是   | []byte | 未编码的公钥内容，数据长度固定为64字节 |
| priKey   | 是   | []byte | 未编码的私钥内容，数据长度固定为32字节 |
| msg      | 是   | []byte | 原文数据                               |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表签名成功，签名内容在返回的字符数组中；
  - 非nil，代表签名失败，具体查看结构体中的错误码Code和错误信息Message。

> 注意：公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

#### Sm2Verify

- 功能描述：使用SM2算法进行验签。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubkey   | 是   | []byte | 未编码的公钥内容，数据长度固定为64字节 |
| msg      | 是   | []byte | 原文数据                               |
| sig      | 是   | []byte | 签名后的数据                           |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，表示验签成功；
  - 非nil，代表验签失败，具体查看结构体中的错误码Code和错误信息Message。

> 注意：公钥长度为固定长度64字节，用户如果输入长度不一致的数据，可能导致内存访问异常。

#### Sm2Encrypt

- 功能描述：使用SM2算法进行加密。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                               |
| -------- | ---- | ------ | ---------------------------------- |
| pubkey   | 是   | []byte | 未编码的公钥内容，数据长度为64字节 |
| source   | 是   | []byte | 源数据                             |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表加密成功，加密后的密文内容在返回的字符数组中；
  - 非nil，代表加密失败，具体查看结构体中的错误码Code和错误信息Message。

> 注意：SM2加密适用于小数据的场景，不建议加密超过256k的数据。

#### Sm2Decrypt

-	功能描述：使用SM2算法进行解密
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| prikey   | 是   | []byte | 未编码的私钥内容，数据长度固定为32字节 |
| source   | 是   | []byte | 加密后的数据                           |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表解密成功，解密后的明文内容在返回
  - 的字符数组中；
  - 非nil，代表解密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm3Hmac

-	功能描述：使用SM3哈希运算Hmac计算。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述               |
| -------- | ---- | ------ | ------------------ |
| data     | 是   | []byte | 原文数据           |
| hmacKey  | 是   | []byte | 计算Hmac的密钥内容 |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表Hmac计算成功，Hmac内容在返回的字符数组中；
  - 非nil，代表Hmac计算失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4CbcEncrypt/Sm4CtrEncrypt

-	功能描述：方法是用于SM4加密算法CBC、CTR模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 原文数据                                     |
| Key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |
| iv       | 是   | []byte | 初始化向量，固定为128位(16字节)              |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表加密成功，加密后的密文内容在返回的字符数组中；
  - 非nil，代表加密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4CbcDecrypt/Sm4CtrDecrypt

-	功能描述：方法是用于SM4加密算法CBC、CTR模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 加密后的数据                                 |
| Key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |
| iv       | 是   | []byte | 初始化向量，固定为128位(16字节)              |

- 返回值：接口返回两个内容，一个字符数组和 一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表解密成功，解密后的明文内容在返回的字符数组中；
  - 非nil，代表解密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4EcbEncrypt

-	功能描述：方法是用于SM4加密算法ECB模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 原文数据                                     |
| Key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表加密成功，加密后的密文内容在返回的字符数组中；
  - 非nil，代表加密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4EcbDecrypt

-	功能描述：方法是用于SM4加密算法ECB模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 加密后的数据                                 |
| Key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表解密成功，解密后的明文内容在解密后的字符数组中；
  - 非nil，代表解密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4GcmEncrypt

-	功能描述：方法是用于SM4加密算法GCM模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 原文数据                                     |
| key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |
| iv       | 是   | []byte | 初始化向量，固定为128位(16字节)              |
| aad      | 是   | []byte | 附加校验信息                                 |
| tag      | 是   | []byte | tag值，即校验码                              |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表加密成功，加密后的密文内容在返回的字符数组中；
  - 非nil，代表加密失败，具体查看结构体中的错误码Code和错误信息Message。

#### Sm4GcmDecrypt

-	功能描述：方法是用于SM4加密算法GCM模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | []byte | 加密后的数据                                 |
| key      | 是   | []byte | 用户自定义的SM4密钥，长度固定为128位(16字节) |
| iv       | 是   | []byte | 初始化向量                                   |
| aad      | 是   | []byte | 附加校验信息                                 |
| tag      | 是   | []byte | tag值，即校验码                              |

- 返回值：接口返回两个内容，一个字符数组和一个EncryptSDKError类型结构体，具体请查看开头说明。
  - 当接口返回的结构体信息为nil，代表解密成功，解密后的明文内容在解密后的字符数组中；
  - 非nil，代表解密失败，具体查看结构体中的错误码Code和错误信息Message。

#### 原生加密方式的接口调用示例：

```
package main

import (
	"fmt"
	"encoding/hex"
)

func Sm4EcbTest(){
	key := []byte("1234567890abcdef")
	msg := []byte("hello world!")
	
	cipherText,enerr := Sm4EcbEncrypt(msg,key)
	if enerr != nil {
		fmt.Println(enerr.Error())
	}else{
		plainText,deerr := Sm4EcbDecrypt(cipherText,key)
		if deerr != nil {
		fmt.Println(deerr.Error())
		}else{
			fmt.Print("Sm4EcbDecrypt:")
			fmt.Println(string(plainText))
		}
	}
}

func main(){
	error := InitSdk("ap-guangzhou","replace-with-real-secretId","replace-with-real-secretKey")
	if (nil != error){
		fmt.Println("InitSdk err",error.Error())
		return 
	}
	fmt.Println("InitSdk is ok")
	
	Sm4CbcTest()
	
}
```
