## 操作场景
WordPress 是一款常用的搭建个人博客网站软件，该软件使用 PHP 语言开发。您可通过在腾讯云服务器的简单操作部署 WordPress，发布个人博客。

本文介绍手动部署 WordPress 的方法，如果您的网站对可扩展性需求要求不高，腾讯云还提供镜像的方式部署  WordPress，具体可参考 [使用镜像部署 WordPress](https://cloud.tencent.com/document/product/213/9740)。

本教程以 Linux 系统 CentOS 7.5 为例，搭建一个 WordPress 个人站点，具体操作方法如下：
![步骤流程](https://main.qcloudimg.com/raw/350c12570478973b9ecd293760c5fde6.png)

## 相关简介
以下是本教程中，将会使用的服务或工具：
- **云服务器**：本教程使用腾讯云云服务器（Cloud Virtual Machine，CVM）创建云服务器实例，用来完成 WordPress 搭建工作。
- **域名注册**：如果您想要使用易记的域名访问您的 WordPress 站点，可以使用腾讯云域名注册服务来购买域名。
- **网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云 [网站备案](https://cloud.tencent.com/product/ba) 产品为您的域名备案。
- **云解析**：配置域名解析后，用户可通过域名访问您的网站，不需要使用复杂的 IP 地址才可访问您的网站。您可以通过腾讯云的 [云解析](https://cloud.tencent.com/product/cns) 服务来解析域名。

## 前提条件

已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤 
### 创建并登录云服务器
>! 此步骤针对全新购买云服务器。如果您已购买云服务器实例，可以通过重装系统选择 WordPress 建站系统。
>
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回至 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看和获取实例的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/3f015e2decf3a89e0fa03a5bf32e13a4.png)    
 - 云服务器实例用户名和密码
 - 云服务器实例公网 IP

### 搭建 LNMP 环境
LNMP 是 Linux、Nginx、MariaDB 和 PHP 的缩写，这个组合是最常见的 Web 服务器的运行环境之一。在创建并登录云服务器实例之后，您可以开始进行 LNMP 环境搭建。
LNMP 组成及使用版本说明：
- Linux：Linux 系统，本文使用 CentOS7.5
- Nginx：Web 服务器程序，用来解析 Web 程序，本文使用 Nginx1.12.2
- MariaDB：一个数据库管理系统，本文使用 MariaDB10.4.6
- PHP：Web 服务器生成网页的程序，本文使用 PHP7.2.19

#### 使用 yum 安装软件和配置
登录云服务器后，默认已获取 root 权限。在 root 权限下，根据以下步骤分步安装。

#### 安装配置 Nginx 
1. 执行以下命令，安装 Nginx。  
```
yum -y install nginx
```
2. 执行以下命令，打开`nginx.conf`文件。
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
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6. 依次执行以下命令，启动 Nginx ，设置为开机自启动。
```
systemctl start nginx
systemctl enable nginx 
```
7. 在浏览器中，访问 CentOS 云服务器实例公网 IP，查看 Nginx 服务是否正常运行。
显示如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/c23831d2579d747625e96afbf45766bb.png)

#### 安装配置 PHP
>? 以下操作以 PHP7.2.19 版本为例。
>
1. 执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
2. 执行以下命令，查看可安装的 PHP7.2.19 的所有包。
```
yum search php72w
```
3. 执行以下命令，安装需要的包。
```
yum -y install mod_php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-mysqlnd php72w-fpm.x86_64
```
4. 依次执行以下命令，启动 PHP-FPM 服务，同时设置为开机自启动。
```
systemctl start php-fpm
systemctl enable php-fpm
```


#### 验证 PHP-Nginx 环境配置
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 在浏览器中，访问该`index.php`文件，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/index.php 
```
页面显示如下，则说明 PHP-Nginx 环境配置成功。
![](https://main.qcloudimg.com/raw/62cac02b422515364d8713062017c9e1.png)

#### 安装配置 MariaDB
1. 执行以下命令，查看系统中是否存在 MariaDB 现有包。
```
rpm -qa | grep -i mariadb
```
返回结果类似如下内容，则表示已存在 MariaDB，请执行 [步骤2](#step2)。
![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
2. <span id="step2">执行以下命令，删除 MariaDB 现有包。</span>
```
yum -y remove 包名
```
3. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。
```
vi /etc/yum.repos.d/MariaDB.repo
```
4. 按 **i** 切换至编辑模式，写入并保存以下内容。
```
# MariaDB 10.4 CentOS7-amd64
[mariadb]  
name = MariaDB  
baseurl = http://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64/
gpgkey = http://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1  
```
>? 腾讯云软件源站每天从各软件源的官网同步一次软件资源，请从 [MariaDB 软件源](http://mirrors.cloud.tencent.com/mariadb/yum/) 中获取最新地址。
> 
5. 执行以下命令，清除 yum 缓存。
```
yum clean all
```
6. 执行以下命令，安装 MariaDB。
```
yum -y install MariaDB-client MariaDB-server
```
7. 依次执行以下命令，启动 MariaDB 服务，并设置为开机自启动。
```
systemctl start mariadb
systemctl enable mariadb
```
8. <span id="login">执行以下命令，设置 root 帐户登录密码及基础配置。</span>
>! 
>- 针对首次登录 MariaDB 的用户需执行以下命令进入用户密码及基础设置。
>- 首次输入 root 帐户密码后，需按 “**Enter**”（设置 root 密码时界面默认不显示），并再次输入 root 密码进行确认。请通过界面上的提示完成基础配置。
>
```
mysql_secure_installation
```
9. 执行以下命令，登录 MariaDB，并输入 [步骤5](#login) 设置的密码，按 “**Enter**”。
```
mysql -uroot -p
```
 显示结果如下，则已成功进入 MariaDB。
![](https://main.qcloudimg.com/raw/cd3996d219c989911dbc3eb397047ce4.png)
10. 执行以下命令，退出 MariaDB。
```
\q
```

### 安装和配置 WordPress
#### 下载 
>? WordPress 可从 [WordPress 官方网站](https://cn.wordpress.org/download/releases/) 下载 WordPress 最新中文版本并安装，本教程采用 WordPress 中文版本。
>
1. 执行以下命令，删除网站根目录下用于测试 PHP-Nginx 配置的`index.php`文件。
```
rm -rf /usr/share/nginx/html/index.php
```
2. 依次执行以下命令，进入`/usr/share/nginx/html/`目录，并下载与解压 WordPress。
```
cd /usr/share/nginx/html
wget https://cn.wordpress.org/wordpress-5.0.4-zh_CN.tar.gz
tar zxvf wordpress-5.0.4-zh_CN.tar.gz
```

<span id="database"></span>

#### 配置数据库
在写博客之前，需要先建好数据库，以存储各类数据。请根据以下步骤进行 MariaDB 数据库配置。
1. 执行以下命令，使用 root 用户登录到 MariaDB 服务器。
```
mysql -uroot -pXXXXX（XXXXX 表示安装 MariaDB 时设置的登录密码）
```
2. 执行以下命令，创建 MariaDB 数据库。例如 “wordpress”。
```
CREATE DATABASE wordpress;
```
3. 执行以下命令，创建一个新用户。例如 “user”。
```
CREATE USER user;
```
4. 执行以下命令，为 “user” 用户设置密码。例如 “wordpresspassword”。
```
SET PASSWORD FOR user=PASSWORD("wordpresspassword");
```
5. 执行以下命令，赋予用户对 “wordpress” 数据库的全部权限。
```
GRANT ALL PRIVILEGES ON wordpress.* TO user IDENTIFIED BY 'wordpresspassword';
```
6. 执行以下命令，使所有配置生效。
```
FLUSH PRIVILEGES;
```
7. 执行以下命令，退出 MariaDB。
```
\q
```

####  写入数据库信息
1. 依次执行以下命令，进入 WordPress 安装目录，将`wp-config-sample.php`文件复制到`wp-config.php`文件中，并将原先的示例配置文件保留作为备份。
```
cd /usr/share/nginx/html/wordpress
cp wp-config-sample.php wp-config.php
```
2. 执行以下命令，打开并编辑新创建的配置文件。
```
vim wp-config.php
```
3. 按 “**i**” 或 “**Insert**” 切换至编辑模式，找到文件中 MySQL 的部分，将 [配置数据库](#database) 中已配置好的数据库相关信息写入。
```
	// ** MySQL settings - You can get this info from your web host ** //
	/** The name of the database for WordPress */
	define('DB_NAME', 'wordpress');
	
	/** MySQL database username */
	define('DB_USER', 'user');
	
	/** MySQL database password */
	define('DB_PASSWORD', 'wordpresspassword');
	
	/** MySQL hostname */
	define('DB_HOST', '127.0.0.1');
```
4. 修改完成后，按“**Esc**”，输入“**:wq**”，保存文件返回。

#### 验证 WordPress 安装
1. 在浏览器地址栏输入云服务器实例的公网 IP 加上 worspress 文件夹，例如：
```
http://192.xxx.xxx.xx /wordpress
```
转至 WordPress 安装页，开始配置 WordPress。
![配置WP1](https://main.qcloudimg.com/raw/c79c35b3d75f763561d7024f46983611.png)
2. 根据 WordPress 安装向导提示输入以下安装信息，单击【安装 WordPress】，完成安装。
<table>
	<th style="width: 18%;">所需信息</th>
	<th style="width: 25%;">说明</th>
					<tr>
					<td>
							站点标题
					</td>
					<td>
							WordPress 网站名称。
					</td>
			</tr>
				<tr>
					<td>
							用户名
					</td>
					<td>
							WordPress 管理员名称。出于安全考虑，建议设置一个不同于 admin 的名称。因为与默认用户名称 admin 相比，该名称更难破解。
					</td>
			</tr>
			<tr>
					<td>
							密码
					</td>
					<td>
							可以使用默认强密码或者自定义密码。请勿重复使用现有密码，并确保将密码保存在安全的位置。
					</td>
			</tr>
				<tr>
					<td>
							您的电子邮件
					</td>
					<td>
							用于接收通知的电子邮件地址。
					</td>
			</tr>
	</table>
现在可以用登录 WordPress 博客，并开始发布博客文章了。

## 后续操作
1. 您可以给自己的 WordPress 博客网站设定一个单独的域名。您的用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。
您可以通过 [腾讯云购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)。 
2. 域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。备案免费，审核时间约为20天。
3. 您需要在腾讯云 [云解析](https://console.cloud.tencent.com/cns/domains)上配置域名解析之后，用户才能通过域名访问您的网站，指引参考 [域名解析](https://cloud.tencent.com/document/product/302/3446)。


此外，您还可以在腾讯云平台横向和纵向扩展服务容量，例如：
- 扩展单个 CVM 实例的 CPU 和内存规格，增强服务器的处理能力。[了解详情 >>](https://cloud.tencent.com/document/product/213/2178)
- 增加多台 CVM 实例，并利用 [负载均衡](https://cloud.tencent.com/document/product/214)，在多个实例中进行负载的均衡分配。
- 利用 [弹性伸缩](https://cloud.tencent.com/document/product/377)，根据业务量自动增加或减少 CVM 实例的数量。
- 利用 [对象存储](https://cloud.tencent.com/document/product/436)，存储静态网页和海量图片、视频等。
