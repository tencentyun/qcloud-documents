
## 操作场景

云数据库 Redis 新版本（Redis 4.0标准版和Redis 4.0集群版）能够体验更灵活的规格配置，更高的性能以及更完善的功能。
如果您使用的Redis版本较低，为保证更好的云数据库服务体验，建议您升级至 Redis 的新版本。

| 术语 | 说明 | 
|---------|---------|
| 源实例 | 版本升级的源实例。 | 
| 目标实例 | 版本升级的目标实例。 | 

Redis 4.0标准版介绍请参见 [Redis 标准版](https://cloud.tencent.com/document/product/239/36151)，Redis 4.0集群版介绍请参见 [Redis 集群版](https://cloud.tencent.com/document/product/239/18336)。


>?Redis 实例版本升级通过腾讯云数据传输服务（Data Transmission Service，DTS）以热迁移的方式进行，升级过程中，保证 Redis 实例的业务不停服，实时增量更新数据。

#### 支持场景
- Redis 2.8标准版到 Redis 4.0标准版

支持您将 Redis 2.8标准版版本升级到 Redis 4.0标准版，实现支持多副本，容量和副本扩缩容平滑无闪断，读写分离，可用性极高；主从热备架构，数据实时同步，故障秒级切换。
- Redis 2.8标准版到 Redis 4.0集群版


支持您将 Redis 2.8标准版版本升级到 Redis 4.0集群版，实现支持多副本，集群架构，支持分片扩展，大容量，高性能，支持业务在容量、读性能、写性能三个维度的无感知调整；主从热备架构，数据实时同步，故障秒级切换。
- Redis 4.0标准版到 Redis 4.0集群版


支持您将 Redis 4.0标准版版本升级到 Redis 4.0集群版，实现支持多副本，集群架构，支持分片扩展，大容量，高性能，支持业务在容量、读性能、写性能三个维度的无感知调整；主从热备架构，数据实时同步，故障秒级切换。
#### 支持版本
在云数据库 Redis 实例版本升级时，通过 DTS 进行版本升级功能支持的实例版本如下：
    <table>
    <tr>
    <td colspan=2 align=center>源实例版本</td>
    <td rowspan=2 align=cente>目标实例版本</td>
    </tr>
    <tr>
    <td>2.8标准版</td>
    <td>4.0标准版</td>
    </tr>
    <tr>
    <td>✓</td>
    <td></td>
    <td>4.0标准版</td>
    </tr>
    <tr>
    <td>✓</td>
    <td>✓</td>
    <td>4.0集群版</td>
    </tr>
    </table>
>?  Redis 4.0 标准版的数据库实例，可以通过 DTS 热迁移到另一个 Redis 4.0 标准版的数据库实例，但相同版本数据库实例间的迁移不便称作版本升级。

## 前提条件
- 正常运行状态下的 Redis 源实例；
- 购买的Redis 4.0标准版或Redis 4.0集群版实例。
>? 如果数据量小于12GB，且后续数据增长不超过60GB，QPS 不超过4W，建议选择 Redis 4.0 标准版，否则建议选择  Redis 4.0 集群版，Redis 4.0 集群版不支持事务命令（如果需要事务支持，请选择 Redis 4.0 标准版），您可根据业务实际情况进行选择。

## 操作步骤
1.使用 DTS 进行云实例间的迁移操作，从Redis 源实例至Redis 4.0标准版或者Redis 4.0集群版实例，进行热迁移。

云数据库Redis使用DTS迁移的具体操作请参见 [DTS 迁移](https://cloud.tencent.com/document/product/239/31958)。

2.数据同步完成，由业务侧验证数据后，可根据业务QPS等指标选择时机断开 Redis 源实例连接，将连接切换到 Redis 目标实例，切换方法有2种可供选择：
- 修改 Redis 源实例的 IP 地址并记下其旧 IP地址；修改 Redis 目标实例的网络信息和Redis 源实例处于同一个 VPC 子网和并指定 Redis 目标实例的新 IP 地址为 Redis 源实例的旧 IP 地址，即完成业务切换。
修改网络信息和 IP 地址的具体操作请参见 [配置网络](https://cloud.tencent.com/document/product/239/30910)。
- 将代码中的 Redis 源实例的 IP 更新为 Redis 目标实例的 IP 即可。
