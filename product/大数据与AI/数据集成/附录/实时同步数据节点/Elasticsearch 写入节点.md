## 支持的版本

| 节点 | 版本|
|---------|---------|
| Elasticsearch	| Elasticsearch：6.x，7.x| 

## 配置 Elasticsearch 节点
1. 在数据集成页面左侧目录栏单击**实时同步**。
2. 在实时同步页面上方选择**单表同步**新建（可选择表单和画布模式）并进入配置页面。
3. 单击左侧**写入**，单击选择 Elasticsearch 节点并配置节点信息。
![](https://qcloudimg.tencent-cloud.cn/raw/ebd39cdc3530039ccfcb1a9312180b53.png)
4. 参数信息：
<table>
<thead>
<tr>
<th>参数</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>节点名称</td>
<td>输入 Elasticsearch 节点名称</td>
</tr>
<tr>
<td>数据源</td>
<td>选择需要写入的 Elasticsearch 数据源</td>
</tr>
<tr>
<td>索引</td>
<td>ElasticSearch 中的索引名称</td>
</tr>
<tr>
<td>写入模式</td>
<td>更新每行记录所有字段（目前支持按行更新）</td>
</tr>
<tr>
<td>主键取值方式</td>
<td>源表主键：document 的 id 使用源表的主键<br>联合主键：document 的 id 使用源表的多个列共同确定<br>无主键：默认生成_id 值</td>
</tr>
<tr>
<td>开启路由</td>
<td>Elasticsearch 是否开启路由分区索引数据。开启路由功能后，可控制在 ElasticSeaerch 中使用哪个分区来存储文档</td>
</tr>
</tbody></table>
5. 预览数据字段并与读取节点配置字段映射，单击**保存**。
