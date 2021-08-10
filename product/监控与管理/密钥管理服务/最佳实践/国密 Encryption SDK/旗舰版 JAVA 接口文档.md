## 说明
Java 语言 SDK，底层通过 C 实现算法，通过 jni 封装后，作为本地接口供 Java 语言调用。

## 错误码
| 异常码               | 说明                             |
| -------------------- | -------------------------------- |
| 0                    | 正常返回                         |
| 10010                   | sdk 初始化错误                         |
| 10011                   | DataKeyManager 无效，不能为 null                   |
| 10013                   | 加密上下文超过最大长度,最大长度为1024                     |
| 10012                   | 算法不支持                       |
| 10014                   | 解密密钥获取失败                |
| 10015                   | 加密密钥过期，重置密钥                |
| 10016                   | 参数不能为空             |
| 10017                   | 无效的 key                     |
| 10018                   | 无效的 iv           |
| 10019                  | aad 不能为 null           |
| 10020                  | 密钥缓存初始化错误                |
| 20011                  | 数据密钥创建异常                |
| 20012                  | 签名检查异常       |
| 20013                  | 腾讯 KMS 加密或解密异常                        |
| 20014                  | 无效参数，主密钥个数超过最大值,最大值为5                   |
| 20015                  | 域名为 null，且环境变量未设置域名              |
| 20016                  | 主密钥 keyId 或 region 为空              |

## 初始化 SDK 接口

### EncryptSdk.initSdk

- 功能描述：检验用户是否开通 KMS 旗舰版服务。
- 输入参数：

| 参数名称  | 必选 | 类型   | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| region    | 是   | String | CMK 地域信息字符串，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/573/34406#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) |
| secretId  | 是   | String | 云账户 API 密钥 ID 值                                            |
| secretKey | 是   | String | 云账号 API 密钥 Key 值                                           |
| domainName | 是   | String | 域名信息字符串                                           |

- 返回值：接口返回一个整数。
  - 当接口返回值为0，表示初始化成功。
  - 当接口返回值非0，代表初始化失败。

>!
> - 需注意 SecretId 和 SecretKey 的保密存储： 腾讯云接口认证主要依靠 SecretID 和 SecretKey，SecretID 和 SecretKey 是用户的唯一认证凭证。
>- 业务系统需要该凭证调用腾讯云接口。
> - 需注意 SecretID 和 SecretKey 的权限控制：建议使用子账号，根据业务需要进行接口授权的方式管控风险。
> - 需注意 domainName 的设置：如果 domainName 入参为""，则从环境变量 TENCENT_SDK_DOMAIN 中读取值，反之，则以入参为准。

## KMS加密方式的接口说明
### EncryptSdk.createKeyManager
- 功能描述：初始化用户的主密钥，包含主密钥信息、密钥加密次数、密钥生效时间等，具体看后续参数。
- 参数说明：

| 参数名称     | 必选 | 类型                  | 描述                                                         |
| ------------ | ---- | --------------------- | ------------------------------------------------------------ |
| masterKey    | 是   | List<MasterKey>                  | 主密钥（CMK）信息列表                                        |
| msgCount     | 是   | KeyCache                   | 每个缓存 DataKey 可加密的消息数量，加密的数量达到后，会重新向 KMS 后台请求，生成新的 DataKey，设置为0表示没有限制使用次数。 |
| enExpiretime | 是   | KeyCache                   | 加密使用的 DataKey 在缓存中的有效期，单位为秒。和消息数量一起生效，消息数量超过或者超时时间达到，都会触发 DataKey 的替换，0表示不过期。 |
| deExpiretime | 是   | KeyCache                   | 解密使用的 DataKey 缓存的有效期，单位为秒，0表示不过期。       |
| secretId     | 是   | String                   | 云账户 API 密钥 ID 值                                            |
| secretKey    | 是   | String                   | 云账号 API 密钥 Key 值                                           |

- 返回值：接口返回 DataKeyManager 对象。
  - 当接口返回值正常，表示初始化成功。
  - 当接口返回值抛异常，代表初始化失败。

