## 操作场景
本文档介绍通过腾讯云静态网站托管服务搭建一个 VuePress 网站，并使用云开发 CLI 工具管理部署 VuePress 网站。

## 前提条件
在进行后续的内容前，请先确保您的电脑中安装了 Node.js 运行环境。如果没有安装，可以访问 https://nodejs.org/ 下载安装。

## 操作步骤
### 步骤1：安装云开发 CLI 工具 和 VuePresss
执行如下命令，安装云开发 CLI 工具以及 VuePress。
```
npm i -g @cloudbase/cli vuepress
```

### 步骤2：在本地初始化一个 VuePress 项目
首先，在本地创建一个目录，这里以 tcb 为例：
```
mkdir tcb && cd tcb
```
进入到 tcb 目录后，创建一个默认的 hello world 文件。
```
echo "# Hello TCB & Vuepress" > README.md
```
![](https://main.qcloudimg.com/raw/db6cfcc664b38c32e8ce08055f6ffc7d.png)

然后，执行命令，启动，并查看效果。
```
vuepress dev
```
等待其编译完成，完成后如下如所示。
![](https://main.qcloudimg.com/raw/0b1c90a075f1f4914ecc6c487e9abcbc.png)

打开浏览器访问： localhost:8080 可以看到刚刚创建的文档产生的页面，说明已经成功的完成了 VuePress 的本地初始化。
![](https://main.qcloudimg.com/raw/ecf3a06a5fef49864fe1e7983f9e091d.png)


### 步骤3：创建一个云开发环境

完成了本地的 Vuepress 建设，接下来我们来创建一个云开发环境，用来部署 VuePresss。打开腾讯云控制台，在产品中找到云开发

1. **开通云开发环境**
打开腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击【新建环境】，新建一个环境进行部署。
![](https://main.qcloudimg.com/raw/f7344bae9468324172aeaae84e10dbbf.png)
 选择新建一个环境，填写环境名称并选择按量计费，开通环境。
![](https://main.qcloudimg.com/raw/99581595ff8cfe491a1563140fd7411e.png)
 在开通环境以后，请记住您的环境 ID，这个 ID 后续部署需要用到。
2. **开通静态网站托管**
云开发环境创建完成后，单击左侧菜单栏中的【静态网站托管】，单击【选择已有按量计费环境】
![](https://main.qcloudimg.com/raw/0066b2dd6c36857cd0f52d3916c3c8d1.png)

 当您看到这样的界面时，就说明已经开通好了。
![](https://main.qcloudimg.com/raw/64f31f5655bfcce0506262c3f7f9163c.png)
![](9.png)

 您现在可以通过上传文件手动上传一个文件测试，稍后，我们将会用云开发 CLI 来完成上传。

### 步骤4：使用 CLI 部署 VuePress
#### 初始化云开发 CLI
完成了云开发环境的配置后，我们需要初始化一下云开发 CLI ，从而实现借助 CLI 工具来上传页面（您也可以通过网页端直接上传，但如果您博客的文章比较多，建议使用 CLI 工具上传更加方便）
在命令行输入如下代码：
```
tcb login
```
会提醒您需要在网页中进行授权：
![](https://main.qcloudimg.com/raw/0390dad15ae1a786d3e492c11c9277bb.png)
在弹出的页面中单击【确认授权】。
![](https://main.qcloudimg.com/raw/40d3367db60f02f9312237d2657ad33f.png)
确认授权后，您会看到控制台输出相应的命令部署，到这里，您的云开发 CLI 就初始化好了。

#### 部署 VuePress
回到我们刚刚创建的 VuePress 的目录，执行命令构建静态页面：
```
vuepress build
```
构建完成后，会提醒您，生成的静态文件在 .vuepress/dist。
![](https://main.qcloudimg.com/raw/f3e4e1d548b947b289a68d8ad7cafbdd.png)

接下来我们只需要把 .vuepress/dist 中的文件夹中的内容上传到云开发静态网站托管中就可以了。
执行如下命令进入到 dist 文件夹
```
cd .vuepress/dist
```
然后执行命令上传文件，记得将这里的 EnvID 替换为您自己的环境的环境 ID。
```
tcb hosting:deploy ./ -e EnvID
```
稍等片刻，文件就上传好了
![](https://main.qcloudimg.com/raw/898ed57cfd784b3204b706c4636b8b0c.png)

此时，您在云开发管理控制台也可以看到这些文件，说明成功上传。
![](https://main.qcloudimg.com/raw/d21f08ea7b0aea3be8d6e5ca1bf1421c.png)

### 步骤5：浏览 VuePress
打开腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击左侧菜单栏中的【静态网站托管】>【设置】，进入设置页面，可以找到默认的的域名，单击域名，就可以看到您刚刚部署的 VuePress。
![](https://main.qcloudimg.com/raw/439da24bfa3827fb41b8305c2ac1a5ae.png)

