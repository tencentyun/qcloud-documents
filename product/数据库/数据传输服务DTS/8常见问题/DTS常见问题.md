### 什么是数据传输服务 DTS?
数据传输服务（TencentDB Service for Transmission，DTS）是提供数据迁移、数据同步、数据订阅于一体的数据库数据传输服务，帮助您在业务不停服的前提下轻松完成数据库迁移，利用实时同步通道轻松构建异地容灾的高可用数据库架构。

### 如何使用 DTS？
使用 DTS 可将数据一次性迁移到基于腾讯云数据库，也可以进行持续的数据复制。DTS 会捕获来源数据库的变更，并将它们以事务一致的方式应用到目标。数据复制方法请参见 [数据订阅](https://cloud.tencent.com/document/product/571/8774)。

### DTS 支持哪些来源和目标？
腾讯云 DTS 目前支持来自有公网 IP 的 MySQL、云服务器上自建的 MySQL、专线接入的 MySQL、VPN 接入的 MySQL、TencentDB for MySQL 的源数据库，以及 TencentDB for MySQL 的目标数据库。
