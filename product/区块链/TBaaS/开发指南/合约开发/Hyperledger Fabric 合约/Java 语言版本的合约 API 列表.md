Fabric Java 语言版本智能合约有丰富的 API 接口，具体的代码实现可以参考 [API接口代码实现](https://github.com/hyperledger/fabric-chaincode-java/blob/release-1.4/fabric-chaincode-shim/src/main/java/org/hyperledger/fabric/shim/impl/ChaincodeStubImpl.java)。
从逻辑上划分，可将 API 接口分为以下类型：
- [交易信息提取](#information)
- [账本交互](#count)
- [参数处理](#parameter)
- [其他辅助类](#auxiliary)

<span id="information"></span>
### 交易信息提取
<table>
	<tr>
		<th>接口</th>
		<th>说明</th>
	</tr>
	<tr>
	<td>byte[] getBinding()</td>
	<td>返回交易的 binding 信息</td>
	</tr>
	<tr>
		<td>String getChannelId()</td>
		<td>获取当前的通道名称</td>
	</tr>
	<tr>
		<td>byte[] getCreator()</td>
		<td>获取交易提交者信息</td>
	</tr>
	<tr>
		<td>SignedProposal getSignedProposal()</td>
		<td>获取交易提案相关数据</td>
	</tr>
	<tr>
		<td>Map&lt;String, byte[]&gt; getTransient()</td>
		<td>获取交易的临时信息</td>
	</tr>
	<tr>
		<td>String getTxId()</td>
		<td>获取交易的交易 ID</td>
	</tr>
	<tr>
		<td>Instant getTxTimestamp()</td>
		<td>获取交易时间戳</td>
	</tr>
</table>

<span id="count"></span>
### 账本交互
<table>
	<tr>
		<th>接口</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>void putState(String key, byte[] value)</td>
		<td>在账本中添加或者更新一对键值</td>
	</tr>
	<tr>
		<td>byte[] getState(String key)</td>
		<td>获取指定键对应的值</td>
	</tr>
	<tr>
		<td>void delState(String key)</td>
		<td>在账本中删除对应的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getStateByRange(String startKey, String endKey)</td>
		<td>查询指定范围内的键值</td>
	</tr>
	<tr>
	<td>QueryResultsIteratorWithMetadata<KeyValue> getStateByRangeWithPagination(String startKey, String endKey, int pageSize, String bookmark)</td>
		<td>分页查询指定范围内的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyValue> getStateByPartialCompositeKey(String compositeKey)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyValue> getStateByPartialCompositeKey(String objectType, String... attributes)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyValue> getStateByPartialCompositeKey(CompositeKey compositeKey)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIteratorWithMetadata<KeyValue> getStateByPartialCompositeKeyWithPagination(CompositeKey compositeKey, int pageSize, String bookmark)</td>
		<td>分页查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyValue> getQueryResult(String query)</td>
		<td>查询状态数据库，需要支持富查询功能的状态数据库</td>
	</tr>
	<tr>
		<td>QueryResultsIteratorWithMetadata<KeyValue> getQueryResultWithPagination(String query, int pageSize, String bookmark)</td>
		<td>分页查询状态数据库，需要支持富查询功能的状态数据库</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyModification> getHistoryForKey(String key)</td>
		<td>返回对应键的所有历史值</td>
	</tr>
</table>

<span id="parameter"></span>
### 参数处理
<table>
	<tr>
		<th>接口</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>List&lt;byte[]&gt; getArgs()</td>
		<td>获取智能合约中调用参数</td>
	</tr>
	<tr>
		<td>List&lt;String&gt; getStringArgs()</td>
		<td>获取智能合约中调用参数</td>
	</tr>
	<tr>
		<td>String getFunction()</td>
		<td>获取智能合约调用的函数名，默认第一个参数为函数名</td>
	</tr>
	<tr>
		<td>List&lt;String&gt; getParameters()</td>
		<td>获取智能合约调用的参数</td>
	</tr>
</table>

<span id="auxiliary"></span>
### 其他辅助类
<table>
	<tr>
		<th>接口</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>CompositeKey createCompositeKey(String objectType, String... attributes)</td>
		<td>组合属性，形成复合键</td>
	</tr>
	<tr>
		<td>CompositeKey splitCompositeKey(String compositeKey)</td>
		<td>解析复合键的字符串</td>
	</tr>
	<tr>
		<td> Response invokeChaincode(final String chaincodeName, final List<byte[]> args, final String channel)</td>
		<td>调用其它智能合约 Invoke 方法</td>
	</tr>
	<tr>
		<td>void setEvent(String name, byte[] payload)</td>
		<td>设置发送的事件</td>
	</tr>
	<tr>
		<td>ChaincodeEvent getEvent()</td>
		<td>获取发送的事件</td>
	</tr>
	<tr>
		<td>void setStateValidationParameter(String key, byte[] value)</td>
		<td>设置 key 的背书策率</td>
	</tr>
	<tr>
		<td>byte[] getStateValidationParameter(String key)</td>
		<td>获取 key 的背书策率</td>
	</tr>
</table>
	

