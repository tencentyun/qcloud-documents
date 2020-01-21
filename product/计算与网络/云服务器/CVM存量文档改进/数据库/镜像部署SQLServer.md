## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

本文档介绍在 Windows 操作系统的腾讯云云服务器（CVM）上使用镜像部署 SQL Server 数据库。

## 技能要求
腾讯云市场中提供了各个版本的 SQL Server 数据库镜像，如果您不熟悉 SQL Server 数据库的安装或想快速部署所需环境，建议您通过镜像部署。

## 操作步骤
### 步骤1：创建云服务器时部署 SQL Server 数据库
>!如果您想使用已购买的云服务器部署 SQL Server 数据库，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署，部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您使用其他地域云服务器进行搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
>!部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有【镜像市场】，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“镜像市场”窗口的搜索框中，输入 sqlserver 并单击<img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px;">。如下图所示：
>?
>- 本文以下图所示 SQL Server 数据库镜像为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/8a22779d278f2486190ffcffef4b06cd.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。

### 步骤2：登录 SQL Server 数据库
1. 参考 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435) 登录云服务器。
2. 双击 Windows 云服务器界面中的 “” 快捷方式。