> ! 初始化 keyManager 对象方法：
>- EncryptSdk.createKeyManager（List<MasterKey> masterKey, KeyCache keyCache,String secretId, String secretKey）。
>- masterKey:主密钥的集合，最多5个主密钥。
>- keyChe：密钥缓存对象，三个成员变量 msgCount、enExpiretime、deExpiretime。

### EncryptSdk.Encrypt
- 功能描述：使用 KMS 平台创建的 DataKey，进行本地数据加密。
- 输入参数：

| 参数名称          | 必选 | 类型                  | 描述                                                         |
| ----------------- | ---- | --------------------- | ------------------------------------------------------------ |
| masterKeys        | 是   | List<MasterKey>                  | 主密钥（CMK）信息列表                                        |
| source            | 是   | byte[]                 | 待加密的明文数据                                             |
| keyManager        | 是   | kms_enc_sdk.KeyManager | 已经初始化的 KeyManager 结构体指针                             |
| algorithm         | 是   | KmsSdk.Algorithm             | 算法枚举值，参照后面算法列表                                 |
| encryptionContext | 是   | String                   | 用于标识 DataKey 的辅助字段，key/value 对的 json 字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"} |
| blockSize         | 是   | int                   | 0 表示加密时不分块加密，非0表示分块加密以及分块大小，单位 byte |

- 返回值：接口返回 EncryptResult 对象。
  - 当接口返回值正常，代表加密成功。
  - 当接口返回值抛异常，代表加密失败。

>! 加密后的数据，会加入 DataKey 相关信息，只能使用 KMS 密钥保护方式的接口进行解密。

### EncryptSdk.Decrypt
- 功能描述：方法用于解密密文，得到明文数据。
- 输入参数：

| 参数名称   | 必选 | 类型                  | 描述                                                         |
| ---------- | ---- | --------------------- | ------------------------------------------------------------ |
| source     | 是   | byte[]                 | 加密后的数据                                                 |
| keyManager | 是   | DataKeyManager | 已经初始化的 KeyManager 对象                             |

- 返回值：接口返回 DecryptResult 对象。
  - 当接口返回值正常，代表解密成功。
  - 当接口返回值抛异常，代表解密失败。

### Algorithm 支持的加密算法列表

| 枚举值                       | 数值 | 说明                            |
| ---------------------------- | ---- | ------------------------------- |
| SM4_CBC_128_WITH_SIGNATURE | 1    | 使用 SM3HA C签名的 SM4 CBC 模式     |
| SM4_CBC_128                | 2    | 不使用签名的 SM4 CBC 模式加密     |
| SM4_GCM_128_WITH_SIGNATURE | 3    | 使用 SM3HAC 签名的 SM4 GCM 模式     |
| SM4_GCM_128                | 4    | 不使用签名的 SM4 GCM 模式加密算法 |
| SM4_CTR_128_WITH_SIGNATURE | 5    | 使用 SM3HAC 签名的 SM4 CTR 模式     |
| SM4_CTR_128                | 6    | 不使用签名的 SM4 CTR 模式         |
| SM4_ECB_128_WITH_SIGNATURE | 7    | 使用 SM3HAC 签名的 SM4 ECB 模式     |
| SM4_ECB_128                | 8    | 不使用签名的 SM4 ECB 模式         |

### 原生加密方式接口说明
- 原生加密方式对应的服务也需要升级为旗舰版，与 KMS 密钥保护方式相比，原生加密方式需要用户自己生成加密密钥进行加解密，来保证密钥的安全性。出于安全与合规的考虑，建议用户使用 KMS 密钥保护方式。
- 其中CTR模式加密没有填充，其他的模式加密采用 PKCS#7 标准进行填充。

### EncryptSdk.genSm2KeyPair
- 功能描述：使用 SM2 算法生成密钥对。
- 输入参数：无需填充输入参数。
- 返回值：接口返回一个字节数组（包含生成的公钥值、私钥值）。
  - 当接口返回返回值正常，表示获取密钥对成功。
  - 当接口返回值抛异常，代表获取失败。

