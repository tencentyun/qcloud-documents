## 命名空间

Namespace=QCE/CDB

## 监控指标

### 资源监控

| 指标英文名    | 指标中文名   | 指标说明                                                     | 单位  | 维度                     | 统计粒度                     |
| ------------- | ------------ | ------------------------------------------------------------ | ----- | ------------------------ | ---------------------------- |
| BytesReceived | 内网入流量   | 每秒接收的字节数                                             | 字节/秒  | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| BytesSent     | 内网出流量   | 每秒发送的字节数                                             | 字节/秒   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| Capacity      | 磁盘占用空间 | 包括 MySQL 数据目录和  binlog、relaylog、undolog、errorlog、slowlog 日志空间 | MB    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| CpuUseRate    | CPU 利用率   | 允许闲时超用，CPU 利用率可能大于100%                         | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| IOPS          | IOPS         | 每秒的输入输出量(或读写次数)                                 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| MemoryUse     | 内存占用     | 允许闲时超用，实际内存占用可能大于购买规格                   | MB     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| MemoryUseRate | 内存利用率   | 允许闲时超用，内存利用率可能大于100%                         | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| RealCapacity  | 磁盘使用空间 | 仅包括 MySQL 数据目录，不含  binlog、relaylog、undolog、errorlog、slowlog 日志空间 | MB    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| VolumeRate    | 磁盘利用率   | 磁盘使用空间/实例购买空间                                    | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（普通）- MyISAM

| 指标英文名      | 指标中文名        | 指标说明                | 单位 | 维度                             | 统计粒度                     |
| --------------- | ----------------- | ----------------------- | ---- | -------------------------------- | ---------------------------- |
| KeyCacheHitRate | myisam 缓存命中率 | myisam 引擎的缓存命中率 | %    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyCacheUseRate | myisam 缓存使用率 | myisam 引擎的缓存使用率 | %    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（普通）- InnoDB

| 指标英文名         | 指标中文名                            | 指标说明                           | 单位  | 维度                             | 统计粒度                     |
| ------------------ | ------------------------------------- | ---------------------------------- | ----- | -------------------------------- | ---------------------------- |
| InnodbCacheHitRate | innodb 缓存命中率                     | Innodb 引擎的缓存命中率            | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbCacheUseRate | innodb 缓存使用率                     | Innodb 引擎的缓存使用率            | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbNumOpenFiles | InnoDB 总页数当前 InnoDB 打开表的数量 | Innodb 引擎当前打开表的数量        | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s         |
| InnodbOsFileReads  | innodb 读磁盘数量                     | Innodb 引擎每秒读磁盘文件的次数    | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbOsFileWrites | innodb 写磁盘数量                     | Innodb 引擎每秒写磁盘文件的次数    | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbOsFsyncs     | innodbfsync 数量                      | Innodb 引擎每秒调用 fsync 函数次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（普通）- 连接

| 指标英文名        | 指标中文名     | 指标说明                                                     | 单位  | 维度                             | 统计粒度                     |
| ----------------- | -------------- | ------------------------------------------------------------ | ----- | -------------------------------- | ---------------------------- |
| ConnectionUseRate | 连接数利用率   | 当前打开连接数/最大连接数                                    | %     | InstanceId、InstanceType（选填） | 5s、10s、60s、300s、3600s    |
| MaxConnections    | 最大连接数     | 最大连接数                                                   | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| Qps               | 每秒执行操作数 | 数据库每秒执行的 SQL 数（含  insert、select、update、delete、replace），QPS 指标主要体现 TencentDB 实例的实际处理能力 | 次/秒 | InsanceId、InstanceType（选填）  | 5s、60s、300s、3600s、86400s |
| ThreadsConnected  | 当前连接数     | 当前打开的连接的数量                                         | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| Tps               | 每秒执行事务数 | 数据库每秒传输的事务处理个数                                 | 个/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（普通）- 访问

| 指标英文名  | 指标中文名 | 指标说明                                    | 单位  | 维度                             | 统计粒度                     |
| ----------- | ---------- | ------------------------------------------- | ----- | -------------------------------- | ---------------------------- |
| ComDelete   | 删除数     | 每秒删除数                                  | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| ComInsert   | 插入数     | 每秒插入数                                  | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| ComReplace  | 覆盖数     | 每秒覆盖数                                  | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| ComUpdate   | 更新数     | 每秒更新数                                  | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| Queries     | 总访问量   | 所有执行的 SQL 语句，包括 set，show 等      | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| QueryRate   | 访问量占比 | 每秒执行操作数 QPS/推荐每秒操作数           | %     | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SelectCount | 查询数     | 每秒查询数                                  | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SelectScan  | 全表扫描数 | 执行全表搜索查询的数量                      | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SlowQueries | 慢查询数   | 查询时间超过 long_query_time 秒的查询的个数 | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（普通）- 表

