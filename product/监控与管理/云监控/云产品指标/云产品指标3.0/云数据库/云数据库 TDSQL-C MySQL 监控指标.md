
## 命名空间

Namespace=QCE/CYNOSDB_MYSQL

## 监控指标
| 指标英文名                   | 指标中文名               | 单位  | 维度       | 统计粒度                     |
| ---------------------------- | ------------------------ | ----- | ---------- | ---------------------------- |
| BytesSent                    | 每秒发送客户端流量           | MB/s  | InstanceId | 5s、60s、300s、3600s、86400s |
| BytesReceived                | 每秒接收客户端流量           | MB/s  | InstanceId | 5s、60s、300s、3600s、86400s |
| ComDelete                    | 删除数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| ComInsert                    | 插入数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| ComUpdate                    | 更新数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| MemoryUse                    | 内存使用量               | MB    | InstanceId | 5s、60s、300s、3600s、86400s |
| ComSelect                    | 查询数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| MaxConnections               | 最大连接数               | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| CreatedTmpTables             | 临时表的数量             | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbCacheHitRate           | InnoDB引擎缓存命中率     | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbCacheUseRate           | InnoDB引擎缓存使用率     | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| SlowQueries                  | 慢查询数                 | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| ThreadsRunning               | 运行的线程数             | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| HandlerRollback              | 内部回滚数               | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| HandlerCommit                | 内部提交数               | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbRowsDeleted            | InnoDB行删除量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbRowsInserted           | InnoDB行插入量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbRowsUpdated            | InnoDB行更新量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbRowsRead               | InnoDB行读取量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| InnodbBufferPoolReadRequests | InnoDB缓冲池写入次数     | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Memoryuserate                | 内存使用率               | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Comreplace                   | 覆盖数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Threadscreated               | 已创建的线程数           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Selectscan                   | 全表扫描数               | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| TmpVolumeUsage               | 临时表空间使用量         | GB    | InstanceId | 5s、60s、300s、3600s、86400s |
| UndoVolumeUsage              | undo表空间使用量         | GB    | InstanceId | 5s、60s、300s、3600s、86400s |
| DataVolumeUsage              | 数据表空间使用量         | GB    | InstanceId | 5s、60s、300s、3600s、86400s |
| Storageuserate               | 存储使用率               | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Storageuse                   | 存储使用量               | GB    | InstanceId | 5s、60s、300s、3600s、86400s |
| Connectionuserate            | 连接数利用率             | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Comrollback                  | 回滚数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Selectfulljoin               | 全表扫描复合查询次数     | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Sortmergepasses              | 排序合并通过次数         | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Qcacheuserate                | Qcache使用率             | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Tablelockswaited             | 等待表锁次数             | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Openedtables                 | 已经打开的表数           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Tablelocksimmediate          | 立即释放的表锁数         | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Tableopencachemisses         | 表打开缓存未命中数       | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbosfilereads            | 读磁盘数量               | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbosfilewrites           | 写磁盘数量               | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbosfsyncs               | InnoDB_fsyncs数          | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbnumopenfiles           | 当前InnoDB打开表的数量   | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdataread               | InnoDB读取量             | B/s   | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdatareads              | InnoDB总读取量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdatawrites             | InnoDB总写入量           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdatawritten            | InnoDB写入量             | B/s   | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbrowlocktimeavg         | InnoDB平均获取行锁时间   | ms    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbrowlockwaits           | InnoDB等待行锁次数       | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodblogwaits               | InnoDB日志等待写入次数   | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodblogwrites              | InnoDB日志物理写入次数   | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodblogwriterequests       | InnoDB日志物理写请求次数 | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Createdtmpdisktables         | 临时表数量               | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Createdtmpfiles              | 临时文件数量             | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Handlerreadrndnext           | 读下一行请求数           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbbufferpoolpagesfree    | InnoDB空页数             | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbbufferpoolpagestotal   | InnoDB总页数             | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbbufferpoolreads        | InnoDB物理读             | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Selectfullrangejoin          | 范围扫描复合查询次数     | 次/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Openfiles                    | 打开文件总数             | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Tableopencachehits           | 表打开缓存命中数         | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Comcommit                    | 提交数                   | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Threadsconnected             | 当前打开连接数           | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Qcachehitrate                | Qcache命中率             | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Cpuuserate                   | CPU使用率                | %     | InstanceId | 5s、60s、300s、3600s、86400s |
| Replicationdelay             | 复制延迟                 | ms    | InstanceId | 5s、60s、300s、3600s、86400s |
| Qps                          | 每秒执行操作数           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Replicationdelaydistance     | 复制落后的lsn距离        | B     | InstanceId | 5s、60s、300s、3600s、86400s |
| Replicationstatus            | 复制状态                 | -     | InstanceId | 5s、60s、300s、3600s、86400s |
| Tps                          | 每秒执行事务数           | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Queries                      | 总请求数                 | 个/秒 | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbbufferpoolpagesdirty   | InnoDB脏页数             | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdatapendingwrites      | InnoDB挂起写入数         | 个    | InstanceId | 5s、60s、300s、3600s、86400s |
| Innodbdatapendingreads       | InnoDB挂起读取数         | 个    | InstanceId | 5s、60s、300s、3600s、86400s |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释                 | 格式                                             |
| :----------------------------- | :--------- | :----------------------- | :----------------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId | 数据库实例 ID 的维度名称 | 输入String 类型维度名称：InstanceId              |
| Instances.N.Dimensions.0.Value | InstanceId | 数据库的实例具体 ID      | 输入具体实例 ID，例如：cynosdbmysql-ins-12ab34cd |

## 入参说明

**查询云数据库（CynosDB for MySQL）产品监控数据，入参取值如下：**

&Namespace=QCE/CYNOSDB_MYSQL
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=CynosDB 数据库中具体实例的 ID




