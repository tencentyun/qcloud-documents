## 操作场景

增加 Mongos 的数量，可提升数据库实例访问的最大连接数。

## 版本说明

当前4.4、4.2、4.0版本的分片集群支持新增 Mongos 节点数。

## 使用须知

增加 Mongos 节点的数量，系统将自动为新增的 Mongos 节点绑定 IP 地址，开通访问 Mongos 的连接串，便可直接在**实例详情**页面的网络区域复制连接串。

## 前提条件

- 实例类型：分片实例。
- 实例状态：运行中。
- Mongos 的 CPU 性能与内存容量不足需提升。

## 操作步骤

1. 登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)。
2. 在左侧导航栏 **MongoDB** 的下拉列表中，选择**分片实例**。
3. 在右侧**实例列表**页面上方，选择地域。
4. 在实例列表中，找到需查看节点的目标实例。
5. 单击其实例 ID，进入**实例详情**页面，单击**节点管理**页签。
6. 在**节点管理**页面，单击 **Mongos 节点**页签。
7. 在 **Mongos 节点**页面，单击**新增 Mongos 节点**。
 - **实例在同一可用区**
![](https://qcloudimg.tencent-cloud.cn/raw/d8cb82286fd24f82a70b5b42b86b614f.png)
 - **实例在不同可用区**
![](https://qcloudimg.tencent-cloud.cn/raw/96cd3432f4d42ce2194a30ce7c535043.png)
<table>
<thead><tr><th>参数名称</th><th>参数解释</th></tr></thead>
<tbody><tr>
<td>实例 ID /名称</td>
<td>实例的唯一标识 ID 及实例的名称。</td></tr>
<tr>
<td>部署可用区</td>
<td>实例为同一个可用区，显示该参数，指实例所属的可以区。</td></tr>
<tr>
<td>Mongos 数量</td>
<td>实例为同一个可用区，显示该参数，指实例当前配置的 Mongos 的数量。</td></tr>
<tr>
<td>Mongos 规格</td>
<td>Mongos 的配置规格，包括：CPU 核数、内存及其最大连接数。</td></tr>
<tr>
<td>新增 Mongos 节点数</td>
<td>请选择需增加的 Mongos 数量，Mongos 节点最大总数为48。</td></tr>
<tr>
<td>总计费用</td>
<td>配置变更之后费用。<ul><li>按量计费：每小时新规格的费用。计费分为三个阶梯。</li><li>包年包月为：新规格剩余可使用时长的总费用。</li></ul></td></tr>
<tr>
<td>对比</td>
<td>可对比 Mongos 变更前后的配置规格、可用区的节点数量及其最连接数，请评估新规格是否满足要求。</td></tr>
</tbody></table>
8. 确认无误后，单击**确定**。


