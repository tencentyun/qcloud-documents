本指南将介绍通过腾讯云云服务器 CVM（以下简称 CVM）上安装的 Discuz! 镜像来启动并运行一个论坛网站。您将了解如何配置并启动 CVM 云主机、如何获取 WordPress 用户名和密码，以及如何登录 WordPress 管理页面。
**注意**：本指南主要针对基本的 Discuz! 论坛搭建，适用于个人使用或学习。建议针对具有较高可扩展性需求要求不高的业务级网站使用本教程。要获取更高级的教程，请参阅 [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8044)。

请保持此指南处于打开状态，同时登录到 [腾讯云管理控制台](https://console.cloud.tencent.com/)。
### 步骤一：启动 CVM
通过腾讯云启动 Discuz! 论坛，前提是拥有一台腾讯云的云服务器。
- 若您已拥有 CVM，请跳过此步骤，进入步骤二。
- 若您还未拥有 CVM，请先购买云服务器。请参考 [创建 Linux 云服务器](https://cloud.tencent.com/document/product/213/2972) 进行购买。
购买成功后，系统将会发送一封站内信至您的账户，请打开 [站内信](https://console.cloud.tencent.com/message) 查看您已购买云服务器的信息，并保存好您的云服务器初始账户和密码。
![站内信1](//mc.qcloudimg.com/static/img/2e1ab9f2401d185f34aa8d945caa7f64/image.png)

### 步骤二：配置云主机
1. 登录 [腾讯云管理控制台](https://console.cloud.tencent.com/)，在【云产品】下找到【云服务器】，点击打开云服务器控制台。
2. 为云主机设置名称，便于区分。
 1. 请点击左侧导航【云主机】，进入云主机页面，选定要使用的云主机。点击云主机的 **ID/主机名**，为云主机修改名称。
![改名a1](//mc.qcloudimg.com/static/img/d4774ae98db54049949bdf31a728cbb3/image.png)
 2. 自定义云主机名称（ 如 Discuz!），点击【确定】保存。
![改名b1](//mc.qcloudimg.com/static/img/2b5c816165ad93021a58822a3458f7f2/image.png)
3. 重装系统
 1. 点击【更多】，选择【重装系统】。
![更多1](//mc.qcloudimg.com/static/img/f0a23ee44d129a9e38b86374b5988fab/image.png)
 2. 在出现的**重装系统**提示框中，选择【服务市场】>【建站模板】，安装对应的镜像。本指南中，我们选择的是** Discuz! X3.2官方正式版 ( CentOS 7.2 64位 Webmin | LAMP )**。 **登录设置**选择【密码】，并为 root 账号设置密码。点击【开始重装】进入重装状态。重装可能需要几分钟的时间。
![重装系统1](//mc.qcloudimg.com/static/img/55cb78eb0f0fd8e5cf25db6cddc001ff/image.png)
3. 云主机状态处于运行中时，就可以测试 Discuz! 论坛了。在云主机的 **主 IP 地址** 下，复制云主机的公网 IP。
![运行中1](//mc.qcloudimg.com/static/img/47010295b9fe1b1d80a2c572117f1883/image.png)
4. 将该公网 IP 粘贴到浏览器的地址栏中访问，可以看到安装引导页面。 

### 步骤三：启动 Discuz! 
1. 在安装引导页面，单击  Discuz!【安装配置】进入安装页面。
![安装0](//mc.qcloudimg.com/static/img/9c158431b6de083811f5a93d545309ed/image.png)
2. 单击【我同意】，进入安装步骤第一步：检查安装环境。
![安装1](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
3. 确认当前状态正常，单击【下一步】，进入设置运行环境步骤。
![安装2](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
4. 选择全新安装，单击【下一步】，进入创建数据库步骤。
![安装3](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
5. 为 Discuz! 创建一个数据库，使用镜像默认的 MySQL 账号和密码（默认为 root/123456）连接数据库。并设置好系统信箱、管理员账号、密码和 Email。单击【下一步】，开始安装。
**注意**：请记住自己的管理员账号和密码。
![安装4改](//mc.qcloudimg.com/static/img/5d5184cfb34f98d791c243273b910065/image.png)
6. 安装完成后，单击【您的论坛已完成安装，点此访问】访问论坛。
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)

更多此镜像详细信息，请参考 [镜像手册](http://www.websoft9.com/xdocs/discuz-image-guide)。
