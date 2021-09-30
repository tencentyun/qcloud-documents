### EMR-Master 节点配置过低运行失败怎么处理？
#### 问题现象
由于 Master 节点配置过低，导致在该节点提交 hive/spark 作业报错或者直接被 kill。

#### 原因分析
Master 的内存不足导致其他应用 OOM 被 kill。

#### 解决方案
1. EMR 的 Master 节点由于部署了太多的业务，通常都会成为整个集群瓶颈，而 Master 节点无法扩容，只能考虑升配，升配步骤如下：
 - 首先确定客户集群中 standby namenode 所在节点。
    - namenode standby 节点上执行如下命令，进入安全模式。
```
hdfs dfsadmin -fs 10.0.0.9(standby节点IP):4007 -safemode enter 进入安全模式
```
     - namenode standby 节点上执行如下命令，保存元数据。
```
hdfs dfsadmin -fs 10.0.0.9(standby节点IP):4007 -saveNamespace 保存元数据
```
    - namenode standby 节点上执行如下命令，离开安全模式。
```
hdfs dfsadmin -fs 10.0.0.9(standby节点IP):4007 -safemode leave 离开安全模式
```
 - 然后在 EMR 控制台（老集群在 CVM 控制台）对 active 节点进行升级配置。
 - standby 节点配置升级，master 的 active 和 standby 节点配置统一。
>!如果客户集群是非 HA 的，也就是非高可用的，那么升级肯定会有一段时间集群不可用。
2. Spark 提交任务默认模式是 client，driver 在 master 执行。可以将其模式 mode 改为 master 后提交任务。
3. 关于 Hive 组件，启用 Router 节点，将 HiveServer2 迁移到 Router，然后关闭 master 上的 Hive 组件，操作流程可参考 [HiveServer2 迁移到 Router](https://cloud.tencent.com/document/product/589/41198)。
4. 停用 master 上不常用的组件，或将 Hue 迁移到 Router 节点上。
关于 Hue 迁移 Router 操作流程：
 - 进入 EMR 控制台，云硬件管理扩容 Router 节点，选中 Hue 组件。
 - 扩容完成后，停用原来 master-hue 组件，保留 Router 节点的 Hue 组件，为该节点绑定弹性外网 IP，同时安全组开放来源策略及端口。

#### EMR 集群 Master 相应组件内存预设值及建议情况：
1. 常用组件堆内存列表情况
<table>
   <tr>
      <th style="width: 80px;">组件</th>
      <th style="width: 100px;">进程</th>
      <th style="width: 80px;">配置文件</th>
      <th style="width: 110px;">配置项</th>
			<th style="width: 110px;">默认堆内存 mb</th>
   </tr>
   <tr>
      <td>HDFS</td>
      <td>Namenode</td>
      <td>hadoop-env.sh</td>
      <td>NNHeapsize</td>
      <td>4096</td>
   </tr>
   <tr>
      <td>YARN</td>
      <td>Resourcemaneger</td>
      <td>yarn-env.sh</td>
      <td>Heapsize</td>
      <td>2000</td>
   </tr>
   <tr>
      <td>Hive</td>
      <td>Hiveserver2</td>
      <td>hive-env.sh</td>
			<td>HS2Heapsize</td>
      <td>4096</td>
   </tr>
   <tr>
      <td>Hbase</td>
      <td>Hmaster</td>
      <td>hbase-env.sh</td>
      <td>Heapsize</td>
      <td>1024</td>
   </tr>
   <tr>
      <td>Presto</td>
      <td>Coordinator</td>
      <td>jvm.config</td>
      <td>jvm 最大值</td>
      <td>3gb</td>
	 </tr>
	  <tr>
      <td>Spark</td>
      <td>spark-driver</td>
      <td>spark-defaults.conf</td>
      <td>spark.driver.memory</td>
      <td>1024</td>
	 </tr>
	 <tr>
      <td>oozie</td>
      <td>oozie</td>
      <td>-</td>
      <td>-</td>
      <td>1024</td>
	 </tr>
	  <tr>
      <td>storm</td>
      <td>Nimbus</td>
      <td>-</td>
      <td>-</td>
      <td>1024</td>
	 </tr>
</table>
2. 组件建议预设值
<table>
   <tr>
      <th style="width: 80px;">组件</th>
      <th style="width: 100px;">堆内存建议值</th>
   </tr>
   <tr>
      <td>HDFS(Namenode)</td>
      <td>堆内存最小内存 = 250 × 文件数量 + 290 × 目录数量 + 368 × 块数量</td>
   </tr>
   <tr>
      <td>YARN(Resourcemaneger) </td>
      <td>根据实际使用情况调整，可增大</td>
   </tr>
   <tr>
      <td>Hive(Hiveserver2)</td>
      <td>根据实际使用情况调整，可增大 </td>
   </tr>
   <tr>
      <td>Hbase(Hmaster)</td>
      <td>master 仅接收 DDL 请求和做负载均衡，默认1g一般够用 </td>
   </tr>
   <tr>
      <td>Presto(Coordinator)</td>
      <td>默认即可</td>
	 </tr>
	  <tr>
      <td>Spark(spark-driver)</td>
      <td>根据实际使用情况调整，可增大</td>
	 </tr>
	 <tr>
      <td>Oozie(oozie)</td>
      <td>默认即可</td>
	 </tr>
	  <tr>
      <td>Storm(Nimbus)</td>
      <td>默认即可</td>
	 </tr>
</table>
3. 机器系统剩余内存建议值：总内存的10% - 20%。
4. EMR 部署组件根据实际的业务情况可分为独立部署或者混合部署。
 - 独立部署：专门用于存储如 HDFS 集群，用于海量数据分析的 Hbase 集群，计算任务的 spark 集群等。
 - 混合部署：测试集群或当前业务量不大，或资源抢占不严重的情况下可以进行多个组件部署到同一个集群。
