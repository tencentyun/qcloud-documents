云数据库 SQL Server 支持内网和外网两种地址类型，默认提供内网地址供您内部访问实例，如果需要使用外网访问，除了开启外网地址后，通过 Linux 或者 Windows 云服务器连接访问实例，也可通过负载均衡 CLB 开启外网服务进行访问，绑定 CLB 开启外网服务必须配置安全组规则才能访问。

以下为您介绍通过 CLB 开启外网服务，并通过 SQL Server Management Studio（SSMS）连接到实例，运行简单查询的操作。

## 前提条件
已申请使用后端服务功能。
1. 进入 [负载均衡跨地域绑定2.0申请页](https://cloud.tencent.com/apply/p/y72ehzwbwzk)。
2. 根据填好资料，填写完后提交申请。
3. 提交完内测申请后，[提单至 CLB](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=14&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&level3_id=1068&radio_title=%E9%85%8D%E9%A2%9D/%E7%99%BD%E5%90%8D%E5%8D%95&queue=96&scene_code=41669&step=2)，申请使用后端服务功能。
 >? 负载均衡 CLB 实例与 SQL Server 实例在同一 VPC 网络和非同一 VPC 网络为两种场景，需要在提单时分别申请不同的功能支持，请根据您的实际场景，在提单时说明需要开通哪种 VPC 场景下的功能支持。

## 步骤1：新购负载均衡
>?如果在云数据库 SQL Server 同地域已经有负载均衡实例，可以不用购买。
>
进入 [负载均衡购买页](https://buy.cloud.tencent.com/clb)，选择完配置后单击**立即购买**。
>!地域需选择云数据库 SQL Server 所在的地域。


## 步骤2：配置负载均衡
配置负载均衡分为同一 VPC 场景和非同一 VPC 场景，以下分别为您介绍。

### 场景一：负载均衡实例与 SQL Server 实例处于同一 VPC
1. 打开跨 VPC 访问功能（启用后 CLB 支持绑定其他内网 IP）。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在**基本信息**页的**后端服务**处，单击**点击配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/8ff86cded677aded4343f4c8ca94bdd3.png)
c. 在弹出的对话框，单击**提交**即可开启。
![](https://qcloudimg.tencent-cloud.cn/raw/ff42f39084a4c37e6558b44e0c645c57.png)

2.  配置外网监听端口。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在实例管理页面，选择**监听器管理**页，在**TCP/UDP/TCP SSL监听器**下方，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/6ec6c16cd556710910349f961ff49799.png)
c. 在弹出的对话框，逐步完成设置，然后单击**提交**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/43f1a017f94712f93ef80d886a8452d5.png)

### 场景二：负载均衡实例与 SQL Server 实例处于非同一 VPC
1. 打开跨 VPC 访问功能（启用后 CLB 支持绑定其他内网 IP）。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在**基本信息**页的**后端服务**处，单击**点击配置**。
c. 在弹出的对话框，单击**提交**。
d. 提交后在**后端服务**下单击**新增 SNAT IP**。
![](https://qcloudimg.tencent-cloud.cn/raw/812c8baa30cacab6c8a54fdf6aba8d43.png)
e. 在弹窗下选择一个**子网**，然后单击分配 IP 后的**新增**，分配方式可自动填写或手动输入分配的 IP，完成后单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/cedd20ab89c323b32625a72b4a059f58.png)
2.  配置外网监听端口。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在实例管理页面，选择**监听器管理**页，在**TCP/UDP/TCP SSL监听器**下方，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/6ec6c16cd556710910349f961ff49799.png)
c. 在弹出的对话框，逐步完成设置，然后单击**提交**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/43f1a017f94712f93ef80d886a8452d5.png)

## 步骤3：绑定 SQL Server 实例
1. 创建好监听器后，在**监听器管理**页，单击创建好的监听器，然后单击右侧出现的**绑定**。
![](https://qcloudimg.tencent-cloud.cn/raw/3f96c6cc462304f626a1ec4c464b1132.png)
2. 在弹出的对话框，选择目标类型为**其他内网IP**，输入 SQL Server 实例的 IP 地址和端口，单击**确认**完成绑定。
>!登录的账号必须是标准账号（带宽上移），如无法绑定，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 协助处理。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d1f887acdf59375add6c0d13afd08d90.png)

## 步骤4：配置 SQL Server 安全组
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，选择地域，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例管理页面。
2. 在实例管理页面，选择**安全组**页，单击**配置安全组**，配置安全组规则为放通全部端口，确认安全组允许外部 IP 访问，详细配置方法请参见 [配置安全组](https://cloud.tencent.com/document/product/238/43287)。
![](https://qcloudimg.tencent-cloud.cn/raw/9e21be547485994b56ee900b9c04fec6.png)

## 步骤5：通过外网连接 SQL Server 实例
1. 在本地下载并安装 [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)。SQL Server Management Studio 相关介绍请参见 [使用 SQL Server Management Studio](https://docs.microsoft.com/zh-cn/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15)。
2. 本地启动 SQL Server Management Studio。在 **Connect to server**  页面，填写相关信息连接云数据库。单击 **Connect**，稍等几分钟后，SQL Server Management Studio 将连接到您的数据库实例。
![](https://main.qcloudimg.com/raw/14d90aa2eda6c841680f0fdc74db8219.png)
 - **Server type**：选择 Database Engine。
 - **Server name**：CLB 的 IP 地址和端口号，需用英文逗号隔开，例如 `10.0.0.1,4000`。
 -  **Authentication**：选择 SQL Server Authentication。
 -  **Login 和 Password**：在实例**账号管理**页创建账号时，填写的账号名和密码。
3. 连接到数据库后，可以查看到 SQL Server 的标准内置系统数据库（master、model、msdb 和 tempdb）。
![](https://main.qcloudimg.com/raw/c65c02197b506bd5b326128f1a3983a0.png)
4. 现在您可以开始创建自己的数据库并对数据库运行查询。选择 **File** > **New** > **Query with Current Connection**，键入以下 SQL 查询：
```
select @@VERSION
```
运行查询，SQL Server Management Studio 会返回 SQL Server 版的腾讯云云数据库实例。
![](https://qcloudimg.tencent-cloud.cn/raw/620a6143d5687581e9f2892e3fb76130.png)

