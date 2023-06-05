云数据库 MySQL 支持内网和外网两种地址类型，默认提供内网地址供您内部访问实例，如果需要使用外网访问，除了开启外网地址后，通过 Linux 或者 Windows 云服务器连接访问实例，也可通过负载均衡 CLB 开启外网服务进行访问，通过 CLB 开启外网服务必须配置安全组规则。

以下为您介绍通过 CLB 开启外网服务，并通过 MySQL workbench 连接到实例的方法。

## 前提条件
已申请使用后端服务功能。
1. 进入 [负载均衡跨地域绑定2.0申请页](https://cloud.tencent.com/apply/p/y72ehzwbwzk)。
2. 根据需要填好资料，填写完后提交申请。
3. 提交完内测申请后，[提单至 CLB](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=14&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&level3_id=1068&radio_title=%E9%85%8D%E9%A2%9D/%E7%99%BD%E5%90%8D%E5%8D%95&queue=96&scene_code=41669&step=2)，申请使用后端服务功能。
>?负载均衡 CLB 实例与 MySQL 实例同一 VPC 网络和非同一 VPC 网络为两种场景，需要在提单时分别申请不同的功能支持，请根据您的实际场景，在提单时说明需要开通哪种 VPC 场景下的功能支持。

## 步骤1：新购负载均衡
>?如果在云数据库 MySQL 同地域已经有负载均衡实例，就可以不用购买。
>
进入 [负载均衡购买页](https://buy.cloud.tencent.com/clb)，选择完配置后单击**立即购买**。
>!地域需选择云数据库 MySQL 所在的地域。

## 步骤2：配置负载均衡
配置负载均衡分为同一 VPC 场景和非同一 VPC 场景，以下分别为您介绍。

### 场景一：负载均衡实例与 MySQL 实例处于同一 VPC
1. 打开跨 VPC 访问功能（启用后 CLB 支持绑定其他内网 IP）。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在**基本信息**页的**后端服务**处，单击**点击配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/8ff86cded677aded4343f4c8ca94bdd3.png)
c. 在弹出的对话框，单击**提交**即可开启。
![](https://qcloudimg.tencent-cloud.cn/raw/ff42f39084a4c37e6558b44e0c645c57.png)

2.  配置外网监听端口。
a. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance)，选择地域，在实例管理列表，单击实例 ID，进入实例管理页面。
b. 在实例管理页面，选择**监听器管理**页，在 **TCP/UDP/TCP SSL/QUIC 监听器**下方，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/a9250ae4778876f1726d183eb7ab5c95.png)
c. 在弹出的对话框，逐步完成设置，然后单击**提交**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/43f1a017f94712f93ef80d886a8452d5.png)

### 场景二：负载均衡实例与 MySQL 实例处于非同一 VPC
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
b. 在实例管理页面，选择**监听器管理**页，在 **TCP/UDP/TCP SSL/QUIC 监听器**下方，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/f423d7fdc8b61c1333f9dbc74cc482d6.png)
c. 在弹出的对话框，逐步完成设置，然后单击**提交**即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/43f1a017f94712f93ef80d886a8452d5.png)

## 步骤3：绑定 MySQL 实例
1. 创建好监听器后，在**监听器管理**页，单击创建好的监听器，然后单击右侧出现的**绑定**。
![](https://qcloudimg.tencent-cloud.cn/raw/b9e32c5f4f40458ca096831e6eddeaf8.png)
2. 在弹出的对话框，选择目标类型为 **IP 类型**，输入 MySQL 实例的 IP 地址和端口，单击**确认**完成绑定。
>!登录的账号必须是标准账号（带宽上移），如无法绑定，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 协助处理。
>
![](https://qcloudimg.tencent-cloud.cn/raw/ab458cdef3847d251c416714c98513b5.png)

## 步骤4：配置 MySQL 安全组
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb/instance)，选择地域，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例管理页面。
2. 在实例管理页面，选择**安全组**页，单击**配置安全组**，配置安全组规则为放通全部端口，确认安全组允许外部 IP 访问，详细配置方法请参见 [配置安全组](https://cloud.tencent.com/document/product/236/9537)。
![](https://qcloudimg.tencent-cloud.cn/raw/9e21be547485994b56ee900b9c04fec6.png)

## 步骤5：通过 MySQL Workbench 客户端连接实例
1. 安装 MySQL Workbench，官方下载地址请参见 [MySQL Workbench](https://dev.mysql.com/downloads/) 下载页面。
 1. 进入下载页面后单击 **MySQL Workbench**。
 2. 跳转页面后在 Windows (x86, 64-bit), MSI Installer 后单击 **Downloads**。
 3. 单击 **No thanks, just start my download**。
2. 安装完成后打开 MySQL Workbench，在 MySQL Connections 后单击加号添加待连接的实例信息。
![](https://qcloudimg.tencent-cloud.cn/raw/1bdd5024d708284fd8dc06b2177e0ea6.png)
3. 在弹出的窗口下，完成如下配置后，单击**ok**。
![](https://qcloudimg.tencent-cloud.cn/raw/ec8f7b944542bc28721446a1e2dbede5.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>Connection name</td>
<td>为此连接命名。</td></tr>
<tr>
<td>Connection Method</td>
<td>连接方法，选择 Standard（TCP/IP）。</td></tr>
<tr>
<td>Hostname</td>
<td>输入负载均衡 CLB 实例的地址。在 CLB 实例详情页的基本信息下可查询 VIP 信息。</td></tr>
<tr>
<td>Port</td>
<td>输入负载均衡 CLB 实例的端口。在 CLB 实例详情页 &gt; 监控器管理下可查询 TCP 端口号。</td></tr>
<tr>
<td>Username</td>
<td>输入待连接 MySQL 实例的帐号名。在实例管理页 &gt; 数据库管理 &gt; 帐号管理下创建的帐号。</td></tr>
<tr>
<td>Store in Vault...</td>
<td>输入待连接 MySQL 实例的帐号密码并会保存此密码。Username 填写帐号对应的密码。</td></tr>
</tbody></table>
4. 返回 MySQL Workbench 首页，单击刚创建的待连接实例信息连接到 MySQL 实例。
![](https://qcloudimg.tencent-cloud.cn/raw/04cb6e563f25bedcaad235be50890aec.png)
5. 成功连接后的界面如下所示。
![](https://qcloudimg.tencent-cloud.cn/raw/ad6c60db6691f5b2f825d36362877fe7.png)
