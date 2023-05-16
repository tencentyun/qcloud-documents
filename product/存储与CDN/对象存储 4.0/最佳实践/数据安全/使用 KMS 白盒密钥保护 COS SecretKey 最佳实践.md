## KMS 白盒密钥简介

KMS 白盒密钥用于保护端上的敏感根密钥信息，例如 API SecretKey、用户内部系统使用的鉴权密钥或 token、其它本地敏感根密钥信息等，**实现全链路无敏感密钥信息明文**。将算法与密钥进行混淆融合，以查找表的形式有效保护密钥信息，在不暴露任何密钥的情况下实现加密与解密，并通过设备绑定的方式进一步确保密钥的安全。

![](https://main.qcloudimg.com/raw/707777b13a8513432bed163dad6c0823.png)


本文为您介绍使用密钥管理系统（Key Management Service，KMS）白盒密钥对 COS 产品 SecretKey 加解密的操作示例，通过白盒密钥对 SecretKey 进行保护和安全使用，详情步骤请参见：

- [密钥的管理和分发](#SecretKey)
- [通过对象存储 SDK 工具访问 COS](#SDK)

## 使用 KMS 白盒密钥优势

**高安全性**

基于高强度混淆加固算法及多重安全防护技术，杜绝 API SecretKey 的明文暴露在源代码中。

**动态白盒**

支持在白盒库不变的情况下实现灵活的密钥的动态轮换。

**设备绑定**

绑定设备指纹信息，实现对解密密钥的加固保护。

**算法支持**

支持国际算法 AES、国密算法 SM4 算法，满足合规要求。




[](id:SecretKey)
## 密钥的管理和分发

### 步骤1：创建白盒密钥

>!
>
>- 白盒密钥为 KMS 收费项，详情请参见 [KMS 计费概述](https://cloud.tencent.com/document/product/573/34388#.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5) 和 [KMS 购买方式](https://cloud.tencent.com/document/product/573/18809#.E8.B4.AD.E4.B9.B0.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5)。
>- 创建白盒密钥对是通过调用白盒服务来实现的，支持控制台方式和 API 方式，本文示例采用控制台方式。

1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在左侧菜单栏选择**白盒密钥管理** > **用户密钥管理**页面，根据业务需求切换“地域” ，单击**新建**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4e33f95bbcaac050688e5f88044a1da1.png)
2. 在弹出的对话框，填写白盒密钥名称，选择加密算法，描述信息及标签（两者选填），单击**确定**，即可完成白盒密钥的创建。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1c2129a99ee16763718d3fb190467a15.png)

### 步骤2：控制台获取 API SecretKey

1. 使用主账号登录 [API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi)，查看您的 API 密钥 。
2. 在密钥操作列中，单击**显示**，完成身份验证，获取并复制 SecretKey。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ee48295d75088b065c974e8296877dd8.png)

### 步骤3：对 SecretKey 明文进行 base64 编码

将步骤2中获取的 SecretKey 内容进行 base64 编码。 例如，要加密的 SecretKey 明文是：`lY9Ynrabcdj05YH1234LE37xxxx`，使用 openssl 命令生成 base64 编码后的结果为：`bFk5WW5yYWJjZGowNVlIMTIzNExFMzcwSE9Nxxxx`。

```
echo lY9Ynrabcdj05YH1234LE37xxxx | openssl base64
```

### 步骤4：使用白盒密钥加密 API SecretKey

1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击“白盒密钥ID/名称”或“操作”列的**加密**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/7103612e6b8b4580d9b85afa8cb99c41.png)
2. 在弹出的对话框，将步骤3中获取的编码内容填充至明文（base64）文本框中，单击**白盒加密**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/16316d9352ec2091ef6b18e38b80fe03.png)

加密成功后，会返回随机生成的初始化向量（简称 IV）和加密后的密文，单击**下载IV**和**下载密文**，即可完成内容的下载。

>?其中初始化向量（简称 IV）和加密后的密文均已进行 base64 编码。

