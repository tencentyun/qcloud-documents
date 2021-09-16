## 背景说明
ClickHouse 的集群性能监控存在两种形式，具体如下：
- 购买集群时未启用 Grafana 监控项，仅可使用默认的集群监控页。
- 集群购买时开启了 Grafana 监控项，可使用高级版的集群监控系统，并支持集群告警策略配置。

## 未启用 Grafana 监控 
进入 [云数据仓库 ClickHouse 控制台](https://console.cloud.tencent.com/cdwch)，在集群列表页中单击集群【ID/名称】进入集群详情页，在【集群监控】中可以查看集群的各项性能指标。
![](https://main.qcloudimg.com/raw/b118e48c21c4c50fd4ed0328c3c8173e.png)

| 指标名                  | 释义                                                 |
| ----------------------- | ---------------------------------------------------- |
| 网络连接数              | 服务器的连接总数                                     |
| Select 查询数            | 单位时间内执行查询次数                               |
| 已打开的文件总数        | 已打开的文件数                                       |
| Insert 行数              | 单位时间内执行插入次数                               |
| 正在后台执行的 merge 总量 | 正在合并中的线程数量                                 |
| 查询处理的线程总量      | 启动查询处理的线程数量                               |
| CPU 使用率               | 各节点的 CPU 使用率                                    |
| CPU 一分钟负载          | 各节点分钟级的 CPU 负载                                |
| 磁盘空间使用率          | 磁盘已使用的空间与规格最大可使用磁盘空间的比值 × 100% |
| 内存使用率              | 各节点的内存使用量                                   |
| 出网络流量速率          | 网卡发送数据速率                                     |
| 入网络流量速率          | 网卡接收数据速率                                     |

## 启用 Granafa 监控项
### 监控看板说明
ClickHouse 集群监控信息共内置4个监控看板，用户也可按需配置个性化的监控看板。内置监控看板分别为 Clickhouse 集群看板、主机单节点详情、主机多节点详情和主机节点概览，下面针对每个看板的指标及公式进行详细说明。

**Clickhouse 集群看板**，详细说明见 [指标项说明](#jump)。单击右上角【Clickhouse 监控】，可切换至集群的其他监控看板。
![](https://main.qcloudimg.com/raw/4179816a544d5062f37b46c2c8776d2d.jpg)
**主机单节点详情**，可以根据 IP 查询主机层面指标的详情。
![](https://main.qcloudimg.com/raw/74ca1b4edc14ed14feca9d9604349774.png)
**主机多节点详情**，可以根据 IP 勾选，横向比较8个基础主机指标。
![](https://main.qcloudimg.com/raw/2d2ea643bf8fdf775ec2fe094bc50471.png)
**主机节点概览**，可以概览所有节点的主机基础情况，方便了解集群整体情况。
![](https://main.qcloudimg.com/raw/50d4694409bb52f038a86ee86470557a.png)

### 指标计算公式
用户如果需要了解看板的某个指标的具体释义，可单击看板标题，在下拉菜单中选择【Explore】。
![](https://main.qcloudimg.com/raw/b554c5a628664413d31e63d1db224cc5.png)
Metrics 中的公式即为具体计算方式，node_cppu_seconds_total 即为具体指标，具体指标的含义可参见 [ClickHouse 官网 metrics](https://clickhouse.tech/docs/en/operations/system-tables/metrics/)。
![](https://main.qcloudimg.com/raw/48e230b468108fd6d639b446bd8a3081.png)


### 配置个性化指标看板
若现有看板不满足用户的使用习惯，可自行新建看板或者面板。
1. 在左侧菜单栏单击【+】，并在下拉菜单中单击【Dashboard】。
![](https://main.qcloudimg.com/raw/5860ae80ed2f08c3265515e426946cc3.png)
2. 然后单击【+ Add new panel】新建看板。
![](https://main.qcloudimg.com/raw/6203ab9604542e0007cf4d1138ef96b9.png)
3. 输入指标或者单击【Metrics】查看计算的指标。
![](https://main.qcloudimg.com/raw/cd72539e6d9322f50d4ab697ac74719a.png)
4. 右侧可以选择展示样式，具体可参见 [Grafana 官网](https://grafana.com/docs/grafana/latest/panels/)。
![](https://main.qcloudimg.com/raw/6155e7249b8e20b3d02007301eafee03.png)
5. 单击右上角【Apply】即可完成看板的配置，最后单击【Save】保存看板。

[](id:jump)
### 指标项说明
<table>
<thead>
<tr>
<th>指标名</th>
<th>释义</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td>Total query</td>
<td>单位时间内增删改查语句的执行次数</td>
<td>-</td>
</tr>
<tr>
<td>Query</td>
<td>单位时间内执行查询次数</td>
<td>-</td>
</tr>
<tr>
<td>Replication</td>
<td>单副本的发送、获取、检查的执行情况</td>
<td>-</td>
</tr>
<tr>
<td>Insert Query</td>
<td>单位时间内执行插入次数</td>
<td>-</td>
</tr>
<tr>
<td>Connections</td>
<td>各节点的连接数展示</td>
<td>-</td>
</tr>
<tr>
<td>Read/Write  Syscalls</td>
<td>各节点读写的系统调用次数</td>
<td>-</td>
</tr>
<tr>
<td>Number of Read/Write with a File Descriptor</td>
<td>单位时间文件读写的句柄数及读写失败的句柄数</td>
<td>-</td>
</tr>
<tr>
<td>Bytes of  Read/Write with a File Descriptor</td>
<td>单位时间文件读写的大小</td>
<td>-</td>
</tr>
<tr>
<td>Cache Rate</td>
<td>缓存命中几率及未命中几率</td>
<td>体现业务的重复查询情况</td>
</tr>
<tr>
<td>Selected Ranges</td>
<td>查询命中索引的个数，匹配某个命中 sql 的查询数据量</td>
<td>-</td>
</tr>
<tr>
<td>Selected Marks</td>
<td>查询命中索引的个数，匹配某个 sql 的查询数据量，粒度更细</td>
<td>-</td>
</tr>
<tr>
<td>Merge1</td>
<td>正在合并中的线程数量</td>
<td>num of merge 的个数不能设置太大，merge rate太大，说明导入每批次数据量太小，数据比较集中，part 文件目录正比</td>
</tr>
<tr>
<td>Merge2</td>
<td>正在合并中的 MergedRows 数量</td>
<td>-</td>
</tr>
<tr>
<td>Merges Time</td>
<td>反应压缩消耗时间（速率）</td>
<td>跟压缩的数据量有关</td>
</tr>
<tr>
<td>Parts of  ReplicatedMergeTree Merged</td>
<td>单位时间内的 Replicated  Part 合并数</td>
<td>-</td>
</tr>
<tr>
<td>Mutations</td>
<td>单位时间内的 Replicated  Part 变化次数</td>
<td>-</td>
</tr>
<tr>
<td>Pool Tasks</td>
<td>后台执行的任务数</td>
<td>-</td>
</tr>
<tr>
<td>Open Files</td>
<td>单位时间内打开的文件数</td>
<td>-</td>
</tr>
<tr>
<td>Compressed Read  Buffer</td>
<td>单位时间内使用的压缩读缓存大小</td>
<td>-</td>
</tr>
<tr>
<td>Memory</td>
<td>各节点的内存使用大小</td>
<td>-</td>
</tr>
</tbody></table>
