## 命名空间

Namespace = QCE/POSTGRES

## 监控指标


| 指标英文名      | 指标中文名                 | 单位  | 指标描述                                                     | 维度       | 统计粒度      |
| --------------- | :------------------------- | :---- | :----------------------------------------------------------- | ---------- | ------------- |
| Cpu             | CPU 利用率                 | %     | CPU 实际利用率                                               | resourceId | 5s、60s、300s |
| Storage         | 已用存储空间               | GB    | 整实例空间占用大小                                           | resourceId | 5s、60s、300s |
| DataFileSize    | 数据文件大小               | GB    | 数据文件占用空间大小                                         | resourceId | 5s、60s、300s |
| LogFileSize     | 日志文件大小               | GB    | wal 日志文件占用空间大小                                     | resourceId | 5s、60s、300s |
| TempFileSize    | 临时文件大小               | MB    | 临时文件的大小                                               | resourceId | 5s、60s、300s |
| StorageRate     | 存储空间使用率             | %     | 总的存储空间使用率，包括临时文件、数据文件、日志文件以及其他类型的数据库文件 | resourceId | 5s、60s、300s |
| Qps             | 每秒查询数                 | 次/秒 | 平均每秒执行的 SQL 语句数量                                  | resourceId | 5s、60s、300s |
| Connections     | 连接数                     | 个    | 对数据库发起采集时，数据库当前总连接数                       | resourceId | 5s、60s、300s |
| NewConnIn5s     | 5秒内新建连接数            | 次    | 对数据库发起采集时，查询出关于最近5秒内建立的所有连接数      | resourceId | 5s、60s、300s |
| ActiveConns     | 活跃连接数                 | 个    | 对数据库发起采集时，数据库瞬时活跃连接（非 idle 连接）       | resourceId | 5s、60s、300s |
| IdleConns       | 空闲连接数                 | 个    | 对数据库发起采集时，查询出来的数据库瞬时空闲连接（idle 连接） | resourceId | 5s、60s、300s |
| Waiting         | 等待会话数                 | 个    | 对数据库发起采集时，数据库正在等待的会话数量（状态为 waiting） | resourceId | 5s、60s、300s |
| LongWaiting     | 等待超过5秒的会话数        | 个    | 一个采集周期内，数据库等待超过5秒的会话数量（状态为 waiting，且等待状态维持了5秒） | resourceId | 5s、60s、300s |
| IdleInXact      | 空闲事务数                 | 个    | 对数据库发起采集时，数据库正在处于 idle 状态的事务数量       | resourceId | 5s、60s、300s |
| LongXact        | 执行时长超过1秒的事务数目  | 个    | 一个采集周期内，执行时间超过1秒的事务数量                    | resourceId | 5s、60s、300s |
| LongIdleInXact  | 超过5秒的空闲事务数        | 个    | 一个采集周期内，空闲时间超过5秒的事务数量                    | resourceId | 5s、60s、300s |
| Tps             | 每秒事务数                 | 次/秒 | 平均每秒执行成功的事务数（包括回滚和提交）                   | resourceId | 5s、60s、300s |
| XactCommit      | 事务提交数                 | 次/秒 | 平均每秒提交的事务数                                         | resourceId | 5s、60s、300s |
| XactRollback    | 事务回滚数                 | 次/秒 | 平均每秒回滚的事务数                                         | resourceId | 5s、60s、300s |
| ReadWriteCalls  | 请求数                     | 次    | 一个统计周期内的总请求数                                     | resourceId | 5s、60s、300s |
| ReadCalls       | 读请求数                   | 次    | 一个统计周期内的读请求数                                     | resourceId | 5s、60s、300s |
| WriteCalls      | 写请求数                   | 次    | 一个统计周期内的写请求数                                     | resourceId | 5s、60s、300s |
| OtherCalls      | 其他请求数                 | 次    | 一个统计周期内的其他请求数（begin、create、非 DML、DDL、DQL 操作） | resourceId | 5s、60s、300s |
| HitPercent      | 缓冲区缓存命中率           | %     | 一个请求周期内的所有 SQL 语句执行的命中率                    | resourceId | 5s、60s、300s |
| SqlRuntimeAvg   | 平均执行时延               | ms    | 一次统计周期内所有 SQL 语句的平均执行时延                    | resourceId | 5s、60s、300s |
| SqlRuntimeMax   | 最长 TOP10 执行时延        | ms    | 一次统计周期内最长 TOP10 的 SQL 平均执行时延                 | resourceId | 5s、60s、300s |
| SqlRuntimeMin   | 最短 TOP10 执行时延        | ms    | 一次统计周期内最短 TOP10 的 SQL 平均执行时延                 | resourceId | 5s、60s、300s |
| RemainXid       | 剩余 XID 数量              | 个    | 对数据库发起采集时，显示当前剩余 xid 最少的库的剩余 xid 数量。只读实例无此指标 | resourceId | 5s、60s、300s |
| XlogDiff        | 备库日志发送与回放位置差异 | byte  | 日志从主库发送至备库与备库回放完成之间的大小差异，主要反映了备库日志应用的速度，主要能够通过此指标查看出备库的性能、网络传输的速度。只读实例无此指标 | resourceId | 5s、60s、300s |
| XlogDiffTime    | 备库日志落盘时间延迟       | byte  | 日志从主库发送至备库与备库接收到日志并落盘之间的时间差异。只读实例无此指标，且实例版本在 10.x 以上版本才有此指标 | resourceId | 5s、60s、300s |
| SlaveApplyDelay | 主备数据同步延迟           | s     | 主备数据同步延迟,对于主实例而言，此指标可以体现出故障切换的 RTO。反映到只读实例在多少时间后能够查询到在主库进行写入的数据. 只读实例指标名为：与主实例数据同步延迟 | resourceId | 5s、60s、300s |
| SlowQueryCnt    | 慢查询数量                 | 个    | 一个采集周期内，出现的慢查询个数                             | resourceId | 5s、60s、300s |
| LongQuery       | 执行时长超过1秒的 SQL 数   | 个    | 对数据库发起采集时，查询出来 执行时间超过1s的 SQL 数量       | resourceId | 5s、60s、300s |
| 2pc             | 2pc事务数                  | 个    | 对数据库发起采集时，当前的 2PC 事务数量                        | resourceId | 5s、60s、300s |
| Long2pc         | 超过5s未提交的 2PC 事务数    | 个    | 对数据库发起采集时，当前执行时间超过5s的 2PC 事务数量        | resourceId | 5s、60s、300s |
| TupDeleted      | 每秒删除记录数             | 个    | 平均每秒删除的 tupe 数量。只读实例无此指标                   | resourceId | 5s、60s、300s |
| TupInserted     | 每秒插入记录数             | 个    | 平均每秒插入的 tupe 数量。只读实例无此指标                   | resourceId | 5s、60s、300s |
| TupUpdated      | 每秒更新记录数             | 个    | 平均每秒更新的 tupe 数量。只读实例无此指标                   | resourceId | 5s、60s、300s |
| TupFetched      | 每秒索引扫描回表记录数     | 个    | 平均每秒通过索引扫描的 tupe 数量                             | resourceId | 5s、60s、300s |
| TupReturned     | 每秒全表扫描记录数         | 个    | 平均每秒全表扫描的 tupe 数量                                 | resourceId | 5s、60s、300s |
| Deadlocks       | 死锁数                     | 个    | 在一个采集周期内的所有死锁数                                 | resourceId | 5s、60s、300s |
| Memory    | 内存占用量    | MB   | 内存已使用量                          | resourceId | 5s、60s、300s |
| MemoryRate    | 内存使用率                 | %    | 内存已使用量占用总量的百分比                             | resourceId | 5s、60s、300s |


> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | resourceId              | resourceId 维度名称   | 输入 String 类型维度名称：resourceId         |
| Instances.N.Dimensions.0.Value | resourceId              | 实例具体的 resourceId       | 输入实例的具体 resourceId，例如：postgres-123456       |


## 入参说明

查询 PostgreSQL 监控数据，入参取值如下：
&Namespace=QCE/POSTGRES
&Instances.N.Dimensions.0.Name=resourceId
&Instances.N.Dimensions.0.Value 为实例的 resourceId 