![](https://qcloudimg.tencent-cloud.cn/raw/05a4fecbcf0dcfa5aacc81ebfb7b36aa.png)

3. （可选步骤）白盒密钥支持将解密密钥与解密运行的物理环境进行绑定。操作方式为：

 - 在白盒密钥控制台中下载对应环境的指纹采集工具，并在指定的环境中运行指纹采集工具，获得该环境的指纹字符串。
 - 在白盒密钥控制台中，选择指定的白盒密钥，单击“新增设备指纹”，输入对应环境的指纹字符串，将该指纹与该密钥进行绑定。
 - 指纹环境变量被绑定到该密钥后，解密密钥会被更新，后续使用该白盒密钥加密的数据只能使用更新后的解密密钥在已绑定的物理环境中进行解密。

下载指纹采集工具：
![](https://qcloudimg.tencent-cloud.cn/raw/58e34bb9a21a48d8265603d51c323e76.png)
将指纹字符串与指定的白盒密钥进行绑定：
![](https://qcloudimg.tencent-cloud.cn/raw/a3d06f7b9acdf14d8ed9b1faa35d3b4b.png)

### 步骤5：下载解密密钥

1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击“白盒密钥ID/名称”，进入密钥基本信息页面。
2. 在密钥基本信息页面，单击**下载解密密钥**，并命名为 decrypt_key_sm4.bin。
   ![](https://qcloudimg.tencent-cloud.cn/raw/75d216b49f6688f62d549cd3c63863a7.jpg)

### 步骤6：下载解密 SDK 文件

1. 登录 [密钥管理系统（合规）控制台](https://console.cloud.tencent.com/kms2/whitebox)，在白盒密钥列表，单击右侧的**下载解密 SDK 文件**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e694189a75ffc0d58cef53be05244944.png)
2. 在弹出的对话框，根据各业务系统自身的编程语言，选择下载相应编程语言的解密 SDK，并将解密 SDK 集成到业务系统中。
   ![](https://qcloudimg.tencent-cloud.cn/raw/3ca227dbe816170a97b4d687e9e9c7b7.png)

### 步骤7：白盒解密密钥和 API SecretKey 密文分发

管理员将上述步骤中下载的解密密钥、IV 和密文三个文件，分发给各业务系统的开发或运维人员。其中，解密密钥部署到相应业务系统的文件中，而初始化向量 IV 和密文会作为解密 SDK 的传参。

>!下载的解密密钥是一个二进制 bin 文件，需要将该文件和可执行文件（已经集成了解密 SDK）放在相同的服务器上，文件路径将作为解密 SDK 的解密参数。



[](id:SDK)
## 通过对象存储 SDK 工具访问 COS

### 步骤1：通过永久密钥初始化身份信息

安装对象存储 SDK 工具后，在客户端代码中引入下载的白盒 SDK，并按照如下步骤获取解密后的 Secret Key：

1. 在代码中引入预先下载的白盒 SDK。
2. 调用白盒密钥解密 SDK 的解密函数对加密后的 Secret Key 进行解密。传入如下参数，从而获得解密后的明文。
 - decrypt_key_bin_dir：步骤7中解密密钥存放的目录。
 - decrypt_key_sm4.bin：步骤5中下载的解密密钥，其对应的文件名。
 - InitializationVector：步骤4中下载的 IV。
 - CipherText：步骤4中用白盒加密后的 SecretKey 密文。
 - algorithmType：是生成密钥时使用的算法类型，取值为0或1。0表示 AES_256，1表示 SM4。
3. 使用解密后的 Secret Key 以及 Secret ID（若 Secret ID 也被加密，则同样需要解密）对 COS SDK 进行初始化。后续针对 COS 的服务调用可参考 COS SDK 的相关文档。

白盒密钥解密 SDK 基于 C 语言实现，并提供了基于其他高级语言的适配，例如 Golang、Python、Java 等。具体使用方法可参考指定语言的解密 SDK 中的代码示例。

Golang 示例代码如下（基于 CGO）：

由于白盒解密 SDK 底层功能由 C lib 库实现，因此示例代码采用 CGO 注解的方式将解密 SDK 头文件目录`#cgo CFLAGS: -I${header_file_dir_path}`以及 lib 库文件`#cgo LDFlags: -L${lib_dir_path} -l${library_name}`引入到代码中。头文件目录以及 lib 库通常位于所下载的白盒解密 SDK 的根目录下，应用集成时可根据项目结构自主调整。


```
/*
#cgo CFLAGS: -I${SRCDIR}/include
#cgo LDFLAGS: -L${SRCDIR}/lib -lydwbcrypto

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "wrp.h"

static int clt_load_key(WRP_KEY_CTX *key_ctx, char *decrypt_key_path, const char *file_name,
        uint32_t mode, uint32_t algoType) {
    printf("begin to load key in dir: %s\n", decrypt_key_path);
    printf("begin to load key: %s\n", file_name);
    int err;
    const WRP_KEY* keyalg = WRP_KEY_wbaes();
    if (algoType == 1) { keyalg = WRP_KEY_wbsm4(); }

    err = WRP_KEY_init(key_ctx, keyalg, 0);
    if (err) { printf("Err: orig_byte init\n"); goto end; }

    err = WRP_KEY_ctrl(key_ctx, WRP_KEY_CTRL_WB_SET_PATH, decrypt_key_path, strlen(decrypt_key_path));
    if (err) { printf("Err: set path\n"); goto end; }

    err = WRP_KEY_import(key_ctx, file_name, mode);
    if (err) { printf("Err: WRP_KEY_import error: %d， \n", err); goto end; }

end:
    return err;
}


int clt_cbc_dec(char * file_dir, const char * file_name, uint8_t* ciph, uint32_t ciphlen, char* iv,
        uint32_t algoType, uint8_t* out, uint32_t* outlen) {
    WRP_KEY_CTX *mykey;
    WRP_CIPHER_CTX *myaes = NULL;

    uint32_t bits;
    ERRNO err = ERRNO_OK;

    const WRP_CIPHER* alg = WRP_wbaes_cbc();
    if (algoType == 1) { alg = WRP_wbsm4_cbc(); }

    // IO: load wbkey
    mykey = WRP_KEY_CTX_new();
    err = clt_load_key(mykey, file_dir, file_name, KEYMODE_DECRYPT, algoType);
    if (err) { printf("load whitebox key error: %d\n", err); goto cleanup; }

    printf("load key success\n");
    bits = WRP_KEY_key_len(mykey, KEYLEN_TYPE_BITS);
    printf("key len=%u\n", bits);

    if (bits == 0) { printf("get whitebox key length error\n"); err=-1; goto cleanup; }

    // crypto
    myaes = WRP_CIPHER_CTX_new();

    err = WRP_CIPHER_Decrypt_init(myaes, alg, mykey, (uint8_t *)iv);
    if (err) { printf("Dec: init Err**\n"); goto cleanup; }
    printf("decrypt init success, begin to decrypt cipher\n");

    err = WRP_CIPHER_Decrypt_doCipher(myaes, ciph, ciphlen, out, outlen);
    if (err) { printf("decrypt error: %.8X\n", err); goto cleanup; }
    //printf("decrypt success\n");
    //printf("output: %s\n", deout);
    //printf("\n");

cleanup:
    WRP_KEY_CTX_free(mykey);
    WRP_CIPHER_CTX_free(myaes);
    return err;
}

void set_fingerprint_env_name(char *fingerprint_env_name) {
    WRP_getENV_KEY((uint8_t *)fingerprint_env_name, strlen(fingerprint_env_name));
}

*/
import “C”

// Decrypt ...
func Decrypt(input DecryptionInput) ([]byte, error) {
    if input.KeyDir == "" || input.KeyFileName == "" || input.CipherText == "" || input.InitializationVector == "" {
        return nil, errors.New("invalid white-box decryption input")
    }
    cipher, err := base64.StdEncoding.DecodeString(input.CipherText)
    if err != nil {
        return nil, fmt.Errorf("failed to decode cipher text: %w", err)
    }
    iv, err := base64.StdEncoding.DecodeString(input.InitializationVector)
    if err != nil {
        return nil, fmt.Errorf("failed to decode initialization vector: %w", err)
    }

    decryptionKeyDir := C.CString(input.KeyDir)
    defer C.free(unsafe.Pointer(decryptionKeyDir))

    decryptionKeyFileName := C.CString(input.KeyFileName)
    defer C.free(unsafe.Pointer(decryptionKeyFileName))

    // malloc a buffer which size is a little greater than your plaintext
    outLen := len(input.CipherText) + 1024
    outBuf := C.malloc(C.size_t(outLen))
    defer C.free(unsafe.Pointer(outBuf))

    errC := C.clt_cbc_dec(
        decryptionKeyDir, decryptionKeyFileName,
        (*C.uchar)(unsafe.Pointer(&cipher[0])),
        C.uint(len(cipher)),
        (*C.char)(unsafe.Pointer(&iv[0])),
        C.uint(input.AlgorithmType),
        (*C.uchar)(outBuf),
        (*C.uint)(unsafe.Pointer(&outLen)),
    )
    if errC != 0 {
        return nil, fmt.Errorf("whitebox decryption failed with code %d", int(errC))
    }
    plain := C.GoBytes(outBuf, C.int(outLen))
    return plain, nil
}

func main() {
    //将<bucket>和<region>修改为真实的信息
    //bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
    u, _ := url.Parse("https://<bucket>.cos.<region>.myqcloud.com")
    // 使用环境变量指定白盒密钥相关信息，以及加密后的 secret ID 以及 secret key。
    encryptionAlgorithm, _ := strconv.Atoi(os.Getenv("EncryptionAlgorithm"))
    whiteboxDecryptInput := DecryptionInput{
        KeyDir:               os.Getenv("WhiteboxKeyDir"),      // e.g.: /usr/local/
        KeyFileName:          os.Getenv("WhiteboxKeyFileName"), // e.g.: whitebox_key.bin
        InitializationVector: os.Getenv("WhiteboxDecryptionIV"),
        AlgorithmType:        uint(encryptionAlgorithm),
    }
    // 使用白盒 sdk 解密 secret ID
    whiteboxDecryptInput.CipherText = os.Getenv("COS_Encrypted_Secret_ID")
    secretID, err := Decrypt(whiteboxDecryptInput)
    if err != nil {
        panic(err)
    }
    // 使用白盒 sdk 解密 secret key
    whiteboxDecryptInput.CipherText = os.Getenv("COS_Encrypted_Secret_Key")
    secretKey, err := Decrypt(whiteboxDecryptInput)
    if err != nil {
        panic(err)
    }

    b := &cos.BaseURL{BucketURL: u}
    c := cos.NewClient(b, &http.Client{
        //设置超时时间
        Timeout: 100 * time.Second,
        Transport: &cos.AuthorizationTransport{
            //如实填写账号和密钥，也可以设置为环境变量
            SecretID:  string(secretID),
            SecretKey: string(secretKey),
        },
    })

    name := "test/hello.txt"
    resp, err := c.Object.Get(context.Background(), name, nil)
    if err != nil {
        panic(err)
    }
    bs, _ := ioutil.ReadAll(resp.Body)
    _ = resp.Body.Close()
    fmt.Printf("%s\n", string(bs))
}

type DecryptionInput struct {
    KeyDir               string
    KeyFileName          string
    InitializationVector string // Base64 encoded.
    CipherText           string // Base64 encoded.
    AlgorithmType        uint   // 0: AES_256, 1: SM4.
}
```


### 步骤2：直接使用 COS SDK 请求 COS 服务

初始化之后，您可以直接使用 COS SDK 工具进行上传、下载等基本操作，而无需像 API 请求一样自行生成签名，因为 SDK 工具代替您通过密钥生成了签名，向 COS 发起请求。

 
