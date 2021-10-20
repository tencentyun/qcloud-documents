## 操作场景
腾讯云提供的**计算型 GPU 实例（GN6/GN6S/GN7/GN8/GN10X）**采用了 NVIDIA P4、T4、P40 以及 V100 等。Tesla 系列 GPU 可同时支持**通用计算**和**图形图像处理**，例如：
- 安装免费的 Tesla Driver 和 CUDA SDK ，可用作深度学习、科学计算等通用计算场景。
- 安装 GRID Driver 并且配置相关的 License 服务器，可开启 GPU 的 OpenGL 或 DirectX 图形加速能力。

使用 Tesla 系列 GPU 用作图形图像处理，需要向 NVIDIA 或其代理商购买对应的 License。此外，NVIDIA 也提供了90天试用 License 的申请。本文将介绍申请试用 License，并配置 License 服务器和安装 GRID driver。
>?
>- 如在申请过程中遇到问题，则请与 NVIDIA 联系，本文仅供参考。
>- 您也可直接使用腾讯云 GN7vw 服务器，免除 vDWS License 申请及搭建服务器步骤。腾讯云 GN7vw 服务器目前在试用阶段，您可 [联系我们](https://cloud.tencent.com/act/event/connect-service) 申请试用。 
>

## 操作步骤
### 申请 License

1. 前往 [NVIDIA Enterprise Account](http://www.nvidia.com/object/nvidia-enterprise-account.html)，注册账号并申请试用 License。具体步骤请参考 [注意事项](https://mp.weixin.qq.com/s/a6U1-GFAM9jXoLfvxO6nGA)。
2. 成功提交申请后，将提示您于2天内在设置的邮箱查收邮件。
  如果您申请的地区是中国，或者使用了公共邮箱进行注册，您可能会收到如下邮件：
![](https://main.qcloudimg.com/raw/886921716160a2e4a60c1960193a2b31.png)
3. 测试 License 账户需要2天的时间由后台进行账号审批，审批通过后，您会收到2封邮件。如下图所示：
![](https://main.qcloudimg.com/raw/29a7849a262bdadee0d2f27d44a28e27.png)
4. 打开邮件 “NVIDIA Set Password”。如下图所示：
![](https://main.qcloudimg.com/raw/aef2da023c67eb2fb65d232ee68e318e.png)
5. 选择 **SET PASSWORD** 并设置初始口令，设置完成即可单击 **LOGIN** 登录您的 NVIDIA 企业账号。也可前往 [NVIDIA 许可门户网站](https://nvid.nvidia.com) 进行登录。
6. 登录成功后，进入 “Dashboard” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/fef04abe7c0bcc9e4c818dfcc930739f.png)
<dx-alert infotype="explain" title="">
vGPU 试用的全部资源均可由此网站获得，包括 vGPU 软件和 License Server 软件。
</dx-alert>



### 软件准备 
1. 选择左侧导航栏中的 **SOFTWARE DOWNLOADS**，进入 “Software Downloads” 页面。
2. [](id:step2)选择下拉框中的 **Miscrosoft Windows Hyper-V** 及 **2016**，单击目标搜索结果所在行右侧的 **Download**。即使用最新的 NVIDIA Virtual GPU SoftWare 版本，本文以 GRID 9.3 版本为例。如下图所示：
![](https://main.qcloudimg.com/raw/1856fd04b607e287ee6646f3b473986a.png)
3. [](id:step3)创建一台普通云服务器，作为 License 服务器。详情请参见 [创建实例](https://cloud.tencent.com/document/product/213/4855)。 
<dx-alert infotype="explain" title="">
云服务器操作系统建议使用 Windows Server 2012 R2 版本。
</dx-alert>
4. 选择页面右上角的 **Additional Software**，单击所需下载的 License Server 软件。本文以下载 **2019.11 64-bit License Manager for Windows** 为例，如下图所示：
![](https://main.qcloudimg.com/raw/ac53951a67c2ead8fbd31162c906ff97.png)
5. [](id:step5)将 License Server 软件安装至 [步骤3](#step3) 创建的云服务器，详情请参见 [License Server User Guide](https://docs.nvidia.com/grid/ls/2019.11/grid-license-server-user-guide/index.html)。在完成安装后获取该 License 服务器的 MAC 地址。
6. 选择左侧导航栏中的 **LICENSE SERVERS**，进入 “License Servers” 页面。
7. 选择右上角的 **CREATE LICENSE SERVER**，在弹出的 “Create License Server” 窗口中填写相关信息注册新的 License Server。
其中 MAC Address 请填写 [步骤5](#step5) 获取的 License 服务器 MAC 地址。
8. 成功创建后，在 “License Servers” 页面选择该项下的 <image src="https://main.qcloudimg.com/raw/ef09b35b77fa2e046f6f072467d47b8f.png" style="margin:-3px 0px"/>，添加多个特性。如下图所示：
![](https://main.qcloudimg.com/raw/9db8abf9839528846cb9881ce1203230.png)
9. 在弹出的 “Add Features” 页面，选择您试用的 License Feature，填写该 License 服务器的 License 数量，并单击 **ADD**。如下图所示：
![](https://main.qcloudimg.com/raw/1027c752bbae5ea762286177f7754e87.png)
10. 确认添加完毕后，单击 **ADD FEATURES**。
11. 成功添加后，可在 “License Servers” 页面查看授权该 License 服务器的状态，包含数量和 License 过期时间。
12. 选择 <image src="https://main.qcloudimg.com/raw/269934ba79e61ca40fccb34de5540e7d.png" style="margin:-3px 0px"/>，下载用于该 License Server 的 License 授权文件。如下图所示：
![](https://main.qcloudimg.com/raw/17264de866a6657c412919a417bb842a.png)


### 配置 License 服务器

<dx-alert infotype="explain" title="">
授权文件下载完成后，需在24小时内通过 License 管理控制台导入该 License 文件。更多信息请参见 [NVIDIA官方文档](https://docs.nvidia.com/grid/6.0/grid-software-quick-start-guide/index.html#installing-grid-license-server-and-licences)。
</dx-alert>

1. 使用 License 服务器访问 License 管理控制台：`http://localhost:8080/licserver`。
2. 选择左侧 License Server 栏中的 **License Management**，并导入 License 文件。
3. 选择 **Licensed Feature Usage**，查看授权数量。如下图所示：
![](https://main.qcloudimg.com/raw/be19c04dc5970ff01e2588ebd532b742.png)

### 安装 GRID Driver
1. 购买并创建一台计算型 GPU 实例（GN6/GN6S/GN7/GN8/G10X）。详情请参见 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
2. 登录实例，详情请参见 [使用标准方式登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/57778)。
3. 安装 GRID Driver 安装程序，即安装 NVIDIA vGPU for Windows 驱动程序。打开安装程序后按照界面提示完成安装，如下图所示：
![](https://main.qcloudimg.com/raw/7c29eb739e3120a1758140da95620486.png)
完成安装后，在控制面板中查看驱动是否安装正确。如下图所示：
![](https://main.qcloudimg.com/raw/b29c6b952a9f8fa339ea8a791c217de7.png)
4. 使用远程桌面连接方式登录 GPU 实例，详情请参见 [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。
<dx-alert infotype="explain" title="">
微软的远程桌面不支持使用 GPU 的 3D 硬件加速能力，如需使用则请安装第三方桌面协议软件，并通过对应客户端连接实例，使用 GPU 图形图像加速能力。
</dx-alert>
5. 在 GPU 实例中，右键单击桌面或者单击任务栏的右下角 <image src="https://main.qcloudimg.com/raw/6ebb7cb48331add50a978ad34d5ede07.png" style="margin:-6px 0px"/>，打开 NVIDIA Control Panel。
6. 选择**管理许可证**，配置 License 服务器的 IP 地址和端口号，并确保 License 服务器的 IP 地址可以被访问，以及端口号已设置为开放状态。例如，将 License 服务器的 IP 地址配置为公网 IP 或者在同一个 VPC 内的内网地址，配置的 IP 地址可以被用户正常访问，且端口号已设置为开放状态。如下图所示：
![](https://main.qcloudimg.com/raw/ecc9a4e31e9b70256cbc2237ee68c6bf.png)
7. 完成以上配置，NVIDIA GPU 实例便即可运行图形图像处理程序。如下图所示：
![](https://main.qcloudimg.com/raw/bc690d2fc2dd6f1828ed9ee1e8e5bf95.png)



