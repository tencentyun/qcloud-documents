
## InnoDB引擎
>!数据库审计功能重构升级中，敬请期待；在此期间数据库新购实例不再开放审计功能。

<table>
<thead><tr><th width="22%">实例架构</th><th>定义</th><th>节点</th><th>特点</th></tr></thead>
<tbody><tr>
<td>标准版（一主一从）</td>
<td>每个分片提供主从双活部署的高可用架构</td>
<td>两个节点：一个 Master 节点，一个 Slave 节点</td>
<td rowspan = "2"><li>支持从机只读</li><dx-alert infotype="explain" title="说明">一主一从架构从机只读仅可用于轻量只读任务，请避免大事务等较高负载任务，影响从机备份任务及可用性。</dx-alert><li>故障后节点自动恢复</li><li>默认监控采样粒度：5分钟/次</li><li>最大可配备份时长：7天</li><li>操作日志备份：7天</li><li>支持数据库审计，审计日志存储15天，规则配置个数暂无限制</li></td></tr>
<tr>
<td>标准版（一主二从）</td>
<td>每个分片提供主从多活部署的高可用架构</td>
<td>三个节点：一个 Master 节点，两个 Slave 节点</td></tr>
<tr>
<td>金融定制版（一主一从）</td>
<td>每个分片提供主从双活部署的高可用架构</td>
<td>两个节点：一个 Master 节点，一个 Slave 节点</td>
<td  rowspan = "2"><li>支持其他部署方案，需联系对应商务</li><li>支持从机只读，从机只读时智能负载</li><li>故障后节点自动恢复</li><li>默认监控采样粒度：1分钟/次</li><li>最大可配备份时长：3650天，需 <a href="https://console.cloud.tencent.com/workorder/category">提交工单</a></li><li>操作日志备份：默认60天，归档存储1年</li><li>支持数据库审计：审计日志存储15天</li><li>监管配合：有</li></td></tr>
<tr>
<td>金融定制版（一主二从）</td>
<td>每个分片提供主从多活部署的高可用架构</td>
<td>三个节点：一个 Master 节点，两个 Slave 节点</td></tr>
</tbody></table>

## TDStore 引擎
内测阶段，TDStore 存储节点采用一主二从的高可用架构（三个节点：一个 Master 节点，两个 Slave 节点）。

