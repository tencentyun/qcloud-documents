## 操作场景
LAMP 环境是指在 Linux 系统下，由 Apache Web 服务器软件 + MySql 数据库  + PHP 语言及其它相关辅助组件组成的网站服务器架构。本文档介绍如何在 Linux 操作系统的腾讯云服务器（CVM）上通过镜像完成 LAMP 环境搭建。

## 技能要求
腾讯云市场中提供了各个版本的 LAMP 环境镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 LAMP 环境。如果您对 Linux 的使用比较熟悉，需要定制化配置 LAMP，请参考 [手动搭建 LAMP 环境](https://cloud.tencent.com/document/product/213/38402)。

## 注意事项
- 如果您**未购买**云服务器，您可以在购买云服务器时，通过选择镜像市场中的 LAMP 镜像直接搭建环境。详情可参考 [创建云服务器时搭建 LAMP 环境](#create)。
- 如果您**已购买**云服务器，但该云服务器的操作系统并不具备 LAMP 环境，您可以参考 [更换系统镜像](#change) 完成 LAMP 环境搭建。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 搭建 LAMP 环境
#### 创建云服务器时搭建 LAMP 环境<span id="create"></span>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 LAMP 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px">。如下图所示：
>?
>- 本文以下图所示 LAMP 环境系统镜像为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/118eddcc7c8f93b57cf3e40d033c7cd8.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。
云服务器创建成功后，您可通过 [环境配置验证](#inspect) 步骤测试 LAMP 环境是否搭建成功。

#### 更换系统镜像<span id="change"></span>
>!
>- 此步骤通过重装云服务器操作系统来搭建 LAMP 环境，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
>- 如果您的云服务器之前使用 Windows 操作系统并挂载了数据盘，请参考 [Windows 重装为 Linux 后读写原 NTFS 类型数据盘](https://cloud.tencent.com/document/product/213/3857) 进行数据盘格式更换，防止重要数据损坏。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，找到需搭建 LAMP 环境的云服务器。
2. 选择右侧的【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/fd3ff594d6b15c8cd289171288d90af8.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】，并搜索 LNMP 镜像。如下图所示：
![](https://main.qcloudimg.com/raw/28485eb561501ee264cb975564165ab7.png)
4. 根据您的实际需求，选择 LAMP 环境的镜像，并可调整磁盘大小，确认配置信息后，单击【开始重装】。
云服务器完成操作系统部署后，您可通过 [环境配置验证](#inspect) 步骤测试 LNMP 环境是否搭建成功。

### 修改数据库密码
1. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
>?phpMyAdmin 是使用 PHP 语言编写，通过 Web 管理 Mysql、MariaDB 数据库的软件。
>
```
http://云服务器实例的公网 IP/phpmyadmin
```
2. 输入数据库账户名及密码，并单击【执行】。如下图所示：
账户名为 `root`，默认密码为 `123456`。
![](https://main.qcloudimg.com/raw/d99dc7989012dfd29df4c819a185232a.png)
显示结果如下，则说明成功连接 MySQL。
![](https://main.qcloudimg.com/raw/113b566dd330e08f01c211ab78936cc7.png)
3. 在 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/83b9a9e5cc85e6fe784d41425bce7490.png)
4. 在弹出的“修改密码”窗口中，选择进行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库密码。
>
![](https://main.qcloudimg.com/raw/5511571605618e7871dba4ebc54841e9.png)


### 环境验证配置<span id="inspect"></span>
>!
> 搭建 LAMP 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
>
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/90210eaf3fd2214134101d9a425a3e98.png)
2. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。
3. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /data/wwwroot/default/index.php
```
4. 在浏览器中访问以下地址，查看 Apache 及 PHP 是否配置成功。
```
http://云服务器实例的公网 IP/index.php
```
显示结果如下，则说明配置成功：
![](https://main.qcloudimg.com/raw/151e4c758747ef6992bf2f2d1b369f1e.png)

## 相关操作
在完成了 LAMP 环境搭建之后，您可以在次基础上进行 [手动搭建 Drupal 网站]() 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在搭建 LAMP 环境的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。





