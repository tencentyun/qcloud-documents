
本文介绍在 Windows 本地通过 SQL Server Management Studio（SSMS）连接到 SQL Server 实例，并运行简单查询的操作。

## 连接场景
根据云上数据库实例类型的不同，连接方式也有所差异：
若从本地连接云上双节点（原高可用版/集群版） SQL Server 实例，可通过以下3种方案进行连接。
- 方案1：通过 [VPN](https://cloud.tencent.com/document/product/554/18980) 或 [专线](https://cloud.tencent.com/document/product/216/7557) 或 [云联网](https://cloud.tencent.com/document/product/877/18768) 连接，更安全更稳定。
- 方案2：通过外网连接，可在控制台 [开启外网地址](#kqwwdz) 或 [绑定 CLB 开启外网服务](#CLBKQWW)。
- 方案3：借助 [具有外网 IP 的 Linux 云服务器进行端口映射](#WWIPLJSL)。

若从本地连接单节点（原基础版） SQL Server 实例，可通过以下3种方案进行连接。
- 方案1：通过 [VPN](https://cloud.tencent.com/document/product/554/18980) 或 [专线](https://cloud.tencent.com/document/product/216/7557) 或 [云联网](https://cloud.tencent.com/document/product/877/18768) 连接，更安全更稳定。
- 方案2：通过外网连接，可在控制台 [开启外网地址](#kqwwdz)。
- 方案3：借助 [具有外网 IP 的 Linux 云服务器进行端口映射](https://cloud.tencent.com/document/product/238/11627#WWIPLJSL)。

下文分别介绍如下连接方案：
- 通过控制台开启外网地址，在本地通过 SSMS 连接到 SQL Server 实例。
- 通过绑定 CLB 开启外网服务，在本地通过 SSMS 连接到 SQL Server 实例。
- 借助具有外网 IP 的 Linux 云服务器进行端口映射，在本地通过 SSMS 连接到 SQL Server 实例。

## 通过控制台开启外网地址在本地通过 SSMS 连接到 SQL Server 实例
[](id:kqwwdz)
### 步骤1：开启外网地址
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)。
2. 选择地域，在实例列表单击需要开启外网的实例 ID 或**操作**列的**管理**。
3. 在**实例详情**页的**基本信息** > **外网地址**后，单击**开通**。
4. 在开通外网设置窗口阅读并勾选提示，单击**确定**。
5. 开通成功后，在实例详情页基本信息下查询实例的外网 IP 地址和端口号。
>?关于开启外网详细的注意事项和步骤，可参见 [开启外网地址](https://cloud.tencent.com/document/product/238/77966)。

### 步骤2：通过外网连接 SQL Server 实例
1. 在本地下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15)。
2. 本地启动 SQL Server Management Studio。在 **Connect to server**  页面，填写相关信息连接云数据库。单击 **Connect**，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
 - **Server type**：选择 Database Engine。
 - **Server name**：实例的外网 IP 地址和端口号，需用英文逗号隔开。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例**账号管理**页创建账号时，填写的账号名和密码。
![](https://main.qcloudimg.com/raw/14d90aa2eda6c841680f0fdc74db8219.png)
3. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/c65c02197b506bd5b326128f1a3983a0.png)
4.  现在您可以开始创建自己的数据库并对数据库运行查询。选择 **File** > **New** > **Query with Current Connection**，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](https://qcloudimg.tencent-cloud.cn/raw/620a6143d5687581e9f2892e3fb76130.png)

## [绑定 CLB 开启外网服务在本地通过 SSMS 连接到 SQL Server 实例](id:CLBKQWW)
### 步骤1：新购负载均衡
>?如果在云数据库 SQL Server 同地域已经有负载均衡实例，可以不用购买。
>
进入 [负载均衡购买页](https://buy.cloud.tencent.com/clb)，选择完配置后单击**立即购买**。
>!
>- 地域需选择云数据库 SQL Server 所在的地域。
>- 所属网络，选择和数据库相同的 VPC 或者不同都可以。

### 步骤2：配置负载均衡
1. 打开跨 VPC 访问功能（如果 CLB 和云数据库 SQL Server 在同一个 VPC 可忽略该步骤）。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在**基本信息**页的**后端服务**处，单击**点击配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/8ff86cded677aded4343f4c8ca94bdd3.png)
c. 在弹出的对话框，单击**提交**即可开启。
![](https://qcloudimg.tencent-cloud.cn/raw/ff42f39084a4c37e6558b44e0c645c57.png)

2. 配置外网监听端口。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在实例管理页面，选择**监听器管理**页，在 **TCP/UDP/TCP SSL监听器**下方，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/6ec6c16cd556710910349f961ff49799.png)
c. 在弹出的对话框，逐步完成设置，然后单击**提交**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/43f1a017f94712f93ef80d886a8452d5.png)

### 步骤3：绑定 SQL Server 实例
1. 创建好监听器后，在**监听器管理**页，单击创建好的监听器，然后单击右侧出现的**绑定**。
![](https://qcloudimg.tencent-cloud.cn/raw/3f96c6cc462304f626a1ec4c464b1132.png)
2. 在弹出的对话框，选择目标类型为**其他内网IP**，输入 SQL Server 实例的 IP 地址和端口，单击**确认**完成绑定。
>!登录的账号必须是标准账号（带宽上移），如无法绑定，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 协助处理。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d1f887acdf59375add6c0d13afd08d90.png)

### 步骤4：配置 SQL Server 安全组
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，选择地域，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例管理页面。
2. 在实例管理页面，选择**安全组**页，单击**配置安全组**，配置安全组规则为放通全部端口，确认安全组允许外部 IP 访问，详细配置方法请参见 [配置安全组](https://cloud.tencent.com/document/product/238/43287)。
![](https://qcloudimg.tencent-cloud.cn/raw/9e21be547485994b56ee900b9c04fec6.png)

### 步骤5：通过外网连接 SQL Server 实例
1. 在本地下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15)。
2. 本地启动 SQL Server Management Studio。在 **Connect to server**  页面，填写相关信息连接云数据库。单击 **Connect**，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
 - **Server type**：选择 Database Engine。
 - **Server name**：CLB 的 IP 地址和端口号，需用英文逗号隔开，例如 `10.0.0.1,4000`。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例**账号管理**页创建账号时，填写的账号名和密码。
![](https://main.qcloudimg.com/raw/14d90aa2eda6c841680f0fdc74db8219.png)
3. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/c65c02197b506bd5b326128f1a3983a0.png)
4.  现在您可以开始创建自己的数据库并对数据库运行查询。选择 **File** > **New** > **Query with Current Connection**，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](https://qcloudimg.tencent-cloud.cn/raw/620a6143d5687581e9f2892e3fb76130.png)

## [借助具有外网 IP 的 Linux 云服务器进行端口映射在本地通过 SSMS 连接到 SQL Server 实例](id:WWIPLJSL)

>?
>- 云服务器和云数据库须是同一账号，且同一个 VPC 内（保障同一个地域，不限可用区）。
>- 考虑到数据安全性，云数据库 SQL Server 尚未开放实例外网 IP，如有需求可以利用 SSH2 的端口映射在外网连接实例，并对其进行配置和管理。

1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，在实例详情页查看实例内网 IP 及端口号。该内网 IP 及端口号会在配置端口映射时使用。
![](https://qcloudimg.tencent-cloud.cn/raw/312bfd162a46e436f10106e978532f9e.png)
2. 准备一台具有外网 IP的 Linux 云服务器，请参见 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
3. 在本地使用 SSH 工具（如 SecureCRT 等，本文以 SecureCRT 为例）登录 Linux 云服务器，请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
4. 在 SecureCRT 菜单栏选择 **Options** > **Session Options**，进入会话属性设置。
![](https://main.qcloudimg.com/raw/acbb1ad0a808ac59a0053063b75aab8b.png)
5. 在会话属性设置页，选择 **Connection** > **Port Forwarding** > **Add**，进入配置端口映射页。
![](https://main.qcloudimg.com/raw/05f0cadcda75c6f931f34eb296a5ab6f.png)
6. 在配置端口映射页，配置对应参数。
![](https://main.qcloudimg.com/raw/0ac1295fb04aebff56050b3bc6b32f6e.png)
7. 在本地下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15)。
8. 本地启动 SQL Server Management Studio。在 **Connect to server**  页面，填写相关信息连接云数据库。单击 **Connect**，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
 - **Server type**：选择 Database Engine。
 - **Server name**：本机 IP 地址和端口号，需用英文逗号隔开，例如`10.0.0.1,4000`。端口号需与第6步中配置的端口保持一致。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例**账号管理**页创建账号时，填写的账号名和密码。
![](https://main.qcloudimg.com/raw/14d90aa2eda6c841680f0fdc74db8219.png)
9.  连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/c65c02197b506bd5b326128f1a3983a0.png)
10. 现在您可以开始创建自己的数据库并对数据库运行查询。选择 **File** > **New** > **Query with Current Connection**，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](https://qcloudimg.tencent-cloud.cn/raw/620a6143d5687581e9f2892e3fb76130.png)