### EncryptSdk.sm2Sign
- 功能描述：使用 SM2 算法进行签名。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubKey   | 是   | byte[] | 公钥内容，数据长度固定为64字节 |
| priKey   | 是   | byte[] | 私钥内容，数据长度固定为32字节 |
| source   | 是   | byte[] | 原文数据                               |

- 返回值：接口返回一个包含签名内容的字节数组。
  - 当接口返回值正常，代表签名成功。
  - 当接口返回值抛异常，代表签名失败。

>! 公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

### EncryptSdk.sm2Verify
- 功能描述：使用 SM2 算法进行验签。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| pubkey   | 是   | byte[] | 公钥内容，数据长度固定为64字节 |
| sign     | 是   | byte[] | 签名后的数据                           |
| source   | 是   | byte[] | 原文数据                               |

- 返回值：接口返回一个 boolean 值。
  - 当接口返回值为 true，表示验签成功。
  - 当接口返回值非 true，代表验签失败。

>! 公钥长度为固定长度64字节，用户如果输入长度不一致的数据，可能导致内存访问异常。

### EncryptSdk.sm2Encrypt
- 功能描述：使用 SM2 算法进行加密。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                               |
| -------- | ---- | ------ | ---------------------------------- |
| pubkey   | 是   | byte[] | 公钥内容，数据长度为64字节 |
| source   | 是   | byte[] | 源数据                             |

- 返回值：接口返回一个包含加密后的密文内容的字节数组。
  - 当接口返回值正常，代表加密成功。
  - 当接口返回值抛异常，代表加密失败。
 >! SM2 加密适用于小数据的场景，不建议加密超过256k的数据。

### EncryptSdk.sm2Decrypt
-	功能描述：使用 SM2 算法进行解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| prikey   | 是   | byte[] | 私钥内容，数据长度固定为32字节 |
| source   | 是   | byte[] | 加密后的数据                           |

- 返回值：接口返回一个包含解密后的明文内容的字节数组。
  - 当接口返回值正常，代表解密成功。
  - 当接口返回值抛异常，代表解密失败。

### EncryptSdk.sm2PemChangeToPubkey
- 功能描述：对 pem 格式的公钥内容进行转换。
- 输入参数：

| 参数名称      | 必选 | 类型   | 描述              |
| ------------- | ---- | ------ | ----------------- |
| pemPubKeyInfo | 是   | byte[] | pem 格式的公钥信息 |

- 返回值：接口返回一个包含转换后的公钥内容的字节数组。
  - 当接口返回值正常，代表转换成功。
  - 当接口返回值抛异常，代表转换失败。

### EncryptSdk.hashForSM3WithSM2

- 功能描述：使用 Sm2GetKey 接口生成的公钥，并基于 SM3 算法生成信息摘要。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                   |
| -------- | ---- | ------ | -------------------------------------- |
| msg      | 是   | byte[] | 原文数据                               |
| pubKey   | 是   | byte[] | 公钥内容，数据长度固定为64字节 |
| id       | 是   | byte[] | ID 值                                   |

- 返回值：接口返回一个包含生成的摘要内容的字节数组。
  - 当接口返回值正常，代表摘要生成成功。
  - 当接口返回值抛异常，代表摘要生成失败。

### EncryptSdk.sm2SignWithDigest

- 功能描述：使用本地生成的消息摘要生成签名
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                     |
| -------- | ---- | ------ | ---------------------------------------- |
| pubKey   | 是   | byte[] | 公钥内容，数据长度固定为64字节   |
| priKey   | 是   | byte[] | 私钥内容，数据长度固定为32字节   |
| digest   | 是   | byte[] | HashForSM3WithSM2 生成的摘要信息内容 |

- 返回值：接口返回一个包含生成的签名内容的字节数组。
  - 当接口返回值正常，代表签名成功。
  - 当接口返回值抛异常，代表摘要签名失败。

### EncryptSdk.sm2VerifyWithDigest

- 功能描述：通过生成的摘要内容进行验签。
- 输入参数：

