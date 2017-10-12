WordPress 是一款常用的搭建个人博客网站软件，该软件使用 PHP 语言和 MySQL 数据库开发。您可借助腾讯云云服务器 CVM，通过简单的操作即可运行 Wordpress，发布个人博客。本教程以 Linux 系统 CentOS 6.8 为例，搭建一个 WordPress 个人站点，具体操作方法如下：
![步骤流程](//mc.qcloudimg.com/static/img/6b7d99e96b495d10cd44624892c2ee46/image.png)
## 相关简介
以下是本教程中，将会使用的服务或工具：

**云服务器 CVM**：本教程使用腾讯云云服务器 CVM （以下简称 CVM ）创建云主机，来完成 WordPress 搭建工作。
 
**域名注册**：如果想要使用易记的域名访问您的 WordPress 站点，可以使用腾讯云域名注册服务来购买域名。
 
** 网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云为您的域名备案。

**云解析**：在配置域名解析之后，用户才能通过域名访问您的网站，而不需要使用复杂的 IP 地址。您可以通过腾讯云的云解析服务来解析域名。

**PuTTY**：PuTTY 是免费且出色的远程登录工具之一，本教程使用这款简单易操作的软件来完成相关搭建工作。点击 [下载 PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524)。

## 步骤 一：创建并运行云服务器
1. 请根据您的需要 [购买云服务器](https://buy.cloud.tencent.com/cvm?regionId=8&projectId=8)。
以下创建指引供您参考：
[创建 Linux 云服务器](https://cloud.tencent.com/document/product/213/2972)
2. 服务器创建成功后，您可登录 [腾讯云管理控制台](https://console.cloud.tencent.com/cvm)  查看或编辑云主机状态。
![云主机1](//mc.qcloudimg.com/static/img/cbd7d2717a9d162df28b4d517ab1d815/image.png)

本教程中云主机的操作系统版本为 CentOS 6.8。后续步骤将会用到以下信息，请注意保存：
- 云主机用户名和密码；
- 云主机公网 IP。

## 步骤 二：搭建 LNMP 环境
LNMP 是 Linux、Nginx、MySQL 和 PHP 的缩写，这个组合是最常见的 Web 服务器的运行环境之一。在创建好云主机之后，您可以开始进行 LNMP 环境搭建。
> Linux：Linux 系统（本文为 CentOS 6.8）；
Nginx：Web 服务器程序，用来解析 Web 程序；
MySQL：一个数据库管理系统；
PHP：Web 服务器生成网页的程序。

腾讯云提供了Yum下载源，在 CentOS 系统下，您可通过 Yum 快速安装软件。
> 搭建过程中将会用到 Yum 命令、Vim 命令以及相关 PuTTY 命令 。

### 2.1 运行 PuTTY 连接 Linux 云主机
1. 请 [下载 PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524) 到您的电脑，打开下载所在文件夹，解压文件；双击 “putty.exe”，出现配置界面。
2. 选择 “Session”，在 “Host Name (or IP address)” 输入框中输入欲访问的主机名或 IP，如 “server1” 或 “192.168.2.10”。本教程输入的是云主机的公网 IP。其他配置保持默认。
3. 在 “Saved Sessions” 输入栏中命名会话，单击 “Save” ，即可保存会话配置。
![putty1](//mc.qcloudimg.com/static/img/a7f57ac399e06522be67de3cf9d264e0/image.png)
4. 配置完成后单击 “Open” 按钮，将会出现确认证书的提示窗，请选择 “是” 。
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
出现登录界面，依次输入云主机的用户名和密码，就可连接到云主机，进行后续操作。
![putty3](//mc.qcloudimg.com/static/img/b632cf3e122832193a77afe04c93fbc1/image.png)

### 2.2 使用 Yum 安装必要软件
1. 登录云服务器后，默认已获取 root 权限。在 root 权限下，通过以下命令，先将必要软件一起安装 （Nginx、MySQL、PHP）：
```
yum install nginx php php-fpm php-mysql mysql-server -y
```
安装完成，PuTTY 窗口会提示“Complete!”。同时可以上滑滚动条查看当前安装包版本：
![安装软件2](//mc.qcloudimg.com/static/img/54fe7152ded20d5048728b5b98566eb6/image.png)
本教程中安装包版本分别如下：
Nginx：1.10.2
MySQL：5.1.73
PHP：5.3.3
2. 将各软件设置为开机启动：
```
chkconfig nginx on
chkconfig mysqld on
chkconfig php-fpm on
```

更多详细操作，可参考 [CentOS 环境下通过 Yum 安装软件](https://cloud.tencent.com/document/product/213/2046)。

### 2.3 软件配置
将 Nginx、MySQL、PHP 等各软件安装好之后，还需要对各软件分别进行配置。以下是详细步骤：
#### 2.3.1 配置 Nginx
1. 请使用 Vim 命令打开`default.conf`文件，取消对 IPv6 地址的监听同时配置 Nginx，实现与 PHP 的联动。
```
vim /etc/nginx/conf.d/default.conf
```
2. 按字母“I”键或 “Insert” 键切换至编辑模式，将已有内容全部清除，复制并粘贴以下内容到 `default.conf`文件。
<div class="code"><p></p><pre> 
server {
    listen       80;
    root   /usr/share/nginx/html;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;

    location / {
            index index.php index.html index.htm;
    }

    #error_page  404              /404.html;

    #redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    #pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    location ~ .php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index   index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
     }

 }</pre></div>
修改完成后，按 “Esc” 键，输入 “:wq”，保存文件并返回。
3. 启动 Nginx。
```
service nginx start
```

4. 测试 Nginx 服务是否正常运行
在浏览器中，访问 CentOS 云主机公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明 Nginx 安装配置成功：
![ 测试Nginx2](//mc.qcloudimg.com/static/img/1a992f4caab3388effc70a856eaac941/image.png)
 
#### 2.3.2 配置 MySQL
1. 启动 MySQL 服务器。
```
service mysqld start
```
2. 设置 MySQL 服务器 root 用户的密码，本教程设置为 “123456”，后续步骤中需要用到此用户名和密码。
```
 /usr/bin/mysqladmin -u root password "123456"
```

#### 2.3.3 配置 PHP
1. 启动 PHP-FPM 服务。
```
service php-fpm start
```
2. 配置 PHP Session 的存储路径。
打开`/etc/php.ini`文件。
```
vim /etc/php.ini
```
进入后直接输入以下内容，回车定位到 “session.save_path” 的位置：
```
/session.save_path
```
按字母“I”键或 “Insert” 键切换至编辑模式，将其改为  ：
```
session.save_path = "/var/lib/php/session"
```
![配置php1](//mc.qcloudimg.com/static/img/0fad1c31cd587308d8a068d767d9a9b8/image.png)
更改`/var/lib/php/session`目录下所有文件的属组都改成 nginx 和 nginx。
```
chown -R nginx:nginx /var/lib/php/session 
``` 
 
#### 2.3.4 验证环境配置
1. 请使用以下命令在 Web 目录下创建`index.php`文件：
```
vim /usr/share/nginx/html/index.php
```
2. 按字母“I”键或 “Insert” 键切换至编辑模式，写入如下内容：
```
<?php
echo "<title>Test Page</title>";
echo "Hello World!";
?>
```
输入完成后，按“Esc”键，输入 “:wq”，保存文件并返回。
3. 在浏览器中，访问该`index.php`文件，查看环境配置是否成功：
```
http://云主机的公网 IP/index.php 
```
页面显示 “Hello World!”，则说明 LNMP 环境配置成功。
![验证环境1](//mc.qcloudimg.com/static/img/88de64e6ff862edfeae10acb2ee787ec/image.png)

## 步骤 三：安装和配置 WordPress
### 3.1 下载 WordPress
腾讯云提供了 Yum 下载源，但内置 WordPress 安装包为英文版，考虑到用语习惯，您也可以从 [WordPress 官方网站](https://cn.wordpress.org/) 下载 WordPress 中文版本并安装。本教程正是采用的 WordPress 中文版本。
1. 先删除网站根目录下的`index.html`文件。
```
rm /usr/share/nginx/html/index.html
```
窗口提示是否删除，输入 “y” 回车。

2. 依次下载 WordPress 并解压到当前目录。
```
wget https://cn.wordpress.org/wordpress-4.7.4-zh_CN.tar.gz
```
```
tar zxvf wordpress-4.7.4-zh_CN.tar.gz
```

### 3.2 配置数据库
在写博客之前，您需要先建好数据库，以存储各类数据。请根据以下步骤进行 MySQL 数据库配置。
1. 登录 MySQL 服务器。
使用 root 用户登录到 MySQL 服务器。
```
mysql -uroot -p
```
在系统提示时，输入密码（步骤 2.3.2 已设置 MySQL root 用户的密码为 123456）登录。

2. 为 WordPress 创建数据库并设置用户名和密码（本教程设置如下，您可自行定义）。
为 WordPress 创建 MySQL 数据库 “wordpress”。
```
CREATE DATABASE wordpress;
```
为已创建好的 MySQL 数据库创建一个新用户 “user@localhost”。
```
CREATE USER user@localhost;
```
并为此用户设置密码“wordpresspassword”。
```
SET PASSWORD FOR user@localhost=PASSWORD("wordpresspassword");
```

3. 为创建的用户开通数据库 “wordpress” 的完全访问权限。
```
GRANT ALL PRIVILEGES ON wordpress.* TO user@localhost IDENTIFIED BY 'wordpresspassword';
```

4. 使用以下命令使所有配置生效。
```
FLUSH PRIVILEGES;
```

5. 配置完成，退出 MySQL。
```
exit
```

### 3.3 写入数据库信息
完成数据库配置后，还需要将数据库信息写入 WordPress 的配置文件。WordPress 安装文件夹包含名为 wp-config-sample.php 的示例配置文件。本步骤将复制此文件并进行编辑以适应具体配置。 
1. 创建新配置文件
将`wp-config-sample.php`文件复制到名为`wp-config.php`的文件,使用以下命令创建新的配置文件，并将原先的示例配置文件保留作为备份。
```
cd wordpress/
cp wp-config-sample.php wp-config.php
```
2. 打开并编辑新创建的配置文件。
```
vim wp-config.php
```
找到文件中 MySQL 的部分，按字母“I”键或 “Insert” 键切换至编辑模式，将步骤 3.2 中已配置好的数据库相关信息写入：

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'user');

/** MySQL database password */
define('DB_PASSWORD', 'wordpresspassword');

/** MySQL hostname */
define('DB_HOST', 'localhost');
```
修改完成后，按“Esc”键，输入“:wq”，保存文件返回。

### 3.4 安装 WordPress
步骤 3.1 到 3.3，已解压了安装文件夹、创建了 MySQL 数据库与用户并自定义了 WordPress 配置文件，此步骤开始完成 WordPress 的安装。
1. 移动安装文件至 Web 服务器文档根目录，以便可以运行安装脚本完成安装。
```
mv * /usr/share/nginx/html/
```
2. 在 Web 浏览器地址栏输入 WordPress 站点的 IP 地址（云主机的公网 IP 地址，或者该地址后跟 “wordpress文件夹”），可以看到 WordPress 安装屏幕，就可以开始配置 WordPress。
![配置WP1](//mc.qcloudimg.com/static/img/6012d2bcc2f5a5a78e333e57f08545f6/image.png)
3. 将其余安装信息输入WordPress 安装向导，单击 “安装 WordPress” 完成安装。

| 所需信息 | 备注 | 
|---------|---------|
| 站点标题 |  WordPress 网站名称。 |
| 用户名 | WordPress 管理员名称。出于安全考虑，建议设置一个不同于 admin 的名称。因为与默认用户名称 admin 相比，该名称更难破解。 |
| 密码 | 可以使用默认强密码或者自定义密码。请勿重复使用现有密码，并确保将密码保存在安全的位置。 |
| 您的电子邮件 | 用于接收通知的电子邮件地址。 | 

现在可以用登录 WordPress 博客，并开始发布博客文章了。

## 后续步骤
1. 您可以给自己的 WordPress 博客网站设定一个单独的域名。您的用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。
您可以通过 [腾讯云购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)。 

2. 域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。备案免费，一般审核时间为20天左右。
3. 您需要在腾讯云 [云解析](https://console.cloud.tencent.com/cns/domains)上配置域名解析之后，用户才能通过域名访问您的网站，指引参考 [域名解析](https://cloud.tencent.com/document/product/302/3446)。


此外，您还可以在腾讯云平台横向和纵向扩展服务容量，例如：
- 扩展单个 CVM 实例的 CPU 和内存规格，增强服务器的处理能力。[了解详情 >>](https://cloud.tencent.com/document/product/213/5730)
- 增加多台 CVM 实例，并利用 [负载均衡](https://cloud.tencent.com/document/product/214)，在多个实例中进行负载的均衡分配。
- 利用 [弹性伸缩](https://cloud.tencent.com/document/product/377)，根据业务量自动增加或减少 CVM 实例的数量。
- 利用 [对象存储](https://cloud.tencent.com/document/product/436)，存储静态网页和海量图片、视频等。

您还可以参考以下视频，完成 WordPress 在 Ubuntu 上的搭建。
> 注：视频中演示操作界面仅为参考，请以实际操作界面为准。

**查看视频：**
