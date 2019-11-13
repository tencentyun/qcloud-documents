## 操作场景
WordPress 是一款使用 PHP 语言开发的博客平台，您可使用通过 WordPress 搭建属于个人的博客平台。本文以 CentOS 7.6 操作系统的腾讯云云服务器为例，手动搭建 WordPress 个人站点。

## 技能要求
搭建 WordPress 个人博客，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。
>!腾讯云建议您可以通过云市场的镜像环境部署 WordPress 个人博客，手动搭建过程可能需要较长时间。具体步骤可参考 [镜像部署 WordPress 个人站点](https://cloud.tencent.com/document/product/213/9740)。

## 操作步骤 
### 步骤1：登录云服务器
登录 Linux 云服务器。如果您还未登录，请准备好您云服务器的登录密码及公网 IP，参考 [使用标准方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 完成登录。

### 步骤2：手动搭建 LNMP 环境
LNMP 是 Linux、Nginx、MariaDB 和 PHP 的缩写，这个组合是最常见的 Web 服务器的运行环境之一。在创建并登录云服务器实例之后，您可参考 [手动搭建 LNMP 环境](https://cloud.tencent.com/document/product/213/38056) 完成基本环境搭建。


### 步骤3：配置 WordPress 数据库<span id="database"></span>
>!根据 MariaDB 版本，设置用户身份验证方式有一定区别，具体步骤请参见 MariaDB 官网。
>
1. 执行以下命令，进入 MariaDB。
```
mysql
```
2. 执行以下命令，创建 MariaDB 数据库。例如 “wordpress”。
```
CREATE DATABASE wordpress;
```
3. 执行以下命令，创建一个新用户。例如 “user”，登录密码为 `123456`。
```
CREATE USER 'user'@'localhost' IDENTIFIED BY '123456';
```
4. 执行以下命令，赋予用户对 “wordpress” 数据库的全部权限。
```
GRANT ALL PRIVILEGES ON wordpress.* TO 'user'@'localhost' IDENTIFIED BY '123456';
```
5. 执行以下命令，使所有配置生效。
```
FLUSH PRIVILEGES;
```
6. 执行以下命令，退出 MariaDB。
```
\q
```

### 步骤4：配置 root 帐户
1. 执行以下命令，进入 MariaDB。
```
mysql
```
2. 执行以下命令，设置 root 帐户密码。
>?MariaDB 10.4 在 CentOS 系统上已增加了 root 帐户免密登录功能，请执行以下步骤设置您的 root 帐户密码并牢记。
>
```
ALTER USER root@localhost IDENTIFIED VIA mysql_native_password USING PASSWORD('输入您的密码');
```
3. 执行以下命令，退出 MariaDB。
```
\q
```


### 步骤5：安装和配置 WordPress
#### 下载 WordPress
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


####  修改 WordPress 配置文件
1. 依次执行以下命令，进入 WordPress 安装目录，将`wp-config-sample.php`文件复制到`wp-config.php`文件中，并将原先的示例配置文件保留作为备份。
```
cd /usr/share/nginx/html/wordpress
cp wp-config-sample.php wp-config.php
```
2. 执行以下命令，打开并编辑新创建的配置文件。
```
vim wp-config.php
```
3. 按 “**i**” 切换至编辑模式，找到文件中 MySQL 的部分，并将相关配置信息修改为 [配置 WordPress 数据库](#database) 中的内容。
```
	// ** MySQL settings - You can get this info from your web host ** //
	/** The name of the database for WordPress */
	define('DB_NAME', 'wordpress');
	
	/** MySQL database username */
	define('DB_USER', 'user');
	
	/** MySQL database password */
	define('DB_PASSWORD', '123456');
	
	/** MySQL hostname */
	define('DB_HOST', 'localhost');
```
4. 修改完成后，按“**Esc**”，输入“**:wq**”，保存文件返回。

### 步骤6：验证 WordPress 安装
1. 在浏览器地址栏输入云服务器实例的公网 IP 加上 wordpress 文件夹，例如：
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



## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。