| 指标英文名       | 指标中文名     | 指标说明                   | 单位  | 维度                             | 统计粒度                     |
| ---------------- | -------------- | -------------------------- | ----- | -------------------------------- | ---------------------------- |
| CreatedTmpTables | 内存临时表数量 | 创建临时表的数量           | 个/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| TableLocksWaited | 等待表锁次数   | 不能立即获得的表的锁的次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- Tmp

| 指标英文名           | 指标中文名     | 指标说明                 | 单位  | 维度                             | 统计粒度                     |
| -------------------- | -------------- | ------------------------ | ----- | -------------------------------- | ---------------------------- |
| CreatedTmpDiskTables | 磁盘临时表数量 | 每秒创建磁盘临时表的次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| CreatedTmpFiles     | 临时文件数量   | 每秒创建临时文件的次数   | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- Key

| 指标英文名       | 指标中文名             | 指标说明                            | 单位  | 维度                             | 统计粒度                     |
| ---------------- | ---------------------- | ----------------------------------- | ----- | -------------------------------- | ---------------------------- |
| KeyBlocksUnused  | 键缓存内未使用的块数量 | myisam 引擎未使用键缓存块的个数     | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyBlocksUsed    | 键缓存内使用的块数量   | myisam 引擎已使用键缓存块的个数     | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyReadRequests  | 键缓存读取数据块次数   | myisam 引擎每秒读取键缓存块的次数   | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyReads         | 硬盘读取数据块次数     | myisam 引擎每秒读取硬盘数据块的次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyWriteRequests | 数据块写入键缓冲次数   | myisam 引擎每秒写键缓存块的次数     | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| KeyWrites        | 数据块写入磁盘次数     | myisam 引擎每秒写硬盘数据块的次数   | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- InnoDB Row

| 指标英文名           | 指标中文名                      | 指标说明                        | 单位  | 维度                     | 统计粒度                     |
| -------------------- | ------------------------------- | ------------------------------- | ----- | ------------------------ | ---------------------------- |
| InnodbRowLockTimeAvg | InnoDB 平均获取行锁时间（毫秒） | Innodb 引擎行锁定的平均时长     | ms    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbRowLockWaits   | InnoDB 等待行锁次数             | Innodb 引擎每秒等待行锁定的次数 | 次/秒    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbRowsDeleted    | InnoDB 行删除量                 | Innodb 引擎每秒删除的行数       | 行/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbRowsInserted   | InnoDB 行插入量                 | Innodb 引擎每秒插入的行数       | 行/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbRowsRead       | InnoDB 行读取量                 | Innodb 引擎每秒读取的行数       | 行/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbRowsUpdated    | InnoDB 行更新量                 | Innodb 引擎每秒更新的行数       | 行/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- InnoDB Data

| 指标英文名        | 指标中文名      | 指标说明                                | 单位    | 维度                             | 统计粒度                     |
| ----------------- | --------------- | --------------------------------------- | ------- | -------------------------------- | ---------------------------- |
| InnodbDataRead    | InnoDB 读取量   | Innodb 引擎每秒已经完成读取数据的字节数 | 字节/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbDataReads   | InnoDB 总读取量 | Innodb 引擎每秒已经完成读取数据的次数   | 次/秒   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbDataWrites  | InnoDB 总写入量 | Innodb 引擎每秒已经完成写数据的次数     | 次/秒   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbDataWritten | InnoDB 写入量   | Innodb 引擎每秒已经完成写数据的字节数   | 字节/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- Handler

| 指标英文名         | 指标中文名     | 指标说明                 | 单位  | 维度                             | 统计粒度                     |
| ------------------ | -------------- | ------------------------ | ----- | -------------------------------- | ---------------------------- |
| HandlerCommit      | 内部提交数     | 每秒事务提交的次数       | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| HandlerReadRndNext | 读下一行请求数 | 每秒读取下一行的请求次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| HandlerRollback    | 内部回滚数     | 每秒事务被回滚的次数     | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- Buff

| 指标英文名                   | 指标中文名              | 指标说明                                | 单位  | 维度                             | 统计粒度                     |
| ---------------------------- | ----------------------- | --------------------------------------- | ----- | -------------------------------- | ---------------------------- |
| InnodbBufferPoolPagesFree    | InnoDB 空页数           | Innodb 引擎内存空页个数                 | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s         |
| InnodbBufferPoolPagesTotal   | InnoDB 总页数           | Innodb 引擎占用内存总页数               | 个    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbBufferPoolReadRequests | innodb 缓冲池预读页次数 | Innodb 引擎每秒已经完成的逻辑读请求次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| InnodbBufferPoolReads        | innodb 磁盘读页次数     | Innodb 引擎每秒已经完成的物理读请求次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- 其他

