## 操作场景

WordPress 是全球最流行的开源的博客和内容管理网站的建站平台，具备使用简单、功能强大、灵活可扩展的特点，提供丰富的主题插件。腾讯云轻量应用服务器 Lighthouse 提供 WordPress 应用镜像，您可以使用它快速搭建博客、企业官网、电商、论坛等各类网站。

>? WordPress 应用镜像底层基于 CentOS 7.6 64位操作系统。
>

## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 单击【新建】，进入轻量应用服务器购买页面。
![](https://main.qcloudimg.com/raw/691f4eaa4679ae8dcd5f8ace46718463.png)
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择 “WordPress 5.4.2” 应用镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付。
4. 返回轻量应用服务器控制台。
5. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 WordPress 应用的各项配置信息。
6. 选择【应用管理】页签，进入应用管理详情页。
7. <span id="step7"></span>在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: 0;"></img>，复制获取 WordPress 管理员帐号及密码的命令。
8. 在“应用内软件信息”栏中，单击【登录】。
![](https://main.qcloudimg.com/raw/7727fbc610a6245bda73d668f1a513ed.png)
9. 在弹出的登录窗口中，粘贴在 [步骤7](#step7) 中获取的命令，并按 **Enter**。
即可获取 WordPress 管理员帐号（admin ）和对应的密码。
![](https://main.qcloudimg.com/raw/2b3a5ac10481b8d63111769fb7f85f4a.png)
10. <span id="step10"></span>复制并记录 WordPress 管理员帐号和密码。
11. 关闭登录窗口，并返回该实例的应用管理详情页。
12. 在“应用内软件信息”栏中，单击 WordPress 的【管理员登录地址】。
![](https://main.qcloudimg.com/raw/d8d9951ce63c7660f6e18d15559a11c4.png)
13. 在新打开的浏览器窗口中，输入 [步骤10](#step10) 记录的账号和密码，单击【登录】。
![](https://main.qcloudimg.com/raw/3fc36b90b8c5022d5a46ac6b718e30db.png)
>?应用镜像 Wordpress 5.4.2 版本需进行管理邮件确认及数据库更新确认，请查阅页面信息并依次单击【此地址正确】及【升级Wordpress数据库】即可。
>
成功登录后，您可根据实际需要对 WordPress 进行管理、自定义和配置。

## 相关操作
### 更新 WordPress 管理员个人资料

1. 在 WordPress 管理界面的左侧导航中，选择【用户】>【所有用户】。
2. 找到 `admin` 用户，单击【编辑】。
3. 根据实际需求，设置个人资料。
例如：
 - 在“联系信息”栏中，输入您的电子邮件地址。
 - 在“账户管理”栏中，单击【生成密码】，输入新的管理员密码。
5. 单击【更新个人资料】。

### 查看其他配置信息

在 WordPress 实例的应用管理详情页，您除了可以查看 WordPress 的配置信息，还可以查看其他配置信息。例如首页地址、 Nginx 主配置文件保存路径、 MariaDB 数据库管理员密码、实例中各个软件的安装路径等。
![](https://main.qcloudimg.com/raw/a70ee3695d07501b9ac0bc53abb3c50e.png)

### 安装 SSL 证书
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 WordPress 实例安装 SSL 证书并开启 HTTPS 访问。
