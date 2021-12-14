## 操作场景
本文档介绍如何在云服务器实例上搭建 Microsoft SharePoint 2016。

## 示例软件版本
本文在示例步骤中使用的云服务器实例硬件规格如下：
- vCPU：4核
- 内存： 8GB

本文在示例步骤中使用如下软件版本：
- 操作系统：Windows Server 2012 R2 数据中心版 64位中文版
- 数据库：SQL Server 2014

## 前提条件
已购买 Windows 云服务器。如果您还未购买云服务器，请参考 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。

## 操作步骤

### 步骤1：登录 Windows 实例
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)。您也可以根据实际操作习惯，[使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。


### 步骤2：添加 AD、DHCP、DNS、IIS 服务[](id:AddAD_DHCP_DNS_IIS)
1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;"></img>，打开服务器管理器。
2. 在左侧导航栏中，选择**本地服务器**，找到 **IE 增强的安全配置**。如下图所示：
![](https://main.qcloudimg.com/raw/9192efa291cfbed136db9a6e3a7c3e59.png)
3. 关闭 **IE 增强的安全配置**。如下图所示：
![](https://main.qcloudimg.com/raw/8b860bb5dfc44ec4993c3a899058b1ae.png)
4. 在左侧导航栏中，选择**仪表盘**，单击**添加角色和功能**，打开 “添加角色和功能向导” 窗口。
5. 在 “添加角色和功能向导” 窗口中，保持默认配置，连续单击3次**下一步**。
6. 在 “选择服务器角色” 界面，勾选 **Active Directory 域服务**、**DHCP 服务器**、**DNS 服务器**和 **Web 服务器(IIS)**，并在弹出的窗口中单击**添加功能**。如下图所示：
![](https://main.qcloudimg.com/raw/532dc46bf0682427e9b210bf36e1986f.png)
7. 单击**下一步**。
8. 在 “选择功能” 界面，勾选“.NET Framework 3.5 功能”，并在弹出的窗口中单击**添加功能**。如下图所示：
![](https://main.qcloudimg.com/raw/44998bf3effff6bec51ea9c502ec8c9a.png)
9. 保持默认配置，连续单击6次**下一步**。
10. 确认安装信息，单击**安装**。
11. 待完成安装后，重启云服务器。
12. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;"></img>，打开服务器管理器。
13. 在服务器管理器窗口中，单击 <img src="https://main.qcloudimg.com/raw/b7b26ebdfecb3b158adac1a37d7a23f3.png" style="margin: 0;"></img>，选择**将此服务器提升为域控制器**。如下图所示：
![](https://main.qcloudimg.com/raw/03def6c00f1bed979c9dde28ebbd2202.png)
14. [](id:step14)在打开的 “Active Directory 域服务配置向导” 窗口中，将 “选择部署操作” 设置为**添加新林**，输入根域名，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/adb2e7cbed1580eebeb201d837f41efa.png)
15. [](id:step15)设置目录服务还原模式（DSRM）密码，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/dc24edd5f6d194cacc7b6ff8511417b7.png)
16. 保持默认配置，连续单击4次**下一步**。
17. 单击**安装**。
18. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;"></img>，打开服务器管理器。
19. 在服务器管理器窗口中，单击 <img src="https://main.qcloudimg.com/raw/b7b26ebdfecb3b158adac1a37d7a23f3.png" style="margin: 0;"></img>，选择**完成 DHCP 配置**。如下图所示：
![](https://main.qcloudimg.com/raw/132eb061b6fd53da22b6211fd2411537.png)
20. 在打开的 “DHCP 安装后配置向导” 窗口中，单击**下一步**。
21. 保持默认配置，单击**提交**，完成安装配置。如下图所示：
![](https://main.qcloudimg.com/raw/6dab6c5968282757ff2e146c74765772.png)
22. 单击**关闭**，关闭向导窗口。

### 步骤3：安装数据库 SQL Server 2014

1. 在云服务器中打开浏览器，并访问 SQL Server 2014 官网下载 SQL Server 2014 安装包。
<dx-alert infotype="explain" title="">
您也可以通过第三方网站或其他合法渠道获取 SQL Server 2014 安装包。
</dx-alert>
2. 双击打开 “Setup.exe” 文件，打开 SQL Server 安装向导，并进入安装选项卡界面。如下图所示：
![](https://main.qcloudimg.com/raw/66c2d6df469197d5550ce2fbae3cc5c9.png)
3. 单击**全新 SQL Server 独立安装或向现有安装添加功能**。
4. 输入产品密钥，单击**下一步**。
5. 勾选“我接受许可条款”，单击**下一步**。
6. 保持默认配置，单击**下一步**。
7. 完成安装检查，单击**下一步**。
8. 保持默认配置，单击**下一步**。
9. 在 “功能选择” 界面，单击**全选**，选中全部功能，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/15bb32c2d2121aadc092428911cefc16.png)
10. 在 “实例配置” 界面，选择**默认实例**，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/3663ca417620325c7b45bc8c60996db7.png)
11. 在 “服务器配置” 界面，配置 SQL Server 数据库引擎服务和 SQL Server Analysis Services 服务的帐号和密码，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/c0bb2b960115d66eda4e38b40a56fc78.png)
 - 将 “SQL Server 数据库引擎” 的帐户名设置为 “NT AUTHORITY\NETWORK SERVICE”。
 - 将 “SQL Server Analysis Services” 的帐户名和密码设置为 [步骤2：添加 AD、DHCP、DNS、IIS 服务](#AddAD_DHCP_DNS_IIS) 中 [14](#step14) - [15](#step15) 设置的域账户及密码。
12. 在 “数据库引擎” 界面，单击**添加当前用户**，将当前帐号作为 SQL Server 的管理员帐号，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/c0218409bfb7044221cb6c0fe1862588.png)
13. 在 “Analysis Services 配置” 界面，单击**添加当前用户**，为当前帐号添加 Analysis Services 的管理员权限，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/43243a387cc67f20ea125fb2491df24d.png)
14. 保持默认配置，单击**下一步**。
15. 在 “Distributed Replay 控制器” 界面，单击**添加当前用户**，为当前帐号添加 Distributed Replay 控制器的权限，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/46158b2f9a6e5f802c2ae27a2f5f0970.png)
16. 保持默认配置，单击**下一步**。
17. 确认 SQL Server 配置，单击**安装**。
18. 待 SQL Server 安装完成后，单击**关闭**。


### 步骤4：安装 SharePoint 2016

1. 在云服务器中打开浏览器，并访问 Microsoft SharePoint 2016 官网下载 Microsoft SharePoint 2016 安装包。
2. 打开 Microsoft SharePoint 2016 镜像文件，双击准备工具的可执行文件 `prerequisiteinstaller.exe`，安装 Microsoft SharePoint 2016 准备工具。如下图所示：
![](https://main.qcloudimg.com/raw/2de50f6a3172bd870f86378e33f1f07e.png)
3. 在打开的 Microsoft SharePoint 2016 产品准备工具向导窗口中，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/e5cd9c8ca37b36984258050443fdf5f1.png)
4. 勾选“我接受许可协议的条款”，单击**下一步**。
5. 等待完成安装必备组件，单击**完成**，重启云服务器。如下图所示：
![](https://main.qcloudimg.com/raw/cc8f3bf7b151946d5fdd8f3882ea9549.png)
6. 打开 Microsoft SharePoint 2016 镜像文件，双击安装文件 `setup.exe`，开始安装 Microsoft SharePoint 2016。如下图所示：
![](https://main.qcloudimg.com/raw/bf0369e20c77e1f57bfef3fef42fab31.png)
7. 输入产品密钥，单击**继续**。
8. 勾选“我接受此协议的条款”，单击**继续**。
9. 选择安装目录（本示例中保持默认设置，您可以根据实际情况选择相应安装目录），单击**立即安装**。如下图所示：
![](https://main.qcloudimg.com/raw/0dbdfedb241b02a7f2fdaefb1a7599af.png)
10. 待安装完成后，勾选“立即运行 SharePoint 产品配置向导”，单击**关闭**。如下图所示：
![](https://main.qcloudimg.com/raw/3fa47faa1f8bed1a8ec478260ee64481.png)

### 步骤5：配置 SharePoint 2016

1. 在运行的 SharePoint 产品配置向导中，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/3e8d015ab34ab8de8172838dd21d31ac.png)
2. 在弹出的提示框中，单击**是**，允许在配置过程中重启服务。
3. 选择**创建新的服务器场**，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/f87545fb79d747bf64c38131fbb318d4.png)
4. 配置数据库设置和指定数据库访问账户信息，单击**下一步**。如下图所示：
由于 Sharepoint 的数据库在本机，所以填写本机的数据库及帐户。
![](https://main.qcloudimg.com/raw/cf9723c7885399e0e5004f1ecee4ea2d.png)
5. 配置指定服务器场的密码，单击**下一步**。
6. 将 “多服务器场” 设置为**前端**，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/95da6977363606dd62835d12bc9b7ae2.png)
7. 设置 Sharepoint 管理中心的端口号（本示例以10000端口号为例，您可以根据实际情况设置端口号），单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/26ef65e1e8e229e9c67c2eafc40c0d32.png)
8. 查看并确认 Sharepoint 配置，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/a0e8ee05fcc2fc4b6f717bb0e03287af.png)
9. 待 Sharepoint 完成配置后，单击**完成**。





