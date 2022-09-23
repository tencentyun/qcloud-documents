## 操作场景

提升 Mongos 的计算规格可提升数据库访问的最大连接数，可根据业务访问实际情况适当调整 Mongos 的规格。

## 使用须知

扩容 Mongos 节点的 CPU 性能及其内存容量，可能会涉及到跨机迁移数据，会引起连接闪断的现象，请在操作前确认业务有自动连接机制，建议在业务低峰期维护时间窗完成操作。

## 版本说明

MongoDB 4.4、4.2、4.0版本支持调整 Mongos 的规格。

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
7. 在 Mongos 节点页面，单击 **Mongos 配置变更**，在弹出的对话框，配置新的 Mongos 规格。
<img src="https://qcloudimg.tencent-cloud.cn/raw/cca2cb793fa943f486fb7832abfc98db.png"  style="zoom:60%;">
<table>
<thead><tr><th>参数名称</th><th>参数解释</th></tr></thead>
<tbody><tr>
<td>实例 ID /名称</td>
<td>实例的唯一标识 ID 及实例的名称。</td></tr>
<tr>
<td>部署可用区</td>
<td>实例所属的可用区。</td></tr>
<tr>
<td>Mongos 数量</td>
<td>当前 Mongos 的数量。</td></tr>
<tr>
<td>Mongos 规格</td>
<td>在下拉列表中重新选择 Mongos 的规格，支持选择1核2GB、2核4GB、4核8GB、8核16GB、16核32GB。</td></tr>
<tr>
<td>切换时间</td>
<td><ul><li>选择<b>调整完成时</b>，立即执行调整实例规格任务。调整实例内存与容量可能涉及节点迁移或者主从切换，主从切换时间点将不可控，可能导致断连或重启。</li><li>选择<b>维护时间内</b>，在维护时间段内执行切换实例规格任务。关于维护时间的更多信息，请参见 <a href="https://cloud.tencent.com/document/product/240/19910">设置实例维护时间</a>。</li></ul></td></tr>
<tr>
<td>配置变更费用</td>
<td>配置变更之后费用。按量计费：每小时新规格的费用。计费分为三个阶梯。包年包月为：新规格剩余可使用时长的总费用。</td></tr>
<tr>
<td>对比</td>
<td>可对比 Mongos 变更前后的配置规格。展示其新规格的最大连接数，请评估新规格是否满足要求。</td></tr>
</tbody></table>
8. 确认变更此规格，单击**确定**。

   
