云数据仓库 ClickHouse 支持通过ClickHouse-Copler 实现集群迁移。

## 通过 ClickHouse-Shipper 实现集群迁移
ClickHouse-Shipper，CDWCH 团队开发的集群迁移工具，主要基于 Part 迁移的能力和方式实现集群的迁移。 
### 理论基础
```
ALTER TABLE table_name FETCH PARTITION|PART partition_expr FROM 'path-in-zookeeper 
```
ClickHouse 支持类似 ReplicatedMergeTree 进行副本间同步的方式，执行一个 SQL，去 zookeeper 路径下获取 partition 或 part 数据，然后同步到本地节点，attach 到表上，实现数据的拷⻉，最终实现数据的迁移。 
例如：
1. FETCH PARTITION                                                          
```
ALTER TABLE users FETCH PARTITION 201902 FROM 'zk_clusterName:/clickhouse/tables/01-01/visits'; ALTER TABLE users ATTACH PARTITION 201902;                  
```
2. FETCH PART
```
ALTER TABLE users FETCH PART '201901_2_2_0' FROM '/clickhouse/tables/01-01/visits';
ALTER TABLE users ATTACH PART '201901_2_2_0';               
```
    
>! 
>- 明显该功能依赖复制表，如果用户有非复制表的MergeTree，数据无法基于该功能拷⻉数据。 
>- 该功能只在21.4以上内核版本支持。 

### Shipper 实现与使用 
目前 Shipper 已经基于以上 ClickHouse 的能力实现了第一个版本的数据迁移功能，支持 ReplicatedMergeTree 类型的表引擎的数据迁移。 
通过配置源端和目标端的 zookeeper 和 cluster 信息，去获取源端可以迁移的 ReplicatedMergeTree 的所有表，以及表包含的所有 part，然后根据一定的 hash 规则，构造一个 part 迁移任务列表，将 part 分配给目标集群的 shard，然 后通过按表、按 part 的循环，去目标集群下发上一节中的 SQL 请求，让目标集群去源集群下载数据、然后 attach 数据，最终完成数据按 part 粒度的迁移。 

Shipper 基本的使用方法如下：
1. 根据业务情况，分析是否需要调整源端的配置参数、执行重启;或者升级目标端内核版本到21.8; 
2. 配置任务配置文件，包括在目标端配置上源端的zookeeper信息，目标端的执行的参数;
3. 执行 shipper 命令，如：
```
./clickhouse-shipper  move_ck_data create_process --srcip src-ck-1-1  --targetip dst-ck-1-1  --port 9000 --clustername  default_cluster   --database_cdn  XXXX    -- table_cdn XXXX --partition_cdn  XXXX           
```

### 使用 Shipper 的优点 
1. 本质问题：给予 part 目录进行迁移，迁移效率高。 
2. 集群负载：相对较小，大部分在内存消耗。
3. 性能：相对优异。
4. 并发：并发好控制。 
5. 代价：基本没有多余的开销。
6. 迭代：基于 Cluster、Database、Table、Shard、Partition 不通维度的迁移都是可以快速迭代和设计的。
7. 迁移：后期可以做增量迁移。
8. 集成：目前 GO 语言实现，方便与管控代码集成。 

### 使用 Shipper 的注意事项
1. 由于迁移计划，即 part 迁移任务列表是在任务一开始就构造好的，如果后续在迁移的过程中，任务列表中的 part 发生了改变，例如 merge、mutation，可能会导致任务列表中的 part 信息已经不存在了，迁移会报错失败，目前没能完美解决该类问题。需要手动调整源端集群的参数的方式去限制 part 的 merge。这会涉及到源集群的参数调整和重启。               
2. 另外不支持增加 insert 数据的迁移，即迁移任务列表不能更新新增的 part，这就要求用户如果想完整的迁移， 需要迁移开始前就完成业务的只读调整，停止数据的写入。 
3. 由于基于 part 的迁移，不支持类似 hash 规则的分片逻辑。如果用户源端和目标端的集群 shard 个数不一样多， 想保持具有类似 hash 规则数据分布的业务逻辑，几乎做不到。另外 FETCH PARTITION 需要明确 zk 的表路径， 目前 shipper 的实现教简单。 
4. 与第3条类似的原因，很难支持物化视图的迁移。虽然我们可以迁移物化视图对应的存储表，但是很难保持迁 移前物化视图和基础表数据的对应关系（每个 shard 上的物化视图都与该 shard 上的基础表的数据几乎是一一对应的关系，而这种关系的维护在迁移时很难保证）。而物化视图如果不能迁移，就会导致大量基于物化视图 的业务，在迁移后短期是不可用的，需要重新构造物化视图，相当于只迁移基础表的数据，对业务来说只是完 成了迁移的一部分。 
5. 由于 ClickHouse 内核在执行 alter 的 DDL 时，是单线程的，这就导致基于 part 的迁移，目前存在性能的限制， 需要优化内核才能彻底提高整体的迁移性能。这部分代码修改容易，但是这就需要源端进行内核升级才可以。 
6. 不支持非 MergeTree 类表引擎。

