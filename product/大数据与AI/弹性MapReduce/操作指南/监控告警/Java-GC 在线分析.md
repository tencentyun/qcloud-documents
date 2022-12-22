## 功能介绍
支持 Java 进程的 GC 在线分析，通过实时采集、记录、分析 GC 日志，帮助用户排查是否因 GC 导致的进程异常。
- GC 视图：筛选服务、角色、节点及时间，查看相关 GC 分布情况及点位信息。
- GC 列表：可根据需要筛选过滤 GC 日志数据，查看 GC 记录的多维度信息。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群监控**，然后选择 JAVA 分析 > GC 在线分析，即可查看 GC 视图及点位信息。
![](https://qcloudimg.tencent-cloud.cn/raw/113a099d782b09273c864bc6884bcd30.png)
3. 同时提供 GC 查询列表信息，部分列头字段支持筛选或排序等操作。
![](https://qcloudimg.tencent-cloud.cn/raw/88a9373579d1aeedca707e5e59a80132.png)
支持 GC 日志采集的服务及角色如下：
<table>
<thead>
<tr>
<th>服务</th>
<th>角色</th>
</tr>
</thead>
<tbody><tr>
<td>Zookeeper</td>
<td>Zookeeper</td>
</tr>
<tr>
<td rowspan=5>HDFS</td>
<td>zkfc</td>
</tr>
<tr>
<td>NameNode</td>
</tr>
<tr>
<td>SecondaryNameNode</td>
</tr>
<tr>
<td>JournalNode</td>
</tr>
<tr>
<td>DataNode</td>
</tr>
<tr>
<td rowspan=4>Yarn</td>
<td>ResourceManager</td>
</tr>
<tr>
<td>NodeManager</td>
</tr>
<tr>
<td>JobHistoryServer</td>
</tr>
<tr>
<td>TimeLineServer</td>
</tr>
<tr>
<td rowspan=3>Hbase</td>
<td>Hmaster</td>
</tr>
<tr>
<td>RegionServer</td>
</tr>
<tr>
<td>HbaseThrift</td>
</tr>
<tr>
<td rowspan=3>Hive</td>
<td>HiveMetaStore</td>
</tr>
<tr>
<td>HiveServer2</td>
</tr>
<tr>
<td>HiveWebHcat</td>
</tr>
<tr>
<td rowspan=2>Knox</td>
<td>ldap</td>
</tr>
<tr>
<td>gateway</td>
</tr>
<tr>
<td>Oozie</td>
<td>Oozie</td>
</tr>
<tr>
<td rowspan=3>Storm</td>
<td>Nimbus</td>
</tr>
<tr>
<td>Supervisor</td>
</tr>
<tr>
<td>worker</td>
</tr>
<tr>
<td>Spark</td>
<td>SparkJobHistoryServer</td>
</tr>
<tr>
<td rowspan=4>Alluxio</td>
<td>AlluxioMaster</td>
</tr>
<tr>
<td>AlluxioJobMaster</td>
</tr>
<tr>
<td>AlluxioWorker</td>
</tr>
<tr>
<td>Alluxio-JobWorker</td>
</tr>
<tr>
<td rowspan=2>Ranger</td>
<td>EmbeddedServer</td>
</tr>
<tr>
<td>EnableUnixAuth</td>
</tr>
<tr>
<td>Livy</td>
<td>LivyServer</td>
</tr>
<tr>
<td>Kylin</td>
<td>Kylin</td>
</tr>
<tr>
<td rowspan=2>Presto</td>
<td>Presto-Coordinator</td>
</tr>
<tr>
<td>Presto-Worker</td>
</tr>
<tr>
<td rowspan=2>Prestosql</td>
<td>PrestoSQL-Coordinator</td>
</tr>
<tr>
<td>PrestoSQL-Worker</td>
</tr>
<tr>
<td>Cosranger</td>
<td>CosRangerServer</td>
</tr>
<tr>
<td rowspan=2>Starrocks</td>
<td>StarRocksFe</td>
</tr>
<tr>
<td>StarRocksBroker</td>
</tr>
<tr>
<td rowspan=2>Doris</td>
<td>DorisFe</td>
</tr>
<tr>
<td>DorisBroker</td>
</tr>
<tr>
<td rowspan=6>Druid</td>
<td>overlord</td>
</tr>
<tr>
<td>coordinator</td>
</tr>
<tr>
<td>router</td>
</tr>
<tr>
<td>broker</td>
</tr>
<tr>
<td>historical</td>
</tr>
<tr>
<td>middleManager</td>
</tr>
<tr>
<td>Zeppelin</td>
<td>Zeppelin</td>
</tr>
<tr>
<td>Kyuubi</td>
<td>KyuubiServer</td>
</tr>
<tr>
<td>Kafka</td>
<td>Kafka</td>
</tr>
</tbody></table>
