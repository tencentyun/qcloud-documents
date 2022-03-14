## 简介

[云数据库 MongoDB](https://cloud.tencent.com/document/product/240)（TencentDB for MongoDB）是腾讯云基于开源非关系型数据库 MongoDB 专业打造的高性能、分布式数据存储服务，完全兼容 MongoDB 协议，适用于面向非关系型数据库的场景。

**产品特点:**

1. 提供云存储服务，云存储服务是腾讯云平台面向互联网应用的数据存储服务。
2. 完全兼容 MongoDB 协议，既适用于传统表结构的场景，也适用于缓存、非关系型数据以及利用 MapReduce 进行大规模数据集的并行运算的场景。
3. 提供高性能、可靠、易用、便捷的 MongoDB 集群服务，每一个实例都是至少一主一从的副本集或者是包含多个副本集的分片集群。
4. 拥有整合备份、扩容等功能，尽可能的保证用户数据安全以及动态伸缩能力。

## 技术特征

**分片集群**

1. 每个副本集是一个分片。
2. 数据写入会根据片键经过一定的 hash 算法写入不同的片中，不需要应用程序。
3. 根据需要去指定读写库表。
4. 存储量扩容只需要添加分片即可。
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
4. 待最后一个 Secondary 节点数据同步完成以后，开始一个一个剔除原节点，剔除的原节点按先从（Secondary）后主（Primary）。
5. 当集群内部没有主节点时，会选举出新的主节点。
![](https://main.qcloudimg.com/raw/c5201c21e42ddb3de20bfa14fb7f297d.png)



**完整的备份机制**
 
1. MongoDB 支持**全量备份**和**增量备份**两种备份方式。
2. 回档功能支持实例回档和库表级别的细粒度回档，极大降低了海量数据库实例的管理难度。
![](https://main.qcloudimg.com/raw/c2b10ab1825823a3126995b209df7e33.png)


**灵活的读写分离策略**

1. 基于 Secondary 的读写分离策略。连接参数中设置 readrefence=secondary 指定从库读。
2. 基于只读实例的读写分离策略。通过购买 MongoDB 主实例的一个或多个只读实例来实现读写分离需求，通过只读实例读操作来满足大量读应用需求，减轻主库的压力。
![](https://main.qcloudimg.com/raw/786169d57777e8331a52f873d8ae1162.png)


**提供库表回档**

1. 细粒度快速处理错误。
2. 可回档至7天内的任意时刻。
![](https://main.qcloudimg.com/raw/734b3bde096ed03e3446895c1dcce7f0.png)

## MongoDB 架构和监控指标

### 架构图和指标

![](https://main.qcloudimg.com/raw/1291b61f25d768e4a13bf74caebd99f4.png)

### 全量监控指标

#### MongoDB 实例


<table>
   <tr>
      <th width="10%">类别</th>
      <th width="15%">指标英文名</th>
      <th width="20%">指标中文名</th>
      <th width="30%">含义</th>
      <th width="10%" >单位</th>
      <th width="15%">维度</th>
   </tr>
   <tr>
      <td rowspan="10">请求类</td>
      <td>Inserts</td>
      <td>写入请求次数</td>
      <td>单位时间内写入次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Reads</td>
      <td>读取请求次数</td>
      <td>单位时间内读取次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Updates</td>
      <td>更新请求次数</td>
      <td>单位时间内更新次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Deletes</td>
      <td>删除请求次数</td>
      <td>单位时间内删除次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Counts</td>
      <td>count 请求次数</td>
      <td>单位时间内 count 次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Aggregates</td>
      <td>聚合请求次数</td>
      <td>单位时间内聚合请求次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Success</td>
      <td>成功请求次数</td>
      <td>单位时间内成功请求次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Commands</td>
      <td>Command 请求次数</td>
      <td>单位时间内 Command 请求次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Timeouts</td>
      <td>超时请求次数</td>
      <td>单位时间内超时请求次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Qps</td>
      <td>每秒钟请求次数</td>
      <td>每秒操作数，包含 CRUD 操作</td>
      <td>次/秒</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td rowspan="3">时延请求类</td>
      <td>Delay10</td>
      <td>时延在10 - 50毫秒间请求次数</td>
      <td>单位时间内成功请求延迟在10ms - 50ms次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Delay50</td>
      <td>时延在50 - 100毫秒间请求次数</td>
      <td>单位时间内成功请求延迟在50ms - 100ms次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Delay100</td>
      <td>时延在100毫秒以上请求次数</td>
      <td>单位时间内成功请求延迟在100ms以上次数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td rowspan="2">连接数类</td>
      <td>ClusterConn</td>
      <td>集群连接数</td>
      <td>集群总连接数，指当前集群 proxy 收到的连接数</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>Connper</td>
      <td>连接使用率</td>
      <td>当前集群的连接数与集群总连接配置的比例</td>
      <td>%</td>
      <td>target（实例 ID）</td>
   </tr>
   <tr>
      <td>系统类</td>
      <td>ClusterDiskusage</td>
      <td>磁盘使用率</td>
      <td>集群当前实际占用存储空间与总容量配置的比例</td>
      <td>次</td>
      <td>target（实例 ID）</td>
   </tr>
</table>


#### MongoDB 副本集


<table>
   <tr>
      <th width="10%">类别</th>
      <th width="15%">指标英文名</th>
      <th width="20%">指标中文名</th>
      <th width="30%">含义</th>
      <th width="10%" >单位</th>
      <th width="15%">维度</th>
   </tr>
   <tr>
      <td>系统类</td>
      <td>ReplicaDiskusage</td>
      <td>磁盘使用率</td>
      <td>副本集容量使用率</td>
      <td>%</td>
      <td>target（副本集 ID）</td>
   </tr>
   <tr>
      <td rowspan="2">主从类</td>
      <td>SlaveDelay</td>
      <td>主从延迟</td>
      <td>主从单位时间内平均延迟</td>
      <td>秒</td>
      <td>target（副本集 ID）</td>
   </tr>
   <tr>
      <td>Oplogreservedtime</td>
      <td>oplog 保存时间</td>
      <td>oplog 记录中最后一次操作和首次操作时间差</td>
      <td>小时</td>
      <td>target（副本集 ID)</td>
   </tr>
   <tr>
      <td rowspan="3">Cache 类</td>
      <td>CacheDirty</td>
      <td>Cache 脏数据百分比</td>
      <td>当前内存 Cache 中脏数据百分比</td>
      <td>%</td>
      <td>target（副本集 ID)</td>
   </tr>
   <tr>
      <td>CacheUsed</td>
      <td>Cache 使用百分比</td>
      <td>当前 Cache 使用百分比</td>
      <td>%</td>
      <td>target（副本集 ID)</td>
   </tr>
   <tr>
      <td>HitRatio</td>
      <td>Cache 命中率</td>
      <td>当前 Cache 命中率</td>
      <td>%</td>
      <td>target（副本集 ID)</td>
   </tr>
</table>




#### MongoDB 节点



<table>
   <tr>
      <th width="10%">类别</th>
      <th width="15%">指标英文名</th>
      <th width="20%">指标中文名</th>
      <th width="30%">含义</th>
      <th width="10%" >单位</th>
      <th width="15%">维度</th>
   </tr>
   <tr>
      <td rowspan="5">系统类</td>
      <td>CpuUsage</td>
      <td>CPU 使用率</td>
      <td>CPU 使用率</td>
      <td>%</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>MemUsage</td>
      <td>内存使用率</td>
      <td>内存使用率</td>
      <td>%</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>NetIn</td>
      <td>网络入流量</td>
      <td>网络入流量</td>
      <td>MB/s</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>NetOut</td>
      <td>网络出流量</td>
      <td>网络出流量</td>
      <td>MB/s</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>Disk</td>
      <td>节点磁盘用量</td>
      <td>节点磁盘用量</td>
      <td>MB</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td rowspan="2">连接数</td>
      <td>Conn</td>
      <td>连接数</td>
      <td>节点连接数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>Qr</td>
      <td>Read 请求等待队列中的个数</td>
      <td>Read 请求等待队列中的个数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td rowspan="3">读写类</td>
      <td>Qw</td>
      <td>Write 请求等待队列中的个数</td>
      <td>Write 请求等待队列中的个数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>Ar</td>
      <td>WT 引擎的 ActiveRead</td>
      <td>Read 请求活跃个数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>Aw</td>
      <td>WT 引擎的ActiveWrite</td>
      <td>Write 请求活跃个数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td rowspan="2">TTL 索引类</td>
      <td>TtlDeleted</td>
      <td>TTL 删除的数据条数</td>
      <td>TTL 删除的数据条数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
   <tr>
      <td>TtlPass</td>
      <td>TTL 运转轮数</td>
      <td>TTL 运转轮数</td>
      <td>个</td>
      <td>target（节点 ID)</td>
   </tr>
</table>






## 告警核心指标和建议阈值

| 告警指标                          | 统计粒度      | 判断条件 | 阈值 | 持续周期     | 告警方式           |
| --------------------------------- | ------------- | -------- | ---- | ------------ | ------------------ |
| 时延在100毫秒以上请求次数（实例） | 统计粒度1分钟 | >        | 5000 | 持续一个周期 | 每三十分钟告警一次 |
| 磁盘使用率（实例）                | 统计粒度1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| 集群连接数百分比（实例）          | 统计粒度1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| 磁盘使用率（副本集）              | 统计粒度1分钟 | >        | 80%  | 持续一个周期 | 每三十分钟告警一次 |
| CPU 使用率（节点）                 | 统计粒度1分钟 | >        | 90%  | 持续一个周期 | 每三十分钟告警一次 |
| 内存使用率（节点）                | 统计粒度1分钟 | >        | 90%  | 持续一个周期 | 每三十分钟告警一次 |
| Qr（节点）                        | 统计粒度1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Qw（节点）                        | 统计粒度1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Ar（节点）                        | 统计粒度1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |
| Aw（节点）                        | 统计粒度1分钟 | >        | 100  | 持续一个周期 | 每三十分钟告警一次 |





#### 云数据库 MongoDB 实例维度

- **磁盘使用率 > 80%**
代表集群容量使用率，集群容量使用率达到100%会被写封禁，影响用户写入，所以需要用户注意提前扩容。
- **时延在100毫秒以上请求次数 > 5000**  
时延在100毫秒以上请求在 MongoDB 中可以理解为慢查询，是性能问题排查的重要指标。
- **集群连接数百分比 > 80%**
预防集群连接数过多，导致 MongoDB 服务端无法建立更多连接造成客户端无法访问 MongoDB 集群。


#### 云数据库 MongoDB 副集本维度

- **磁盘使用率 > 80%**
代码副本集容量使用率，副本集容量使用率达到100%会被写封禁，影响用户写入，所以需要用户注意提前扩容。


#### 云数据库 MongoDB 节点
- **CPU 使用率 > 80%**
CPU 使用率过高会影响在服务器正常运行程序等系统层面问题。
- **内存使用率 > 80%**
内存使用率过高容易引起服务响应速度变慢，服务器登录不上等系统层面问题。
Qr>100，Qw>100，Ar>100，Aw>100

> ?
- Qr|Qw 为等待读/写的队列长度， Ar|Aw 为执行读/写操作客户端数量，都为0的话表示 MongoDB 毫无压力。
- MongoDB 负载高时，命令来不及处理，MongoDB 将命令放入队列。高并发时，一般队列值会升高。
- 3Qr|Qw ，Ar|Aw 如果一直0说明很健康，如果过高的话那就说明 MongoDB 处理起来很慢了，有可能有慢查询，锁表排队等现象（Ar|Aw 表示引擎层当前时刻获取“ticket令牌”执行读写操作的请求数。如果请求处理的很快，这个值会很低。如果请求处理很慢，一直占用“ticket令牌”，这个值会很高，需要关注。）


## 操作步骤

### 配置云数据库 MongoDB 告警

1. 登录 [腾讯云监控控制台](https://console.cloud.tencent.com/monitor )。
2. 单击**告警配置** > **告警策略** > **新建**。
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

### 配置 MongoDB 节点告警总览

**配置 Dashboard**
1. 登录 [腾讯云监控控制台](https://console.cloud.tencent.com/monitor )。
2. 单击 **Dashboard** > **Dashboard 列表**。
3. 在 Dashboard 列表中选择“云数据库 MongoDB 预设面板”。
	- 选择 MongoDB 实例
	- 选择 MongoDB 副本集
	- 选择 MongoDB 节点
	 ![](https://main.qcloudimg.com/raw/91dca17a764ba86211f0ac6710f07eb2.png)
	- 选择 MongoDB 实例，副本集，节点，系统会自动展示出预设的 Dashboard
	 ![](https://main.qcloudimg.com/raw/1efcbc0d25561c0f6a4a21662b47eaac.png)

