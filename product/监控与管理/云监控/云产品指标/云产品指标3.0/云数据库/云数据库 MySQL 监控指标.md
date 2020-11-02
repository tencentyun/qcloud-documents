## 命名空间

Namespace=QCE/CDB

## 监控指标

| 指标英文名                   | 指标中文名                               | 含义                                                         | 单位    | 维度                     |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------------------ | ------- | ------------------------ |
| CPUUseRate                   | CPU 利用率                                | 允许闲时超用，CPU 利用率可能大于100%                         | %       | InstanceId、InstanceType |
| MemoryUseRate                | 内存利用率                               | 允许闲时超用，内存利用率可能大于100%                         | %       | InstanceId、InstanceType |
| MemoryUse                    | 内存占用                                 | 允许闲时超用，实际内存占用可能大于购买规格                   | MB      | InstanceId、InstanceType |
| VolumeRate                   | 磁盘使用率                               | 磁盘使用空间/实例购买空间                                    | %       | InstanceId、InstanceType |
| RealCapacity                 | 磁盘使用空间（仅包含数据空间使用量）     | 仅包括 MySQL 数据目录，不含 binlog、relaylog、undolog、errorlog、slowlog 日志空间 | MB      | InstanceId、InstanceType |
| Capacity                     | 磁盘占用空间（包含数据及日志空间使用量） | 包括 MySQL 数据目录和 binlog、relaylog、undolog、errorlog、slowlog 日志空间 | MB      | InstanceId、InstanceType |
| BytesSent                    | 内网出流量                               | 内网每秒出流量                                               | Byte/秒 | InstanceId、InstanceType |
| BytesReceived                | 内网入流量                               |      内网每秒入流量                                          | Byte/秒 | InstanceId、InstanceType |
| QPS                          | 每秒执行操作数                           | 数据库每秒执行的 SQL 数（含 insert、select、update、delete、replace），QPS 指标主要体现 TencentDB 实例的实际处理能力 | 次/秒   | InstanceId、InstanceType |
| TPS                          | 每秒执行事务数                           | 数据库每秒执行的事务数                                       | 次/秒   | InstanceId、InstanceType |
| MaxConnections               | 最大连接数                               | 数据库最大连接数                                             | 个      | InstanceId、InstanceType |
| ThreadsConnected             | 当前打开连接数                           | 当前打开连接数                                               | 个      | InstanceId、InstanceType |
| ConnectionUseRate            | 连接数利用率                             | 当前打开连接数/最大连接数                                    | %       | InstanceId、InstanceType |
| SlowQueries                  | 慢查询数                                 | 查询时间超过 long_query_time 秒的查询的个数                  | 次/分   | InstanceId、InstanceType |
| SelectScan                   | 全表扫描数                               | 执行全表搜索查询的数量                                       | 次/秒   | InstanceId、InstanceType |
| SelectCount                  | 查询数                                   | 每秒查询数                                                   | 次/秒   | InstanceId、InstanceType |
| ComUpdate                    | 更新数                                   | 每秒更新数                                                   | 次/秒   | InstanceId、InstanceType |
| ComDelete                    | 删除数                                   | 每秒删除数                                                   | 次/秒   | InstanceId、InstanceType |
| ComInsert                    | 插入数                                   | 每秒插入数                                                   | 次/秒   | InstanceId、InstanceType |
| ComReplace                   | 覆盖数                                   | 每秒覆盖数                                                   | 次/秒   | InstanceId、InstanceType |
| Queries                      | 总请求数                                 | 所有执行的 SQL 语句，包括 set，show 等                       | 次/秒   | InstanceId、InstanceType |
| QueryRate                    | 查询使用率                               | 每秒执行操作数 QPS/推荐每秒操作数                            | %       | InstanceId、InstanceType |
| CreatedTmpTables             | 临时表数量                               | 创建临时表的数量                                             | 次/秒   | InstanceId、InstanceType |
| TableLocksWaited             | 等待表锁次数                             | 不能立即获得的表的锁的次数                                   | 次/秒   | InstanceId、InstanceType |
| InnodbCacheUseRate           | innodb 缓存使用率                         | Innodb 引擎的缓存使用率                                      | %       | InstanceId、InstanceType |
| InnodbCacheHitRate           | innodb 缓存命中率                         | Innodb 引擎的缓存命中率                                      | %       | InstanceId、InstanceType |
| InnodbOsFileReads            | innodb 读磁盘数量                         | Innodb 引擎每秒读磁盘文件的次数                              | 次/秒   | InstanceId、InstanceType |
| InnodbOsFileWrites           | innodb 写磁盘数量                         | Innodb 引擎每秒写磁盘文件的次数                              | 次/秒   | InstanceId、InstanceType |
| InnodbOsFsyncs               | innodb fsync 数量                         | Innodb 引擎每秒调用 fsync 函数次数                           | 次/秒   | InstanceId、InstanceType |
| InnodbNumOpenFiles           | 当前 InnoDB 打开表的数量                   | Innodb 引擎当前打开表的数量                                  | 个      | InstanceId、InstanceType |
| KeyCacheUseRate              | myisam 缓存使用率                         | myisam 引擎的缓存命中率                                      | %       | InstanceId、InstanceType |
| KeyCacheHitRate              | myisam 缓存命中率                         | myisam 引擎的缓存使用率                                      | %       | InstanceId、InstanceType |
| ComCommit                    | 提交数                                   | 每秒提交次数                                                 | 次/秒   | InstanceId、InstanceType |
| ComRollback                  | 回滚数                                   | 每秒回滚次数                                                 | 次/秒   | InstanceId、InstanceType |
| ThreadsCreated               | 已创建的线程数                           | 创建用来处理连接的线程数                                     | 个      | InstanceId、InstanceType |
| ThreadsRunning               | 运行的线程数                             | 激活的（非睡眠状态）线程数                                   | 个      | InstanceId、InstanceType |
| CreatedTmpDiskTables         | 磁盘临时表数量                           | 每秒创建磁盘临时表的次数                                     | 次/秒   | InstanceId、InstanceType |
| CreatedTmpFiles              | 临时文件数量                             | 每秒创建临时文件的次数                                       | 次/秒   | InstanceId、InstanceType |
| HandlerReadRndNext           | 读下一行请求数                           | 每秒读取下一行的请求次数                                     | 次/秒   | InstanceId、InstanceType |
| HandlerRollback              | 内部回滚数                               | 每秒事务被回滚的次数                                         | 次/秒   | InstanceId、InstanceType |
| HandlerCommit                | 内部提交数                               | 每秒事务提交的次数                                           | 次/秒   | InstanceId、InstanceType |
| InnodbBufferPoolPagesFree    | InnoDB 空页数                             | Innodb 引擎内存空页个数                                      | 个      | InstanceId、InstanceType |
| InnodbBufferPoolPagesTotal   | InnoDB 总页数                             | Innodb 引擎占用内存总页数                                    | 个      | InstanceId、InstanceType |
| InnodbBufferPoolReadRequests | InnoDB 逻辑读                             | Innodb 引擎每秒已经完成的逻辑读请求次数                      | 次/秒   | InstanceId、InstanceType |
| InnodbBufferPoolReads        | InnoDB 物理读                             | Innodb 引擎每秒已经完成的物理读请求次数                      | 次/秒   | InstanceId、InstanceType |
| InnodbDataReads              | InnoDB 总读取量                           | Innodb 引擎每秒已经完成读取数据的字节数                      | 次/秒   | InstanceId、InstanceType |
| InnodbDataRead               | InnoDB 读取量                             | Innodb 引擎每秒已经完成读取数据的次数                        | Byte/秒 | InstanceId、InstanceType |
| InnodbDataWrites             | InnoDB 总写入量                           | Innodb 引擎每秒已经完成写数据的次数                          | 次/秒   | InstanceId、InstanceType |
| InnodbDataWritten            | InnoDB 写入量                             | Innodb 引擎每秒已经完成写数据的字节数                        | Byte/秒 | InstanceId、InstanceType |
| InnodbRowsDeleted            | InnoDB 行删除量                           | Innodb 引擎每秒删除的行数                                    | 次/秒   | InstanceId、InstanceType |
| InnodbRowsInserted           | InnoDB 行插入量                           | Innodb 引擎每秒插入的行数                                    | 次/秒   | InstanceId、InstanceType |
| InnodbRowsUpdated            | InnoDB 行更新量                           | Innodb 引擎每秒更新的行数                                    | 次/秒   | InstanceId、InstanceType |
| InnodbRowsRead               | InnoDB 行读取量                           | Innodb 引擎每秒读取的行数                                    | 次/秒   | InstanceId、InstanceType |
| InnodbRowLockTimeAvg         | InnoDB 平均获取行锁时间                   | Innodb 引擎行锁定的平均时长                                  | 毫秒    | InstanceId、InstanceType |
| InnodbRowLockWaits           | InnoDB 等待行锁次数                       | Innodb 引擎每秒等待行锁定的次数                              | 次/秒   | InstanceId、InstanceType |
| KeyBlocksUnused              | 键缓存内未使用的块数量                   | myisam 引擎未使用键缓存块的个数                              | 个      | InstanceId、InstanceType |
| KeyBlocksUsed                | 键缓存内使用的块数量                     | myisam 引擎已使用键缓存块的个数                              | 个      | InstanceId、InstanceType |
| KeyReadRequests              | 键缓存读取数据块次数                     | myisam 引擎每秒读取键缓存块的次数                            | 次/秒   | InstanceId、InstanceType |
| KeyReads                     | 硬盘读取数据块次数                       | myisam 引擎每秒读取硬盘数据块的次数                          | 次/秒   | InstanceId、InstanceType |
| KeyWriteRequests             | 数据块写入键缓冲次数                     | myisam 引擎每秒写键缓存块的次数                              | 次/秒   | InstanceId、InstanceType |
| KeyWrites                    | 数据块写入磁盘次数                       | myisam 引擎每秒写硬盘数据块的次数                            | 次/秒   | InstanceId、InstanceType |
| OpenedTables                 | 已经打开的表数                           | 当前数据库已经打开的表数                                     | 个      | InstanceId、InstanceType |
| TableLocksImmediate          | 立即释放的表锁数                         | 立即释放的表锁个数                                           | 个      | InstanceId、InstanceType |
| OpenFiles                    | 打开文件总数                             | 当前数据库打开文件总数                                       | 个      | InstanceId、InstanceType |
| LogCapacity                  | 日志使用量                               | 当前数据库日志使用量                                         | MB      | InstanceId、InstanceType |
| SlaveIoRunning               | IO 线程状态                               | Slave 下 IO 线程状态                                          | —       | InstanceId、InstanceType |
| SlaveSqlRunning              | SQL 线程状态                              | Slave 下 SQL 线程状态                                         | —       | InstanceId、InstanceType |
| MasterSlaveSyncDistance      | 主从延迟距离                             | 主从 binlog 差距                                             | MB      | InstanceId、InstanceType |
| SecondsBehindMaster          | 主从延迟时间                             | 主从延迟时间                                                 | MB      | InstanceId、InstanceType |

>?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称     | 维度解释                                                     | 格式                                     |
| ------------------------------ | ------------ | ------------------------------------------------------------ | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId   | 数据库的实例 ID 名称                                          | 输入 String 类型维度名称，例如：topicId      |
| Instances.N.Dimensions.0.Value | InstanceId   | 数据库的具体ID                                               | 输入具体实例 ID，例如：topic-i4p4k0u0      |
| Instances.N.Dimensions.1.Name  | InstanceType | 数据库实例类型                                               | 输入 String 类型维度名称，例如：InstanceType |
  | Instances.N.Dimensions.1.Value | InstanceType | 数据库实例类型，默认取值为1，详细取值如下：<br><li>取值为1：表示拉取实例主机的监控数据<br><li>取值为2：表示拉取实例从机的监控数据<br><li>取值为3：表示拉取只读实例的监控数据<br><li>取值为4：表示拉取实例第二从机（仅金融版实例有第二从机）的监控数据 | 输入实例类型，默认取值为1                |
	
	
	
## 入参说明

查询云数据库（MySQL）产品监控数据，入参取值如下：
&Namespace=QCE/CDB
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=数据库的具体 ID 