## 通过 ClickHouse-Copier 实现集群迁移
### Copier 实现与使用 
ClickHouse-Copier，ClickHouse 官方的数据迁移工具，主要基于分布式表的 insert 方式实现集群的迁移或数据的重分布。 
ClickHouse-Copier 的创建是为了在集群之间移动数据。它运行简单的 INSERT...SELECT 查询，并且可以在具有不 同引擎参数的表之间以及具有不同分片数量的集群之间复制数据。在任务配置文件中，您需要描述源集群和目标集 群的布局，并列出您需要复制的表。您可以复制整个表或特定分区。ClickHouse-Copier 使用临时分布式表从源集 群中选择并插入到目标集群中。 
Copier 通过配置源端和目标端集群的信息，以及迁移表的分布式逻辑，通过在每个 shard 上，每个 partition 构造迁 移任务，将数据基于一定的规则从每个partition 中读取，然后 insert 到目标集群的临时表中，然后基于 attach partition 将数据挂载到最终表中。而且整个任务的执行情况会保存到 zookeeper 中，可以实现任务的重启、短点续传，以及多个 Copier 进程共同执行一个任务。 
Copier 作为官方的迁移工具，也是支持 MergeTree 的表引擎，包括复制表和非复制表。 
![](https://qcloudimg.tencent-cloud.cn/raw/f14491c962f44d448d6af87e380bd11e.png)
                    
### 使用 Copier 的优点
1. ClickHouse 社区官方工具，社区一直在维护和改进，包括功能和性能等。           
2. 虽然基于 select & insert 的逻辑实现，并且每个 copier 进程基本是单线程执行，但是 copier 支持多个进程处理 一个任务。如果每个 shar上都执行一个或多个进程，让每个 copier 都处理本地 shard 数据，会提高整体性能，集群越大，进程数越多，整体性能越好。                              
3. 能够很好的兼容各种分布式表的分片规则，完全基于分布式表的逻辑进行数据的读取和写入，能够根据用户在任务中配置的逻辑，实现迁移时的数据写入逻辑的控制（例如保持原来的逻辑或调整分片规则）。                              
4. 能够兼容迁移前后的集群分片大小，不需要一一对应。 
5. 不受业务的写入和后台 merge 的影响。 
6. 能够在 zookeeper 中记录迁移任务的状态，支持遇错重试，支持短点重试。通过多个进程的逻辑，让迁移的稳定有一定保证。 
7. 不依赖复制表，只要是 MergeTree 类的表都可以支持。 
                            
### 使用 Copier 的注意事项
1. 易用性一般，从社区反馈来说，很多人配置起来较麻烦，较难，官方的资料较少，需要摸索出一套最佳实践。 
2. 单机性能较低，需要较多进程较多 shard 的情况下性能较高，官方也推荐较大集群下性能较好。 
3. 物化视图的迁移不能做到一步到位，很难保证基础表和物化视图的逻辑关系的保持，需要根据表的特点精心设置迁移方案，降低迁移整体流程的时⻓，才能让业务尽可能低的受到迁移的影响。                             
4. 不支持增量迁移，虽然在迁移的过程中支持业务的写入和 merge 等操作，但是同样不能支持增量迁移，客观的需要业务停止写入；也不支持 DDL 操作。            
5. 不支持非 MergeTree 类表引擎。 

## 综合对比 
| 序 号   | 参考项 | shipper | copier | 
|---------|---------|---------|---------|
| 1         | 是否需要停业务 | 不完全需要(停止 merge 即可) | 不需要 | 
|2           |是否需要停写，只读 |需要，不支持增量 |需要，不支持增量 |
| 3             | 是否需要升级、重启、调整配置                    | 需要，以停止 merge，需要目标节点是 21.8 | 不需要 | 
| 4  |  是否支持 hash 分片规则 | 需 shard 一对一迁移才支持 | 支持 | 
| 5         | 是否支持扩容或缩容 | 不需要 hash 分片规则时支持 | 支持 | 
| 6     | 是否支持物化视图的迁移 | 需 shard 一对一迁移才支持 | 需验证是否支持 | 
| 7  | 是否支持断点续传 | 不支持 | 支持 | 
| 8                     | 性能|  高 | 中 | 
| 9          |      是否需要必须是复制表 | 需要|  不需要 | 
| 10     | 是否支持 S3 存储|  支持 | 支持 | 

                                            

