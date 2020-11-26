## 简介

[云数据库 MySQL](https://cloud.tencent.com/document/product/236)（TencentDB for MySQL）是腾讯云基于开源数据库 MySQL 专业打造的一种高性能分布式数据存储服务，提供了备份恢复、监控、容灾、快速扩容、数据传输等全套解决方案，简化数据库运维工作，让用户专注于业务发展。

云数据库 MySQL 的优势：

- 快速便捷的数据库服务交付能力，在几分钟内部署可扩展的 MySQL，并可按需弹性升降配置
- 真正100%的 MySQL 兼容能力，主流 MySQL 分支完全兼容
- 提供热备、冷备、binlog 三重灾备体系，可用性达到99.95%，可靠性达到99.9996%，确保服务可用，数据不丢失
- 提供一系列数据库管理服务：监控、备份、回档、扩容、性能诊断、数据迁移等
- 实例最高 QPS 可达245509次/秒，极大的简化业务开发，减少业务架构复杂度
- 卓越的高可用，支持多可用区部署，跨城容灾的能力

## 技术架构

### MySQL 架构

MySQL 整体逻辑架构如下图所示，主要分为服务层、存储引擎层和系统文件层，下面我们先做一个简单的分析。
![](https://main.qcloudimg.com/raw/27544b35dea625e086ac63bf2251b7da.png)

#### 网络连接层

客户端连接器：提供与 Mysql 服务器监理连接的支持。各个语言使用各自的 API 技术与 MySQL 建立连接。

#### 服务层

服务层是 MySQL 的核心，主要包含以下六个部分：

| 服务层             | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| 连接器             | 管理缓冲用户连接，线程处理，权限验证等需要缓存的需求         |
| 系统管理和控制工具 | 提供备份恢复、安全管理、集群管理等功能                       |
| SQL 接口           | 接收客户端发送的各种 SQL 命令，并且返回用户需要查询的结果。例如 DML、DDL、存储过程、视图、触发器等，select from 就是调用 SQL Interface |
| 解析器             | 将客户端发送的SQL进行语义和语法的分析，分解成数据结构，生成"解析树"。预处理器根据规则进一步检查“解析树”是否合法，最终生成新的“解析树” |
| 查询优化器         | 当“解析树”通过解析器语法检查后，交由优化器对查询进行优化，将其转换成执行计划，然后与存储引擎交互 |
| 缓存               | 将客户端提交给 MySQL 的 Select 类 query 请求的返回结果集 cache 到内存中，与该 query 的一个 hash 值做一个对应。缓存机制是由一系列小缓存组成，比如表缓存、记录缓存、权限缓存、引擎缓存等 |

#### 存储引擎层

存储引擎负责 MySQL 中数据的存储和提取，与底层系统文件进行交互。MySQL 存储引擎是插件式的，服务器中的查询执行引擎通过接口与存储引擎进行通信，屏蔽了不同引擎之间的差异。

#### 系统文件层

系统文件层主要负责将数据库的数据和日志存储在文件系统之上，并完成与存储引擎的交互，是文件的物理存储层。

## 查询处理过程

通过一条查询处理语句来理解 InnoDB 引擎和执行器内部执行更新的流程，流程图如下：

![](https://main.qcloudimg.com/raw/144a671d23fa452b8c7da58bcdb421a4.png)

**SQL 执行步骤**：请求、缓存、SQL 解析、优化 SQL 查询、调用引擎执行，返回结果。
- **连接**：客户端向 MySQL 服务器发送一条查询请求，与连接器交互，连接池相关处理，当该请求从等待队列进入到处理队列，管理器会将该请求丢给 SQL 接口。
- **缓存**：SQL 接口接收到请求后，服务器首先检查查询缓存，如果命中缓存，则立刻返回存储在缓存中的结果，否则进入下一阶段。
- **解析**：服务器进行 SQL 解析，判断 SQL 语句正确与否，若正确则将其转化为数据结构。
- **优化**：再由优化器生成对应的执行计划。
- **执行**：MySQL 根据执行计划，调用存储引擎的 API 来执行 SQL 语句。
- **结果**：将结果返回给客户端，同时缓存查询结果。

## 云数据库 MySQL 技术架构

![](https://main.qcloudimg.com/raw/b198f08b38d30d5fda139bbf60fcc786.png)

云数据库 MySQL 高可用版完全兼容 MySQL，并且采用一主 N 从的高可用模式，实时热备，提供宕机自动检测和故障自动转移。

数据节点部署在强大的硬件之上，底层存储使用本地 PCI-e SSD 硬盘，提供强大的 IO 性能。

可以覆盖游戏、互联网、金融、物联网、零售电商、物流、保险、证券等行业应用。

## 技术特征

### 多实例

![](https://main.qcloudimg.com/raw/6dc9553e5e903f87c8e4fafbefd535c5.png)

- 只读实例：只开放读能力，分担主实例读压力，实现读写分离。
- 主实例：可读写，主从实时热备，保证高可用，支持一主两从强同步，零误差，无错乱。
- 异地灾备实例：满足跨地域容灾金融级需求。

### 数据迁移

![](https://main.qcloudimg.com/raw/c95f6c3e46a7367b97abac28262f5133.png)

无需停机迁移，数据迁移时对业务无影响。

数据完成同步后，仅需切换数据库读写 IP 到云数据库 MySQL，即可完成迁移任务。

### 异地灾备（金融行业）

![](https://main.qcloudimg.com/raw/d960a74cbdd139e8a3cce0e127ebada5.png)

两地三中心部署架构——同城节点直线距离大于10KM，异地节点直线距离大于100KM。

同城多可用区网络互通，且网络延迟低于5ms。

多地域间使用多地域之间使用腾讯云专线连接，广州-上海同步延迟仅三十余毫秒。

### 备份和回档机制

![](https://main.qcloudimg.com/raw/b6a2eeec1788fa7f9c5b675d24a5d623.png)

云数据库 MySQL 每日自动冷备，备份于业务低峰期在备机上完成，不影响现网业务。

每份冷备数据保存3份副本，实现数据强一致性，保证数据不丢。

支持逻辑备份和物理备份两种备份方式：
- 逻辑备份支持导出 SQL 文件，可仅针对部分库表回档，适合需要细粒度回档的场景。
- 物理备份速度极快，支持增量备份，但需对整个实例回档，适合需要频繁备份数据的场景。

## 云数据库 MySQL--云监控

云监控为用户提供了统一监控云数据库 MySQL 的平台，可以通过使用云监控全面了解云数据库 MySQL 的资源使用、引擎性能和运行状况，提供指标分类、预设常用告警指标、预设核心指标的 Dashboard 面板。帮助用户更轻松的理解云数据库 MySQL 的指标，更方便、快捷的掌控 云数据库 MySQL 出现的突发情况，提升运维效率，减少运维成本。

### 监控指标及其分类

通过对云数据库 MySQL 的架构分析及其工作特性，腾讯云监控对云数据库 MySQL 的每一部分进行相应指标的监控，详细指标见 [指标说明](#.E6.8C.87.E6.A0.87.E8.AF.B4.E6.98.8E)。
![](https://main.qcloudimg.com/raw/47018a9e21ef0952a89f1ea09598df0b.png)

并将指标进行分类，以便用户理解。
![](https://main.qcloudimg.com/raw/5d50c50e6ba44bbaf26349f6181da6f5.png)

### 预设专家建议核心告警指标

腾讯云监控与云数据库 MySQL 业务侧经过讨论，根据多年运维经验，提供常用告警指标和阈值的专家建议。用户配置告警时，页面将默认显示预设的指标及阈值建议（暂未上线），支持修改，方便用户快速配置告警策略。

### 预设核心指标 Dashboard 面板

腾讯云监控与云数据库 MySQL 业务侧经过讨论，将核心指标和统计方式配置成预设 Dashboard 面板。用户使用 Dashboard 时，无需进行配置，即可看到如图所示的云数据库 云数据库 MySQL 的 Dashboard 预设面板，提升用户体验，降低使用成本。
![](https://main.qcloudimg.com/raw/2ed69ab82a9ab78255ba87db3a146f03.png)

## 指标说明

>?下方表格中加粗的指标为核心指标。


<table class="confluenceTable"><colgroup><col style="width: 144.0px;" /><col style="width: 227.0px;" /><col style="width: 179.0px;" /><col style="width: 173.0px;" /><col style="width: 548.0px;" /></colgroup><tbody><tr><th class="confluenceTh"><br /></th><th class="confluenceTh">指标英文名</th><th class="confluenceTh">单位</th><th class="confluenceTh">指标中文名</th><th class="confluenceTh">指标说明</th></tr><tr><th class="confluenceTh" rowspan="9">资源监控</th><td class="confluenceTd"><em><strong>CpuUseRate</strong></em></td><td class="confluenceTd"><em><strong>%</strong></em></td><td class="confluenceTd"><em><strong>CPU利用率</strong></em></td><td class="confluenceTd"><em><strong>允许闲时超用，CPU 利用率可能大于100%</strong></em></td></tr><tr><td class="confluenceTd">Capacity</td><td class="confluenceTd">MB</td><td class="confluenceTd">磁盘占用空间</td><td class="confluenceTd">包括 MySQL 数据目录和 binlog、relaylog、undolog、errorlog、slowlog 日志空间</td></tr><tr><td class="confluenceTd">MemoryUse</td><td class="confluenceTd">%</td><td class="confluenceTd">内存占用</td><td class="confluenceTd">允许闲时超用，实际内存占用可能大于购买规格</td></tr><tr><td class="confluenceTd"><em><strong>MemoryUseRate</strong></em></td><td class="confluenceTd"><em><strong>%</strong></em></td><td class="confluenceTd"><em><strong>内存利用率</strong></em></td><td class="confluenceTd"><em><strong>允许闲时超用，内存利用率可能大于100%</strong></em></td></tr><tr><td class="confluenceTd"><em><strong>BytesReceived</strong></em></td><td class="confluenceTd"><em><strong>Bps</strong></em></td><td class="confluenceTd"><em><strong>内网入流量</strong></em></td><td class="confluenceTd"><em><strong>每秒接受的字节数</strong></em></td></tr><tr><td class="confluenceTd"><em><strong>BytesSent</strong></em></td><td class="confluenceTd"><em><strong>Bps</strong></em></td><td class="confluenceTd"><em><strong>内网出流量</strong></em></td><td class="confluenceTd"><em><strong>每秒发送的字节数</strong></em></td></tr><tr><td class="confluenceTd">RealCapacity</td><td class="confluenceTd">MB</td><td class="confluenceTd">磁盘使用空间</td><td class="confluenceTd">仅包括 MySQL 数据目录，不含 binlog、relaylog、undolog、errorlog、slowlog 日志空间</td></tr><tr><td class="confluenceTd"><em><strong>VolumeRate</strong></em></td><td class="confluenceTd"><em><strong>%</strong></em></td><td class="confluenceTd"><em><strong>磁盘利用率</strong></em></td><td class="confluenceTd"><em><strong>磁盘使用空间/实例购买空间</strong></em></td></tr><tr><td class="confluenceTd"><em><strong>IOPS</strong></em></td><td class="confluenceTd"><em><strong>count/s</strong></em></td><td class="confluenceTd"><em><strong>IOPS</strong></em></td><td class="confluenceTd"><em><strong>每秒输入/输出操作</strong></em></td></tr><tr><th class="confluenceTh" rowspan="5">引擎监控(普通)-连接</th><td class="confluenceTd"><em><strong>QPS</strong></em></td><td class="confluenceTd"><em><strong>times/s</strong></em></td><td class="confluenceTd"><em><strong>每秒执行操作数</strong></em></td><td class="confluenceTd"><em><strong>数据库每秒执行的 SQL 数（含 insert、select、update、delete、replace），QPS 指标主要体现 TencentDB 实例的实际处理能力</strong></em></td></tr><tr><td class="confluenceTd"><strong><em>ConnectionUseRate</em></strong></td><td class="confluenceTd"><strong><em>%</em></strong></td><td class="confluenceTd"><strong><em>连接数利用率</em></strong></td><td class="confluenceTd"><strong><em>当前打开连接数/最大连接数</em></strong></td></tr><tr><td class="confluenceTd"><em><strong>TPS</strong></em></td><td class="confluenceTd"><em><strong>times/s</strong></em></td><td class="confluenceTd"><em><strong>每秒执行事务数</strong></em></td><td class="confluenceTd"><em><strong>数据库每秒传输的事务处理个数</strong></em></td></tr><tr><td class="confluenceTd">mMaxConnections</td><td class="confluenceTd">count</td><td class="confluenceTd">最大连接数</td><td class="confluenceTd">最大连接数</td></tr><tr><td class="confluenceTd"><em><strong>ThreadsConnected</strong></em></td><td class="confluenceTd"><em><strong>count</strong></em></td><td class="confluenceTd"><em><strong>当前连接数</strong></em></td><td class="confluenceTd"><em><strong>当前打开的连接的数量</strong></em></td></tr><tr><th class="confluenceTh" rowspan="9">引擎监控(普通)-访问</th><td class="confluenceTd">ComDelete</td><td class="confluenceTd">times/s</td><td class="confluenceTd">删除数</td><td class="confluenceTd">每秒删除数</td></tr><tr><td class="confluenceTd">ComInsert</td><td class="confluenceTd">times/s</td><td class="confluenceTd">插入数</td><td class="confluenceTd">每秒插入数</td></tr><tr><td class="confluenceTd">ComReplace</td><td class="confluenceTd">times/s</td><td class="confluenceTd">覆盖数</td><td class="confluenceTd">每秒覆盖数</td></tr><tr><td class="confluenceTd">ComUpdate</td><td class="confluenceTd">times/s</td><td class="confluenceTd">更新数</td><td class="confluenceTd">每秒更新数</td></tr><tr><td class="confluenceTd">Queries</td><td class="confluenceTd">times/s</td><td class="confluenceTd">总访问量</td><td class="confluenceTd">所有执行的 SQL 语句，包括 set，show 等</td></tr><tr><td class="confluenceTd">QueryRate</td><td class="confluenceTd">%</td><td class="confluenceTd">访问量占比</td><td class="confluenceTd">每秒执行操作数 QPS/推荐每秒操作数</td></tr><tr><td class="confluenceTd"><em><strong>SlowQueries</strong></em></td><td class="confluenceTd"><em><strong>count</strong></em></td><td class="confluenceTd"><em><strong>慢查询数</strong></em></td><td class="confluenceTd"><em><strong>查询时间超过 long_query_time 秒的查询的个数</strong></em></td></tr><tr><td class="confluenceTd">SelectCount</td><td class="confluenceTd">times/s</td><td class="confluenceTd">查询数</td><td class="confluenceTd">每秒查询数</td></tr><tr><td class="confluenceTd"><em><strong>SelectScan</strong></em></td><td class="confluenceTd"><em><strong>count/s</strong></em></td><td class="confluenceTd"><em><strong>全表扫描数</strong></em></td><td class="confluenceTd"><em><strong>执行全表搜索查询的数量</strong></em></td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(普通)-表</th><td class="confluenceTd">TableLocksWaited</td><td class="confluenceTd">times/s</td><td class="confluenceTd">等待表锁次数</td><td class="confluenceTd">不能立即获得的表的锁的次数</td></tr><tr><td class="confluenceTd">CreatedTmpTables</td><td class="confluenceTd">times/s</td><td class="confluenceTd">内存临时表数量</td><td class="confluenceTd">创建临时表的数量</td></tr><tr><th class="confluenceTh" rowspan="6">引擎监控(普通)-InnoDB</th><td class="confluenceTd">InnodbCacheHitRate</td><td class="confluenceTd">%</td><td class="confluenceTd">innodb缓存命中率</td><td class="confluenceTd">Innodb 引擎的缓存命中率</td></tr><tr><td class="confluenceTd">InnodbCacheUseRate</td><td class="confluenceTd">%</td><td class="confluenceTd">innodb缓存使用率</td><td class="confluenceTd">Innodb 引擎的缓存使用率</td></tr><tr><td class="confluenceTd">InnodbNumOpenFiles</td><td class="confluenceTd">count</td><td class="confluenceTd">InnoDB总页数当前InnoDB打开表的数量</td><td class="confluenceTd">Innodb 引擎当前打开表的数量</td></tr><tr><td class="confluenceTd">InnodbOsFileReads</td><td class="confluenceTd">times/s</td><td class="confluenceTd">innodb读磁盘数量</td><td class="confluenceTd">Innodb 引擎每秒读磁盘文件的次数</td></tr><tr><td class="confluenceTd">InnodbOsFileWrites</td><td class="confluenceTd">times/s</td><td class="confluenceTd">innodb写磁盘数量</td><td class="confluenceTd">Innodb 引擎每秒写磁盘文件的次数</td></tr><tr><td class="confluenceTd">InnodbOsFsyncs</td><td class="confluenceTd">times/s</td><td class="confluenceTd">innodbfsync数量</td><td class="confluenceTd">Innodb 引擎每秒调用 fsync 函数次数</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(普通)-MyISAM</th><td class="confluenceTd">KeyCacheHitRate</td><td class="confluenceTd">%</td><td class="confluenceTd">myisam缓存命中率</td><td class="confluenceTd">myisam 引擎的缓存命中率</td></tr><tr><td class="confluenceTd">KeyCacheUseRate</td><td class="confluenceTd">%</td><td class="confluenceTd">myisam缓存使用率</td><td class="confluenceTd">myisam 引擎的缓存使用率</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(扩展)-访问</th><td class="confluenceTd">ComCommit</td><td class="confluenceTd">times/s</td><td class="confluenceTd">提交数</td><td class="confluenceTd">每秒提交次数</td></tr><tr><td class="confluenceTd">ComRollback</td><td class="confluenceTd">times/s</td><td class="confluenceTd">回滚数</td><td class="confluenceTd">每秒回滚次数</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(扩展)-连接</th><td class="confluenceTd">ThreadsCreated</td><td class="confluenceTd">count</td><td class="confluenceTd">已创建的线程数</td><td class="confluenceTd">创建用来处理连接的线程数</td></tr><tr><td class="confluenceTd">ThreadsRunning</td><td class="confluenceTd">count</td><td class="confluenceTd">运行的线程数</td><td class="confluenceTd">激活的（非睡眠状态）线程数</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(扩展)-Tmp</th><td class="confluenceTd">CreatedTmpDiskTables</td><td class="confluenceTd">times/s</td><td class="confluenceTd">磁盘临时表数量</td><td class="confluenceTd">每秒创建磁盘临时表的次数</td></tr><tr><td class="confluenceTd">CreatedTmpFiles</td><td class="confluenceTd">times/s</td><td class="confluenceTd">临时文件数量</td><td class="confluenceTd">每秒创建临时文件的次数</td></tr><tr><th class="confluenceTh" rowspan="3">引擎监控(扩展)-Handler</th><td class="confluenceTd">HandlerCommit</td><td class="confluenceTd">times/s</td><td class="confluenceTd">内部提交数</td><td class="confluenceTd">每秒事务提交的次数</td></tr><tr><td class="confluenceTd">HandlerReadRndNext</td><td class="confluenceTd">times/s</td><td class="confluenceTd">读下一行请求数</td><td class="confluenceTd">每秒读取下一行的请求次数</td></tr><tr><td class="confluenceTd">HandlerRollback</td><td class="confluenceTd">times/s</td><td class="confluenceTd">内部回滚数</td><td class="confluenceTd">每秒事务被回滚的次数</td></tr><tr><th class="confluenceTh" rowspan="4">引擎监控(扩展)-Buff</th><td class="confluenceTd">InnodbBufferPoolPagesFree</td><td class="confluenceTd">count</td><td class="confluenceTd">InnoDB空页数</td><td class="confluenceTd">Innodb 引擎内存空页个数</td></tr><tr><td class="confluenceTd">InnodbBufferPoolPagesTotal</td><td class="confluenceTd">count</td><td class="confluenceTd">InnoDB总页数</td><td class="confluenceTd">Innodb 引擎占用内存总页数</td></tr><tr><td class="confluenceTd">InnodbBufferPoolReadRequests</td><td class="confluenceTd">times/s</td><td class="confluenceTd">innodb缓冲池预读页次数</td><td class="confluenceTd">Innodb 引擎每秒已经完成的逻辑读请求次数</td></tr><tr><td class="confluenceTd">InnodbBufferPoolReads</td><td class="confluenceTd">times/s</td><td class="confluenceTd">innodb磁盘读页次数</td><td class="confluenceTd">Innodb 引擎每秒已经完成的物理读请求次数</td></tr><tr><th class="confluenceTh" rowspan="4">引擎监控(扩展)-InnoDB Data</th><td class="confluenceTd">InnodbDataRead</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB读取量</td><td class="confluenceTd">Innodb 引擎每秒已经完成读取数据的字节数</td></tr><tr><td class="confluenceTd">InnodbDataReads</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB总读取量</td><td class="confluenceTd">Innodb 引擎每秒已经完成读取数据的次数</td></tr><tr><td class="confluenceTd">InnodbDataWrites</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB总写入量</td><td class="confluenceTd">Innodb 引擎每秒已经完成写数据的次数</td></tr><tr><td class="confluenceTd">InnodbDataWritten</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB写入量</td><td class="confluenceTd">Innodb 引擎每秒已经完成写数据的字节数</td></tr><tr><th class="confluenceTh" rowspan="6">引擎监控(扩展)-InnoDB Row</th><td class="confluenceTd">InnodbRowLockTimeAvg</td><td class="confluenceTd">ms</td><td class="confluenceTd">InnoDB平均获取行锁时间（毫秒）</td><td class="confluenceTd">Innodb 引擎行锁定的平均时长</td></tr><tr><td class="confluenceTd">InnodbRowLockWaits</td><td class="confluenceTd">ms</td><td class="confluenceTd">InnoDB等待行锁次数</td><td class="confluenceTd">Innodb 引擎每秒等待行锁定的次数</td></tr><tr><td class="confluenceTd">InnodbRowsDeleted</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB行删除量</td><td class="confluenceTd">Innodb 引擎每秒删除的行数</td></tr><tr><td class="confluenceTd">InnodbRowsInserted</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB行插入量</td><td class="confluenceTd">Innodb 引擎每秒插入的行数</td></tr><tr><td class="confluenceTd">InnodbRowsRead</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB行读取量</td><td class="confluenceTd">Innodb 引擎每秒读取的行数</td></tr><tr><td class="confluenceTd">InnodbRowsUpdated</td><td class="confluenceTd">times/s</td><td class="confluenceTd">InnoDB行更新量</td><td class="confluenceTd">Innodb 引擎每秒更新的行数</td></tr><tr><th class="confluenceTh" rowspan="6">引擎监控(扩展)-Key</th><td class="confluenceTd">KeyBlocksUnused</td><td class="confluenceTd">count</td><td class="confluenceTd">键缓存内未使用的块数量</td><td class="confluenceTd">myisam 引擎未使用键缓存块的个数</td></tr><tr><td class="confluenceTd">KeyBlocksUsed</td><td class="confluenceTd">count</td><td class="confluenceTd">键缓存内使用的块数量</td><td class="confluenceTd">myisam 引擎已使用键缓存块的个数</td></tr><tr><td class="confluenceTd">KeyReadRequests</td><td class="confluenceTd">times/s</td><td class="confluenceTd">键缓存读取数据块次数</td><td class="confluenceTd">myisam 引擎每秒读取键缓存块的次数</td></tr><tr><td class="confluenceTd">KeyReads</td><td class="confluenceTd">times/s</td><td class="confluenceTd">硬盘读取数据块次数</td><td class="confluenceTd">myisam 引擎每秒读取硬盘数据块的次数</td></tr><tr><td class="confluenceTd">KeyWriteRequests</td><td class="confluenceTd">times/s</td><td class="confluenceTd">数据块写入键缓冲次数</td><td class="confluenceTd">myisam 引擎每秒写键缓存块的次数</td></tr><tr><td class="confluenceTd">KeyWrites</td><td class="confluenceTd">times/s</td><td class="confluenceTd">数据块写入磁盘次数</td><td class="confluenceTd">myisam 引擎每秒写硬盘数据块的次数</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(扩展)-表</th><td class="confluenceTd">OpenedTables</td><td class="confluenceTd">count</td><td class="confluenceTd">已经打开的表数</td><td class="confluenceTd">引擎已经打开的表的数量</td></tr><tr><td class="confluenceTd">TableLocksImmediate</td><td class="confluenceTd">count</td><td class="confluenceTd">立即释放的表锁数</td><td class="confluenceTd">引擎即将释放的表锁数</td></tr><tr><th class="confluenceTh" rowspan="2">引擎监控(扩展)-其他</th><td class="confluenceTd">LogCapacity</td><td class="confluenceTd">MB</td><td class="confluenceTd">日志使用量</td><td class="confluenceTd">引擎已使用的日志量</td></tr><tr><td class="confluenceTd">OpenFiles</td><td class="confluenceTd">times/s</td><td class="confluenceTd">打开文件数</td><td class="confluenceTd">引擎打开的文件数量</td></tr><tr><th class="confluenceTh" rowspan="4">部署监控(备机)</th><td class="confluenceTd">MasterSlaveSyncDistance</td><td class="confluenceTd">MB</td><td class="confluenceTd">主从延迟距离</td><td class="confluenceTd">主从 binlog 差距</td></tr><tr><td class="confluenceTd">SlaveIoRunning</td><td class="confluenceTd">状态值（0-Yes，1-No，2-Connecting）</td><td class="confluenceTd">IO线程状态</td><td class="confluenceTd">IO 线程运行状态</td></tr><tr><td class="confluenceTd">SlaveSqlRunning</td><td class="confluenceTd">slave_sql_running</td><td class="confluenceTd">SQL线程状态</td><td class="confluenceTd">SQL 线程运行状态</td></tr><tr><td class="confluenceTd">SecondsBehindMaster</td><td class="confluenceTd">MB</td><td class="confluenceTd">主从延迟时间</td><td class="confluenceTd">主从延迟时间</td></tr></tbody></table>

