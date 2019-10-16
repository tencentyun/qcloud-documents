## 操作场景
LNMP 环境代表 Linux 系统下 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档以 CentOS 6.9 及 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 LNMP 环境。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，详情请参见 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046)。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。


## 操作步骤

### 创建并登录云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看并获取云服务器的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/96a5f8e2eca54d4ea3ec56cb439b025a.png)
 - 云服务器用户名和密码。
 - 云服务器公网 IP。
3. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。

### 安装 Nginx
1. 执行以下命令，安装 Nginx。
```
yum -y install nginx
```
2. 执行以下命令，打开 `nginx.conf` 文件。
```
vim /etc/nginx/nginx.conf
```
3. 按 “**i**” 或 “**Insert**” 切换至编辑模式，将 `nginx.conf` 文件中 server{...} 的内容替换成以下内容。
用于取消对 IPv6 地址的监听，同时配置 Nginx，实现与 PHP 的联动。
```
server {
 listen       80;
 root   /usr/share/nginx/html;
 server_name  localhost;
 #charset koi8-r;
 #access_log  /var/log/nginx/log/host.access.log  main;
 #
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
     fastcgi_index  index.php;
     fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
     include        fastcgi_params;
  }
}
```
4. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
5. 根据安装操作系统的不同，依次执行对应命令启动 Nginx 并设置为开机自启动。
 - CentOS 6.9 请依次执行以下命令：
```
	 service nginx start
	 chkconfig --add nginx
	 chkconfig  nginx on
```
 - CentOS 7.6 请依次执行以下命令：
```
systemctl start nginx
systemctl enable nginx 
```
6. 在浏览器中，访问 CentOS 云服务器实例公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/aafa7ee638e68a8771953908a06fd704.png)

### 安装配置 PHP
由于操作系统版本不同，PHP 版本也不相同，请结合您使用的操作系统按照以下步骤进行安装配置 PHP。
#### CentOS 6.9 安装配置 PHP
1. 执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-6.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm
```
2. 执行以下命令，安装 PHP 7.1.32 所需要的包。
```
yum -y install mod_php71w.x86_64 php71w-cli.x86_64 php71w-common.x86_64 php71w-mysqlnd php71w-fpm.x86_64
```
3. 依次执行以下命令，启动 PHP-FPM 服务，同时设置为开机自启动。
```
service php-fpm start
chkconfig --add php-fpm  
chkconfig php-fpm on
```

#### CentOS 7.6 安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
2. 执行以下命令，安装 PHP 7.2.22 所需要的包。
```
yum -y install mod_php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-mysqlnd php72w-fpm.x86_64
```
3. 依次执行以下命令，启动 PHP-FPM 服务，同时设置为开机自启动。
```
systemctl start php-fpm
systemctl enable php-fpm
```

### 安装数据库
由于操作系统版本不同，数据库使用的版本也不相同，请对应您使用的操作系统进行安装配置。
#### CentOS 6.9 安装 MySQL
1. 执行以下命令，安装 MySQL。
```
yum install -y mysql55w-libs  mysql55w-server mysql55w-devel
```
2. 依次执行以下命令，启动 MySQL 服务，同时设置为开机自启动。
```
service mysqld start 
chkconfig --add mysqld
chkconfig mysqld  on 
```
3. 执行以下命令，验证 MySQL 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/9c9347ad0264ddad5e98c8dd48adcc6a.png)

#### CentOS 7.6 安装 MariaDB
1. 执行以下命令，查看系统中是否存在 MariaDB 现有包。 
```
rpm -qa | grep -i mariadb
```
返回结果类似如下内容，则表示已存在 MariaDB，请执行 [步骤2](#step2)。
![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
2. <span id="step2"></span>执行以下命令，删除 MariaDB 现有包。
```
yum -y remove 包名
```
3. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。
```
vi /etc/yum.repos.d/MariaDB.repo
```
4. 按 “**i**” 或 “**Insert**” 切换至编辑模式，写入以下内容。
```
# MariaDB 10.4 CentOS7-amd64
[mariadb]  
name = MariaDB  
baseurl = http://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64/
gpgkey = http://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```
>?腾讯云软件源站每天从各软件源的官网同步一次软件资源，请从 [MariaDB 软件源](http://mirrors.cloud.tencent.com/mariadb/yum/) 中获取最新地址。
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6. 执行以下命令，安装 MariaDB。
```
yum -y install MariaDB-client MariaDB-server
```
7. 依次执行以下命令，启动 MariaDB 服务，并设置为开机自启动。
```
systemctl start mariadb
systemctl enable mariadb
```
8. 执行以下命令，验证 MariaDB 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/bfe9a604457f6de09933206c21fde13b.png)

### 环境配置验证
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/index.php
```
 - CentOS 6.9 系统显示结果如下， 则说明环境配置成功。
![](https://main.qcloudimg.com/raw/aba0d414cc3954909b1e97fdc72bc4ea.png)
 - CentOS 7.6 系统显示结果如下， 则说明环境配置成功。
![](https://main.qcloudimg.com/raw/c47f6aab01fcf0cfcb716b69da7b0474.png)

