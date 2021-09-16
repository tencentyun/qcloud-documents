此文档帮助用户最大程度地安全、可靠地使用云服务器。

## 安全与网络

- **限制访问：**通过使用防火墙（[安全组](https://cloud.tencent.com/document/product/213/12452)）允许受信任的地址访问实例来限制访问，在安全组中配置最严格的规则。例如限制端口访问、IP 地址访问等。
- **安全级别：**创建不同的安全组规则应用于不同安全级别的实例组上，确保运行重要业务的实例无法轻易被外部触达。
- **网络逻辑隔离：**选择使用 [私有网络](https://cloud.tencent.com/document/product/213/5227) 进行逻辑区的划分。
- **账户权限管理：**当对同一组云资源需要多个不同账户控制时，用户可以使用 [策略机制](https://cloud.tencent.com/document/product/598/10601) 控制其对云资源的访问权限。
- **安全登录：**尽量使用 [SSH 密钥](https://cloud.tencent.com/document/product/213/6092) 方式登录用户的 Linux 类型实例。使用 [密码登录](https://cloud.tencent.com/document/product/213/6093) 的实例需要不定期修改密码。

## 存储

- **硬件存储：**对于可靠性要求极高的数据，请使用腾讯云云硬盘保证数据的持久存储可靠性，尽量不要选择 [本地盘](https://cloud.tencent.com/document/product/213/5798)。有关更多信息，请参阅 [云硬盘产品文档](https://cloud.tencent.com/document/product/362)。
- **数据库：**对于访问频繁、容量不稳定的数据库，可使用 [腾讯云云数据库](https://cloud.tencent.com/product/tencentdb-catalog)。

## 备份和恢复

- **同地域备份实例：**可以使用**自定义镜像**以及**云硬盘快照**的方式来备份您的实例与业务数据。详见 [云硬盘快照](https://cloud.tencent.com/document/product/362/5754) 与 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942)。
- **跨地域备份实例：**可以使用 [复制镜像](https://cloud.tencent.com/document/product/213/4943) 跨地域复制与备份实例。
- **屏蔽实例故障：**可以通过 [弹性 IP](https://cloud.tencent.com/document/product/213/5733) 进行域名映射，保证在服务器不可用时能快速将服务 IP 重新指向另一台云服务器实例，从而屏蔽实例故障。

## 监控与告警
- **监控和响应事件：**定期查看监控数据并设置好适当的告警。有关更多信息，请参阅 [云监控产品文档](https://cloud.tencent.com/document/product/248)。
- **突发请求处理：**使用 [弹性伸缩](https://cloud.tencent.com/document/product/377) 能够保证服务峰值中的云服务器稳定，还能自动替换不健康的实例。


