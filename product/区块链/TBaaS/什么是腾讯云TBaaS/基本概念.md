## 通用概念
<table>
	<tr>
	<th width="26%" class="update">关键词</th>
	<th alingn="center" class="update">描述</th>
	</tr>
	<tr>
	<td class="update">联盟<br>（Consortium）</td>
	<td>由若干成员组成的区块链业务团体，联盟成员作为参与方共同参与到区块链网络的建设之中。
	<ul class="params">
	<li>联盟创建者指定联盟名称、参与成员是否需要实名认证等信息。</li>
	<li>联盟成员可以邀请其他机构、公司或者个人加入联盟。</li>
	</ul>
	</td>
	</tr>
	<tr>
	<td class="update">区块链网络<br>（Blockchain Network）</td>
	<td> 区块链是一种由多方共同维护，使用密码学保证传输和访问安全，能够实现数据一致存储、无法篡改、无法抵赖的技术体系。</td>
	</tr>
	<tr>
	<td class="update">组织<br>（Org）</td>
	<td>代表一个联盟成员，可以是企业或部门。一个组织可以管理多个节点。
	</ul>
</td>
	</tr>
	<tr>
	<td class="update">节点<br>（Peer）</td>
	<td>维护账本的网络节点，在 Fabric 区块链网络中默认指背书节点（endorser）。</td>
	</tr>
	<tr>
	<td class="update">联盟链</td>
	<td>多个联盟成员共同参与的区块链网络。
	<ul class="params">
	<li>联盟链是指参与的每个节点的权限都完全对等，各节点可以在不需要完全信任的情况下就能够实现数据的可信交换。</li>
	<li>联盟链的各个节点通常有与之对应的实体机构组织，通过授权后才能加入或退出网络。</li>
  <li>	在联盟链中，每个组织代表一个联盟成员，组织（成员）可以是企业或部门。</li>
	</ul>
</td>
	</tr>
	<tr>
	<td class="update">分布式账本<br>（Distribute Ledger）</td>
	<td>由网络中若干去中心化节点共同维护的数据账本。</td>
	</tr>
	<tr>
	<td class="update">智能合约<br>（Smart Contract）</td>
	<td>根据特定条件自动执行的合约程序。<br>智能合约是区块链的重要特征，是用户与区块链进行交互，利用区块链实现业务逻辑的重要途径。</td>
	</tr>
	<tr>
	<td class="update">区块</td>
	<td>区块是在区块链网络中承载交易数据的数据包，是一种被标记上时间戳和之前一个区块的哈希值的数据结构，区块经过网络的共识机制验证并确认区块中的交易。</td>
	</tr>
</table>


## 长安链·ChainMaker 相关概念
<table>
	<tr>
	<th width="26%" class="update">关键词</th>
	<th class="update">描述</th>
	</tr>
	<tr>
	<td class="update">同步节点<br>（Sync node）</td>
	<td>或称见证节点，参与区块和交易同步、区块验证，交易执行，并记录完整账本数据，但不参与共识投票。</td>
	</tr>
	<tr>
	<td class="update">共识节点<br>（Consensus node）<br></td>
	<td>参与区块链网络中共识投票、交易执行、区块验证和记账的节点。</td>
	</tr>
	<tr>
	<td class="update">读写集<br>（Read-write set）<br></td>
	<td>区块链上的一条交易执行过程中，被读取和被修改或写入的状态数据的集合。</td>
	</tr>
		<tr>
	<td class="update">长安链 CA<br>（Chainmaker CA）<br></td>
	<td>指使用长安链配套证书管理工具 chainmaker-cryptogen 管理的证书、密钥体系。</td>
	</tr>
	<tr><td class="update">wasm文件<br>（webassembly file）<br></td>
	<td>长安链指的智能合约编译后生成的文件。wasm 指通过各自符合 WebAssembly 规范的编译器编译出来的以 .wasm 结尾的文件。</td>
	</tr>
</table>

