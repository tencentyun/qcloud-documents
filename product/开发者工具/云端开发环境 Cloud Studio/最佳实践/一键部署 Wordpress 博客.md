## 操作场景
一键部署可以帮助您快速部署动态（PHP，支持 MySQL）或静态网站，可用于部署 Wordpress、CMS、Vuepress、Hexo 等应用。本文指导您在云端开发环境 Cloud Studio 控制台中，通过一键部署快速搭建一个 Wordpress 站点。
静态网站部署请参考 [一键部署静态网站](https://cloud.tencent.com/document/product/1039/34041)。

## 限制条件
- 一键部署的磁盘空间和数据库空间限制都是128MB，部署文件的限制是100MB，超出会导致部署出错。
- 一键部署禁止访问外网，在后台无法安装插件、主题，如需安装请使用上传的方式进行。
- 由于安全原因，一键部署禁了以下函数，请避免使用：
 - exec
 - passthru
 - shell_exec
 - system
 - proc_open
 - popen
 - show_source
 - curl_exec
 - curl_multi_exec
 - stream_socket_client
 - putenv
 - dl
 - fsockopen
 - pfsockopen


## 操作步骤
### 创建工作空间
1. 登录云端开发环境 Cloud Studio 控制台。
2. 在 [工作空间创建](https://console.cloud.tencent.com/cloudstudio/workspace/create) 页面，选择代码来源为【模板】>【WrodPress 模板】。
3. 根据页面提示，创建一个工作空间。
4. 创建成功后，进入工作空间，可以看到 WordPress 的代码已经被 clone 下来。
![](https://main.qcloudimg.com/raw/42c574fdb9f02f1c1588139c570cfe03.jpg)

### 一键部署站点
1. 在页面右侧的功能区，选择【一键部署】。
2. 在【一键部署】面板中，单击【一键开启】即可打开一键部署功能。
3. 一键部署入口文件。
入口指 Web 请求可访问的目，默认情况下是根目录，若您的应用不是根目录，例如`public`，则需要在此填写`/public`。应用入口应该以`/`开头，且处于根目录下面。
![](https://main.qcloudimg.com/raw/2aa05e4c1147b4415122a989b5e315a1.jpg)
本例中代码都在根目录，可直接单击【一键部署】后稍等几秒，页面会显示部署成功的信息，此时我们可以通过测试域名直接访问应用。
![](https://main.qcloudimg.com/raw/270d28c6c3871febef5b3c6d527cd4c0.jpg)
4. 部署成功后会进入 Wordpress 安装页面，安装后需要填写一键部署面板中【资源管理】里面提供的数据库名、用户名、密码等信息，提交后就可以进入 Wordpress 首页了。
![](https://main.qcloudimg.com/raw/a0781bdda73e4693012995b55ed44e6a.jpg)


### 管理数据库
应用创建成功之后，您可以通过我们提供的数据库管理链接进行数据库管理。
1. 切换到【资源管理】，可以看到当前的资源信息和数据库管理链接。
![](https://main.qcloudimg.com/raw/5130bdda254a94027a26dd9843cb916f.jpg)
2. 单击链接，进入数据库管理页面（首次登录需要输入用户名和密码），即可管理自己的数据。
![](https://main.qcloudimg.com/raw/8133f244300e6e82fea3fbf578a3626e.jpg)

### 绑定域名
您可以给部署的网站绑定自己的域名， 单击 Tab 菜单最后一项【域名绑定】，添加自己的域名。
#### 添加域名解析
1. 进入自己的域名服务商网站，给域名添加一条 CNAME 解析记录到测试域名。
![](https://main.qcloudimg.com/raw/bedfca52d393492f6d89883f72134791.jpg)
2. 返回工作空间，添加刚才解析的域名。
添加成功后，可以看到下方多了一条绑定的域名。如果绑定失败会显示错误信息，此时您需要根据错误信息来重新绑定。
![](https://main.qcloudimg.com/raw/49093db8c80a27da1b6c0723835db7ef.jpg)
3. 此时，您可以通过自定义域名访问您的应用了。
如果您遇到了以下错误提示，说明您之前已经绑定过该域名导致其被占用，需要前往域名服务商后台添加一条 TXT 解析记录来验证所有权。
![](https://main.qcloudimg.com/raw/60d585f1b19f62bfc8248d25d13212d6.jpg)


#### 设置首选域名
当您设置了多个域名时，可以选择一个首选域名。设置首选域名后，可以设置让用户访问其它域名时自动跳转到首选域名。
![](https://main.qcloudimg.com/raw/9ce00f035f6f01180e0610b50ea63f86.jpg)

#### 强制 HTTPS 访问
一键部署会自动申请证书，强制 HTTPS 访问，这有助于提高您的网站安全性。请**不要随意更改 DNS 配置**，否则将有可能导致证书续期失败。

