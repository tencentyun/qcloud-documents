Drupal 是使用 PHP 语言编写的开源内容管理框架（CMF），它由内容管理系统（CMS）和 PHP  开发框架（Framework）共同构成。它用于构造提供多种功能和服务的动态网站，能支持从个人博客到大型社区等各种不同应用的网站项目。
本教程说明如何在腾讯云服务器 CVM 上搭建 Drupal 电子商务网站。使用的软件环境为：centos7.2 | Drupal7.56  | PHP5.4.16。
### 初始化云数据库实例
云数据库的购买和初始化请参考 [购买与续费](https://www.qcloud.com/document/product/236/5160) 和 [初始化 MySQL 数据库](https://www.qcloud.com/document/product/236/3128)。
### 安装 MySQL 服务
1. 在云服务器实例中使用 `yum` 安装 MySQL 服务。
```
yum install mysql mysql-server mysql-devel -y
```
2. 启动 MySQL 服务。
```
service mysqld start
```
3. 创建 Drupal 数据库。
```
mysqladmin -u root -p create drupal
```
其中，drupal 为 Drupal 服务使用的数据库名。
3. 创建 Drupal 的用户。
```
mysql -u root -p
```
```
mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON drupal.* TO 'username'@'localhost' IDENTIFIED BY 'password';
mysql> FLUSH PRIVILEGES;
mysql> exit
```
其中，username 为 Drupal 服务使用的数据库用户名，password 为 Drupal 服务使用的数据库密码。

### 安装 Apache 服务
1. 在云服务器实例中使用 `yum` 安装 Apache。
```
yum install httpd -y
```
2. 启动 Apache 服务。
```
service httpd start
```
3. 测试 Apache 。
>**注意：**
此步骤需要您的云主机在安全组中配置来源为 **all**，端口协议为 **TCP:80** 的入站规则。关于安全组的配置方法请参考 [安全组](https://www.qcloud.com/document/product/213/5221)。

在您本地的浏览器中输入您服务器的外网地址，出现下列画面表示 Apache 启动成功。
![](//mc.qcloudimg.com/static/img/3cde70e76a386b81f96ea9919280269d/image.png)

### 安装 PHP 
1. 在云服务器实例中使用 `yum` 安装 PHP 及其扩展。
```
yum install php php-dom php-dg php-mysql php-pdo -y
```
2. 我们在云服务器 /var/www/html 目录下创建一个 info.php 文件来检查 PHP 是否安装成功，示例代码参考如下。
info.php
```
<?php phpinfo(); ?>
```
3. 重启 Apache 服务。
```
service httpd restart
```
4. 在您本地的浏览器中输入 `http:// 云服务器外网 IP /info.php` ，出现下列画面表示 PHP 安装成功。
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
4. 修改sites目录属主属组。
```
chown -R apache:apache /var/www/html/sites
```
5. 重启 Apache 服务。
```
service httpd restart
```
6. 在您本地的浏览器中输入 `http:// 云服务器外网 IP ` ，进入到Drupal安装界面。选择安装版本，单击Save and continue。
![](//mc.qcloudimg.com/static/img/73f38550392e4fa6c496ed2afd0263a9/image.png)
7. 选择安装语言，单击 Save and continue。
![](//mc.qcloudimg.com/static/img/9ab7121915a685816504a80d347be29c/image.png)
8. 设置数据库，输入您之前配置的数据库信息。
![](//mc.qcloudimg.com/static/img/a4d53a2d9421be3d223862585cf1c61e/image.png)
9. 输入站点信息。
 ![](//mc.qcloudimg.com/static/img/c124ba56012c3a3bd8023a65cdb87b52/image.png)
10. 完成 Drupal 的安装。
![](//mc.qcloudimg.com/static/img/ed4795e8c6cb3183c56aeb8e18ef5d4a/image.png)
11. 后续可以访问云服务器的外网 IP 网站进行个性化设置。
12. ![](//mc.qcloudimg.com/static/img/1c27ddd5419452fb92b8348d03586101/image.png)