| 参数名称 | 必选 | 类型   | 描述                                     |
| -------- | ---- | ------ | ---------------------------------------- |
| pubKey   | 是   | byte[] | 公钥内容，数据长度固定为64字节   |
| sig      | 是   | byte[] | Sm2SignWithDigest 生成的签名内容                               |
| digest   | 是   | byte[] | HashForSM3WithSM2 生成的摘要信息内容 |

- 返回值：接口返回一个整数。
  - 当接口返回的整数信息为0，代表验签成功。
  - 当接口返回的整数信息为非0，代表摘要验签失败。

### EncryptSdk.sm3Hmac

-	功能描述：使用 SM3 哈希运算 Hmac 计算。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述               |
| -------- | ---- | ------ | ------------------ |
| source     | 是   | byte[] | 原文数据           |
| hmacKey  | 是   | byte[] | 计算 Hmac 的密钥内容 |

- 返回值：接口返回一个包含 Hmac 内容的字节数组。
  - 当接口返回值正常，代表 Hmac 计算成功。
  - 当接口返回值抛异常，代表 Hmac 计算失败。

### EncryptSdk.sm3Digest
-	功能描述：使用 SM3 生成摘要。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述               |
| -------- | ---- | ------ | ------------------ |
| source     | 是   | byte[] | 原文数据           |

- 返回值：接口返回一个包含摘要内容的字节数组。
  - 当接口返回值正常，代表生成摘要成功。
  - 当接口返回值抛异常，代表生成摘要失败。

### EncryptSdk.sm4CbcEncrypt/EncryptSdk.sm4CtrEncrypt
-	功能描述：方法是用于 SM4 加密算法 CBC、CTR 模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 原文数据                                     |
| Key      | 是   | byte[] | 用户自定义的SM4密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | byte[] | 初始化向量，固定为128位(16字节)，不能设置为空              |

- 返回值：接口返回一个包含加密后的密文内容的字节数组。
  - 当接口返回值正常，代表加密成功。
  - 当接口返回值抛异常，代表加密失败。

### EncryptSdk.sm4CbcDecrypt/EncryptSdk.sm4CtrDecrypt
-	功能描述：方法是用于 SM4 加密算法 CBC、CTR 模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 加密后的数据                                 |
| Key      | 是   | byte[] | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | byte[] | 初始化向量，固定为128位(16字节)，不能设置为空              |

- 返回值：接口返回一个包含解密后的明文内容的字节数组。
  - 当接口返回值正常，代表解密成功。
  - 当接口返回值抛异常，代表解密失败。

### EncryptSdk.sm4EcbEncrypt
-	功能描述：方法是用于 SM4 加密算法 ECB 模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 原文数据                                     |
| Key      | 是   | byte[] | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |

- 返回值：接口返回一个包含加密后的密文内容的字节数组。
  - 当接口返回值正常，代表加密成功。
  - 当接口返回值抛异常，代表加密失败。

### EncryptSdk.sm4EcbDecrypt
-	功能描述：方法是用于 SM4 加密算法 ECB 模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 加密后的数据                                 |
| Key      | 是   | byte[] | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |

- 返回值：接口返回一个包含解密后的明文内容的字节数组。
  - 当接口返回值正常，代表解密成功。
  - 当接口返回值抛异常，代表解密失败。

### EncryptSdk.sm4GcmEncrypt
-	功能描述：方法是用于 SM4 加密算法 GCM 模式下的加密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 原文数据                                     |
| key      | 是   | byte[] | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | byte[] | 初始化向量，不能设置为空             |
| aad      | 是   | byte[] | 附加校验信息                                 |

- 返回值：接口返回一个 Map 对象。
  - 当接口返回值正常，代表加密成功。
  - 当接口返回值抛异常，代表加密失败。

### EncryptSdk.sm4GcmDecrypt
-	功能描述：方法是用于 SM4 加密算法 GCM 模式下的解密。
-	输入参数：

