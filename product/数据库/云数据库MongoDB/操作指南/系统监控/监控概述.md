云数据库 MongoDB 提供的监控功能可以实时查看实例资源的监控指标数据，通过可视化图形、表格、大屏、多种方式统计监控数据，并支持设置告警规格，通过消息推送的方式帮助您第一时间了解数据库服务的异常，及时调整业务，保障业务稳定运行。

## 监控粒度
云数据库 MongoDB 暂不支持监控数据采集粒度的自定义选择，自适应策略如下表所示。

| 时间跨度   | 监控粒度 | 保留时长 |
| ---------- | -------- | -------- |
| 0天 - 1天  | 5秒      | 1天      |
| 0天 - 1天  | 1分钟    | 15天     |
| 0天 - 1天  | 5分钟    | 31天     |
| 0天 - 1天  | 1小时    | 93天     |
| 0天 - 1天  | 1天      | 186天    |
| 0天 - 7天  | 1小时    | 93天     |
| 0天 - 7天  | 1天      | 186天    |
| 7天 - 30天 | 1小时    | 93天     |
| 7天 - 30天 | 1天      | 186天    |



## 支持监控的实例类型

- 实例：主实例、只读实例和灾备实例的监控，并为每个实例提供独立的监控视图。
- 节点：Mongod 节点与 Mongos 节点，为每一个节点提供独立的监控视图。

## 监控指标
### 实例

