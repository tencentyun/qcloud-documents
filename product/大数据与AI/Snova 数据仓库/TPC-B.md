## 测试说明
云数据仓库 PostgreSQL 最新版本封装了 Greenplum 6.x 版本，相比于 5.x 版本，极大的改进了多并发场景下的增删改查能力，即 OLTP 能力，这些改进包括：
1. 合并 PostgreSQL 内核至9.4，引入 fastpath 等锁优化。
2. 提供全局死锁检测。
3. 优化全局事务。
 
Greenplum 官方采用 [TPC-B](http://www.tpc.org/tpcb/) 测试 6.x 的 OLTP 能力，因此云数据仓库 PostgreSQL 也采用此 benchmark 进行测试。

## 测试环境
云数据仓库 PostgreSQL 分为**计算密集型**和**存储密集型**，其简单区别如下：
- 计算密集型：底层硬件为 SSD 盘，随机读写能力强，适合进行热数据分析，以及带有混合负载的场景。
- 存储密集型：底层硬件为 HDD 盘，随机读写能力一般，但是磁盘容量较大，适合存储分析较大规模的历史数据。

综上，测试 TPC-B，需要选择**计算密集型**机型，我们选择2个节点的 nc2.large，可直接在 [购买页](https://buy.cloud.tencent.com/snova#/) 购买。

## 测试工具
使用 PostgreSQL 自带的 pgbench 工具进行测试。
1. 如果测试环境是 CentOS 7.X，可以直接在此处下载已经编译好的工具 [pgbench](https://packagedown-online-1256722404.cos.ap-guangzhou.myqcloud.com/pgbench/pgbench)。
2. 其它环境可以自行编译 PostgreSQL 或者直接安装二进制包，为了更好的兼容性，建议采用 PostgreSQL9.4 版本。

## 测试步骤
### 创建测试数据库
```
CREATE DATABASE pgbench;
```

### 修改查询优化器
```
ALTER DATABASE pgbench SET optimizer = off;
```
>?
>1. 云数据仓库 PostgreSQL 内置2种查询优化器，GPORCA 和 Postgres Planner，其中 GPORCA 是默认的，适合复杂查询的解析；对于 OLTP 类型的查询，需要使用 Postgres Planner。
>2. 该参数也支持 session 级别的设置，这里为了方便，直接在数据库级别设置，也就是对于该数据库的访问，都是使用 Postgres Planner，而其它数据库仍使用 GPORCA。

### 初始化测试数据
```
./pgbench -i pgbench -s 100 -p 5436 -h {host} -U {user} pgbench
```
>?此处测试1000W的数据。

### 运行测试脚本
```
./pgbench -h {host} -p 5436 -r -n -c 32 -j 32 -T 120 -P 1 -U {user} pgbench
```

## 优化
根据 Greenplum 官方数据，6.x 在理想环境下能达到5000左右的 TPS，在云数据仓库 PostgreSQL 上实测可以达到更高的数据，不过需要调整一些配置，如下：
<table>
	<thead>
	<tr>
	<th>参数</th>
  <th>值</th>
	<th>说明</th>
	</tr>
	</thead>
<tbody>
	<tr>
		<td>log_statement</td>
    <td>none</td>
		<td>关闭 master 节点的日志输出</td>
	</tr>
	<tr>
		<td>gp_enable_fast_sri</td>
		<td>on</td>
		<td>提高单条 insert 的效率</td>
	</tr>
	<tr>
		<td>gp_enable_gpperfmon</td>
		<td>off</td>
		<td>关闭监控采样</td>
	</tr>
</tbody>
</table>

>?
>1. 除上述配置外，还需关闭 master 的备节点以达到最佳性能。
>2. 上述配置主要用于测试云数据仓库 PostgreSQL 的极限性能，在实际生产环境中，不建议做上述修改。
>2. 由于目前云数据仓库 PostgreSQL 还未提供配置修改功能，用户如果希望进行测试，可以 [联系我们](https://cloud.tencent.com/document/product/878/45996) 进行修改，修改后需要重启集群。


