## 操作场景
本文档指导用户创建 FISCO BCOS 引擎下的区块链网络。

## 前提条件
已登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)。

## 操作步骤
1. 在 [TBaaS 购买页](https://cloud.tencent.com/product/tbaas)，单击 FISCO BCOS 中的【立即购买】进入 “[区块链服务TBaaS-BCOS](https://buy.cloud.tencent.com/tbaas_blockchain?engine=1)” 购买页。
2. 请按照页面提示填写基本信息、组织与节点配置，单击【立即购买】即可成功创建一个区块链网络。如下图所示：
![](https://main.qcloudimg.com/raw/44c03215c7c6316810a55043055fb6a7.png)
主要参数信息如下：
 - **联盟**：选择所属联盟。需建立联盟后才可以购买区块链网络，网络建立后联盟不可更换。
 - **区块链网络名称**：长度为4 - 60个字符，不可与当前您已加入的区块链网络名称重复。
 - **组织和节点配置**：组织名称需以字母开头，12位以内数字和字母组成，建议以 Org 结尾，例如 “AliceTest1Org”。您可自行选择节点证书加密方式。
 >!
 >- BCOS 网络至少需要4个节点才可启动运行。
 >- 参与该区块链网络的组织，可以是企业或部门。
 >- 每个组织最大支持10个节点，整个网络节点总数不超过100个。
 >
 -  **证书加密方式**：选择证书加密方式，支持国密 SM2 证书和 ECC 证书。默认为 ECC 证书。


