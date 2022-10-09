
### TDStore 兼容什么数据库协议？
TDStore 兼容 MySQL8.0 协议，用户可以将其视为一个 MySQL 8.0 实例来使用，但有个别受限的操作，具体请参考 [使用说明](https://cloud.tencent.com/document/product/557/63523)。

### TDStore 的内部架构原理是怎样的？
请参考 [TDStore 引擎介绍](https://cloud.tencent.com/document/product/557/65092)。

### TDStore 支持公网/外网访问吗？
出于安全和性能考虑，TDStore 实例目前仅支持从私有网络 VPC 内网访问。

### 使用轻量应用服务器 Lighthouse 如何连接 TDStore 数据库？
轻量应用服务器 Lighthouse 使用腾讯云自动分配的私有网络 VPC 进行网络隔离，默认情况下内网不与云数据库等其他处于私有网络 VPC 中的腾讯云资源内网互通，需通过关联云联网实现。请参考 [Lighthouse 内网连通性说明](https://cloud.tencent.com/document/product/1207/50103#IntranetUnicom)、[内网互联](https://cloud.tencent.com/document/product/1207/56847)。

### 系统提示"实例版本校验错误；请升级内核至最新版后重试"，需要怎么做？
TDStore 引擎内核在不断迭代升级中，如果您遇到上述系统提示，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云工程师为您升级引擎内核。

