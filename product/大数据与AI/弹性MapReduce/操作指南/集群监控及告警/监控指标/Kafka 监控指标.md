<table>
<thead>
<tr>
<th>标题</th>
<th>指标名称</th>
<th>指标单位</th>
<th>指标含义</th>
</tr>
</thead>
<tbody><tr>
<td>CPU 利用率</td>
<td>ProcessCpuLoad</td>
<td>%</td>
<td>进程 CPU 利用率</td>
</tr>
<tr>
<td>CPU 使用时间</td>
<td>ProcessCpuTime</td>
<td>ms</td>
<td>CPU 累计使用时间</td>
</tr>
<tr>
<td rowspan=2>GC 次数</td>
<td>YGC</td>
<td>次</td>
<td>Young GC 次数</td>
</tr>
<tr>
<td>FGC</td>
<td>次</td>
<td>Full GC 次数</td>
</tr>
<tr>
<td rowspan=3>GC 时间</td>
<td>GCT</td>
<td>s</td>
<td>垃圾回收时间消耗</td>
</tr>
<tr>
<td>FGCT</td>
<td>s</td>
<td>Full GC 消耗时间</td>
</tr>
<tr>
<td>YGCT</td>
<td>s</td>
<td>Young GC 消耗时间</td>
</tr>
<tr>
<td rowspan=6>内存区域占比</td>
<td>O</td>
<td>%</td>
<td>Old 区内存使用占比</td>
</tr>
<tr>
<td>M</td>
<td>%</td>
<td>Metaspace 区内存使用占比</td>
</tr>
<tr>
<td>CCS</td>
<td>%</td>
<td>Compressed class space 区内存使用占比</td>
</tr>
<tr>
<td>S0</td>
<td>%</td>
<td>Survivor 0区内存使用占比</td>
</tr>
<tr>
<td>S1</td>
<td>%</td>
<td>Survivor 1区内存使用占比</td>
</tr>
<tr>
<td>E</td>
<td>%</td>
<td>Eden 区内存使用占比</td>
</tr>
<tr>
<td rowspan=7>JVM 内存</td>
<td>MemHeapInitM</td>
<td>MB</td>
<td>JVM 初始 HeapMemory 的数量</td>
</tr>
<tr>
<td>MemNonHeapInitM</td>
<td>MB</td>
<td>JVM 初始 NonHeapMemory 的数量</td>
</tr>
<tr>
<td>MemHeapMaxM</td>
<td>MB</td>
<td>JVM 配置的 HeapMemory 的数量</td>
</tr>
<tr>
<td>MemHeapCommittedM</td>
<td>MB</td>
<td>JVM 当前已经提交的  HeapMemory 的数量</td>
</tr>
<tr>
<td>MemHeapUsedM</td>
<td>MB</td>
<td>JVM 当前已经使用的  HeapMemory 的数量</td>
</tr>
<tr>
<td>MemNonHeapCommittedM</td>
<td>MB</td>
<td>JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr>
<tr>
<td>MemNonHeapUsedM</td>
<td>MB</td>
<td>JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr>
<tr>
<td rowspan=2>文件句柄数</td>
<td>OpenFileDescriptorCount</td>
<td>count</td>
<td>已打开文件描述符数</td>
</tr>
<tr>
<td>MaxFileDescriptorCount</td>
<td>count</td>
<td>最大文件描述符数</td>
</tr>
<tr>
<td>进程运行时间</td>
<td>Uptime</td>
<td>s</td>
<td>进程运行时间</td>
</tr>
<tr>
<td rowspan=3>工作线程数</td>
<td>PeakThreadCount</td>
<td>count</td>
<td>峰值线程数</td>
</tr>
<tr>
<td>ThreadCount</td>
<td>count</td>
<td>总线程数量</td>
</tr>
<tr>
<td>DaemonThreadCount</td>
<td>count</td>
<td>Daemon 线程数量</td>
</tr>
<tr>
<td>Broker 生产流量</td>
<td>OneMinuteRate</td>
<td>bytes/s</td>
<td>一分钟 Broker 生产消息流量</td>
</tr>
<tr>
<td>Broker 消费流量</td>
<td>OneMinuteRate</td>
<td>bytes/s</td>
<td>一分钟 Broker 消费消息流量</td>
</tr>
<tr>
<td>消费被拒流量</td>
<td>OneMinuteRate</td>
<td>bytes/s</td>
<td>一分钟 Topic 请求被拒速率</td>
</tr>
<tr>
<td>Fetch 失败请求次数</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 Fetch 失败请求次数</td>
</tr>
<tr>
<td>Produce 失败请求次数</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 Produce 失败请求次数</td>
</tr>
<tr>
<td>消息生产数</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟消息生产速率</td>
</tr>
<tr>
<td>读取其他 Brokers 流量</td>
<td>OneMinuteRate</td>
<td>bytes</td>
<td>一分钟读取其他 brokers 速率</td>
</tr>
<tr>
<td>读到其他 Brokers 流量</td>
<td>OneMinuteRate</td>
<td>bytes</td>
<td>一分钟读到其他 brokers 速率</td>
</tr>
<tr>
<td>Fetch 请求次数</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 Fetch 总请求速率</td>
</tr>
<tr>
<td>Produce 请求次数</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 Produce 总请求速率</td>
</tr>
<tr>
<td>ControllerBroker</td>
<td>IsControllerBroker</td>
<td>-</td>
<td>Controller所在Broker上的指标值是1，其它Broker上的值是 0</td>
</tr>
<tr>
<td>LeaderElection 速率</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 LeaderElection 速率</td>
</tr>
<tr>
<td rowspan=3>LeaderElection 延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td>
<td>LeaderElection 延时_99thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>LeaderElection 延时_999thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>LeaderElection 延时_Mean</td>
</tr>
<tr>
<td>UncleanLeaderElections 速率</td>
<td>OneMinuteRate</td>
<td>count/s</td>
<td>一分钟 UncleanLeaderElections 速率</td>
</tr>
<tr>
<td>GlobalPartition 数量</td>
<td>GlobalPartitionCount</td>
<td>count</td>
<td>此控制器观察到的全局分区数</td>
</tr>
<tr>
<td>OfflinePartitions 数量</td>
<td>OfflinePartitionCount</td>
<td>count</td>
<td>此控制器观察到的离线分区数</td>
</tr>
<tr>
<td>GlobalTopic 数量</td>
<td>GlobalTopicCount</td>
<td>count</td>
<td>该控制器观察到的 GlobalTopic 的数量</td>
</tr>
<tr>
<td>离线日志目录数</td>
<td>OfflineLogDirectory</td>
<td>count</td>
<td>离线日志目录数量</td>
</tr>
<tr>
<td>LogFlush 速率</td>
<td>OneMinuteRate</td>
<td>calls/s</td>
<td>一分钟消息日志刷新速率</td>
</tr>
<tr>
<td rowspan=3>LogFlush 延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td>
<td>LogFlush 延时_99thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>LogFlush 延时_999thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>LogFlush 延时_Mean</td>
</tr>
<tr>
<td>网络处理器平均空闲率</td>
<td>NetworkProcessorAvgIdlePercent</td>
<td>-</td>
<td>网络线程池线程平均的空闲比例</td>
</tr>
<tr>
<td>ISR 扩展速率</td>
<td>OneMinuteRate</td>
<td>count</td>
<td>一分钟 ISR 扩展速率</td>
</tr>
<tr>
<td>ISR 收缩速率</td>
<td>OneMinuteRate</td>
<td>count</td>
<td>一分钟 ISR 收缩速率</td>
</tr>
<tr>
<td rowspan=2>Replica 数量</td>
<td>LeaderReplicaCount</td>
<td>count</td>
<td>离线 Replica 数量</td>
</tr>
<tr>
<td>OfflineReplicaCount</td>
<td>count</td>
<td>Leader Replica 数量</td>
</tr>
<tr>
<td rowspan=3>Partitions 数量</td>
<td>PartitionCount</td>
<td rowspan=3>count</td>
<td>Partition 数量</td>
</tr>
<tr>
<td>UnderMinIsrPartitionCount</td>
<td>最小 In-Sync  Replica(ISR) 计数下的分区数量</td>
</tr>
<tr>
<td>UnderReplicatedPartitions</td>
<td>UnderReplicatedPartitions 数量</td>
</tr>
<tr>
<td rowspan=3>FetchConsumer 请求延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td>
<td>FetchConsumer 请求时间_75thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>FetchConsumer 请求时间_75thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>平均 FetchConsumer 请求时间</td>
</tr>
<tr>
<td rowspan=3>FetchFollower 请求延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td>
<td>FetchFollower 请求时间_75thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>FetchFollower 请求时间_75thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>平均 FetchFollower 请求时间</td>
</tr>
<tr>
<td rowspan=3>Produce 请求延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td> 
<td>Produce 请求时间_75thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>Produce 请求时间_75thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>平均 Produce 请求时间</td>
</tr>
<tr>
<td>请求队列大小</td>
<td>RequestQueueSize</td>
<td>size</td>
<td>请求队列大小</td>
</tr>
<tr>
<td rowspan=2>Purgatory 大小</td>
<td>Fetch</td>
<td>size</td>
<td>请求在 fetch purgatory 等待的数量</td>
</tr>
<tr>
<td>Produce</td>
<td>-</td>
<td>请求在 producer  purgatory 等待的数量</td>
</tr>
<tr>
<td>请求处理平均空闲率</td>
<td>OneMinuteRate</td>
<td>-</td>
<td>一分钟请求处理空闲率</td>
</tr>
<tr>
<td rowspan=3>ZooKeeper 请求延时</td>
<td>99thPercentile</td>
<td rowspan=3>ms</td>
<td>ZooKeeper 请求延时_99thPercentile</td>
</tr>
<tr>
<td>999thPercentile</td>
<td>ZooKeeper 请求延时_999thPercentile</td>
</tr>
<tr>
<td>Mean</td>
<td>ZooKeeper 请求延时_Mean</td>
</tr>
</tbody></table>
