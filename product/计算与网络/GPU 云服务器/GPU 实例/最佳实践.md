## 安全组与网络
- 安全组是一种有状态的提供包过滤功能的虚拟防火墙，用户可通过设置安全组允许受信任的地址访问实例，达到限制访问的目的。创建不同的安全组规则应用于不同安全级别的实例组上，确保运行重要业务的实例无法轻易从外部触达。有关更多信息，请参阅 [安全组](/doc/product/213/5221) 。
- 定期修补，更新和保护实例上的操作系统和应用程序。
- 借助弹性公网 IP 地址，快速将地址重新映射到账户中的另一个实例（或 NAT 网关实例），从而屏蔽实例故障。有关更多信息，请参阅 [弹性 IP 地址](https://cloud.tencent.com/doc/product/213/5733) 。
- 尽量使用 [SSH 密钥](https://cloud.tencent.com/doc/product/213/6092) 方式登录用户的 Linux 类型实例。使用 [密码登录](https://cloud.tencent.com/doc/product/213/6093) 的实例需要不定期修改密码。
- 选择使用 [私有网络](https://cloud.tencent.com/doc/product/213/5227) 进行逻辑区的划分。

## 存储
- 对于可靠性要求极高的数据，请使用 [腾讯云云硬盘](https://cloud.tencent.com/doc/product/362) 以保证数据持久可靠存储。
- 对于访问频繁、容量不稳定的数据库，可使用 [腾讯云云数据库](https://cloud.tencent.com/product/cdb-overview.html) 。
- 利用 [对象存储 COS](https://cloud.tencent.com/product/cos) ，存储静态网页和海量图片、视频等重要数据。

## 备份与恢复
- 通过 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 回滚备份好的 [自定义镜像](https://cloud.tencent.com/doc/product/213/4942) 恢复等方式。
- 跨多个可用区部署应用程序的关键组件，并适当地复制数据。
- 定期查看监控数据并设置好适当的告警。有关更多信息，请参阅 [云监控产品文档](https://cloud.tencent.com/doc/product/248) 。