<table width="100">
<thead>
<tr><th width="15%">监控维度</th><th width="25%">监控指标中文名称</th><th width="10%">监控指标英文名称</th><th width="5%">单位</th><th width="45%">指标说明</th></tr>
</thead>
<tbody>
<tr>
<td rowspan="4">CPU 监控</td>
<td>Mongod 最大 CPU 使用率</td><td>mongod_max_mem_usage</td><td>%</td><td>集群所有 Mongod 节点最大的 CPU 使用率。</td></tr>
<tr>
<td>Mongod 平均 CPU 使用率</td><td>monogd_avg_cpu_usage</td><td>%</td><td>集群所有 Mongod 节点 CPU 使用率取平均值。</td></tr>
<tr>
<td>Mongos 最大 CPU 使用率</td><td>monogs_max_cpu_usage</td><td>%</td><td>分片集群所有 Mongos 节点最大的 CPU 使用率。</td></tr>
<tr>
<td>Mongos 平均 CPU 使用率</td><td>monogs_avg_cpu_usage</td><td>%</td><td>分片集群所有 Mongos 节点 CPU 使用率取平均值。</td></tr>   
<tr>
<td rowspan="4">内存监控</td>
<td>Mongod 最大内存使用率</td><td>mongod_max_mem_usage</td><td>%</td><td>集群所有 Mongod 节点最大的内存使用率。</td></tr>
<tr>
<td>Mongod 平均内存使用率</td><td>mongod_avg_mem_usage</td><td>%</td><td>集群所有 Mongod 节点内存使用率取平均值。</td></tr>
<tr>
<td>Mongos 最大内存使用率</td><td>mongos_max_mem_usage</td><td>%</td><td>分片集群所有 Mongos 节点最大的内存使用率。</td></tr>    
<tr>
<td>Mongos 平均内存使用率</td><td>mongos_avg_mem_usage</td><td>%</td><td>分片集群所有 Mongos 节点内存使用率取平均值。</td></tr>
<tr>
<td>磁盘监控</td>
<td>磁盘空间利用率</td><td>disk_usage</td><td>%</td><td>实际磁盘使用量与申请的磁盘空间的占比。</td></tr>    
<tr>
<td rowspan="4">网络监控</td>
<td>连接数量</td><td>cluster_conn</td><td>个</td><td>连接到实例的 TCP 连接数量。</td></tr>
<tr>
<td>连接百分比</td><td>connper</td><td>%</td><td>当前集群的连接数量与最大连接数的比例。</td></tr>
<tr>
<td>入流量</td><td>cluster_view</td><td>Bytes</td><td>集群的入流量字节数统计。</td></tr>     
<tr>
<td>出流量</td><td>cluster_netout</td><td>Bytes</td><td>集群的出流量字节数统计。</td></tr>
<tr>
<td rowspan="12">时延监控</td>
<td>所有请求平均时延<td>avg_all_request_delay</br></td><td>ms</td><td>集群所有请求执行的平均时延。</td></tr>
<tr>
<td>更新平均延迟</td><td>avg_update_delay</td><td>ms</td><td>集群更新请求的平均时延。</td></tr>
<tr>
<td>插入平均延迟</td><td>avg_insert_delay</td><td>ms</td><td>集群插入请求的平均时延。</td></tr>
<tr>
<td>读平均时延</td><td>avg_read_delay</td><td>ms</td><td>集群读请求的平均时延。</td></tr>
<tr>
<td>聚合请求平均时延</td><td>avg_aggregate_delay</td><td>ms</td><td>集群聚合请求的平均时延。</td></tr>
<tr>
<td>Count 的平均延迟</td><td>avg_count_delay</td><td>ms</td><td>集群 Count 请求的平均时延。</td></tr>
<tr>
<td>Getmore 平均延迟</td><td>avg_getmore_delay</td><td>ms</td><td>集群 Getmore 请求的平均时延。</td></tr>
<tr>
<td>删除平均延迟</td><td>avg_delete_delay</td><td>ms</td><td>集群删除请求的平均时延。</td></tr>
<tr>
<td>Command 平均时延</td><td>avg_command_delay</td><td>ms</td><td>集群 Command 请求的平均时延。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
<tr>
<td>10毫秒 - 50毫秒</td><td>10ms</td><td>次</td><td>执行时间在10毫秒和50毫秒之间的请求次数。</td></tr>
<tr>
<td>50毫秒 - 100毫秒</td><td>50ms</td><td>次</td><td>执行时间在50毫秒和100毫秒之间的请求次数。</td></tr>
<tr>
<td>100毫秒</td><td>100ms</td><td>次</td><td>执行时间超过100毫秒的请求次数。</td></tr>
<tr><td rowspan="9">请求监控</td>
<td>总请求量</td><td>success_per_second</td><td>次/秒</td><td>集群每秒所有请求执行成功的次数。</td></tr>
<tr>
<td>插入请求</td><td>insert_per_second</td><td>次/秒</td><td>集群每秒插入请求执行次数。</td></tr>
<tr>
<td>读请求</td><td>read_per_second</td><td>次/秒</td><td>集群每秒读请求执行次数。</td></tr>
<tr>
<td>更新请求</td><td>update_per_second</td><td>次/秒</td><td>集群每秒更新请求执行次数。</td></tr>
<tr>
<td>删除请求</td><td>delete_per_second</td><td>次/秒</td><td>集群每秒删除请求执行次数。</td></tr>
<tr>
<td>count 请求</td><td>count_per_second</td><td>次/秒</td><td>集群每秒收到的 Count 请求的次数。</td></tr>
<tr>
<td>Getmore 请求</td><td>getmore_per_second</td><td>次/秒</td><td>集群每秒收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求</td><td>aggregate_per_second</td><td>次/秒</td><td>集群每秒聚合请求的次数。</td></tr>
<tr>
<td>Command 请求</td><td>command_per_second</td>
<td>次/秒</td><td>集群每秒收到的 Command 请求的次数。Command 为除 insert、update、delete、query以外命令的总称。</td></tr>
<tr>
<td rowspan="9">请求量</td>
<td>总请求量</td><td>node_success</td><td>次</td><td>集群所有请求的次数。</td></tr>
<tr>
<td>插入请求</td><td>node_inserts</td><td>次</td><td>集群收到的插入请求的次数。</td></tr>
<tr>
<td>读请求</td><td>node_reads</td><td>次</td><td>集群收到的读请求的次数。</td></tr>
<tr>
<td>更新请求</td><td>node_updates</td><td>次</td><td>集群更新请求的次数。</td></tr>
<tr>
<td>删除请求</td><td>node_deletes</td><td>次</td><td>集群删除请求的次数。</td></tr>
<tr>
<td>count 请求</td><td>node_counts</td><td>次</td><td>集群收到的 Count 请求的次数。</td></tr>
<tr>
<td>Getmore 请求</td><td>node_getmores</td><td>次</td><td>集群收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求</td><td>node_aggregates</td><td>次</td><td>集群聚合所有请求的次数。</td></tr>
<tr>
<td>Command 请求</td><td>node_commands</td><td>次</td><td>集群收到的 Command 请求的次数。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
</tbody></table>

### Mongod 节点

