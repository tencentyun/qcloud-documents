
## 操作场景
[私有网络](https://cloud.tencent.com/document/product/215/20046)（Virtual Private Cloud，VPC）是一块您在腾讯云上自定义的逻辑隔离网络空间，您可以为云服务器、云数据库等资源构建逻辑隔离的、用户自定义配置的网络空间，以提升用户云上资源的安全性，并满足不同的应用场景需求。

**设备自定义 IP 端口**
自定义主实例 IP：支持在实例详情页自定义主实例 IP 和端口。

## 注意事项
- 切换网络会导致该实例内网 IP 地址变化，旧的 IP 地址会保留3小时可用，3小时后将不可访问，请及时更新客户端程序为新的 IP 地址访问，24小时后旧的 IP 地址将会被彻底销毁。
- 实例隔离之后，所有内网 IP 地址将不可用，即使旧的 IP 地址在保留时间内，也会被立即释放修改，请谨慎操作。

## 操作步骤
1. 登录 [TDSQL PostgreSQL版 控制台](https://console.cloud.tencent.com/tdsqld/tdpg)，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例详情页面。
2. 在实例基本信息的**内网地址**、**端口**后，单击<img src="https://main.qcloudimg.com/raw/788902e3f8c335cf17de420f7181c2a8.png"  style="margin:0;">。
>!修改内网地址和端口会影响正在访问的数据库业务。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1460ac5477a3b419a25389895637d38f.png)
3. 在弹出的对话框，自定义 IP 或端口，确认无误后，单击**确定**。
