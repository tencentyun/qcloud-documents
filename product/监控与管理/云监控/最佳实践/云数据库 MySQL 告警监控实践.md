## 简介

[云数据库 MySQL](https://cloud.tencent.com/document/product/236)（TencentDB for MySQL）是腾讯云基于开源数据库 MySQL 专业打造的一种高性能分布式数据存储服务，提供了备份恢复、监控、容灾、快速扩容、数据传输等全套解决方案，简化数据库运维工作，让用户专注于业务发展。

云数据库 MySQL 的优势：

- 快速便捷的数据库服务交付能力，在几分钟内部署可扩展的 MySQL，并可按需弹性升降配置。
- 真正100%的 MySQL 兼容能力，主流 MySQL 分支完全兼容。
- 提供热备、冷备、binlog三重灾备体系，可用性达到99.95%，可靠性达到99.9996%，确保服务可用，数据不丢失。
- 提供一系列数据库管理服务：监控、备份、回档、扩容、性能诊断、数据迁移等。
- 实例最高 QPS 可达245509次/秒，极大的简化业务开发，减少业务架构复杂度。
- 卓越的高可用，支持多可用区部署，跨城容灾的能力。

## 技术架构

### 云数据库MySQL 技术架构

![](https://main.qcloudimg.com/raw/b198f08b38d30d5fda139bbf60fcc786.png)

云数据库 MySQL 高可用版完全兼容 MySQL，并且采用一主N从的高可用模式，实时热备，提供宕机自动检测和故障自动转移。数据节点部署在强大的硬件之上，底层存储使用本地 PCI-e SSD 硬盘，提供强大的 IO 性能。可以覆盖游戏、互联网、金融、物联网、零售电商、物流、保险、证券等行业应用。

## 技术特征

### 多实例

![](https://main.qcloudimg.com/raw/dddd0883cd4b796f726e834fafbc2099.png)

- 只读实例：只开放读能力，分担主实例读压力，实现读写分离。
- 主实例：可读写，主从实时热备，保证高可用，支持一主两从强同步，零误差，无错乱。
- 异地灾备实例：满足跨地域容灾金融级需求。

### 数据迁移

![](https://main.qcloudimg.com/raw/c95f6c3e46a7367b97abac28262f5133.png)

- 无需停机迁移，数据迁移时对业务无影响。
- 数据完成同步后，仅需切换数据库读写 IP 到云数据库 MySQL，即可完成迁移任务。

### 异地灾备（金融行业）

![](https://main.qcloudimg.com/raw/d960a74cbdd139e8a3cce0e127ebada5.png)

- 两地三中心部署架构：同城节点直线距离大于10KM，异地节点直线距离大于100KM。
- 同城多可用区网络互通，且网络延迟低于5ms。
- 多地域间使用多地域之间使用腾讯云专线连接，广州与上海同步延迟仅三十余毫秒。

### 备份和回档机制

<img src="https://main.qcloudimg.com/raw/b6a2eeec1788fa7f9c5b675d24a5d623.png" data-nonescope="true">

云数据库 MySQL 每日自动冷备，备份于业务低峰期在备机上完成，不影响现网业务。

每份冷备数据保存3份副本，实现数据强一致性，保证数据不丢失。

支持逻辑备份和物理备份两种备份方式：

- 逻辑备份支持导出 SQL 文件，可仅针对部分库表回档，适合需要细粒度回档的场景。
- 物理备份速度极快，支持增量备份，但需对整个实例回档，适合需要频繁备份数据的场景。

## 云数据库 MySQL 监控

云监控为用户提供了统一监控云数据库 MySQL 的平台，可以通过使用云监控全面了解云数据库 MySQL 的资源使用、引擎性能和运行状况，提供指标分类、预设常用告警指标、预设核心指标的 Dashboard 面板。帮助用户更轻松的理解云数据库 MySQL 的指标，更方便、快捷的掌控云数据库 MySQL 出现的突发情况，提升运维效率，减少运维成本。

### 监控指标及其分类

#### 监控实例分析

云数据库 MySQL 实例的架构主要分为三个部分：[网络连接层](#Network)、[服务层](#service)、[存储引擎层](#storage)。
![](https://main.qcloudimg.com/raw/47018a9e21ef0952a89f1ea09598df0b.png)


<span id="Network"></span>

**网络连接层**

接入集群：提供与 MySQL 服务器建立连接的支持。


<span id="service"></span>

**服务层**

服务层是 MySQL 的核心，主要包含以下五个部分：

- **连接器**：管理缓冲用户连接，线程处理，权限验证等需要缓存的需求。
- **查询缓存**：将客户端提交 给MySQL 的 Select 类 query 请求的返回结果集 cache 到内存中，与该 query 的一个 hash 值做一个对应。缓存机制是由一系列小缓存组成，例如表缓存、记录缓存、权限缓存、引擎缓存等。
- **分析器**：将客户端发送的SQL进行语义和语法的分析，分解成数据结构，生成"解析树"。预处理器根据规则进一步检查“解析树”是否合法，最终生成新的“解析树”。
- **优化器**：当“解析树”通过解析器语法检查后，交由优化器对查询进行优化，将其转换成执行计划。
- **执行器**：执行优化器给出的执行计划，然后存储引擎交互。

<span id="storage"></span>

**存储引擎层**

存储引擎负责 MySQL 中数据的存储和提取，与底层系统文件进行交互，云数据库 MySQL 主要使用 InnoDB 引擎和 MyISAM 引擎。


#### 指标分类

腾讯云监控对云数据库 MySQL 的每一部分进行相应指标的监控，并将指标进行分类，以便用户理解和使用，详情请参见 [指标说明](#step1)。

![](https://main.qcloudimg.com/raw/5d50c50e6ba44bbaf26349f6181da6f5.png)

### 预设专家建议核心告警指标

腾讯云监控与云数据库MySQL业务侧经过讨论，根据多年运维经验，提供常用告警指标和阈值的专家建议。用户配置告警时，页面将默认显示预设的指标及阈值建议，支持修改，方便用户快速配置告警策略。

**1. 磁盘利用率 > 80%**

MySQL实例可能因长时间运行，未进行磁盘及数据管理等原因，导致磁盘使用率升高，从而影响业务正常运行。尤其当实例显示“磁盘空间满”状态，数据库不可进行写入操作，会有实例异常、数据库备份失败、数据库实例只读状态等潜在风险。

为避免业务因磁盘利用率过高而受影响，设置磁盘利用率>80%告警，当接收到告警后，建议根据实际情况采用磁盘容量扩容、迁移冷数据等解决方案确保磁盘有一定的冗余度，保证数据库的正常使用。

**2. CPU 利用率 >8 0%**

系统执行应用来进行提交查询（包括数据修改操作）时需要大量的逻辑读（逻辑 IO，执行查询所需访问的表的数据行数），所以系统需要消耗大量的 CPU 资源以维护从存储系统读取到内存中的数据一致性。若 MySQL CPU 的利用率长时间处于100%，会严重影响数据库的整体性能，极端情况下可能会出现实例 HANG 住的情况。

为避免业务因 CPU 资源不足而受影响，设置 CPU 使用率 > 80%告警，当接收到告警后，建议从应用架构、实例规格等方面来解决，例如：

- 升级实例规格，增加 CPU 资源。
- 增加只读实例，将对数据一致性不敏感的查询转移到只读实例上，分担主实例压力。

**3. 内存利用率 > 80%**

MySQL 的内存是重要的性能参数，常出现由于低效 SQL 请求以及待优化的数据库导致内存利用率过高甚至超过100%的情况。内存利用率过高容易引起服务响应速度变慢，严重时还会触发内存 OOM 进而发生主备切换。

为避免业务因内存利用率过高而受影响，设置内存利用率>80%告警，当接收到告警后，建议对内存利用率过高的实例进行业务优化或者升级内存空间。

### 预设核心指标 Dashboard 面板

为了让用户更快捷、更方便的监控云数据库 MySQL 的资源使用、运行等状况，腾讯云监控将核心指标配置成预设 Dashboard 面板，用户可直接进入云监控的 Dashboard 页面，无需进行其他配置，即可看到如图所示的云数据库 MySQL 的 Dashboard 预设面板。

![](https://main.qcloudimg.com/raw/d752e218e7ccc358ed4cb9b23418850c.png)

当用户选择自己已有的实例后，便可自动展示预设的资源、引擎连接和引擎访问等核心指标的监控Dashboard，提升用户体验，降低使用成本。

- 监控CPU利用率、磁盘利用率、内存利用率、内网入流量、内网出流量等资源，配合告警，当监控值超过某一值时，要关注是否需要扩容。
- 监控QPS、TPS、当前打开的连接数的量，提前感知数据库的状态。如果发现监控值突增，可能是业务出现了问题，需要根据实际情况定位问题，提前做好数据库的扩容和优化。
- 监控慢查询数和全表扫描数，如果出现，及时查看哪些 SQL 语句引起的慢查询，然后可能需要对这些 SQL 或者服务做优化。

![](https://main.qcloudimg.com/raw/2ed69ab82a9ab78255ba87db3a146f03.png)



## 指标说明

<span id="step1"></span>

> ?下方表格中加粗的指标为核心指标。

<table>
   <tr>
      <th>监控项</th>
      <th>指标英文名</th>
      <th>指标中文名</th>
      <th>单位</th>
      <th>指标说明</th>
   </tr>
   <tr>
      <td rowspan="9">资源监控</td>
      <td><b>CpuUseRate</b></td>
      <td><b>CPU 利用率</b></td>
      <td><b>%</b></td>
      <td><b>允许闲时超用，CPU 利用率可能大于100%</b></td>
   </tr>
   <tr>
      <td>Capacity</td>
      <td>磁盘占用空间</td>
      <td>MB</td>
      <td>包括 MySQL 数据目录和 binlog、relaylog、undolog、errorlog、slowlog 日志空间</td>
   </tr>
   <tr>
      <td>MemoryUse</td>
      <td>内存占用</td>
      <td>%</td>
      <td>允许闲时超用，实际内存占用可能大于购买规格</td>
   </tr>
   <tr>
      <td><b>MemoryUseRate</b></td>
      <td><b>内存利用率</b></td>
      <td><b>%</b></td>
      <td><b>允许闲时超用，内存利用率可能大于100%</b></td>
   </tr>
   <tr>
      <td><b>BytesReceived</b></td>
      <td><b>内网入流量</b></td>
      <td><b>Bps</b></td>
      <td><b>每秒接受的字节数</b></td>
   </tr>
   <tr>
      <td><b>BytesSent</b></td>
      <td><b>内网出流量</b></td>
      <td><b>Bps</b></td>
      <td><b>每秒发送的字节数</b></td>
   </tr>
   <tr>
      <td>RealCapacity</td>
      <td>磁盘使用空间</td>
      <td>MB</td>
      <td>仅包括 MySQL 数据目录，不含 binlog、relaylog、undolog、errorlog、slowlog 日志空间</td>
   </tr>
   <tr>
      <td><b>VolumeRate</b></td>
      <td><b>磁盘利用率</b></td>
      <td><b>%</b></td>
      <td><b>磁盘使用空间/实例购买空间</b></td>
   </tr>
   <tr>
      <td><b>IOPS</b></td>
      <td><b>IOPS</b></td>
      <td><b>count/s</b></td>
      <td><b>每秒输入/输出操作</b></td>
   </tr>
   <tr>
      <td rowspan="5">引擎监控（普通）-连接</td>
      <td><b>QPS</b></td>
      <td><b>每秒执行操作数</b></td>
      <td><b>times/s</b></td>
      <td><b>数据库每秒执行的 SQL 数（含 insert、select、update、delete、replace），QPS 指标主要体现 TencentDB 实例的实际处理能力</b></td>
   </tr>
   <tr>
      <td><b>ConnectionUseRate</b></td>
      <td><b>连接数利用率</b></td>
      <td><b>%</b></td>
      <td><b>当前打开连接数/最大连接数</b></td>
   </tr>
   <tr>
      <td><b>TPS</b></td>
      <td><b>每秒执行事务数</b></td>
      <td><b>times/s</b></td>
      <td><b>数据库每秒传输的事务处理个数</b></td>
   </tr>
   <tr>
      <td>mMaxConnections</td>
      <td>最大连接数</td>
      <td>count</td>
      <td>最大连接数</td>
   </tr>
   <tr>
      <td><b>ThreadsConnected</b></td>
      <td><b>当前连接数</b></td>
      <td><b>count</b></td>
      <td><b>当前打开的连接的数量</b></td>
   </tr>
   <tr>
      <td rowspan="9">引擎监控（普通）-访问</td>
      <td>ComDelete</td>
      <td>删除数</td>
      <td>times/s</td>
      <td>每秒删除数</td>
   </tr>
   <tr>
      <td>ComInsert</td>
      <td>插入数</td>
      <td>times/s</td>
      <td>每秒插入数</td>
   </tr>
   <tr>
      <td>ComReplace</td>
      <td>覆盖数</td>
      <td>times/s</td>
      <td>每秒覆盖数</td>
   </tr>
   <tr>
      <td>ComUpdate</td>
      <td>更新数</td>
      <td>times/s</td>
      <td>每秒更新数</td>
   </tr>
   <tr>
      <td>Queries</td>
      <td>总访问量</td>
      <td>times/s</td>
      <td>所有执行的 SQL 语句，包括 set，show 等</td>
   </tr>
   <tr>
      <td>QueryRate</td>
      <td>访问量占比</td>
      <td>%</td>
      <td>每秒执行操作数 QPS/推荐每秒操作数</td>
   </tr>
   <tr>
      <td><b>SlowQueries</td>
      <td><b>慢查询数</td>
      <td><b>count</td>
      <td><b>查询时间超过 long_query_time 秒的查询的个数</td>
   </tr>
   <tr>
      <td>SelectCount</td>
      <td>查询数</td>
      <td>times/s</td>
      <td>每秒查询数</td>
   </tr>
   <tr>
      <td><b>SelectScan</td>
      <td><b>全表扫描数</td>
      <td><b>count/s</td>
      <td><b>执行全表搜索查询的数量</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（普通）-表</td>
      <td>TableLocksWaited</td>
      <td>等待表锁次数</td>
      <td>times/s</td>
      <td>不能立即获得的表的锁的次数</td>
   </tr>
   <tr>
      <td>CreatedTmpTables</td>
      <td>内存临时表数量</td>
      <td>times/s</td>
      <td>创建临时表的数量</td>
   </tr>
   <tr>
      <td rowspan="6">引擎监控（普通）-InnoDB</td>
      <td>InnodbCacheHitRate</td>
      <td>innodb 缓存命中率</td>
      <td>%</td>
      <td>Innodb 引擎的缓存命中率</td>
   </tr>
   <tr>
      <td>InnodbCacheUseRate</td>
      <td>innodb缓存使用率</td>
      <td>%</td>
      <td>Innodb 引擎的缓存使用率</td>
   </tr>
   <tr>
      <td>InnodbNumOpenFiles</td>
      <td>InnoDB 总页数当前 InnoDB 打开表的数量</td>
      <td>count</td>
      <td>Innodb 引擎当前打开表的数量</td>
   </tr>
   <tr>
      <td>InnodbOsFileReads</td>
      <td>innodb 读磁盘数量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒读磁盘文件的次数</td>
   </tr>
   <tr>
      <td>InnodbOsFileWrites</td>
      <td>innodb 写磁盘数量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒写磁盘文件的次数</td>
   </tr>
   <tr>
      <td>InnodbOsFsyncs</td>
      <td>innodbfsync数量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒调用 fsync 函数次数</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（普通）-MyISAM</td>
      <td>KeyCacheHitRate</td>
      <td>myisam缓存命中率</td>
      <td>%</td>
      <td>myisam 引擎的缓存命中率</td>
   </tr>
   <tr>
      <td>KeyCacheUseRate</td>
      <td>myisam缓存使用率</td>
      <td>%</td>
      <td>myisam 引擎的缓存使用率</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（扩展）-访问</td>
      <td>ComCommit</td>
      <td>提交数</td>
      <td>times/s</td>
      <td>每秒提交次数</td>
   </tr>
   <tr>
      <td>ComRollback</td>
      <td>回滚数</td>
      <td>times/s</td>
      <td>每秒回滚次数</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（扩展）-连接</td>
      <td>ThreadsCreated</td>
      <td>已创建的线程数</td>
      <td>count</td>
      <td>创建用来处理连接的线程数</td>
   </tr>
   <tr>
      <td>ThreadsRunning</td>
      <td>运行的线程数</td>
      <td>count</td>
      <td>激活的（非睡眠状态）线程数</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（扩展）-Tmp</td>
      <td>CreatedTmpDiskTables</td>
      <td>磁盘临时表数量</td>
      <td>times/s</td>
      <td>每秒创建磁盘临时表的次数</td>
   </tr>
   <tr>
      <td>CreatedTmpFiles</td>
      <td>临时文件数量</td>
      <td>times/s</td>
      <td>每秒创建临时文件的次数</td>
   </tr>
   <tr>
      <td rowspan="3">引擎监控（扩展）-Handler</td>
      <td>HandlerCommit</td>
      <td>内部提交数</td>
      <td>times/s</td>
      <td>每秒事务提交的次数</td>
   </tr>
   <tr>
      <td>HandlerReadRndNext</td>
      <td>读下一行请求数</td>
      <td>times/s</td>
      <td>每秒读取下一行的请求次数</td>
   </tr>
   <tr>
      <td>HandlerRollback</td>
      <td>内部回滚数</td>
      <td>times/s</td>
      <td>每秒事务被回滚的次数</td>
   </tr>
   <tr>
      <td rowspan="4">引擎监控（扩展）-Buff</td>
      <td>InnodbBufferPoolPagesFree</td>
      <td>InnoDB空页数</td>
      <td>count</td>
      <td>Innodb 引擎内存空页个数</td>
   </tr>
   <tr>
      <td>InnodbBufferPoolPagesTotal</td>
      <td>InnoDB总页数</td>
      <td>count</td>
      <td>Innodb 引擎占用内存总页数</td>
   </tr>
   <tr>
      <td>InnodbBufferPoolReadRequests</td>
      <td>innodb缓冲池预读页次数</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成的逻辑读请求次数</td>
   </tr>
   <tr>
      <td>InnodbBufferPoolReads</td>
      <td>innodb 磁盘读页次数</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成的物理读请求次数</td>
   </tr>
   <tr>
      <td rowspan="4">引擎监控（扩展）-InnoDB Data</td>
      <td>InnodbDataRead</td>
      <td>InnoDB读取量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成读取数据的字节数</td>
   </tr>
   <tr>
      <td>InnodbDataReads</td>
      <td>InnoDB总读取量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成读取数据的次数</td>
   </tr>
   <tr>
      <td>InnodbDataWrites</td>
      <td>InnoDB总写入量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成写数据的次数</td>
   </tr>
   <tr>
      <td>InnodbDataWritten</td>
      <td>InnoDB写入量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒已经完成写数据的字节数</td>
   </tr>
   <tr>
      <td rowspan="6">引擎监控（扩展）-InnoDB Row</td>
      <td>InnodbRowLockTimeAvg</td>
      <td>InnoDB平均获取行锁时间（毫秒）</td>
      <td>ms</td>
      <td>Innodb 引擎行锁定的平均时长</td>
   </tr>
   <tr>
      <td>InnodbRowLockWaits</td>
      <td>InnoDB等待行锁次数</td>
      <td>ms</td>
      <td>Innodb 引擎每秒等待行锁定的次数</td>
   </tr>
   <tr>
      <td>InnodbRowsDeleted</td>
      <td>InnoDB行删除量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒删除的行数</td>
   </tr>
   <tr>
      <td>InnodbRowsInserted</td>
      <td>InnoDB 行插入量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒插入的行数</td>
   </tr>
   <tr>
      <td>InnodbRowsRead</td>
      <td>InnoDB 行读取量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒读取的行数</td>
   </tr>
   <tr>
      <td>InnodbRowsUpdated</td>
      <td>InnoDB 行更新量</td>
      <td>times/s</td>
      <td>Innodb 引擎每秒更新的行数</td>
   </tr>
   <tr>
      <td rowspan="6">引擎监控（扩展）-Key</td>
      <td>KeyBlocksUnused</td>
      <td>键缓存内未使用的块数量</td>
      <td>count</td>
      <td>myisam 引擎未使用键缓存块的个数</td>
   </tr>
   <tr>
      <td>KeyBlocksUsed</td>
      <td>键缓存内使用的块数量</td>
      <td>count</td>
      <td>myisam 引擎已使用键缓存块的个数</td>
   </tr>
   <tr>
      <td>KeyReadRequests</td>
      <td>键缓存读取数据块次数</td>
      <td>times/s</td>
      <td>myisam 引擎每秒读取键缓存块的次数</td>
   </tr>
   <tr>
      <td>KeyReads</td>
      <td>硬盘读取数据块次数</td>
      <td>times/s</td>
      <td>myisam 引擎每秒读取硬盘数据块的次数</td>
   </tr>
   <tr>
      <td>KeyWriteRequests</td>
      <td>数据块写入键缓冲次数</td>
      <td>times/s</td>
      <td>myisam 引擎每秒写键缓存块的次数</td>
   </tr>
   <tr>
      <td>KeyWrites</td>
      <td>数据块写入磁盘次数</td>
      <td>times/s</td>
      <td>myisam 引擎每秒写硬盘数据块的次数</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（扩展）-表</td>
      <td>OpenedTables</td>
      <td>已经打开的表数</td>
      <td>count</td>
      <td>引擎已经打开的表的数量</td>
   </tr>
   <tr>
      <td>TableLocksImmediate</td>
      <td>立即释放的表锁数</td>
      <td>count</td>
      <td>引擎即将释放的表锁数</td>
   </tr>
   <tr>
      <td rowspan="2">引擎监控（扩展）-其他</td>
      <td>LogCapacity</td>
      <td>日志使用量</td>
      <td>MB</td>
      <td>引擎已使用的日志量</td>
   </tr>
   <tr>
      <td>OpenFiles</td>
      <td>打开文件数</td>
      <td>times/s</td>
      <td>引擎打开的文件数量</td>
   </tr>
   <tr>
      <td rowspan="4">部署监控（备机）</td>
      <td>MasterSlaveSyncDistance</td>
      <td>主从延迟距离</td>
      <td>MB</td>
      <td>主从 binlog 差距</td>
   </tr>
   <tr>
      <td>SlaveIoRunning</td>
      <td>IO线程状态</td>
      <td>状态值（0-Yes，1-No，2-Connecting）</td>
      <td>IO 线程运行状态</td>
   </tr>
   <tr>
      <td>SlaveSqlRunning</td>
      <td>SQL线程状态</td>
      <td>slave_sql_running</td>
      <td>SQL 线程运行状态</td>
   </tr>
   <tr>
      <td>SecondsBehindMaster</td>
      <td>主从延迟时间</td>
      <td>MB</td>
      <td>主从延迟时间</td>
   </tr>
</table>
