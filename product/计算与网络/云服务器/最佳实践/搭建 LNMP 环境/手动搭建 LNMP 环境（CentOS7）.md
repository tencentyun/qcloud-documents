## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档以 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 LNMP 环境。

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
2. 按 “**i**” 切换至编辑模式，写入以下内容。
```
[nginx] 
name = nginx repo 
baseurl = https://nginx.org/packages/mainline/centos/7/$basearch/ 
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
6. 按 “**i**” 切换至编辑模式，编辑 `nginx.conf` 文件。
用于取消对 IPv6 地址的监听，同时配置 Nginx，实现与 PHP 的联动。
>?找到 `nginx.conf` 文件中的 `#gzip on;`，另起一行并输入以下内容。
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
7. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
8. 执行以下命令启动 Nginx。
```
systemctl start nginx
```
9. 执行以下命令，设置 Nginx 为开机自启动。
```
systemctl enable nginx 
```
10. 在浏览器中，输入云服务器实例公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/fdc40877928729679d392eb304a3f12c.png)


### 步骤2：安装数据库
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
4. 按 “**i**” 切换至编辑模式，写入以下内容。
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
7. 执行以下命令，启动 MariaDB 服务。
```
systemctl start mariadb
```
8. 执行以下命令，设置 MariaDB 为开机自启动。
```
systemctl enable mariadb
```
9. 执行以下命令，验证 MariaDB 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/bfe9a604457f6de09933206c21fde13b.png)
10. 执行以下命令，退出 MariaDB。
```
\q
```


### 步骤3：安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm
```
```
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
2. 执行以下命令，安装 PHP 7.2.22 所需要的包。
```
yum -y install mod_php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-mysqlnd php72w-fpm.x86_64
```
3. 执行以下命令，启动 PHP-FPM 服务。
```
systemctl start php-fpm
```
4. 执行以下命令，设置 PHP-FPM 服务为开机自启动。
```
systemctl enable php-fpm
```




### 验证环境配置是否成功
当您完成环境配置后，可以通过以下验证 LNMP 环境是否搭建成功。
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 执行以下命令，重启 Nginx 服务。
```
systemctl restart nginx
```
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP
```
显示结果如下， 则说明环境配置成功。
![](https://main.qcloudimg.com/raw/640812413941a61efe29d7faa546ad80.png)


## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。




