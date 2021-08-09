## 背景
弹性 MapReduce 产品于2019年9月10日对主机以及组件服务监控项进行了升级，新增了“弹性 MapReduce”策略类型，覆盖了数百监控项指标，您可以在云监控**“[弹性 MapReduce](https://cloud.tencent.com/document/product/248/44797)”**策略类型下配置告警策略。**原“EMR”策略类型将于2021年03月30日23:00下线，已配置的“EMR”策略类型将全部失效**。后续新增告警策略，请配置在“弹性 MapReduce”策略类型下。

 **“EMR”与“弹性 MapReduce”策略类型对比：**

| 策略类型      | 指标覆盖                                       | 支持与维护                              |
| ------------- | ---------------------------------------------- | --------------------------------------- |
| EMR           | <li>集群告警（12个指标）</li> <li>子机告警（8个指标）</li> | 将于2021年04月09日23:00下线，且不在维护 |
| 弹性 MapReduce | <li>主机监控</li><li>服务监控</li> <li>集群监控</li>            | 已于2019年09月10日上线，持续维护         |

>!“弹性 MapReduce”策略类型已覆盖原有 EMR 策略所有指标，详情可参考 [新老指标对照表](#jump)。

## 告警策略迁移说明
在“EMR”策略类型下线时，系统会自动将原有的“EMR”策略类型的告警策略后台迁移至新的“弹性 MapReduce”策略类型下，具体规则和验证方法见后续通知。

>!不排除极个别用户存在需要手动迁移的特殊情况。

**手动迁移具体步骤如下:**
1. 梳理已有告警指标以及告警策略
登录 [云监控控制台](https://console.cloud.tencent.com/monitor/overview)，选择左侧菜单栏【告警管理】>【告警配置】>【告警策略】中，单击【高级筛选】，在弹出页面中按【策略类型】选择“EMR”策略类型对应的告警策略类型，查询对应类别下的告警策略，并下载原“EMR”策略类型下已配置的告警策略。
![](https://main.qcloudimg.com/raw/915aa69f6ef27fe2fda9bb289f1ff40d.png)
2. 配置新告警策略
在集群列表中单击【告警配置】，跳转至【告警策略】页面后，单击【新建】，在策略类型中选择“弹性 MapReduce”，根据第1步梳理下载的策略进行告警配置，告警配置方法可参考 [配置告警](https://cloud.tencent.com/document/product/589/14626)。
3. 验证新的告警策略
验证“弹性 MapReduce”告警策略是否启用并能成功触发告警。在【指标告警】设置一个最小触发阈值，选择设定【接收组或接收人】，以及选择接受渠道（邮件、短信、微信），达到测试验证效果。例如内存区域占比\_SO，统计周期五分钟，当阈值大于等于1%，持续1周期即触发告警，每五分钟告警一次。
4. 清理旧告警策略
新策略类型验证完成后删除原“EMR”策略类型下配置的告警策略。在告警策略筛选条件中按【策略类型】选择“EMR”策略类型对应的告警策略进行查询，对照步骤1中下载策略表，进行删除。
![](https://main.qcloudimg.com/raw/e17098fecacf63c0957e298fe39e70ab.png)
如果您在迁移中遇到问题，请及时通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们进行处理。

[](id:jump)
## 新老指标对照表

<table>
<thead>
<tr>
<th><strong>原有策略类型</strong></th>
<th><strong>指标/事件告警</strong></th>
<th><strong>原有指标/事件告警名称</strong></th>
<th><strong>新策略类型</strong></th>
<th><strong>新指标/事件名称</strong></th>
</tr>
</thead>
<tbody><tr>
<td rowspan="14">EMR-集群告警</td>
<td>指标告警</td>
<td>HDFS 已用存储空间</td>
<td>弹性 MapReduce-HDFS-概览</td>
<td>集群存储容量_CapacityUsed</td>
</tr>
<tr>
<td>指标告警</td>
<td>HDFS 存储利用率</td>
<td>弹性 MapReduce-HDFS-概览</td>
<td>HDFS 存储空间使用率_capacityused</td>
</tr>
<tr>
<td>指标告警</td>
<td>YARN 应用阻塞数</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>Applications_pending</td>
</tr>
<tr>
<td>指标告警</td>
<td>YARN 应用失败数</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>Applications_failed</td>
</tr>
<tr>
<td>指标告警</td>
<td>集群 CPU 已分配核数</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>Cores_allocatedVirtualCores</td>
</tr>
<tr>
<td>指标告警</td>
<td>集群 CPU 利用率</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>CPU 使用率_usageRatio</td>
</tr>
<tr>
<td>指标告警</td>
<td>集群内存可用空间</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>Memory_availableMB</td>
</tr>
<tr>
<td>指标告警</td>
<td>集群内存利用率</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>内存使用率_usageRatio</td>
</tr>
<tr>
<td>指标告警</td>
<td>集群容器阻塞数</td>
<td>弹性 MapReduce-YARN-概览</td>
<td>Containers_containersPending</td>
</tr>
<tr>
<td>指标告警</td>
<td>Hbase 请求量</td>
<td>弹性 MapReduce-HBASE-概览</td>
<td>集群总请求数量_clusterRequests</td>
</tr>
<tr>
<td>指标告警</td>
<td>Hbase 同步耗时</td>
<td>不在维护</td>
<td>-</td>
</tr>
<tr>
<td>指标告警</td>
<td>Hbase 同步 log 长度</td>
<td>不在维护</td>
<td>-</td>
</tr>
<tr>
<td>事件告警</td>
<td>节点监控心跳丢失</td>
<td>弹性 MapReduce-主机监控-网络</td>
<td>节点监控心跳丢失</td>
</tr>
<tr>
<td>事件告警</td>
<td>进程重启</td>
<td>弹性 MapReduce-主机监控-进程</td>
<td>进程 OOM</td>
</tr>
<tr>
<td rowspan="8">EMR-子机告警</td>
<td>指标告警</td>
<td>磁盘利用率</td>
<td>弹性 MapReduce-主机监控-磁盘</td>
<td>磁盘空间使用率_used_all</td>
</tr>
<tr>
<td>指标告警</td>
<td>内存使用量</td>
<td>弹性 MapReduce-主机监控-内存</td>
<td>内存使用情况_MemFree</td>
</tr>
<tr>
<td>指标告警</td>
<td>机器重启</td>
<td>不在维护</td>
<td>机器重启</td>
</tr>
<tr>
<td>指标告警</td>
<td>内存利用率</td>
<td>弹性 MapReduce-主机监控-内存</td>
<td>内存使用占比_used_percent</td>
</tr>
<tr>
<td>指标告警</td>
<td>CPU 利用率</td>
<td>弹性 MapReduce-主机监控-CPU</td>
<td>CPU 使用率_idle</td>
</tr>
<tr>
<td>指标告警</td>
<td>内网入包量</td>
<td>不在维护</td>
<td>-</td>
</tr>
<tr>
<td>指标告警</td>
<td>内网出包量</td>
<td>不在维护</td>
<td>-</td>
</tr>
<tr>
<td>指标告警</td>
<td>TCP 连接数</td>
<td>弹性 MapReduce-主机监控-网络</td>
<td>TCP 连接数</td>
</tr>
</tbody></table>

