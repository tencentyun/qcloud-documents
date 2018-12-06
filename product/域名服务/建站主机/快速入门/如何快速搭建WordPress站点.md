完成网站代码后，需要上传至建站主机发布。

### 1.	获取 FTP 信息
点击主机 ID 进入主机管理页面，可获取 FTP 和 MySQL 地址、用户名，用户可在此处重置密码。
![](https://main.qcloudimg.com/raw/78d6e646e8e503f824c5d7e83d8e384c.png)

### 2. 下载 WordPress 安装包
前往 [WordPress 中文官网](https://cn.wordpress.org/) 下载最新版本的 WordPress 安装包。

### 3.	上传安装包
通过 FTP 工具上传网站程序，具体可以参考 [FTP 工具使用说明](https://cloud.tencent.com/document/product/615/11181)。
> 注意：使用 FTP 工具上传文件，建站主机不提供解压功能。  

### 4. 获取数据信息
进入主机的管理页面，获取数据库信息。
![](https://mc.qcloudimg.com/static/img/c7fa30c75349f24270cf1493943373b1/image.png)

### 5. 执行安装
浏览器访问`http://您的域名/wordpress/wp-admin/setup-config.php`，单击【现在就开始！】，进入安装步骤，
![](https://mc.qcloudimg.com/static/img/82428f6e9f68ed89373eb8e2f364b66c/1.png)

填写数据库信息。

数据库名：需填写为 webuser
数据库用户名：（从管理页面获取）
数据库密码：（从管理页面获取）
数据库主机：localhost
表前缀：可填写为 wp_

![](https://mc.qcloudimg.com/static/img/2ff2cdf395e25449aede1bce9d75ba85/2.png)

完成数据连接，可单击运行安装。
![](https://mc.qcloudimg.com/static/img/4a2d132befb79ad15ee4bc2fb5f4dca1/3.png)

填写网站信息，单击【安装WordPress】。

站点标题：可填写‘我的博客’
管理员帐号（用户名）：可填写为 admin
管理员密码：（填写管理员登录网站后台的密码，需要牢记）
管理员 Email：填写管理员/站长的邮箱
![](https://mc.qcloudimg.com/static/img/47f73a3cacb5ba14d901ae9fd1c1bdb7/4.png)

完成安装，可以登录网站后台。
![](https://mc.qcloudimg.com/static/img/d0dc0d2b5d8fd5f1027b0e28374050f5/5.png)

### 6. 访问网站
通过临时域名`http://xxxxxx.mylitesite.com/wordpress` 或者已绑定域名 `http://您的域名/wordpress` 访问站点。
