## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档以 CentOS 6.9 及 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 LNMP 环境。

## 技能要求
进行手动搭建 LNMP 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。
>!腾讯云建议您可以通过云市场的镜像环境部署 LNMP 环境，手动搭建 LNMP 环境可能需要较长的时间。具体步骤可参考 [使用镜像搭建 LNMP 环境](https://cloud.tencent.com/document/product/213/38053)。

## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已登录 Linux 云服务器。如果您还未登录，请准备好您云服务器的登录密码及公网 IP，参考 [使用标准方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 完成登录。


## 操作步骤
当您登录 Linux 云服务器后，可以按照以下步骤分别安装 Nginx， MySQL 和 PHP。

### 步骤1：安装 Nginx
1. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `nginx.repo` 文件。
```
vi /etc/yum.repos.d/nginx.repo
```
2. 按 “**i**” 或 “**Insert**” 切换至编辑模式，写入以下内容。
 - CentOS 6.9 请写入以下内容：
```
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/mainline/centos/6/$basearch/
gpgcheck=0
enabled=1
```
 - CentOS 7.6 请写入以下内容：
```
[nginx] 
name = nginx repo 
baseurl = https：//nginx.org/packages/mainline/centos/7/$basearch/ 
gpgcheck = 0 
enabled = 1
```
3. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
4. 执行以下命令，安装 nginx。
```
yum install nginx
```
5. 执行以下命令，打开 `nginx.conf` 文件。
```
vim /etc/nginx/nginx.conf
```
6. 按 “**i**” 或 “**Insert**” 切换至编辑模式，对应使用的操作系统编辑 `nginx.conf` 文件。
用于取消对 IPv6 地址的监听，同时配置 Nginx，实现与 PHP 的联动。
>?
>- 若在 http{...} 中已存在 server{...}，则请替换为以下内容。
>- 若在 http{...} 中无 server{..}，则请在 http{..} 中添加以下内容。
>
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
6. 在浏览器中，输入云服务器实例公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/fdc40877928729679d392eb304a3f12c.png)

### 步骤2：安装配置 PHP
由于操作系统版本不同，所使用的 PHP 的版本也不相同，请结合您使用的操作系统并按照以下步骤进行安装配置 PHP。
#### CentOS 6.9 安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
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

### 步骤3：安装数据库
由于操作系统版本不同，所使用的数据库版本也不相同，请对应您使用的操作系统并按照以下步骤进行进行安装配置。
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
 - 返回结果类似如下内容，则表示已存在 MariaDB，请执行 [步骤2](#step2) 依次移除。
![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
 - 返回结果类似如下内容，请执行 [步骤3](#step3) 开始安装 MariaDB。
![](https://main.qcloudimg.com/raw/2695390041ffef31032739281c91c228.png)
2. <span id="step2"></span>执行以下命令，删除 MariaDB 现有包。
```
yum -y remove 包名
```
3. <span id="step3"></span>执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。
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


### 验证环境配置是否成功
当您完成环境配置后，可以通过以下验证 LNMP 环境是否搭建成功。
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


## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。




