# 启动 WordPress 个人站点
本指南将介绍通过腾讯云云服务器 CVM（以下简称 CVM）上安装的 WordPress 镜像来启动并运行一个网站。您将了解如何配置并启动 CVM 云主机、如何获取 WordPress 用户名和密码，以及如何登录 WordPress 管理页面。
**注意**：本指南主要针对基本的 WordPress 网站搭建，适用于个人使用或学习。不建议针对具有较高可扩展性需求的业务级网站使用本教程。要获取更高级的教程，请参阅 搭建 [WordPress 个人站点](https://www.qcloud.com/document/product/213/8044)。

请保持此指南处于打开状态，同时登录到 [腾讯云管理控制台](https://console.qcloud.com/)。
### 步骤一：启动 CVM
通过腾讯云启动 WordPress 网站，前提是拥有一台腾讯云的云服务器。
- 若您已拥有 CVM，请跳过此步骤，进入步骤二。
- 若您还未拥有 CVM，请先购买云服务器。请按照如下步骤购买。
 1. 请点击 [购买云服务器](https://buy.qcloud.com/cvm)，进入购买页面。
 2. 点击【快速配置】，镜像选择【操作系统+应用】，选购带有 WordPress 开源博客系统应用的镜像。
![购买云服务器1](//mc.qcloudimg.com/static/img/49267c2c92a05e171ef44ee44ed32222/image.png)
 3. 购买成功后，系统将会发送一封站内信至您的账户，请打开 [站内信](https://console.qcloud.com/message) 查看您已购买云服务器的信息，请保存好您的云服务器初始账户和密码。
![站内信1](//mc.qcloudimg.com/static/img/2e1ab9f2401d185f34aa8d945caa7f64/image.png)

### 步骤二：配置云主机
1. 登录 [腾讯云管理控制台](https://console.qcloud.com/)，在【云产品】下找到【云服务器】，点击打开云服务器控制台。
![打开控制台1](//mc.qcloudimg.com/static/img/64198e0147f6a6eea021976a6eac55fd/image.png)
2. 为云主机设置名称，便于区分。
 1. 请点击左侧导航【云主机】，进入云主机页面，选定要使用的云主机。点击云主机的 **ID/主机名**，为云主机修改名称。
![改名a](//mc.qcloudimg.com/static/img/18f7dde588d5abbf0f1266897e766c43/image.png)
 2. 修改为 “WordPress”（可以自定义），点击确定以保存。
![改名b1](//mc.qcloudimg.com/static/img/982ffd605178fdee45ae0b35d78fe40b/image.png)
3. 重装系统
 1. 点击云主机右侧的 【更多】，选择【重装系统】。
![更多1](//mc.qcloudimg.com/static/img/f0a23ee44d129a9e38b86374b5988fab/image.png)
 2. 在出现的**重装系统**提示框中，选择【服务市场】 -> 【建站模板】，安装对应的镜像。本指南中，我们选择的是** WordPress博客平台（CentOS 6.8 64位）**。
![重装系统1](//mc.qcloudimg.com/static/img/36d24cce5afbececa8637a4d9e97fcb4/image.png)
 3. **登录设置**选择【密码】，并且为 root 账号设置密码。点击【开始重装】进入重装状态。重装可能需要几分钟的时间。
4. 云主机状态处于运行中时，就可以测试 WordPress 网站了。在云主机的 **主 IP 地址** 下，复制云主机的公网 IP。
5. 将该公网 IP 粘贴到浏览器的地址栏中访问，可以看到引导页面。 
![IP页面](//mc.qcloudimg.com/static/img/f7ea8180f0c49be0f422e88140bbafee/image.png)

### 步骤三：启动 WordPress 网站
1. 在引导页面中，点击【获取权限】，下载该镜像的相关信息文档到本地。（该文档包含 WordPress 网站的相关重要信息，请注意保存。）
2. 下载完成后请打开文档，获取 WordPress 网站的管理员登录账号和密码。
![管理员账密1](//mc.qcloudimg.com/static/img/bc8ebd15b688b7e92b67ac12a83aa7b6/image.png)
3. 刷新引导页面，出现 WordPress 的欢迎页面，至此，WordPress 网站启动成功。
4. 接下来您可以登录管理页面来自定义网站。
 1. 在欢迎页面右下角的【功能】下点击【登录】。
![登录1](//mc.qcloudimg.com/static/img/076e034cc8dcd206c627d8b924aab0bf/image.png)
 2. 输入管理员账号和密码，点击登录。
![账号密码登录wp](//mc.qcloudimg.com/static/img/48f8740a24c0602616a5935ab6b6ae64/image.png)
 3. 恭喜您！您已启动并运行 WordPress 网站。现在，您可以根据需要对其进行管理、自定义和配置了。