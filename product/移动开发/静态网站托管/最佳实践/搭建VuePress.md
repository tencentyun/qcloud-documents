## 操作场景

本文档介绍通过腾讯云静态网站托管服务搭建一个 VuePress 网站，并使用云开发 CLI 工具管理部署 VuePress 网站。
- 方式一：一键部署项目至云端。
- 方式二：使用 CLI 工具，手动将本地文件部署至云端。



## 一键部署 VuePress

单击下方按钮可一键部署 VuePress 到云开发：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https://github.com/TencentCloudBase/cloudbase-templates&workDir=vuepress" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div>



## CLI 工具部署

### 前提条件

在进行后续的内容前，请先确保您的电脑中已安装 Node.js 运行环境。如果未安装，可以访问 [Node.js 官网](https://nodejs.org/) 下载安装。


### 操作步骤
#### 步骤1：安装云开发 CLI 工具 和 VuePresss

执行以下命令，安装云开发 CLI 工具以及 VuePress。
```plaintext
npm i -g @cloudbase/cli vuepress
```

#### 步骤2：在本地初始化一个 VuePress 项目

1. 执行以下命令，在本地创建一个目录，本文以 tcb 为例：
```plaintext
mkdir tcb && cd tcb
```
2. 进入到 tcb 目录后，执行以下命令，创建一个默认的 hello world 文件。
```plaintext
echo "# Hello TCB & Vuepress" > README.md
```
 ![](https://main.qcloudimg.com/raw/db6cfcc664b38c32e8ce08055f6ffc7d.png)
3. 执行以下命令，启动 VuePresss。
```plaintext
vuepress dev
```
 等待其编译完成，完成后如下图所示：
![](https://main.qcloudimg.com/raw/0b1c90a075f1f4914ecc6c487e9abcbc.png)
5. 打开浏览器访问 `localhost:8080`，可以看到上述步骤创建的文档产生的页面，说明已成功完成 VuePress 的本地初始化。
![](https://main.qcloudimg.com/raw/ecf3a06a5fef49864fe1e7983f9e091d.png)


#### 步骤3：创建一个云开发环境

完成本地的 Vuepress 建设，接下来创建一个云开发环境，用于部署 VuePresss。

1. **开通云开发环境**
 1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击**新建**，新建一个环境进行部署。
 2. 应用来源选择**模板仓库**或**代码导入**，并进行相应的配置，详情可参见 [应用部署](https://cloud.tencent.com/document/product/1210/52128)。
 3. 选择环境所属地域，选择**按量计费**计费方式，填写环境名称后单击**下一步**。
![](https://main.qcloudimg.com/raw/20fcf922ca5ef64ddea391c695b53fd1.jpg)
 4. 根据提示进行相应的配置创建一个云开发环境。
>?在开通环境以后，请记住您的环境 ID，该 ID 后续部署需要用到。
2. **开通静态网站托管**
云开发环境创建完成后，单击左侧菜单栏中的**静态网站托管**，根据页面提示单击**开通静态网站托管**进行开通。
![](https://main.qcloudimg.com/raw/2fe3d190ee80896ff59a65e0680f486d.jpg)
 当出现如下图时，则说明静态网站托管已经开通。
![](https://main.qcloudimg.com/raw/bba86e0e75526788d65c931bdcd5296d.jpg)
 您现在可以通过上传文件手动上传一个文件测试，稍后，我们将会使用云开发 CLI 来完成上传。

#### 步骤4：使用 CLI 部署 VuePress

1. 初始化云开发 CLI
完成云开发环境配置后，需要初始化云开发 CLI ，从而实现借助 CLI 工具来上传页面（您也可以通过网页端直接上传，但如果您博客的文章比较多，建议使用 CLI 工具进行上传）。
 1. 在命令行中执行以下命令登录云开发：
```plaintext
tcb login
```
 2. 执行之后将提醒您需要在网页中进行授权：
![](https://main.qcloudimg.com/raw/0390dad15ae1a786d3e492c11c9277bb.png)
在弹出的页面中单击**确认授权**。
![](https://main.qcloudimg.com/raw/463da60ca3bc6a14939147e525c45636.png)
确认授权后，您会看到控制台输出相应的命令部署。至此，您的云开发 CLI 已初始化完毕。
2. 部署 VuePress
 1. 在 VuePress 的目录，执行以下命令构建静态页面：
	```plaintext
	vuepress build
	```
	 构建完成后，系统将提醒您生成的静态文件在 `.vuepress/dist`。如下图所示：
	![](https://main.qcloudimg.com/raw/f3e4e1d548b947b289a68d8ad7cafbdd.png)
 2. 需要将 `.vuepress/dist` 中的文件夹中的内容上传到云开发静态网站托管。
执行以下命令进入到 dist 目录：
```plaintext
cd .vuepress/dist
```
    在 dist 目录中执行以下命令上传文件，此处需要将 EnvID 替换为您自己环境的环境 ID：
```plaintext
tcb hosting:deploy ./ -e EnvID
```
    稍等片刻，文件即可上传完毕，如下图所示：
![](https://main.qcloudimg.com/raw/4ebdc5d9e04d2af69be4068f7e43da71.png)
此时，您在云开发控制台 [静态网站托管](https://console.cloud.tencent.com/tcb/hosting) 页面同样可以查看到已上传的文件，说明成功上传。
![](https://main.qcloudimg.com/raw/1e5f7bfa48b48a1db6ca159077f4637a.jpg)





#### 步骤5：浏览 VuePress

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击左侧菜单栏中的**静态网站托管** > **文件管理**，进入文件管理页面。
2. 在文件管理页面可以找到默认的域名，单击域名，即可访问您部署的 VuePress。
![](https://main.qcloudimg.com/raw/bba86e0e75526788d65c931bdcd5296d.jpg)

