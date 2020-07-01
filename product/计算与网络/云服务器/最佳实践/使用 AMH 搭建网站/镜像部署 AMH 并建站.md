## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

AMH 是基于 Linux + Nginx + MySQL + PHP （LNMP）环境运行的虚拟主机面板，支持 Web 端管理主机及多种应用服务。本文介绍在腾讯云云服务器（CVM）上通过镜像部署 AMH 并搭建 PHP 网站。


## 技能要求
腾讯云市场中提供了多个版本的 AMH 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 AMH 并建站。如果您对 Linux 的使用较为熟悉，也可参考 [手动安装 AMH 和建站](https://cloud.tencent.com/document/product/213/38362)。


## 注意事项<span id="note"></span>
使用 AMH 搭建网站的过程中需要使用已完成备案，并且已解析到所使用云服务器的域名。
腾讯云提供 [域名注册](https://dnspod.cloud.tencent.com/)、[网站备案](https://cloud.tencent.com/product/ba) 及 [云解析](https://cloud.tencent.com/product/cns) 服务，您可通过服务并参考 [建站基本流程](https://cloud.tencent.com/document/product/242/8584) 获得可使用域名。


## 操作步骤
### 步骤1：创建云服务器时使用 AMH 镜像
>! 如果您想使用已购买的云服务器使用 AMH 镜像，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动安装 AMH 和建站](https://cloud.tencent.com/document/product/213/38362) 或者使用其他地域云服务器进行搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
>! 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有【镜像市场】，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“镜像市场”窗口的搜索框中，输入 AMH 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px"/>。如下图所示：
>?单击镜像名可查看镜像详情，本文使用镜像为 [PHP运行环境 AMH4.2面板PHP5.3CentOS 6.8](https://market.cloud.tencent.com/products/5774?productId=5774&_ga=1.62974056.658663049.1568024654)。
>
<img src="https://main.qcloudimg.com/raw/96815a1b05ae819ef4f50716def2276d.png" style="width: 88%;"></img>
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。


### 步骤2：搭建 PHP 网站

<span id="create"></span>
#### 创建虚拟主机
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a33ce52cd6195a07b5d4fba29e1dd598.png)
2. 使用本地浏览器访问以下地址，进入 AMH 后台管理登录页面。
```
http://云服务器实例的公网 IP:8888
```
显示结果如下图所示：
![](https://main.qcloudimg.com/raw/eb92ded2d7fa118d009b7e30ba622ad0.png)
3. 输入如下信息并单击【登录】。
 - 管理员帐号：默认 `admin`。
 - 管理员密码：默认 `cldera.com`。
4. 成功登录后，选择顶部导航栏的【虚拟主机】>【虚拟主机】。如下图所示：
![](https://main.qcloudimg.com/raw/1df79c49c83ed087c18810367c748744.png)
5. 将**已解析到云服务器**的域名填入【主机标识域名】及【绑定域名】中，其余设置保持默认，并单击【保存】。如下图所示：
>?本文使用域名以 `qcloudxxxxxx.com` 为例，您可参考 [注意事项](#note) 准备域名。
>
![](https://main.qcloudimg.com/raw/f5e6eb2ce639175839b5f1d8249288d6.png)
创建成功则如下图所示：
![](https://main.qcloudimg.com/raw/14f3df0f132e15cba9a10a22887e2b15.png)

#### 创建数据库
1. 选择顶部导航栏【MySQL】>【快速建库】。如下图所示：
![](https://main.qcloudimg.com/raw/d51b16f13d3df4e28d9a872229dc97f4.png)
2. <span id="database"></span>请参考以下配置信息创建数据库。如下图所示：
![](https://main.qcloudimg.com/raw/f86413fd5e314e46863233768b5cc77f.png)
 - **数据库名称**：自定义数据库名称，本文以 `mysqlTest` 为例。
 - **数据库编码**：一般使用 `UTF8`。
 - **同时创建用户**：自定义数据库名，本文以 `mysqlTest_user` 为例。
 - **用户名**：数据库用户名，本文以 `mysqlTest_user` 为例。
 - **用户密码**：数据库用户登录密码，本文以 `123456` 为例。
 - **允许链接来源地址**：请参考说明结合实际情况填写，本文以 `localhost` 为例。 
 - **用户权限**：保持默认设置。

#### 配置 FTP 服务
1. 选择顶部导航栏【模块扩展】>【管理模块】。如下图所示：
![](https://main.qcloudimg.com/raw/3bc51265e0ab32f8287e59a3bee5b838.png)
2. 找到 AMFTP 模块，并单击【安装】。如下图所示：
![](https://main.qcloudimg.com/raw/14057c6d9f86119064271790b4ca7009.png)
安装完成后，页面会有成功安装的提示信息。
3. 单击顶部导航栏【FTP】。
4. <span id="ftp"></span>请参考以下配置信息，并单击【保存】创建 FTP 账号。如下图所示：
![](https://main.qcloudimg.com/raw/e4e8bebfc942891f9ca46e7f0f87c2d4.png)
 - **账号**：FTP 账号名，本文以 `ftpuser` 为例。
 - **密码**：FTP 账号密码，本文以 `123456` 为例。
 - **主机根目录**：网站根目录，选择下拉列表中的 `/home/wwwroot/xxxxxxxxx/web`。
 - **权限用户**：保持默认设置。
5. 成功创建 FTP 账号后，单击账号操作中的【管理】。如下图所示：
![](https://main.qcloudimg.com/raw/66033f8d6e8252e8da0a5757a7c62bc5.png)
6. 在 AMFTP 登录页面上，填写 [步骤4](#ftp) 中已创建的 FTP 账号信息，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/86b62685fb566e8384a72e668abada1d.png)
7. 准备 PHP 网站文件。
 - 本文使用 [DedeCMS内容管理系统](http://www.dedecms.com/products/dedecms/)，您可结合实际情况准备相关文件。
 - 请将网站文件压缩为 zip 文件，本文以 `upload.zip` 为例。如下图所示：
 ![](https://main.qcloudimg.com/raw/fd734bafdac587f18f4f188bac182030.png)
8. 请勾选 AMFTP 中默认的主页文件 `ErrorPages` 和 `index.html`，并单击下方的【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/e26357cbf7671664ebb0a38485ad6ad8.png)
9. 选择【上传】>【极速上传】， 并在本地目录中选择 `upload.zip`。
10. 成功上传后，请根据页面提示单击【刷新列表】。如下图所示：
 ![](https://main.qcloudimg.com/raw/9cbe6fd84ea6ef607d3b45e82ccb2fc6.png)
11. 勾选 `upload.zip` 文件，并单击下方的【智能解压】。如下图所示：
![](https://main.qcloudimg.com/raw/a8c20c04d5505441d38f31bb4ba3fa4a.png)

### 步骤3：安装 PHP 网站
1. 使用本地浏览器访问在 [创建虚拟主机](#create) 中已配置的绑定域名。
2. 勾选”我已经阅读并同意此协议“，并单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/519761fdd468e44a851a1c34713b9d1b.png)
3. 查看环境检测结果，并单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/c4276d4c51ac88c736674515b7e8eb3f.png)
4.  在“参数配置”页面，输入在 [创建数据库](#database) 中已创建的数据库配置，并单击页面下方的【继续】。如下图所示：
>?其余配置可结合您的实际需求自行设置。
>
![](https://main.qcloudimg.com/raw/9e3d2b24c9a536bfe6a0c8afb3e7dce8.png)
5. 安装完成后，您可单击【访问网站首页】。如下图所示：
![](https://main.qcloudimg.com/raw/9981fc66d1751daae3baa7de327e9a09.png)
显示结果如下，成功进入网站首页。
![](https://main.qcloudimg.com/raw/8f6336e585395b98d8f25f1c847fe5b2.png)

## 常见问题
如果您在部署 AMH 及建站的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。


