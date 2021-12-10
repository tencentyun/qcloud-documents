## 简介
DBbrain为方便 Mongo  DBA的日常运维，为您提供了Tencent MongoDB Status工具，此工具主要完成，实时流量及存储引擎监控。可以实现实例级MongoDB Status，和单节点级的MongoDB Status。
## 操作步骤
#### 实例级MongoDB Status
1.   登录[DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择【性能趋势】页。
2.  点击【实例】-->【MongoStaus】
3.  右上方有暂停按钮，可以暂停后观看数据情况。

![](https://qcloudimg.tencent-cloud.cn/raw/97cc7bf6f69350fbd327aba4b18ee6a6.png)

#### 单节点 MongoDB Status

1.   登录[DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择【性能趋势】页。
2.  点击【mongod节点】-->【MongoStaus】
3.  通过下拉列表，选择一个您要查看的节点即可。
4.  右上方有暂停按钮，可以暂停后观看数据情况。

![](https://qcloudimg.tencent-cloud.cn/raw/33d3f710f603ad34f1b5399697b04c4e.png)

## mongostat监控列表字段说明

mongostat，各参数项功能说明如下：

| 监控列表字段 | 说明                     | 性能影响及优化方法                                           |
| ------------ | ------------------------ | ------------------------------------------------------------ |
| host         | 节点地址信息             | -                                                            |
| insert       | 每秒插入数               | 如果update持续性很高，可以配合dirty、used分析进行优化        |
| query        | 每秒查询请求数           | 注意检查索引，确保查询有对应索引                             |
| update       | 每秒更新数               | 1.    注意检查索引，确保查询有对应索引  <br />  2.    如果update持续性很高，可以配合dirty、used分析进行优化 |
| delete       | 每秒删除数               | 1.    注意检查索引，确保查询有对应索引  <br />  2.    如果delete持续性很高，可以配合dirty、used分析进行优化 |
| getmore      | 每秒getMore请求数        | -                                                            |
| command      | 每秒command统计          | -                                                            |
| dirty        | 存储引擎cache脏数据占比  | 如果脏数据持续性高(默认超过20%)，建议提高存储引擎threads_max线程数 |
| used         | 存储引擎cache已用百分比  | 如果脏数据持续性高(默认超过95%)，建议提高存储引擎threads_max线程数 |
| flushes      | 一秒内flush的次数        | -                                                            |
| vsize        | 进程所使用的虚拟内存数量 | -                                                            |
| res          | 进程使用的常驻内存的数量 | -                                                            |
| qrw          | 客户端读写等待队列信息   | 如果arw持续性接近128，并且qrw持续性大于0，则说明请求有排队   |
| arw          | 客户端读写活跃队列信息   | -                                                            |
| net_in       | 入流量                   | -                                                            |
| net_out      | 出流量                   | -                                                            |
| conn         | 连接数                   | -                                                            |
| set          | 副本集名称               | -                                                            |
| repl         | 主从状态信息             | -                                                            |
| time         | 监控时间点               | -                                                            |

  
