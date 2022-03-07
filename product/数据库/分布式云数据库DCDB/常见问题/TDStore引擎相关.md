
### TDStore 兼容什么数据库协议？
TDStore 兼容 MySQL8.0 协议，用户可以将其视为一个 MySQL 8.0 实例来使用，但有个别受限的操作，具体请参考 [使用说明](https://cloud.tencent.com/document/product/557/63523)。

### TDStore 的内部架构原理是怎样的？
请参考 [TDStore 引擎介绍](https://cloud.tencent.com/document/product/557/65092)。

### TDStore 怎样收费？
TDStore 目前是免费内测期，不收费。内测结束后正式商用前，我们将会通过腾讯云官网控制台等多种方式通知用户。

### 我可以申请多个 TDStore 实例吗？
内测期间，每个用户仅可申请1个 TDStore 试用。如果您的企业需要更多实例，可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=10&level2_id=101&source=0&data_title=TDSQL%20MySQL%E7%89%88&step=1) 申请，我们将有客户专员与您联系。

### 如果 TDStore 的性能达不到我的预期，规格和容量可以调整吗？
内测期间，用户默认申请到的是入门标准规格的 TDStore 实例，此规格的实例可以用于功能验证。如果您的企业需要更高规格的实例（例如进行性能测试），可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=10&level2_id=101&source=0&data_title=TDSQL%20MySQL%E7%89%88&step=1) 申请，我们将有客户专员与您联系。

### TDStore 支持公网/外网访问吗？
出于安全和性能考虑，TDStore 实例目前仅支持从私有网络 VPC 内网访问。

### 使用轻量应用服务器 Lighthouse 如何连接 TDStore 数据库？
轻量应用服务器 Lighthouse 使用腾讯云自动分配的私有网络 VPC 进行网络隔离，默认情况下内网不与云数据库等其他处于私有网络 VPC 中的腾讯云资源内网互通，需通过关联云联网实现。请参考 [Lighthouse 内网连通性说明](https://cloud.tencent.com/document/product/1207/50103#IntranetUnicom)、[内网互联](https://cloud.tencent.com/document/product/1207/56847)。

