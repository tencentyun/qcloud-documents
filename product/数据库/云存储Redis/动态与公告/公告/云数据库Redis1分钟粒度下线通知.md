云监控将计划于**2022年9月31日下线云数据库 Redis 1分钟粒度的告警策略和 QCE/REDIS 命名空间**，下线后将会有以下影响：

- 无法正常接收云数据库 Redis -内存版（1分钟粒度）的告警通知。
- 云数据库 Redis -内存版（1分钟粒度）的 Dashboard 将无法正常显示数据。
- 无法正常拉取云数据库 Redis -内存版（1分钟粒度）监控数据。

**迁移方案**

- 告警策略：需要您将存量云数据库 Redis 1分钟监控粒度实例的告警策略迁移至5秒监控粒度。[单击查看指标对应关系](#step1)。
- Dashboard：需要您将存量云数据库 Redis 1分钟监控粒度实例的 Dashboard 迁移至5秒监控粒度。[单击查看指标对应关系](#step1)。
- API 拉取监控指标数据：需要您将 QCE/REDIS 命名空间切换到 QCE/REDIS_MEM，并且同步修改拉取的指标名称。[单击查看指标对应关系](#step1)。

由于云数据库 Redis 1分钟监控粒度与 [指标对应关系](#step1) 的指标名称命名不完全一致。本文将详细说明云数据库 Redis 1分钟监控粒度与 5秒监控粒度监控指标的对应关系，便于您对照迁移。

<span id="step1"></span>


## 分钟与秒级告警策略监控指标对应关系

<table>
<thead>
<tr><th width="24%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="24%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="40%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU 负载</td>
<td>cpu_us_min</td>    
<td>CPU 使用率</td>
<td>cpu_util</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>CPU 负载最大值</td>
<td>CpuMaxUsMin</td>    
<td>节点最大 CPU 使用率</td>
<td>cpu_max_util</td>
<td>%</td>
<td>实例中节点（分片或者副本）最大 CPU 使用率</td></tr>    
<tr>
<td>内存使用量</td>
<td>storage_min</td>    
<td>内存使用量</td>
<td>mem_used</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>容量使用率</td>
<td>storage_us_min</td>    
<td>内存使用率</td>
<td>mem_util</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr>
<tr>  
<td>容量使用率最大值</td>
<td>StorageMaxUsMin</td>    
<td>节点最大内存使用率</td>
<td>mem_max_util</td>
<td>%</td>
<td>实例中节点（分片或者副本）最大内存使用率</td></tr>    
<tr>
<td>内网入流量</td>
<td>in_flow_min</td>     
<td>入流量</td>
<td>in_flow</td>
<td>Mb/s</td>
<td>内网入流量</td></tr>
<tr>
<td>入流使用率</td> 
<td>in_flow_us_min</td>    
<td>入流量使用率</td>
<td>in_bandwidth_util</td>
<td>%</td>
<td>内网入流量实际使用和最大流量比</td></tr>    
<tr>
<td>内网出流量</td>
<td>out_flow_min</td>      
<td>出流量</td>
<td>out_flow</td>
<td>Mb/s</td>
<td>内网出流量</td></tr>
<tr>
<td>出流使用率</td>
<td>out_flow_us_min</td>     
<td>出流量使用率</td>
<td>out_bandwidth_util</td>
<td>%</td>
<td>内网出流量实际使用和最大流量比</td></tr>
<tr>
<td>连接数</td>
<td>connections_min</td>     
<td>连接数量</td>
<td>connections</td>
<td>个</td>
<td>连接到实例的 TCP 连接数量</td></tr>
    <tr>
<td>连接数使用率</td> 
<td>connections_us_min</td>         
<td>连接使用率</td>
<td>connections_util</td>
<td>%</td>
<td>实际 TCP 连接数量和最大连接数比</td></tr>
<tr>
<td>慢查询个数</td>
<td>slow_query_min</td>    
<td>慢查询</td>
<td>cmd_slow</td>
<td>次</td>
<td>执行时延大于 slowlog - log - slower - than 配置的命令次数</td></tr>
<tr>
<td>Key总个数</td>
<td>keys_min</td>    
<td>Key总个数</td>
<td>keys</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>key 过期数</td>
<td>expired_keys_min</td>   
<td>key 过期数</td>
<td>expired</td>
<td>个</td>
<td>时间窗内被淘汰的 Key 个数，对应 info 命令输出的 expired_keys</td></tr>
<tr>
<td>key驱逐数</td>
<td>evicted_keys_min</td>    
<td>key驱逐数</td>
<td>evicted</td>
<td>个</td>
<td>时间窗内被驱逐的 Key 个数，对应 info 命令输出的 evicted_keys</td></tr>
<tr>
<td>平均执行时延</td>
<td>latency_min</td>    
<td>平均执行时延</td>
<td>latency_avg</td>
<td>ms</td>
<td>proxy 到 redis server 的执行时延平均值</td></tr>
<tr>
<td>读平均时延</td>
<td>latency_get_min</td>    
<td>读平均时延</td>    
<td>latency_read</td>
<td>ms</td>
<td>proxy 到 redis server 的读命令平均执行时延</td></tr>
<tr>
<td>写平均时延</td>
<td>latency_set_min</td>
<td>写平均时延</td>    
<td>latency_write</td>
<td>ms</td>
<td>proxy 到 redis server 的写命令平均执行时延</td></tr>
<tr>
<td>其他命令平均时延</td>
<td>latency_other_min</td>    
<td>其他命令平均时延</td>
<td>latency_other</td>
<td>ms</td>
<td>proxy 到 redis server 的读写命令之外的命令平均执行时延</td></tr>
<tr>
<td>qps</td>
<td>qps_min</td>    
<td>总请求</td>
<td>commands</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求</td>
<td>stat_get_min</td>    
<td>读请求</td>    
<td>cmd_read</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求</td>     
<td>stat_set_min</td>    
<td>写请求</td>
<td>cmd_write</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
<tr>
<td>其他请求</td>    
<td>stat_other_min</td>
<td>其他请求</td> 
<td>cmd_other</td>
<td>次/秒</td>
<td>每秒读写命令之外的命令执行次数</td></tr>
<tr>
<td>大 Value 请求</td>
<td>big_value_min</td>    
<td>大 Value 请求</td>    
<td>cmd_big_value</td>
<td>次/秒</td>
<td>每秒请求命令大小超过32KB的执行次数</td></tr>
<tr>
<td>读请求命中</td>
<td>stat_success_min</td>    
<td>读请求命中</td>    
<td>cmd_hits</td>
<td>次</td>
<td>读请求 Key 存在的个数，对应 info 命令输出的 keyspace_hits 指标</td></tr>
<tr>
<td>读请求Miss</td>
<td>stat_missed_min</td>    
<td>读请求Miss</td>    
<td>cmd_miss</td>
<td>次</td>
<td>读请求 Key 不存在的个数，对应 info 命令输出的 keyspace_misses 指标</td></tr>
<tr>
<td>执行错误</td>
<td>cmd_err_min</td>     
<td>执行错误</td>   
<td>cmd_err</td>
<td>次</td>
<td>命令执行错误的次数，例如命令不存在、参数错误等情况</td></tr>
<tr>
<td>读请求命中率</td> 
<td>cache_hit_ratio_min</td>      
<td>读请求命中率</td>
<td>cmd_hits_ratio</td>
<td>%</td>
<td>Key 命中 / (Key 命中 + KeyMiss)，该指标可以反应 Cache Miss 的情况，当访问为0时，该值为 null</td></tr>
</tbody></table>


## 分钟与秒级 Dashboard 监控指标对应关系

<table>
<thead>
<tr><th width="24%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="24%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="40%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU 使用率</td>
<td>cpu_us_min</td>    
<td>平均 CPU 使用率</td>
<td>cpu_util</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>分片最大 CPU 使用率</td>
<td>cpu_max_us_min</td>    
<td>节点最大 CPU 使用率</td>
<td>cpu_max_util</td>
<td>%</td>
<td>实例中节点（分片或者副本）最大 CPU 使用率</td></tr>    
<tr>
<td>内存使用量</td>
<td>storage_min</td>    
<td>内存使用量</td>
<td>mem_used</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>内存使用率</td>
<td>storage_us_min</td>    
<td>内存使用率</td>
<td>mem_util</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr>
<tr>  
<td>分片最大内存使用率</td>
<td>storage_max_us_min</td>    
<td>节点最大内存使用率</td>
<td>mem_max_util</td>
<td>%</td>
<td>实例中节点（分片或者副本）最大内存使用率</td></tr>    
<tr>
<td>入流量</td>
<td>in_flow_min</td>     
<td>入流量</td>
<td>in_flow</td>
<td>Mb/s</td>
<td>内网入流量</td></tr>
<tr>
<td>入流量使用率</td> 
<td>in_flow_us_min</td>    
<td>入流量使用率</td>
<td>in_bandwidth_util</td>
<td>%</td>
<td>内网入流量实际使用和最大流量比</td></tr>    
<tr>
<td>出流量</td>
<td>out_flow_min</td>      
<td>出流量</td>
<td>out_flow</td>
<td>Mb/s</td>
<td>内网出流量</td></tr>
<tr>
<td>出流量使用率</td>
<td>out_flow_us_min</td>     
<td>出流量使用率</td>
<td>out_bandwidth_util</td>
<td>%</td>
<td>内网出流量实际使用和最大流量比</td></tr>
<tr>
<td>连接数量</td>
<td>connections_min</td>     
<td>连接数量</td>
<td>connections</td>
<td>个</td>
<td>连接到实例的 TCP 连接数量</td></tr>
<tr>
<td>连接使用率</td> 
<td>connections_us_min</td>         
<td>连接数使用率</td>
<td>connections_util</td>
<td>%</td>
<td>实际 TCP 连接数量和最大连接数比</td></tr>
<tr>
<td>慢查询</td>
<td>slow_query_min</td>    
<td>慢查询</td>
<td>cmd_slow</td>
<td>次</td>
<td>执行时延大于 slowlog - log - slower - than 配置的命令次数</td></tr>
<tr>
<td>Key总数</td>
<td>keys_min</td>    
<td>Key总个数</td>
<td>keys</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>key过期数</td>
<td>expired_keys_min</td>   
<td>key过期数</td>
<td>expired</td>
<td>个</td>
<td>时间窗内被淘汰的 Key 个数，对应 info 命令输出的 expired_keys</td></tr>
<tr>
<td>key驱逐数</td>
<td>evicted_keys_min</td>    
<td>key驱逐数</td>
<td>evicted</td>
<td>个</td>
<td>时间窗内被驱逐的 Key 个数，对应 info 命令输出的 evicted_keys</td></tr>
<tr>
<td>平均执行时延</td>
<td>latency_min</td>    
<td>平均执行时延</td>
<td>latency_avg</td>
<td>ms</td>
<td>proxy 到 redis server 的执行时延平均值</td></tr>
<tr>
<td>读平均时延</td>
<td>latency_get_min</td>    
<td>读平均时延</td>    
<td>latency_read</td>
<td>ms</td>
<td>proxy 到 redis server 的读命令平均执行时延</td></tr>
<tr>
<td>写平均时延</td>
<td>latency_set_min</td>
<td>写平均时延</td>    
<td>latency_write</td>
<td>ms</td>
<td>proxy 到 redis server 的写命令平均执行时延</td></tr>
<tr>
<td>其他命令平均时延</td>
<td>latency_other_min</td>    
<td>其他命令平均时延</td>
<td>latency_other</td>
<td>ms</td>
<td>proxy 到 redis server 的读写命令之外的命令平均执行时延</td></tr>
<tr>
<td>qps</td>
<td>qps_min</td>    
<td>总请求</td>
<td>commands</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求数</td>
<td>stat_get_min</td>    
<td>读请求</td>    
<td>cmd_read</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求数</td>     
<td>stat_set_min</td>    
<td>写请求</td>
<td>cmd_write</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
<tr>
<td>get 请求数</td>    
<td>cmdstat_get_min</td>
<td rowspan="18">其他请求</td> 
<td rowspan="18">cmd_other</td>
<td rowspan="18">次/秒</td>
<td rowspan="18">每秒读写命令之外的命令执行次数</td>    
</tr>
<tr>    
<td>getbit 请求数</td>    
<td>cmdstat_getbit_min</td>
</tr>
<tr>       
<td>getrange 请求数</td>    
<td>cmdstat_getrange_min</td>
</tr>
<tr>    
<td>hget 请求数</td>    
<td>cmdstat_hget_min</td>
</tr>
<tr>    
<td>hgetall 请求数</td>    
<td>cmdstat_hmget_min</td>
</tr>
<tr>       
<td>hmget 请求数</td>    
<td>cmdstat_hmget_min</td>
 </tr>
<tr>     
<td>hmset请求数</td>    
<td>cmdstat_hmset_min</td>
</tr>
<tr>      
<td>hset 请求数</td>    
<td>cmdstat_hset_min</td>
</tr>
<tr>      
<td>hsetnx 请求数</td>    
<td>cmdstat_hsetnx_min</td>
</tr>
<tr>      
<td>lset请求数</td>    
<td>cmdstat_lset_min</td>
</tr>
<tr>      
<td>mget请求数</td>    
<td>cmdstat_mget_min</td>
</tr>
<tr>      
<td>mset 请求数</td>    
<td>cmdstat_mset_min</td>
</tr>
<tr>      
<td>msetnx 请求数</td>    
<td>cmdstat_msetnx_min</td>
</tr>
<tr>      
<td>set 请求数</td>    
<td>cmdstat_set_min</td>
</tr>
<tr>      
<td>setbit 请求数</td>    
<td>cmdstat_setbit_min</td>
</tr>
<tr>      
<td>setex 请求数</td>    
<td>cmdstat_setex_min</td>
</tr>
<tr>      
<td>setnx 请求数</td>    
<td>cmdstat_setnx_min</td>
</tr>
<tr>      
<td>setrange 请求数</td>    
<td>cmdstat_setnx_min</td>
</tr>
<tr>
<td>大 Value 请求</td>
<td>big_value_min</td>    
<td>大 Value 请求</td>    
<td>cmd_big_value</td>
<td>次/秒</td>
<td>每秒请求命令大小超过32KB的执行次数</td></tr>
<tr>
<td>读请求命中</td>
<td>stat_success_min</td>    
<td>读请求命中</td>    
<td>cmd_hits</td>
<td>次</td>
<td>读请求 Key 存在的个数，对应 info 命令输出的 keyspace_hits 指标</td></tr>
<tr>
<td>读请求 Miss</td>
<td>stat_missed_min</td>    
<td>读请求 Miss</td>    
<td>cmd_miss</td>
<td>次</td>
<td>读请求 Key 不存在的个数，对应 info 命令输出的 keyspace_misses 指标</td></tr>
<tr>
<td>执行错误</td>
<td>cmd_err_min</td>     
<td>执行错误</td>   
<td>cmd_err</td>
<td>次</td>
<td>命令执行错误的次数，例如命令不存在、参数错误等情况</td></tr>
<tr>
<td>读请求命中率</td> 
<td>cache_hit_ratio_min</td>      
<td>读请求命中率</td>
<td>cmd_hits_ratio</td>
<td>%</td>
<td>Key 命中 / (Key 命中 + KeyMiss)，该指标可以反应 Cache Miss 的情况，当访问为0时，该值为 null</td></tr>
</tbody></table>




### 分钟与秒级 API 监控指标对应关系

### 命名空间

- 分钟： Namespace=QCE/REDIS 
- 秒级： Namespace=QCE/REDIS_MEM 

### 监控指标

#### 实例维度（标准架构）

<table>
<thead>
<tr><th width="35%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="35%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="18%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU 使用率</td>
<td>CpuUsMin</td>    
<td>CPU 使用率</td>
<td>CpuUtil</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>内存使用量</td>
<td>StorageMin</td>    
<td>内存使用量</td>
<td>MemUsed</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>内存使用率</td>
<td>StorageUsMin</td>    
<td>内存使用率</td>
<td>MemUtil</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr> 
<tr>
<td>Key 总数</td>
<td>KeysMin</td>    
<td>Key 总个数</td>
<td>Keys</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>Key 过期数</td>
<td>ExpiredKeysMin</td>    
<td>Key 过期数</td>
<td>Expired</td>
<td>个</td>
<td>时间窗内被淘汰的 Key 个数，对应 info 命令输出的 expired_keys</td></tr>
<tr>
<td>Key驱逐数</td>
<td>EvictedKeysMin</td>    
<td>Key驱逐数</td>
<td>Evicted</td>
<td>个</td>
<td>时间窗内被驱逐的 Key 个数，对应 info 命令输出的 evicted_keys</td></tr>
<tr>
<td>连接数量</td>
<td>ConnectionsMin</td>     
<td>连接数量</td>
<td>Connections</td>
<td>个</td>
<td>连接到实例的 TCP 连接数量</td></tr>
<tr>
<td>连接数使用率</td>
<td>ConnectionsUsMin</td>    
<td>连接使用率</td>
<td>ConnectionsUtil</td>
<td>%</td>
<td>实际 TCP 连接数量和最大连接数比</td></tr>
    <tr>
<td>入流量</td>
<td>InFlowMin</td>     
<td>入流量</td>
<td>InFlow</td>
<td>Mb/s</td>
<td>内网入流量</td></tr>
<tr>
<td>入流量使用率</td>
<td>InFlowUsMin</td>     
<td>入流量使用率</td>
<td>InBandwidthUtil</td>
<td>%</td>
<td>内网入流量实际使用和最大流量比</td></tr>    
<tr>
<td>出流量</td>
<td>OutFlowMin</td>      
<td>出流量</td>
<td>OutFlow</td>
<td>Mb/s</td>
<td>内网出流量</td></tr>
<tr>
<td>出流量使用率</td>
<td>OutFlowUsMin</td>      
<td>出流量使用率</td>
<td>OutBandwidthUtil</td>
<td>%</td>
<td>内网出流量实际使用和最大流量比</td></tr>    
<tr>
<td>平均执行时延</td>
<td>LatencyMin</td>    
<td>平均执行时延</td>
<td>LatencyAvg</td>
<td>ms</td>
<td>proxy 到 redis server 的执行时延平均值</td></tr>
<tr>
<td>读平均时延</td>
<td>LatencyGetMin</td>    
<td>读平均时延</td>    
<td>LatencyRead</td>
<td>ms</td>
<td>proxy 到 redis server 的读命令平均执行时延</td></tr>
<tr>
<td>写平均时延</td>
<td>LatencySetMin</td>
<td>写平均时延</td>    
<td>LatencyWrite</td>
<td>ms</td>
<td>proxy 到 redis server 的写命令平均执行时延</td></tr>
<tr>
<td>其他命令平均时延</td>
<td>LatencyOtherMin</td>    
<td>其他命令平均时延</td>
<td>LatencyOther</td>
<td>ms</td>
<td>proxy 到 redis server 的读写命令之外的命令平均执行时延</td></tr>
<tr>
<td>总请求</td>
<td>QpsMin</td>    
<td>总请求</td>
<td>Commands</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求</td>
<td>StatGetMin</td>    
<td>读请求</td>    
<td>CmdRead</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求</td>     
<td>StatSetMin</td>    
<td>写请求</td>
<td>CmdWrite</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
<tr>
<td>其他请求</td>     
<td>StatOtherMin</td>    
<td>其他请求</td>
<td>CmdOther</td>
<td>次/秒</td>
<td>每秒读写命令之外的命令执行次数</td></tr>
<tr>
<td>大 Value 请求</td>
<td>BigValueMin</td>    
<td>大 Value 请求</td>    
<td>CmdBigValue</td>
<td>次/秒</td>
<td>每秒请求命令大小超过32KB的执行次数</td></tr>
<tr>
    <td>慢查询</td>
    <td>SlowQueryMin</td>
    <td>慢查询</td>
    <td>CmdSlow</td>
    <td>次</td>
    <td>执行时延大于 slowlog - log - slower - than 配置的命令次数</td></tr>    
<tr>
<td>读请求命中</td>
<td>StatSuccessMin</td>    
<td>读请求命中</td>    
<td>CmdHits</td>
<td>次</td>
<td>读请求 Key 存在的个数，对应 info 命令输出的 keyspace_hits 指标</td></tr>
<tr>
<td>读请求Miss</td>
<td>StatMissedMin</td>    
<td>读请求Miss</td>    
<td>CmdMiss</td>
<td>次</td>
<td>读请求 Key 不存在的个数，对应 info 命令输出的 keyspace_misses 指标</td></tr>
<tr>
<td>执行错误</td>
<td>CmdErrMin</td>     
<td>执行错误</td>   
<td>CmdErr</td>
<td>次</td>
<td>命令执行错误的次数，例如命令不存在、参数错误等情况</td></tr>
<tr>
<td>读请求命中率</td> 
<td>CacheHitRatioMin</td>      
<td>读请求命中率</td>
<td>CmdHitsRatio</td>
<td>%</td>
<td>Key 命中 / (Key 命中 + KeyMiss)，该指标可以反应 Cache Miss 的情况，当访问为0时，该值为 null</td></tr>    
</tbody></table>


#### 实例维度（集群架构）

<table>
<thead>
<tr><th width="35%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="35%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="18%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>平均 CPU 使用率</td>
<td>CpuUsMin</td>    
<td>CPU 使用率</td>
<td>CpuUtil</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>分片最大 CPU 使用率</td>
<td>CpuMaxUsMin</td>    
<td>节点最大 CPU 使用率</td>
<td>CpuMaxUtil</td>
<td>%</td>
<td>集群所有分片中，CPU 使用率最高值</td></tr>   
<tr>
<td>内存使用量</td>
<td>StorageMin</td>    
<td>内存使用量</td>
<td>MemUsed</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>内存使用率</td>
<td>StorageUsMin</td>    
<td>内存使用率</td>
<td>MemUtil</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr> 
<tr>
<td>分片最大内存使用率</td>
<td>StorageMaxUsMin</td>    
<td>节点最大内存使用率</td>
<td>MemMaxUtil</td>
<td>%</td>
<td>集群所有分片中，内存使用率最高值</td></tr>  
<tr>
<td>Key总个数</td>
<td>KeysMin</td>    
<td>Key总个数</td>
<td>Keys</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>Key 过期数</td>
<td>ExpiredKeysMin</td>    
<td>Key 过期数</td>
<td>Expired</td>
<td>个</td>
<td>时间窗内被淘汰的 Key 个数，对应 info 命令输出的 expired_keys</td></tr>
<tr>
<td>Key 驱逐数</td>
<td>EvictedKeysMin</td>    
<td>Key 驱逐数</td>
<td>Evicted</td>
<td>个</td>
<td>时间窗内被驱逐的 Key 个数，对应 info 命令输出的 evicted_keys</td></tr>
<tr>
<td>连接数量</td>
<td>ConnectionsMin</td>     
<td>连接数量</td>
<td>Connections</td>
<td>个</td>
<td>连接到实例的 TCP 连接数量</td></tr>
<tr>
<td>连接数使用率</td>
<td>ConnectionsUsMin</td>    
<td>连接使用率</td>
<td>ConnectionsUtil</td>
<td>%</td>
<td>实际 TCP 连接数量和最大连接数比</td></tr>
    <tr>
<td>入流量</td>
<td>InFlowMin</td>     
<td>入流量</td>
<td>InFlow</td>
<td>Mb/s</td>
<td>内网入流量</td></tr>
<tr>
<td>入流量使用率</td>
<td>InFlowUsMin</td>     
<td>入流量使用率</td>
<td>InBandwidthUtil</td>
<td>%</td>
<td>内网入流量实际使用和最大流量比</td></tr>    
<tr>
<td>出流量</td>
<td>OutFlowMin</td>      
<td>出流量</td>
<td>OutFlow</td>
<td>Mb/s</td>
<td>内网出流量</td></tr>
<tr>
<td>出流量使用率</td>
<td>OutFlowUsMin</td>      
<td>出流量使用率</td>
<td>OutBandwidthUtil</td>
<td>%</td>
<td>内网出流量实际使用和最大流量比</td></tr>    
<tr>
<td>平均执行时延</td>
<td>LatencyMin</td>    
<td>平均执行时延</td>
<td>LatencyAvg</td>
<td>ms</td>
<td>proxy 到 redis server 的执行时延平均值</td></tr>
<tr>
<td>读平均时延</td>
<td>LatencyGetMin</td>    
<td>读平均时延</td>    
<td>LatencyRead</td>
<td>ms</td>
<td>proxy 到 redis server 的读命令平均执行时延</td></tr>
<tr>
<td>写平均时延</td>
<td>LatencySetMin</td>
<td>写平均时延</td>    
<td>LatencyWrite</td>
<td>ms</td>
<td>proxy 到 redis server 的写命令平均执行时延</td></tr>
<tr>
<td>其他命令平均时延</td>
<td>LatencyOtherMin</td>    
<td>其他命令平均时延</td>
<td>LatencyOther</td>
<td>ms</td>
<td>proxy 到 redis server 的读写命令之外的命令平均执行时延</td></tr>
<tr>
<td>总请求</td>
<td>QpsMin</td>    
<td>总请求</td>
<td>Commands</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求</td>
<td>StatGetMin</td>    
<td>读请求</td>    
<td>CmdRead</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求</td>     
<td>StatSetMin</td>    
<td>写请求</td>
<td>CmdWrite</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
<tr>
<td>其他请求</td>     
<td>StatOtherMin</td>    
<td>其他请求</td>
<td>CmdOther</td>
<td>次/秒</td>
<td>每秒读写命令之外的命令执行次数</td></tr>
<tr>
<td>大 Value 请求</td>
<td>BigValueMin</td>    
<td>大 Value 请求</td>    
<td>CmdBigValue</td>
<td>次/秒</td>
<td>每秒请求命令大小超过32KB的执行次数</td></tr>
<tr>
    <td>慢查询</td>
    <td>SlowQueryMin</td>
    <td>慢查询</td>
    <td>CmdSlow</td>
    <td>次</td>
    <td>执行时延大于 slowlog - log - slower - than 配置的命令次数</td></tr>    
<tr>
<td>读请求命中</td>
<td>StatSuccessMin</td>    
<td>读请求命中</td>    
<td>CmdHits</td>
<td>次</td>
<td>读请求 Key 存在的个数，对应 info 命令输出的 keyspace_hits 指标</td></tr>
<tr>
<td>读请求Miss</td>
<td>StatMissedMin</td>    
<td>读请求Miss</td>    
<td>CmdMiss</td>
<td>次</td>
<td>读请求 Key 不存在的个数，对应 info 命令输出的 keyspace_misses 指标</td></tr>
<tr>
<td>执行错误</td>
<td>CmdErrMin</td>     
<td>执行错误</td>   
<td>CmdErr</td>
<td>次</td>
<td>命令执行错误的次数，例如命令不存在、参数错误等情况</td></tr>
<tr>
<td>读请求命中率</td> 
<td>CacheHitRatioMin</td>      
<td>读请求命中率</td>
<td>CmdHitsRatio</td>
<td>%</td>
<td>Key 命中 / (Key 命中 + KeyMiss)，该指标可以反应 Cache Miss 的情况，当访问为0时，该值为 null</td></tr>    
</tbody></table>


#### 集群版分片

<table>
<thead>
<tr><th width="35%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="35%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="18%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU 使用率</td>
<td>CpuUsNodeMin</td>    
<td>CPU 使用率</td>
<td>CpuUtilNode</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>内存使用量</td>
<td>StorageNodeMin</td>    
<td>内存使用量</td>
<td>MemUsedNode</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>内存使用率</td>
<td>StorageUsNodeMin</td>    
<td>内存使用率</td>
<td>MemUtilNode</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr> 
<tr>
<td>Key总个数</td>
<td>KeysNodeMin</td>    
<td>Key总个数</td>
<td>KeysNode</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>Key 过期数</td>
<td>ExpiredKeysNodeMin</td>    
<td>Key 过期数</td>
<td>ExpiredNode</td>
<td>个</td>
<td>时间窗内被淘汰的 Key 个数，对应 info 命令输出的 expired_keys</td></tr>
<tr>
<td>Key 驱逐数</td>
<td>EvictedKeysNodeMin</td>    
<td>Key 驱逐数</td>
<td>EvictedNode</td>
<td>个</td>
<td>时间窗内被驱逐的 Key 个数，对应 info 命令输出的 evicted_keys</td></tr>    
<tr>
<td>总请求</td>
<td>QpsNodeMin</td>    
<td>总请求</td>
<td>CommandsNode</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求</td>
<td>StatGetNodeMin</td>    
<td>读请求</td>    
<td>CmdReadNode</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求</td>     
<td>StatSetNodeMin</td>    
<td>写请求</td>
<td>CmdWriteNode</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
<tr>
<td>其他请求</td>     
<td>StatOtherNodeMin</td>    
<td>其他请求</td>
<td>CmdOtherNode</td>
<td>次/秒</td>
<td>每秒读写命令之外的命令执行次数</td></tr>
<tr>
    <td>慢查询</td>
    <td>SlowQueryNodeMin</td>
    <td>慢查询</td>
    <td>CmdSlowNode</td>
    <td>次</td>
    <td>执行时延大于 slowlog-log-slower-than 配置的命令次数</td></tr>    
<tr>
<td>读请求命中</td>
<td>StatSuccessNodeMin</td>    
<td>读请求命中</td>    
<td>CmdHitsNode</td>
<td>次</td>
<td>读请求 Key 存在的个数，对应 info 命令输出的 keyspace_hits 指标</td></tr>
<tr>
<td>读请求 Miss</td>
<td>StatMissedNodeMin</td>    
<td>读请求 Miss</td>    
<td>CmdMissNode</td>
<td>次</td>
<td>读请求 Key 不存在的个数，对应 info 命令输出的 keyspace_misses 指标</td></tr>
<tr>
<td>执行错误</td>
<td>CmdErrNodeMin</td>     
<td>执行错误</td>   
<td>CmdErr</td>
<td>次</td>
<td>命令执行错误的次数，例如命令不存在、参数错误等情况</td></tr>
<tr>
<td>读请求命中率</td> 
<td>CacheHitRatioNodeMin</td>      
<td>读请求命中率</td>
<td>CmdHitsRatioNode</td>
<td>%</td>
<td>Key 命中 / (Key 命中 + KeyMiss)，该指标可以反应 Cache Miss 的情况，当访问为0时，该值为 null</td></tr>    
</tbody></table>


#### 各维度对应参数对应关系说明

| 参数名称（秒级）               | 维度名称   | 维度解释               | 格式                                                         | 对应分钟级说明              |
| ------------------------------ | ---------- | ---------------------- | ------------------------------------------------------------ | --------------------------- |
| Instances.N.Dimensions.0.Name  | instanceid | 实例 ID 维度名称       | 输入 String 类型维度名称：instanceid                         | 分钟和秒级保持一致          |
| Instances.N.Dimensions.0.Value | instanceid | 实例具体 ID            | 输入实例的具体 Redis 实例 ID，例如：tdsql-123456 也可以是实例串号，例如：crs-ifmymj41，可通过 [查询 Redis 实例列表接口](https://cloud.tencent.com/document/api/239/20018) 查询 | 分钟和秒级保持一致          |
| Instances.N.Dimensions.1.Name   | rnodeid    | redis 节点 ID 维度名称 | 输入 String 类型维度名称：rnodeid                            | 对应分钟维度名称：clusterid |
| Instances.N.Dimensions.1.Value  | rnodeid    | redis 具体节点 ID      | 输入 Redis 具体节点 ID，可以通过 [查询实例节点信息](https://cloud.tencent.com/document/api/239/48603) 接口获取 | 对应分钟维度名称：clusterid |

