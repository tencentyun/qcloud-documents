
## 操作场景
Cloud Studio 应用镜像是一个提供了轻量级，且功能强大的源代码编辑器的应用镜像，底层基于 VS Code 扩展实现，除了完全兼容 VS Code 所有能力外，还提供了额外扩展能力。您可以使用浏览器直接访问使用，对多种开发语言支持良好。Cloud Studio 应用镜像内置了对 JavaScript、TypeScript 和 Node.js 的支持，并为其他语言在运行时（如 C++、C#、Java、Python、PHP、Go、.NET）提供了丰富的扩展生态系统。镜像中已预置 Go、Python、Node.js、Clang 及 JDK 开发环境。
您可以通过 Cloud Studio 快速搭建一个云端开发环境，只要有浏览器和网络，就可以快速访问您的云端开发环境，从而开发业务项目或者管理服务器环境。
## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在 **服务器** 页面单击新建。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
 - **镜像**：选择为应用模板 > 开发工具场景 > Cloud Studio 应用模板，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 应用模板即应用镜像。
- 查看镜像说明详情请参见 [基本概念](https://cloud.tencent.com/document/product/1207/79254)。
</dx-alert>
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，则地域选择 “广州”。
 - **可用区**：默认勾选“随机分配”，也可自行选择可用区。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、带宽或峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用“镜像名称 + 四位随机字符”。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的 3 个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击**立即购买**，并根据页面提示提交订单完成支付，返回轻量应用服务器控制台。
4. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。您可以在此页面查看 Cloud Studio 应用的各项配置信息。
5. 选择**应用管理**页签，进入应用管理详情页。
6. 在“应用内软件信息”栏中，单击 ![](https://qcloudimg.tencent-cloud.cn/raw/b3dddaaafdaa1ede470b557a90433121.png)，复制获取 Cloud Studio 1.0.1 的管理员帐户密码的命令。
7. 在“应用内软件信息”栏中，单击**登录**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b2e1b14cd007e7842513d0366ee551c7.png)
8. 在弹出的登录窗口中，粘贴步骤 6 复制的命令并按 Enter。即可获取 Cloud Studio 管理员账号密码，请妥善保管并记录。
9. 关闭登录窗口，并返回该实例的应用管理详情页。
10. 在“应用内软件信息”栏中，单击 Cloud Studio 1.0.1 的访问地址。
11. 自动跳转到登录地址，在登录页面中输入步骤 8 获取的管理员帐户密码，并单击"SUBMIT"。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d297adc941033b22f44174e85e0a49da.png)
验证成功后即可进入 Cloud Studio 工作界面。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6f65614ae8dcb63835d665b64b56632d.png)
>?如果您的应用访问地址是非 HTTPS 协议，部分功能和插件将不可用（WebView 需要在 HTTPS 协议下工作）。



## 后续操作
### 创建项目
创建项目的本质是创建或者选择一个目录作为项目，在 Cloud Studio 中创建项目的方式有很多种：

#### 方式一：选择一个已有的目录作为项目
![](https://qcloudimg.tencent-cloud.cn/raw/2ab259921e06d7aad4c06097615a05d1.png)

#### 方式二：通过文件菜单选择一个目录作为项目
![](https://qcloudimg.tencent-cloud.cn/raw/aba42efb3e98fc26fba6fd1ed2aa935e.png)

#### 方式三：通过命令行终端选择一个目录作为项目
1. 新建一个终端：
![](https://qcloudimg.tencent-cloud.cn/raw/b3fcf5467d9d753b678018d64e26a3ba.png)
2. 使用 `cloudstudio` 命令打开一个目录作为项目：
![](https://qcloudimg.tencent-cloud.cn/raw/b05a1aeaeed1dd5ab2e2590b5dba2cfe.png)
>?cloudstudio 命令除了快速打开一个目录以外，还有更多丰富的功能，例如：安装插件、计算文件之间的差异、定位到文件内容的行列。

#### 方式四：从代码仓库中克隆项目：
![](https://qcloudimg.tencent-cloud.cn/raw/e9946f7f786cf8b2418fcf2cc48c5957.png)



### 使用示例
Cloud Studio 目前支持 Python、Java、Go、C/C++ 及 Node.js 语言。该步骤以命令行及界面两种方式分别运行 Python、Go 及 C++ 语言程序示例，您可按需选择对应语言进行操作。

#### Python

1. 创建一个目录 DEMO，并在 Cloud Studio 打开 DEMO 目录。
2. 在 DEMO 目录下创建简单示例文件 main.py。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/71aefbf09c1298a48021908c4f0ede8c.png)
3. 使用以下任意一种方式运行该程序：
<dx-tabs>
::: 命令行方式
1. 选择窗口上方的**终端** > **新建终端**，打开终端。
2. 在终端中执行以下命令：`python main.py`，运行程序。执行结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d938e4a879e93f0fa764e21ab8049cd2.png)
:::
::: 界面方式
当您打开 main.py 文件，编辑器会提示您是否要安装 Python 插件，选在安装，安装完后就可以通过界面方式运行程序了。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/95c3da58de083832fc9ecf12dd77ea7f.png)
:::
</dx-tabs>


#### Node.js

1. 创建一个目录 DEMO，并在 Cloud Studio 打开 DEMO 目录。
2. 在 DEMO 目录下创建简单示例文件 main.js。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fe2c7c63e4f4ee982d219b455214cdd6.png)
3. 使用以下任意一种方式运行该程序：
<dx-tabs>
::: 命令行方式
1. 选择窗口上方的**终端** > **新建终端**，打开终端。
2. 在终端中执行以下命令：`node main.js` 运行程序。执行结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8eb2756a59412e2874e863db808dd442.png)
:::

::: 界面方式
1. 选择左侧的第四个“运行和调试”活动页。
2. 在“运行和调试”活动页中，有三种方式运行您的 Node.js 代码：点击“运行和调试”按钮、创建 launch.json 文件和使用 JavaScript 调试终端（在这个终端运行 `node main.js` 命令，将以调试模式运行，支持设置断点）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6de330d5d8c39d67134cd9c75e9e9598.png)
3. 选择单击“运行和调试”按钮方式运行，并选择 Node.js 调试器（不同语言需要选择不同的调试器）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f990374646f7830a06d7e734054380ef.png)
4. 选择完调试器后，就会以调试模式运行程序，如果在程序中，存在断点，程序的执行会停在断点的位置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/912b5ece652e18efe1441ac90584f056.png)
:::
</dx-tabs>


  