| 指标英文名  | 指标中文名 | 指标说明             | 单位  | 维度                             | 统计粒度                     |
| ----------- | ---------- | -------------------- | ----- | -------------------------------- | ---------------------------- |
| LogCapacity | 日志使用量 | 引擎使用日志的数量   | MB    | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s         |
| OpenFiles   | 打开文件数 | 引擎打开的文件的数量 | 个/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- 连接

| 指标英文名     | 指标中文名     | 指标说明                   | 单位 | 维度                             | 统计粒度                     |
| -------------- | -------------- | -------------------------- | ---- | -------------------------------- | ---------------------------- |
| ThreadsCreated | 已创建的线程数 | 创建用来处理连接的线程数   | 个   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| ThreadsRunning | 运行的线程数   | 激活的（非睡眠状态）线程数 | 个   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- 访问

| 指标英文名  | 指标中文名 | 指标说明     | 单位  | 维度                             | 统计粒度                     |
| ----------- | ---------- | ------------ | ----- | -------------------------------- | ---------------------------- |
| ComCommit   | 提交数     | 每秒提交次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| ComRollback | 回滚数     | 每秒回滚次数 | 次/秒 | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 引擎监控（扩展）- 表

| 指标英文名          | 指标中文名       | 指标说明               | 单位 | 维度                             | 统计粒度                     |
| ------------------- | ---------------- | ---------------------- | ---- | -------------------------------- | ---------------------------- |
| OpenedTables        | 已经打开的表数   | 引擎已经打开的表的数量 | 个   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| TableLocksImmediate | 立即释放的表锁数 | 引擎立即释放的表锁数   | 个   | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

### 部署监控（备机）

| 指标英文名              | 指标中文名   | 指标说明         | 单位                                | 维度                             | 统计粒度                     |
| ----------------------- | ------------ | ---------------- | ----------------------------------- | -------------------------------- | ---------------------------- |
| MasterSlaveSyncDistance | 主从延迟距离 | 主从 binlog 差距 | MB                                  | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SecondsBehindMaster     | 主从延迟时间 | 主从延迟时间     | 秒                                  | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SlaveIoRunning          | IO 线程状态  | IO 线程运行状态  | 状态值（0-Yes，1-No，2-Connecting） | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |
| SlaveSqlRunning         | SQL 线程状态 | SQL 线程运行状态 | 状态值（0-Yes，1-No）               | InstanceId、InstanceType（选填） | 5s、60s、300s、3600s、86400s |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称             | 维度解释                                                     | 格式                                         |
| ------------------------------ | -------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId           | 数据库的实例 ID 名称                                         | 输入 String 类型维度名称，例如：InstanceId   |
| Instances.N.Dimensions.0.Value | InstanceId           | 数据库的具体 ID                                              | 输入具体实例 ID，例如：cdb-ebul6659          |
| Instances.N.Dimensions.1.Name  | InstanceType（选填） | 数据库实例类型                                               | 输入 String 类型维度名称，例如：InstanceType |
| Instances.N.Dimensions.1.Value | InstanceType（选填） | 数据库实例类型，默认取值为1，详细取值如下：<br><li>取值为1：表示拉取实例主机的监控数据<br><li>取值为2：表示拉取实例从机的监控数据（仅支持单节点和双节点）<br><li>取值为3：表示拉取只读实例的监控数据（InstanceId 需入参为只读实例 ID，否则仍默认取值为1）<br><li>取值为4：表示拉取实例第二从机（仅金融版实例有第二从机）的监控数据 | 输入实例类型，可不入参，默认取值为1          |

> ? InstanceType 说明：
>
> - 假设 InstanceId 入参值为主实例的ID，仅 InstanceType 支持拉取主机（取值为1）、从机（取值为2）、只读实例（取值为3）、第二从机（取值为4）的监控数据。
> - 假设 InstanceId 入参值为主实例的ID，InstanceType入参为 2 （从机），且该主实例是三节点（一主两从）。由于拉取从机监控数据仅支持单节点和双节点，会导致缺少一个监控节点数据。
> - 若需要拉取只读实例监控数据，InstanceId 需入参为只读实例 ID。



## 入参说明

**查询云数据库（MySQL）产品监控数据，入参说明如下：**

&Namespace=QCE/CDB
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=数据库的具体 ID 
&Instances.N.Dimensions.1.Name=InstanceType
&Instances.N.Dimensions.1.Value=数据库实例类型
