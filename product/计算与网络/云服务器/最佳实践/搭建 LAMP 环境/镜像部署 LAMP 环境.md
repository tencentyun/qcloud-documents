## 操作场景
腾讯云市场中提供了例如包含多种操作系统、热门软件等不同类型的镜像。您可选择这些镜像，在腾讯云云服务器（CVM）上快速部署具有较高稳定性和安全性的软件环境以及个人网站。

LAMP 环境是指在 Linux 系统下，由 Apache Web 服务器软件 + MySql 数据库  + PHP 语言及其它相关辅助组件组成的网站服务器架构。本文档介绍如何在 Linux 操作系统的腾讯云云服务器（CVM）上通过镜像完成 LAMP 环境部署。

## 技能要求
腾讯云市场中提供了各个版本的 LAMP 环境镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 LAMP 环境。如果您对 Linux 的使用比较熟悉，需要定制化配置 LAMP，请参考 [手动搭建 LAMP 环境](https://cloud.tencent.com/document/product/213/38402)。



## 操作步骤
### 步骤1：创建云服务器时部署 LAMP 环境



<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 LAMP 环境，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动搭建 LAMP 环境](https://cloud.tencent.com/document/product/213/38402) 或者使用其他地域云服务器进行搭建。
</dx-alert>



1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在“镜像”中选择**镜像市场** > **从镜像市场选择**。如下图所示：
>! 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“镜像市场”窗口的搜索框中，输入 LAMP 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px">。如下图所示：
<dx-alert infotype="explain" title="">
- 本文以下图所示 LAMP 环境系统镜像为例，您可根据实际需求进行选择。
- 单击镜像名可查看镜像详情。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/af2e8d4ae22fa5b6805195c78def93c1.png" style="width: 88%;"></img>
4. 单击**免费使用**。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。



### 步骤2：修改数据库密码

<dx-alert infotype="notice" title="">
镜像中默认数据库密码较为简单，为提高数据库安全性，建议执行此步骤修改默认密码。
</dx-alert>

1. 在本地浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
2. 输入数据库账户名及密码，并单击**执行**。如下图所示：
账户名为 `root`，密码随机生成，请前往 [云市场](https://market.cloud.tencent.com/) 提供的 LAMP 环境系统镜像详情页获取。
![](https://main.qcloudimg.com/raw/3d944937e2474f1167f16d291fe8a7ae.png)
3. 在 phpMyAdmin 管理页面，单击**修改密码**。如下图所示：
![](https://main.qcloudimg.com/raw/8a59eedcfa52cb62af7d7476b324d7fe.png)
4. 在弹出的“修改密码”窗口中，选择进行设置或自动生成密码，并单击**执行**。如下图所示：
<dx-alert infotype="explain" title="">
本文使用自动生成密码，请记录您的数据库密码。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/c0d842586c7f805efd89f100a8cc194a.png"/>


### 步骤3：环境验证配置


<dx-alert infotype="notice" title="">
搭建 LAMP 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
</dx-alert>


1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/90210eaf3fd2214134101d9a425a3e98.png)
2. 登录 Linux 云服务器，具体操作请参考 [使用标准方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
3. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /data/wwwroot/default/index.php
```
4. 在本地浏览器中访问以下地址，查看 Apache 及 PHP 是否配置成功。
```
http://云服务器实例的公网 IP/index.php
```
显示结果如下，则说明配置成功：
![](https://main.qcloudimg.com/raw/151e4c758747ef6992bf2f2d1b369f1e.png)

## 相关操作
在完成了 LAMP 环境搭建之后，您可以在此基础上进行 [手动搭建 Drupal 网站](https://cloud.tencent.com/document/product/213/38617) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在搭建 LAMP 环境的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。