## Hyperledger Fabric 相关概念
<table>
	<tr>
	<th width="26%" class="update">关键词</th>
	<th class="update">描述</th>
	</tr>
	<tr>
	<td class="update">通道<br>（Channel）</td>
	<td>构建在 Hyperledger Fabric 区块链网络上的私有区块链，实现了数据的隔离和保密。
	<ul class="params">
	<li>通道中的 Chaincode 和交易只有加入该通道的节点（Peer）可见。</li>
  <li>同一个节点可以加入多个通道，并为每个通道内容维护一个账本。</li>
	<li>每一个通道即为一条逻辑上的区块链。</li>
	<li>可以按照业务来划分通道，也可以按照行政职能和隐私策略来划分通道。</li>
	</ul>
</td>
	</tr>
	<tr>
	<td class="update">排序服务或共识服务<br>（Order Services） </td>
	<td>提供排序服务或共识服务的网络节点，完成交易的排序和区块打包等工作，支持可插拔的共识组件，当前生产环境下使用 Kafka 进行交易排序。</td>
	</tr>
	<tr>
	<td class="update">组织<br>（Org）</td>
	<td>
	<ul class="params">
	<li>	联盟链中按照访问和使用账本的网络节点，一个联盟（或者一个区块链网络）有多个组织（成员），一个组织内可以有多个节点（Peer），每个节点参与账本和世界状态维护。</li>
	<li>Hyperledger Fabric 中，组织即是一个参与方在区块链中的身份标识，组织可以独立管理属于自身的区块链节点、成员证书等细节。</li>
	</ul>
</td>
	</tr>
		<tr>
	<td class="update">节点<br>（Peer）</td>
	<td> 区块链网络中实际负责网络互联、协议交换、账本维护、世界状态维护的信息处理设备，通常是一个进程或者一台运行了节点进程的计算设备。<br>在 Hyperledger Fabric 中，节点按照其功能职责可以承担不同角色，例如 endorser 和 committer。</td>
	</tr>
	<tr>
	<td class="update">智能合约<br>（Smart Contract）</td>
	<td>根据特定条件自动执行的合约程序。<br>智能合约是区块链的重要特征，是用户与区块链进行交互，利用区块链实现业务逻辑的重要途径。</td>
	</tr>
	<tr>
	<td class="update">链码<br>（Chaincode）</td>
	<td>链码是 Hyperledger Fabric 对智能合约的一种实现方式，是运行于 Hyperledger Fabric 网络之上一段应用程序代码，也是用户与 Hyperledger Fabric 交互的唯一途径。</td>
	</tr>
	<tr>
	<td class="update">链<br>（Chain）</td>
	<td>一个链即是一个由若干区块通过特定指向链接、摘要算法或加密算法锚定组成的数据集合。</td>
	</tr>
</table>

## FISCO BCOS 相关概念
<table>
	<tr>
	<th width="15%" class="update">关键词</th>
	<th class="update">描述</th>
	</tr>
	<tr>
	<td class="update">链</td>
	<td>各个组织机构/企业间搭建的区块链。</td>
	</tr>
	<tr>
	<td class="update">共识算法</td>
	<td>构筑区块链信任特性的基础，也是各个节点保证数据一致性的基础。FISCO-BCOS 采用的 pbft 和 raft，可灵活配置。</td>
	</tr>
	<tr>
	<td class="update">智能合约</td>
	<td>为了保证区块链图灵完备，用代码片段编写一份承诺以及各参与方在上面执行承诺的协议，FISCO-BCOS 的智能合约采用 solidity 语言来编写。</td>
	</tr>
	<tr>
	<td class="update">群组</td>
	<td>区块链中可存在多个不同的账本，区块链节点可以根据业务关系选择群组加入，参与到对应账本的数据共享和共识过程中。在群组架构中，可以更好地实现平行扩展，满足金融级高频交易场景的需求。同时，群组架构可以快速支持组链需求，极大降低运维难度，真正能够实现企业间建链就像建“聊天群”一样简便。</td>
	</tr>
</table>





<style>
	.params{margin-bottom:0px !important;}
	.update{text-align:center !important;}
</style>
