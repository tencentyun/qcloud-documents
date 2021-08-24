EMR 定义了5种节点类型，您可以根据集群类型进行选择：

## Hadoop 集群
<table>
<thead>
<tr>
<th>节点类型</th>
<th>说明</th>
<th>HA（高可用）数量</th>
<th>非 HA 数量</th>
</tr>
</thead>
<tbody><tr>
<td>主节点（Master）</td>
<td>部署 NameNode、ResourceManager、HMaster 等进程。</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>核心节点（Core）</td>
<td>部署 DataNode、NodeManager、RegionServer 等进程。</td>
<td>≥ 3</td>
<td>≥ 2</td>
</tr>
<tr>
<td>计算节点（Task）</td>
<td>部署 NodeManager、PrestoWork 等进程。</td>
<td colspan=2>可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。</td>
</tr>
<tr>
<td>通用节点（Common）</td>
<td>部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点。</td>
<td>≥ 3</td>
<td>0</td>
</tr>
<tr>
<td>路由节点（Router）</td>
<td>部署 Hadoop 软件包，可选择部署 Hive、Hue、Spark 等软件和进程。</td>
<td colspan=2>可随时更改 Router 节点数，最小值为0。</td>
</tr>
</tbody></table>


- Master 节点为管理节点，保证集群的调度正常进行。
- Core 节点为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容。
- Task 节点为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容。
- Common 节点为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务。
- Router 节点用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容。

## ClickHouse 集群
<table>
   <tr>
      <th style="width: 80px;">节点类型</th>
      <th style="width: 100px;">说明</th>
      <th style="width: 80px;">HA（高可用）数量</th>
      <th style="width: 110px;">非 HA 数量</th>
   </tr>
   <tr>
      <td>核心节点（Core）</td>
      <td>部署 ClickHouseServer 进程。</td>
      <td>≥ 2</td>
      <td>≥ 1</td>
   </tr>
   <tr>
      <td>通用节点（Common）</td>
      <td>部署分布式协调器组件 ZooKeeper 节点。</td>
      <td>≥ 3</td>
      <td>0</td>
   </tr>
</table>

- Core 节点为计算及存储节点。
- Common 节点为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务。

## Druid 集群
<table>
<thead>
<tr>
<th>节点类型</th>
<th>说明</th>
<th>HA（高可用）数量</th>
<th>非 HA 数量</th>
</tr>
</thead>
<tbody><tr>
<td>主节点（Master）</td>
<td>部署 NameNode、ResourceManager、Ooverlord、coordinator、ZKFailoverController、JobHistoryServer 等进程。</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>核心节点（Core）</td>
<td>部署 DataNode、NodeManager、middlemanager、historical 等进程。</td>
<td>≥ 3</td>
<td>≥ 2</td>
</tr>
<tr>
<td>计算节点（Task）</td>
<td>部署 NodeManager、middlemanager 等进程。</td>
<td colspan=2>可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。</td>
</tr>
<tr>
<td>通用节点（Common）</td>
<td>部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点。</td>
<td>≥ 3</td>
<td>0</td>
</tr>
<tr>
<td>路由节点（Router）</td>
<td>部署 Hadoop 软件包，可选择部署 broker 等软件和进程。</td>
<td colspan=2>可随时更改 Router 节点数，最小值为0。</td>
</tr>
</tbody></table>

- Master 节点为管理节点，保证集群的调度正常进行。
- Core 节点为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容。
- Task 节点为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容。
- Common 节点为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务。
- Router 节点用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容。


## Kafka 集群
<table>
   <tr>
      <th style="width: 80px;">节点类型</th>
      <th style="width: 100px;">说明</th>
      <th style="width: 80px;">HA（高可用）数量</th>
      <th style="width: 110px;">非 HA 数量</th>
   </tr>
   <tr>
      <td>核心节点（Core）</td>
      <td>部署 Kafka、KafkaManager 等进程。</td>
      <td>≥ 2</td>
      <td>≥ 1</td>
   </tr>
   <tr>
      <td>通用节点（Common）</td>
      <td>部署分布式协调器组件，如 ZooKeeper 等节点。</td>
      <td>≥ 3</td>
      <td>0</td>
   </tr>
</table>

- Core 节点为计算及存储节点。
- Common 节点为 HA 集群 Core 节点提供数据共享同步以及高可用容错服务。


## Doris 集群
<table>
   <tr>
      <th style="width: 80px;">节点类型</th>
      <th style="width: 100px;">说明</th>
      <th style="width: 80px;">HA（高可用）数量</th>
      <th style="width: 110px;">非 HA 数量</th>
   </tr>
	 <tr>
      <td>主节点（Master）</td>
      <td>部署 FE Follower、Broker 等进程。</td>
      <td>≥ 3</td>
      <td>≥ 1</td>
   </tr>
   <tr>
      <td>核心节点（Core）</td>
      <td>部署 BE、Broker 等进程。</td>
      <td colspan=2>≥ 3</td>
   </tr>
   <tr>
      <td>路由节点（Router）</td>
      <td>可选择部署 FE Observer、Broker 等进程。</td>
      <td colspan=2>可扩容增加 router 节点，不支持缩容。</td>
   </tr>
</table>

- Master 节点为 Frontend 模块，同时提供 Web UI 的功能。
- Core 节点为 Backend 模块，主要提供数据存储功能。
- Router 节点部署 Frontend 模块，实现读写高可用。
