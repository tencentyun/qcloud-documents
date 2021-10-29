## 操作场景
本文档介绍通过腾讯云静态网站托管服务搭建一个 Hexo 网站，并使用云开发 CLI 工具管理部署 Hexo 网站。
云开发提供两种方式进行部署：
- 方式一：一键部署项目至云端。
- 方式二：使用 CLI 工具，手动将本地文件部署至云端。

## 一键部署 Hexo

单击下方按钮可一键部署 Hexo 到云开发：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-templates&workDir=hexo&branch=master" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div>



## CLI 工具部署

### 前提条件

在进行后续的内容前，请先确保您的电脑中安装了 Node.js 运行环境。如果未安装，可以前往 [Node.js 官网](https://nodejs.org/) 下载安装。

### 操作步骤

#### 步骤1：安装云开发 CLI 工具和 Hexo

执行以下命令，安装云开发 CLI 工具以及 Hexo：
```plaintext
npm i -g @cloudbase/cli hexo-cli
```

#### 步骤2：在本地初始化一个 Hexo 项目

1. 执行以下命令，创建一个 Hexo 项目：
```plaintext
hexo init
```
 命令执行之后，可以查看到如下图输出：
![](https://main.qcloudimg.com/raw/7f3545701357ca19faff23e834622496.png)
2. 初始化完成后，执行以下命令进入到目录中，并启动预览。
```plaintext
cd blog
hexo s
```
 命令执行过程如下图所示：
 ![](https://main.qcloudimg.com/raw/5debcf8d5401a1b4e69c2035d54d330d.png)
3. 在浏览器中输入 `localhost:4000`，看到 Hexo 的界面即说明已成功完成 Hexo 的本地初始化。
![](https://main.qcloudimg.com/raw/ac6d94e3810b192ed8d13d3df1a8921f.png)

#### 步骤3：创建一个云开发环境

完成本地的 Hexo 建设，接下来创建一个云开发环境，用于部署 Hexo。

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



#### 步骤4：使用 CLI 部署 Hexo
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
2. 构建 Hexo 并上传
	1. 在 Hexo 目录，执行 `Hexo g` 命令来生成文件，Hexo 会默认将文件生成在 Public 目录下。如下图所示：
	![](https://main.qcloudimg.com/raw/24f9830110b6bb10c661e07b128ea74b.png)
	2. 文件生成完成后，可以执行以下命令来进行部署（需要将 EnvID 替换为前面您的环境 ID）：
	```plaintext
	cd public
	tcb hosting deploy ./ -e EnvID
	```
    稍等片刻等待部署完成，即可预览页面。
![](https://main.qcloudimg.com/raw/127bae3dbb9fc635acb535ce592c3664.png)



#### 步骤5：浏览 Hexo

1. 登录腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，单击左侧菜单栏中的**静态网站托管** > **文件管理**，进入文件管理页面。
2. 在文件管理页面可以找到默认的域名，单击域名，即可访问您部署的 VuePress。
![](https://main.qcloudimg.com/raw/bba86e0e75526788d65c931bdcd5296d.jpg)



### 相关命令

#### 卸载 Hexo
```bash
npm uninstall -g @cloudbase/cli hexo-cli
```
