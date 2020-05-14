## 操作场景
本文档介绍通过腾讯云静态网站托管服务搭建一个 Hexo 网站，并使用云开发 CLI 工具管理部署 Hexo 网站。

## 前提条件
在进行后续的内容前，请先确保您的电脑中安装了 Node.js 运行环境。如果没有安装，可以访问 https://nodejs.org/ 下载安装。

## 操作步骤
### 步骤1：安装云开发 CLI 工具和 Hexo

执行如下命令，安装云开发 cli 工具以及 Hexo：
```
npm i -g @cloudbase/cli hexo-cli
```
### 步骤2：在本地初始化一个 Hexo 项目
首先，我们创建一个 Hexo 项目，执行如下命令：
```
hexo init
```
可以看到下面这样的输出：
![](https://main.qcloudimg.com/raw/e819da34ec6c93e5b144567652b6dd8f.png)
初始化完成后，输入下面这段代码进入到目录中，并启动预览。
```
cd blog
hexo s
```
![](https://main.qcloudimg.com/raw/5debcf8d5401a1b4e69c2035d54d330d.png)
然后，在浏览器中打开 localhost:4000，看到 Hexo 的界面就说明已经成功的完成了 Hexo 的本地初始化。
![](https://main.qcloudimg.com/raw/ac6d94e3810b192ed8d13d3df1a8921f.png)

### 步骤3：创建一个云开发环境

完成了本地的 Hexo 建设，接下来我们来创建一个云开发环境，用来部署 Hexo。

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



### 步骤4：使用 CLI 部署 Hexo
#### 初始化云开发 CLI
完成了云开发环境的配置后，我们需要初始化一下云开发 CLI ，从而实现借助 CLI 工具来上传页面（您也可以通过网页端直接上传，但如果您博客的文章比较多，建议使用 CLI 工具上传更加方便）
在命令行输入如下代码：
```
tcb login
```
会提醒您需要在网页中进行授权：
![](https://main.qcloudimg.com/raw/0390dad15ae1a786d3e492c11c9277bb.png)

在弹出的页面中单击【确认授权】。
![](https://main.qcloudimg.com/raw/40d3367db60f02f9312237d2657ad33f.png)

确认授权后，您会看到控制台输出相应的命令部署，到这里，您的云开发 CLI 就初始化好了。

#### 构建 Hexo 并上传
回到您的 Hexo 目录中，执行 Hexo g 来生成文件，Hexo 会默认将文件生成在 Public 目录下。
![](https://main.qcloudimg.com/raw/24f9830110b6bb10c661e07b128ea74b.png)
文件生成完成后，可以执行如下命令来进行部署（需要将 EnvID 替换为前面您的环境 ID）
```
cd public
tcb hosting:deploy ./ -e EnvID
```
稍等片刻，部署完成，接下来就可以预览了。
![](https://main.qcloudimg.com/raw/11710d7039ea7d3c1cef4bdcb33dbd13.png)

### 步骤5：浏览 Hexo

打开腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击左侧菜单栏中的【静态网站托管】>【设置】，进入设置页面，可以找到默认的域名，单击域名，就可以看到您刚部署的 Hexo。
![](https://main.qcloudimg.com/raw/439da24bfa3827fb41b8305c2ac1a5ae.png)


