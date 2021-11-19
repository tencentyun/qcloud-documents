Fabric Go 语言版本智能合约有丰富的 API 接口，代码实现详情可以参考 [API 接口代码实现](https://github.com/hyperledger/fabric/blob/v1.4.1/core/chaincode/shim/chaincode.go)。
从逻辑方面划分，可将 type 为 ChaincodeStub 的 API 划分为以下类型：
- [交易信息提取](#informationExtraction)
- [账本交互](#accountInteraction)
- [参数处理](#parametersProcess)
- [其他辅助类](#otherClass)




[](id:informationExtraction)
### 交易信息提取

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>GetBinding() ([]byte, error)</td>
<td>返回交易的 binding 信息</td>
</tr>
<tr>
<td>GetChannelID() string</td>
<td>获取当前的通道名称</td>
</tr>
<tr>
<td>GetCreator() ([]byte, error)</td>
<td>获取交易提交者信息</td>
</tr>
<tr>
<td>GetDecorations() map[string][]byte</td>
<td>获取交易的额外信息</td>
</tr>
<tr>
<td>GetSignedProposal() (*pb.SignedProposal, error)</td>
<td>获取交易提案相关数据</td>
</tr>
<tr>
<td>GetTransient() (map[string][]byte, error)</td>
<td>获取交易的临时信息</td>
</tr>
<tr>
<td>GetTxID() string</td>
<td>获取交易的交易 ID</td>
</tr>
<tr>
<td>GetTxTimestamp() (*timestamp.Timestamp, error)</td>
<td>获取交易时间戳</td>
</tr>
</tbody></table>

[](id:accountInteraction)
### 账本交互

<table><thead>
<tr>
<th width="60%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>PutState(key string, value []byte) error</td>
<td>在账本中添加或者更新一对键值</td>
</tr>
<tr>
<td>GetState(key string) ([]byte, error)</td>
<td>获取指定键对应的值</td>
</tr>
<tr>
<td>DelState(key string) error</td>
<td>在账本中，删除对应的键值</td>
</tr>
<tr>
<td>GetStateByRange(startKey, endKey string) (StateQueryIteratorInterface, error)</td>
<td>查询指定范围内的键值</td>
</tr>
<tr>
<td>GetStateByRangeWithPagination(startKey, endKey string, pageSize int32, bookmark string) (StateQueryIteratorInterface, *pb.QueryResponseMetadata, error)</td>
<td>分页查询指定范围内的键值</td>
</tr>
<tr>
<td>GetStateByPartialCompositeKey(objectType string, attributes []string) (StateQueryIteratorInterface, error)</td>
<td>查询匹配局部复合键的所有键值</td>
</tr>
<tr>
<td>GetStateByPartialCompositeKeyWithPagination(objectType string, keys []string, pageSize int32, bookmark string) (StateQueryIteratorInterface, *pb.QueryResponseMetadata, error)</td>
<td>分页查询匹配局部复合键的所有键值</td>
</tr>
<tr>
<td>GetQueryResult(query string)(StateQueryIteratorInterface, error)</td>
<td>查询状态数据库，需要支持富查询功能的状态数据库</td>
</tr>
<tr>
<td>GetQueryResultWithPagination(query string, pageSize int32, bookmark string) (StateQueryIteratorInterface, *pb.QueryResponseMetadata, error)</td>
<td>分页查询状态数据库，需要支持富查询功能的状态数据库</td>
</tr>
<tr>
<td>GetHistoryForKey(key string) (HistoryQueryIteratorInterface, error)</td>
<td>返回对应键的所有历史值</td>
</tr>
<tr>
<td>SetStateValidationParameter(key string, ep []byte) error</td>
<td>设置特定键的背书策略</td>
</tr>
<tr>
<td>GetStateValidationParameter(key string) ([]byte, error)</td>
<td>获取特定键的背书策略</td>
</tr>
<tr>
<td>GetPrivateData(collection, key string) ([]byte, error)</td>
<td>获取指定私有数据集中的键的值</td>
</tr>
<tr>
<td>GetPrivateDataHash(collection, key string) ([]byte, error)</td>
<td>获取指定私有数据集中的键的值的 hash</td>
</tr>
<tr>
<td>PutPrivateData(collection string, key string, value []byte) error</td>
<td>设置指定私有数据集中键的值</td>
</tr>
<tr>
<td>DelPrivateData(collection, key string) error</td>
<td>删除指定私有数据集中对应的键</td>
</tr>
<tr>
<td>SetPrivateDataValidationParameter(collection, key string, ep []byte) error</td>
<td>设置指定私有数据集中键的背书策略</td>
</tr>
<tr>
<td>GetPrivateDataValidationParameter(collection, key string) ([]byte, error)</td>
<td>获取指定私有数据集中键的背书策略</td>
</tr>
<tr>
<td>GetPrivateDataByRange(collection, startKey, endKey string) (StateQueryIteratorInterface, error)</td>
<td>获取指定私有数据集中特定范围键的键值</td>
</tr>
<tr>
<td>GetPrivateDataByPartialCompositeKey(collection, objectType string, keys []string) (StateQueryIteratorInterface, error)</td>
<td>获取指定私有数据集中匹配局部复合键的键值</td>
</tr>
<tr>
<td>GetPrivateDataQueryResult(collection, query string) (StateQueryIteratorInterface, error)</td>
<td>获取指定私有数据集中特定查询的键值，需要支持富查询功能的状态数据库</td>
</tr>
</tbody></table>



[](id:parametersProcess)
### 参数处理

<table>
<thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>GetArgs() [][]byte</td>
<td>以 byte 数组的形式获取智能合约中调用参数</td>
</tr>
<tr>
<td>GetArgsSlice() ([]byte, error)</td>
<td>以 byte 切片的形式获取智能合约中调用参数</td>
</tr>
<tr>
<td>GetStringArgs() []string</td>
<td>以字符串数组的形式获取智能合约中调用参数</td>
</tr>
<tr>
<td>GetFunctionAndParameters() (function string, params []string)</td>
<td>获取智能合约调用的函数名和参数， 默认第一个参数为函数名</td>
</tr>
</tbody></table>

[](id:otherClass)
### 其他辅助类

<table>
<thead>
<tr>
<th width="65%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>CreateCompositeKey(objectType string, attributes []string) (string, error)</td>
<td>组合属性，形成复合建</td>
</tr>
<tr>
<td>SplitCompositeKey(compositeKey string) (string, []string, error)</td>
<td>拆分复合键成一系列属性</td>
</tr>
<tr>
<td>InvokeChaincode(chaincodeName string, args [][]byte, channel string) pb.Response</td>
<td>调用其它智能合约 Invoke 方法</td>
</tr>
<tr>
<td>SetEvent(name string, payload []byte) error</td>
<td>设置发送的事件</td>
</tr>
</tbody></table>
