您可通过本文快速开始使用 Hyperledger Fabric 正式版，同时可前往 [Hyperledger Fabric](https://cloud.tencent.com/document/product/663/38473) 了解相关信息。

## 步骤1：组建区块链网络
>?一个腾讯云账号可购买一个区块链组织及所需的多个节点资源。
>
1. 前往 [区块链服务TBaaS-Fabric](https://buy.cloud.tencent.com/tbaas_blockchain?engine=0) 购买页面，按照以下信息设置基本信息、组织与节点配置。
主要参数信息如下：
 - **联盟**：选择一个已创建或已加入的联盟。
 如果您是联盟初创者，请参考 [创建联盟](https://cloud.tencent.com/document/product/663/38470#.E5.88.9B.E5.BB.BA.E8.81.94.E7.9B.9F) 完成创建。其他参与组织可前往“[事件中心](https://console.cloud.tencent.com/tbaas/event)”页面，选择【我待办的】>【邀请加入联盟】，接受邀请并加入联盟。
 - **区块链网络名称**：自定义名称，长度为4 - 60个字符，不可与当前您已加入的区块链网络名称重复。
 - **节点配置**：您可根据实际需求选择高级配置，请谨慎选择以匹配后续业务需要。
2. 选择【下一步】进入邀请组织步骤，可根据实际需求选择组织或单击【跳过】。
3. 支付完成后即可组建区块链网络。
成功组建区块链网络后，可登录  [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)，选择左侧导航栏中的【Fabric】>【[区块链网络](https://console.cloud.tencent.com/tbaas/fabric/deploy)】，在“区块链网络”列表页面查看网络信息。

## 步骤2：邀请组织加入联盟及网络
### 邀请其他组织加入联盟
1. 登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)，选择左侧导航栏中的【[联盟](https://console.cloud.tencent.com/tbaas/alliance)】。
2. 在“联盟”列表页面，选择需邀请组织联盟所在行右侧的【邀请成员】。如下图所示：
![](https://main.qcloudimg.com/raw/8396a9f7d502664b493779b800f786a0.png)
3. 在弹出的“邀请成员”窗口中，按照以下信息填写受邀成员信息，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/62110c5cc413f08e1f98886888c19371.png)
 - **成员名称**：被邀请者的腾讯云账号昵称。
 - **账号 ID**：被邀请者的账号 ID，腾讯云的唯一标识。
 - **APPID**：被邀请者腾讯云账号的 APPID。
 以上信息，可前往“[账号信息](https://console.cloud.tencent.com/developer)”页面获取。被邀组织需前往“[事件中心](https://console.cloud.tencent.com/tbaas/event)”页面，选择【我待办的】>【邀请加入联盟】接受或拒绝邀请。

### 邀请其他组织加入网络
1. 选择左侧导航栏中的【Fabric】>【[区块链网络](https://console.cloud.tencent.com/tbaas/fabric/deploy)】，进入“区块链网络”列表页面。
2. 在“区块链网络”列表页面，选择网络所在行右侧的【更多】>【邀请组织】。如下图所示：
>?需确保被邀请组织已成为该网络所属联盟成员。
>
![](https://main.qcloudimg.com/raw/7939b857d87da9f46fb36a647b688da1.png)
被邀组织需前往“[事件中心](https://console.cloud.tencent.com/tbaas/event)”页面，选择【我待办的】>【邀请加入网络】接受或拒绝邀请。

## 步骤3：创建业务通道
当您成功组建区块链网络，并成功邀请组织加入网络后，可参考以下步骤新建业务通道并邀请组织加入。

### 新建业务通道
1. 选择左侧导航栏中的【Fabric】>【[区块链网络](https://console.cloud.tencent.com/tbaas/fabric/deploy)】，进入“区块链网络”列表页面。
2. 选择资源 ID 进入区块链网络详情页，单击【通道管理】页签。
3. 单击【新建】，在弹出的“新建通道”窗口中按照以下信息新建业务通道。如下图所示：
![](https://main.qcloudimg.com/raw/6e3b629310a85459b8f3c14918704545.png)
 - **通道名称、通道描述**：自定义通道名称及描述。
 - **成员限制**：通道准入率，项目初期阶段准入门槛可设置为1%，请根据实际场景设置。
4. 通道创建完成后，选择该通道所在行右侧的【加入节点】。如下图所示：
![](https://main.qcloudimg.com/raw/47e6aa9f52d4ccaa6f57d8ac06aec072.png)
5. 在弹出的“加入节点”窗口中，勾选需加入节点并单击【确定】。

### 邀请组织加入业务通道
1. 在“区块链网络”列表页面，选择资源 ID 进入网络详情页。
2. 选择【通道管理】页面，并选择通道所在行右侧的【新增组织】。
3. 在弹出的“邀请组织”窗口中，按照指引邀请组织。
被邀请加入通道的组织可前往“[事件中心](https://console.cloud.tencent.com/tbaas/event)”页面，选择【我待办的】>【邀请加入通道】查询事件进展情况并等待准入。

## 步骤4：创建及安装合约
### 新建合约
1. 选择左侧导航栏中的【Fabric】>【[区块链网络](https://console.cloud.tencent.com/tbaas/fabric/deploy)】，进入“区块链网络”列表页面。 
2. 选择资源 ID 进入网络详情页面，单击【合约管理】页签。
3. 单击【新建】，并在弹出的“新建合约”窗口中按照以下步骤进行合约创建：
    1. 在“基本信息”步骤中，设置名称及合约版本。
    2. 在“设置合约”步骤中，选择合约语言及上传合约。
    3. 在“选择组织”步骤中，选择组织。仅选择的组织有权使用合约，目前版本合约创建后**可新增组织但不可删除组织**，请谨慎选择。
    4. 单击【创建】即可完成合约创建。

### 安装并实例化合约
此步骤介绍如何将已创建的智能合约安装在区块链网络节点上，并将该智能合约在已创建的业务通道上实例化。完成此步骤后，您即可通过智能合约完成交易上链整个过程。
1. 选择左侧导航栏中的【Fabric】>【[区块链网络](https://console.cloud.tencent.com/tbaas/fabric/deploy)】，进入“区块链网络”列表页面。 
2. 选择资源 ID 进入网络详情页面，单击【合约管理】页签。
3. 选择合约所在行右侧的【安装】。如下图所示：
![](https://main.qcloudimg.com/raw/ee2404eed84388fb4f3c0f8d9a30bbe2.png)
4. 在弹出的“安装合约”窗口中，选择节点并单击【安装】即可完成合约安装。
5. 选择合约所在行右侧的【实例化】，进入“合约管理/实例化合约”页面进行合约实例化。如下图所示：
>!在“背书策略”中，如没有特殊的合约背书策略要求，可选择【无】。
>
![](https://main.qcloudimg.com/raw/ab307bf3d5fbba80deeaeb06aa96055e.png)
6. 您可通过智能合约发起交易上链。发起交易后，可在通道详情页或区块链浏览器来查询交易和区块。如下图所示：
![](https://main.qcloudimg.com/raw/4da33819b9409e7ea5f5b68760214f1c.png)
