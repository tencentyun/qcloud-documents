本文为您介绍如何使用长安链 SDK 对接 v2.2.0 版本的长安链网络，长安链网络版本可以从区块链网络概览页右下角的**网络配置信息**中查看。

<img src="https://main.qcloudimg.com/raw/e4e4d83849297385f09a7846cab9ee81.png" style="zoom: 60%;" />

## 下载 SDK

下载 [chainmaker-sdk-go-demo](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/chainmaker-sdk-go-demo-v2_2.zip)，压缩包主要包含以下内容：

- **chainmaker-sdk-demo**：目录。
  - **config**：目录，存放 SDK 配置文件，后续证书也可放置在该目录下。
    - **config.yml**：SDK 配置文件。
  - **wasm**、**evm**：目录，为 SDK 调用合约示例代码。
  - **rust-fact.wasm**：文件，Rust 存证合约示例代码编译后字节码，可根据 [智能合约开发（Rust）](https://cloud.tencent.com/document/product/663/72540) 指南编译得到，通过 TBaaS 控制台上传该文件可部署该合约。
  - **token.abi**：文件，Solidity 合约示例代码编译后字节码，可根据 [智能合约开发（Solidity）](https://cloud.tencent.com/document/product/663/72542) 指南编译得到，通过 TBaaS 控制台上传该文件可部署该合约。
  - **token.bin**：文件，Solidity 合约示例代码编译后 abi 文件。
  - **token.sol**：文件，Solidity 合约示例代码。
- **chainmaker-sdk-go**：目录，存放长安链 Go 版本 SDK 源代码。
- **chainmaker-pb-go**：目录，存放长安链 pb-go 库源代码。
- **chainmaker-common**：目录，存放长安链 common 库源代码。

## 操作步骤

### 查看长安链 SDK 配置文件

长安链 SDK 配置文件 config.yml 如下所示：

```yml
chain_client:
  # 链 ID
  chain_id: "chain_txtxt"
  # 组织 ID
  org_id: "orgtxtxtxt.chainmaker-txtxtxtxtx"
  # 客户端用户私钥路径
  user_key_file_path: "../config/user_ecc_tls.key"
  # 客户端用户证书路径
  user_crt_file_path: "../config/user_tls.crt"
  # 客户端用户交易签名私钥路径（若未设置，将使用 user_key_file_path)
  user_sign_key_file_path: "../config/user_ecc_sign.key"
  # 客户端用户交易签名证书路径（若未设置，将使用 user_crt_file_path)
  user_sign_crt_file_path: "../config/user_sign.crt"
  # 同步交易结果模式下，轮训获取交易结果时的最大轮训次数，删除此项或设为<=0 则使用默认值 10
  retry_limit: 10
  # 同步交易结果模式下，每次轮训交易结果时的等待时间，单位：ms 删除此项或设为<=0 则使用默认值 500
  retry_interval: 500

  nodes:
    - # 节点地址，格式为：IP: 端口：连接数
      node_addr: "orgtxtxtxt.chainmaker-txtxtxtxtx.tbaas.tech:8080"  #"外网域名：端口"
      # 节点连接数
      conn_cnt: 1
      # RPC 连接是否启用双向 TLS 认证
      enable_tls: true
      # 信任证书池路径，ca.crt 所在路径
      trust_root_paths:
        - "../config/"
      # TLS hostname
      tls_host_name: "common1-orgtxtxtxt.chainmaker-txtxtxtxtx"
  archive:
    # 数据归档链外存储相关配置
    type: "mysql"
    dest: "root:123456:localhost:3306"
    secret_key: xxx
  rpc_client:
    max_receive_message_size: 16 # grpc 客户端接收消息时，允许单条 message 大小的最大值 (MB)
    max_send_message_size: 16 # grpc 客户端发送消息时，允许单条 message 大小的最大值 (MB)
  pkcs11:
    enabled: false # pkcs11 is not used by default
    library: /usr/local/lib64/pkcs11/libupkcs11.so # path to the .so file of pkcs11 interface
    label: HSM # label for the slot to be used
    password: 11111111 # password to logon the HSM(Hardware security module)
    session_cache_size: 10 # size of HSM session cache, default to 10
    hash: "SHA256" # hash algorithm used to compute SKI
```

### 获取访问地址和链 ID

1. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)。
2. 选择左侧导航栏中的**长安链** > **区块链网络**，进入“区块链网络”页面。
3. 在“区块链网络”页面中，选择需查看的网络，单击**管理**进入“网络概览”页面。
4. 在“网络基础信息”模块找到链 ID 和外网域名，分别填写到配置文件的 `chain_id` 和 `node_addr` 字段。
   <img src="https://main.qcloudimg.com/raw/7eb254ab8e889e163c8fb5bf681c86a4.png">

### 获取组织 ID

1. 单击**组织与节点**页签，进入“组织与节点”页面。
2. 找到当前组织 ID 信息，填写到配置文件的 `org_id` 字段。如下图所示： 
   ![](https://main.qcloudimg.com/raw/8f0ab0369019b96e64db29efd2e72ac4.png)

### 获取节点名称

1. 在“组织与节点”页面单击**节点管理**，进入“节点管理”页面。
2. 找到当前组织的节点列表，选择一个节点并复制节点名称，填写到配置文件的 `tls_host_name` 字段。如下图所示： 
   ![](https://main.qcloudimg.com/raw/930294344d259011819adfab7dc9db3f.png)

### 申请证书

1. 根据 [证书申请 CSR 生成指南](https://cloud.tencent.com/document/product/663/60114)，生成证书 CSR 和相应私钥。
2. 以生成非国密 ECC 证书为例，运行 ecccsr.sh 脚本将会得到以下四种文件：

 - **user_ecc_sign.key**：用户证书私钥。
 - **user_ecc_sign.csr**：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户证书。
 - **user_ecc_tls.key**：用户 tls 证书私钥。
 - **user_ecc_tls.csr**：用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户 tls 证书。

3. 在“证书管理”界面添加申请证书，填写证书标识，并上传 `user_ecc_sign.csr` 和 `user_ecc_tls.csr`。如下图所示： 
   ![](https://main.qcloudimg.com/raw/cc4ad0d188524a6a6bc6fcdc161d2dd6.png)
4. 申请成功后可以单击**下载**下载对应证书，压缩包包含如下文件：

 - **ca.crt**：组织根证书。
 - **user_sign.crt**：用户证书。
 - **user_tls.crt**：用户 tls 证书。
   <img src="https://main.qcloudimg.com/raw/6e0bf44f12f26a16fc5a0dab3d483881.png"/>

5. 将三个证书 `ca.crt`，`user_sign.crt`，`user_tls.crt` 和两个私钥 `user_ecc_sign.key` 和 `user_ecc_tls.key` 放置到 `chainmaker-sdk-go-demo/chainmaker-sdk-demo/config` 目录下。
6. 根据下表，修改 SDK 配置文件 config.yml 的证书路径和 CA 路径：
<table>
<thead>
<tr>
<th>参数</th>
<th>值</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>user_key_file_path</td>
<td>./config/user_ecc_tls.key</td>
<td>用户 tls 证书所对应私钥</td>
</tr>
<tr>
<td>user_crt_file_path</td>
<td>./config/user_tls.crt</td>
<td>用户 tls 证书</td>
</tr>
<tr>
<td>user_sign_key_file_path</td>
<td>./config/user_ecc_sign.key</td>
<td>用户证书所对应私钥</td>
</tr>
<tr>
<td>user_sign_crt_file_path</td>
<td>./config/user_sign.crt</td>
<td>用户证书</td>
</tr>
<tr>
<td>trust_root_paths</td>
<td>./config/</td>
<td>根 CA 证书 <code>ca.crt</code> 所在目录</td>
</tr>
</tbody></table>

### 部署合约

#### 部署 wasm 合约

1. 单击**合约管理**页签，进入“合约管理”页面
2. 使用压缩包内的 `rust-fact.wasm` 上传，并且进行如下配置：
   - **合约名称**：填写 `fact`。
   - **版本号**：填写 `v1.0`。
   - **执行环境**：选择 `Rust`。
   - **初始化参数（选填）**：保存为空。
     <img src="https://main.qcloudimg.com/raw/97f396c802f5e410cec1d9e5ecb19e72.png" style="zoom: 60%;" />
3. 部署成功后，合约列表将会展示刚刚部署的合约。如下图所示： 
   <img src="https://main.qcloudimg.com/raw/885c9d29c52caad6fa49ba88e380ec89.png" style="zoom: 60%;" />

#### 部署 solidity 合约

1. 单击**合约管理**页签，进入“合约管理”页面
2. 根据 [合约调用 (Solidity)](https://cloud.tencent.com/document/product/663/72544)，将下载的证书文件 user_sign.crt 转换为 EVM 地址，并根据该 EVM 地址生成合约初始化参数的 ABI 编码
3. 使用压缩包内的 `token.bin` 上传，并且进行如下配置：
   - **合约名称**：填写 `token`。
   - **版本号**：填写 `v1.0`。
   - **执行环境**：选择 `Solidity`。
   - **初始化参数（选填）**：key 为 data，value 为 hex 格式的 ABI 编码。
     <img src="https://main.qcloudimg.com/raw/8a141576b1193db70183413d1d792ab3.png" style="zoom: 60%;" />
4. 部署成功后，合约列表将会展示刚刚部署的合约。如下图所示： 
   <img src="https://main.qcloudimg.com/raw/efbcd1f4a85bad362553b48975c2590c.png" style="zoom: 60%;" />

### 运行 Demo

#### 运行 wasm 合约调用 demo

1. 进入 `chainmaker-sdk-go-demo/chainmaker-sdk-demo/wasm` 目录。
2. 将 `main.go` 示例代码中的 `claimContractName` 修改为上述部署的合约的名字，示例如下：
```go
var (
	claimContractName = "fact"
)
```
3. 执行以下命令：
```sh
go run main.go ../config/config.yml
```
成功运行可以查看到如下图输出：
<img src="https://qcloudimg.tencent-cloud.cn/raw/2914b0552c23b473c488c12c6c5220c8.png" />

#### 运行 evm 合约调用 demo

1. 进入 `chainmaker-sdk-go-demo/chainmaker-sdk-demo/evm` 目录。
2. 将 `main.go` 示例代码中的 `contractName` 修改为上述部署的 evm 合约的名字，示例如下：
```go
var (
	contractName = "token"
)
```
3. 生成另一套证书 CSR 和相应私钥，并在“证书管理”界面上申请证书，将对应的证书文件`user_sign.crt`重命名为`user2_sign.crt`，并放置到 `chainmaker-sdk-go-demo/chainmaker-sdk-demo/config` 目录下。
4. 运行`go run main.go ../config/config.yml`
成功运行可以查看到如下图输出：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d7bfd0560834b126f79c0cd344a72168.png" />

## 更多对接方式

长安链提供了多种语言的 SDK，包括 Go SDK、Java SDK 等，方便开发者根据需求进行选用。更多详情请参见 [长安链 SDK 开发指南](https://docs.chainmaker.org.cn/v2.2.0_alpha/html/dev/SDK.html#)。
