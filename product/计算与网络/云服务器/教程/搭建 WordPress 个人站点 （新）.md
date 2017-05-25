WordPress 是一款常用的搭建个人博客网站软件，该软件使用 PHP 语言和 MySQL 数据库开发。您可借助腾讯云云服务器 CVM，通过简单的操作即可运行 Wordpress，发布个人博客。具体操作方法如下：
## 相关简介
以下是您在本教程中，将会使用的服务或工具：

**云服务器 CVM**：您将使用腾讯云云服务器 CVM （以下简称 CVM ）创建云主机，来完成搭建 WordPress 搭建工作。

**PuTTY**：PuTTY 是免费且出色的远程登录工具之一，您将使用这款简单易操作的软件来完成相关搭建工作。点击 [下载 PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524)。

## 步骤 1：创建并运行云服务器
1. 请根据您的需要 [创建云服务器](https://buy.qcloud.com/cvm?regionId=8&projectId=8)。
以下创建指引供您参考：
[创建 Windows 云服务器](https://www.qcloud.com/document/product/213/2763)
[创建 Linux 云服务器](https://www.qcloud.com/document/product/213/2972)
2. 服务器创建成功后，您可登录 [腾讯云管理控制台](https://console.qcloud.com/cvm)  查看或编辑云主机状态。
![云主机1](//mc.qcloudimg.com/static/img/45c91766dea3e929af02e31dc029b9b0/image.png)

本教程中创建的云主机配置及系统镜像信息如下：
 
| 信息 | 参数 | 
|---------|---------|
| 操作系统 | CentOS 6.8 64位 |
| CPU | 1核|
|内存 | 1GB|
|系统盘|	20GB(本地磁盘)|
|数据盘|	30GB(本地磁盘)|
|公网带宽|	1Mbps|
|镜像名称|	CentOS 6.8 64位|
|类型|	公有镜像|

后续步骤将会用到以下信息，请注意保存：
云主机用户名和密码；
云主机公网 IP。

## 步骤 2：搭建 LNMP 环境
LNMP 是 Linux、Nginx、MySQL 和 PHP 的缩写，这个组合是最常见的 Web 服务器的运行环境之一。在创建好云主机之后，您可以开始进行 LNMP 环境搭建。
> Linux：Linux 环境（本文为 CentOS 6.8）；
Nginx：Web 服务器程序，用来解析 Web 程序；
MySQL：一个数据库管理系统；
PHP：Web 服务器生成网页的程序。

本教程适用于 CentOS 6.x 版本，以 CentOS 6.8 为例，搭建一套 LNMP 环境。腾讯云提供了Yum下载源，在 CentOS 系统下，您可通过 Yum 快速安装软件。
> 搭建过程中将会用到 Yum 命令、Vi 命令以及相关 PuTTY 命令 。

### 2.1 运行 PuTTY 连接 Linux 云主机
1. 请下载 PuTTY 到您的电脑，打开下载所在文件夹，解压文件；双击 `putty.exe`，出现配置界面。
2. 选择 `Session` ，在 `Host Name (or IP address)` 输入框中输入欲访问的主机名或 IP，如 “server1” 或 “192.168.2.10”。本教程输入的是已启动的云主机公网 IP：119.29.228.67。其他配置保持默认。
3. 在 `Saved Session` 输入栏中命名会话，单击 “Save” ，即可保存会话配置。
![putty1](//mc.qcloudimg.com/static/img/6495f1d572e504235ed7b02beb1d1dc3/image.png)
4. 配置完成后单击 “Open” 按钮，将会出现确认证书的提示窗，请选择 “是” 。
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
出现登录界面，依次输入云主机的用户名和密码，就可连接到云主机，进行后续操作。
![putty3](//mc.qcloudimg.com/static/img/f77d788bccec02c0fa936fe295bb5103/image.png)

### 2.2 使用 Yum 安装必要软件
1. 登录操作系统为 CentOS 的云服务器后，默认已获取 root 权限。在 root 权限下，通过以下命令来安装必要软件 （Nginx、MySQL、PHP）：
```
yum install nginx php php-fpm php-mysql mysql-server -y
```
安装完成，PuTTY 窗口会提示“Complete!”。
![安装软件1](//mc.qcloudimg.com/static/img/5eab9d11f7f6fe299613a0ac5cec0fc0/image.png)
同时可以上滑滚动条查看当前安装包版本：
![安装软件2](//mc.qcloudimg.com/static/img/b2c0d28096e5089d58590fdc4d64ebc7/image.png)

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
> 更多详细操作，可参考[ CentOS 环境下通过 Yum 安装软件](https://www.qcloud.com/document/product/213/2046)。

### 2.3 软件配置
将 Nginx、MySQL、PHP 等各软件安装好之后，还需要对各软件分别进行配置。以下是详细步骤：
#### 2.3.1 配置 Nginx
1. 请使用 Vi 命令打开`default.conf`文件，取消对 IPv6 地址的监听同时配置 Nginx，实现与 PHP 的联动。文件路径： `/etc/nginx/conf.d/default.conf`。
```
vi /etc/nginx/conf.d/default.conf
```

2. 按字母“I”键或 “Insert” 键切换至编辑模式，将已有内容全部清除，复制并粘贴（Vim 命令下，单击鼠标右键即可执行粘贴操作）以下内容到 `default.conf`文件。
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
修改完成后，按“Esc”键，输入“:wq”，保存文件并返回。
3. 启动 Nginx：
```
service nginx start
```

3. 测试 Nginx 服务是否正常运行
在浏览器中，访问 CentOS 云主机公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明Nginx安装配置成功：
![ 测试Nginx2](//mc.qcloudimg.com/static/img/807692945e05c68f7fe5d24c6b186f2f/image.png)

#### 2.3.2 配置 MySQL
1. 启动 MySQL 服务：
```
service mysqld restart
```
2. 设置 MySQL 服务账户名和密码，本教程设置用户名为 root，密码为 123456，后续步骤中需要用到此用户名和密码：
```
 /usr/bin/mysqladmin -u root password "123456"
```
![mysql2](//mc.qcloudimg.com/static/img/46b5580b98423eb171ac8759d8bce5d1/image.png)

#### 2.3.3 配置 PHP
1. 请使用以下命令启动 PHP-FPM 服务：
```
service php-fpm start
```
2. 配置 PHP Session 的存储路径。
打开`/etc/php.ini`文件。
```
vi /etc/php.ini
```
进入后直接输入：
```
/session.save_path
```
按字母“I”键或 “Insert” 键切换至编辑模式，将其改为  ：
```
session.save_path =  “/var/lib/php/session”
```
![配置php1](//mc.qcloudimg.com/static/img/50036b980ac464375c51d2d78177de36/image.png)
更改`/var/lib/php/session`目录下的用户组：
```
chown -R nginx:nginx /var/lib/php/session 
``` 

#### 2.3.4 验证环境配置
1. 请使用以下命令在 Web 目录下创建`index.php`文件：
```
vi /usr/share/nginx/html/index.php
```
2. 按字母“I”键进入 INSERT 模式，写入如下内容（Vim 命令下，单击鼠标右键即可执行粘贴操作）：
```
<?php
echo "<title>Test Page</title>";
echo "Hello World!";
?>
```
输入完成后，按“Esc”键，输入 “:wq”，保存文件并返回。
3. 在浏览器中，访问该`index.html` 文件，查看环境配置是否成功：
```
http://119.29.228.67/index.php
```
```
http://CentOS 云主机的公网 IP/index.php 
```
页面显示 “Hello World!”，则说明 LNMP 环境配置成功。
![验证环境1](//mc.qcloudimg.com/static/img/9da10fc81a5ca2af45d1a39727d5b84a/image.png)

## 步骤 3：安装和配置 WordPress
### 3.1 下载和安装 WordPress
腾讯云提供了Yum下载源，但内置 WordPress 安装包为英文版，出于方便使用的考虑，本教程从[ WordPress 官方网站](https://cn.wordpress.org/)下载 WordPress 中文版本并安装。
1. 先删除网站根目录下的`index.html`文件。
```
rm /usr/share/nginx/html/index.html
```
窗口提示是否删除，输入 “y” 回车。
![安装WP0](//mc.qcloudimg.com/static/img/54b9ca3f101b22e8323266120b9e427b/image.png)
2. 依次下载 WordPress 并解压到当前目录。
```
wget https://cn.wordpress.org/wordpress-4.7.4-zh_CN.tar.gz
```
```
tar zxvf wordpress-4.7.4-zh_CN.tar.gz
```
3. 将已解压的所有文件移动到网站根目录 `/usr/share/nginx/html/` 。 
```
mv wordpress/* /usr/share/nginx/html/
```
窗口提示是否覆盖原文件，输入 “y” 回车。
4. 修改`html`文件夹权限为 777，赋予文件或目录最大读写权限（配置完成后，改回 755）。
```
chmod -R 777 /usr/share/nginx/html
```

### 3.2 配置数据库
在写博客之前，您需要先建好数据库，以存储各类数据。请根据以下步骤进行 MySQL 数据库配置。
1. 进入 MySQL：
```
mysql -uroot -p
```
输入root用户的密码（本教程中 MySQL 用户 root 的密码已设置为 123456）进入 MySQL。
![配置数据库1](//mc.qcloudimg.com/static/img/dc2420d8a32c659d40872d2aef5e4717/image.png)
2. 为 WordPress 创建数据库并设置用户名和密码。
本教程中将数据库命名为`wordpress` （以下称为`wordpress 数据库`）：
```
CREATE DATABASE wordpress;
```
 为 `wordpress 数据库`创建一个新用户，本教程中，用户名设置为`user@localhost`：
```
CREATE USER user@localhost;
```
并为此用户设置密码，如`wordpresspassword`：
```
SET PASSWORD FOR user@localhost=PASSWORD("wordpresspassword");
```
3. 为新用户开通访问`wordpress 数据库`的权限并使之生效：
```
GRANT ALL PRIVILEGES ON wordpress.* TO user@localhost IDENTIFIED BY 'wordpresspassword';
```
使用以下命令使权限生效：
```
FLUSH PRIVILEGES;
```
4. 配置完成，退出 MySQL：
```
quit
```

### 3.3 写入数据库信息
完成数据库配置后，还需要将数据库信息写入 WordPress 的配置文件。
1. 打开配置文件
使用以下命令打开 WordPress 的配置文件：
```
vi /usr/share/nginx/html/wp-config-sample.php
```
找到文件中 MySQL 的部分，按字母“I”键进入 INSERT 模式（Vim 命令下，单击鼠标右键即可执行粘贴操作），将3.1 中已配置好的数据库相关信息写入：

<div class="code"><p></p><pre> 
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', <font color="red">'wordpress'</font>);

/** MySQL database username */
define('DB_USER', <font color="red">'user'</font>);

/** MySQL database password */
define('DB_PASSWORD', <font color="red">'wordpresspassword'</font>);

/** MySQL hostname */
define('DB_HOST', 'localhost');
</div></pre>
修改完成后，按“Esc”键，输入“:wq”，保存文件并返回。

### 3.4 配置 WordPress
在配置好环境后，在浏览器地址栏输入 IP 地址，就可以开始配置 WordPress。
```
http://119.29.228.67
```
```
http://公网IP
```

1. 在出现的页面中配置站点名称，用户名和密码，点击安装，完成后进入登录页面。
![配置WP1](//mc.qcloudimg.com/static/img/7a73ea1be112aa80891e74684c0fccf0/image.png)
![配置WP2](//mc.qcloudimg.com/static/img/8f3b3291b7a90554af392a66ab0cf64e/image.png)
2. 输入刚才设置的用户名和密码，点击登录。
![配置WP3](//mc.qcloudimg.com/static/img/3d24a1747ba899a1d3812e8f30992a8a/image.png)
3. 成功登录到网站管理后台（中文称为仪表盘）。可在仪表盘对网站进行管理，如更换网站主题、发表文章等。
![配置WP4](//mc.qcloudimg.com/static/img/9b543d0311fba3de07ca954ef5e4a733/image.png)
4. 此时，其他用户通过访问以下地址，即可看到网站。
```
http://119.29.228.67
```
![配置WP5](//mc.qcloudimg.com/static/img/a7360313672aa00c6c90a1050c562538/image.png)
5. 配置完成后， 将`html`文件夹权限改回 755。您就可以开启个人博客之旅了。
```
chmod -R 755 /usr/share/nginx/html
```