| 参数名称 | 必选 | 类型   | 描述                                         |
| -------- | ---- | ------ | -------------------------------------------- |
| source   | 是   | byte[] | 加密后的数据                                 |
| key      | 是   | byte[] | 用户自定义的 SM4 密钥，长度固定为128位(16字节)，不能设置为空 |
| iv       | 是   | byte[] | 初始化向量，不能设置为空                                   |
| aad      | 是   | byte[] | 附加校验信息                                 |
| tag      | 是   | byte[] | tag 值，即校验码                              |

- 返回值：接口返回一个包含解密后的明文内容的字节数组。
  - 当接口返回值正常，代表解密成功。
  - 当接口返回值抛异常，代表解密失败。

### 接口调用示例
>?接口示例适用以下加密方式:
>- KMS 方式加解密
>- 原生加密方式

```
import com.ciphergateway.sdk.EncryptSdk;
import com.ciphergateway.sdk.exception.SdkException;
import com.ciphergateway.sdk.exception.SdkExceptionEnum;
import com.ciphergateway.sdk.vo.*;
import kmsmsg.KmsSdk;

import javax.xml.bind.DatatypeConverter;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import java.util.List;
import java.util.Map;


/**
 * @ClassName : TestSdk
 * @Description : ${description}
 * @Author : crisp
 * @Date: 2020-06-28 14:25
 */
public class DemoSdkTest {

    public  static String secretId = "replace-with-real-secretId";
    public static String secretKey = "replace-with-real-secretKey";
    public static String keyID1_guangzhou="replace-with-realkeyid";
    public static String keyID2_shanghai="replace-with-realkeyid";

    public static String algorithmPath = "real-algorithm-path"; //libkms_enc_sdk_jni.so文件路径,例如：/root/user/kms_enc_sdk_java/lib/linux/libkms_enc_sdk_jni.so

    private static int ret = 0;

    static {


        //初始化sdk，此处启动程序只需执行一次，返回０说明初始化成功
        try {
            ret = EncryptSdk.initSdk("ap-shanghai", secretId, secretKey, null);
        } catch (SdkException e) {
            e.printStackTrace();
        }
        System.out.println("init encrypt worker status is " + ret);
        //linux 环境下加载方式
        System.load(algorithmPath);

        //windows环境下配置方式,需要把windows库的路径加入到系统的环境变量（path环境变量）中
        //System.load("D:\\java\\tencent-kms-sdk\\src\\main\\resources\\lib\\windows\\libkms_enc_sdk_jni.dll");

    }

    public static void main(String[] args) throws UnsupportedEncodingException, SdkException {
        if (ret != 0) {
            throw new SdkException(new ErrorInfo(SdkExceptionEnum.TENCENT_DOMAIN_NAME_NULL.message, null).toString());
        }

        MasterKey key1 = new MasterKey();
        key1.setKeyId(keyID1_guangzhou);
        key1.setRegion("ap-guangzhou");

        MasterKey key2 = new MasterKey();
        key2.setKeyId(keyID2_shanghai);
        key2.setRegion("ap-shanghai");

        //构建datamanager所需要的参数
        List<MasterKey> list = Arrays.asList(key1, key2, key1, key2, key1);

        DataKeyManager dataKeyManager = null;
        try {
            dataKeyManager = EncryptSdk.createKeyManager(list, new KeyCache(2, 0, 0), secretId, secretKey);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //System.out.println(" error occur");
        }

        String cipherBlob = "test1234567890";

        long start = System.currentTimeMillis();

        String encryptionContext = "{\"ceshi\":\"fgdfgdfgdg\"}";
        //Test_CBCEnAndDe_withEncryptionContextNotjosnformatParams();
        for (int i = 0; i < 5; i++) {

            // encryptionContext =  Constant.EMPTY;
            //encryptionContext = "afa";
            EncryptResult result = null;
            try {
                result = EncryptSdk.Encrypt(list, cipherBlob.getBytes(), dataKeyManager, KmsSdk.Algorithm.SM4_GCM_128, encryptionContext, 7);
                // System.out.println("------------result------------"+result);
            } catch (Exception e) {
                e.printStackTrace();
            }


            try {
                DecryptResult decryptResult = EncryptSdk.Decrypt(result.getCipher(), dataKeyManager);
                if (new String(decryptResult.getPlainText()).equals(cipherBlob)) {
                    continue;
                } else {
                    System.out.println("decrypt faild");
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("encrypt 5 times costs: "+(end-start)/1000 +"  seconds");


        System.out.println("----------------------------------------------------------------------------------------------------------------------------------------------");


        System.out.println("begin to en");
        com.ciphergateway.encryptsdk.EncryptSdk enf = new com.ciphergateway.encryptsdk.EncryptSdk();

        String data = "1234567890123456";
        String key = "0123456789abcdef";
        String iv = "0123456789abcdef";
        String aad = "0123456789abcdef";

        String region = "ap-guangzhou";

        byte[] pubkey = {(byte) 0xcd, (byte) 0x70, (byte) 0x6a, (byte) 0xc4, (byte) 0xc6, (byte) 0x00, (byte) 0x7c, (byte) 0x67, (byte) 0xed, (byte) 0xa7, (byte) 0xdc, (byte) 0xa7, (byte) 0x3f, (byte) 0x8a, (byte) 0xed, (byte) 0x55, (byte) 0x2d, (byte) 0x75, (byte) 0x12, (byte) 0x21, (byte) 0xb5, (byte) 0x8a, (byte) 0x81, (byte) 0xaa, (byte) 0xbb, (byte) 0xd6, (byte) 0xe2, (byte) 0x85, (byte) 0x15, (byte) 0xa5, (byte) 0x23, (byte) 0xf3, (byte) 0x5e, (byte) 0xe5, (byte) 0x05, (byte) 0x9d, (byte) 0xf0, (byte) 0x4b, (byte) 0x1b, (byte) 0xee, (byte) 0x7e, (byte) 0x90, (byte) 0x21, (byte) 0x50, (byte) 0x58, (byte) 0x07, (byte) 0x3a, (byte) 0xd5, (byte) 0x63, (byte) 0x9f, (byte) 0x0a, (byte) 0xd0, (byte) 0x2e, (byte) 0x33, (byte) 0x67, (byte) 0xe5, (byte) 0xd9, (byte) 0x71, (byte) 0x66, (byte) 0xd9, (byte) 0x57, (byte) 0xeb, (byte) 0x1a, (byte) 0xb1};
        byte[] prikey = {(byte) 0x55, (byte) 0x13, (byte) 0xa7, (byte) 0xe3, (byte) 0x18, (byte) 0x4f, (byte) 0x28, (byte) 0x55, (byte) 0xd3, (byte) 0x20, (byte) 0x9a, (byte) 0x2f, (byte) 0x5e, (byte) 0x24, (byte) 0xd3, (byte) 0x6c, (byte) 0xa9, (byte) 0xb2, (byte) 0x8e, (byte) 0x13, (byte) 0x3d, (byte) 0xa9, (byte) 0x74, (byte) 0xb8, (byte) 0xbc, (byte) 0xff, (byte) 0xfa, (byte) 0xa9, (byte) 0x7e, (byte) 0x8e, (byte) 0x0a, (byte) 0x5a};


        //sm4　ctr enc
        byte[] enctrdata = EncryptSdk.sm4CtrEncrypt(data.getBytes(), key.getBytes(), iv.getBytes());
        ////sm4　ctr dec
        byte[] dectrdata = EncryptSdk.sm4CtrDecrypt(enctrdata, key.getBytes(), iv.getBytes());
        System.out.println("Sm4CtrDecrypt:" + new String(dectrdata));


        //sm4　cbc enc


        byte[] encbcdata = EncryptSdk.sm4CbcEncrypt(data.getBytes(), key.getBytes(), iv.getBytes());
        //sm4　cbc dec
        byte[] decbcdata = EncryptSdk.sm4CbcDecrypt(encbcdata, key.getBytes(), iv.getBytes());
        String result = new String(decbcdata);
        System.out.println("Sm4CbcDecrypt:" + result);


        //sm4　ecb enc
        byte[] enecbdata = EncryptSdk.sm4EcbEncrypt(data.getBytes(), key.getBytes());
        //sm4　ecb dec
        byte[] deecbdata = EncryptSdk.sm4EcbDecrypt(enecbdata, key.getBytes());
        System.out.println("Sm4EcbEncrypt:" + new String(deecbdata));


        //sm4 gcm enc
        Map<String, byte[]> map = EncryptSdk.sm4GcmEncrypt(data.getBytes(), key.getBytes(), iv.getBytes(), "".getBytes());
        if (!map.isEmpty()) {
            byte[] realdata = map.get("data");
            byte[] tagdata = map.get("tag");

            //sm4 gcm dec
            byte[] degcmdata = EncryptSdk.sm4GcmDecrypt(realdata, key.getBytes(), iv.getBytes(), "".getBytes(), tagdata);
            System.out.println("Sm4GcmDecrypt:" + new String(degcmdata));
        }


        //sm3计算hmac 值
        byte[] hmac = EncryptSdk.sm3Hmac(data.getBytes(), key.getBytes());
        System.out.print("Sm3Hmac(len):");
        System.out.println(hmac.length);

        //生成公私钥对，字节数组长度是９６字节，前６４字节为公钥，后３２字节为私钥
        byte[] keyPair = EncryptSdk.genSm2KeyPair();
        System.out.println("The derived key --> " + DatatypeConverter.printHexBinary(keyPair));

        String plainmsg = "hello, bingo";
        System.out.println("the input message " + plainmsg);
        //sm2 加密

        byte[] sm2encbyte = EncryptSdk.sm2Encrypt(Arrays.copyOf(keyPair, 64), plainmsg.getBytes());
        System.out.println("sm2 encrypt --> " + DatatypeConverter.printHexBinary(sm2encbyte));

        //sm2解密
        byte[] sm2decbyte = EncryptSdk.sm2Decrypt(Arrays.copyOfRange(keyPair, keyPair.length - 32, keyPair.length), sm2encbyte);

        System.out.println("sm2 decrypt --> " + new String(sm2decbyte));


        //签名
        byte[] sign = EncryptSdk.sm2Sign(pubkey, prikey, data.getBytes());


        //验证签名

        boolean isRight = EncryptSdk.sm2Verify(pubkey, sign, data.getBytes());

        System.out.println(isRight);


        System.out.println("=============================2021-02-24========================================");

        //sm3 digest
        byte[] digest_message = EncryptSdk.sm3Digest(data.getBytes());
        System.out.println("digest message " + DatatypeConverter.printHexBinary(digest_message));


        String smid = "1234567812345678";

        byte[] sm2sm3hash = EncryptSdk.hashForSM3WithSM2(data.getBytes(), pubkey, smid.getBytes());
        System.out.println("HashForSM3WithSM2  hash " + DatatypeConverter.printHexBinary(sm2sm3hash));


        byte[] sm2digest = EncryptSdk.sm2SignWithDigest(pubkey, prikey, sm2sm3hash);
        System.out.println("Sm2SignWithDigest " + DatatypeConverter.printHexBinary(sm2digest));

        int sm2verify1 = EncryptSdk.sm2VerifyWithDigest(pubkey, sm2digest, sm2sm3hash);
        System.out.println("Sm2VerifyWithDigest " + sm2verify1);

        String pem = "-----BEGIN PUBLIC KEY-----\n";
        pem += "MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE5rwEIw9e5fX87uSN7C/vy6lyEZ2R\n";
        pem += "gzLqWLnY8EPN1C+nJP2v4rLgaQCbHV38+vBVLimbLmdccLM69R83JxpxuQ==\n";
        pem += "-----END PUBLIC KEY-----\n";

        byte[] pk = EncryptSdk.sm2PemChangeToPubkey(pem.getBytes());
        System.out.println("Sm2PemChangeToPubkey " + DatatypeConverter.printHexBinary(pk));
    }
}

```
