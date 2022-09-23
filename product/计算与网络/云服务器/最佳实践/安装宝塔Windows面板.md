## 操作场景
宝塔面板是一款使用方便、功能强大、交互友好且终身免费的服务器管理软件，支持 Linux 与 Windows 系统。在宝塔面板中，您可以一键配置 LAMP、LNMP、网站、数据库、FTP、SSL，还可以通过 Web 端轻松管理服务器。

本文介绍如何在 Windows 操作系统的云服务器上通过腾讯云市场镜像快速安装宝塔面板。


## 操作步骤

### 创建云服务器时安装宝塔面板


<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部安装宝塔面板，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择镜像市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过镜像市场重装系统，建议您使用其他地域云服务器进行搭建，或前往 [宝塔面板官网](https://www.bt.cn/)  获取更多安装信息。
</dx-alert>

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在“镜像”中选择**镜像市场** > **从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
- 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
- 建议选择内存大于2GB，系统盘容量大于40GB的实例配置。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png"/>
3. 在“镜像市场”窗口的搜索框中，选择**运维工具**，输入“宝塔”并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px">。
4. 按需选择镜像，本文以选择 **[宝塔Windows面板官方版（WAMP/WNMP/Tomcat/Node.js）](https://market.cloud.tencent.com/products/31884)** 为例，单击**免费使用**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d6152c2ba86ed0225e830e5df6898a58.png)
5. 在实例关联的安全组需添加放通8888端口的入站规则，详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。
存储介质、带宽等其他配置请根据实际需求选择，最终选择购买完成宝塔面板搭建。


### 获取面板登录信息
1. 登录云服务器，详情请参见 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
2. 在操作系统界面中，右键单击左下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/c6e9910fc4f983d45729b4f6924e8273.png" style="margin:-3px 0px">，并在弹出菜单中单击**运行**。
3. 在 cmd 窗口中执行以下命令，获取登录信息。
```
bt default
```
返回结果如下图所示，请记录宝塔面板地址及登录信息。
![](https://qcloudimg.tencent-cloud.cn/raw/ad3ab06a63ee68bfffdc340ced45c532.png)


### 登录宝塔面板
1. 在本地计算机中，打开浏览器，访问已获取的宝塔面板地址。
```shell
http://云服务器公网 IP:8888/xxxx
```
2. 输入记录的 “username” 和 “password”，单击**登录**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2047353089c078d898de93d01313174f.png)
3. 勾选“我已同意《用户协议》”，单击**进入面板**。
4. 根据实际的业务需求，在面板中选择相关的套件安装和部署网站。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5b6d49694bf924d2edbdb98559d192cc.png)
