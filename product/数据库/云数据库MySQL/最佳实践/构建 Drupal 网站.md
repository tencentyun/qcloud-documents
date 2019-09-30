Drupal 是使用 PHP 语言编写的开源内容管理框架（Content Management Framework），它由内容管理系统（Content Management System）和 PHP  开发框架（Framework）共同构成。Drupal 可用于构造提供多种功能和服务的动态网站，能支持从个人博客到大型社区等各种不同应用的网站项目。
您可以通过本教程了解如何在腾讯云服务器上搭建 Drupal 电子商务网站。
使用的软件环境为：CentOS7.2、Drupal7.56、PHP5.4.16。

### 登录到云服务器实例
云服务器的购买和访问请参见 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

### 安装 MariaDB 服务
1. CentOS7 以上版本默认支持 MariaDB 数据库，因此我们将使用 MariaDB 数据库。在云服务器实例中使用`yum`安装 MariaDB 服务。
```
yum install mariadb-server mariadb -y
```
2. 启动 MariaDB 服务。
```
systemctl start mariadb
```
3. 为 Drupal 创建数据库。（本项目中使用 drupal 作为数据库名）
```
mysqladmin -u root -p create drupal
```
其中，drupal 为 Drupal 服务使用的数据库名。
3. 为数据库创建用户。
```
mysql -u root -p
```
为用户授权，授权成功后退出数据库。
```
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON drupal.* TO 'username'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
exit
```
其中，username 为 Drupal 服务使用的数据库用户名，password 为 Drupal 服务使用的数据库密码。

### 安装 Apache 服务
1. 在云服务器实例中使用`yum`安装 Apache。
```
yum install httpd -y
```
2. 启动 Apache 服务。
```
service httpd start
```
3. 测试 Apache。
>!此步骤需要您的云服务器在安全组中配置来源为 **all**，端口协议为 **TCP:80** 的入站规则。安全组配置请参见 [安全组](https://cloud.tencent.com/document/product/213/12452)。
>
在您本地的浏览器中输入`http://115.xxx.xxx.xxx/`（其中 `115.xxx.xxx.xxx`为您的云服务器公网 IP 地址），出现下列画面表示 Apache 启动成功。
![](https://main.qcloudimg.com/raw/c9b20e150bd5330feef6d978b8308629.png)

### 安装 PHP 
1. 在云服务器实例中使用`yum`安装 PHP 及其扩展。
```
yum install php php-dom php-dg php-mysql php-pdo -y
```
2. 在云服务器`/var/www/html`目录下创建一个 info.php 文件来检查 PHP 是否安装成功，示例代码如下：
```
<?php phpinfo(); ?>
```
3. 重启 Apache 服务。
```
service httpd restart
```
4. 在您本地的浏览器中输入 `http://115.xxx.xxx.xxx/info.php`（其中 `115.xxx.xxx.xxx`为您的云服务器公网 IP 地址） ，出现下列画面表示 PHP 安装成功。
![](//mc.qcloudimg.com/static/img/0bc6667d122fe85d505fbe50b507b60a/image.png)

### 安装 Drupal 服务
1. 下载 Drupal 安装包。
```
wget http://ftp.drupal.org/files/projects/drupal-7.56.zip
```
2. 解压到网站根目录。
```
unzip drupal-7.56.zip 
mv drupal-7.56/* /var/www/html/
```
3. 下载中文翻译包。
```
cd /var/www/html/
wget -P profiles/standard/translations http://ftp.drupal.org/files/translations/7.x/drupal/drupal-7.56.zh-hans.po
```
4. 修改`sites`目录属主属组。
```
chown -R apache:apache /var/www/html/sites
```
5. 重启 Apache 服务。
```
service httpd restart
```
6. 在您本地的浏览器中输入`http://115.xxx.xxx.xxx/`（其中 `115.xxx.xxx.xxx`为您的云服务器公网 IP 地址），进入 Drupal 安装界面。选择安装版本，单击【Save and continue】。
![](https://main.qcloudimg.com/raw/f52af1bb9822ddefc1989df9a0a95e8c.png)
7. 选择安装语言，单击【Save and continue】。
![](https://main.qcloudimg.com/raw/11a8f788ebd0595e6afdff936656c2cc.png)
8. 设置数据库，输入您在**安装 mariadb 服务**中配置的数据库信息。
![](https://main.qcloudimg.com/raw/3bcd676f2d0bb91a23b80589d89ea576.png)
9. 输入站点信息。
 ![](//mc.qcloudimg.com/static/img/c124ba56012c3a3bd8023a65cdb87b52/image.png)
10. 完成 Drupal 的安装。
![](//mc.qcloudimg.com/static/img/ed4795e8c6cb3183c56aeb8e18ef5d4a/image.png)
11. 后续可以访问 `http://115.xxx.xxx.xxx/`（其中 `115.xxx.xxx.xxx`为您的云服务器公网 IP 地址）对网站进行个性化设置。
![](https://main.qcloudimg.com/raw/6e73b18ffe3be7936e220d005b252719.png)
