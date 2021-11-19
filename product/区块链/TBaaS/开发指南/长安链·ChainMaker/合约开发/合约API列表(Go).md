ChainMake Go 语言版本智能合约有丰富的 API 接口，供用户在撰写智能合约的时候与链进行交互，代码实现详情可参见 [API 接口代码实现](https://docs.chainmaker.org.cn/dev/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#go-tinygo)。

从逻辑方面划分，可将 API 划分为以下类型：

[](id:informationExtraction)

### 交易信息提取

<table><thead>
<tr>
<th width="50%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>GetCreatorOrgId() string  </td>
<td>获取合约创建者所属组织ID</td>
</tr>
<tr>
<td>GetCreatorRole() string </td>
<td>获取合约创建者角色</td>
</tr>
<tr>
<td>GetCreatorPk() string </td>
<td>获取合约创建者公钥</td>
</tr>
<tr>
<td>GetSenderOrgId() string  </td>
<td>获取交易发起者所属组织ID</td>
</tr>
<tr>
<td>GetSenderRole() string </td>
<td>获取交易发起者角色</td>
</tr>
<tr>
<td>GetTxId() string </td>
<td>获取交易ID</td>
</tr>
<tr>
<td>GetSenderPk() string </td>
<td>获取交易发起者公钥</td>
</tr>
<tr>
<td>GetBlockHeight() string </td>
<td>获取当前区块高度</td>
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
<td>GetState(key string, field string) (string, ResultCode)</td>
<td>获取合约账户信息。该接口可从链上获取类别 “key” 下属性名为 “field” 的状态信息。</td>
</tr>
<tr>
<td>GetStateFromKey(key string) ([]byte, ResultCode)</td>
<td>获取合约账户信息。该接口可以从链上获取类别为key的状态信息</td>
</tr>
<tr>
<td>PutState(key string, field string, value string) ResultCode</td>
<td>写入合约账户信息。该接口可把类别 “key” 下属性名为 “filed” 的状态更新到链上。更新成功返回0，失败则返回1。</td>
</tr>
<tr>
<td>PutStateFromKey(key string, value string) ResultCode</td>
<td>写入合约账户信息。</td>
</tr>
<tr>
<td>DeleteState(key string, field string) ResultCode</td>
<td>删除合约账户信息。该接口可把类别 “key” 下属性名为 “name” 的状态从链上删除。</td>
</tr>
<tr>
<td>CallContract(contractName string, method string, param map[string]string) ([]byte, ResultCode)</td>
<td>跨合约调用。</td>
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
<td>Args() map[string]interface{}</td>
<td>该接口调用 getArgsMap() 接口，把 json 格式的数据反序列化，并将解析出的数据返还给用户。</td>
</tr>
<tr>
<td>Arg(key string) interface{}</td>
<td>该接口可返回属性名为 “key” 的参数的属性值。</td>
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
<td>SuccessResult(msg string)</td>
<td>该接口可记录用户操作成功的信息，并将操作结果记录到链上。</td>
</tr>
<tr>
<td>ErrorResult(msg string)</td>
<td>该接口可记录用户操作失败的信息，并将操作结果记录到链上。</td>
</tr>
<tr>
<td>LogMessage(msg string)</td>
<td>该接口可记录事件日志。查看方式为在链配置的log.yml中，开启vm:debug即可看到类似：gasm log>> + msg</td>
</tr>
<tr>
<td>EmitEvent(topic string, data ...string)</td>
<td>发送合约事件</td>
</tr>
<tr>
<td>NewIterator(startKey string, limitKey string) (ResultSetKV, ResultCode)</td>
<td>新建key范围迭代器，key前闭后开，即：startKey <= dbkey < limitKey</td>
</tr>
<tr>
<td>NewIteratorWithField(key string, startField string, limitField string) (ResultSetKV, ResultCode)</td>
<td>新建field范围迭代器，key需相同，field前闭后开，即：key = dbdbkey and startField <= dbfield < limitField</td>
</tr>
<tr>
<td>NewIteratorPrefixWithKey(key string) (ResultSetKV, ResultCode)</td>
<td>新建指定key前缀匹配迭代器，key需前缀一致，即dbkey.startWith(key)</td>
</tr>
<tr>
<td>NewIteratorPrefixWithKeyField(key string, field string) (ResultSetKV, ResultCode)</td>
<td>新建指定field前缀匹配迭代器，key需相同，field前缀一致，即dbkey = key and dbfield.startWith(field)</td>
</tr>
</tbody></table>