<table width="100">
<thead>
<tr><th width="15%">监控维度</th><th width="25%">监控指标中文名称</th><th width="10%">监控指标英文名称</th><th width="5%">单位</th><th width="45%">指标说明</th></tr>
</thead>
<tbody>
<tr>
<td>CPU 监控</td>
<td>CPU 使用率</td><td>cpuusage</td><td>%</td><td>Mongod 节点 CPU 使用率。</td></tr> 
<tr>
<td>内存监控</td>
<td>内存使用率</td><td>memusage</td><td>%</td><td>Mongod 节点的内存使用率。</td></tr>
<tr>
<td rowspan="3">磁盘监控</td>
<td>磁盘空间使用量</td><td>diskusage</td><td>MBytes</td><td>Mongod 节点磁盘容量的使用率。</td></tr>
<tr>
<td>磁盘读次数</td><td>ioread</td><td>次/秒</td><td>Mongod 节点磁盘每秒读的次数。</td></tr>
<tr>
<td>磁盘写次数</td><td>iowrite</td><td>次/秒</td><td>Mongod 节点磁盘每秒读的次数。</td></tr>     
<tr>
<td rowspan="2">网络监控</td>
<td>入流量</td><td>netout</td><td>Bytes</td><td>Mongod 节点入流量字节数统计。</td>   
<tr>
<td>出流量</td><td>netin</td><td>Bytes</td><td>Mongod 节点的出流量字节数统计。</td></tr>
<tr>
<td rowspan="12">请求平均延迟监控</td>
<td>所有请求平均时延</td><td>node_avg_all_requests_delay</td><td>ms</td><td>Mongod 节点收到的所有请求平均时延。</td></tr>
<tr>
<td>更新平均延迟</td><td>node_avg_update_delay</td><td>ms</td><td>Mongod 节点 update 请求时延平均值。</td></tr>
<tr>
<td>插入平均延迟</td><td>node_avg_insert_delay</td><td>ms</td><td>Mongod 节点 insert 请求时延平均值。</td></tr>
<tr>
<td>读平均时延</td><td>node_avg_read_delay</td><td>ms</td><td>Mongod 节点读请求时延平均值。</td></tr>
<tr>
<td>聚合请求平均时延</td><td>node_avg_aggregate_delay</td><td>ms</td><td>Mongod 节点聚合请求时延平均值。</td></tr>
<tr>
<td>Count 的平均延迟</td><td>node_avg_count_delay</td><td>ms</td><td>Mongod 节点 Count 请求时延平均值。</td></tr>
<tr>
<td>Getmore 平均延迟</td><td>node_avg_getmore_delay</td><td>ms</td><td>Mongod 节点 Getmore 请求时延平均值。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
<tr>
<td>删除平均延迟</td><td>node_avg_delete_delay</td><td>ms</td><td>Mongod 节点删除请求时延平均值。</td></tr>
<tr>
<td>Command 平均时延</td><td>node_avg_command_delay</td><td>ms</td><td>Mongod 节点 Command 请求时延平均值。</td></tr>
<tr>
<td>10-50毫秒</td><td>10ms</td><td>次</td><td>执行时间在10毫秒和50毫秒之间的请求次数。</td></tr>
<tr>
<td>50-100毫秒</td><td>50ms</td><td>次</td><td>执行时间在50毫秒和100毫秒之间的请求次数。</td></tr>
<tr>
<td>100毫秒</td><td>100ms</td><td>次</td><td>执行时间超过100毫秒的请求次数。</td></tr>
<tr>
<td rowspan="9">请求监控</td>
<td>总请求</td><td>node_success_per_second</td><td>次/秒</td><td>Mongod 节点每秒所有请求的次数。</td></tr>
<tr>
<td>插入请求</td><td>node_insert_per_second<td>次/秒</td><td>Mongod 节点每秒插入请求的次数。</td></tr>
<tr>
<td>读请求</td><td>node_read_per_second</td><td>次/秒</td><td>Mongod 节点每秒读请求的次数。</td></tr>
<tr>
<td>更新请求</td><td>node_update_per_second</td><td>次/秒</td><td>Mongod 节点每秒更新请求的次数。</td></tr>
<tr>
<td>删除请求</td><td>node_delete_per_second</td><td>次/秒</td><td>Mongod 节点每秒删除请求的次数。</td></tr>
<tr>
<td>Count 请求</td><td>node_count_per_second</td><td>次/秒</td><td>Mongod 节点每秒收到的 Count 请求的次数。</td></tr>
<tr>
<td>Getmore 请求</td><td>node_getmore_per_second</td><td>次/秒</td><td>Mongod 节点每秒收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求</td><td>node_aggregate_per_second</td><td>次/秒</td><td>Mongod 节点每秒聚合请求的次数。</td></tr>
<tr>
<td>Command 请求</td><td>node_command_per_second</td><td>次/秒</td><td>Mongod 节点每秒收到的 Command 请求的次数。Command 为除 insert、update、delete、query 以外命令的总称</td></tr>
<tr>
<td rowspan="12">内核监控</td>
<td>活跃写请求</td><td>ar</td><td>个</td><td>Mongod 节点活跃写请求的个数。</td></tr>
<tr>
<td>活跃读请求</td><td>aw</td><td>个</td><td>Mongod 节点活跃读请求的个数。</td></tr>
<tr>
<td>排队读请求</td><td>qr</td><td>个</td><td>Mongod 节点等待读操作的客户端队列长度。</td></tr>
<tr>
<td>排队写请求</td><td>qw</td><td>个</td><td>Mongod 节点等待写操作的客户端队列长度。</td></tr>
<tr>
<td>TTL 删除数据条数</td><td>ttl_deleted</td><td>次</td><td>Mongod 节点 TTL  删除文档的数量。</td></tr>
<tr>
<td>TTL 发起次数</td><td>ttl_pass</td><td>次</td><td>后台进程从 TTL 聚合中删除文档的次数。</td></tr>
<tr>
<td>活跃 session 数量</td><td>active_session</td><td>个</td><td>节点活跃 session 数量。</td></tr>
<tr>
<td>Oplog 保存时长</td><td>node_oplog_reserved_time</td><td>小时</td><td>oplog 保存的时长。</td></tr>
<td>主从延迟</td><td>node_slavedelay</td><td>秒</td><td>主从节点的延迟时长。</td></tr>   
<tr>
<td>Cache 命中率</td><td>replicaset_node</td><td>%</td><td>当前集群 Cache 的命中率。</td></tr><tr>
<td>Cache 使用百分比</td><td>node_cache_used</td><td>%</td><td>Cache 使用量占总量的百分比。</td></tr>
<tr>
<td>Cache脏 数据百分比</td><td>node_cache_dirty</td><td>%</td><td>Cache 脏数据占总量的百分比。</td></tr>
<tr>
<td rowspan="9">请求量</td>
<td>总请求量</td><td>node_success</td><td>次</td><td>集群总请求次数。</td></tr>
<tr>
<td>插入请求量</td><td>node_inserts</td><td>次</td><td>集群插入请求的次数。</td></tr>
<tr>
<td>读请求量</td><td>node_reads</td><td>次</td><td>集群读请求的次数。</td></tr>
<tr>
<td>更新请求量</td><td>replicaset_node</td><td>次</td><td>集群更新请求的次数。</td></tr>
<tr>
<td>删除请求量</td><td>node_deletes</td><td>次</td><td>集群删除请求的次数。</td></tr>
<tr>
<td>Count 请求量</td><td>node_counts</td><td>次</td><td>集群收到的 Count 请求的次数。</td></tr>
<tr><td>Getmore 请求量</td><td>node_getmores</td><td>次</td><td>集群收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求量</td><td>node_aggregates</td><td>次</td><td>集群聚合请求的次数。</td></tr>
<tr>
<td>Command 请求量</td><td>node_commands</td><td>次</td><td>集群收到的 Command 请求的次数。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
</tbody></table>

