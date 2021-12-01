云数据库 MongoDB 提供的监控功能可以实时查看实例资源的监控指标数据，通过可视化图形、表格、大屏、多种方式统计监控数据，并支持设置告警规格，通过消息推送的方式帮助您第一时间了解数据库服务的异常，及时调整业务，保障业务稳定运行。

## 监控粒度
云数据库 MongoDB 暂不支持监控数据采集粒度的自定义选择，自适应策略如下表所示。

| 时间跨度   | 监控粒度 | 保留时长 |
| ---------- | -------- | -------- |
| 0天-1天    | 5秒      | 1天      |
| 0天 - 1天  | 1分钟    | 15天     |
| 0天 - 1天  | 5分钟    | 31天     |
| 0天 - 7天  | 1小时    | 93天     |
| 7天 - 30天 | 1天      | 186天    |

## 支持监控的实例类型
云数据库 MongoDB 支持主实例、只读实例和灾备实例的监控，并为每个实例提供独立的监控视图供查询。

## 监控指标
腾讯云监控为云数据库 MongoDB 实例提供以下监控指标：

<table width="100">
<thead>
<tr><th width="15%">监控维度</th><th width="25%">监控指标</th><th width="5%">单位</th><th width="55%">指标说明</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="21">集群</td>
<td>写入请求</td><td>次</td><td>当前集群写入请求的数量统计</td></tr>
<tr>
<td>读取请求</td><td>次</td><td>当前集群读取请求的数量统计</td></tr>
<tr>
<td>更新请求</br></td><td>次</td><td>当前集群更新请求的数量统计</td></tr>
<tr>
<td>删除请求</td><td>次</td><td>当前集群删除请求的数量统计</td></tr>
<tr>
<td>count 请求次数</br></td><td>次</td><td>当前集群 Count 的请求数量统计</td></tr>
<tr>
<td>Aggregates 请求</td><td>次</td><td>当前集群聚合请求数量统计</td></tr>
<tr>
<td>集群连接数</td><td>次</td><td>集群总连接数，指当前集群 proxy 收到的连接数</td></tr>
<tr>
<td>集群连接数百分比</td><td>%</td><td>当前集群的连接数量与总连接数量的比例</td></tr>
<tr>
<td>最大容量使用率</td><td>%</td><td>集群当前实际占用存储空间与总容量的比例</td></tr>
<tr>
<td>QPS</td><td>次/秒</td><td>每秒操作数量统计，包含 CRUD 操作</td></tr>
<tr>
<td>成功请求</td><td>次</td><td>集群请求成功的数量统计</td></tr>
<tr>
<td>10毫秒 - 50毫秒</td><td>次</td><td>执行时间在10毫秒和50毫秒之间的请求数</td></tr>
<tr>
<td>50毫秒 - 100毫秒</td><td>次</td><td>执行时间在50毫秒和100毫秒之间的请求数</td></tr>
<tr>
<td>100毫秒</td><td>次</td><td>执行时间超过100毫秒的请求数</td></tr>
 <tr>
<td>超时</td><td>次</td><td>执行时间超时的请求数</td></tr>
<tr>
<td>oplog 时间差</td><td>小时</td><td>oplog 记录中最后一次操作和首次操作时间差</td></tr>
<tr>
<td>主从延迟</td><td>次</td><td>主从延迟时间</td></tr>
<tr>
<td>oplog 保存时间</td><td>小时</td><td>oplog 保存的时长</td></tr>
<tr>
<td>Cache 使用百分比</td><td>%</td><td>Cache 使用量占总量的百分比</td></tr>
<tr>
<td>Cache 脏数据百分比</td><td>%</td><td>Cache 脏数据占总量的百分比</td></tr>
<tr>
<td>Cache 命中率</td><td>%</td><td>当前集群 Cache 的命中率</td></tr>
<tr>
<td rowspan="11">节点</td>
<td>CPU 使用率</td><td>%</td><td>当前节点的 CPU 使用率</td></tr>
<tr>
<td>内存使用率</td><td>%</td><td>当前节点的内存使用率</td></tr>
<tr>
<td>Active Write</td><td>次</td><td>当前节点写数据的次数</td></tr>
<tr>
<td>Active Read</td><td>次</td><td>当前节点读数据的次数</td></tr>
<tr>
<td>TTL 删除数据条数</td><td>条</td><td>TTL 删除数据的数量</td></tr>
<tr>
<td>TTL 运转轮数</td><td>条</td><td>当前节点 TTL 运转的轮数</td></tr>
<tr>
<td>qr</td><td>个</td><td>等待读操作的客户端队列长度</td></tr>
<tr>
<td>qw</td><td>个</td><td>等待写操作的客户端队列长度</td></tr>
<tr>
<td>连接数</td><td>个</td><td>当前 mongod 节点的连接数</td></tr>
<tr>
<td>netin</td><td>MB/s</td><td>入站流量</td></tr>
<tr>
<td>netout</td><td>MB/s</td><td>出站流量</td></tr>
</tbody></table>

