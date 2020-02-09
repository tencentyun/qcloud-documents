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

### 步骤2：连接 SQL Server 数据库<sapn id="Step2"></span>
1. 参考 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435) 登录云服务器。
2. 双击 Windows 云服务器界面中的 “SQL Server Management Studio” 快捷方式，打开数据库控制面板。
3. 在弹出的“连接到服务器”窗口中，参考以下信息连接到数据库。如下图所示：
主要参数信息如下，其余配置请保持默认设置：
![](https://main.qcloudimg.com/raw/42581bbace6881dbd36abab63644706d.png)
  - **登录名**：sa。
  - **密码**：本文使用镜像初始密码默认为 `websoft9!`。为保证数据库安全性，请参考 [步骤3](#Step3) 设置自定义密码。
4. 单击【连接】即可成功连接数据库。如下图所示：
![](https://main.qcloudimg.com/raw/f05a7557389ca26ded8a059a5f1dbcb0.png)

### 步骤3：修改数据库连接密码<span id="Step3"></sapn>
1. 成功连接数据库后，选择左侧导航栏中的【安全性】>【登录名】>【sa】。
2. 右键单击【sa】，并选择【属性】。如下图所示：
![](https://main.qcloudimg.com/raw/ffa7876f04ba3e2be31567f098c264eb.png)
3. 在弹出的 “登录属性 - sa” 窗口中，在“密码”中重新输入新密码，并在“确认密码”中再次输入确认密码。
4. 单击【确定】即可成功修改密码。如下图所示：
![](https://main.qcloudimg.com/raw/94b1abbeffcbb4dff84a4118513c9398.png)
5. 当您再次打开此数据库控制面板时，即可参考 [步骤2](#Step2) 使用新密码连接数据库。


## 常见问题
如果您在部署 SQL Server 数据库的过程中遇到问题，可参考以下文档进行分析并解决问题：

- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
