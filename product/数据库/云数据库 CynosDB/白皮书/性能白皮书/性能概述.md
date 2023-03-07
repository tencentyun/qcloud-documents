TDSQL-C MySQL 版（TDSQL-C for MySQL）是腾讯云自研的新一代云原生关系型数据库。融合了传统数据库、云计算与新硬件技术的优势，100%兼容 MySQL，为用户提供极致弹性、高性能、高可用、高可靠、安全的数据库服务。实现超百万 QPS 的高吞吐、PB 级海量分布式智能存储、Serverless 秒级伸缩，助力企业加速完成数字化转型。

TDSQL-C MySQL 版提供备份、恢复、监控、快速扩容、数据传输等数据库运维全套解决方案，为您简化 IT 运维工作，让您能更加专注于业务发展。

TDSQL-C MySQL 版经专业团队不断测试和优化，提供了多种 MySQL 企业版功能，TDSQL-C MySQL 版引擎内核也进行了大量优化，具备灵活、高效的事务处理能力、先进完备的合规安全防护能力以及超大实例容量使其具备了优越强劲的性能。

本章节通过对 TDSQL-C MySQL 版和腾讯云 MySQL 从全缓存、大数据集、单表1T的数据集特征，分别从只写、只读以及混合读写场景进行性能测试对比，来展示 TDSQL-C MySQL 版的总体性能概况，具体测试场景请参见下表。

TDSQL-C MySQL 版重磅升级，新版本架构采用全链路 RDMA、基于企业级 TXSQL 内核优化多项性能、升级分布式存储层架构，以及提供全新硬件设备支撑。

>?目前新架构已上线北京六区，提供开放公测，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取公测资格。

<table>
<tr><th>数据集特征</th><th>测试场景</th><th>读类型</th></tr>
<tr><td rowspan = "5"  width="33%">全缓存</td><td>只写</td><td>-</td></tr>
<tr><td>只读</td><td>point select</td></tr>
<tr><td>只读</td><td>range select</td></tr>
<tr><td>混合读写</td><td>point select</td></tr>
<tr><td>混合读写</td><td>range select</td></tr>
<tr><td rowspan = "5"  width="33%">大数据集</td><td>只写</td><td>-</td></tr>
<tr><td>只读</td><td>point select</td></tr>
<tr><td>只读</td><td>range select</td></tr>
<tr><td>混合读写</td><td>point select</td></tr>
<tr><td>混合读写</td><td>range select</td></tr>
<tr><td rowspan = "5"  width="33%">单表1T</td><td>只写</td><td>-</td></tr>
<tr><td>只读</td><td>point select</td></tr>
<tr><td>只读</td><td>range select</td></tr>
<tr><td>混合读写</td><td>point select</td></tr>
<tr><td>混合读写</td><td>range select</td></tr>
<table>

>?表格中，**point select** 和 **range select** 定义如下。
>- **point select**：点测试，表示单次事务中点选择测试的查询次数。
>- **range select**：范围测试，表示单次事务中范围选择测试的查询次数。
>
