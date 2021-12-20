## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

Magento 是使用 PHP 语言开发的开源电子商务平台，是国际电子商务解决方案之一。本文介绍通过在腾讯云云服务器（CVM）上通过 Magento 镜像来部署个人电子商务网站。


## 操作步骤

### 步骤1：创建云服务器时使用 Magento 镜像
>!如果您想使用已购买的云服务器部署 Magento 个人网站，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您使用其他地域云服务器进行搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
>! 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有【镜像市场】，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“镜像市场”窗口的搜索框中，输入 Magento 并单击 <image src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px"/>。如下图所示：
>?
>- 本文以下图所示的 Magento开源电子商务系统为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
<img src="https://main.qcloudimg.com/raw/fffcdcd863e85aaee62faecad688fcc4.png" style="width: 88%;"></img>
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


### 步骤2：修改数据库密码
>!镜像中默认数据库密码较为简单，为提高数据库安全性，建议执行此步骤修改默认密码。
>
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a5eab449a37929844c7f3af268b76e0d.png)
2. 在本地浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
3. 输入数据库账户名及密码，并单击【执行】。如下图所示： 
帐户名为 `root`，密码请前往 [云市场](https://market.cloud.tencent.com/) 提供的 Magento 开源电子商务系统镜像详情页获取。
![](https://main.qcloudimg.com/raw/30bc260727a56b8779236e8fdb502478.png)
4. 进入 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/c7ea866691b61167dcac1cf467a35896.png)
5. <span id="password"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库密码。
>
![](https://main.qcloudimg.com/raw/f7f4e146148fb8e3c6866ff996fce235.png)

### 步骤3：配置 Magento 客户端
1. 在本地浏览器访问以下地址，进入 Magento 配置页面。
```
http://云服务器实例的公网 IP
```
2. 在 Magento 配置页面，单击【Agree and Setup Magento】。如下图所示：
![](https://main.qcloudimg.com/raw/f32243c018ed86b0dfafcdb2e1082311.png)
3. 单击【Start Readiness Check】，进行环境检测。如下图所示：
![](https://main.qcloudimg.com/raw/8e883ec4322f3f0d26fa181d62cebb82.png)
4. 环境检测通过后，单击【Next】进入下一步。如下图所示：
![](https://main.qcloudimg.com/raw/77e0ec4010c82232c26c4fe3a351ba93.png)
5. 添加数据库信息，请输入从 [修改密码](#password) 步骤中设置的数据库密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/277d201ee1422c4db4e96ff6133c993f.png)
6. <span id="admin"></span>将 Magento 管理员登录地址修改为 `admin` ，并单击【Next】。如下图所示：
>?请记录网站地址及网站管理员登录地址。
>
![](https://main.qcloudimg.com/raw/64f6941b18fdbbf969a865407af39d90.png)
7. 根据您的实际情况设置语言、时区等信息，并单击【Next】。本文设置如下图所示：
![](https://main.qcloudimg.com/raw/d14949a09a8f8bd1d56268a386fc3e7f.png)
8. 根据您的实际情况设置管理员登录账号及密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/b73a4d1593e4250b944255b5d202e33a.png)
9. 单击【Install Now】进行安装。
10. 成功安装后请记录页面上的信息，并单击【Launch Magento Admin】。如下图所示：
![](https://main.qcloudimg.com/raw/a5d9c2fbe7f17c454a0cbae30217390b.png)
11. 进入管理员登录页面，输入 [步骤6](#admin) 设置的管理员账号及密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/d196f04eec071c0ab27895698c75c88b.png)
12. 登录成功后，即可进入管理员页面配置个人商务网站。如下图所示：
![](https://main.qcloudimg.com/raw/897866cc646521b0d32ce09515dc4efc.png)


### 步骤4：验证配置
使用本地浏览器访问下列地址，查看 Magento 客户端是否安装成功。
```
http://云服务器实例的公网 IP
```
显示结果为 Magento 默认主页，则说明安装成功。如下图所示：
![](https://main.qcloudimg.com/raw/da502fe4310e49fae659310b3d778fa7.png)

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。





