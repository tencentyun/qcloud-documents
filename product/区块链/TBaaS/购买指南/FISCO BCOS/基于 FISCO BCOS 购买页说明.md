## 操作场景
本文档指导用户创建 FISCO BCOS 引擎下的区块链网络。

## 前提条件
已登录 [TBaaS 控制台](https://console.cloud.tencent.com/tbaas)。

## 操作步骤
1. 在 [TBaaS 购买页](https://cloud.tencent.com/product/tbaas)，单击 FISCO BCOS 中的【立即购买】进入 “[区块链服务TBaaS-BCOS](https://buy.cloud.tencent.com/tbaas_blockchain?engine=1)” 购买页。
2. 请按照页面提示填写基本信息、组织与节点配置，单击【立即购买】即可成功创建一个区块链网络。如下图所示：
![](https://main.qcloudimg.com/raw/ee098e87339360f15fdc8320e9e53214.png)
主要参数信息如下：
 - **联盟**：选择所属联盟。需建立联盟后才可以购买区块链网络，网络建立后联盟不可更换。
 - **区块链网络名称**：长度为4 - 60个字符，不可与当前您已加入的区块链网络名称重复。
 - **组织配置**：组织名称需以字母开头，12位以内数字和字母组成，建议以 Org 结尾，例如 “AliceTest1Org”。BCOS 网络至少需要4个节点。
 >!
 >- 参与该区块链网络的组织，可以是企业或部门。
 >- 每个组织最大支持10个节点，整个网络节点总数不超过100个。
 >
 -  **证书加密方式**：选择证书加密方式，支持国密 SM2 证书和 ECC 证书。默认为 ECC 证书。
 -  **节点配置**：单击【默认配置】，选择数据盘和机型。
 -  **数据盘**：200GB - 4000GB。
 -  **机型**：目前系统支持以下三种类型的服务器配置，可根据实际需求选择。
 <table>
	<tr>
	<th>型号</th>
	<th>CPU</th>
	<th>内存</th>
	<th>系统盘</th>
	</tr>
	<tr>
	<td>S2.LARGE8</td>
	<td>4核</td>
	<td>8GB</td>
	<td>50GB</td>
	</tr>
	<tr>
	<td>S2.2XLARGE16</td>
	<td>4核</td>
	<td>16GB</td>
	<td>50GB</td>
	</tr>
	<tr>
	<td>S2.4XLARGE32</td>
	<td>4核</td>
	<td>32GB</td>
	<td>50GB</td>
	</tr>
</table>
