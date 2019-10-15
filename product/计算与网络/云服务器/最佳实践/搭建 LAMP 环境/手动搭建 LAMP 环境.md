## 操作场景
本文档以 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 LAMP 环境。文档包含软件安装内容，请确保您已熟悉软件安装方法，详情请参见 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046)。
LAMP 环境代表 Linux 系统下由 Apache  + MySql + PHP 及其它相关辅助组件组成的网站服务器架构。

LAMP 组成及使用版本说明：
- Linux 系统，本文使用 CentOS 7.6。
- Apache：Web 服务器软件，本文使用 2.4.41 版本。
- MySQL：数据库管理系统，本文使用
- PHP：脚本语言，本文使用 PHP 7.0.32
- phpMyAdmin：通过 Web 管理数据库的软件，本文使用


## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建并登录云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看并获取云服务器的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/9563d4c3cd313c588a532be7fdd9fc29.png)
- 云服务器用户名和密码。
- 云服务器公网 IP。
3. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。

### 安装配置 Apache
1. 依次执行以下命令，安装依赖包。
```
yum groupinstall "Development Tools" -y
yum install libtool -y
yum install expat-devel pcre pcre-devel openssl-devel -y
```
2. 依次运行以下命令，下载 Apache、Apr、Apr-util 的源码包。
>?腾讯云软件源每天同步一次各官网软件源，请从 [Apache 软件源](http://mirrors.tencent.com/apache) 获取最新下载地址。 
>
```
wget http://mirrors.tencent.com/apache/httpd/httpd-2.4.41.tar.gz
wget http://mirrors.tencent.com/apache/apr/apr-1.7.0.tar.gz
wget http://mirrors.tencent.com/apache/apr/apr-util-1.6.1.tar.gz
```
3. 依次执行以下命令，将源码包解压到指定目录。
```
tar xvf httpd-2.4.41.tar.gz -C /usr/local/src
tar xvf apr-1.7.0.tar.gz -C /usr/local/src
tar xvf apr-util-1.6.1.tar.gz -C /usr/local/src
```
4. 依次执行以下命令，将 Apr 及 Apr-util 文件移动至 Apache 下的 srclib 文件夹中。
```
cd /usr/local/src
mv apr-1.7.0 httpd-2.4.41/srclib/apr
mv apr-util-1.6.1 httpd-2.4.41/srclib/apr-util
```
5. 依次执行以下命令，编译源码并安装。
```
cd /usr/local/src/httpd-2.4.41
```
```
./buildconf
```
```
./configure --prefix=/usr/local/apache2 \
--enable-ssl \
--enable-so \
--with-mpm=event \
--with-included-apr \
--enable-cgi \
--enable-rewrite \
--enable-mods-shared=most \
--enable-mpms-shared=all
```
```
make && make install
```
6. 运行以下命令，设置 Apache 的环境变量。
```
echo "export PATH=$PATH:/usr/local/apache2/bin" > /etc/profile.d/httpd.sh
```
7. 运行以下命令，读取环境变量。
```
source /etc/profile.d/httpd.sh
```
8. 运行以下命令，查看 Apache 版本号。
```
httpd -v
```
返回结果如下，则说明环境变量配置成功。
![](https://main.qcloudimg.com/raw/a1bc1d985c625510411fbd13b0b56512.png)
9. 执行以下命令，创建 Apache 启动配置文件。
```
vi /usr/lib/systemd/system/httpd.service
```
10. 按 “**i**” 或 “**Insert**” 切换至编辑模式，将以下内容输入到文件中。
```
[Unit] 
Description=The Apache HTTP Server 
After=network.target 
[Service] 
Type=forking 
ExecStart=/usr/local/apache2/bin/apachectl -k start 
ExecReload=/usr/local/apache2/bin/apachectl -k graceful 
ExecStop=/usr/local/apache2/bin/apachectl -k graceful-stop 
PIDFile=/usr/local/apache2/logs/httpd.pid 
PrivateTmp=false
[Install] 
WantedBy=multi-user.target
```
11. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
12. 依次运行以下命令，启动 Apache 并设置为开机自启动。
```
systemctl start httpd
systemctl enable httpd
```
13. 在浏览器中访问云服务器实例公网 IP，查看安装结果。
显示如下，则说明 Apache 成功安装。
![](https://main.qcloudimg.com/raw/1386035d4b1d7b2f72608a35dc92dc01.png)

### 安装配置 MySQL
1. 依次执行以下命令，安装依赖包。
```
yum install ncurses-devel bison gnutls-devel -y
yum install cmake -y
```
2. 依次执行以下命令，创建 MySQL 文件目录。
```
cd
mkdir /mnt/data
```
3. 依次执行以下命令，创建组、系统用户，并查看用户 ID 及 组 ID。
```
groupadd -r mysql
useradd -r -g mysql -s /sbin/nologin mysql
id mysql
```
4. 执行以下命令，设置目录的用户权限。
```
chown -R mysql:mysql /mnt/data
```
5. 依次运行以下命令，下载 MySQL 安装包及解压到指定目录。
```
wget https://downloads.mysql.com/archives/get/file/mysql-5.6.24.tar.gz
tar xvf mysql-5.6.24.tar.gz -C  /usr/local/src
```
6. 依次执行以下命令，进行编译安装。
```
cd /usr/local/src/mysql-5.6.24
```
```
cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DMYSQL_DATADIR=/mnt/data \
-DSYSCONFDIR=/etc \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITH_READLINE=1 \
-DWITH_SSL=system \
-DWITH_ZLIB=system \
-DWITH_LIBWRAP=0 \
-DMYSQL_TCP_PORT=3306 \
-DDEFAULT_CHARSET=utf8 \
-DMYSQL_UNIX_ADDR=/usr/local/mysql/mysql.sock \
-DDEFAULT_COLLATION=utf8_general_ci \
-DWITH_SYSTEMD=1 \
-DINSTALL_SYSTEMD_UNITDIR=/usr/lib/systemd/system 
```
```
make && make install
```
7. 执行以下命令，设置安装目录的用户权限。
```
chown -R mysql:mysql /usr/local/mysql/
```
8. 依次执行以下命令，初始化数据库并备份配置文件。
```
cd /usr/local/mysql
/usr/local/mysql/scripts/mysql_install_db --user=mysql --datadir=/mnt/data/
mv /etc/my.cnf /etc/my.cnf.bak
cp /usr/local/mysql/support-files/my-default.cnf /etc/my.cnf
```
9. 执行以下命令，修改配置文件。
```
echo -e "basedir = /usr/local/mysql\ndatadir = /mnt/data\n" >> /etc/my.cnf
```
10. 执行以下命令，创建 MySQL 的启动配置文件。
```
vi /usr/lib/systemd/system/mysql.service
```
11. 按 “**i**” 或 “**Insert**” 切换至编辑模式，添加以下内容。
```
[Unit]
Description=MySQL Community Server
After=network.target
After=syslog.target
[Install]
WantedBy=multi-user.target
Alias=mysql.service
[Service]
User=mysql
Group=mysql
PermissionsStartOnly=true
ExecStart=/usr/local/mysql/bin/mysqld
TimeoutSec=600
Restart=always
PrivateTmp=false
```
12. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
13. 执行以下命令，设置 MySQL 的环境变量。
```
echo "export PATH=$PATH:/usr/local/mysql/bin" > /etc/profile.d/mysql.sh
```
14. 执行以下命令，读取环境变量。
```
source /etc/profile.d/mysql.sh
```
15. 依次执行以下命令，启动 MySQL 并设置为开机自启动。
```
systemctl start mysql
systemctl enable mysql
```
16. 执行以下命令，设置 MySQL 的 root 账户密码。
```
mysqladmin -u root password
```
17. 执行以下命令，登录 MySQL 数据库。
```
mysql -uroot -p
```
显示结果如下，则说明成功安装 MySQL。
![](https://main.qcloudimg.com/raw/9738ba9487eb8e2ebaf52c2a7a741871.png)
18. 执行以下命令，脱出 MySQL。
```
\q
```

### 安装配置 PHP
1. 执行以下命令，安装依赖包。
```
yum install -y libmcrypt libmcrypt-devel mhash mhash-devel libxml2 libxml2-devel bzip2 bzip2-devel 
```
2. 依次运行以下命令，进入对应目录，下载 PHP 7.3.10 源码包。
```
cd
wget https://www.php.net/distributions/php-7.3.10.tar.bz2
```
3. 依次执行以下命令，解压 PHP 源码包到指定目录。
```
tar xvf php-7.3.10.tar.bz2 -C /usr/local/src
cd /usr/local/src/php-7.3.10
```
4. 依次执行以下命令，编译安装 PHP。
```
./configure --prefix=/usr/local/php \
--with-config-file-scan-dir=/etc/php.d \
--with-apxs2=/usr/local/apache2/bin/apxs \
--with-config-file-path=/etc \
--with-pdo-mysql=mysqlnd \
--with-mysqli=/usr/local/mysql/bin/mysql_config \
--enable-mbstring \
--with-freetype-dir \
--with-jpeg-dir \
--with-png-dir \
--with-zlib \
--with-libxml-dir=/usr \
--with-openssl \
--enable-xml \
--enable-sockets \
--enable-fpm \
--with-bz2 \
--disable-fileinfo
```
```
make && make install
```
5. 执行以下命令，复制 PHP 配置文件。
```
cp php.ini-production /etc/php.ini
```
6. 执行以下命令，修改 Apache 配置文件。
```
vi /usr/local/apache2/conf/httpd.conf
```
按 “**i**” 或 “**Insert**” 切换至编辑模式：
 - 在 `ServerName www.example.com:80` 下另起一行，增加以下内容：
```
ServerName localhost:80
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/b0ea5d5cea2883a89890482b98b9e81d.png)
 - 将 `<Directory>` 中的 `Require all denied` 修改为以下内容：
```
Require all granted
```
 修改完成后如下图所示：
 ![](https://main.qcloudimg.com/raw/5c4e2019b90e038d169ede1e1606dcba.png)
 - 将 `<IfModule dir_module>` 中内容替换为以下配置：
```
DirectoryIndex index.php index.html
```
 修改完成后如下图所示：
 ![](https://main.qcloudimg.com/raw/ae7ff73d2af51b3989474cb51971ddf0.png)
 - 在 `AddType application/x-gzip .gz .tgz` 后另起一行，输入以下内容：
```
AddType application/x-httpd-php .php
AddType application/x-httpd-php-source .phps
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/57ff0ddb44c0bcbf20148b5df8bc0e38.png)
7. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
8. 执行以下命令，重启 Apache 服务。
```
systemctl restart httpd
```

### 环境配置验证
1. 执行以下命令，创建测试文件。
```
echo "<? php phpinfo(); ?>" >> /usr/local/apache2/htdocs/index.php
```
在浏览中访问以下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/index.php
```
显示结果如下，则说明 LAMP 环境配置成功。
![](https://main.qcloudimg.com/raw/fa49126902d4f87f0e5a945f1c11fbd3.png)

