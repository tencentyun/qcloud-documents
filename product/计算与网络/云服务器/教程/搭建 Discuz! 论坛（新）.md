Discuz! 是全球成熟度最高、覆盖率最大的论坛网站软件系统之一，被 200 多万网站用户使用，本教程介绍在 LAMP （Linux + Apache + MySQL + PHP）环境下搭建 Discuz! 论坛网站的步骤，以 Discuz! X3.2 为例。
> Linux：Linux 系统；
Apache：用来解析 Web 程序，最流行的 Web 服务器端软件之一；
MySQL：一个数据库管理系统；
PHP：Web 服务器生成网页的程序。

本教程提供两种搭建 Discuz! 论坛的方式，您可根据需求自由选择：
- 使用 Discuz! 镜像快速安装
- 自主安装 LAMP 环境并搭建论坛

如果您是第一次进行 Discuz! 论坛搭建，不熟悉相关命令操作，您可以通过第一种方法来搭建您的论坛：使用 Discuz! 镜像快速安装 。
如果您已拥有相关论坛搭建经验和一定的命令操作基础，想自定义搭建一个 Discuz! 论坛，您可以参考第二种方法：自主安装 LAMP 环境并搭建论坛。
## 镜像安装 
您可以通过镜像来快捷安装 Discuz! 论坛，以下教程供您参考：
![流程图1](//mc.qcloudimg.com/static/img/db454d696e269f0f29c9c63abf11db59/image.png)
### 相关简介
以下是本教程中，将会使用的服务或工具：
**云服务器 CVM**：本教程使用腾讯云云服务器 CVM （以下简称 CVM ）创建云主机，来完成 Discuz! 搭建工作。
 
**域名注册**：如果想要使用易记的域名访问您的 Discuz! 论坛，可以使用腾讯云域名注册服务来购买域名。
 
**网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云为您的域名备案。

**云解析**：在配置域名解析之后，用户才能通过域名访问您的网站，而不需要使用复杂的 IP 地址。您可以通过腾讯云的云解析服务来解析域名。

### 步骤一：安装 Discuz! 相关镜像 
1. 获取 Discuz! 镜像
请 [登录腾讯云](https://www.qcloud.com/login?s_ur=https://console.qcloud.com)，通过首页顶部导航进入 [云市场](http://market.qcloud.com/categories?q=discuz)，在搜索框中搜索 “Discuz”，获取免费 Discuz! 镜像。
![获取Discuz1](//mc.qcloudimg.com/static/img/54021a861602cdf6560306848cdcef0f/image.png)
2. 购买云服务器
购买镜像的过程同时会配套购买云服务器，云服务器的配置可以根据网站自身访问量来确定。
3. 创建云主机
完成购买后，控制台开始创建一个新的云主机。创建完成后，云主机会自动处于运行中，请耐心等待 2-3 分钟后再进入步骤二。
![获取Discuz2](//mc.qcloudimg.com/static/img/e8f6ff29add95aaadb09f3401a918093/image.png)
**注意**：若您已经有了腾讯云云主机，您可以通过云服务器控制台 > 云主机 > 更多 > 重装系统，在服务市场的建站模板中找到 Discuz! 相关的镜像后，重装系统。
![获取Discuz3](//mc.qcloudimg.com/static/img/942086a3d094f298195c46128ee0c2b9/image.png)

### 步骤二：验证 Discuz! 镜像 
镜像的原理是系统盘的拷贝（任何使用镜像的用户获得的都是一模一样的程序和运行环境），因此如果您认为计算机自动化拷贝过程是 100% 准确无误的，那么镜像显然也是100%可用的。但在某些特殊情况下，可能无法正常打开镜像。所以，镜像的验证完全有必要。
镜像安装成功后，等待 3 分钟左右，即可使用浏览器打开网址 `http://云主机的公网 IP`， 访问正常会出现如下界面：
![安装Discuz1](//mc.qcloudimg.com/static/img/6cc33ab8677f55fd3ae5e26df67a7953/image.png)
若上图的页面不显示，请按照如下建议依次排除问题：
- 重启服务器再试。
- Ping 公网IP地址，查看网络连接是否可用。
- 查看服务器的 [安全组配置](https://www.qcloud.com/document/product/213/5221)，排除是否禁止了 http 的默认端口。

### 步骤三：创建数据库 
一般情况下，我们需要为 Discuz! 程序创建一个独立的数据库和用户，本步骤介绍通过 phpMyAdmin 工具来创建数据库的方法。（数据库的默认用户名和密码请通过 [镜像帮助文档](http://www.websoft9.com/xdocs/discuz-image-guide) 查看，一般是 root/123456）。
1. 使用浏览器打开网址 `http://云主机的公网 IP/phpMyAdmin` ，将出现 phpMyAdmin 工具的登录界面。
2. 登录后新建并命名一个数据库，如 Discuz。
![创建数据库1](//mc.qcloudimg.com/static/img/b45754c3149817e9d99fcd5c8e6fd344/image.png)
3. 为 Discuz 数据库添加一个新用户。
![创建数据库2](//mc.qcloudimg.com/static/img/2c2455f187da38959dfbc38d34c621cf/image.png)
并为新用户设置登录密码，并且授予其权限。最后点击页面右下角的执行保存即可。
![创建数据库3](//mc.qcloudimg.com/static/img/3fc55757983147941d9df17ffecdb6e5/image.png)
数据库创建完成后，可以关闭此网页，进入下一步骤。

### 步骤四：配置域名（可选）
您可以给自己的 Discuz! 论坛网站设定一个单独的域名。您的用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。但是有些用户没有域名，搭建论坛仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。
如果您使用 IP 直接安装，可以跳过此步骤，直接进行下一步骤。
如果您已有域名或者想要通过域名来访问您的论坛，可以参考以下步骤。
1. 请通过 [腾讯云购买域名](https://dnspod.qcloud.com/?from=qcloud)。 
2. 请进行 [网站备案](https://www.qcloud.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，一般审核时间为20天左右。
3. 通过腾讯云 [云解析](https://www.qcloud.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。
登录 [云解析控制台](https://console.qcloud.com/cns/domains)，选择域名或添加您已有的域名。
点击【解析】，进入该域名的域名记录管理界面。
![配置域名1](//mc.qcloudimg.com/static/img/c2e3da7449cf42697a15f5c2bf9e80cf/image.png)
点击【添加记录】，添加需要解析的记录。
![配置域名2](//mc.qcloudimg.com/static/img/4a5054890890418d83ced42db4f3a98a/image.png)

### 步骤五：安装配置 Discuz! 
1. 首先通过浏览器访问步骤四中已经配置好的域名，点击  Discuz!【安装配置】进入安装页面。单击【我同意】，然后选择【下一步】。
![安装1](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
2. 进入安装步骤第一步：检查安装环境，继续单击 【下一步】。
![安装2](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
3. 进入设置运行环境步骤，此教程中选择全新安装，继续【下一步】。
![安装3](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
4. 在安装数据库步骤中，填写步骤三已创建的数据库名称、用户、密码，并且设置管理员账号和密码。
**注意**：请记住自己的管理员用户和密码。
![安装4](//mc.qcloudimg.com/static/img/b2729abfc2e3fd5679ab8d1e7efc102b/image.png)
5. 安装完成后，您可以访问论坛。
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)
 
镜像安装更多相关问题，请参考 [Discuz! 镜像安装手册](http://www.websoft9.com/xdocs/discuz-image-guide)。

## 自主安装
对于想自主安装 Discuz! 论坛的用户，您可以参考以下教程：
![流程图2](//mc.qcloudimg.com/static/img/6b60f627a0f72093c39bf0fb34b35724/image.png)
### 相关简介
以下是本教程中，将会使用的服务或工具：
**云服务器 CVM**：本教程使用腾讯云云服务器 CVM （以下简称 CVM ）创建云主机，来完成 Discuz! 搭建工作。
 
**域名注册**：如果想要使用易记的域名访问您的 Discuz! 论坛，可以使用腾讯云域名注册服务来购买域名。
 
**网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云为您的域名备案。

**云解析**：在配置域名解析之后，用户才能通过域名访问您的网站，而不需要使用复杂的 IP 地址。您可以通过腾讯云的云解析服务来解析域名。

**PuTTY**：PuTTY 是免费且出色的远程登录工具之一，本教程使用这款简单易操作的软件来完成相关搭建工作。点击 [下载 PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524)。
### 步骤一：创建云服务器 
1. 请根据您的需要 [购买云服务器](https://buy.qcloud.com/cvm?regionId=8&projectId=8)。
以下创建指引供您参考：
[创建 Linux 云服务器](https://www.qcloud.com/document/product/213/2972)
2. 服务器创建成功后，您可登录 [腾讯云管理控制台](https://console.qcloud.com/cvm)  查看或编辑云主机状态。
![云主机1](//mc.qcloudimg.com/static/img/cbd7d2717a9d162df28b4d517ab1d815/image.png)

本教程中云主机的操作系统版本为 CentOS 6.8。后续步骤将会用到以下信息，请注意保存：
- 云主机用户名和密码；
- 云主机公网 IP。

### 步骤二：搭建 LAMP 环境 
对于 CentOS 系统，腾讯云提供软件安装源，是同步 CentOS 官方的安装源，包涵的软件都是当前最稳定的版本，因此我们可以直接通过 Yum 快速安装软件。
#### 2.1 运行 PuTTY 连接 Linux 云主机
1. 请 [下载 PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524) 到您的电脑，打开下载所在文件夹，解压文件；双击 “putty.exe”，出现配置界面。
2. 选择 “Session”，在 “Host Name (or IP address)” 输入框中输入欲访问的主机名或 IP，如 “server1” 或 “192.168.2.10”。本教程输入的是云主机的公网 IP。其他配置保持默认。
3. 在 “Saved Sessions” 输入栏中命名会话，单击 “Save” ，即可保存会话配置。
![putty1](//mc.qcloudimg.com/static/img/85df3247daae4982003a91ad1ad6f89e/image.png)
4. 配置完成后单击 “Open” 按钮，将会出现确认证书的提示窗，请选择 “是” 。
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
出现登录界面，依次输入云主机的用户名和密码，就可连接到云主机，进行后续操作。
![putty3](//mc.qcloudimg.com/static/img/b632cf3e122832193a77afe04c93fbc1/image.png)

#### 2.2 安装必要软件
1. 登录云服务器后，默认已获取 root 权限。在 root 权限下，通过以下命令，先将必要软件一起安装 （Apache、MySQL、PHP）：
```
yum install httpd php php-fpm php-mysql mysql mysql-server -y
```
安装完成，PuTTY 窗口会提示“Complete!”。同时可以上滑滚动条查看当前安装包版本：
![软件版本](//mc.qcloudimg.com/static/img/4d1e4ee237bcd67ad39051f843bded53/image.png)
本教程中安装包版本分别如下：
Apache：2.2.15
MySQL：5.1.73
PHP：5.3.3
2. 启动服务
```
service httpd start
service mysqld start
service php-fpm start
```
3. 配置 MySQL 数据库
我们需要为 Discuz 程序创建一个独立的数据库和用户来存储数据，步骤 2.2 已启动了数据库服务，本步骤需要给 MySQL 设定一个 root 密码，使 root 用户可以访问数据库。
```
mysqladmin -u root password "XXXXXXXX" (此处的密码可进行自定义）
```
设置好 MySQL的密码后， 对账号密码进行验证。
```
mysql -u root -p
``` 
输入刚刚设定好的密码，可以登录到 MySQL 中，则说明配置正确。退出 MySQL：
```
exit
```
![配置数据库](//mc.qcloudimg.com/static/img/5f180f866334ee46e4b7e77851c5add0/image.png)

#### 2.3 验证环境配置
一般情况下，到此步时，环境已经配置成功，为确认和保证环境搭建成功，可以通过本步骤来验证。
1. 请使用以下命令在 在 Apache 的默认根目录 “/var/www/html” 中创建`test.php`测试文件:
```
vim /var/www/html/test.php
```
2. 按字母“I”键或 “Insert” 键切换至编辑模式，写入如下内容：
```
<?php
echo "<title>Test Page</title>";
phpinfo()
?>
```
输入完成后，按“Esc”键，输入 “:wq”，保存文件并返回。
3. 在浏览器中，访问该`test.php`文件，查看环境配置是否成功：
```
http://云主机的公网 IP/test.php 
```
出现以下页面,则说明 LAMP 环境配置成功。
![环境验证](//mc.qcloudimg.com/static/img/3e2a1d07e4429d640461b64956b240cb/image.png)

### 步骤三：配置域名（可选）
您可以给自己的 Discuz! 论坛网站设定一个单独的域名。您的用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。但是有些用户没有域名，搭建论坛仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。
如果您使用 IP 直接安装，可以跳过此步骤，直接进行下一步骤。
如果您已有域名或者想要通过域名来访问您的论坛，可以参考以下步骤。
2. 请通过 [腾讯云购买域名](https://dnspod.qcloud.com/?from=qcloud)。 
3. 请进行 [网站备案](https://www.qcloud.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，一般审核时间为20天左右。
4. 通过腾讯云 [云解析](https://www.qcloud.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。
登录 [云解析控制台](https://console.qcloud.com/cns/domains)，选择域名或添加您已有的域名。
点击【解析】，进入该域名的域名记录管理界面。
![配置域名1](//mc.qcloudimg.com/static/img/c2e3da7449cf42697a15f5c2bf9e80cf/image.png)
点击【添加记录】，添加需要解析的记录。
![配置域名2](//mc.qcloudimg.com/static/img/4a5054890890418d83ced42db4f3a98a/image.png)

### 步骤四：安装 Discuz!  
#### 4.1 下载 Discuz! 
1. 腾讯云未内置 Discuz! 下载源，可以从 [Discuz! 官网](http://www.comsenz.com/downloads/install/discuzx) 下载安装包。
```
wget http://download.comsenz.com/DiscuzX/3.2/Discuz_X3.2_SC_UTF8.zip
```
2. 解压安装包。
```
unzip Discuz_X3.2_SC_UTF8.zip
```

#### 4.2 安装准备工作
1. 把解压后的 “upload”文件夹下的所有文件复制到 “/var/www/html/”。
```
cp -r upload/* /var/www/html/
```
2. 这些目录文件上传到服务器之后，默认只有 root 用户才有写权限，所以还要将写权限赋予给其他用户。
```
chmod -R 777 /var/www/html
```
#### 4.3 安装 Discuz!
至此，论坛已经完全搭建完毕，可以在浏览器中进行安装了。
1. 在 Web 浏览器地址栏输入步骤四中配置好的域名或 Discuz! 站点的 IP 地址（云主机的公网 IP 地址），可以看到 Discuz! 安装界面，就可以开始安装 Discuz! 了。单击【我同意】，然后选择【下一步】。
![安装1](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
2. 进入安装步骤第一步：检查安装环境，继续单击 【下一步】。
![安装2](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
3. 进入设置运行环境步骤，此教程中选择全新安装，继续【下一步】。
![安装3](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
4. 在安装数据库步骤中，为 Discuz! 创建一个数据库，使用步骤 2.2 设置的 root 账号和密码连接数据库。
**注意**：请记住自己的管理员用户和密码。
![安装4](//mc.qcloudimg.com/static/img/8aef8e7750a2cba4dfa0a39aacad8023/image.png)
5. 安装完成后，您可以访问论坛。
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)

