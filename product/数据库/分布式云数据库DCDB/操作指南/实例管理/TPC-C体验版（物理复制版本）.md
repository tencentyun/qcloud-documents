本文将介绍 TDSQL MySQL 版中 TPC-C 体验版（物理复制版本）的特性、性能及使用方式。该版本是 TDSQL 通过 TPC-C 基准测试的版本，在高 IO 并发性能上有较大的提升。

>? 
>- 由 TPC 发起的 TPC-C 是全球数据库认可的一套性能评价标准，它模拟超大型高并发的极值场景，对数据库系统的软硬件协同能力要求极高。
>- 2023年3月，腾讯云数据库 TDSQL 实现每分钟交易量8.14亿次，同时在超高压下稳定运行8小时，波动率为0.2%，成功打破纪录。
>- TPC官网链接：[官网链接](https://www.tpc.org/tpcc/results/tpcc_results5.asp?print=false&orderby=tpm&sortby=desc) 。

## 物理复制版本特性
- 支持物理复制。物理复制是将主库 WAL 日志流直接发给备库，备库根据 WAL 日志进行重做的一种复制方式，这种复制和 MySQL 原生复制有明显区别，复制期间不会产生 binlog 文件。

 <table>
 <thread>
 <tr><th width=10%>复制类型</th><th>特性</th></tr>
 </thread>
 <tbody>
 <tr>
 <td>物理复制</td>
 <td><ul><li>以 WAL 日志流传输，不涉及 binlog 和 gtid，减少了数据写盘量，实例整体的吞吐量和响应时间都得到了提升。</li></ul>
<ul><li> 拥有更好的并发性，redolog 的同步可以支持同时在主备库上执行事务，而无需等待主库上执行完成再执行备库。</li></ul></td>
 </tr>
 <tr>
 <td>原生复制</td><td>生成 binlog 进行同步复制，binlog 是较为统一的日志格式，有成熟的工具来进行解析，通过 binlog 可以提供回档、迁移、同步等能力，并使主备之间的复制方式更加多样化。</td>
 </tr>
 </tbody>
 </table>

- 不支持创建灾备关系。
- 不支持 binlog 查看和备份克隆。
- 不支持全局一致性读。
- 不支持一级 list/range 和二级分区表。
- 不支持 SET 级全局索引。
- 不支持 TDE 透明加密。
- 不支持作为源数据库或目标数据库创建 DTS 数据迁移和数据同步任务。
- 不支持 DBS 数据库备份。

## 物理复制版本性能
经过测试，在高 IO 场景下，物理复制版本的性能有显著提升。
系统架构：x86

<table>
<thread>
<tr><td width="120">测试工具</td><td colspan=4>sysbench 1.1.0</td></tr>
</thread>
<tbody>
<tr>
<td>实例类型</td><td colspan=4>分布式实例，4SET，100G内存，1主1备，强同步，64张表，400w行/张，72G数据（每个节点18G）</td>
</tr>
<tr><td>测试版本</td><td colspan=2>TPCC 体验版</td><td  colspan=2>8.0.24版本</td></tr>
<tr><td>测试并发</td><td  colspan=2>1000个</td><td colspan=2>1000个</td></tr>
<tr><td>导数耗时</td><td colspan=2>2 min</td><td colspan=2>2 min</td></tr>
<tr><td>结果指标</td><td>TPS</td><td>QPS</td><td>TPS</td><td>QPS</td></tr>
<tr><td>点查</td><td>466200</td><td>466200</td><td>467623</td><td>467623</td></tr>
<tr><td>混合读写</td><td>25873</td><td>413982</td><td>24079</td><td>385268</td></tr>
<tr><td>索引更新</td><td>420240</td><td>420240</td><td>223315</td><td>223315</td></tr>
<tr><td>非索引更新</td><td>450442</td><td>450442</td><td>246283</td><td>246283</td></tr>
</tbody>
</table>

<table>
<thread>
<tr><td>测试工具</td><td colspan=4>TPCC</td></tr>
</thread>
<tbody>
<tr>
<td>实例类型</td><td colspan=4>分布式实例，4SET，100G内存，1主1备，强同步</td>
</tr>
<tr><td>测试版本</td><td colspan=2>TPCC 体验版</td><td  colspan=2>8.0.24版本</td></tr>
<tr><td>测试并发</td><td  colspan=2>1500个</td><td colspan=2>1500个</td></tr>
<tr><td>导数耗时</td><td colspan=2>6 min</td><td colspan=2>10 min</td></tr>
<tr><td>仓数</td><td colspan=2>400仓（24G数据）</td><td colspan=2>400仓（24G数据）</td></tr>
<tr><td>tpmC(NewOrders)</td><td colspan=2>718987.05</td><td colspan=2>657133.54</td></tr>
<tr><td>tpmTOTAL</td><td colspan=2>1597821.41</td><td colspan=2>1460117.75</td></tr>
<tr><td>Transaction Count</td><td colspan=2>31962792</td><td colspan=2>29208876</td></tr>
</tbody>
</table>

## 使用物理复制版本
1. 登录 [TDSQL MySQL版控制台](https://console.cloud.tencent.com/tdsqld/instance-tdmysql)，单击**新建**创建新实例。
2. 在**数据库版本**选择 TPCC 体验。
![](https://qcloudimg.tencent-cloud.cn/raw/bba28928896522fa4b9a181ad6c853a6.png)
3. 购买实例并体验使用。
>? 当前 **TPCC 体验版**由白名单控制开放，如需体验请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行开通。