### Mongos 节点（分片集群）

<table width="100">
<thead>
<tr><th width="15%">监控维度</th><th width="25%">监控指标中文名称</th><th width="10%">监控指标中文名称</th><th width="5%">单位</th><th width="45%">指标说明</th></tr>
</thead>
<tbody>
<tr>
<td>CPU 监控</td>
<td>CPU 使用率</td><td>cpuusage</td><td>%</td><td>Mongos节点的 CPU 使用率。</td></tr> 
<tr>
<td>内存监控</td>
<td>内存使用率</td><td>memusage</td><td>%</td><td>Mongos 节点的内存使用率。</td></tr>   
<tr>
<td rowspan="2">网络监控</td>
<td>内网入流量</td><td>netin</td><td>Bytes</td><td>Mongos 节点入流量字节数统计。</td>   
<tr>
<td>内网出流量</td><td>netout</td><td>Bytes</td><td>Mongos 节点的出流量字节数统计。</td></tr>
<tr>
<td rowspan="12">时延监控</td>
<td>所有请求平均时延</td><td>node_avg_all_request_delay</td><td>ms</td><td>Mongos 节点收到的所有请求平均时延。</td></tr>
<tr>
<td>更新平均延迟</td><td>node_avg_update_delay</td><td>ms</td><td>Mongos 节点更新命令时延平均值。</td></tr>
<tr>
<td>插入平均延迟</td><td>replicaset_node</td><td>ms</td><td>Mongos 节点插入命令时延平均值。</td></tr>
<tr>
<td>读平均时延</td><td>node_avg_read_delay</td><td>ms</td><td>Mongos 节点读命令时延平均值。</td></tr>
<tr>
<td>聚合请求平均时延</td><td>node_avg_aggregate_delay</td><td>ms</td><td>Mongos 节点 aggregate 命令时延平均值。</td></tr>
<tr>
<td>Count 的平均延迟</td><td>node_avg_count_delay</td><td>ms</td><td>Mongos 节点 counts 命令时延平均值。</td></tr>
<tr>
<td>Getmore 平均延迟</td><td>node_avg_getmore_delay</td><td>ms</td><td>Mongos 节点 Getmore 命令时延平均值。</td></tr>
<tr>
<td>删除平均延迟</td><td>node_avg_delete_delay</td><td>ms</td><td>Mongos 节点删除命令时延平均值。</td></tr>
<tr>
<td>Command 平均时延</td><td>node_avg_command_delay</td><td>ms</td><td>Mongos 节点  Command 命令时延平均值。Command 为 除insert、update、delete、query 以外命令的总称。</td></tr>
<tr>
<td>10-50毫秒</td><td>10ms</td><td>次</td><td>执行时间在10毫秒和50毫秒之间每秒请求次数。</td></tr>
<tr>
<td>50-100毫秒</td><td>50ms</td><td>次</td><td>执行时间在50毫秒和100毫秒之间每秒请求次数。</td></tr>
<tr>
<td>100毫秒</td><td>100ms</td><td>次</td><td>执行时间超过100毫秒每秒请求次数。</td></tr>
<tr>
<td rowspan="9">请求监控</td>
<td>总请求</td><td>qps</td><td>次/秒</td><td>Mongos 节点每秒所有请求的次数。</td></tr>
<tr>
<td>插入请求</td><td>inserts</td><td>次/秒</td><td>Mongos 节点每秒插入请求的次数。</td></tr>
<tr>
<td>读请求</td><td>reads</td><td>次/秒</td><td>Mongos 节点每秒读请求的次数。</td></tr>
<tr>
<td>更新请求</td><td>updates</td><td>次/秒</td><td>Mongos 节点每秒更新请求的次数。</td></tr>
<tr>
<td>删除请求</td><td>deletes</td><td>次/秒</td><td>Mongos 节点每秒删除请求的次数。</td></tr>
<tr>
<td>Count 请求</td><td>counts</td><td>次/秒</td><td>Mongos 节点每秒收到的 Count 请求的次数。</td></tr>
<tr><td>Getmore 请求</td><td>getmores</td><td>次/秒</td><td>Mongos 节点每秒收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求</td><td>aggregates</td><td>次/秒</td><td>Mongos 节点每秒聚合请求的次数。</td></tr>
<tr>
<td>Command 请求</td><td>commands</td><td>次/秒</td><td>Mongos 节点每秒收到的 Command 请求的次数。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
<tr><td rowspan="9">请求量</td>
<td>总请求量</br></td><td>node_success</td><td>次</td><td>Mongos 节点收到的总请求次数。</td></tr>
<tr>
<td>插入请求量</br></td><td>node_inserts</td><td>次</td><td>Mongos 节点收到的插入请求的次数。</td></tr>
<tr>
<td>读请求量</br></td><td>node_reads</td><td>次</td><td>Mongos 节点收到的读请求的次数。</td></tr>
<tr>
<td>更新请求量</br></td><td>node_updates</td><td>次</td><td>Mongos 节点收到的更新请求的次数。</td></tr>
<tr>
<td>删除请求量</td><td>node_deletes</td><td>次</td><td>Mongos 节点收到的删除请求的次数。</td></tr>
<tr>
<td>Count 请求量</br></td><td>node_counts</td><td>次</td><td>Mongos 节点收到的 Count 请求的次数。</td></tr>
<tr><td>Getmore 请求量</br></td><td>node_getmores</td><td>次</td><td>Mongos节点收到的 Getmore 请求的次数。</td></tr>
<tr>
<td>Aggregates 请求量</td><td>node_aggregates</td><td>次</td><td>Mongos 节点收到的聚合请求的次数。</td></tr>
<tr>
<td>Command 请求量</td><td>node_commands</td><td>次</td><td>Mongos 节点收到的 Command 请求的次数。Command 为除 insert、update、delete、query 以外命令的总称。</td></tr>
</tbody></table>

