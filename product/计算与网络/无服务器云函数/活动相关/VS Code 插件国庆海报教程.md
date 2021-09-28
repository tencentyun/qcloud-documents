## 操作场景
本文介绍了如何使用 VS Code 插件开发并部署 H5 页面，成功部署 H5 页面后填写 [礼物发送表](http://serverlesscloud.mikecrm.com/1bmzgEO) 即可领取礼物。

## 前提条件
- 已注册腾讯云账户。若未注册，请前往 [注册页面](https://cloud.tencent.com/register)。
- 已激活 SCF 使用权限。
如果您从未使用过 SCF，您需要前往 [SCF 控制台](<https://console.cloud.tencent.com/scf/index?rid=1>) 打开函数页面进行权限激活。打开页面后会自动激活权限，无需其他操作。
- 已安装 Node.js 8.9.x 版本。请查看您是否安装或是否使用对应版本，若不符合条件，请前往 [Node.js 官网](https://nodejs.org/zh-cn/download/releases/) 选择对应的版本进行安装。
- 已安装  Python 2.7（及以上版本）或 Python 3.6（及以上版本）。若为安装，请参考  [安装 Python 及 pip](https://cloud.tencent.com/document/product/583/33449#.E5.AE.89.E8.A3.85-python-.E5.8F.8A-pip)， 安装所需软件。


## 操作步骤




### 安装 SCF CLI
VS Code 插件部分功能依赖 SCF CLI，更多关于 SCF CLI 请参见 [概述](https://cloud.tencent.com/document/product/583/33445)。

1. 执行  `pip install scf` 命令，安装 SCF CLI。
2. 安装后执行 `scf --version` 命令验证是否安装成功。
输出结果如下，则成功安装 SCF CLI。如果未安装成功，请参考 [SCF 工具类常见问题](<https://cloud.tencent.com/document/product/583/33456>)。
```
SCF CLI, version 0.0.1
```

### 安装 VS Code 插件
1. 运行 VS Code IDE。
2. 单击左侧导航栏中的<img src="https://main.qcloudimg.com/raw/14b7872880f99820e01ad74de38fc956.png" style="margin:-3px 0;">，打开 VS Code 插件市场。
3. 在搜索框中输入以下信息：
```
Tencent Serverless Toolkit for VS Code
```
单击搜索框下方列表中的 Tencent Serverless 插件查看详情并选择**install**。如下图所示：
![](https://main.qcloudimg.com/raw/49a9ec2dad6e19a497dd148d9f2b88ee.png)
       

### 插件配置
1. 单击左侧导航栏的<img src="https://main.qcloudimg.com/raw/4395057dfb3a8f4a92c90ba7dff9b1c1.png" style="margin:-3px 0;">，打开已安装好的 Tencent Serverless 插件。
2. 单击创建一个腾讯云用户凭证，并输入相关凭证信息。如下图所示：
![](https://main.qcloudimg.com/raw/15592fb57aa84d524c07554dd852b31c.png)
 - AppId：请前往 [账号信息](https://console.cloud.tencent.com/developer) 获取。
 - ServiceId 及 ServiceKey：请前往 **访问管理** > **访问密钥** >  **[API 密钥](https://console.cloud.tencent.com/cam/capi)**获取。
 >!
 >- 若您未创建 ServiceId 及 ServiceKey，请在 [API 密钥](https://console.cloud.tencent.com/cam/capi) 管理页面进行创建。
 >- 函数期望所在地域请勿选择**成都**。

### 创建函数
您可根据实际需求，选择以下方式使用 VS Code 插件创建函数。



#### Git 拉取创建函数
>?使用 Git 拉取创建函数，须完成 VS Code IDE 和 git 的配置。若您没有安装 git 或已完成配置，请选择 [源码创建函数](#create)。
>
1. 打开插件，单击本地函数右侧的<img src="https://main.qcloudimg.com/raw/1a14823bd6129b9989e3ef34ed80a9cc.png" style="margin:-3px 0;">，并选择**Git 仓库**为代码来源后按 “**Enter**”。如下图所示：
![](https://main.qcloudimg.com/raw/2c9d4f9c05cbc41ce1fa84b59ad94551.png)
2. 将以下 git 地址填入输入框，并按 “**Enter**”。如下图所示：
```
https://github.com/TencentServerless/scf_vscode_demo1.git 
```
![](https://main.qcloudimg.com/raw/9836d6ebc8c9093c43190f2382a88884.png)
3. 输入自定义函数名（本文以 `testFunc` 为例），并按 “**Enter**”。如下图所示：
![](https://main.qcloudimg.com/raw/85c6edfe032cb8aeb5bf4349a81fe750.png)
4. 打开插件即可看到本地函数下已创建函数 `testFunc`。如下图所示：
![](https://main.qcloudimg.com/raw/30cd6a9c4ce2c70cebfd0e1316781594.png)        


[](id:create)
#### 源码创建函数
1. 请前往 [活动包下载地址](https://github.com/TencentServerless/scf_vscode_demo1.git )，选择**Clone or download** > **Download ZIP**。如下图所示：
![](https://main.qcloudimg.com/raw/c960496a9f897256383b7962763caa26.png)
2. 成功下载压缩包后请解压，并进入**scf_vscode_demo1-master** > **{{cookiecutter.project_name}}**目录打开 `template.yaml` 文件。
 - 将文件中的 `{{cookiecutter.namespace}}:` 替换为 `default:`。
 - 将文件中的 `{{cookiecutter.project_name}}:` 替换为 `testFunc:`。
 成功替换后保存，如下图所示：
 ![](https://main.qcloudimg.com/raw/ae7e46637e20316a580735b08889634d.png)
3. 单击 VS Code IDE 左上角的**File**，选择**Open Folder**。如下图所示：
![](https://main.qcloudimg.com/raw/da2380944925aace539b6b82b1a98c4d.png)
4. 在弹出界面上选择已下载的 `scf_vscode_demo1-master` 目录，单击**选择文件夹**确认选择。
5. 打开插件即可看到本地函数下已创建函数 `testFunc`。如下图所示：
![](https://main.qcloudimg.com/raw/30cd6a9c4ce2c70cebfd0e1316781594.png)     




### 修改函数
1. 单击左侧导航栏<img src="https://main.qcloudimg.com/raw/ac3668c67f7d6a66f977d5b32474390f.png" style="margin:-3px 0;">，打开 `index.js` 文件进入代码编辑页面。
2. 您可编辑以下信息来制定个性化海报，编辑后保存 `index.js` 文件 。如下图所示：
![](https://main.qcloudimg.com/raw/6c6620cbdae364dec9289d49dab6b46c.png)
     


### 调试函数
1. 进入插件页面，单击 `testFunc` 函数右侧的<img src="https://main.qcloudimg.com/raw/0e5a9ac04a38053224f6881b721cf35a.png" style="margin:-3px 0;">，打开本地调用页面。
2. 选择**API Gateway 网关响应请求时间模版**，并等待调试结果。如下图所示：
![](https://main.qcloudimg.com/raw/65ed4038c42540b3f1c96124565a8d76.png)
函数成功调用，则如下图所示：
![](https://main.qcloudimg.com/raw/79a829e0c74ba72076d448b5caaf21f3.png)



### 部署并测试函数
1. 单击 `testFunc` 函数右侧的<img src="https://main.qcloudimg.com/raw/2df1f1737b1b4c67f4ca8b5f3135247f.png" style="margin:-3px 0;">，并选择云端函数所在地域，本文以广州为例。如下图所示：
![](https://main.qcloudimg.com/raw/1d9b8f3e992fe289269995d2f55f1663.png)
2. 选择该地域下的 `defalut` 命名空间，`testFunc` 函数将被部署至此命名空间下。如下图所示：
![](https://main.qcloudimg.com/raw/ad3758a22bebfd05162c7b48a2afbfff.png)
3. 在右下角弹出框中，单击**Yes**并等待函数部署。如下图所示：
![](https://main.qcloudimg.com/raw/c7eff5687bc53452f99b08077fa360c4.png)
4. 部署成功后，您可通过右下角弹出框前往 SCF 控制台查看该函数。如下图所示：
![](https://main.qcloudimg.com/raw/83a1e90b2cbf3a1bac82a590375fdee2.png)
5.您可在输出信息中找到访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/e177e583e85b2f2da8dbdd4d0fde334a.png)
6. 在浏览器中访问此路径，即可看到成功部署的 H5 页面。如下图所示：
![](https://main.qcloudimg.com/raw/d92b529543f096fed16d6f6a1573deef.jpg)      

## 联系我们
如果您在使用的过程中遇到问题或者对 Tencent Serverless 感兴趣，欢迎扫描下方二维码加入 QQ 群（854582882）与我们交流。
![](https://main.qcloudimg.com/raw/afd3b9ad25dd3cc8c9d53288bc111d21.png)



