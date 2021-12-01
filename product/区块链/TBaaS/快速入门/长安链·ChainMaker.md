## 操作场景

您可通过本文快速开始使用 长安链·ChainMaker 区块链网络，同时可前往 [长安链·ChainMaker 操作指南](https://cloud.tencent.com/document/product/663/60106) 了解更多信息。

长安链·ChainMaker 网络的使用过程主要分为以下步骤：
<dx-steps>
-[创建联盟](#league)
-[购买网络](#network)
-[安装合约](#chaincode)
-[申请并下载证书](#cert)
-[应用开发与对接](#app)
-[通过浏览器查看链上数据](#data)
</dx-steps>



## 前提条件

已登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)。



## 操作步骤

### 步骤1：创建联盟[](id:league)

登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)，选择左侧导航中的**联盟**，进入联盟管理页面，单击左上角的“新建”，填写联盟名称等信息即可完成创建。

更多联盟管理的信息可参考操作指南 [联盟](https://cloud.tencent.com/document/product/663/38470) 部分。



### 步骤2：购买网络[](id:network)

参考 [长安链·ChainMaker 购买页说明](https://cloud.tencent.com/document/product/663/60096) 创建长安链·ChainMaker 网络。



### 步骤3：安装合约[](id:chaincode)

1. 在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas) 中，选择左侧导航中的**长安链** > **[区块链网络](https://console.cloud.tencent.com/tbaas/chainmaker/chain)** 进入网络卡片页面。
2. 当购买的长安链·ChainMaker 区块链网络完成部署后，点击卡片即可进入网络详情页面，点击顶部菜单栏的**合约管理**页签，进入对应页面后点击**安装合约**，在弹窗中填写对应的信息及上传合约文件后即可将合约安装至链上。如下图所示：
![](https://main.qcloudimg.com/raw/167ef56bf7c870e000dae7c18c51f25d.png)

<dx-alert infotype="notice" title="">
- 当前 TBaaS 控制台暂支持上传编译过后的 .wasm 合约文件。
- 合约支持 Rust、Go、C++ 、Solidity 四种语言。
- 合约编译方法可参考开发指南 [智能合约开发（Go）](https://cloud.tencent.com/document/product/663/60112) 或 [智能合约开发（Rust）](https://cloud.tencent.com/document/product/663/60113)。
</dx-alert>





### 步骤4：申请并下载证书[](id:cert)

TBaaS 平台支持通过长安链 SDK、云 API 两种方式进行对接上链，若使用云 API 方式上链，则本步骤可直接跳过。详细的对接流程请见“步骤5”
1. 在 TBaaS 控制台中，选择左侧导航中的**长安链** > **[区块链网络](https://console.cloud.tencent.com/tbaas/chainmaker/chain)**，单击对应的卡片进入网络详情页。
2. 在网络详情页面中，单击顶部菜单栏的**证书管理**页签，进入对应页面后点击**申请证书**，在弹窗中填写证书标识并上传用户证书及 TLS 证书的 CSR 文件，确认后即生成证书，在证书列表中可下载证书。CSR 文件的生成方法请参考 [证书申请 CSR 生成指南](https://cloud.tencent.com/document/product/663/60114)。
![](https://main.qcloudimg.com/raw/4db7df54c5bfd5d13628baab50b88347.png)



### 步骤5：应用开发与对接[](id:app)

TBaaS 平台支持通过长安链 SDK、云 API 两种方式进行对接上链，详细的对接开发流程请参考开发指南 [对接说明](https://cloud.tencent.com/document/product/663/47512) 章节。



### 步骤6：通过浏览器查看链上数据[](id:data)

TBaaS 平台提供区块链浏览器，便于用户实时查看或检索链上的数据，操作方式如下：

1. 在 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas) 中，选择左侧导航中的**长安链** > **[区块链网络](https://console.cloud.tencent.com/tbaas/chainmaker/chain)**，单击对应的卡片进入网络详情页。
2. 在网络详情页面中，点击顶部菜单栏的**区块链浏览器**页签，进入对应页面即可实时查看或检索区块信息、交易信息、链上指标等数据。如下图所示：
![](https://main.qcloudimg.com/raw/2a315b1a269f8272139882ff90aa9765.png)
