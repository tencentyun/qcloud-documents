在本文档中，您可以创建 PostgreSQL 云数据库实例并连接到该数据库实例。最后，您将删除该数据库实例。

> **注意：**
> 在创建 PostgreSQL 云数据库实例之前，您必须拥有一个腾讯云帐户。如果您没有腾讯云帐户，请在 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云帐户。

## 一、创建 PostgreSQL 云数据库实例
在此步骤中，您会使用腾讯云控制台创建 PostgreSQL 云数据库实例。
1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb)。
![](//mc.qcloudimg.com/static/img/7f454c8f988ec22c4045b33c47571024/image.png)
2. 在右侧导航栏选择需要创建的云数据库类型，这里选择【PostgreSQL】。单击【+新建】，进入 PostgreSQL 云数据库购买界面。
![](//mc.qcloudimg.com/static/img/f57f66cceeca480952916d836f7908a5/image.png)
3. 在 PostgreSQL 云数据库购买界面中，选择数据库相关配置。确认无误后，单击【立即购买】。
 - 计费模式。目前只支持包年包月。
 - 地域和可用区。本教程以“广州”和“广州三区”为例。地域说明请参见 [地域与可用区](/doc/product/236/8458)。
 - 网络类型。支持基础网络和私有网络。本教程以“基础网络”为例。基础网络和私有网络的区别请参见 [网络类型](/doc/product/213/5227)。
 - 数据库版本。提供 PostgreSQL 9.3.5 和 PostgreSQL 9.5.4 两个版本。不同可用区可能有所不同，具体以实际情况为准。本教程以“PostgreSQL 9.5.4”为例。
 - 实例规格和所需的硬盘。
 - 购买数量和购买时长。
 ![](//mc.qcloudimg.com/static/img/90a26e59a3f499409592b1389dc976bb/image.png)
4. 进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，选择【PostgreSQL】，查看刚才创建的云数据库实例。状态显示是 **待初始化**。
![](//mc.qcloudimg.com/static/img/e0fbab1eb77b29a8eae650ec8224a3eb/image.png)
5. 单击【初始化】，弹出初始化配置窗口，进行云数据库初始化操作。
![](//mc.qcloudimg.com/static/img/d745d2fc8bc465594da63c5cf9be46f6/image.png)
6. 配置初始化参数，确认无误后，单击【确定】。初始化需要一定的时间，请耐心等待。当状态显示 **运行中**，表示云数据库初始化成功。
 - 管理员用户名和密码。本教程以“test”为例。**此步骤填写的管理员用户名和密码将在连接 PostgreSQL 云数据库时使用，请妥善保管。**
 - 支持的字符集。提供 UTF8 和 LANTIN1 两种字符集。本教程以 UTF8 为例。

 ![](//mc.qcloudimg.com/static/img/341efb01ff99b57fbd928ffc2f43d39c/image.png)
7. 在  PostgreSQL 云数据库管理界面，单击【管理】，进入  PostgreSQL 云数据库实例详情页。
![](//mc.qcloudimg.com/static/img/828816fa32e3469697c956761291552b/image.png)
8. 在 PostgreSQL 云数据库实例详情页，开通外网地址。当您需要从外网访问云数据库时，本步骤必选。其他情况下，本步骤可选。
![](//mc.qcloudimg.com/static/img/dc3bd909a53992bcecc1ab58a5bfea83/image.png)
> **注意：**
> 长期开放数据库外网 IP 可能存在安全风险，建议您在不需使用时及时关闭。
9. 在 PostgreSQL 云数据库实例详情页，查看内网地址和外网地址。**内网地址和外网地址会在后续连接服务器时使用。**
![](//mc.qcloudimg.com/static/img/4139ef19afc83751f6bcef1e62ff4934/image.png)


## 二、连接 PostgreSQL 云数据库实例
当您的数据库实例初始化后，您可以使用任何标准的 SQL 客户端连接到该实例。本教程以 pgAdmin 为例进行说明。
### 1. 下载并安装 pgAdmin
您可以从 [pgAdmin 的官方网站](https://www.pgadmin.org/download/) 下载并安装 pgAdmin。本教程以 pgAdmin4 为例进行说明。
### 2. 新建数据库连接
安装好 pgAdmin4 后，打开客户端。右键单击【Servers】>【Create】>【Server】。
![](//mc.qcloudimg.com/static/img/d858eff4877223e5e8749a0a0e3aa193/image.png)
在弹出的 **Create-Server** 对话框的【General】和【Connection】子菜单项中填写名称、主机 IP 地址、端口号、用户名和密码，新建数据库连接并单击【Save】保存。
- Name。数据库连接名称。
- Host name/address。云数据库的 IP 地址。分为内网地址和外网地址。如果在外网访问云数据库，请使用外网地址和端口号；如果在内网访问云数据库，请使用内网地址和端口号。
- Port。云数据库的端口号。
- Username。登录云数据库的管理员用户名。本教程中以“test”为例。
- Password。登录云数据库的密码。
![](//mc.qcloudimg.com/static/img/4b491e5ee00e89d6a7252126b0229971/image.png)
![](//mc.qcloudimg.com/static/img/350e87013f354317824e02140b177412/image.png)
### 3. 查询数据库版本
连接到数据库后，可以通过执行 SQL 语句查询数据库的版本信息。单击【Tools】>【Query Tool】。
![](//mc.qcloudimg.com/static/img/702f39ba986b7794178f78685f2a32de/image.png)
在弹出的 PSQL CONSOLE 中，运行以下代码查询数据库版本信息。
```
select version()
```
![](//mc.qcloudimg.com/static/img/03f1cbd94d5ec5df154365575a3eb469/image.png)

## 三、删除 PostgreSQL 云数据库实例
PostgreSQL 云数据库实例暂时不支持手动删除，到期后没有续费将会自动停止。

[1]:https://msdn.microsoft.com/zh-cn/library/ms174173(v=sql.105).aspx
