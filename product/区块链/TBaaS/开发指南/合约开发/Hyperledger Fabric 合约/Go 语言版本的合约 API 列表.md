Fabric Go 语言版本智能合约有丰富的 API 接口，代码实现详情可以参考 [API 接口代码实现](https://github.com/hyperledger/fabric/blob/release-1.1/core/chaincode/shim/chaincode.go)。
从逻辑方面划分，可将 API 划分为以下类型：
- [交易信息提取](#informationExtraction)
- [账本交互](#accountInteraction)
- [参数处理](#parametersProcess)
- [其他辅助类](#otherClass)

<span id="informationExtraction"></span>
### 交易信息提取

| 接口 | 说明 |
|---------|---------|
| GetBinding() ([]byte, error) | 返回交易的 binding 信息 |
| GetChannelID() string | 获取当前的通道名称 |
| GetCreator() ([]byte, error) | 获取交易提交者信息 |
| GetDecorations() map[string][]byte | 获取交易的额外信息 |
| GetSignedProposal() (*pb.SignedProposal, error) | 获取交易提案相关数据 |
| GetTransient() (map[string][]byte, error) | 获取交易的临时信息 |
| GetTxID() string | 获取交易的交易 ID |
| GetTxTimestamp() (*timestamp.Timestamp, error) | 获取交易时间戳 |

<span id="accountInteraction"></span>
### 账本交互

| 接口 | 说明 |
|---------|---------|
| PutState(key string, value []byte) error | 在账本中添加或者更新一对键值 |
| GetState(key string) ([]byte, error) | 获取指定键对应的值 |
| DelState(key string) error | 在账本中，删除对应的键值 |
| GetStateByRange(startKey, endKey string) (StateQueryIteratorInterface, error) | 查询指定范围内的键值 |
| GetStateByPartialCompositeKey(objectType string, attributes []string) (StateQueryIteratorInterface, error) | 查询匹配局部复合键的所有键值 |
| GetQueryResult(query string)(StateQueryIteratorInterface, error) | 查询状态数据库，只对支持富查询功能的状态数据库 |
| GetHistoryForKey(key string) (HistoryQueryIteratorInterface, error) | 返回对应键的所有历史值 |

<span id="parametersProcess"></span>
### 参数处理

| 接口 | 说明 |
|---------|---------|
| GetArgs() [][]byte | 获取智能合约中调用参数 |
| GetArgsSlice() ([]byte, error) | 获取智能合约中调用参数 |
| GetStringArgs() []string | 获取智能合约中调用参数 |
| GetFunctionAndParameters() (function string, params []string) | 获取智能合约调用的函数名和参数， 默认第一个参数为函数名 |

<span id="otherClass"></span>
### 其他辅助类

| 接口 | 说明 |
|---------|---------|
| CreateCompositeKey(objectType string, attributes []string) (string, error) | 组合属性，形成复合建 |
| SplitCompositeKey(compositeKey string) (string, []string, error) | 拆分复合键成一系列属性 |
| InvokeChaincode(chaincodeName string, args [][]byte, channel string) pb.Response | 调用其它智能合约 Invoke 方法 |
| SetEvent(name string, payload []byte) error | 设置发送的事件 |
