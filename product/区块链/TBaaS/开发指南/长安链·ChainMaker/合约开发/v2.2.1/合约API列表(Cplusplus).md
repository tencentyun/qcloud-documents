ChainMaker C++ 语言版本智能合约有丰富的 API 接口，供用户在撰写智能合约的时候与链进行交互，代码实现详情可以参考[API 接口代码实现](https://docs.chainmaker.org.cn/v2.2.1/html/operation/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#c)。

从逻辑方面划分，可将 API 划分为以下类型：

[](id:accountInteraction)

### 账本交互

<table><thead>
<tr>
<th width="60%">接口</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>bool get_object(const std::string& key, std::string&#42 value){}</td>
<td>获取key为"key"的值。</td>
</tr>
<tr>
<td>bool put_object(const std::string& key, const std::string& value){}</td>
<td>存储key为"key"的值，注意key长度不允许超过64，且只允许大小写字母、数字、下划线、减号、小数点符号。</td>
</tr>
<tr>
<td>bool delete_object(const std::string& key) {}</td>
<td>删除key为"key"的值。</td>
</tr>
<tr>
<td>bool call(const std::string &contract, const std::string &method, EasyCodecItems &#42args, std::string &#42resp){}</td>
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
<td>bool arg(const std::string& name, std::string& value){}</td>
<td>该接口可返回属性名为 “name” 的参数的属性值。需要注意的是通过arg接口返回的参数，全部为字符串，合约开发者有必要将其他数据类型的参数与字符串做转换，包括atoi、itoa、自定义序列化方式等。</td>
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
<td>void success(const std::string& body) {}</td>
<td>返回成功的结果</td>
</tr>
<tr>
<td>void error(const std::string& body) {}</td>
<td>返回失败结果</td>
</tr>
<tr>
<td>void log(const std::string& body) {}</td>
<td>输出日志事件。查看方式为在链配置的log.yml中，开启vm:debug即可看到类似：wxvm log>> + msg</td>
</tr>
<tr>
<td>bool emit_event(const std::string &topic, int data_amount, const std::string data, ...)</td>
<td>发送合约事件</td>
</tr>
</tbody></table>
