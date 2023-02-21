## 支持的版本

| 节点 | 版本 | 
|---------|---------|
|kafka	|0.10+|

## 创建 kafka 节点
1. 在数据集成页面左侧目录栏单击**实时同步**。
2. 在实时同步页面上方选择**单表同步**新建（可选择表单和画布模式）并进入配置页面。
3. 单击左侧**读取**，单击选择 kafka 节点并配置节点信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6beb9ff521c0e55386140d93bce5ae19.png)
4. 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>节点名称</td>
<td>输入 kafka 节点名称</td>
</tr>
<tr>
<td>数据源</td>
<td>kafka 读取端数据源类型支持 kafka、Ckafka</td>
</tr>
<tr>
<td>topic</td>
<td>Kafka 数据源中的 Topic</td>
</tr>
<tr>
<td>序列化格式</td>
<td>Kafka 消息序列化格式类型，支持：canal-json、json、avro、csv</td>
</tr>
<tr>
<td>消息类型</td>
<td>append 消息：kafka 内消息来源于 append 消息流，通常消息中不携带唯一键。写入节点建议搭配 append 写入模式<br>upsert 消息：kafka 内消息来源于 upsert 消息流，通常消息中携带唯一键，设置后消息可保证 Exactly-Once。写入节点建议搭配 upsert 写入模式</td>
</tr>
<tr>
<td>读取位置</td>
<td>启动同步任务时开始同步数据的起始位点</td>
</tr>
<tr>
<td>消费组 id</td>
<td>请避免该参数与其他消费进程重复，以保证消费位点的正确性。如果不指定该参数，默认设定 group.id=WeData_ group_＄{任务id}</td>
</tr>
</tbody></table>
5. 预览字段，单击**保存**。

