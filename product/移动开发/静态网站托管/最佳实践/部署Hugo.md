## 概述
Hugo 是一款用 Go 编写的静态站点生成器，具有丰富的主题资源。
云开发（CloudBase）是一款云端一体化的产品方案，采用 serverless 架构，免环境搭建等运维事务，支持一云多端，助力快速构建小程序、Web应用、移动应用。
云开发静态网站托管支持通过云开发SDK调用服务端资源如：云函数、云存储、云数据库等，从而将静态网站扩展为全栈网站
无论是腾讯云·云开发用户，还是小程序·云开发用户，只要开通按量付费，即可享有云开发静态网站托管服务。


## 操作步骤 
### 步骤1：安装 Hugo
1. 我们需要先安装 Hugo：
```
brew install hugo
```
>? Windows 的用户可以去 Hugo 的 githubc 仓库上下载安装 hugo 的可执行程序进行安装，具体安装流程请参阅 [Hugo官方操作文档](https://www.gohugo.org/doc/tutorials/installing-on-windows/)。

2. 用 Hugo 创建一个 blog 项目：
```
hugo new site hugo-demo && cd hugo-demo
```

3. 创建一个测试的文章：
```
hugo new posts/my-first-post.md
```
4. 在目录中运行：
```
hugo server
```
5. 在浏览器打开 [http://localhost:1313/](http://localhost:1313/) 即可查看效果：
![](https://main.qcloudimg.com/raw/cacf94928922dc655ae5374cf6eb58c6.png)

6. 使用下面的代码部署编译完成的静态页面文件：
```
hugo -D
```
生成好的静态页面文件会放在项目的 public 目录中，目录结构如下：
```
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

7. 如果您不喜欢 Hugo 站点的默认主题样式的话，可以自行在 github 上找到开源的 Hugo 主题，并放置到您的 Hugo 项目中，例如：
```
git clone https://github.com/olOwOlo/hugo-theme-even themes/even
```

### 步骤2：静态托管部署
1. 打开腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击【新建环境】，选择空模板，单击下一步，填写环境名称并开通"按量计费"环境。
![](https://main.qcloudimg.com/raw/7b66272b50c4ffce1a8912e687000e30.png)
 在开通环境以后，进入[环境概览](https://console.cloud.tencent.com/tcb/env/overview)页面请记住您的`环境Id`，这个 ID 后续部署需要用到。
2. 在本地安装 Node.js：如果未安装请前往 [Node.js 官网](https://nodejs.org) 下载安装，并确保 Node.js 安装成功。
3. 打开命令提示符，执行如下命令，安装 cloudbase cli：
```
npm install -g @cloudbase/cli
```

4. 执行登录命令：
```
tcb login
```
![](https://main.qcloudimg.com/raw/eb121b85b0d531343a44431c29678a05.png)
5. 在弹出的页面确认授权：
![](https://main.qcloudimg.com/raw/1daf46247dee75d63d86e017b6e3b3a1.png)
6. 在 hugo-site 中将 public 目录中的文件给部署上去：
```
cloudbase hosting:deploy ./public  -e EnvID
```
这里的 EnvID 替换为刚创建好的环境 ID。
![](https://main.qcloudimg.com/raw/e81c2cfea537c6a20730495c1a2c5d57.png)

7. 打开腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，进入[静态网站托管](https://console.cloud.tencent.com/tcb/hosting/index)页面，可以找到默认的域名，单击域名，就可以看到您刚部署的 Hugo。
