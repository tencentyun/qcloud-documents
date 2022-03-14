>! 区块链 SDK 对接网络调用方式支持 Fabric 网络。

若应用系统调用频率较高，则需要直接使用区块链 SDK 与区块链网络对接。这种情况下**应用系统应部署在与区块链网络同一地域内的云服务器 CVM 上**。在云 API 调用方式中，需要应用系统提供账户的 SecretID 和 SecretKey，用于认证授权访问权限。而在区块链 SDK 中，则需要应用系统在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview) 上申请用于访问的证书（节点证书和 nginx 证书）。如下图所示：
![img](https://main.qcloudimg.com/raw/81e1898de06b79a0b848345a72e4df4c.png)            
如果应用在开发测试中希望在本地访问区块链网络，则可以开启并使用网络的外网域名，使用该域名访问区块链网络的代理组件。这种访问方式仅适用于开发调试，在生产环境中推荐使用访问管理打通 VPC 的方式。


两种访问方式都需要在“访问管理”标签页中获取访问端地址，分别为“外网域名”和“访问端地址”。其区别可参考以下表格：

| VPC访问                                | 外网访问                   |
| ------------------------------------- | -------------------------- |
| 使用内网地址，无法在本地访问。                                | 使用公网域名，可在本地访问。 |
| 性能高。                                                       | 性能低。                     |
| 可用于生产环境。                                               | 一般只用于调试。             |
| 应用系统需要部署在与区块链节点同地域的VPC内，并在访问管理页面进行内网打通。 | 应用系统可部署在本地。       |






除了支持社区版区块链 SDK（Java、NodeJS、Golang），TBaaS 对 Java 版的社区区块链 SDK 进行了定制（tbaas-fabric-sdk-java），简化了应用系统与区块链网络连接的流程。

## 获取访问地址及证书
### VPC 访问
1. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)。
2. 选择左侧导航栏中的**Fabric** > **区块链网络**，进入“区块链网络”页面。
3. 在“区块链网络”页面中，选择需查看的网络，进入“访问管理”页面。
4. 在“访问管理”页面中，单击**新建**。在弹出的“新建链接”窗口中，参考以下信息进行创建：
![](https://main.qcloudimg.com/raw/aa9b66415677d8e0cc49a9fd6ab66015.png)
  - 名称：即链接标识。
  - 选择访问端：即选择应用系统所在的 VPC 和子网。
5. 创建成功后即可获取 VPC 访问地址（记为 PROXY_URL），即访问端地址（内网地址）。如下图所示：
![](https://main.qcloudimg.com/raw/86c7e8f4e7e4c51d83f1ab5c8aaef922.png)
  在本端链接选项中单击**查看**，并下载 nginx 证书（记为TLS_CERT），保存在文件中。如下图所示：
![](https://main.qcloudimg.com/raw/33ecdd5e5e06c82834716821db248a76.png)

### 外网访问（仅用于开发测试）[](id:stepwaiwang)
1. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)。
2. 选择左侧导航栏中的**Fabric** > **区块链网络**，进入“区块链网络”页面。
3.  在“区块链网络”页面中，选择需查看的网络，进入“访问管理”页面。
4.  在“访问管理”页面中，单击外网域名右侧的**开启**。如下图所示：
![](https://main.qcloudimg.com/raw/423f571003ad6d7e549a68e78bb8253a.png)
 获取外网域名后并单击**nginx 证书下载**。
![](https://main.qcloudimg.com/raw/105eabc138754834a377017c6fbaa805.png)
5. 前往 [OpenSSL](https://www.openssl.org/source/) 官网，下载 openssl 并配置安装。
6. 下载 [ecccsr](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/ecccsr.zip?_ga=1.59257006.2054822156.1595822583) 工具，解压后执行 `sh ecccsr.sh`，得到以下三个文件：
  - out.key
  - out.csr
  - out_sk


### 申请证书流程
1. 前往 [认证信息](https://console.cloud.tencent.com/developer/auth) 页面，查看企业名称。如下图所示：
<img src="https://main.qcloudimg.com/raw/123d94ea2854ce6cf83f6ab71e7209a1.png" alt="img" style="zoom:40%;" />            
2. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas/overview)，选择左侧导航栏中的**Fabric** > **区块链网络**，进入“区块链网络”页面。
4. 在“区块链网络”页面中，选择需查看的网络，进入“证书管理”页面。
5. 在“证书管理”页面中单击**申请**，在“申请证书”弹窗中，填写认证信息中的企业名称。如下图所示：
![](https://main.qcloudimg.com/raw/ff07dc48863aff4b78e452ad8d61f4fe.png)           
6. 在“证书信息”页面上传通过 [外网访问](#stepwaiwang) 获取的 `out.csr` 文件。如下图所示：[](id:1)
<img src="https://main.qcloudimg.com/raw/87d60ce40d8a630e138c36d674fd700b.png" alt="img" style="zoom:40%;" />  
7. 下载 [上一步](#1) 申请到的证书，记为 USER_CERT。如下图所示：
![img](https://main.qcloudimg.com/raw/de368d437f5a1a27a8517da9807dfd0f.png)            

经过上述步骤后，得到了访问域名（PROXY_URL）、NGINX证书（TLS_CERT）、out_sk 和用户证书（USER_CERT），在后续的访问中需要使用到这些数据。除此之外，关于网络名、通道名、chaincodeName 等信息的获取方式，请参阅 [对接说明及对接前准备](https://cloud.tencent.com/document/product/663/47512)。

## tbaas-fabric-sdk-java

下载 [tbaas-fabric-sdk-java](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/tbaas-fabric-sdk-java.zip)。
以下代码示例为不同步骤的代码编写：
1. 配置基本参数。

```java
// 通道名称
static String CHANNEL_NAME = "ydtest";
// 开启TLS
static boolean TLS_ENABLE = true;
// 是否通过代理进行访问区块链网络
static boolean PROXY_NETWORK = true;

// 开启TLS需要传证书
static String TLS_CERT = "cert/nginx.bcj4ew1lql10.tbaas.pem";

// "grpcs://"+PROXY_URL
static String PROXY_GRPC_URL = "grpcs://aliceorg-bcj4ew1lql10.tbaas.tech:8080";

// MSP_ID可以在控制台-组织管理查看
static String MSP_ID = "AliceOrgMSP-bcj4ew1lql10";

// https://cloud.tencent.com/document/product/663/38395
// out.csr、out_sk在本地生成，client.pem在控制台上传out.csr文件后，通过控制台下载
static String USER_KEY_FILE_PATH = "cert/out_sk_20200804";
static String USER_CERT_FILE_PATH = "cert/leyuchen@aliceorg.bcj4ew1lql10@client.pem";

// 控制台-运营监控可查到节点域名/名称
static String PEER_DOMAIN = "peer0.aliceorg.bcj4ew1lql10";
static String PEER_ENDPOINT = "peer0.aliceorg.bcj4ew1lql10:7051";

// 合约名称
static String CHAINCODE_NAME = "ccc";
// 仅在安装合约时需要填写版本号，调用合约不需要不需要填版本号，默认会调用最新部署版本的合约
private static final String CHAINCODE_VERSION = "";
// 仅在调用GO智能合约时需要添加合约路径
private static final String CHAINCODE_PATH = "";
```

2. 初始化用户并设置访问通道的默认用户。

```go
FabricUser user = new FabricUser.Builder()
        .setKeyBytes(FileUtils.getResourceFileBytes(USER_KEY_FILE_PATH))
        .setCertBytes(FileUtils.getResourceFileBytes(USER_CERT_FILE_PATH)) // FileUtils.getFileBytes("系统中文件的绝对路径")
        .setMspId(MSP_ID)
        .build();
ChannelContext.setDefaultUser(user);
```

3. 连接到通道。

```java
Channel demoChannel = ChannelHandler.create()
        .setChannelName(CHANNEL_NAME)
        .addServiceDiscoveryNode(PEER_ENDPOINT)
        .setNetworkType(new ProxyNetworkContext(PROXY_GRPC_URL))
        .setTLSCertBytes(FileUtils.getResourceFileBytes(TLS_CERT))
        .init();
```

4. 创建 fabric 模板。

```java
FabricTemplate fabricTemplate = FabricTemplate.getInstance();
```

5. 通过 fabric 模板快速获取通道内信息。

```java
// 查询通道内可发现的peer节点
List peerList = fabricTemplate.findPeers(CHANNEL_NAME);
// 获取通道内参与的组织msp列表
List memberList = fabricTemplate.findMemberships(CHANNEL_NAME);
// 获取通道内可发现节点内的合约列表
List chainCodeList = fabricTemplate.findChainCodes(CHANNEL_NAME);
```

6. 通过 fabric 模板调用合约。

```java
// 调用智能合约query函数
List queryArgs = Collections.singletonList("a");
FabricQueryResponse response = fabricTemplate.query(where(CHANNEL_NAME).has(CHAINCODE_ID)
        .callFunc("query").addArgs(queryArgs), Integer.class);


// 调用智能合约并完成交易
List invoke = Arrays.asList("a", "b", "1");
TransactOptions transactOptions = new TransactOptions()
        .waitForBlockEvent(false) // 设置为false则直接返回结果的future，不等交易从peer确认返回，默认值为true
        .eventCallback(Arrays.asList("TEST_EVENT_ID_1"), (b, e) -> LOGGER.debug(e.getChaincodeId() + new String(e.getPayload())))
        .eventCallback(Arrays.asList("TEST_EVENT_ID_2"), (b, e) -> LOGGER.debug("这是不同的回调函数"));

FabricTransactResponse invokeResponse = fabricTemplate.transact(where(CHANNEL_NAME).has(CHAINCODE_ID)
        .callFunc("invoke").addArgs(invoke), transactOptions);
```

