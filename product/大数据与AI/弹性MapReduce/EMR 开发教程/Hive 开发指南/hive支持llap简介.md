apache hive 从 Hive 2.0 版本引⼊了 LLAP（Live Long And Process），2.1版本进⾏了⽐较⼤的优化，可以说 hive 已经⾛向了内存计算。⽬前 hortonworks 测试 llap + tez ⽐ hive1.x 快了25倍。LLAP 提供了混合执行 model，由一个 long-lived 守护进程组成，取代了与 HDFS DataNode 的直接交互和一个紧密集成的 DAG-based framework。例如，缓存 pre-fetching，部分查询处理和访问控制之类的功能被移动到守护进程中。Small/short 查询由此守护程序直接处理，其他较为复杂的查询将在标准 YARN 容器中执行。

## hive-llap 架构图

![](https://main.qcloudimg.com/raw/c650eee1bc1019d8d7d3353b86a469ec.png)
- 持久守护进程
为了便于缓存和 JIT 优化，并消除大部分启动成本，守护程序在 cluster 上的 worker 节点上运行。守护程序处理 I/O、缓存和查询片段执行。
- 执行引擎
LLAP 在现有的 process-based Hive 执行中工作，以保持 Hive 的可伸缩性和多功能性。它不会替换现有的执行 model，而是会增强它。
- 查询片段执行
LLAP 节点执行“查询片段”，例如过滤器、投影、数据变换、部分聚合、排序、分组、散列 `joins/semi-joins` 等。
- I/O
守护进程 off-loads I/O 并从压缩格式转换为单独的线程。数据在准备就绪时传递给执行，因此可以在准备下一批数据时处理以前的批次。数据以简单的 RLE-encoded 柱状格式传递给执行，可以进行矢量化处理；这也是缓存格式，旨在最小化 I/O、缓存和执行之间的复制。
- 缓存
守护进程缓存输入 files 的元数据以及数据。即使对于当前未缓存的数据，也可以缓存元数据和索引信息。

## 安装 hive-llap
1. 进入 EMR [购买页](https://buy.cloud.tencent.com/emapreduce#/)。
2. 选择产品版本：EMR-V2.3.0。
3. 在【可选组件】列表中，选择【TEZ 0.9.2】后就会默认安装 hive-llap，安装目录位于 `/usr/local/service/slider`。
 
## 使用 hive-llap
- 修改`/usr/local/service/slider/conf/slider-client.xml`，增加配置项：
```
<property>
	<name>hadoop.registry.zk.quorum</name>
	<value>zk_ip:zk_port</value>
</property>
```
这里的 value，如果是非高可用集群 IP 是 master 节点，如果是高可用集群，执行如下命令查看 zookeeper 组件（即 zk）。
```
cat /usr/local/service/hadoop/etc/hadoop/hdfs-site.xml |grep 2181
```
- 修改 hive-site.xml（通过控制台下发）
```
<property>
	<name>hive.execution.engine</name>
	<value>tez</value>
</property>
<property>
	<name>hive.llap.execution.mode</name>
	<value>all</value>
</property>
<property>
	<name>hive.execution.mode</name>
	<value>llap</value>
</property>
<property>
	<name>hive.llap.daemon.service.hosts</name>
	<value>@llap_service</value>
</property>
<property>
	<name>hive.zookeeper.quorum</name>
	<value>zk_ip:zk_port</value>
</property>
<property>
	<name>hive.llap.daemon.memory.per.instance.mb</name>
	<value>4000</value>
</property>
<property>
	<name>hive.llap.daemon.num.executors</name>
	<value>2</value>
</property>
<property>
	<name>hive.server2.tez.default.queues</name>
	<value>root.default</value>
</property>
<property>
	<name>hive.server2.tez.initialize.default.sessions</name>
	<value>true</value>
</property>
<property>
	<name>hive.server2.tez.sessions.per.default.queue</name>
	<value>2</value>
</property>
```
>!这里的`hive.zookeeper.quorum`配置项需要填写实际的 zookeeper 地址和端口。
>
 - 重启 hive 所有服务
 - 生成 llap 启动文件和命令
```
hive --service llap --name llap_service --instances 2 --size 2g --loglevel INFO --cache 1g --executors 2 --iothreads 5 --slider-am-container-mb 1024 --args " -XX:+UseG1GC -XX:+ResizeTLAB -XX:+UseNUMA -XX:-ResizePLAB" 
```
这里会在当前目录下生成 llap 的运行和配置文件，根据提示执行`run.sh`脚本，如：
![](https://main.qcloudimg.com/raw/3ed9ac7564736a89a2b17b972582af56.png)
```
llap-slider-27May2020/run.sh
```
执行上面这个`run.sh`文件，这里会在 yarn 上提交一个常驻 application，等待几分钟会在 `yarn-ui` 上看到这个application。
>?这里 LLAP 初始化会需要几分钟，等待几分钟后再去执行数据操作。
- 验证 llap
进入 hive cli
```
create table t1(id int, name string);
insert into t1 values('1','test1'),('2', 'test2');
select id, count(1) from t1 group by id;
```
预期结果：
![](https://main.qcloudimg.com/raw/e29c4a4032916bb0e00edca55876ebd0.png)
