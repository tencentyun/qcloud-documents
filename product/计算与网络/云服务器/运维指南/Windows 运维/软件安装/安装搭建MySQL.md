## 操作场景
本文档以 Windows Server 2012 R2 数据中心版 64位中文版操作系统云服务器为例，介绍搭建 MySQL 8.0.19 的具体步骤。
通常情况下 Windows 系统经常使用 SQL Server 数据库，但由于 SQL Server 属于收费产品需要您自行授权，您也可购买 [腾讯云云数据库 TencentDB for SQL Server 实例](http://cloud.tencent.com/product/sqlserver.html)。

## 操作步骤

### 下载 MySQL 安装包
1. 登录云服务器。
2. 在云服务器中打开浏览器，并访问 [MySQL 官网](https://www.mysql.com/) 下载 MySQL 安装包。

### 安装 MySQL 基础环境

1. 双击打开 MySQL 安装包，并在 “Choosing a Setup Type” 安装界面，选择【Developer Default】，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/4077db7bfe9f7b97e1d7ddd649efa966.png)
2. 在 “Check Requirements” 安装界面，单击【Execute】，并根据界面提示配置 MySQL 的基础环境。如下图所示：
![](https://main.qcloudimg.com/raw/16a5f7190d7720562681528072cf8129.png)
3. 单击【Next】。
4. 在 “Installation” 安装界面，单击【Execute】，安装 MySQL 所需的安装包。如下图所示：
![](https://main.qcloudimg.com/raw/1b4a3e338bb816e7c47b4603a7a1dbb4.png)
5. 待 MySQL 所需的安装包完成安装后，单击【Next】，进入 “Product Configuration” 配置界面。


###  配置 MySQL

#### 配置 MySQL 服务

1. 在 “Product Configuration” 配置界面，单击【Next】。
2. 在 “Hight Availability” 界面，选择【Standalone MySQL Server / Classic MySQL Replication】，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/5355f286598388f9e9846bf8122e6d98.png)
3. 在 “Type and Networking” 配置界面，保持默认配置，单击【Next】。如下图所示：
>? 
> - 默认启用 TCP/IP 网络。
> - 默认使用 3306 端口。
> 
![](https://main.qcloudimg.com/raw/fbece2fafb34beb5825ae294a8e214fd.png)
4. 在 “Authentication Method” 配置界面，保持默认配置，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/402624aaf02dce01ca2912d3548c03de.png)
5. 设置 root 密码，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/a0472f0b93c590997e78c2f590a0f901.png)
6. 在 “Windows Service” 配置界面，保持默认配置，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/a85625c446218a275e743ff0ec599ece.png)
7. 在 “Apply Configuration” 配置界面，单击【Execute】。
![](https://main.qcloudimg.com/raw/2ee6000630d88774951ddf8aaea16fbb.png)
8. 单击【Finish】，完成 MySQL 服务配置。

#### 配置 MySQL 路由器

1. 在 “Product Configuration” 配置界面，单击【Next】。
2. 在 “MySQL Router Configuration” 界面，保持默认配置，单击【Finish】。如下图所示：
![](https://main.qcloudimg.com/raw/adece1334b6e1579eb2ace782cf47c59.png)

#### 配置 MySQL 示例

1. 在 “Product Configuration” 配置界面，单击【Next】。
2. 在 “Connect To Server” 配置界面，输入 root 的密码，单击【Check】。如下图所示：
![](https://main.qcloudimg.com/raw/ab8637391012a14ab2e5160c61675912.png)
3. 待 root 的密码验证成功后，单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/bff0aece8da11d15a52f4db91b4d7e69.png)
4. 在 “Apply Configuration” 配置界面，单击【Execute】。
![](https://main.qcloudimg.com/raw/8fe1f90eed50860e064044b314719cf6.png)
5. 单击【Finish】，完成 MySQL 示例配置。
6. 在 “Product Configuration” 配置界面，单击【Next】。
7. 在 “Installation Complete” 界面，根据实际需求，勾选需启动的 MySQL 环境，单击【Finish】。如下图所示：
![](https://main.qcloudimg.com/raw/13f46296b85b00ce7e3bd08be13108c9.png)
 - 若成功打开如下图所示的 MySQL 工作台，即表示 MySQL 安装成功。
![](https://main.qcloudimg.com/raw/288f4cfbf1a9671b73dff64a940e0dc1.png)
 - 若成功打开如下图所示的 MySQL Shell，即表示 MySQL 安装成功。
![](https://main.qcloudimg.com/raw/90b788ffe3a8f92e0e5e70f35fb94356.png)


### 添加安全组规则

在已购云服务器实例的安全组入方向添加规则，并放行3306端口。
具体操作，请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。






