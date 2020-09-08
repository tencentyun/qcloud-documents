本文主要介绍如何使用云开发快速搭建一个简介的 Hexo 博客框架，无需搭建服务器、无需购买域名，即可完成您的博客搭建与部署。
最终博客成果展示如下：
![](https://main.qcloudimg.com/raw/590b7ee62174aa74f0119ac4775c6362.png)



## 步骤1：安装 CloudBase CLI 以及本地部署 Hexo

1. 在本地安装 Node.js：如果未安装请前往 [Node.js 官网](https://nodejs.org) 下载安装，并确保 Node.js 安装成功。
2. 安装 CloudBase CLI。打开命令提示符，执行如下命令：
```plaintext
npm i -g @cloudbase/cli hexo-cli
```
3. <span id="step1.3"></span>执行完毕后，在本地新建名称为 Hexo 的文件夹。在该文件夹中，打开命令提示符，并执行如下命令进行初始化：
```plaintext
hexo init
```
4. 在初始化过程中，您可以看到如下图的输出：
   ![](https://main.qcloudimg.com/raw/a194e51c289b3ec2e4662237387ed613.png)
5. 初始化完成后，执行如下命令，启动预览：
```plaintext
hexo s
```
![](https://main.qcloudimg.com/raw/789d798d929e69b980eb37f55bbbeb37.png)
预览后，在浏览器中打开 [localhost:4000](http://localhost:4000)，即可看到部署的 Hexo 博客。
![](https://main.qcloudimg.com/raw/5b91e6303e40aea5c1d5f0cfc521dc4a.png)



## 步骤2：创建云开发环境

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击【立即创建并使用】，新建一个环境来进行部署。
   ![](https://main.qcloudimg.com/raw/4b8ab97312e8cf697d3de48bf8c6d507.jpg)
   如果您之前创建过环境，可以继续使用已创建的**按量计费**环境，或者再次【新建环境】。
    ![](https://main.qcloudimg.com/raw/ac440a0f9e91f1f1dd3ac779d28ca008.jpg)
2. 在新建环境窗口中，根据实际需求填写环境名称，选择【按量计费】，单击【立即开通】即可开通环境。
   ![](https://main.qcloudimg.com/raw/5516e22060227892fe254d6027d343bf.jpg)
3. <span id="step2.3"></span>开通成功之后，单击环境名称，进入环境总览页面。如下所示：
   ![](https://main.qcloudimg.com/raw/c7fb3e0eaacfd716fddd0914a43eff00.jpg)
>!请记住您的环境 ID，这个 ID 在后续步骤将被使用。您可单击**环境Id**右侧的【<img src="https://main.qcloudimg.com/raw/a06f957521023a64e977041f9181f251.jpg"  style="margin:0;">】图标进行复制。
4. 单击左侧菜单栏中的【静态网站托管】，在页面中单击【开启使用】，开通静态托管服务。
![](https://main.qcloudimg.com/raw/b2722f1c74c77d582802a0ddedf1823c.png)
当您能看到如下界面时，即说明开通成功。
![](https://main.qcloudimg.com/raw/c76868e35d23f97bbd39f261073385a6.jpg)





## 步骤3：初始化云开发 CLI

1. 在本地打开命令提示符，执行如下命令：
```plaintext
cloudbase login
```
2. 执行命令时，系统将拉起浏览器授权，请登录上述 [步骤2](#step2.3) 中创建云开发环境的账号，进行确认授权。
![](https://main.qcloudimg.com/raw/07bbd145af217f65a4c321d977fdcb32.jpg)



## 步骤4：构建 Hexo 部署文件

1. 打开命令提示符，进入到 [步骤1](#step1.3) 创建的 Hexo 文件夹中，执行如下命令：
```plaintext
Hexo g
```
2. Hexo 将会生成部署文件，默认将文件生成在 Public 文件夹下：
![](https://main.qcloudimg.com/raw/8d2308d3afe74030237f03545d9371fc.png)
3. 执行如下命令，将 Hexo 部署到云开发静态托管中（需要将 EnvID 替换为 [步骤2](#step2.3) 中您创建的环境 ID）。
```plaintext
cloudbase hosting:deploy public -e [EnvID]
```
![](https://main.qcloudimg.com/raw/0bf195a98476e103199bdfeefd375945.png)

## 步骤5：浏览部署的 Hexo

1. 回到云开发控制台 [静态网站托管](https://console.cloud.tencent.com/tcb/hosting/index) 页面。
2. 单击【基础配置】，在域名信息中找到默认域名。
   ![](https://main.qcloudimg.com/raw/f5bec269430faa18cb19ce9792c09d13.jpg)
3. 在浏览器中输入该链接并回车，即可打开线上部署好的 Hexo 博客。
   ![](https://main.qcloudimg.com/raw/590b7ee62174aa74f0119ac4775c6362.png)
