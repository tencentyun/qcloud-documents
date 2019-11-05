## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

LNMP 环境是指在 Linux 系统下，由 Nginx+MySQL+PHP 搭建的网站服务器架构。本文档介绍如何在 Linux 操作系统的腾讯云云服务器上通过镜像完成 LNMP 环境搭建。


## 技能要求
腾讯云市场中提供了各个版本的 LNMP 环境组合，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 LNMP 环境。如果您对 Linux 的使用比较熟悉，需要定制化配置 LNMP，您也可以 [手动搭建 LNMP 环境](https://cloud.tencent.com/document/product/213/38056)。



## 操作步骤
### 创建云服务器时搭建 LNMP 环境
>!如果您想使用已购买的云服务器搭建 LNMP 环境，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 LNMP 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px;">。如下图所示：
>?
>- 本文以下图所示 LNMP 环境系统镜像为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/3dcee56060fdabbdc3b92d01f6480df9.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。
云服务器创建成功后，您可通过 [环境配置验证](#inspect) 步骤测试 LNMP 环境是否搭建成功。



### 环境配置验证<span id="inspect"></span>

>!搭建 LNMP 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
>
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 在本地浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/phpinfo.php
```
页面显示如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/fc3d72b5c5522cd942dfceab7ca8bc8a.png)

## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E9.85.8D.E7.BD.AE-wordpress-.E6.95.B0.E6.8D.AE.E5.BA.93.3Cspan-id.3D.22database.22.3E.3C.2Fspan.3E) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在搭建 LNMP 环境的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。

