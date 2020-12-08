## 命名空间

Namespace=QCE/POSTGRES

## 监控指标


<table>
<thead>
<tr>
<th>指标英文名</th>
<th>指标中文名</th>
<th>指标含义</th>
<th>单位</th>
<th>维度</th>
</tr>
</thead>
<tbody><tr>
<td>Connections</td>
<td>连接数</td>
<td>实例的活跃连接历史变化趋势</td>
<td>个</td>
<td>resourceId</td>
</tr>
<tr>
<td>Cpu</td>
<td>CPU 利用率</td>
<td>实例 CPU 使用率，由于在闲时采用灵活的 CPU 限制策略，CPU 利用率可能大于100%</td>
<td>%</td>
<td>resourceId</td>
</tr>
<tr>
<td>HitPercent</td>
<td>缓冲区缓存命中率</td>
<td>数据缓存命中率</td>
<td>%</td>
<td>resourceId</td>
</tr>
<tr>
<td>InFlow</td>
<td>输入流量</td>
<td>实例读写输入的流量</td>
<td>KB/秒</td>
<td>resourceId</td>
</tr>
<tr>
<td>OutFlow</td>
<td>输出流量</td>
<td>实例读写输出的流量</td>
<td nowrap="nowrap">KB/秒</td>
<td>resourceId</td>
</tr>
<tr>
<td>Iops</td>
<td>磁盘 IOPS</td>
<td>实例的 IOPS（每秒的请求次数)</td>
<td>次/秒</td>
<td>resourceId</td>
</tr>
<tr>
<td>Memory</td>
<td>内存占用</td>
<td>实例占用内存的可用空间</td>
<td>KB</td>
<td>resourceId</td>
</tr>
<tr>
<td>OtherCalls</td>
<td>其他请求数</td>
<td>除了读和写以外的请求总数（例如 Drop），按分钟累加</td>
<td nowrap="nowrap">次/分钟</td>
<td>resourceId</td>
</tr>
<tr>
<td>Qps</td>
<td>每秒查询数</td>
<td>每秒查询次数</td>
<td>次/秒</td>
<td>resourceId</td>
</tr>
<tr>
<td>WriteCalls</td>
<td>写请求数</td>
<td>写请求每分钟总数</td>
<td>次/分钟</td>
<td>resourceId</td>
</tr>
<tr>
<td>ReadCalls</td>
<td>读请求数</td>
<td>读请求每分钟总数</td>
<td>次/分钟</td>
<td>resourceId</td>
</tr>
<tr>
<td>ReadWriteCalls</td>
<td>读写请求数</td>
<td>读写（增删改查）请求每分钟总数</td>
<td>次/分钟</td>
<td>resourceId</td>
</tr>
<tr>
<td>RemainXid</td>
<td>剩余XID数量</td>
<td>剩余的 Transaction Id 数量，Transaction Id 最大有2^32个，小于1000000建议手工执行 vacuum full</td>
<td>个</td>
<td>resourceId</td>
</tr>
<tr>
<td>SqlRuntimeAvg</td>
<td>平均执行时延</td>
<td>所有 SQL 请求的平均执行时间，不包含事务里面的 SQL</td>
<td>Ms</td>
<td>resourceId</td>
</tr>
<tr>
<td>SqlRuntimeMax</td>
<td>最长TOP10执行时延</td>
<td>执行时间最长的 TOP10 的 SQL 的平均值</td>
<td>Ms</td>
<td>resourceId</td>
</tr>
<tr>
<td>SqlRuntimeMin</td>
<td>最短TOP10执行时延</td>
<td>执行时间最短的 TOP10 的 SQL 的平均值</td>
<td>Ms</td>
<td>resourceId</td>
</tr>
<tr>
<td>Storage</td>
<td>已用存储空间</td>
<td>实例使用储存容量</td>
<td>GB</td>
<td>resourceId</td>
</tr>
<tr>
<td>XlogDiff</td>
<td>主备 XLOG 同步差异</td>
<td>每分钟采样，主备 XLOG 的同步的大小差异，代表着同步的延迟，越小越好</td>
<td>Byte</td>
<td>resourceId</td>
</tr>
<tr>
<td>SlowQueryCnt</td>
<td>慢查询数量</td>
<td>查询时间超过规定时间内（默认为1s）的查询的个数</td>
<td>次</td>
<td>resourceId</td>
</tr>
<tr>
<td>StorageRate</td>
<td>存储空间使用率</td>
<td>实例储存空间使用率</td>
<td>%</td>
<td>resourceId</td>
</tr>
</tbody></table>



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
