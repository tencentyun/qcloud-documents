## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

Moodle 是一个开源的在线教育系统，也被称为在线学习系统（LMS）。Moodle 采用 PHP 语言和 MySQL 开发，您可使用 Moodle 为学习者建立开放式课程系统。本文档介绍在腾讯云云服务器（CVM）上通过镜像部署 Moodle 在线学习系统。

## 操作步骤
### 步骤1：创建云服务器时使用 Moodle 镜像
>!如果您想使用已购买的云服务器部署 Moodle，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您使用其他地域云服务器进行搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 据页面提示选择机型，并在“镜像”中选择**镜像市场** > **从镜像市场选择**。如下图所示：
>! 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“镜像市场”窗口的搜索框中，输入 moodle 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px;"/>。如下图所示：
>?单击镜像名可查看镜像详情，本文使用 [Moodle LMS在线学习系统](https://market.cloud.tencent.com/products/708?productId=708&_ga=1.158416825.2093467297.1571788865)。
>
<img src="https://main.qcloudimg.com/raw/4ea728940dd2c7b9961542fe38147e3c.png" style="width: 88%;"></img>
4. 单击**免费使用**。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。



### 步骤2：修改数据库密码
>!镜像中默认数据库密码较为简单，为提高数据库安全性，建议执行此步骤修改默认密码。
>
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/392ce24430ac82c418ebad7a28874645.png)
2. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
3. 输入数据库账户名及密码，并单击**执行**。如下图所示：
帐户名为 `root`，密码随机生成，请前往 [云市场](https://market.cloud.tencent.com/) 提供的 Moodle LMS在线学习系统镜像详情页获取。
![](https://main.qcloudimg.com/raw/54443cb3bc233568a78271f0cea07e0a.png)
4. 进入 phpMyAdmin 管理页面，单击**修改密码**。如下图所示：
![](https://main.qcloudimg.com/raw/324ae5bb2a6fa8b26af795f4ea5b6426.png)
5. <span id="sercet"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击**执行**。如下图所示：
>?本文使用自动生成密码，请记录您的数据库帐号及密码。
>
![](https://main.qcloudimg.com/raw/dd319a9e59595a2c6aeb28ec036295d3.png)


### 步骤3：安装配置 Moodle
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/392ce24430ac82c418ebad7a28874645.png)
2. 在本地浏览器中访问该云服务器实例的公网 IP，进入 Moodle 安装页面。
3. 在“语言”选择简体中文（zh_cn），并单击**向后**。如下图所示：
![](https://main.qcloudimg.com/raw/609e424cb0d1379dc0217994f8bc55df.png)
4. 在“确认路径”页面，保持所有默认设置不变，并单击**向后**。如下图所示：
![](https://main.qcloudimg.com/raw/db6f66fcf913ee0deab2648614661607.png)
5. 在“选择数据库驱动”页面，保持所有默认设置不变。并单击**向后**。如下图所示：
![](https://main.qcloudimg.com/raw/b5fdcb6d83e27baf793f29efa97567b8.png)
6. 在“数据库设置”页面根据以下提示填写相关信息，并单击**向后**。如下图所示：
![](https://main.qcloudimg.com/raw/78c372843bc0e25e2097504e97606c55.png)
 - **数据库用户名**：请输入 `root`。
 - **数据库密码**：请输出在步骤 [修改密码](#sercet) 中设置的数据库密码，如果您未修改密码，则请输入默认密码 `123456`。
 - **数据库服务端口**：请输入3306。
7. 阅读并理解版权说明，并单击**继续**。
8. 在检查安装组件页面看到提示确认部署完毕后，单击**继续**。如下图所示：
![](https://main.qcloudimg.com/raw/24b607d5e402b0f39df05e09a607facc.png)
9. 等待组件安装完成后，单击页面底部的**继续**。如下图所示：
![](https://main.qcloudimg.com/raw/724c4f9a35e073d8d36eb8c55c6390a8.png)
10. 按照页面提示填写系统管理员信息，并单击**更新个人资料**。如下图所示：
![](https://main.qcloudimg.com/raw/fa13ed59be616e97d08d027e49275f1e.png)
11. 根据页面提示进行网站名称及其他相关设置，并单击**保存更改**。
12. 安装成功后，自动登录后台管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/3b7d66d6a52056fcf33a7d615662effe.png)
您已成功搭建 Moodle 在线学习系统，可根据您的实际需求进行网站管理及个性化设置。

## 常见问题
如果您在部署 Moodle 网站的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。


