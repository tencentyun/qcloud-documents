## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

Joomla 是使用 PHP 语言及 MySQL 数据库开发的开源内容管理系统，您可通过 Joomla 建立个人网站或功能强大的在线应用。本文介绍如何在腾讯云云服务器（CVM）上通过镜像部署 Joomla 基础管理平台。

## 操作步骤
### 步骤1：创建云服务器时使用 Joomla 镜像

<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 Joomla，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您使用其他地域云服务器进行搭建。
</dx-alert>

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在“镜像”中选择**镜像市场** > **从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
</dx-alert> 
<img src="https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png"/>
3. 在“镜像市场”窗口的搜索框中，输入 Joomla 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px">。如下图所示：
<dx-alert infotype="explain" title="">
单击镜像名可查看镜像详情，本文使用镜像为 [LNMP环境（CentOS7.6 Nginx PHP7.2 内置Joomla）](https://market.cloud.tencent.com/products/16472?productId=16472&_ga=1.121836424.2093467297.1571788865)。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/0491f528a88ebfbaa95bebe862bea6d5.png" style="width: 88%;"></img>
4. 单击**免费使用**。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。

### 步骤2：修改数据库密码
<dx-alert infotype="notice" title="">
镜像中已设置默认数据库密码，为提高数据库安全性，建议执行此步骤修改默认密码。
</dx-alert>

1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a87c24c75bdbcc568a1ab0f1fd62c357.png)
2. 在本地浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/tools/phpMyAdmin
```
3. 输入数据库帐户名及密码，并单击**执行**。如下图所示：
帐户名为 `root`，默认密码为 `joomla@2019`。
![](https://main.qcloudimg.com/raw/7e04ec9d80e569513a8fbe13f2ce27a2.png)
4. 进入 phpMyAdmin 管理页面，单击**修改密码**。如下图所示：
<img src="https://main.qcloudimg.com/raw/8cd53ce1e7aaa1895339a3a0b8c2f1f4.png"/>
5. [](id:step5)在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击**执行**。如下图所示：
<dx-alert infotype="explain" title="">
本文使用自动生成密码，请记录您的数据库密码。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/9a30d91a7ab835f009294f0049899c1e.png"/>

### 步骤3：安装配置 Joomla
1. 在本地浏览器中访问以下地址，即可进入 Joomla 安装页面。
```
http://云服务器实例的公网 IP
```
2. 根据页面上的提示信息进行网站配置，填写完成后单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/be1b9cf8f48e5ddb59ceb4a0545c0d94.png)
3. 在“数据库配置”页面根据以下提示，填写相关信息后单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/45a328a49867931295e0e379ad47a06b.png)
 - **数据库类型**：选择 MySQL(PDO)。
 - **数据库主机名**：输入127.0.0.1。
 - **数据库用户名**：输入 root。
 - **数据库密码**：输入在 [修改密码](#step5) 中已设置的 root 帐户密码，如果您未修，则请输入默认密码 `joomla@2019`。
 - **数据库名称**：自定义，本文以 Joomla 为例。
 其余设置保持默认值。
4. 在“配置概览”页面确认配置，并单击**安装**。如下图所示：
![](https://main.qcloudimg.com/raw/399c145fb0638f3ba7af086c7d371d15.png)
5. 安装成功后，单击**删除 “installation” 目录**。如下图所示：
![](https://main.qcloudimg.com/raw/88821300d63199371f9cb2bd540f6d10.png)
Joomla 基础管理平台已搭建完成，请使用本地浏览器访问以下地址，进行网站访问及管理：
 - 网站前台地址：`http://云服务器实例的公网 IP`
 - 网站后台管理地址：`http://云服务器实例的公网 IP/administrator`

## 相关操作
### Joomla 汉化
您可参考以下步骤对已安装的 Joomla 基础管理平台进行汉化。 
1. 将 Joomla 中文语言包下载至本地。
2. 访问网站后台管理地址，并使用管理员帐户登录。如下图所示：
![](https://main.qcloudimg.com/raw/5c90b6c74d43ece34763015ff3d5222d.png)
3. 选择左侧导航栏中的 **install Extensions** 进入扩展安装页面。
4. 单击 **Or browse for file**，在弹出页面中选择本地已下载的语言包。如下图所示：
![](https://main.qcloudimg.com/raw/67788422ef677ee8c039e749493a6a60.png)
上传成功后，界面如下图所示：
![](https://main.qcloudimg.com/raw/bf315f55924ce54599482cef1a59537c.png)
5. 选择界面上方 **Extensions** > **Languages(s)** > **installed**，进入语言安装界面。如下图所示：
![](https://main.qcloudimg.com/raw/07ed99772a9cba4eff064b9cbba055f4.png)
6. 单击<img src="https://main.qcloudimg.com/raw/7b76d0bf4a03cdc8faa0775a4bf76972.png" style="margin:-3px 0px">，将简体中文设置为默认使用语言。如下图所示：
![](https://main.qcloudimg.com/raw/26254e040f23646d8c7c5c9c91bfc9af.png)
7. 单击页面右上角<img src="https://main.qcloudimg.com/raw/48da0f5df951306d1616ba6b3bea9705.png" style="margin:-3px 0px">，并选择 **Logout** 退出后台管理。
8. 再次访问后台管理地址，选择使用语言为**简体中文**并重新登录。如下图所示：
![](https://main.qcloudimg.com/raw/cc43e51bc18fa8faa9daf8c37e73bced.png)
成功登录后即可开始配置 Joomla 管理平台。如下图所示：
![](https://main.qcloudimg.com/raw/a0530f220f258c37e87649ab26b319fa.png)

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
