## 云 MongoDB 简介

云数据库 MongoDB（TencentDB for MongoDB）是腾讯云基于开源非关系型数据库 MongoDB 专业打造的高性能、分布式数据存储服务，完全兼容 MongoDB 协议，适用于面向非关系型数据库的场景。

**产品特点:**

1. 提供云存储服务，云存储服务是腾讯云平台面向互联网应用的数据存储服务。
2. 完全兼容 MongoDB 协议，既适用于传统表结构的场景，也适用于缓存、非关系型数据以及利用 MapReduce 进行大规模数据集的并行运算的场景。
3. 提供高性能、可靠、易用、便捷的 MongoDB 集群服务，每一个实例都是至少一主一从的副本集或者是包含多个副本集的分片集群。
4. 拥有整合备份、扩容等功能，尽可能的保证用户数据安全以及动态伸缩能力。

## 技术特征

**分片集群**

1. 每个副本集就是一个分片。
2. 数据写入会根据片健经过一定的hash算法写入不同的片中，不需要应用程序3.根据需要去指定读写库表。
3. 存储量扩容只需要添加分片即可。
![](https://main.qcloudimg.com/raw/39fec6f08d91bf31272722a305026689.png)

**自动容灾**

1. 当发生意外导致主节点不可达时， 集群内部会自动选举出主节点。
2. 如果挂掉的是主节点，重新拉起时，那么它就会变身成一个从节点；如果拉起失败会补充新节点进入集群以达到用户所选择的集群规模。
3. 同样的当任何一个从节点不可达时，也会尝试拉起节点或者补充新节点。
![](https://main.qcloudimg.com/raw/5e3f6a97a3c31f40a1610138b897698f.png)


**在线扩容**

1. 在 Web 控制台或者 API 发起扩容操作。
2. 系统根据需要按新规格创建对应数量的 Secondary 节点。
3. 依次把新创建的 Secondary 节点加入集群实例内部，同步数据。
4. 待最后一个 Secondary 节点数据同步完成以后，开始一个一个剔除原节点，剔除的舒徐按先从（Secondary）后主（Primary）。
5. 当集群内部没有主节点时，会选举出新的主节点。
![](https://main.qcloudimg.com/raw/c5201c21e42ddb3de20bfa14fb7f297d.png)



**完整的备份机制**
 
1. MongoDB 支持全量备份和增量备份两种备份方式
2. 回档功能支持实例回档和库表级别的细粒度回档，极大的减少了海量数据库实例的管理难度。
![](https://main.qcloudimg.com/raw/c2b10ab1825823a3126995b209df7e33.png)

**灵活的读写分离策略**

1. 基于 Secondary 的读写分离策略。连接参数中设置 readrefence=secondary 指定从库读。
2. 基于只读实例的读写分离策略。通过购买 MongoDB 主实例的一个或多个只读实例来实现读写分离需求，通过只读实例读操作来满足大量读应用需求，减轻主库的压力。
![](https://main.qcloudimg.com/raw/786169d57777e8331a52f873d8ae1162.png)


**提供库表回档**
1. 细粒度快速处理错误。
2. 可回档至7天内的任意时刻。
![](https://main.qcloudimg.com/raw/734b3bde096ed03e3446895c1dcce7f0.png)

## MongoDB 架构&监控指标

### 架构图&指标

![](https://main.qcloudimg.com/raw/1291b61f25d768e4a13bf74caebd99f4.png)

### 全量监控指标

<table class="relative-table confluenceTable"><colgroup><col style="width: 10.3214%;" /><col style="width: 7.19368%;" /><col style="width: 17.3587%;" /><col style="width: 16.8895%;" /><col style="width: 25.4907%;" /><col style="width: 6.48995%;" /><col style="width: 15.7948%;" /></colgroup><thead><tr><th class="confluenceTh" style="text-align: left;" colspan="1"><br /></th><th class="confluenceTh" style="text-align: left;" colspan="1">类别</th><th class="confluenceTh" style="text-align: left;">指标英文名</th><th class="confluenceTh" style="text-align: left;">指标中文名</th><th class="confluenceTh" style="text-align: left;">含义</th><th class="confluenceTh" style="text-align: left;">单位</th><th class="confluenceTh" style="text-align: left;">维度</th></tr></thead><tbody><tr><td class="confluenceTd" style="text-align: center;" rowspan="16"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p>MongoDB实例</p></td><td class="confluenceTd" rowspan="10"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p>请求类</p></td><td class="confluenceTd" style="text-align: left;">Inserts</td><td class="confluenceTd" style="text-align: left;">写入请求次数</td><td class="confluenceTd" style="text-align: left;">单位时间内写入次数</td><td class="confluenceTd" style="text-align: left;">次</td><td class="confluenceTd" style="text-align: left;">target（实例 ID）</td></tr><tr><td class="confluenceTd" style="text-align: left;">Reads</td><td class="confluenceTd" style="text-align: left;">读取请求次数</td><td class="confluenceTd" style="text-align: left;">单位时间内读取次数</td><td class="confluenceTd" style="text-align: left;">次</td><td class="confluenceTd" style="text-align: left;">target（实例 ID）</td></tr><tr><td class="confluenceTd" style="text-align: left;">Updates</td><td class="confluenceTd" style="text-align: left;">更新请求次数</td><td class="confluenceTd" style="text-align: left;">单位时间内更新次数</td><td class="confluenceTd" style="text-align: left;">次</td><td class="confluenceTd" style="text-align: left;">target（实例 ID）</td></tr><tr><td class="confluenceTd" style="text-align: left;">Deletes</td><td class="confluenceTd" style="text-align: left;">删除请求次数</td><td class="confluenceTd" style="text-align: left;">单位时间内删除次数</td><td class="confluenceTd" style="text-align: left;">次</td><td class="confluenceTd" style="text-align: left;">target（实例 ID）</td></tr><tr><td class="confluenceTd" style="text-align: left;">Counts</td><td class="confluenceTd" style="text-align: left;">count 请求次数</td><td class="confluenceTd" style="text-align: left;">单位时间内 count 次数</td><td class="confluenceTd" style="text-align: left;">次</td><td class="confluenceTd" style="text-align: left;">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1"><span style="color: #444444;">Aggregates</span></td><td class="confluenceTd" colspan="1"><span style="color: #444444;">聚合请求次数</span></td><td class="confluenceTd" colspan="1">单位时间内聚合请求次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1">Success</td><td class="confluenceTd" colspan="1">成功请求次数</td><td class="confluenceTd" colspan="1">单位时间内成功请求次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1">Commands</td><td class="confluenceTd" colspan="1">command请求次数</td><td class="confluenceTd" colspan="1">单位时间内command请求次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1">Timeouts</td><td class="confluenceTd" colspan="1">超时请求次数</td><td class="confluenceTd" colspan="1">单位时间内超时请求次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1">Qps</td><td class="confluenceTd" colspan="1"><span style="color: #444444;">每秒钟请求次数</span></td><td class="confluenceTd" colspan="1">每秒操作数，包含 CRUD 操作</td><td class="confluenceTd" colspan="1">次/秒</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" rowspan="3"><p><br /></p><p>时延请求类</p></td><td class="confluenceTd" colspan="1">Delay10</td><td class="confluenceTd" colspan="1">时延在10 - 50毫秒间请求次数</td><td class="confluenceTd" colspan="1">单位时间内成功请求延迟在10ms - 50ms次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1">Delay50</td><td class="confluenceTd" colspan="1">时延在50 - 100毫秒间请求次数</td><td class="confluenceTd" colspan="1">单位时间内成功请求延迟在50ms - 100ms次数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1"><strong>Delay100</strong></td><td class="confluenceTd" colspan="1"><strong>时延在100毫秒以上请求次数</strong></td><td class="confluenceTd" colspan="1"><strong>单位时间内成功请求延迟在100ms以上次数</strong></td><td class="confluenceTd" colspan="1"><strong>次</strong></td><td class="confluenceTd" colspan="1"><strong>target（实例 ID）</strong></td></tr><tr><td class="confluenceTd" rowspan="2">连接数类</td><td class="confluenceTd" colspan="1">ClusterConn</td><td class="confluenceTd" colspan="1">集群连接数</td><td class="confluenceTd" colspan="1">集群总连接数，指当前集群 proxy 收到的连接数</td><td class="confluenceTd" colspan="1">次</td><td class="confluenceTd" colspan="1">target（实例 ID）</td></tr><tr><td class="confluenceTd" colspan="1"><strong>Connper</strong></td><td class="confluenceTd" colspan="1"><strong>连接使用率</strong></td><td class="confluenceTd" colspan="1"><strong>当前集群的连接数与集群总连接配置的比例</strong></td><td class="confluenceTd" colspan="1"><strong>%</strong></td><td class="confluenceTd" colspan="1"><strong>target（实例 ID）</strong></td></tr><tr><td class="confluenceTd">系统类</td><td class="confluenceTd" style="text-align: left;"><strong>ClusterDiskusage</strong></td><td class="confluenceTd" style="text-align: left;"><strong>磁盘使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>集群当前实际占用存储空间与总容量配置的比例</strong></td><td class="confluenceTd" style="text-align: left;"><strong>次</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（实例 ID）</strong></td></tr><tr><td class="confluenceTd" style="text-align: center;" rowspan="6"><p><br /></p><p><br /></p><p><br /></p><p>MongoDB副本集</p></td><td class="confluenceTd" colspan="1">系统类</td><td class="confluenceTd" style="text-align: left;"><strong>ReplicaDiskusage</strong></td><td class="confluenceTd" style="text-align: left;"><strong>磁盘使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>副本集容量使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>%</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（副本集 ID）</strong></td></tr><tr><td class="confluenceTd" rowspan="2"><br />主从类</td><td class="confluenceTd" style="text-align: left;">SlaveDelay</td><td class="confluenceTd" style="text-align: left;">主从延迟</td><td class="confluenceTd" style="text-align: left;">主从单位时间内平均延迟</td><td class="confluenceTd" style="text-align: left;">秒</td><td class="confluenceTd" style="text-align: left;">target（副本集 ID）</td></tr><tr><td class="confluenceTd" style="text-align: left;">Oplogreservedtime</td><td class="confluenceTd" style="text-align: left;">oplog保存时间</td><td class="confluenceTd" style="text-align: left;">oplog 记录中最后一次操作和首次操作时间差</td><td class="confluenceTd" style="text-align: left;">小时</td><td class="confluenceTd" style="text-align: left;">target（副本集 ID)</td></tr><tr><td class="confluenceTd" rowspan="3"><br /><br />Cache类</td><td class="confluenceTd" colspan="1">CacheDirty</td><td class="confluenceTd" colspan="1"><span style="color: #003366;">Cache脏数据百分比</span></td><td class="confluenceTd" colspan="1">当前内存Cache中脏数据百分比</td><td class="confluenceTd" colspan="1"><span style="color: #000000;">%</span></td><td class="confluenceTd" colspan="1">target（副本集 ID)</td></tr><tr><td class="confluenceTd" colspan="1">CacheUsed</td><td class="confluenceTd" colspan="1"><span style="color: #003366;">Cache使用百分比</span></td><td class="confluenceTd" colspan="1">当前Cache使用百分比</td><td class="confluenceTd" colspan="1">%</td><td class="confluenceTd" colspan="1">target（副本集 ID)</td></tr><tr><td class="confluenceTd" colspan="1">HitRatio</td><td class="confluenceTd" colspan="1">Cache命中率</td><td class="confluenceTd" colspan="1">当前Cache命中率</td><td class="confluenceTd" colspan="1"><span style="color: #000000;">%</span></td><td class="confluenceTd" colspan="1">target（副本集 ID)</td></tr><tr><td class="confluenceTd" style="text-align: center;" rowspan="12"><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p>MongoDB节点</p></td><td class="confluenceTd" rowspan="5"><p><br /></p><p><br />系统类</p></td><td class="confluenceTd" style="text-align: left;"><strong>CpuUsage</strong></td><td class="confluenceTd" style="text-align: left;"><strong>CPU 使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>CPU 使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>%</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" style="text-align: left;"><strong>MemUsage</strong></td><td class="confluenceTd" style="text-align: left;"><strong>内存使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>内存使用率</strong></td><td class="confluenceTd" style="text-align: left;"><strong>%</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" colspan="1">NetIn</td><td class="confluenceTd" colspan="1">网络入流量</td><td class="confluenceTd" colspan="1">网络入流量</td><td class="confluenceTd" colspan="1">MB/s</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr><tr><td class="confluenceTd" colspan="1">NetOut</td><td class="confluenceTd" colspan="1">网络出流量</td><td class="confluenceTd" colspan="1">网络出流量</td><td class="confluenceTd" colspan="1">MB/s</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr><tr><td class="confluenceTd" colspan="1">Disk</td><td class="confluenceTd" colspan="1"><span style="color: #003366;">节点磁盘用量</span></td><td class="confluenceTd" colspan="1"><span style="color: #003366;">节点磁盘用量</span></td><td class="confluenceTd" colspan="1">MB</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr><tr><td class="confluenceTd">连接数</td><td class="confluenceTd" colspan="1">Conn</td><td class="confluenceTd" colspan="1">连接数</td><td class="confluenceTd" colspan="1">节点连接数</td><td class="confluenceTd" colspan="1">个</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr><tr><td class="confluenceTd" rowspan="4"><p><br /></p><p><br />读写类</p></td><td class="confluenceTd" style="text-align: left;"><strong>Qr</strong></td><td class="confluenceTd" style="text-align: left;"><strong>Read 请求等待队列中的个数</strong></td><td class="confluenceTd" style="text-align: left;"><strong>Read 请求等待队列中的个数</strong></td><td class="confluenceTd" style="text-align: left;"><strong>个</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" style="text-align: left;"><strong>Qw</strong></td><td class="confluenceTd" style="text-align: left;"><strong>Write 请求等待队列中的个数</strong></td><td class="confluenceTd" style="text-align: left;"><strong>Write 请求等待队列中的个数</strong></td><td class="confluenceTd" style="text-align: left;"><strong>个</strong></td><td class="confluenceTd" style="text-align: left;"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" colspan="1"><strong>Ar</strong></td><td class="confluenceTd" colspan="1"><strong>WT引擎的ActiveRead</strong></td><td class="confluenceTd" colspan="1"><strong>Read 请求活跃个数</strong></td><td class="confluenceTd" colspan="1"><strong>个</strong></td><td class="confluenceTd" colspan="1"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" colspan="1"><strong>Aw</strong></td><td class="confluenceTd" colspan="1"><strong>WT引擎的ActiveWrite</strong></td><td class="confluenceTd" colspan="1"><strong>Write 请求活跃个数</strong></td><td class="confluenceTd" colspan="1"><strong>个</strong></td><td class="confluenceTd" colspan="1"><strong>target（节点 ID)</strong></td></tr><tr><td class="confluenceTd" rowspan="2"><p>TTL索引类</p></td><td class="confluenceTd" colspan="1">TtlDeleted</td><td class="confluenceTd" colspan="1">TTL删除的数据条数</td><td class="confluenceTd" colspan="1">TTL删除的数据条数</td><td class="confluenceTd" colspan="1">个</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr><tr><td class="confluenceTd" colspan="1">TtlPass</td><td class="confluenceTd" colspan="1">TTL运转轮数</td><td class="confluenceTd" colspan="1">TTL运转轮数</td><td class="confluenceTd" colspan="1">个</td><td class="confluenceTd" colspan="1">target（节点 ID)</td></tr></tbody></table>




## 告警核心指标&建议阈值

| 告警指标                          | 统计周期      | 判断条件 | 阈值 | 持续周期     | 告警方式           |
| --------------------------------- | ------------- | -------- | ---- | ------------ | ------------------ |
| 时延在100毫秒以上请求次数（实例） | 统计周期1分钟 | >        | 5000 | 持续一个周期 | 每三十分钟告警一次 |
| 磁盘使用率（实例）                | 统计周期1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| 集群连接数百分比（实例）          | 统计周期1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| 磁盘使用率（副本集）              | 统计周期1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| CPU使用率（节点）                 | 统计周期1分钟 | >        | 90%  | 持续一个周期 | 每三十分钟告警一次 |
| 内存使用率（节点）                | 统计周期1分钟 | >        | 90%  | 持续一个周期 | 每三十分钟告警一次 |
| Qr（节点）                        | 统计周期1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Qw（节点）                        | 统计周期1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Ar（节点）                        | 统计周期1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Aw（节点）                        | 统计周期1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |

## 告警最佳实践

### 配置告警的核心指标及建议阈值

1.云数据库 MongoDB实例维度
**磁盘使用率>80%**
注：代表集群容量使用率，集群容量使用率达到100%会被写封禁，影响用户写入，所以需要用户注意提前扩容。

**时延在100毫秒以上请求次数>5000 **  
注：时延在100毫秒以上请求在MongoDB中可以理解为慢查询，是性能问题排查的重要指标。

**集群连接数百分比>80%**
注：预防集群连接数过多，导致MongoDB服务端无法建立更多连接造成客户端无法访问MongoDB集群。

2. 云数据库 MongoDB副集本维度

**磁盘使用率>80%**
注：代码副本集容量使用率，副本集容量使用率达到100%会被写封禁，影响用户写入，所以需要用户注意提前扩容。

3.云数据库 MongoDB节点
**CPU使用率>80%**
注：CPU使用率过高会影响在服务器正常运行程序等系统层面问题。

**内存使用率>80%**
注：内存使用率过高容易引起服务响应速度变慢，服务器登录不上等系统层面问题。
Qr>100，Qw>100，Ar>100，Aw>100

> ?
- Qr|Qw 为等待读/写的队列长度， Ar|Aw 为执行读/写操作客户端数量，都为0的话表示MongoDB毫无压力。
- MongoDB负载高时，命令来不及处理，MongoDB将命令放入队列。高并发时，一般队列值会升高。
- 3Qr|Qw ，Ar|Aw如果一直0说明很健康，如果过高的话那就说明MongoDB处理起来很慢了，有可能有慢查询，锁表排队等现象（Ar|Aw 表示引擎层当前时刻获取“ticket令牌”执行读写操作的请求数。如果请求处理的很快，这个值会很低。如果请求处理很慢，一直占用“ticket令牌”，这个值会很高，需要关注。）


### 实践步骤

#### 设置云数据库 MongoDB 告警

1. 登录 [腾讯云监控控制台](https://console.cloud.tencent.com/monitor )。
2. 单击【告警配置】>【告警策略】>【新建】。
3. 进入新建告警策略页，填写如下信息：
	- 输入策略名称
	- 输入备注
	- 选择策略类型
	- 选择 MongoDB 实例
	- 设置告警指标及触发条件
	- 选择告警渠道，包括接收对象，接收渠道，有效时段，接收语言
  ![](https://main.qcloudimg.com/raw/714c5eae544a9f0713bca7eef9a6cb85.png)

**配置的 MongoDB 节点告警总览**

![](https://main.qcloudimg.com/raw/d134bd3cba3d80185adba0a3ed4c42d3.png)

#### 配置的 MongoDB 节点告警总览

**配置 Dashboard**
1. 登录 [腾讯云监控控制台](https://console.cloud.tencent.com/monitor )。
2. 单击【Dashboard】>【Dashboard 列表】。
3. 在 Dashboard 列表中选择“云数据库 MongoDB 预设面板”。
	- 选择 MongoDB 实例
	- 选择 MongoDB 副本集
	- 选择 MongoDB 节点
	 ![](https://main.qcloudimg.com/raw/91dca17a764ba86211f0ac6710f07eb2.png)
	- 选择 MongoDB 实例，副本集，节点，系统会自动展示出预设的 Dashboard。
	 ![](https://main.qcloudimg.com/raw/1efcbc0d25561c0f6a4a21662b47eaac.png)

