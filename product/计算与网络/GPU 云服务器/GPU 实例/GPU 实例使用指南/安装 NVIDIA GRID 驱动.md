腾讯云提供的**计算型 GPU 实例（GN6/GN6S/GN8/GN10X）**采用的 NVIDIA P4、P40以及 V100 等。Tesla 系列 GPU 可同时支持**通用计算**和**图形图像处理**。
- 安装免费的 Tesla Driver 和 CUDA SDK ，可用作深度学习、科学计算等通用计算场景。
- 安装 GRID Driver 并且配置相关的 License 服务器，可打开 GPU 的 OpenGL 或 DirectX 图形加速能力。

使用 Tesla 系列 GPU 用作图形图像处理，需要向 NVIDIA 或其代理商购买对应的 License。此外，NVIDIA 也提供了 90天试用 License 的申请。
本文将介绍如何申请试用 License，如何配置 License 服务器和安装 GRID driver。

## 申请 License 与准备软件

1. 访问 [NVIDIA Enterprise Account](http://www.nvidia.com/object/nvidia-enterprise-account.html)，注册账号且申请试用 License。具体步骤请参考 [注意事项](https://mp.weixin.qq.com/s/qKmUdAnG9WAg1WLZLLegkA)。
2. 收到 License 申请成功的邮件后，登录 [NVIDIA Enterprise](https://nvid.nvidia.com/dashboard/)，并根据该网站的页面提示，输入 License 激活邮件中的序列号和相关信息。激活成功后，页面提示 **“Product Activation Key was redeemed successfully”** 即表示激活成功。
![](https://main.qcloudimg.com/raw/ad0b82aa0771fbd1f80ce31e3e0bd31f.png)
3. 根据下图，选择最新的 NVIDIA Virtual GPU SoftWare 版本，即 GRID 6.3 版本。
![](https://main.qcloudimg.com/raw/ce7465dd96375c1184ae4587b0e07dfe.png)
4. 分别单击 “NVIDIA vGPU for Windows” 和 “License Manager for Windows”，下载 GRID Driver 和 License Server 安装包。
![](https://main.qcloudimg.com/raw/67308d8f6d08221f4801560b7b51281e.png)
5. 创建一台普通 CVM，用作 License 服务器。建议选择 Windows Server 2012 R2 / Windows Server 2016 操作系统。
6.  获取 License 服务器的 MAC 地址，在 License 管理页面，选择注册 License，输入 MAC 地址，单击 **Create**。
![](	https://main.qcloudimg.com/raw/5de341edfb96450e8fe5ed9527df83c8.png)
7. 	配置 License 中，根据实际需求，在 **Qty to Add** 中输入授权用户的数量，单击 **Map Add-Ons**。
![](	https://main.qcloudimg.com/raw/16172658931dda3273b4d6fe591e1eab.png)
8. 	单击 “Download License File”，下载 License 文件，并将该 License 文件上传到新建的 CVM License 服务器中。
![](	https://main.qcloudimg.com/raw/b8726a29a15383fee194a67bd0bfe28d.png)

## 配置 License 服务器

1. 登录 License 服务器，安装 License Manager for Windows 安装包。具体安装过程请参考 [NVIDIA官方文档](https://docs.nvidia.com/grid/6.0/grid-software-quick-start-guide/index.html#installing-grid-license-server-and-licences)。
2. 使用 IE 浏览器打开 License 的管理页面，选择已下载的 License 文件存放路径，单击 **Upload**，完成配置。
   ![](https://main.qcloudimg.com/raw/0eb8fedc852592d0c204412a3fabc66e.png)

## 安装 GRID Driver
1. 购买并创建一台计算型 GPU 实例（GN6/GN6S/GN8/G10X）。
2. 登录新建的计算型 GPU 实例，安装 GRID Driver，即安装 NVIDIA vGPU for Windows 驱动程序。
3. 安装 VNC/Citrix HDX/PCoIP 等第三方桌面协议，使用户可通过远程桌面连接方式操作 GPU 实例的图形图像处理程序。
4. 使用远程桌面连接方式登录 GPU 实例。
5. 在 GPU 实例中，右键单击桌面或者单击任务栏的右下角图标，打开 NVIDIA Control Panel。
6. 选择 “Manage License”，配置 License 服务器的 IP 地址和端口号，并确保 License 服务器的 IP 地址可以被访问，以及端口号已设置为开放状态。例如，将 License 服务器的 IP 地址配置为公网 IP 或者在同一个 VPC 内的内网地址，那么需要确保配置的 IP 地址可以被用户正常访问，且端口号已设置为开放状态。
  ![](https://main.qcloudimg.com/raw/c9779eee64a02984901fd63e3cc7269b.png)
7. 完成以上配置，NVIDIA GPU 实例便即可运行图形图像处理程序。
  ![](https://main.qcloudimg.com/raw/bc690d2fc2dd6f1828ed9ee1e8e5bf95.png)
