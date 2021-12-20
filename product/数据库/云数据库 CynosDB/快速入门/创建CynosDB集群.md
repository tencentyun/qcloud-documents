
本文为您介绍通过云原生数据库 TDSQL-C 控制台创建集群的操作。

## 前提条件
购买前需要实名认证，请参见 [实名认证指引](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
1. 登录 [TDSQL-C 购买页](https://buy.cloud.tencent.com/cynosdb?regionId=8)，选择所要部署的地域、可用区以及数据库规格等，单击**立即购买**。
 - **计费模式**：支持包年包月、按量计费、Serverless 模式。
 - **网络**：出于性能安全考虑，目前仅支持私有网络（VPC），云服务器需要与 TDSQL-C 在同一 [VPC](https://cloud.tencent.com/document/product/215) 下方可通信。
 - **兼容数据库**：支持 MySQL 5.7、8.0 和 PostgreSQL 10。
 - **计算实例数**：建议至少选择两个实例保证集群高可用，集群创建后可通过增加只读实例扩展集群的读能力。
 - **实例规格**：数据库规格和价格请参见 [计费概述](https://cloud.tencent.com/document/product/1003/30493)。
 - **存储计费**：
    - 支持按量计费，即购买时无需指定存储，TDSQL-C 按每小时存储实际使用量计费。
    - 支持包年包月，即预购存储空间，未使用部分仍然计费。
>?仅 TDSQL-C for MySQL 支持选择预购存储空间，且仅在 TDSQL-C for MySQL 选择包年包月计费模式后，存储才能选择预购存储空间包年包月计费模式。
![](https://main.qcloudimg.com/raw/7147f31f66d003d0e4824456015480ee.png)
 - **项目**：选择数据库所属的项目，缺省设置为默认项目。
 - **购买数量**：在每个可用区，每个用户可购买的 TDSQL-C 集群（按量计费模式）总数量不超过10个。
>?当集群存储数据量超过最大存储空间时，集群仅能读取数据不能写入，用户可以选择删除冗余数据或者升级规格。
>
2. 购买成功后，返回集群列表，待集群状态显示为**运行中**，即可正常使用。

## 后续操作
购买 TDSQL-C 集群后，可通过集群内外网地址或数据管理平台连接 TDSQL-C 集群，请参见 [连接 TDSQL-C 集群](https://cloud.tencent.com/document/product/1003/37907)。
