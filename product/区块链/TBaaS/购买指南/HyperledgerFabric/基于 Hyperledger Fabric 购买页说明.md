## 操作场景
本文档指导用户创建 Hyperledger Fabric 腾讯云增强版引擎下的区块链网络。



## 前提条件
- 金融安全版仅限金融专区用户，如需购买请先 [申请金融专区](https://cloud.tencent.com/document/product/304/2768)。
- 已登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)。

## 操作步骤
1. 选择左侧导航栏中的【Fabric】>【区块链网络】，进入“区块链网络”页面。
2. 单击【新建】，进入 “[区块链服务TBaaS-Fabric](https://buy.cloud.tencent.com/tbaas_blockchain?engine=0)” 购买页面，按照页面提示填写基本信息、组织及节点配置。如下图所示：
![](https://main.qcloudimg.com/raw/fa12ace92b2dc12b1c95b1da4d57235c.png)
主要参数信息如下：
	- **联盟**：选择所属联盟。需建立联盟后才可以购买区块链网络，网络建立后联盟不可更换。
	- **区块链网络名称**：长度为4 - 60个字符，不可与当前您已加入的区块链网络名称重复。
	- **版本选择**：提供标准版、企业版和金融安全版三个版本选择。
	- **地域**：根据不同的版本选择地域。
	- **节点配置**：单击默认配置，可以选择 CA 机构、证书加密方式和状态数据库类型。
	- **选择 CA 机构**：为网络中所有节点/用户生成的证书，默认为 Fabric CA。
	- **证书加密方式**：选择证书加密方式，支持国密 SM2 证书和 ECC 证书，默认为ECC证书。
	- **状态数据库类型**：支持 LevelDB 状态数据库和 CouchDB 状态数据库，默认为LevelDB 状态数据库。
3. 单击【下一步】，选择要邀请的组织，也可以直接跳过该步骤。
4. 单击【立即购买】即可成功部署 Fabric 网络。
>?如需购买私有链，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&step=1)。私有链中单一账号可分配组织，详情请参见 [组织管理](https://cloud.tencent.com/document/product/663/38482)。
>
