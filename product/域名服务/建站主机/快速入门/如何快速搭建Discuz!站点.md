下文介绍如何基于建站主机快速搭建 Discuz! 站点。

### 1. 获取FTP信息
进入主机的管理页面，获取 FTP 地址、用户名和密码
![](https://mc.qcloudimg.com/static/img/44989bcf85458672bb503e76d334e92d/ftp.png)

### 2. 下载 Discuz! 安装包
前往 [Discuz!官网](http://www.comsenz.com/downloads/install/discuzx) 下载最新版本的 Discuz! 安装包。

### 3. 上传安装包
通过 FTP 工具上传网站程序，具体可以参考 [FTP 工具使用说明](https://cloud.tencent.com/document/product/615/11181)。

### 4. 获取数据信息
进入主机的管理页面，获取数据库信息。
![](https://mc.qcloudimg.com/static/img/c7fa30c75349f24270cf1493943373b1/image.png)

### 5. 执行安装
浏览器访问`http://您的域名/discuz/install `，点击【我同意】，进入安装步骤。
![](https://mc.qcloudimg.com/static/img/f9137bfcba9227930828430754f8b274/1.png)

确认当前环境，选择【全新安装】，点击【下一步】。
![](https://mc.qcloudimg.com/static/img/eada7ee01817fd5139ca9a4b7bb534ef/2.png)

填写数据库信息和网站管理员信息，点击【下一步】。

数据库名：可填写为 discuz
数据库用户名：（从管理页面获取）
数据库密码：（从管理页面获取）
数据库前缀：可填写为 dz_
系统信箱 Email：填写网站开发者的邮箱

管理员帐号：可填写为admin
管理员密码：（填写管理员登录网站后台的密码，需要牢记）
管理员Email：填写管理员/站长的邮箱

![](https://mc.qcloudimg.com/static/img/7d51cc0c69319aef4a08d18ecdd9a5a3/3.png)

完成安装。
![](https://mc.qcloudimg.com/static/img/ced1f86f7b53a95232d33cb2b40cf5e4/4.png)

### 6. 访问网站首页
通过临时域名`http://xxxxxx.mylitesite.com/discuz/forum.php`或者已绑定域名 `http://youdoamin.com/discuz/forum.php` 访问站点。
![](https://mc.qcloudimg.com/static/img/efae2237651909501cd9a332753ab36f/5.png)
