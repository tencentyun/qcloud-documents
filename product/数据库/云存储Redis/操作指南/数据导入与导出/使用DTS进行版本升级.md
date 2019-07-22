
## 操作场景

云数据库 Redis 新版本（Redis 4.0标准版和Redis 4.0集群版）能够体验更灵活的规格配置，更高的性能以及更完善的功能。
如果您使用的Redis版本较低，为保证更好的云数据库服务体验，建议您升级至 Redis 的新版本。

Redis 4.0标准版介绍请参见 [Redis 标准版](https://cloud.tencent.com/document/product/239/36151)，Redis 4.0集群版介绍请参见 [Redis 集群版](https://cloud.tencent.com/document/product/239/18336)。


>?Redis 旧版本实例通过腾讯云数据传输服务（Data Transmission Service，DTS）以热迁移的方式进行版本升级，升级过程中，保证 Redis 实例的业务不停服，实时增量更新数据。

#### 支持版本
在云数据库 Redis 实例版本升级时，通过 DTS 进行版本升级功能支持的具体实例版本如下：
    <table>
    <tr>
    <td colspan=2 align=center>旧版本实例</td>
    <td rowspan=2 align=cente>新版本实例</td>
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
- 正常运行状态下的 Redis 旧版本实例；
- 购买的Redis 4.0标准版或Redis 4.0集群版实例。
>? 如果数据量小于12GB，且后续数据增长不超过60GB，QPS 不超过4W，建议选择 Redis 4.0 标准版，否则建议选择  Redis 4.0 集群版，Redis 4.0 集群版不支持事务命令（如果需要事务支持，请选择 Redis 4.0 标准版），您可根据业务实际情况进行选择。

## 操作步骤
1.使用 DTS 进行云实例间的迁移操作，从Redis 旧版本实例至Redis 4.0标准版或者Redis 4.0集群版实例，进行热迁移。

云数据库Redis使用DTS迁移的具体操作请参见 [DTS 迁移](https://cloud.tencent.com/document/product/239/31958)。

2.数据同步完成，由业务侧验证数据后，可根据业务QPS等指标选择时机断开 Redis 旧版本实例连接，将连接切换到 Redis 新版本实例，切换方法有2种可供选择：
- 修改 Redis 旧版本实例的 IP 地址并记下其旧 IP地址；修改 Redis 新版本实例的网络信息和Redis 旧版本实例处于同一个 VPC 子网和并指定 Redis 新版本实例的新 IP 地址为 Redis 旧版本实例的旧 IP 地址，即完成业务切换。
修改网络信息和 IP 地址的具体操作请参见 [配置网络](https://cloud.tencent.com/document/product/239/30910)。
- 将代码中的 Redis 旧版本实例的 IP 更新为 Redis 新版本实例的 IP 即可。
