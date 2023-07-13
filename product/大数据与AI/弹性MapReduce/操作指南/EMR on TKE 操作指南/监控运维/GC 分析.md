## 操作场景
支持 Java 进程的 GC 在线分析，通过实时采集、记录、分析 GC 日志，帮助用户排查是否因 GC 导致的进程异常。
- GC 视图：筛选服务、角色、节点及时间，查看相关 GC 分布情况及点位信息。
- GC 列表：可根据需要筛选过滤 GC 日志数据，查看 GC 记录的多维度信息。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群监控**，然后选择 **JAVA 分析 > GC 在线分析**，即可查看 GC 视图及点位信息。
3. 单击集群详情页**集群信息 > 服务架构 >服务卡片**或者**集群服务> 服务名称**，然后选择 GC 分析即可按需选择角色、节点查看 GC 视图及点位信息。
4. 同时提供 GC 查询列表信息，部分列头字段支持筛选或排序等操作。

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
<td rowspan=3>Trino</td>
<td>Hmaster</td>
</tr>
<tr>
<td>RegionServer</td>
</tr>
<tr>
<td>HbaseThrift</td>
</tr>
<tr>
<td  rowspan=3>Hive</td>
<td>HiveMetaStore</td>
</tr>
<tr>
<td>HiveServer2</td>
</tr>
<tr>
<td>HiveWebHcat</td>
</tr>
<tr>
<td  rowspan=2>Knox</td>
<td>ldap</td>
</tr>
<tr>
<td>gateway</td>
</tr>
<tr>
<td>Spark</td>
<td>SparkJobHistoryServer</td>
</tr>
<tr>
<td  rowspan=2>Ranger</td>
<td>EmbeddedServer</td>
</tr>
<tr>
<td>EnableUnixAuth</td>
</tr>
<tr>
<td>RSS</td>
<td>LivyServer</td>
</tr>
<tr>
<td>Kyuubi</td>
<td>KyuubiServer</td>
</tr>
</tbody></table>

