本文主要介绍如何使用云开发快速搭建一个简介的 Hexo 博客框架，无需搭建服务器、无需购买域名，即可完成您的博客搭建与部署。
最终博客成果展示如下：
![](https://main.qcloudimg.com/raw/590b7ee62174aa74f0119ac4775c6362.png)




## 步骤1：安装 CloudBase CLI 以及本地部署 Hexo

1. 在本地安装 Node.js：如果未安装请前往 [Node.js 官网](https://nodejs.org) 下载安装，并确保 Node.js 安装成功。
2. 安装 CloudBase CLI。打开命令提示符，执行如下命令：
```plaintext
npm i -g @cloudbase/cli hexo-cli
```
3. 执行完毕后，在本地新建一个文件夹。在该文件夹中，运行命令提示符，并执行如下命令进行初始化：
```plaintext
hexo init
```
4. 在初始化过程中，您可以看到如下图的输出：
![](https://main.qcloudimg.com/raw/bd3621309a7209aca11eb251f3ed139a.png)
5. 初始化完成后，执行如下命令，启动预览：
```plaintext
hexo s
```
![](https://main.qcloudimg.com/raw/2cfab06f6c487057cbb8934cea6a5fb0.png)
预览后，在浏览器中打开 [localhost:4000](http://localhost:4000)，即可看到部署的 Hexo 博客。
![](https://main.qcloudimg.com/raw/5b91e6303e40aea5c1d5f0cfc521dc4a.png)



## 步骤2：创建云开发环境

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击【立即创建】，新建一个环境来进行部署。
   ![](https://main.qcloudimg.com/raw/373ce011bfad392b5c2fedd8008bb6f5.png)
   如果您之前创建过环境，可以继续使用已创建的**按量计费**环境，或者再次【新建环境】。
	 ![](https://main.qcloudimg.com/raw/ac440a0f9e91f1f1dd3ac779d28ca008.jpg)
2. 在新建环境窗口中，根据实际需求填写环境名称，选择按量计费，开通环境。
   ![](https://main.qcloudimg.com/raw/529c3e20d8eb4edc7ab4c6fa504a52c7.png)
>!在开通环境以后， 记住您的环境 ID，这个 ID 在后续步骤将被使用。
4. 单击环境，进入到环境管理页面。单击左侧菜单栏中的【静态网站托管】，在页面中单击【开启使用】，开通静态托管服务。
   ![](https://main.qcloudimg.com/raw/cb71498de333edd4006a6708d896de6d.png)
   当您能看到如下界面时，即说明已开通成功。
   ![](https://main.qcloudimg.com/raw/2f02da70e4fa2f52170ef7b1577717b1.png)



## 步骤3：初始化云开发 CLI

1. 在本地打开命令提示符，执行如下命令：
```plaintext
cloudbase login
```
2. 执行命令是，系统将拉起浏览器授权，请登录上述步骤2中创建云开发环境的账号，进行确认授权。
![](https://main.qcloudimg.com/raw/026ba161e5820db9efa889c3b0d0c367.png)



## 步骤4：构建 Hexo 部署文件

1. 打开命令提示符，定位到步骤1新建的 Hexo 目录中，执行如下命令：
```plaintext
Hexo g
```
2. Hexo 将会生成部署文件，默认将文件生成在 Public 目录下：
![](https://main.qcloudimg.com/raw/3be759a243289440eb5aaf7eee423195.png)
3. 执行如下命令，将 Hexo 部署到云开发静态托管中（需要将 EnvID 替换为步骤2中您创建的环境 ID）。
```plaintext
cloudbase hosting:deploy public -e [EnvID]
```
![](https://main.qcloudimg.com/raw/7d539f3190b6c8c457044448424d4ee4.png)

## 步骤5：浏览部署的 Hexo

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击部署的云开发环境。
2. 在左侧菜单栏中，单击【静态网站托管】-【基础配置】，在域名信息中找到默认域名。
   ![](https://main.qcloudimg.com/raw/961855455d64f242bc96f9c951bf53b2.png)
2. 在浏览器中打开此链接，则看到线上部署好的 Hexo 博客。
   ![](https://main.qcloudimg.com/raw/590b7ee62174aa74f0119ac4775c6362.png)
