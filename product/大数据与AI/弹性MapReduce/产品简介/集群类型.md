EMR 支持6种集群类型及相应的应用场景，并定义了5种节点类型，不同集群类型及应用场景支持的节点类型及部署节点数、部署服务不同；可根据业务选择不同的集群类型及应用场景创建集群。
>? ClickHouse、Doris、Kafka 集群类型未默认开放，如需要可 [联系工单](https://console.cloud.tencent.com/workorder/category) 开通。

## 集群类型说明
### Hadoop 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >基于开源 Hadoop 及其周边生态组件，提供了海量数据存储、离线/实时数据分析、流式数据计算、机器学习等场景的大数据解决方案。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为管理节点，保证集群的调度正常进行；主要部署 NameNode、ResourceManager、HMaster 等进程；非 HA 模式下数量为1，HA 模式下数量为2。
<br><b>注意：部署组件中含 Kudu 时，集群仅支持 HA 模式，Master 节点数量为3。</b>
<li/><b>Core 节点：</b>为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容；主要部署 DataNode、NodeManager、RegionServer 等进程。非 HA 模式下数量≥2，HA 模式下数量≥3。
<li/><b>Task 节点：</b>为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；主要部署 NodeManager、PrestoWork 等进程；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。 
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点。非HA模式数量为0，HA 模式下数量≥3。
<li/><b>Router 节点：</b>用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容；主要部署 Hadoop 软件包，可选择部署 Hive、Hue、Spark 等软件和进程；可随时更改 Router 节点数，最小值为0。</ul></td>
</tr><tr>
<td >ZooKeeper</td>
<td >适用于大规模集群建立分布式、高可用性的协调服务。</td>
<td><ul style="margin:0"><li/><b>Common 节点：</b>主要部署分布式协调器组件 ZooKeeper，部署节点个数必须是单数，最少3个 Common 节点，仅支持高可用（HA）。</ul></td>
</tr><tr>
<td >HBase</td>
<td >适用于存储海量非结构化数据或半结构化数据，提供高可靠性、高性能、面向列和可伸缩的，实时数据读写的分布式存储系统。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为管理节点，保证集群的调度正常进行；主要部署 NameNode、ResourceManager、HMaster 等进程；非 HA 模式下数量为1，HA 模式下数量为2。
<li/><b>Core 节点：</b>为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容；主要部署 DataNode、NodeManager、RegionServer 等进程。非 HA 模式下数量≥2，HA 模式下数量≥3。
<li/><b>Task 节点：</b>为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；主要部署 NodeManager等进程；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点。非 HA 模式数量为0，HA 模式下数量≥3。
<li/><b>Router 节点：</b>用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容；可随时更改 Router 节点数，最小值为0。
</ul></td>
</tr><tr>
<td >Presto</td>
<td >提供开源的分布式 SQL 查询引擎，适用于交互式分析查询，支持对海量数据进行快速查询分析。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为管理节点，保证集群的调度正常进行；主要部署 NameNode、ResourceManager等进程；非 HA 模式下数量为1，HA 模式下数量为2。
<li/><b>Core 节点：</b>为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容；主要部署 DataNode、NodeManager等进程。非 HA 模式下数量≥2，HA 模式下数量≥3。
<li/><b>Task 节点：</b>为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；主要部署 NodeManager、PrestoWork 等进程；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点。非 HA 模式数量为0，HA 模式下数量≥3。
<li/><b>Router 节点：</b>用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容；可随时更改 Router 节点数，最小值为0。
</ul></td>
</tr><tr>
<td >Kudu</td>
<td >提供分布式可扩展性的列式存储管理器，支持随机读写和 OLAP 分析对更新较快的数据进行处理。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为管理节点，保证集群的调度正常进行；主要部署 NameNode、ResourceManager等进程；非 HA 模式下数量为1，HA 模式下数量为2。
<li/><b>Core 节点：</b>为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容；非 HA 模式下数量≥2，HA 模式下数量≥3。
<li/><b>Task 节点：</b>为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点，非HA模式数量为0，HA模式下数量≥3。
<li/><b>Router 节点：</b>用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容；可随时更改 Router 节点数，最小值为0。
</ul></td>
</tr>
</tbody>
</table>

### Druid 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >支持高性能实时分析，提供了大数据查询毫秒级延迟，支持多种数据摄入方式，适用于大数据实时查询场景。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为管理节点，保证集群的调度正常进行；主要部署 NameNode、ResourceManager等进程；非 HA 模式下数量为1，HA 模式下数量为2。
<li/><b>Core 节点：</b>为计算及存储节点，您在 HDFS 中的数据全部存储于 Core 节点中，因此为了保证数据安全，扩容 Core 节点后不允许缩容；主要部署 DataNode、NodeManager等进程，非 HA 模式下数量≥2，HA 模式下数量≥3。
<li/><b>Task 节点：</b> 为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；主要部署 NodeManager等进程；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件，如 ZooKeeper、JournalNode 等节点，非 HA 模式数量为0，HA 模式下数量≥3。
<li/><b>Router 节点：</b>用以分担 Master 节点的负载或者作为集群的任务提交机，可以随时扩容和缩容；可随时更改 Router 节点数，最小值为0。
</ul></td>
</tr>
</tbody>
</table>

### ClickHouse 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >提供列式数据库管理系统，适用于大宽表实时分析、实时 BI 报表分析、用户行为分析等高性能数仓分析业务场景。</td>
<td><ul style="margin:0"><li/><b>Core 节点：</b>为计算及存储节点；主要部署 ClickHouseServer 进程。
<li/><b>Common 节点：</b>为 HA 集群 Master 节点提供数据共享同步以及高可用容错服务；主要部署分布式协调器组件 ZooKeeper 节点，非 HA 模式数量为0，HA 模式下数量≥3。
</ul></td>
</tr>
</tbody>
</table>

### Doris 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >提供 MPP 分析型数据库产品，对于 PB 数量级、结构化数据可以做到亚秒级查询响应，使用上兼容 MySQL 协议，语法是标准的 SQL。适用于固定历史报表分析、实时数据分析、交互式数据分析等场景。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为 Frontend 模块，同时提供 Web UI 的功能；部署 FE Follower、Broker 等进程，非 HA 模式下数量≥1，HA 模式下数量≥3。
<li/><b>Core 节点：</b>为 Backend 模块，主要提供数据存储功能；部署 BE、Broker 等进程，部署数量≥3。
<li/><b>Router 节点：</b>部署 Frontend 模块，实现读写高可用；可选择部署 FE Observer、Broker 等进程，可扩容增加 Router 节点，不支持缩容。
</ul></td>
</tr>
</tbody>
</table>

### Kafka 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >提供一个分布式、分区的、多副本的、多订阅者，基于 ZooKeeper 协调的消息处理系统，主要适用于异步处理，消息通讯以及流式数据接收和分发场景。</td>
<td><ul style="margin:0"><li/><b>Core 节点：</b>为 Backend 模块，主要提供数据存储功能；部署 BE、Broker 等进程非 HA 模式下数量≥1，HA 模式下数量≥2。
<li/><b>Common 节点：</b>为 HA 集群 Core 节点提供数据共享同步以及高可用容错服务，非 HA 模式数量为0，HA 模式下数量≥3。</ul></td>
</tr>
</tbody>
</table>

### StarRocks 集群
<table>
<thead>
<tr>
<th width=10%>应用场景</th>
<th width=20%>描述</th>
<th width=60%>节点部署说明</th>
</tr>
</thead>
<tbody><tr>
<td >默认场景</td>
<td >StarRocks 采用了全面向量化技术，支持极速统一的OLAP分析数据库，适用多维分析，实时分析，高并发等场景等多种数据分析场景。</td>
<td><ul style="margin:0"><li/><b>Master 节点：</b>为 Frontend 模块，同时提供 Web UI 的功能；部署 FE Follower、Broker 等进程，非 HA 模式下数量≥1，HA 模式下数量≥3。
<li/><b>Core 节点：</b>为 Backend 模块，主要提供数据存储功能；部署 BE、Broker 等进程，部署数量≥3。
<li/><b>Task 节点：</b> 为纯计算节点，不存储数据，被计算的数据来自 Core 节点及 COS 中，因此 Task 节点往往被作为弹性节点，可随时扩容和缩容；主要部署Compute Node进程；可随时更改 Task 节点数，实现集群弹性伸缩，最小值为0。
<li/><b>Router 节点：</b>部署 Frontend 模块，实现读写高可用；可选择部署 FE Observer、Broker 等进程，可扩容增加 Router 节点，不支持缩容。
</ul></td>
</tr>
</tbody>
</table>
