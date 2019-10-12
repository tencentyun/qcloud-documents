## 操作场景
AMH 是基于 Linux + Nginx + MySQL + PHP （LNMP）环境运行的虚拟主机面板，支持 Web 端管理主机及多种应用服务。本文介绍在腾讯云云服务器（CVM）上通过镜像安装 AMH 并搭建 PHP 网站。


<span id="setting"></span>
## 相关简介
- **域名注册**：请通过腾讯云域名注册服务购买域名，用于部署个人网站。
- **网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云 [网站备案](https://cloud.tencent.com/product/ba) 产品为您的域名备案。
- **云解析**：配置域名解析后，用户可通过域名访问您的网站，不需要使用复杂的 IP 地址才可访问您的网站。您可以通过腾讯云的 [云解析](https://cloud.tencent.com/product/cns) 服务来解析域名。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并参考 [手动安装 AMH]() 完成安装。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 AMH 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px"/>。如下图所示：
>?单击镜像名可查看镜像详情，本文使用镜像为 [PHP 运行环境 AMH 4.2 面板 CentOS 6.8](https://market.cloud.tencent.com/products/5774?productId=5774&_ga=1.62974056.658663049.1568024654)。
>
![](https://main.qcloudimg.com/raw/2a54522e85402984269c696e90a7024c.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


### 搭建 PHP 网站

<span id="create"></span>
#### 创建虚拟主机
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 使用浏览器访问以下地址，进入 AMH 后台管理登录页面。
```
http://云服务器实例的公网 IP:8888
```
显示结果如下图所示：
![](https://main.qcloudimg.com/raw/6d2d36d2c192b7c8822fa2c8f64f95c8.png)
3. 输入如下信息并单击【登录】。
 - 管理员帐号：默认 `admin`。
 - 管理员密码：默认 `cldera.com`。
4. 成功登录后，选择顶部导航栏的【虚拟主机】>【虚拟主机】。如下图所示：
![](https://main.qcloudimg.com/raw/d55cb4f779130edfd850a1a14bf38f76.png)
5. 将域名填入【主机标识域名】及【绑定域名】中，其余设置保持默认，并单击【保存】。如下图所示：
>?
>- 关于域名与注册等相关服务，请参考 [相关简介](#setting)。
>- 本文使用域名以 `qcloudxxxxxx.com` 为例.
>
![](https://main.qcloudimg.com/raw/b355c46a258b0052a173bd30b8b6dfb2.png)
创建成功则如下图所示：
![](https://main.qcloudimg.com/raw/9a833e6faad609eff43010f0c72dc7c7.png)

#### 创建数据库
1. 选择顶部导航栏【MySQL】>【快速建库】。如下图所示：
![](https://main.qcloudimg.com/raw/422d9fd2d3dc19e592d11b0121303990.png)
2. <span id="database"></span>请参考以下配置信息创建数据库。如下图所示：
 ![](https://main.qcloudimg.com/raw/c02da96c26432e69d74c28ac525d263e.png)
 - **数据库名称**：自定义数据库名称，本文以 `mysqlTest` 为例。
 - **数据库编码**：一般使用 `UTF8`。
 - **同时创建用户**：保持默认设置。
 - **用户名**：数据库用户名，本文以 `mysqlTest_user` 为例。
 - **用户密码**：数据库用户登录密码，本文以 `123456` 为例。
 - **允许链接来源地址**：请参考说明结合实际情况填写，本文以 `localhost` 为例。 
 - **用户权限**：保持默认设置。

#### 配置 FTP 服务
1. 选择顶部导航栏【模块扩展】>【管理模块】。如下图所示：
![](https://main.qcloudimg.com/raw/181a1975ddc32c002aab5df40076b0fd.png)
2. 找到 AMFTP 模块，并单击【安装】。如下图所示：
![](https://main.qcloudimg.com/raw/6ac9368b428db1f47c24db7925f0a15c.png)
安装完成后，页面会有成功安装提示。
3. 单击顶部导航栏【FTP】。
4. <span id="ftp"></span>请参考以下配置信息，并单击【保存】创建 FTP 账号。如下图所示：
![](https://main.qcloudimg.com/raw/0050365b3bb6211626d47821e6781938.png)
 - **账号**：FTP 账号名，本文以 ftpuser 为例。
 - **密码**：FTP 账号密码，本文以 `123456` 为例。
 - **主机根目录**：网站根目录，选择下拉列表中的 `/home/wwwroot/xxxxxxxxx/web`。
 - **权限用户**：保持默认设置。
5. 成功创建 FTP 账号后，单击账号操作中的【管理】。如下图所示：
![](https://main.qcloudimg.com/raw/b622e01e3e1846dd3c5fb7a9baead989.png)
6. 在 AMFTP 登录页面上，填写 步骤4 中已创建的 FTP 账号信息，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/86b62685fb566e8384a72e668abada1d.png)
7. 准备 PHP 网站文件。
 - 本文使用 [DedeCMS内容管理系统](http://www.dedecms.com/products/dedecms/)，您可结合实际情况准备文件。
 - 请将网站文件压缩为 zip 文件，本文以 `upload.zip` 为例。如下图所示：
 ![](https://main.qcloudimg.com/raw/fd734bafdac587f18f4f188bac182030.png)
8. 请勾选 AMFTP 中默认的主页文件，并单击下方的【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/0a6da6636e1857f4f15b6fee0b90fc01.png)
9. 选择【上传】>【极速上传】， 在本地目录中选择 `upload.zip`。如下图所示：
10. 成功上传后，请根据页面提示单击【刷新列表】。如下图所示：
 ![](https://main.qcloudimg.com/raw/9cbe6fd84ea6ef607d3b45e82ccb2fc6.png)
10. 勾选 `upload.zip` 文件，并单击下方的【智能解压】。如下图所示：
![](https://main.qcloudimg.com/raw/30d8bceef34420250a6d4c2f76a25b92.png)

### 安装 PHP 网站
1. 使用浏览器访问在 [创建虚拟机](#create) 中已配置的绑定域名。
>!请参考 [相关简介](#setting) 将该云服务器的公网 IP 解析到已配置的绑定域名。
>
2. 勾选”我已经阅读并同意此协议“，并单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/1a27b376150077e14668be1a5814f8dc.png)
3. 查看环境检测结果，并单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/e76298799d6bdd94e9f0c604807ff366.png)
4.  在“参数配置”页面，输入在 [创建数据库](#database) 中已创建的数据库配置，并单击页面下方的【继续】。如下图所示：
>?其余配置可结合您的实际需求自行配置。
>
![](https://main.qcloudimg.com/raw/7eed5b81ae8ac2b13e0c1561e153a3a2.png)
5. 安装完成后，您可单击【访问网站首页】。如下图所示：
![](https://main.qcloudimg.com/raw/04b8566fac9bd72aa0e0572433e883b0.png)
显示结果如下，成功进入网站首页。
![](https://main.qcloudimg.com/raw/92348716dfb81d753bf31dea0ae6e208.png)



