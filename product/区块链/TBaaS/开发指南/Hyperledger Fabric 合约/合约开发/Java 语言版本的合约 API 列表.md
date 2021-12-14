Fabric Java 语言版本智能合约有丰富的 API 接口，具体的代码实现可以参考 [API 接口代码实现](https://github.com/hyperledger/fabric-chaincode-java/blob/v1.4.1/fabric-chaincode-shim/src/main/java/org/hyperledger/fabric/shim/impl/ChaincodeStubImpl.java)。
从逻辑上划分，可将 API 接口分为以下类型：
- [交易信息提取](#information)
- [账本交互](#count)
- [参数处理](#parameter)
- [其他辅助类](#auxiliary)

[](id:information)
### 交易信息提取
<table>
	<tr>
		<th width="50%">接口</th>
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

[](id:count)
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
		<td>void putStringState(String key, String value)</td>
		<td>在账本中添加或者更新一对键值</td>
	</tr>
	<tr>
		<td>byte[] getState(String key)</td>
		<td>获取指定键对应的值</td>
	</tr>
	<tr>
		<td>String getStringState(String key)</td>
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
	<td>QueryResultsIteratorWithMetadata&lt;KeyValue&gt; getStateByRangeWithPagination(String startKey, String endKey, int pageSize, String bookmark)</td>
		<td>分页查询指定范围内的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getStateByPartialCompositeKey(String compositeKey)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getStateByPartialCompositeKey(String objectType, String... attributes)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getStateByPartialCompositeKey(CompositeKey compositeKey)</td>
		<td>查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIteratorWithMetadata&lt;KeyValue&gt; getStateByPartialCompositeKeyWithPagination(CompositeKey compositeKey, int pageSize, String bookmark)</td>
		<td>分页查询匹配局部复合键的所有键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getQueryResult(String query)</td>
		<td>查询状态数据库，需要支持富查询功能的状态数据库</td>
	</tr>
	<tr>
	<td>QueryResultsIteratorWithMetadata&lt;KeyValue&gt; getQueryResultWithPagination(String query, int pageSize, String bookmark)</td>
		<td>分页查询状态数据库，需要支持富查询功能的状态数据库</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyModification&gt; getHistoryForKey(String key)</td>
		<td>返回对应键的所有历史值</td>
	</tr>
		<tr>
		<td>void setStateValidationParameter(String key, byte[] value)</td>
		<td>设置特定键的背书策略</td>
	</tr>
	<tr>
		<td>byte[] getStateValidationParameter(String key)</td>
		<td>获取特定键的背书策略</td>
	</tr>
	<tr>
		<td>byte[] getPrivateData(String collection, String key)</td>
		<td>获取指定私有数据集集中的键的值</td>
	</tr>
	<tr>
		<td>String getPrivateDataUTF8(String collection, String key)</td>
		<td>获取指定私有数据集集中的键的值</td>
	</tr>
	<tr>
		<td>byte[] getPrivateDataHash(String collection, String key)</td>
		<td>获取指定私有数据集集中的键的值的 hash</td>
	</tr>
	<tr>
		<td>void putPrivateData(String collection, String key, byte[] value)</td>
		<td>设置指定私有数据集集中键的值</td>
	</tr>
	<tr>
		<td>void putPrivateData(String collection, String key, String value)</td>
		<td>设置指定私有数据集集中键的值</td>
	</tr>
	<tr>
		<td>void delPrivateData(String collection, String key)</td>
		<td>删除指定私有数据集集中对应的键</td>
	</tr>
	<tr>
		<td>void setPrivateDataValidationParameter(String collection, String key, byte[] value)</td>
		<td>设置指定私有数据集集中键的背书策略</td>
	</tr>
	<tr>
		<td>byte[] getPrivateDataValidationParameter(String collection, String key)</td>
		<td>获取指定私有数据集集中键的背书策略</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getPrivateDataByRange(String collection, String startKey, String endKey)</td>
		<td>获取指定私有数据集集中特定范围键的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getPrivateDataByPartialCompositeKey(String collection, String compositeKey)</td>
		<td>获取指定私有数据集集中匹配局部复合键的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator<KeyValue> getPrivateDataByPartialCompositeKey(String collection, CompositeKey compositeKey)</td>
		<td>获取指定私有数据集集中匹配局部复合键的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getPrivateDataByPartialCompositeKey(String collection, String objectType, String... attributes)</td>
		<td>获取指定私有数据集集中匹配局部复合键的键值</td>
	</tr>
	<tr>
		<td>QueryResultsIterator&lt;KeyValue&gt; getPrivateDataQueryResult(String collection, String query)</td>
		<td>获取指定私有数据集集中特定查询的键值，需要支持富查询功能的状态数据库</td>
	</tr>
</table>

[](id:parameter)
### 参数处理
<table>
	<tr>
		<th width="50%">接口</th>
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

[](id:auxiliary)
### 其他辅助类
<table>
	<tr>
		<th width="65%">接口</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>CompositeKey createCompositeKey(String objectType, String... attributes)</td>
		<td>组合属性，形成复合键</td>
	</tr>
		<tr>
		<td>CompositeKey splitCompositeKey(String compositeKey)</td>
		<td>拆分复合键成一系列属性</td>
	</tr>
	<tr>
		<td> Response invokeChaincode(final String chaincodeName, final List&lt;byte[]&gt; args, final String channel)</td>
		<td>调用其它智能合约 invoke 方法</td>
	</tr>
	<tr>
		<td> Response invokeChaincode(String chaincodeName, List&lt;byte[]&gt; args)</td>
		<td>调用其它智能合约 invoke 方法</td>
	</tr>
	<tr>
		<td>Response invokeChaincodeWithStringArgs(String chaincodeName, List&lt;String&gt; args, String channel)</td>
		<td>调用其它智能合约 invoke 方法</td>
	</tr>
	<tr>
		<td>Response invokeChaincodeWithStringArgs(String chaincodeName, List&lt;String&gt; args)</td>
		<td>调用其它智能合约 invoke 方法</td>
	</tr>
		<tr>
		<td>Response invokeChaincodeWithStringArgs(final String chaincodeName, final String... args)</td>
		<td>调用其它智能合约 invoke 方法</td>
	</tr>
	<tr>
		<td>void setEvent(String name, byte[] payload)</td>
		<td>设置发送的事件</td>
	</tr>
	<tr>
		<td>ChaincodeEvent getEvent()</td>
		<td>获取发送的事件</td>
	</tr>
</table>
	
	
	
