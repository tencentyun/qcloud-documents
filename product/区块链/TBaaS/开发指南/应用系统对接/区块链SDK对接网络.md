# 区块链SDK对接网络

应用系统如果调用频率较高，则需要直接使用区块链SDK与区块链网络对接。这种情况下**应用系统应部署在与区块链网络同一地域内的CVM上**。在云API调用方式中，需要应用系统提供账户的SecretID和SecretKey，用于认证授权访问权限；而在区块链SDK中，则需要应用系统在TBaaS控制台上申请用于访问的证书（节点证书和nginx证书）。

​            ![img](https://main.qcloudimg.com/raw/81e1898de06b79a0b848345a72e4df4c.png)            

如果应用在开发测试中希望在本地访问区块链网络，则可以开启并使用网络的外网域名，使用该域名访问区块链网络的代理组件。这种访问方式仅适用于开发调试。在生产环境中强烈推荐使用访问管理打通VPC的方式。

除了支持社区版区块链SDK（Java、NodeJS、Golang），TBaaS对Java版的社区区块链SDK进行了定制（tbaas-fabric-sdk-java），简化了应用系统与区块链网络连接的流程。

## 获取访问地址及证书

1. 获取访问地址（记为PROXY_URL），并下载nginx证书（记为TLS_CERT）

   a)  VPC访问，访问地址为下图中的访问端地址

   <img src="https://main.qcloudimg.com/raw/e6eb5c2f97f48f24805d83a2a3437e06.png" alt="img" style="zoom:30%;" />

   <img src="https://main.qcloudimg.com/raw/8a75cb8188e0c00fcfb97a0391c0613a.png" alt="img" style="zoom:30%;" />

   <img src="https://main.qcloudimg.com/raw/3923bce61d0849a879a9bf542d706cc4.png" alt="img" style="zoom:33%;" />

​                上图的内容即为Nginx证书（TLS_CERT），保存在文件中。

​	b)  外网访问（**仅用于开发测试**）

<img src="https://main.qcloudimg.com/raw/800524c9ef8a5fdd329c732cfdd37763.png" alt="img" style="zoom:33%;" />

- 前往 [OpenSSL](https://www.openssl.org/source/) 官网，下载 openssl 并配置安装。

- 下载[ecccsr](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/ecccsr.zip?_ga=1.59257006.2054822156.1595822583)工具，解压后执行sh ecccsr.sh，得到以下三个文件
  - out.key
  - out.csr
  - out_sk

2. 在TBaaS控制台上传out.csr用于申请证书，申请流程如下图所示

<img src="https://main.qcloudimg.com/raw/14db9e9f7a7134b9693ff0a47c319e5a.png" alt="img" style="zoom:33%;" />            

<img src="https://main.qcloudimg.com/raw/123d94ea2854ce6cf83f6ab71e7209a1.png" alt="img" style="zoom:40%;" />            

![img](https://main.qcloudimg.com/raw/e8be3c9c8fee0e174137b1ec89178ddd.png)            

<img src="https://main.qcloudimg.com/raw/9588c4c7a01d61d83ad7d073eb9f5300.png" alt="img" style="zoom:30%;" />            

<img src="https://main.qcloudimg.com/raw/f237330223e3667ce0a46d06ff0b990d.png" alt="img" style="zoom:33%;" />            

3. 下载上一步申请到的证书，记为USER_CERT

![img](https://main.qcloudimg.com/raw/de368d437f5a1a27a8517da9807dfd0f.png)            



经过上述步骤后，得到了访问域名（PROXY_URL）、NGINX证书（TLS_CERT）、out_sk和用户证书（USER_CERT），在后续的访问中需要使用到这些数据。除此之外，网络名、通道名、chaincodeName等信息的获取方式上一节相同。

## tbaas-fabric-sdk-java

[tbaas-fabric-sdk-java](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/tbaas-fabric-sdk-java.zip)

1. 配置基本参数

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

2. 初始化用户并设置访问通道的默认用户

```go
FabricUser user = new FabricUser.Builder()
        .setKeyBytes(FileUtils.getResourceFileBytes(USER_KEY_FILE_PATH))
        .setCertBytes(FileUtils.getResourceFileBytes(USER_CERT_FILE_PATH)) // FileUtils.getFileBytes("系统中文件的绝对路径")
        .setMspId(MSP_ID)
        .build();
ChannelContext.setDefaultUser(user);
```

3. 连接到通道

```java
Channel demoChannel = ChannelHandler.create()
        .setChannelName(CHANNEL_NAME)
        .addServiceDiscoveryNode(PEER_ENDPOINT)
        .setNetworkType(new ProxyNetworkContext(PROXY_GRPC_URL))
        .setTLSCertBytes(FileUtils.getResourceFileBytes(TLS_CERT))
        .init();
```

4. 创建fabric模板

```java
FabricTemplate fabricTemplate = FabricTemplate.getInstance();
```

5. 通过fabric模板快速获取通道内信息

```java
// 查询通道内可发现的peer节点
List peerList = fabricTemplate.findPeers(CHANNEL_NAME);
// 获取通道内参与的组织msp列表
List memberList = fabricTemplate.findMemberships(CHANNEL_NAME);
// 获取通道内可发现节点内的合约列表
List chainCodeList = fabricTemplate.findChainCodes(CHANNEL_NAME);
```

6. 通过fabric模板调用合约

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

# 
