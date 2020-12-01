## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LNMP 环境。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，请参见  [openSUSE 环境下通过 zypper 安装软件](https://cloud.tencent.com/document/product/213/2047)。

## 示例软件版本
本文搭建的 LNMP 环境软件组成版本及说明如下：
- Linux：Linux 系统，本文以 openSUSE 42.3 为例。
- Nginx：Web 服务器程序，用来解析 Web 程序，本文以 Nginx1.14.2 为例。
- MySQL：一个数据库管理系统，本文以 MySQL5.6.43 为例。
- PHP：Web 服务器生成网页的程序，本文以 PHP7.0.7 为例。

## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：配置镜像源
1. 登录云服务器。
2. 执行以下命令，添加镜像源。
```
zypper ar https://mirrors.cloud.tencent.com/opensuse/distribution/leap/42.3/repo/oss suseOss
zypper ar https://mirrors.cloud.tencent.com/opensuse/distribution/leap/42.3/repo/non-oss suseNonOss
```
3. 执行以下命令，更新镜像源。
```
zypper ref
```

### 步骤3：安装配置 Nginx
1. 执行以下命令，安装 Nginx。
``` 
zypper install -y nginx
```
2. 依次执行以下命令，启动 Nginx 服务并设置为开机自启动。
```
systemctl start nginx
systemctl enable nginx
```
3. 执行以下命令，修改 Nginx 配置文件。
```
vim /etc/nginx/nginx.conf
```
4. 按 “**i**” 切换至编辑模式。
5. 找到 server{...} 并将其替换成以下内容。
```
server {
	listen       80;
	server_name  localhost;
	#access_log  /var/log/nginx/host.access.log  main;
	location / {
			root   /srv/www/htdocs/;
			index  index.php index.html index.htm;
	}
	#error_page  404              /404.html;
	# redirect server error pages to the static page /50x.html
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
			root   /srv/www/htdocs/;
	}
	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {
			root           /srv/www/htdocs/;
			fastcgi_pass   127.0.0.1:9000;
			fastcgi_index  index.php;
			fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
			include        fastcgi_params;
	}
}
```
7. 输入完成后，按 “**Esc**” ，输入 “**:wq**”，保存文件并返回。
8. 执行以下命令，重启 Nginx 服务。
```
systemctl restart nginx
```
9. 执行以下命令，新建`index.html`首页。
```
vi /srv/www/htdocs/index.html
```
10. 按 “**i**” 切换至编辑模式，输入以下内容：
```html
<p> hello world!</p>
```
10. 输入完成后，按 “**Esc**” ，输入 “**:wq**”，保存文件并返回。
11. 在浏览器中，访问 openSUSE 云服务器实例公网 IP，查看 Nginx 服务是否正常运行。
如下图所示，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/df09d1fe6baed50cebd89ef7402db4b2.png)

### 步骤4：安装配置 MySQL
1. 执行以下命令，安装 MySQL。
```
zypper install -y mysql-community-server mysql-community-server-tools
```
2. 依次执行以下命令，启动 MySQL 服务并设置为开机自启动。
```
systemctl start mysql 
systemctl enable mysql
```
3. 执行以下命令，首次登录 MySQL。
>? 首次登录 MySQL 时，系统将提示输入密码，若不进行输入密码的操作，可直接按 “**Enter**” 进入 MySQL。
>
```
mysql -u root -p
```
成功进入 MySQL，如下图所示。
![](https://main.qcloudimg.com/raw/1e9daf876fb08c70674789865688f695.png)
4. 执行以下命令，修改 root 密码。
```
update mysql.user set password = PASSWORD('此处输入您新设密码') where user='root';
```
5. 执行以下命令，使配置生效。
```
flush privileges;
```
6. 执行以下命令，退出 MySQL。
```
\q
```

### 步骤5：安装配置 PHP
执行以下命令，安装 PHP。
```
zypper install -y php7 php7-fpm php7-mysql
```

### 步骤6：Nginx 与 PHP-FPM 集成
1. 依次执行以下命令，进入 `/etc/php7/fpm` 目录，将 `php-fpm.conf.default` 文件复制并重命名为 `php-fpm.conf` 文件。
```
cd /etc/php7/fpm
cp php-fpm.conf.default php-fpm.conf
``` 
2. 依次执行以下命令，进入 `/etc/php7/fpm/php-fpm.d` 目录，将 `www.conf.default` 文件复制并重命名为 `www.conf` 文件。
```
cd /etc/php7/fpm/php-fpm.d
cp www.conf.default www.conf
```
4. 依次执行以下命令，启动服务并设置为开机自启动。
```
systemctl start php-fpm
systemctl enable php-fpm
```

## 验证环境配置
1. 执行以下命令，创建测试文件 index.php。
```
vim /srv/www/htdocs/index.php
```
2. 按 “**i**” 切换至编辑模式，写入如下内容：
```
<?php
	echo "hello new world!";
?>
```
3. 按 “**Esc**” 键，输入 “**:wq**”，保存文件并返回。
4. 在浏览器中，访问 openSUSE 云服务器公网 IP。
如下图所示，则 LNMP 环境搭建成功。
![](https://main.qcloudimg.com/raw/0adc6168e7407931c597228520b35413.png)

## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行[ 手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。







