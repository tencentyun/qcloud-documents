腾讯云提供的**计算型 GPU 实例（GN6/GN6S/GN7/GN8/GN10X）**采用的 NVIDIA P4、T4、P40以及 V100 等。Tesla 系列 GPU 可同时支持**通用计算**和**图形图像处理**。
- 安装免费的 Tesla Driver 和 CUDA SDK ，可用作深度学习、科学计算等通用计算场景。
- 安装 GRID Driver 并且配置相关的 License 服务器，可打开 GPU 的 OpenGL 或 DirectX 图形加速能力。

使用 Tesla 系列 GPU 用作图形图像处理，需要向 NVIDIA 或其代理商购买对应的 License。此外，NVIDIA 也提供了 90天试用 License 的申请。
本文将介绍如何申请试用 License，如何配置 License 服务器和安装 GRID driver。

**注：具体申请中遇到的问题请与NVIDIA联系，本文档仅做参考，如果不想自己申请vDWS license与搭建服务器，也可试用腾讯云GN7vw服务器。**

## 申请 License 与准备软件

1. 访问 [NVIDIA Enterprise Account](http://www.nvidia.com/object/nvidia-enterprise-account.html)，注册账号且申请试用 License。具体步骤请参考 [注意事项](https://mp.weixin.qq.com/s/a6U1-GFAM9jXoLfvxO6nGA)。

2. 信息填写完整，将有如下提示，15分钟后在您的邮箱查收确认邮件。 ![](https://main.qcloudimg.com/raw/55059e692e58f365352cfebe1798b7be.png)

  如果您申请的地区是中国，或者使用了公共邮箱进行注册，您可能会收到一封邮件，内容如下:![](https://main.qcloudimg.com/raw/886921716160a2e4a60c1960193a2b31.png)

  测试License账户需要2天的时间由后台进行账号审批，审批通过后，您会收到2封邮件:![](https://main.qcloudimg.com/raw/0df3833a223367126d1d137aa24689fb.png)

  打开邮件“NVIDIA Set Password”，内容如下:

  <img src="https://main.qcloudimg.com/raw/a0ac02109e3fabd68b84a7ded97961b2.png" style="zoom:50%;" />

  点击 SET PASSWORD 按钮，设置初始口令，口令设置完成后，即可点击LOGIN登录您的NVIDIA企业账号。也可从https://nvid.nvidia.com进行登录。![](https://main.qcloudimg.com/raw/aa5e1071aac548635f657b38545d55b0.png)

  点击进入 Licensing Portal，如下图所示:![](https://main.qcloudimg.com/raw/b4e7f6d4013cca2d52d95fe17befe1f0.png)

  vGPU试用的全部资源均可由此Portal 获得，包括vGPU 软件和License Server 软件。

3. 根据下图，选择最新的 NVIDIA Virtual GPU SoftWare 版本，即 GRID 9.3 版本。 ![](https://main.qcloudimg.com/raw/1904f5e1adc80a39714d8cfd9aab877b.png)

4. 创建一台普通 CVM，用作 License 服务器。建议选择 Windows Server 2012 R2 / Windows Server 2016 操作系统。

5. License Server 软件下载:在软件下载右上角点击Additional Software 即可找到License Server 下载项。![](https://main.qcloudimg.com/raw/d9a881fc0d155db19350fe84acdc20c0.png)

  License Server 软件安装：https://docs.nvidia.com/grid/ls/2019.11/grid-license-server-user-guide/index.html

6. 在安装完成后，从LS的管理控制台中可以获得本LS的MAC地址，用于后续步骤的注册。
   注册 License Server MAC地址:![](https://main.qcloudimg.com/raw/d1ef9b9bafd6f872663c02ab3519fae3.png)

   在License Server页面中点击右下角添加按钮，填写表单。注册新的LS。Create完成后，点击该项，在如下页面中选择“添加特性”(ADD FEATURES)。![](https://main.qcloudimg.com/raw/72c20e28d9f35338053eaaece0325a7f.png)

   找到您的试用licenseFeature，填写授予本license服务器的license数量。点击添加按钮。![](https://main.qcloudimg.com/raw/ae187966e2fa2e722d2f5b4b7a07e2b5.png)

7. 以看到授予该License服务器的状态，包括数量和License过期时间。点击Download License File下载用于本LicenseServer的License授权文件。![](https://main.qcloudimg.com/raw/aa4e9bb6767a6771c1e468ba8d7ebbc6.png)

## 配置 License 服务器

1. 下载完成后，要在24小时内通过License的管理控制台(http://license-server:8080/licserver)导入此license文件。具体安装过程请参考 [NVIDIA官方文档](https://docs.nvidia.com/grid/6.0/grid-software-quick-start-guide/index.html#installing-grid-license-server-and-licences)。![](https://main.qcloudimg.com/raw/e79d2f4441c22842a85bbd930bef78e8.png)
2. 可在LS上看到授权的数量:![](https://main.qcloudimg.com/raw/c17eb955e59bd60c623fa403ac7b8e11.png)

## 安装 GRID Driver
1. 购买并创建一台计算型 GPU 实例（GN6/GN6S/GN7/GN8/G10X）。
2. 登录新建的计算型 GPU 实例，安装 GRID Driver，即安装 NVIDIA vGPU for Windows 驱动程序。之后在控制面板中查看驱动是否安装正确。![](https://main.qcloudimg.com/raw/b29c6b952a9f8fa339ea8a791c217de7.png)
3. 安装 VNC/Citrix HDX/PCoIP 等第三方桌面协议，使用户可通过远程桌面连接方式操作 GPU 实例的图形图像处理程序。
4. 使用远程桌面连接方式登录 GPU 实例。
5. 在 GPU 实例中，右键单击桌面或者单击任务栏的右下角图标，打开 NVIDIA Control Panel。
6. 选择 “Manage License”，配置 License 服务器的 IP 地址和端口号，并确保 License 服务器的 IP 地址可以被访问，以及端口号已设置为开放状态。例如，将 License 服务器的 IP 地址配置为公网 IP 或者在同一个 VPC 内的内网地址，那么需要确保配置的 IP 地址可以被用户正常访问，且端口号已设置为开放状态。
    ![](https://main.qcloudimg.com/raw/c9779eee64a02984901fd63e3cc7269b.png)
7. 完成以上配置，NVIDIA GPU 实例便即可运行图形图像处理程序。
    ![](https://main.qcloudimg.com/raw/bc690d2fc2dd6f1828ed9ee1e8e5bf95.png)
