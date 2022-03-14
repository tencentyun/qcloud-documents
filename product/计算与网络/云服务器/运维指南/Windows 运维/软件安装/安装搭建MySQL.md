## 操作场景
本文档以 Windows Server 2012 R2 数据中心版 64位中文版操作系统云服务器为例，介绍搭建 MySQL 8.0.19 的具体步骤。
通常情况下 Windows 系统经常使用 SQL Server 数据库，但由于 SQL Server 属于收费产品需要您自行授权，您也可购买 [腾讯云云数据库 TencentDB for SQL Server 实例](http://cloud.tencent.com/product/sqlserver.html)。

## 操作步骤

### 下载 MySQL 安装包
1. 登录云服务器。
2. 在云服务器中打开浏览器，并访问 [MySQL 官网](https://www.mysql.com/) 下载 MySQL 安装包。

### 安装 MySQL 基础环境

1. 双击打开 MySQL 安装包，并在 “Choosing a Setup Type” 安装界面，选择 **Developer Default**，单击 **Next**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/46578b0e47c0a8283c72680070578916.png)
2. 在 “Check Requirements” 安装界面，单击 **Execute**，并根据界面提示配置 MySQL 的基础环境。
3. 单击 **Next**。
4. 在 “Installation” 安装界面，单击 **Execute**，安装 MySQL 所需的安装包。
5. 待 MySQL 所需的安装包完成安装后，单击 **Next**，进入 “Product Configuration” 配置界面。


###  配置 MySQL

#### 配置 MySQL 服务

1. 在 “Product Configuration” 配置界面，单击 **Next**。
2. 在 “Hight Availability” 界面，选择 **Standalone MySQL Server / Classic MySQL Replication**，单击 **Next**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/821c0ab18a477ffdf3458889ff698b08.png)
3. 在 “Type and Networking” 配置界面，保持默认配置，单击 **Next**。
<dx-alert infotype="explain" title="">
- 默认启用 TCP/IP 网络。
- 默认使用 3306 端口。
</dx-alert>
4. 在 “Authentication Method” 配置界面，选择 <b>Use Legacy Authentication Method(Retain MySQL 5.x Compatibility)</b>，并单击 **Next**。如下图所示：
本文为搭建 WordPress 网站设置该选项，您可按需选择。
![](https://qcloudimg.tencent-cloud.cn/raw/599dff879af20e25ce1d8e7fb5b1a33f.png)
5. 设置 root 密码，单击 **Next**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a85f3a6affb6d71dda27a7a1fe5a5870.png)
6. 在 “Windows Service” 配置界面，保持默认配置，单击 **Next**。如下图所示：
7. 在 “Apply Configuration” 配置界面，单击 **Execute**。
8. 单击 **Finish**，完成 MySQL 服务配置。

#### 配置 MySQL 路由器

1. 在 “Product Configuration” 配置界面，单击 **Next**。
2. 在 “MySQL Router Configuration” 界面，保持默认配置，单击 **Finish**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f13a5db6d40390a3b5c650e00720d587.png)

#### 配置 MySQL 示例

1. 在 “Product Configuration” 配置界面，单击 **Next**。
2. 在 “Connect To Server” 配置界面，输入 root 的密码，单击 **Check**。
3. 待 root 的密码验证成功后，单击 **Next**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5e4157ae76b5ae7aa4f7e9d99f40bfe8.png)
4. 在 “Apply Configuration” 配置界面，单击 **Execute**。
5. 单击 **Finish**，完成 MySQL 示例配置。
6. 在 “Product Configuration” 配置界面，单击 **Next**。
7. 在 “Installation Complete” 界面，根据实际需求，勾选需启动的 MySQL 环境，单击 **Finish**。
   - 若成功打开如下图所示的 MySQL 工作台，即表示 MySQL 安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/7f960c3d6e8c26f9fb68ee9de5d5b96b.png)
   - 若成功打开如下图所示的 MySQL Shell，即表示 MySQL 安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/985d2e239aae0bcc1d84f51e3eecd296.png)


### 添加安全组规则

在已购云服务器实例的安全组入方向添加规则，并放行3306端口。
具体操作，请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。






