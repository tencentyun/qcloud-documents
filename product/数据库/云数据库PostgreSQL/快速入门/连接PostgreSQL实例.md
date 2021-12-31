您可以使用标准的 SQL 客户端，通过内网地址或外网地址连接到云数据库 PostgreSQL。
- **内网连接**：使用云服务器 CVM 访问自动分配给云数据库的内网地址，这种连接方式使用内网高速网络，延迟低。CVM 和数据库须是同一账号，且同一个[ VPC](https://cloud.tencent.com/document/product/215/20046) 内（保障同一个地域），或同在基础网络内。
>?对于不同的 VPC 下（包括同账号/不同账号，同地域/不同地域）的 CVM 和数据库，内网连接方式请参见 [对等连接](https://cloud.tencent.com/document/product/553/18827)。
- **外网连接**：通过外网地址连接云数据库 PostgreSQL。
>!
>- 外网连接需要开启数据库实例的外网地址，此操作会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网访问的方式来登录数据库。
>- 云数据库外网连接适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。
>- 仅广州、上海、北京、成都、中国香港、硅谷的实例支持开启外网访问地址。

下面介绍如何从 Windows 和Linux 操作系统的 CVM 登录，以内外网两种不同的方式连接云数据库 PostgreSQL。

### Windows 操作系统连接方法
1. [登录到 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764) 或在本地，下载并安装一个标准的 SQL 客户端。
>?本文以 pgAdmin 为例，您可根据自己的系统下载适配版本的安装程序，下载地址请参见https://www.pgadmin.org/download/。
2. 在 pgAdmin 上方选择 **Object** > **Create** > **Server**。
![](https://main.qcloudimg.com/raw/38db0fb15e9de97762362a7afb105796.png)
3. 在 **Create - Server** 对话框，填写名称、主机 IP 地址、端口号、用户名和密码等后，单击 **Save**。
 - 主机 IP 地址和端口号：可至 [PostgreSQL 控制台](https://console.cloud.tencent.com/pgsql)， 实例详情页中的**内网地址**或**外网地址**查看。若外网地址未开启，请参见 [开启外网地址](#kqww) 开启。
>?这里的内网地址为 VIP，是通过接入网关集群统一访问数据库实例，而非直接连接到数据库实例物理机上，因此当主机发生故障或主备切换时，内网 IP 都不会变化。
 - 用户名和密码：使用初始化实例时设置的数据库管理员用户名与密码，如忘记密码，可至 [控制台](https://console.cloud.tencent.com/pgsql) 的帐号管理页重置密码。
![](https://main.qcloudimg.com/raw/ef6b1975a212ee352adda4dd4e1159e7.png)
4. 登录数据库后，在左侧导航选择 **Databases** > **postgres**，可看到连接好的服务器（数据库实例）。
![](https://main.qcloudimg.com/raw/ede1361fb76d38deaf9cf22d3a43e8f3.png)

### Linux 操作系统连接方法
1. [登录到 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936) 或在本地 Linux 服务器中，通过yum 源安装一个 psql 客户端。
2. 安装 psql 客户端可参考 [安装 PostgreSQL 数据库](https://cloud.tencent.com/document/product/409/11642) 的描述来进行安装，安装完成之后 psql 客户端也会同时被安装成功。
3. 执行以下命令登录至 PostgreSQL 数据库。
```
psql -U 用户名 -h 访问地址 -p 端口 -d postgres
```
>?如果是在与数据库同 VPC 的 CVM 中，“访问地址”可直接使用数据库内网地址进行访问；如果是使用互联网中的 Linux 服务器，则“访问地址”需要使用数据库外网地址进行访问。

### [附录：开启外网访问地址](id:kqww)
1. 登录 [PostgreSQL 控制台](https://console.cloud.tencent.com/pgsql)，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例详情页面。
2. 在实例详情页的**基本信息**里找到**外网地址**，单击**开通**。
![](https://main.qcloudimg.com/raw/9ca9cd47bbf25fbbf8af012cafcdcfdf.png)
3. 在弹出的对话框，单击**确定**后，外网开通进入处理状态。
4. 开启成功后，即可在基本信息中查看到外网地址。
