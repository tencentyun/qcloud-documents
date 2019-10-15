## 操作场景
本文介绍对应区块链证书加密方式 ECC 和 SM2 的证书请求文件（CSR）创建步骤，请结合您的实际情况通过以下两种方式创建 CSR：
- ECC 创建 CSR
- SM2 创建 CSR

## 操作步骤
### ECC 创建 CSR 
1. 前往 [OpenSSL 官网](https://www.openssl.org/source/)，下载 openssl 并配置安装。
2. 下载 [ecccsr 工具]() 并解压。
3. 执行以下命令，生成对应文件。
```
sh ecccsr.sh
```
 该命令会生成以下三个文件：
 - `out.key`：为用户的私钥，需安全保存。
 - `out.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请证书。
 - `out_sk`：为 `out.key` 的 pkcs#8 格式，支持 SDK 使用。

#### 工具说明
以下为工具中主要使用的命令：
- **生成密钥对**：生成的 `out.key` 文件为用户的私钥，需安全保存。
```
openssl ecparam -name prime256v1 -genkey -out out.key
```
- **生成 CSR 文件**：命令中使用的 `openssl_user.cnf` 文件已包含在下载工具中，无需变更内容。
```
openssl req -batch -config openssl_user.cnf -key out.key -new -sha256 -out out.csr
```
- **转换私钥格式**：将已生成的 `out.key` 私钥转换为 pkcs#8 格式的 `out_sk` 文件，用于 fabric-sdk 识别。
```
openssl pkcs8 -topk8 -in out.key -nocrypt -out out_sk
```

### SM2 创建 CSR
1. 前往 [gmssl 官网](http://gmssl.org/docs/quickstart.html)，下载 gmssl 并配置安装。 
2. 下载 [sm2csr 工具]() 并解压。
3. 执行以下命令，生成对应文件。
```
sh sm2csr.sh
```
该命令会生成以下三个文件：
 - `out.key`：为用户的私钥，需安全保存。
 - `out.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请证书。
 - `out_sk`：为 `out.key` 的 pkcs#8 格式，支持 SDK 使用。

#### 工具说明
以下为工具中主要使用的命令：
- **生成密钥对**：生成的 `out.key` 文件为用户的私钥，需安全保存。
```
gmssl ecparam -name sm2p256v1 -genkey -out out.key
```
- **生成 CSR 文件**：命令中使用的 `gmssl_user.cnf` 文件已包含在下载工具中，无需变更内容。
```
gmssl req -batch -config gmssl_user.cnf -key out.key -new -sm3 -out out.csr
```
- **转换私钥格式**：将已生成的 `out.key` 私钥转换为 pkcs#8 格式的 `out_sk` 文件，用于 fabric-sdk 识别。
```
gmssl pkcs8 -topk8 -in out.key -nocrypt -out out_sk
```

### Fabric 原生 SDK 示例
您可参考以下代码，在 Fabric 原生 SDK 中使用生成的私钥及已下载的证书：
#### Java SDK
```java
 Wallet wallet = Wallet.createFileSystemWallet("本地存储证书信息目录"); 
 FileReader keyReader = new FileReader("pkcs#8 格式私钥证书文件");
 FileReader certReader = new FileReader("TBaaS 上下载的证书");
 wallet.put("证书标识", Identity.createIdentity("组织 MSP", certReader, keyReader));
```

#### Node.js SDK
```
var fs = require('fs-extra');
 var fabric_client = new Fabric_Client();

 var cert = fs.readFileSync('TBaaS 上下载的证书');
 var priv = fs.readFileSync('pkcs#8 格式私钥证书文件');

 fabric_client.createUser({
     username: '证书标识',
     mspid: 'Org1MSP',
     cryptoContent: {
     privateKeyPEM: priv,
     signedCertPEM: cert
         }
     });
```
