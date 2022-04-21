云监控将计划于**2022年5月30日下线云数据库 Redis 1分钟粒度的告警策略和 QCE/REDIS 命名空间**，下线后将会有以下影响：

- 无法正常接收云数据库 Redis -内存版（1分钟粒度）和 CKV 版本的告警通知。
- 云数据库 Redis -内存版（1分钟粒度）和 CKV 版本的 Dashboard 将无法正常显示数据。
- 无法正常拉取云数据库 Redis -内存版（1分钟粒度）和 [CKV 版监控指标](https://cloud.tencent.com/document/product/248/45110) 监控数据。

**迁移方案**

- 告警策略：需要您将存量云数据库 Redis 1分钟监控粒度实例的告警策略迁移至5秒监控粒度。[单击查看指标对应关系](#step1)。
- Dashboard：需要您将存量云数据库 Redis 1分钟监控粒度实例的 Dashboard 迁移至5秒监控粒度。[单击查看指标对应关系](#step2)。
- API 拉取监控指标数据：需要您将 QCE/REDIS 命名空间切换到QCE/REDIS_MEM，并且同步修改拉取的指标名称。[单击查看指标对应关系](#step2)。

由于云数据库 Redis 1分钟监控粒度与[单击查看指标对应关系](#step1)的指标名称命名不完全一致。本文将详细说明云数据库 Redis 1分钟监控粒度与 5秒监控粒度监控指标的对应关系，便于您对照迁移。

<span id="step1"></span>

## 分钟与秒级告警策略监控指标对应关系

<table>
<thead>
<tr><th width="24%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="24%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="40%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU负载</td>
<td>cpu_us_min</td>    
<td>CPU使用率</td>
<td>cpu_util</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>CPU负载最大值</td>
<td>CpuMaxUsMin</td>    
<td>节点最大CPU使用率</td>
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



<span id="step2"></span>

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
<td>分片最大CPU使用率</td>
<td>cpu_max_us_min</td>    
<td>节点最大CPU使用率</td>
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
<td>get请求数</td>    
<td>cmdstat_get_min</td>
<td rowspan="18">其他请求</td> 
<td rowspan="18">cmd_other</td>
<td rowspan="18">次/秒</td>
<td rowspan="18">每秒读写命令之外的命令执行次数</td>    
</tr>
<tr>    
<td>getbit请求数</td>    
<td>cmdstat_getbit_min</td>
</tr>
<tr>       
<td>getrange请求数</td>    
<td>cmdstat_getrange_min</td>
</tr>
<tr>    
<td>hget请求数</td>    
<td>cmdstat_hget_min</td>
</tr>
<tr>    
<td>hgetall请求数</td>    
<td>cmdstat_hmget_min</td>
</tr>
<tr>       
<td>hmget请求数</td>    
<td>cmdstat_hmget_min</td>
 </tr>
<tr>     
<td>hmset请求数</td>    
<td>cmdstat_hmset_min</td>
</tr>
<tr>      
<td>hset请求数</td>    
<td>cmdstat_hset_min</td>
</tr>
<tr>      
<td>hsetnx请求数</td>    
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
<td>mset请求数</td>    
<td>cmdstat_mset_min</td>
</tr>
<tr>      
<td>msetnx请求数</td>    
<td>cmdstat_msetnx_min</td>
</tr>
<tr>      
<td>set请求数</td>    
<td>cmdstat_set_min</td>
</tr>
<tr>      
<td>setbit请求数</td>    
<td>cmdstat_setbit_min</td>
</tr>
<tr>      
<td>setex请求数</td>    
<td>cmdstat_setex_min</td>
</tr>
<tr>      
<td>setnx请求数</td>    
<td>cmdstat_setnx_min</td>
</tr>
<tr>      
<td>setrange请求数</td>    
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



<span id="step3"></span>



## 分钟与秒级 API 监控指标对应关系

### 命名空间

- 分钟： Namespace=QCE/REDIS 
- 秒级： Namespace=QCE/REDIS_MEM 

### 监控指标

<table>
<thead>
<tr><th width="24%">1分钟粒度指标</th><th width="5%">1分钟粒度指标英文名</th><th width="24%">5秒粒度指标</th><th width="5%">5秒粒度指标英文名</th><th width="2%">单位</th><th width="40%">指标说明</th></tr>
</thead>
<tbody><tr>
<td>CPU使用率</td>
<td>CpuUs</td>    
<td>CPU使用率</td>
<td>CpuUtil</td>
<td>%</td>
<td>平均 CPU 使用率</td></tr>
<tr>
<td>内存使用量</td>
<td>Storage</td>    
<td>内存使用量</td>
<td>MemUsed</td>
<td>MB</td>
<td>实际使用内存容量，包含数据和缓存部分</td></tr>
<tr>  
<td>内存使用率</td>
<td>StorageUs</td>    
<td>内存使用率</td>
<td>MemUtil</td>
<td>%</td>
<td>实际使用内存和申请总内存之比</td></tr> 
<tr>
<td>入流量</td>
<td>InFlow</td>     
<td>入流量</td>
<td>InFlow</td>
<td>Mb/s</td>
<td>内网入流量</td></tr>  
<tr>
<td>出流量</td>
<td>OutFlow</td>      
<td>出流量</td>
<td>OutFlow</td>
<td>Mb/s</td>
<td>内网出流量</td></tr>
<tr>
<td>连接数量</td>
<td>Connections</td>     
<td>连接数量</td>
<td>Connections</td>
<td>个</td>
<td>连接到实例的 TCP 连接数量</td></tr>
<tr>
<td>Key总个数</td>
<td>Keys</td>    
<td>Key总个数</td>
<td>keys</td>
<td>个</td>
<td>实例存储的总 Key 个数（一级 Key）</td></tr>
<tr>
<td>总请求</td>
<td>Qps</td>    
<td>总请求</td>
<td>Commands</td>
<td>次/秒</td>
<td>QPS，命令执行次数</td></tr>
<tr>
<td>读请求</td>
<td>StatGet</td>    
<td>读请求</td>    
<td>CmdRead</td>
<td>次/秒</td>
<td>每秒读命令执行次数</td></tr>
<tr>
<td>写请求</td>     
<td>StatSet</td>    
<td>写请求</td>
<td>CmdWrite</td>
<td>次/秒</td>
<td>每秒写命令执行次数</td></tr>
</tbody></table>
