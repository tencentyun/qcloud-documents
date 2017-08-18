LAMP 指 Linux+Apache+Mysql/MariaDB+Perl/PHP/Python 是一组常用来搭建动态网站或者服务器的开源软件，本身都是各自独立的程序，但是因为常被放在一起使用，拥有了越来越高的兼容度，共同组成了一个强大的 Web 应用程序平台。
本教程将指导您完成以下过程：启动一个腾讯云数据库 CDB 实例并通过腾讯云服务器 CVM 配置一个 LAMP 应用程序以连接该数据库实例的高可用性环境。运行腾讯云数据库实例会将数据库与环境的生命周期分离。这让您可以从多个服务器连接到同一个数据库，并且简化数据库的运维，让您无需再关心数据库的安装、部署、版本更新及故障处理等问题。
>**注意：**
本教程中使用到的云数据库实例和云服务器实例处于同一地域下，如果您的云数据库实例和云服务器实例不处于同一地域下，请参考 [外网访问](https://www.qcloud.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE)。

### 初始化云数据库实例
云数据库的购买和初始化请参考 [购买与续费](https://www.qcloud.com/document/product/236/5160) 和 [初始化 MySQL 数据库](https://www.qcloud.com/document/product/236/3128)。
### 登录到云服务器实例
云服务器的购买和访问请参考 [快速入门 Linux 云服务器](https://www.qcloud.com/document/product/213/2936)，本教程中使用的是 centOS 7.2 系统。
### 安装 MySQL 客户端
1. 在云服务器实例中使用 `yum` 安装 MySQL 客户端：
```
yum install mysql -y
```
![](//mc.qcloudimg.com/static/img/8b952d6d7d767413a6558e82df092d44/image.png)
2. 安装完成后，连接到腾讯云数据库实例：
```
mysql -h hostname -u username -p
```
![](//mc.qcloudimg.com/static/img/297856a53959582220b9bba6f06ce9f6/image.png)
其中，hostname 为数据库实例的内网 IP 地址，username 为您的数据库用户名。
连接成功后，即可使用 `quit;` 退出数据库，进行下一步操作。
### 安装 Apache 服务
1. 在云服务器实例中使用 `yum` 安装 Apache：
```
yum install httpd -y
```
![](//mc.qcloudimg.com/static/img/dc142f813e8e8474a5994e2e841828f2/image.png)
2. 启动 Apache 服务：
```
service httpd start
```
3. 测试 Apache ：
>**注意：**
此步骤需要您的云主机在安全组中配置来源为 **all**，端口协议为 **TCP:80** 的入站规则。关于安全组的配置方法请参考 [安全组](https://www.qcloud.com/document/product/213/5221)。

在您本地的浏览器中输入您服务器的外网地址，出现下列画面表示 Apache 启动成功。
![](//mc.qcloudimg.com/static/img/3cde70e76a386b81f96ea9919280269d/image.png)

### 安装 PHP 
1. 在云服务器实例中使用 `yum` 安装 PHP：
```
yum install php -y
```
![](//mc.qcloudimg.com/static/img/61a0864ddbb70e65c63ad5093e8165d4/image.png)
2. 我们在云服务器 /var/www/html 目录下创建一个 info.php 文件来检查 PHP 是否安装成功，示例代码参考如下：
info.php
```
<?php phpinfo(); ?>
```
3. 重启 Apache 服务：
```
service httpd restart
```
4. 在您本地的浏览器中输入 `http:// 云服务器外网 IP /info.php` ，出现下列画面表示 LAMP 服务部署成功。
![](//mc.qcloudimg.com/static/img/0bc6667d122fe85d505fbe50b507b60a/image.png)
