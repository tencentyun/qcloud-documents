下文介绍如何基于建站主机快速搭建 Discuz! 站点。

### 1. 获取 FTP 信息
点击主机 ID 进入主机管理页面，可获取 FTP 和 MySQL 地址、用户名，用户可在此处重置密码。
![](https://main.qcloudimg.com/raw/78d6e646e8e503f824c5d7e83d8e384c.png)

### 2. 下载 Discuz! 安装包
前往 [Discuz!官网](http://www.comsenz.com/downloads/install/discuzx) 下载最新版本的 Discuz! 安装包。

### 3. 上传安装包
通过 FTP 工具上传网站程序，具体可以参考 [FTP 工具使用说明](https://cloud.tencent.com/document/product/615/11181)。
只需要把upload目录下所有的文件和目录上传到wwwroot目录下，安装包其他的文件和目录不需要上传。
![](https://ask.qcloudimg.com/draft/1173778/2vl1cnc78k.png)
> 注意：使用 FTP 工具上传文件，建站主机不提供解压功能。



### 4. 获取数据信息
进入主机的管理页面，获取数据库信息。
![](https://mc.qcloudimg.com/static/img/c7fa30c75349f24270cf1493943373b1/image.png)

### 5. 执行安装
浏览器访问`http://您的域名/install `，单击【我同意】，进入安装步骤。
![](https://ask.qcloudimg.com/draft/1070625/h989h6uhsx.png)

确认当前环境，选择【全新安装】，单击【下一步】。
![](https://ask.qcloudimg.com/draft/1070625/i6mqjkknjj.png)

填写数据库信息和网站管理员信息，单击【下一步】。

数据库名：需填写为 webuser
数据库用户名：（从管理页面获取）
数据库密码：（从管理页面获取）
数据库前缀：可填写为 dz_
系统信箱 Email：填写网站开发者的邮箱

管理员帐号：可填写为 admin
管理员密码：（填写管理员登录网站后台的密码，需要牢记）
管理员 Email：填写管理员/站长的邮箱

![](https://ask.qcloudimg.com/draft/1070625/xcgt0r9jwl.png)

完成安装。
![](https://ask.qcloudimg.com/draft/1070625/dn2ehcikb9.png)

### 6. 访问网站首页
通过临时域名`http://xxxxxx.mylitesite.com/forum.php`或者已绑定域名 `http://youdoamin.com/forum.php` 访问站点。
![](https://ask.qcloudimg.com/draft/1070625/wftihv7vih.png)
