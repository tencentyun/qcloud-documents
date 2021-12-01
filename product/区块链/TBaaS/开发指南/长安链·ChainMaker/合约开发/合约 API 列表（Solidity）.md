

ChainMake Solidity 语言版本智能合约有丰富的 API 接口，供用户在撰写智能合约的时候与链进行交互，代码实现详情可以参考 [API 接口代码实现](https://docs.chainmaker.org.cn/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#solidity)。

从逻辑方面划分，可将 API 划分为以下类型：

[](id:informationExtraction)

### 交易信息提取

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>msg.data -> bytes </td>
<td>获取调用合约的完整数据</td>
</tr>
<tr>
<td>msg.sender -> address </td>
<td>获取消息发送者地址</td>
</tr>
<tr>
<td>tx.origin -> address </td>
<td>获取交易发送者地址</td>
</tr>
<tr>
<td>tx.gasprice -> uint </td>
<td>获取交易的gas价格</td>
</tr>
</tbody></table>


### 账本交互

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>blockhash(uint blockNumber) -> bytes32</td>
<td>获取指定区块高度的哈希值</td>
</tr>
<tr>
<td>block.gaslimit -> uint</td>
<td>获取当前区块的 gas 限制</td>
</tr>
<tr>
<td>block.number -> uint</td>
<td>获取当前区块的高度</td>
</tr>
<tr>
<td>block.timestamp -> uint</td>
<td>获取当前区块的时间戳</td>
</tr>
</tbody></table>


### 异常处理

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>assert(bool condition)</td>
<td>断言给定条件是否成立，如果不满足条件，则状态更改恢复</td>
</tr>
<tr>
<td>require(bool condition)</td>
<td>如果不满足条件，则返回</td>
</tr>
<tr>
<td>require(bool condition, string memory message)</td>
<td>如果不满足条件，则返回，并提供错误消息</td>
</tr>
<tr>
<td>revert()</td>
<td>中止执行并还原状态更改</td>
</tr>
<tr>
<td>revert(string memory reason)</td>
<td>中止执行并还原状态更改，并提供错误消息</td>
</tr>
</tbody></table>


### 数学和密码函数类

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>addmod(uint x, uint y, uint k) -> uint</td>
<td>计算(x+y)%k</td>
</tr>
<tr>
<td>mulmod(uint x, uint y, uint k) -> uint</td>
<td>计算(x*y)%k</td>
</tr>
<tr>
<td>keccak256(bytes memory) -> bytes32</td>
<td>计算给定输入的 Keccak-256 哈希</td>
</tr>
<tr>
<td>sha256(bytes memory) -> bytes32</td>
<td>计算给定输入的 sha256 哈希</td>
</tr>
<tr>
<td>ripemd160(bytes memory) -> bytes32</td>
<td>计算给定输入的 RIPEMD-160 哈希</td>
</tr>
<tr>
<td>ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) -> address</td>
<td>从椭圆曲线签名中恢复与公钥关联的地址</td>
</tr>
</tbody></table>


ChainMake Solidity 语言版本智能合约完全兼容 EVM，Solidity 的具体使用详情可参见 [Solidity 官方文档](https://docs.soliditylang.org/en/v0.5.6/units-and-global-variables.html)。

