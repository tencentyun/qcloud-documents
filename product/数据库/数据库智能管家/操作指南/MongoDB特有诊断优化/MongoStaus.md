## 简介
为方便数据库管理员的日常运维，DBbrain 为您提供了 Tencent MongoDB Status 工具，此工具主要完成实时流量及存储引擎监控，可以实现实例级 MongoDB Status 和单节点级的 MongoDB Status。

## 操作步骤
### 实例级 MongoDB Status
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/performance/monitor)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**性能趋势**页。
2. 选择**实例** > **MongoStaus**。
3. 单击右上方暂停按钮，可以暂停后观看数据情况。
![](https://qcloudimg.tencent-cloud.cn/raw/3d2e438d2552c9de27211fd0e21189ae.png)

### 单节点 MongoDB Status
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/performance/monitor)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**性能趋势**页。
2. 选择**mongod节点** > **MongoStaus**。
3. 通过下拉列表，选择一个您要查看的节点。
3. 单击右上方暂停按钮，可以暂停后观看数据情况。
![](https://qcloudimg.tencent-cloud.cn/raw/a6b976a83db094e0fe6bb9c98f462554.png)

## MongoStaus 监控列表字段说明
MongoStaus 各参数项功能说明如下：

| 监控列表字段 | 说明                     | 性能影响及优化方法                                           |
| ------------ | ------------------------ | ------------------------------------------------------------ |
| host         | 节点地址信息             | -                                                            |
| insert       | 每秒插入数               | 如果 update 持续性很高，可以配合 dirty、used 分析进行优化        |
| query        | 每秒查询请求数           | 注意检查索引，确保查询有对应索引                             |
| update       | 每秒更新数               | 1. 注意检查索引，确保查询有对应索引<br>2. 如果 update 持续性很高，可以配合 dirty、used 分析进行优化 |
| delete       | 每秒删除数               | 1. 注意检查索引，确保查询有对应索引<br> 2. 如果 delete 持续性很高，可以配合 dirty、used 分析进行优化 |
| getmore      | 每秒 getMore 请求数        | -                                                            |
| command      | 每秒 command 统计          | -                                                            |
| dirty        | 存储引擎 cache 脏数据占比  | 如果脏数据持续性高（默认超过20%），建议提高存储引擎 threads_max 线程数 |
| used         | 存储引擎 cache 已用百分比  | 如果脏数据持续性高（默认超过95%），建议提高存储引擎 threads_max 线程数 |
| flushes      | 一秒内 flush 的次数        | -                                                            |
| vsize        | 进程所使用的虚拟内存数量 | -                                                            |
| res          | 进程使用的常驻内存的数量 | -                                                            |
| qrw          | 客户端读写等待队列信息   | 如果 arw 持续性接近128，并且 qrw 持续性大于0，则说明请求有排队   |
| arw          | 客户端读写活跃队列信息   | -                                                            |
| net_in       | 入流量                   | -                                                            |
| net_out      | 出流量                   | -                                                            |
| conn         | 连接数                   | -                                                            |
| set          | 副本集名称               | -                                                            |
| repl         | 主从状态信息             | -                                                            |
| time         | 监控时间点               | -                                                            |

  
