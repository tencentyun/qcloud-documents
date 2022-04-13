## TXRocks 概述
RocksDB 是⼀个⾮常流⾏的⾼性能持久化 KV（key-value）存储，经过⼤量的适配⼯作，Facebook 的数据库⼯程师将 RocksDB 改造为 MySQL 的⼀个存储引擎 MyRocks。
TXRocks 是腾讯 TXSQL 团队基于 MyRocks 开发的事务型存储引擎。

## 为什么要使用 TXRocks 存储引擎
TXRocks 事务型存储引擎得益于 RocksDB LSM Tree 存储结构，既减少了 InnoDB ⻚⾯半满和碎⽚浪费，⼜可以使⽤紧凑格式存储，因此 TXRocks 在保持与 InnoDB 接近的性能前提下，存储空间相⽐ InnoDB 可以节省⼀半甚⾄更多，更适合对事务读写性能有要求，且数据存储量⼤的业务。

## RocksDB 的 LSM Tree 架构
RocksDB 使⽤ LSM Tree 存储结构，数据组织为⼀组在内存中的 MemTable 和磁盘上若⼲层的 SST ⽂件。
写⼊请求先将新版本记录写⼊ Active MemTable，同时写 WAL ⽇志持久化。写⼊请求写完 MemTable 和 WAL 就可以返回。
当 Active MemTable 写满到⼀定程度，将 Active MemTable 切换为冻结的 Immutable MemTable。后台线程将 Immutable MemTable 刷到硬盘，⽣成对应的 SST ⽂件。SST 按照刷新的次序分层，通常分为L0层 ~ L6层。L1层 ~ L6层，每层内的 SST 中的记录都是有序的，SST ⽂件之间不会有记录范围的交叠。L0为了⽀持尽快将 Immutable MemTable 占⽤的内存空间释放出来，允许 Flush ⽣成的 L0层的 SST 出现记录范围交叠。 
当读取⼀⾏记录时，按照新旧，依次从 Active MemTable、Immutable MemTable、L0、L1 ~ L6各个组件查找这⼀⾏，从任⼀组件找到，就表明找到了最新的版本，可以⽴刻返回。
当执⾏范围扫描时，对包含每层 MemTable 在内的各层数据，分别⽣成⼀个迭代器，这些迭代器归并查找下⼀条记录。从读的流程可以看到，如果 LSM Tree 层数太多，则读性能，尤其是范围扫描的性能会明显下降。所以，为了维持⼀个更好的 LSM Tree 形状，后台会不断地执⾏ compaction 操作，将低层数据合并到⾼层数据，减少层数。
![](https://qcloudimg.tencent-cloud.cn/raw/5f5e47996ea8af096ef4b79efecabe61.png)

## TXRocks 架构
![](https://qcloudimg.tencent-cloud.cn/raw/6eaaa7a50072a6de3f2cecb364e3ac42.png)

## TXRocks 存储引擎的优势
#### 更节省存储空间
相⽐ InnoDB 使⽤的 B+Tree 索引结构，LSM Tree 可以节省相当⽐例的存储空间。
InnoDB 的 B+Tree 分裂通常会导致⻚⾯半满，⻚⾯内空闲、空间浪费，⻚⾯有效利⽤率⽐较低。

TXRocks 的 SST ⽂件⼀般设置为 MB 量级或者更⼤，⽂件要4K对⻬产⽣的浪费⽐例很低，SST 内部虽然也划分为 Block，但 Block 是不需要对⻬的。
另外，TXRocks 的 SST ⽂件采⽤前缀压缩，相同的前缀只会记录⼀份，同时 TXRocks 不同层的 SST 可以采⽤不同的压缩算法，进⼀步降低存储空间开销。 事务 overhead ⽅⾯，InnoDB 的记录上要包含 trx id，roll_ptr 等字段信息，TXRocks 最底层的 SST ⽂件（包含绝⼤部分⽐例的 数据）上，数据不需要存放其他事务开销，例如记录上的版本号在经过⾜够⻓的时间后就可以抹掉。

#### 写放大更低
InnoDB 采⽤ In-Place 的修改⽅式，即使仅修改⼀⾏记录也可能要刷盘⼀整个⻚⾯，导致⽐较⾼的写⼊放⼤和随机写。

TXRocks 采⽤ Append-Only ⽅式，相⽐⽽⾔写⼊放⼤更低。因此 TXRocks 对于擦写次数有限的 SSD 等产品更友好。

## 适用场景
TXRocks ⾮常适合对存储成本⽐较敏感，读多写少但对事务读写性能有要求的，数据存储量⼤的业务场景。

## 如何使用 TXRocks 存储引擎
请参见 [TXRocks 引擎使用须知](https://cloud.tencent.com/document/product/236/71456)。

## 优化和后续发展 
TXRocks 根据业务需求做了部分优化，例如优化 sum 算⼦下推优化，将 sum 查询性能优化了30多倍。同时 TXRocks 也在积极探索与新硬件结合，利⽤ AEP 做⼆级缓存，⼤幅提升性能，提升性价⽐。

TXRocks 作为 MySQL 的存储引擎，后续会针对在业务使⽤中遇到的问题逐渐优化和改进，并计划针对新硬件去做一些新的技术探索，作为 InnoDB 的重要补充，TXRocks 存储引擎会在更多重要业务中上线并平稳运行。
