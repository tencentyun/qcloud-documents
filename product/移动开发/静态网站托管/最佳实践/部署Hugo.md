## 概述
Hugo 是一款用 Go 编写的静态站点生成器，具有丰富的主题资源。
云开发（CloudBase）是一款云端一体化的产品方案，采用 serverless 架构，免环境搭建等运维事务，支持一云多端，助力快速构建小程序、Web应用、移动应用。
云开发静态网站托管支持通过云开发SDK调用服务端资源如：云函数、云存储、云数据库等，从而将静态网站扩展为全栈网站
无论是腾讯云·云开发用户，还是小程序·云开发用户，只要开通按量付费，即可享有云开发静态网站托管服务。


## 操作步骤 

### 步骤1：安装 Hugo

1. 我们需要先安装 Hugo：
```plaintext
brew install hugo
```
 >? Windows 的用户可以去 Hugo 的 githubc 仓库上下载安装 hugo 的可执行程序进行安装，具体安装流程请参阅 [Hugo官方操作文档](https://www.gohugo.org/doc/tutorials/installing-on-windows/)。
2. 用 Hugo 创建一个 blog 项目：
```plaintext
hugo new site hugo-demo && cd hugo-demo
```
3. 为 Hugo 添加一个主题。
 1. 执行以下命令，将主题添加进项目中：
```plaintext
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
```
	 >?对于无法使用 git 的用户，可以使用如下方法来添加主题。
	 1. 下载最新版的主题压缩包，[点击下载](https://github.com/budparr/gohugo-theme-ananke/archive/master.zip)
	 2. 解压`.zip`安装包，得到 “gohugo-theme-ananke-master” 文件夹
	 3. 重命名文件夹为 “ananke”，并将其移动到`hugo-demo`项目中的 “themes/” 文件夹。
 2. 执行以下命令，添加主题至配置文件中：
```plaintext
echo 'theme = "ananke"' >> config.toml
```
4. 执行以下命令，创建一篇用于测试的文章：
```plaintext
hugo new posts/my-first-post.md
```
5. 执行以下命令，在目录中运行：
```plaintext
hugo server
```
6. 在浏览器输入 `http://localhost:1313` 即可查看效果：
![](https://main.qcloudimg.com/raw/629324c3cb698a93e2fe733b4c3cbe44.png)
7. 自定义主题（可选）
截止上一步骤，我们建立的博客已经可以访问，如果您需要按照自己的需求继续美化博客，可以按照下列步骤进行：
	1. 打开配置文件 `config.toml`，文件示例如下：
	```
	baseURL = "http://example.org/"
	languageCode = "en-us"
	title = "My New Hugo Site"
	theme = "ananke"
	```
	2. 修改 “title” 的值为网站名称。
	3. 设置域名 “baseURL” 为默认或者自定义域名。
	>?此处默认/自定义域名可以使用云开发提供的域名，请完成后续的 [步骤2：静态托管部署](#step2)。
	4. 如需了解主题 “ananke”，请参见 [gohugo-theme-ananke](https://github.com/budparr/gohugo-theme-ananke)。如需配置更多主题，请参见 [自定义主题](https://gohugo.io/themes/customizing/)。
8. 使用下面的代码部署编译完成的静态页面文件：
```plaintext
hugo -D
```
 生成好的静态页面文件会放在项目的 public 目录中，目录结构如下：
```plaintext
├── 404.html
├── categories
│   ├── index.html
│   └── index.xml
├── dist
│   ├── css
│   │   └── app.1cb140d8ba31d5b2f1114537dd04802a.css
│   └── js
│       └── app.3fc0f988d21662902933.js
├── images
│   └── gohugo-default-sample-hero-image.jpg
├── index.html
├── index.xml
├── posts
│   ├── index.html
│   ├── index.xml
│   ├── my-first-post
│   │   └── index.html
│   └── page
│       └── 1
│           └── index.html
├── sitemap.xml
└── tags
    ├── index.html
└── index.xml
```

### 步骤2：静态托管部署[步骤2](id:step2)

1. 登录 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击【新建环境】，填写环境名称并选择按量计费，开通环境。
![](https://main.qcloudimg.com/raw/225f9ed84be7739cfe27327fcab8c424.png)
 在开通环境以后，请记住您的环境 ID，这个 ID 后续部署需要用到。
2. 云开发环境创建完成后，单击左侧菜单栏中的【静态网站托管】，单击【选择已有按量计费环境】
![](https://main.qcloudimg.com/raw/0066b2dd6c36857cd0f52d3916c3c8d1.png)
当您看到如下界面时，说明已经开通成功。
![](https://main.qcloudimg.com/raw/64f31f5655bfcce0506262c3f7f9163c.png)
3. 执行以下命令，安装 cloudbase cli：
```plaintext
npm install -g @cloudbase/cli
```
4. 执行以下登录命令：
```plaintext
tcb login
```
 ![](https://main.qcloudimg.com/raw/eb4492e95cac7a0c9c8eeaa7dcf08c62.png)
5. 在弹出的页面中单击【确认授权】进行授权：
![](https://main.qcloudimg.com/raw/d24d089ce30054b1978122082bb26ca0.png)
6. 在 hugo-site 中将 public 目录中的文件给部署上去：
```plaintext
cloudbase hosting:deploy ./public  -e EnvID
```
 此处的 EnvID 替换为上述创建好的环境 ID。
![](https://main.qcloudimg.com/raw/ad682ccff5b02b232062d89dea40fb7c.png)
7. 登录 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击左侧菜单栏中的【静态网站托管】>【设置】，进入设置页面，可以找到默认的域名，单击域名，就可以看到您刚部署的 Hugo。
![](https://main.qcloudimg.com/raw/439da24bfa3827fb41b8305c2ac1a5ae.png)
