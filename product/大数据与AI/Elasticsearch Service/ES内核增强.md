在完全兼容开源内核的基础上，腾讯云 Elasticsearch Service（ES）基于多场景大规模的丰富应用经验，围绕集群性能增强、稳定性提升、成本优化等方向，对 ES 内核进行了持续的深度研究和优化，并始终与开源社区保持着密切的交流。本文为大家介绍腾讯云 ES 的关键内核优化工作。

如果您感兴趣，欢迎访问我们的内核优化专栏 [Elasticsearch 实验室](https://cloud.tencent.com/developer/column/2428) 来获得更多内核特性优化的背景和深度技术剖析，这里记录了我们的最新研究成果。

**2021年2月**发布的重点优化特性：
<table border="1">
    <tr>
        <th>优化维度</th>
        <th>优化分类</th>
				<th>优化策略</th>
				<th>支持版本</th>
    </tr>
    <tr>
        <td rowspan="2">性能优化</td>
        <td>写入性能优化</td>
				<td>分片定向路由优化，解决单索引多分片场景写入流程长尾分片问题，写入吞吐提升10%+，CPU 下降20%+。</td>
				<td>6.8.2、7.5.1、7.10.1</td>
    </tr>
		<tr>
        <td>查询性能优化</td>
				<td>对查询结果进行裁剪，代替 filter_path，查询性能提升10%+。</td>
				<td>6.8.2、7.5.1、7.10.1  </td>
    </tr>
		<tr>
        <td rowspan="3">稳定性优化</td>
        <td>内存优化</td>
				<td>大幅降低高并发写入、大查询导致节点卡死、集群雪崩问题，整体可用性提升至 99.99%。<li/>基于内存资源的 Netty 网络层高并发写入限流。快速回收查询、写入异常的请求所消耗内存，避免异常请求导致内存堆积。优化自研单个请求熔断器，避免单个大查询占用资源过多。<li/>基于 GC 负债管理及时自动重启内存彻底打满的节点。Lucene 文件类型内存映射模型可配置，根据不同的业务场景优化系统内存使用。</td>
				<td>6.8.2、7.5.1、7.10.1</td>
    </tr>
		<tr>
        <td>JDK、GC 优化</td>
				<td>引入腾讯自研优化的 KONA JDK11，修复已知 JDK bug，提升 FGC 串行回收能力。 切换 G1 垃圾回收器，提升 GC 效率，减少 Old GC 导致的毛刺。</td>
				<td>6.8.2、7.5.1、7.10.1</td>
    </tr>
		<tr>
        <td>元数据性能优化</td>
				<td>mapping 更新任务优先级优化，解决高并发 mapping 更新任务堵塞导致大量请求堆积打挂节点问题。元数据异步落盘优化，提升元数据同步性能，避免索引创建、mapping 更新频繁超时。</td>
				<td>6.8.2、7.5.1、7.10.1</td>
    </tr>
		<tr>
        <td rowspan="2">成本优化</td>
        <td>存储优化</td>
				<td>引入 zstd 压缩算法，压缩比提升30% - 50%，压缩性能提升30%。</td>
				<td>6.8.2、7.5.1、7.10.1</td>
    </tr>
</table>


**截至2020年7月**腾讯云 ES 团队自启动内核研究至今的重点优化特性：

<table class="tg">
  <tbody><tr>
    <th class="tg-llyw">优化维度</th>
    <th class="tg-llyw">优化分类</th>
    <th class="tg-llyw">优化策略</th>
    <th class="tg-llyw">	支持版本</th>
  </tr>
<tr>
    <td class="tg-0pky"  rowspan="2">性能优化</td>
    <td class="tg-0pky">写入性能优化</td>
    <td class="tg-0pky">Translog 锁机制优化，总体写入性能提升20%。写入去重优化，segment 文件裁剪优化，带主键写入性能提升50%+。</td>
    <td class="tg-0pky">7.5.1</td>
  </tr>
	<tr>
    <td class="tg-0pky">查询性能优化</td>
    <td class="tg-0pky"><li>聚合性能优化，查询高效剪枝，排序场景 composite 聚合性能提升3 - 7倍。
<li>查询缓存优化，取消开销高、命中率低的数据缓存，实际场景查询毛刺从750ms降至50ms。
<li>合并策略优化，自研基于时序、大小相似性分层合并策略、冷分片自动合并策略，搜索场景查询性能提升40%+。
<li>查询 Fetch 阶段顺序抓取优化，提升缓存命中率，查询结果集较大场景，性能提升10%+。</td>
    <td class="tg-0pky">6.4.3、6.8.2、7.5.1</td>
  </tr>
<tr>
    <td class="tg-0pky"  rowspan="4">稳定性优化</td>
    <td class="tg-0pky">可用性优化</td>
    <td class="tg-0pky"><li>接入层曲线平滑限流。<li>协调节点汇聚子查询结果反序列化膨胀预估、内存检查。<li>大聚合查询结果集流式检查，内存达到阈值熔断请求。<li>自研单个请求熔断器（Single Request Circuit Breaker），避免单个大查询占用资源过多，避免单个大查询占用资源过多影响其它查询。<li>大幅降低高并发写入、大查询导致节点卡死、集群雪崩问题，整体可用性提升至99.99%。
</td>
    <td class="tg-0pky">6.4.3、6.8.2、7.5.1</td>
  </tr>
<tr>
    <td class="tg-0pky">均衡策略优化</td>
    <td class="tg-0pky"><li>引入基于索引、节点打散的均衡策略，优化集群新增节点导致分片严重不均问题。<li>优化多盘（多数据目录）之间分片不均问题。<li>提升集群扩容场景、多盘场景新建索引分片均衡性，减少人工运维成本。
</td>
    <td class="tg-0pky">5.6.4、6.4.3、6.8.2、7.5.1</td>
  </tr>
	<tr>
    <td class="tg-0pky">滚动重启速度优化</td>
    <td class="tg-0pky"><li>优化节点重启分片复用本地数据逻辑。<li>精准控制预定延时时间内的分片拷贝恢复。
大集群单节点重启时间从10多分钟降至1分钟。
</td>
    <td class="tg-0pky">6.4.3、6.8.2、7.5.1</td>
  </tr>
<tr>
    <td class="tg-0pky">在线切主</td>
    <td class="tg-0pky">自研在线切主功能，用户通过 API 指定偏好 master，实现秒级在线切换，典型使用场景：
<li>人工运维时发现当前 master 高负载，在线切换 master 至规格更高、负载低的节点。
<li>滚动重启时，master 节点放到最后重启，重启之前先将 master 角色快速切到别的节点再重启，服务影响从分钟级缩短到秒级。
</td>
    <td class="tg-0pky">6.4.3、6.8.2、7.5.1</td>
  </tr>
	<tr>
	 <td class="tg-0pky"  rowspan="2">成本优化</td>
    <td class="tg-0pky">内存优化</td>
    <td class="tg-0pky"><li>自研堆外 cache，实现 FST Off-Heap 优化。<li>堆外 cache 保障 FST 回收策略可控。<li>精准淘汰策略提高 cache 命中率。<li>零拷贝加多级 cache 保障访问性能。<li>大幅降低堆内存开销，GC 时长下降10%+，单节点磁盘管理规模可达50TB，读写性能基本不受影响。
</td>
    <td class="tg-0pky">6.8.2、7.5.1</td>
  </tr>
	<tr>
    <td class="tg-0pky">存储优化</td>
    <td class="tg-0pky"><li>自研 ID 字段行存裁剪，时序场景存储开销降低20%+。
</td>
    <td class="tg-0pky">5.6.4、6.4.3、6.8.2、7.5.1</td>
  </tr>
</tbody></table>



