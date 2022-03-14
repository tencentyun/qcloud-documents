## 操作场景
宝塔 Linux 面板（BT-Panel）是一款简单好用的服务器运维面板，支持一键 LAMP、LNMP、集群、监控、网站、FTP、数据库、JAVA 等100多项服务器管理功能，能够极大提升运维管理效率。本文指导您如何在轻量应用服务器上安装和使用宝塔 Linux 面板。


<dx-alert infotype="notice" title="">
宝塔 Linux 面板（BT-Panel）目前已下线，您可使用宝塔 Linux 面板 7.5.2 腾讯云专享版。专享版覆盖普通版所有功能，还默认集成腾讯云对象存储、文件存储、内容分发网络和 DNS 解析插件。详情请参见 [使用宝塔 Linux 面板腾讯云专享版管理服务器](https://cloud.tencent.com/document/product/1207/54078)。
</dx-alert>



## 操作步骤
### 安装和配置宝塔 Linux 面板

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面中单击**新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为**应用镜像** > **宝塔Linux面板 7.2.0**，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
3. 返回轻量应用服务器控制台，待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
4. 选择**防火墙**页签，单击**添加规则**，并根据界面提示放通8888端口。
<dx-alert infotype="notice" title="">
- 为提高宝塔面板安全性，建议将面板默认的8888端口修改为其他端口，您可以登录面板后进行修改。修改后需在轻量应用服务器网络防火墙中放通对应端口，详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 。
- CentOS 系统在安装了宝塔面板后，会默认开启操作系统防火墙（可通过命令行 `systemctl status firewalld.service` 查看）。在完成轻量应用服务器网络防火墙配置后，请参考 [修改安全设置](#updateSafe)，同步在操作系统中放通对应端口。
</dx-alert>
具体操作步骤请参见 <a href="https://cloud.tencent.com/document/product/1207/44577#.E6.B7.BB.E5.8A.A0.E9.98.B2.E7.81.AB.E5.A2.99.E8.A7.84.E5.88.99">添加防火墙规则</a>，添加成功后如下图所示：
<img src="https://main.qcloudimg.com/raw/1a892aa6c6672fa960eb7e79e9a0a507.png"/>
5. 选择**应用管理**页签，进入应用管理详情页。
您可以在此页面查看宝塔 Linux 面板应用的各项配置信息。
![](https://main.qcloudimg.com/raw/bf65068c79b3841b5543e6a90e07afca.png)
6. [](id:step06)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: 0;">，复制获取宝塔 Linux 面板的用户名与密码的命令。
7. 在“应用内软件信息”栏中，单击**登录**。
8. 在弹出的登录窗口中，粘贴 [步骤6](#step06) 获取的命令，按 **Enter**。
9. 复制并记录宝塔 Linux 面板的用户名与密码（即 “username” 和 “password”）。
![](https://qcloudimg.tencent-cloud.cn/raw/cfeecc8912438fd877df507a54ff3f24.png)
10. 关闭登录窗口，并返回该实例的应用管理详情页。
11. 在“应用内软件信息”栏中获取宝塔 Linux 面板的“首页地址”，并使用浏览器访问。如下图所示：
![](https://main.qcloudimg.com/raw/8f90703fc72c53d17aa7fd50f0729809.png)
12. 进入宝塔面板页面，输入记录的用户名与密码（即 “username” 和 “password”），单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/60f0f6af7d4e2d085b142593349903fb.png)
13. 根据实际的业务需求，在面板中选择相关的套件安装和部署网站。
![](https://main.qcloudimg.com/raw/bbc4baa515b594167ef186e910896184.png)

### 使用宝塔 Linux 面板创建网站

您可以通过以下两种方式创建网站：
- **方式一：**在宝塔 Linux 面板的**软件商店**中，选择**应用分类** > **一键部署**。
您可以通过此方式一键部署常用的建站软件，例如一键部署 WordPress、 Discuz 、 ECshop 等。
![](https://main.qcloudimg.com/raw/095c86f45ee522b42c70d8407cfc1e69.png)
- **方式二：**
 1. 在宝塔 Linux 面板的**软件商店**中，选择**应用分类** > **运行环境**，安装您所需要的网站环境。例如安装 LNMP 环境（即安装 Nginx、MySQL、PHP、phpMyAdmin、FTP 等软件）。
 2. 单击**网站**，选择**添加站点**，进行网站创建。
![](https://main.qcloudimg.com/raw/9d93b13f71eafa1898f68f5003e0447f.png)

随后您可以参考 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446) 将域名解析到对应的轻量应用服务器 IP 地址，即可通过域名来访问您新创建的网站。
<dx-alert infotype="explain" title="">
如您使用的轻量应用服务器位于中国内地地域，请参考 [如何快速备案您的网站](https://cloud.tencent.com/document/product/243/39038) 进行网站备案。
</dx-alert>




## 相关操作

### 修改默认配置
在宝塔 Linux 面板的**面板设置**中，建议修改以下默认配置：
- 修改**面板端口**：建议将默认端口8888修改为其他不常用的端口。
<dx-alert infotype="notice" title="">
 修改面板端口后，请前往轻量应用服务器控制台，在对应实例的防火墙中同步更新放行的端口。并参考 [修改安全设置](#updateSafe) 步骤同步更新操作系统端口。
</dx-alert>
- 绑定**域名**：您可以绑定一个域名，后续可以直接通过域名来访问宝塔 Linux 面板。
- 授权 IP：设置访问授权 IP，用户只能通过该 IP 访问宝塔 Linux 面板。
<dx-alert infotype="notice" title="">
 一旦设置了授权 IP，将只有指定 IP 的终端才能访问宝塔 Linux 面板。
</dx-alert>
- 修改**面板用户**和**面板密码**：若修改了宝塔 Linux 面板默认的用户名和密码，请妥善保存。

###  修改安全设置[](id:updateSafe)
在宝塔 Linux 面板的**安全**中，您可以按需对服务器进行安全设置。包含启动/禁用 SSH 、禁用 Ping 、配置操作系统放行端口、配置屏蔽 IP 等，您还可以查看面板操作日志。其中，配置操作系统放行端口步骤如下：
1. 在宝塔 Linux 面板中，选择左侧**安全**。
2. 在“系统安全”页面的“防火墙”中，填写需放行端口号及说明。如下图所示：
![](https://main.qcloudimg.com/raw/866b18637a5587cd09b0919e16aa5f0d.png)
3. 单击**放行**即可放通对应端口。



### 安装软件
在宝塔 Linux 面板的**软件商店**中，您可以快速安装您需要的软件、运行环境以及各类插件。


### 网站迁移
您可参考 [使用宝塔 Linux 面板快速迁移网站](https://cloud.tencent.com/document/product/1207/47412)，快速迁移其他云平台的云服务器中的网站数据至腾讯云轻量应用服务器中。
