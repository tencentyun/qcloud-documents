此指引适用于使用人脸核身服务接口，需要对传输敏感数据进行加密的场景。
>? 如果您在2023年3月17日前已开通 KMS 加密服务，可继续使用腾讯云密钥管理系统 KMS 安全保护的主密钥 CMK 作为加密密钥。
>
## 操作步骤
### 步骤1：获取密钥
登录 [人脸核身控制台](https://console.cloud.tencent.com/faceid/kms)，由于您已开通 KMS 加密服务，可在信息展示页获取密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/16e28464c1471ecd3ff7469f1b47f363.png)
### 步骤2：业务加解密流程
人脸核身使用信封加密（Envelope Encryption）应对海量数据的高性能加解密方案。使用 [GenerateDataKey](https://cloud.tencent.com/document/product/573/34419) 接口生成数据加密密钥 DEK 明文和密文，使用 DEK 明文对数据进行加密，并只需要传输数据加密密钥 DEK 密文到 KMS 服务端（通过 CMK 进行加解密），所有的业务数据都是采用高效的本地对称加密处理，对业务的访问体验影响很小。

### 接入流程示意图 
![](https://qcloudimg.tencent-cloud.cn/raw/af97b3c897a7eb851697624ffbacd398.png)

### 操作流程
1. 获取加密密钥，业务后台通过 API 调用密钥管理系统 KMS GenerateDataKey 接口生成数据密钥（明文密钥 Plaintext 和密文密钥 CiphertextBlob，Plaintext 需要先 base64 解码后才能作为明文密钥），GenerateDataKey 接口参数解析：
 - KeyId 统一使用第一步人脸核身控制台生成的 密钥 ID。
 - KeySpec 统一选择 AES_256。
2. 业务方对需要加密的敏感数据使用 AES-256-CBC 加密算法和明文密钥将数据进行加密，AES 加密可参考 [加密示例](#strep1) 中各语言示例。
3. 调用人脸核身接口时，将密文密钥传输给人脸核身服务，即可完成数据解密。

###  注意事项
- 需注意业务系统对明文密钥的处理：信封加密场景中采用的是对称加密，故明文密钥不可落盘，需在业务流程的内存中使用。
- 需注意后台系统对数据密钥的处理信封加密场景中采用的是对称加密，可根据业务需求复用同一个数据密钥或针对不同用户、不同时间使用不同的数据密钥进行加密，避免 DEK 重复。

### 加密示例[](id:strep1)
#### NodeJS 代码参考

```
function encryptAes256CBCPKCS7(data, secretKey) {
    try {
        let iv = "";
        var clearEncoding = 'utf8';
        var cipherEncoding = 'base64';
        var cipherChunks = [];
        var cipher = crypto.createCipheriv('aes-256-cbc', secretKey, iv);
         ///  secretKey： GenerateDataKey 接口获取的 Plaintext ，并将 Plaintext base64 解码后作为明文密钥使用
         ///  iv：初始化向量，16位  
        cipher.setAutoPadding(true);
        cipherChunks.push(cipher.update(data, clearEncoding, cipherEncoding));
        cipherChunks.push(cipher.final(cipherEncoding));
        return cipherChunks.join('');
    } catch (e) {
        console.error(e);
        return "";
    }
}
```

