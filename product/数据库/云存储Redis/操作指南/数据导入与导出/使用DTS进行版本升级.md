
## 操作场景
云数据库 Redis [4.0、5.0 内存版（标准架构）](https://cloud.tencent.com/document/product/239/36151) 和 [4.0、5.0 内存版（集群架构）](https://cloud.tencent.com/document/product/239/18336) 提供更灵活的规格配置、更高的性能及更完善的功能。如果您使用的 Redis 版本较低，为保证更好的云数据库服务体验，建议您升级至 Redis 4.0、5.0 版本。

云数据库 Redis 实例版本升级通过数据传输服务 DTS 以热迁移的方式进行，保证升级过程中 Redis 实例业务不停服，能实时增量更新数据。

| 术语 | 说明 | 
|---------|---------|
| 源实例 | 版本升级的源实例 | 
| 目标实例 | 版本升级的目标实例 | 

#### 支持版本
<table>
<tr><td rowspan=2 align=center>源实例版本</td><td colspan=4 align=center>目标实例版本</td></tr>
<tr>
<td>4.0内存版（标准架构）</td><td>4.0内存版（集群架构）</td><td>5.0内存版（标准架构）</td><td>5.0内存版（集群架构）</td></tr>
<tr>
<td>2.8内存版（标准架构）</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr>
<td>4.0内存版（标准架构）</td><td>-</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr>
<td>4.0内存版（集群架构）</td><td>-</td><td>-</td><td>✓</td><td>✓</td></tr>
<tr>
<td>5.0内存版（标准架构）</td><td>-</td><td>-</td><td>-</td><td>✓</td></tr>
</table>

## 前提条件
- 需是正常运行状态下的 Redis 源实例。
- 已购买 Redis 4.0、5.0 内存版（标准架构）或 Redis 4.0、5.0 内存版（集群架构）实例。
>?数据量小于12GB，且后续数据增长不超过60GB，QPS 不超过4W的情况，或是需要事务支持的情况，建议选择 Redis 4.0、5.0 内存版（标准架构），否则建议选择  Redis 4.0、5.0 内存版（集群架构）。

## 操作步骤
1. 使用 DTS 从云数据库 Redis 源实例，迁移数据至 Redis 4.0、5.0 内存版（标准架构）或 Redis 4.0、5.0 内存版（集群架构）实例，请参见 [使用 DTS 进行迁移](https://cloud.tencent.com/document/product/239/31958#1.-.E6.96.B0.E5.BB.BA.E8.BF.81.E7.A7.BB.E4.BB.BB.E5.8A.A1)。
2. 数据同步完成，业务侧验证数据无误后，可根据业务 QPS 等指标选择时间断开 Redis 源实例连接，将连接切换到 Redis 目标实例，切换方法有以下两种：
**登录控制台切换：**
 1) 记录 Redis 源实例的旧 IP 地址并修改 IP 地址。
 2) 修改 Redis 目标实例的网络信息和 Redis 源实例处于同一个 VPC 子网，并将目标实例的 IP 地址修改为源实例的旧 IP 地址，即可完成业务切换。修改网络信息和 IP 地址的具体操作请参见 [配置网络](https://cloud.tencent.com/document/product/239/30910)。
**登录实例切换：**将代码中 Redis 源实例的 IP 更新为 Redis 目标实例的 IP 即可。
