## 操作场景

本文介绍对应长安链区块链网络 **非国密ECC证书** 和 **国密SM2证书** 申请 证书请求文件CSR 生成的步骤，请结合您的实际情况通过以下两种方式生成 CSR：

- [非国密ECC 证书申请 CSR](#ecc)
- [国密SM2 证书申请 CSR](#sm2)

## 操作步骤

[](id:ecc)

### 非国密ECC 证书申请 CSR 

1. 前往 [OpenSSL 官网](https://www.openssl.org/source/)，下载 openssl 并配置安装。
2. 下载 [cmecccsr 工具](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/cmecccsr.zip) 并解压。
3. 执行以下命令，生成对应文件。

```
sh ecccsr.sh
```

 该命令会生成以下四个文件：

 - `user_ecc_sign.key`：为用户证书对应私钥，需安全保存，支持在 SDK 中使用。
 - `user_ecc_sign.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户证书。
 - `user_ecc_tls.key`：为用户tls证书对应私钥，需安全保存，支持在 SDK 中使用。
 - `user_ecc_tls.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户tls证书。

#### 工具说明

以下为工具中主要使用的命令：

1. 生成用户证书对应私钥和CSR文件

   - **生成密钥对**：生成的 `temp` 文件为用户证书对应私钥。

   ```
   openssl ecparam -name prime256v1 -genkey -out temp
   ```

   - **生成用户证书CSR文件**：命令中使用的 `openssl_user.cnf` 文件已包含在下载工具中。

   ```
   openssl req -batch -config openssl_user.cnf -key temp -new -sha256 -out user_ecc_sign.csr
   ```

   - **转换私钥格式**：将已生成的 `temp` 私钥转换为 `pkcs#8` 格式的 `user_ecc_sign.key` 文件，后续用于 chainmaker-sdk 的配置和识别。

   ```
   openssl pkcs8 -topk8 -in temp -nocrypt -out user_ecc_sign.key
   ```

2. 生成用户tls证书对应私钥和CSR文件

   - **生成密钥对**：生成的 `temp` 文件为用户tls证书对应私钥。

   ```
   openssl ecparam -name prime256v1 -genkey -out temp
   ```

   - **生成用户tls证书CSR文件**：命令中使用的 `openssl_user.cnf` 文件已包含在下载工具中。

   ```
   openssl req -batch -config openssl_user.cnf -key temp -new -sha256 -out user_ecc_tls.csr
   ```

   - **转换私钥格式**：将已生成的 `temp` 私钥转换为 `pkcs#8` 格式的 `ser_ecc_tls.key` 文件，后续用于 chainmaker-sdk 的配置和识别。

   ```
   openssl pkcs8 -topk8 -in temp -nocrypt -out user_ecc_tls.key
   ```

[](id:sm2)

### 国密SM2 证书申请 CSR

1. 前往 [GmSSL 官网](http://gmssl.org/docs/quickstart.html)，下载 gmssl 并配置安装。 
2. 下载 [cmsm2csr 工具](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/cmsm2csr.zip) 并解压。
3. 执行以下命令，生成对应文件。

```
sh sm2csr.sh
```

 该命令会生成以下四个文件：

 - `user_sm2_sign.key`：为用户证书对应私钥，需安全保存，支持在 SDK 中使用。
 - `user_sm2_sign.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户证书。
 - `user_sm2_tls.key`：为用户tls证书对应私钥，需安全保存，支持在 SDK 中使用。
 - `user_sm2_tls.csr`：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户tls证书。

#### 工具说明

以下为工具中主要使用的命令：

1. 生成用户证书对应私钥和CSR文件

   - **生成密钥对**：生成的 `temp` 文件为用户证书对应私钥。

   ```
   gmssl ecparam -name sm2p256v1 -genkey -out temp
   ```

   - **生成用户证书CSR文件**：命令中使用的 `gmssl_user.cnf` 文件已包含在下载工具中。

   ```
   gmssl req -batch -config gmssl_user.cnf -key temp -new -sm3 -out user_sm2_sign.csr
   ```

   - **转换私钥格式**：将已生成的 `temp` 私钥转换为 `pkcs#8` 格式的 `user_sm2_sign.key` 文件，后续用于 chainmaker-sdk 的配置和识别。

   ```
   gmssl pkcs8 -topk8 -in temp -nocrypt -out user_sm2_sign.key
   ```

2. 生成用户tls证书对应私钥和CSR文件

   - **生成密钥对**：生成的 `temp` 文件为用户tls证书对应私钥

   ```
   gmssl ecparam -name sm2p256v1 -genkey -out temp
   ```

   - **生成用户tls证书CSR文件**：命令中使用的 `gmssl_user.cnf` 文件已包含在下载工具中。

   ```
   gmssl req -batch -config gmssl_user.cnf -key temp -new -sm3 -out user_sm2_tls.csr
   ```

   - **转换私钥格式**：将已生成的 `temp` 私钥转换为 `pkcs#8` 格式的 `user_sm2_tls.key` 文件，后续用于 chainmaker-sdk 的配置和识别。

   ```
   gmssl pkcs8 -topk8 -in temp -nocrypt -out user_sm2_tls.key
   ```

###  长安链原生SDK 证书配置示例

您可参考以下代码，在长安链原生SDK chainmaker-sdk-go中使用生成的私钥及已下载的证书配置sdk_config.yml文件，以非国密ECC证书为例

#### Go SDK

```yml
chain_client:
  # 链ID
  chain_id: "chain_txtxt"
  # 组织ID
  org_id: "orgtxtxtxt.chainmaker-txtxtxtxtx"
  # 客户端用户tls私钥路径
  user_key_file_path: "./user_ecc_tls.key"
  # 客户端用户tls证书路径
  user_crt_file_path: "./user_tls.crt"
  # 客户端用户交易签名私钥路径(若未设置，将使用user_key_file_path)
  user_sign_key_file_path: "./user_ecc_sign.key"
  # 客户端用户交易签名证书路径(若未设置，将使用user_crt_file_path)
  user_sign_crt_file_path: "./user_sign.crt"

  nodes:
    - # 节点地址，格式为：IP:端口:连接数
      node_addr: "orgtxtxtxt.chainmaker-txtxtxtxtxt.baas.tech:8080"  #外网域名
      # 节点连接数
      conn_cnt: 1
      # RPC连接是否启用双向TLS认证
      enable_tls: true
      # 信任证书池路径
      trust_root_paths: # 包含组织根证书ca.crt的目录
        - "./ca"
      # 节点 TLS hostname
      tls_host_name: "common1-orgtxtxtxt.chainmaker-txtxtxtxtx"

```
