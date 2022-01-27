## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

Magento 是使用 PHP 语言开发的开源电子商务平台，是国际电子商务解决方案之一。本文介绍通过在腾讯云云服务器（CVM）上通过 Magento 镜像来部署个人电子商务网站。


## 操作步骤

### 步骤1：创建云服务器时使用 Magento 镜像


<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 Magento 个人网站，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您使用其他地域云服务器进行搭建。
</dx-alert>


1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在“镜像”中选择**镜像市场** > **从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png"/>
3. 在“镜像市场”窗口的搜索框中，输入 Magento 并单击 <image src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px"/>。如下图所示：
<dx-alert infotype="explain" title="">
- 本文以下图所示的 “Magento 开源电子商务系统”为例，您可根据实际需求进行选择。
- 单击镜像名可查看镜像详情。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/b6d9446b7d1b51f9e1a99c7a0dd60f8b.png" style="width: 88%;"><br>
更多关于此镜像信息，请参见 <a href="https://market.cloud.tencent.com/products/24706">Magento 开源电子商务系统(含演示数据)基于LNMP搭建 PHP环境 Redis|CentOS</a>。
4. 单击**免费使用**。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


### 步骤2：登录 Magento 后台管理页面

<dx-alert infotype="explain" title="">
Magento 2.4 版本后官方不再支持 Web 向导模式安装，由于示例镜像使用了 Magento 2.4.1 版本，请在实例创建完毕后等待大约5分钟，完成自动初始化安装。
</dx-alert>


1. 在浏览器中访问以下地址，登录 Magento 后台管理页面。
```
http://云服务器实例的公网 IP/admin
```
2. 在 Magento 后台管理登录页面中，输入管理员帐户及登录密码。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f54e834003dd506be12e8e40125c20da.png)
   - **Username**：请输入 `admin`。
   - **Password**：该镜像管理员密码默认为实例 ID，请前往 [实例](https://console.cloud.tencent.com/cvm/instance/index) 页面获取。
显示如下页面，则表示已成功登录 Magento 后台管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/4382343f2828a736dc8bd53f0ef06ecc.png)

### 后续步骤：访问 Magento 主页面
您可使用本地浏览器访问下列地址，访问 Magento 主页面。
```
http://云服务器实例的公网 IP
```


## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。





