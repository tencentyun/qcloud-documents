本文为您介绍如何使用长安链 SDK 对接网络。




## 下载 SDK

下载 [chainmaker-sdk-go-demo](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/chainmaker-sdk-go-demo.zip)，压缩包主要包含以下内容：

- **chainmaker-sdk-demo**：目录。
  - **config**：目录，存放 SDK 配置文件，后续证书也可放置在该目录下。
    - **config.yml**：SDK 配置文件。
  - **main.go**：文件，为 SDK 调用合约示例代码。
  - **go-fact-1.2.0.wasm**：文件，存证合约示例代码编译后字节码，可根据 [智能合约开发（Go）](https://cloud.tencent.com/document/product/663/60112) 指南编译得到，通过 TBaaS 控制台上传该文件可部署该合约。
- **chainmaker-sdk-go**：目录，存放长安链 Go 版本 SDK 源代码。


## 操作步骤


### 查看长安链 SDK 配置文件

长安链 SDK 配置文件 config.yml 如下所示：

```yml
chain_client:
  # 链ID
  chain_id: "chain_txtxt"
  # 组织ID
  org_id: "orgtxtxtxt.chainmaker-txtxtxtxtx"
  # 客户端用户私钥路径
  user_key_file_path: "./config/user_ecc_tls.key"
  # 客户端用户证书路径
  user_crt_file_path: "./config/user_tls.crt"
  # 客户端用户交易签名私钥路径(若未设置，将使用user_key_file_path)
  user_sign_key_file_path: "./config/user_ecc_sign.key"
  # 客户端用户交易签名证书路径(若未设置，将使用user_crt_file_path)
  user_sign_crt_file_path: "./config/user_sign.crt"

  nodes:
    - # 节点地址，格式为：IP:端口:连接数
      node_addr: "orgtxtxtxt.chainmaker-txtxtxtxtx.tbaas.tech:8080"  #"外网域名:端口"
      # 节点连接数
      conn_cnt: 1
      # RPC连接是否启用双向TLS认证
      enable_tls: true
      # 信任证书池路径, ca.crt所在路径
      trust_root_paths:
        - "./config/"
      # TLS hostname
      tls_host_name: "common1-orgtxtxtxt.chainmaker-txtxtxtxtx"
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


### 部署合约

1. 单击**合约管理**页签，进入“合约管理”页面
2. 使用压缩包内的 `go-fact-1.2.0.wasm` 上传，并且进行如下配置：
   - **合约名称**：填写 `fact`。
   - **版本号**：填写 `v1.0`。
   - **执行环境**：选择 `Go`。
   - **初始化参数（选填）**：保存为空。
     <img src="https://main.qcloudimg.com/raw/2d6651004a61dcb4dcd03133bf2a12c0.png" style="zoom: 60%;" />
3. 部署成功后，合约列表将会展示刚刚部署的合约。如下图所示：
   <img src="https://main.qcloudimg.com/raw/36139a20c5410526c643bc79c8e84092.png" style="zoom: 60%;" />


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




### 运行 Demo

1. 进入 `chainmaker-sdk-go-demo/chainmaker-sdk-demo` 目录。
2. 将 `main.go` 示例代码中的 `claimContractName` 和 `claimVersion` 修改为上述部署的合约的名字和版本号，示例如下：

```go
var (
	claimContractName = "fact"
	claimVersion      = "v1.0"
)
```

3. 执行以下命令：

```sh
go run main.go config/config.yml
```

成功运行可以查看到如下图输出：
<img src="https://qcloudimg.tencent-cloud.cn/raw/2914b0552c23b473c488c12c6c5220c8.png" />



## 更多对接方式

长安链提供了多种语言的 SDK，包括 Go SDK、Java SDK 等，方便开发者根据需求进行选用。更多详情请参见 [长安链 SDK 开发指南](https://docs.chainmaker.org.cn/dev/SDK.html)。
