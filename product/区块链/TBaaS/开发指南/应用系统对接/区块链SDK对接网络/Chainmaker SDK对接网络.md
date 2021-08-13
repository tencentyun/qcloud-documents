### 下载准备

下载 [chainmaker-sdk-go-demo](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/chainmaker-sdk-go-demo.zip)，压缩包主要包含以下内容：

- 目录：`chainmaker-sdk-demo`
  - 目录`config SDK`配置文件，后续证书可放置在改目录下
    - 文件`config.yml` SDK配置文件
  - 文件`main.go` SDK调用合约示例代码
  - 文件`rust-fact-1.0.0.wasm` 存证合约示例代码编译后字节码，可在TBaaS控制台上传该文件部署合约
- 目录：`chainmaker-sdk-go`目录： 长安链go版本SDK源代码

### 长安链SDK配置文件config.yml

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

### 获取访问地址和链ID

1. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)。
2. 选择左侧导航栏中的【长安链】>【区块链网络】，进入“区块链网络”页面。
3. 在“区块链网络”页面中，选择需查看的网络，点击管理，进入“网络概览”页面。
4. 在“网络基础信息”模块找到链ID和外网域名，分别填写到配置文件的`chain_id`和`node_addr`字段

<img src="https://main.qcloudimg.com/raw/7eb254ab8e889e163c8fb5bf681c86a4.png" style="zoom: 60%;" />

### 获取组织ID

1. 紧接着上述，点击“组织与节点”标签，进入“组织与节点”页面
2. 找到当前组织ID信息，填写到配置文件的`org_id`字段

<img src="https://main.qcloudimg.com/raw/63459fb78a589611d082dbc66c4dfaf5.png" style="zoom: 60%;" />

### 获取节点名称

1. 紧接着上述，在“组织与节点”页面点击“节点管理”进入“节点管理”页面。
2. 找到当前组织的节点列表，选择一个节点并复制节点名称，填写到配置文件的`tls_host_name`字段

<img src="https://main.qcloudimg.com/raw/588c6f25094e037f408bfd66ace0ffd0.png" style="zoom: 60%;" />

### 部署合约

1. 紧接着上述，点击“合约管理”标签，进入“合约管理”页面
2. 使用压缩包内的`rust-fact-1.0.0.wasm`上传，并且填写合约名称为`fact`，版本号为`v1.0`，执行环境选为`Rust`，初始化参数置为空
3. 部署成功后，合约列表将会出现刚刚部署的合约。

<img src="https://main.qcloudimg.com/raw/a9e16a6d16edd1e3d252673356597c1a.png" style="zoom: 60%;" />

<img src="https://main.qcloudimg.com/raw/31f04653ef34264704db3c7d652380ef.png" style="zoom: 60%;" />

### 证书申请

1. 根据[证书申请 CSR 生成指南](https://cloud.tencent.com/document/product/663/60114)，生成证书CSR和相应私钥。
2. 以生成非国密ECC证书为例，运行ecccsr.sh脚本将会得到四个文件

- `user_ecc_sign.key`: 用户证书私钥
- `user_ecc_sign.csr`: 用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户证书。
- `user_ecc_tls.key`: 用户tls证书私钥
- `user_ecc_tls.csr`: 用于在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 申请用户tls证书。

3. 在“证书管理”界面添加申请证书，填写证书标识，并将将`user_ecc_sign.csr`和`user_ecc_tls.csr`上传
4. 申请成功后可以下载对应证书，压缩包包含：

- `ca.crt`: 组织根证书
- `user_sign.crt`: 用户证书
- `user_tls.crt`: 用户tls证书

5. 将三个证书`ca.crt`，`user_sign.crt`，`user_tls.crt`和两个私钥`user_ecc_sign.key`和`user_ecc_sign.csr` 放置到 `chainmaker-sdk-go-demo/chainmaker-sdk-demo/config`目录下
6. 修改SDK配置文件config.yml的证书路径和跟CA路径为:

| 参数                    | 值                         | 说明                     |
| ----------------------- | -------------------------- | ------------------------ |
| user_key_file_path      | ./config/user_ecc_tls.key  | 用户tls证书所对应私钥    |
| user_crt_file_path      | ./config/user_tls.crt      | 用户tls证书              |
| user_sign_key_file_path | ./config/user_ecc_sign.key | 用户证书所对应私钥       |
| user_sign_crt_file_path | ./config/user_sign.crt     | 用户证书                 |
| trust_root_paths        | ./config/                  | 根CA证书`ca.crt`所在目录 |

<img src="https://main.qcloudimg.com/raw/f880540c149d8e99a57ac22c367e5232.png" style="zoom: 60%;" />

<img src="https://main.qcloudimg.com/raw/d899e6d3754a16ff916f64d55cf1070a.png" style="zoom: 60%;" />

### 运行demo

1. 进入`chainmaker-sdk-go-demo/chainmaker-sdk-demo`目录
2. 修改`main.go`示例代码中的`claimContractName`和`claimVersion`为上述部署的合约的名字和版本号

```go
var (
	claimContractName = "fact"
	claimVersion      = "v1.0"
)
```

3. 运行`go run main.go config/config.yml`, 可以看到一下输出：

<img src="https://main.qcloudimg.com/raw/4a7b27e80503e68a117c3944aa58f4c0.png" style="zoom: 60%;" />

### 更多对接方式

长安链提供了多种语言的SDK，包括：Go SDK、Java SDK、Python SDK（实现中）、Nodejs SDK（实现中）方便开发者根据需要进行选用。更多详情可以参考[长安链SDK开发指南](https://docs.chainmaker.org.cn/dev/SDK.html)。
