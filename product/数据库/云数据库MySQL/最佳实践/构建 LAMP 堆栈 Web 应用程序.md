LAMP 指 Linux+Apache+Mysql/MariaDB+Perl/PHP/Python，是一组常用来搭建动态网站或者服务器的开源软件。程序都是独立的，但是因为常被一起使用，相互间的兼容性越来越高，共同组成了一个强大的 Web 应用程序平台。
本教程将指导您完成以下过程：启动一个腾讯云数据库实例，通过腾讯云服务器配置一个 LAMP 应用程序，用以连接腾讯云数据库实例的高可用性环境。
运行腾讯云数据库实例会将数据库与环境的生命周期分离，这让您可以从多个服务器连接到同一个数据库，并且简化数据库的运维，让您无需再关心数据库的安装、部署、版本更新及故障处理等问题。

>?本教程中使用到的云数据库实例和云服务器实例处于同一地域下，如果您的云数据库实例和云服务器实例不处于同一地域下，请参见 [外网访问](https://cloud.tencent.com/document/product/236/3130)。

### 初始化云数据库实例
云数据库的购买和初始化请参见 [购买方式](https://cloud.tencent.com/document/product/236/5160) 和 [初始化 MySQL 数据库](https://cloud.tencent.com/document/product/236/3128)。

### 登录云服务器实例
云服务器的购买和访问请参见 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)，本教程中使用的是 CentOS 系统。

### 安装 MySQL 客户端
1. 在云服务器实例中使用`yum`安装 MySQL 客户端。
```
yum install mysql -y
```
![](//mc.qcloudimg.com/static/img/8b952d6d7d767413a6558e82df092d44/image.png)
2. 安装完成后，连接到腾讯云数据库实例。
```
mysql -h hostname -u username -p
```
![](//mc.qcloudimg.com/static/img/297856a53959582220b9bba6f06ce9f6/image.png)
其中，hostname 为数据库实例的内网 IP 地址，username 为您的数据库用户名。
3. 连接成功后，即可退出数据库，进行下一步操作。
```
quit;
```

### 安装 Apache 服务
1. 在云服务器实例中使用`yum`安装 Apache。
```
yum install httpd -y
```
![](//mc.qcloudimg.com/static/img/dc142f813e8e8474a5994e2e841828f2/image.png)
2. 启动 Apache 服务。
```
service httpd start
```
3. 测试 Apache。
>!此步骤需要您的云服务器在安全组中配置来源为 **all**，端口协议为 **TCP:80** 的入站规则。安全组配置请参见 [安全组](https://cloud.tencent.com/document/product/213/12452)。
>
在您本地的浏览器中输入`http://115.xxx.xxx.xxx/`（其中`115.xxx.xxx.xxx`为您的云服务器公网 IP 地址），出现下列画面表示 Apache 启动成功。
![](https://main.qcloudimg.com/raw/80941070a1a309ba484527473c915221.png)

### 安装 PHP 
1. 在云服务器实例中使用`yum`安装 PHP。
```
yum install php -y
```
![](//mc.qcloudimg.com/static/img/61a0864ddbb70e65c63ad5093e8165d4/image.png)

### 创建项目测试 LAMP 环境
1. 在云服务器`/var/www/html`目录下创建一个 info.php 文件，示例代码如下：
```
<?php phpinfo(); ?>
```
2. 重启 Apache 服务。
```
service httpd restart
```
3. 在您本地的浏览器中输入 `http://0.0.0.0/info.php` ，其中`0.0.0.0`为您的云服务器公网 IP 地址，出现下列画面表示 LAMP 服务部署成功。
![](//mc.qcloudimg.com/static/img/0bc6667d122fe85d505fbe50b507b60a/image.png)
