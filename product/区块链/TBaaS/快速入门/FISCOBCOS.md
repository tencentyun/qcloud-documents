## 操作场景
您可通过本文快速开始使用 FISCO BCOS 区块链网络，同时可前往 [FISCO BCOS](https://cloud.tencent.com/document/product/663/38491) 了解更多信息。

## 前提条件
已登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)。

## 操作步骤
### 步骤1：组建区块链网络
参考 [FISCO BCOS 购买页说明](https://cloud.tencent.com/document/product/663/38266) 创建 FISCO BCOS 区块链网络。

### 步骤2：查看区块链信息
1. 选择左侧导航中的【BCOS】>【[区块链网络](https://console.cloud.tencent.com/tbaas/bcos/deploy)】。
2. 单击需查看信息的网络资源 ID，即可进入该网络的概览页。
您可通过区块链网络的概览页查看信息，其中包含该网络区块、节点、交易和已部署合约数量、最近7天的交易数量和区块列表。

### 步骤3：邀请组织加入联盟
1. 登录 TBaaS 控制台，选择左侧导航栏中的【[联盟](https://console.cloud.tencent.com/tbaas/alliance)】。
2. 在“联盟”列表页面，选择需邀请组织联盟所在行右侧的【邀请成员】。如下图所示：
![](https://main.qcloudimg.com/raw/74553f05e8b9cbf8ce1cbdeb1b9500a6.png)
3. 在弹出的“邀请成员”窗口中，按照以下信息填写受邀成员信息，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/a501920eafa120f426d9fd8cea6e6475.png)
	- **成员名称**：被邀请者的腾讯云账号昵称。
	- **账号 ID**：被邀请者的账号 ID，腾讯云的唯一标识。
	- **APPID**：被邀请者腾讯云账号的 APPID。
以上信息，可前往“[账号信息](https://console.cloud.tencent.com/developer)”页面获取。被邀组织需前往“[事件中心](https://console.cloud.tencent.com/tbaas/event)”页面，选择【我待办的】>【邀请加入联盟】接受或拒绝邀请。

### 步骤4：新建合约
1. 选择左侧导航中的【BCOS】>【[区块链网络](https://console.cloud.tencent.com/tbaas/bcos/deploy)】。
2. 单击资源 ID 进入区块链网络概览页，选择【合约管理】>【新建】。
3. 在弹出的“新建合约”窗口中，输入合约版本，并选择需要上传的合约，单击【确定】即可新建合约。
>!合约仅支持 solidity 语言。
>


### 步骤5：编译及部署合约
>?合约需要先编译后部署，且编译成功后才能部署。
>
1. 选择左侧导航中的【BCOS】>【[区块链网络](https://console.cloud.tencent.com/tbaas/bcos/deploy)】。
1. 选择资源 ID 进入区块链网络概览页，单击【合约管理】。
2. 单击需编译合约行右侧【更多】>【编译】，并在弹出窗口上单击【编译】即可开始编译合约。
3. 编译完成后单击【部署】，即可部署合约。
合约部署完毕后即可调用合约发交易。

### （可选）步骤6：查看节点信息
1. 选择左侧导航中的【BCOS】>【[区块链网络](https://console.cloud.tencent.com/tbaas/bcos/deploy)】。
1. 选择资源 ID ，进入区块链网络概览页。
2. 单击【节点查看】，进入“节点查看”页面。
2. 在“节点查看”页面，您可查看该网络下节点的相关信息，包括节点名称、节点 IP、节点块高和节点运行状态等信息。

### （可选）步骤7：查看组织信息
1. 选择左侧导航中的【BCOS】>【[区块链网络](https://console.cloud.tencent.com/tbaas/bcos/deploy)】。
1. 选择资源 ID，进入区块链网络概览页。
2. 单击【网络组织】，进入“网络组织”页面。
2. 在“网络组织”页面中，您可查看该网络的组织相关信息，包括组织名称、联盟 ID 和时间。
