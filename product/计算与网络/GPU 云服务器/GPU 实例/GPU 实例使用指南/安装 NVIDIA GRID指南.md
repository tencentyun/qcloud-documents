腾讯云提供的**计算型GPU实例（GN6/GN6S/GN8/GN10/GN10S/GN10X）**采用的NVIDIA P4、P40以及V100 等Tesla系列GPU可同时支持**通用计算**和**图形图像处理**,
- 安装免费的Tesla Driver和CUDA SDK后可以用作深度学习、科学计算等通用计算场景；
- 安装GRID Driver并且配置相关的License服务器，可打开GPU的OpenGL或DirectX图形加速能力；

使用Tesla系列GPU用作图形图像处理，需要向NVIDIA或其代理商购买对应的License；此外NVIDIA也提供了90天试用License的申请。

本文将介绍如何申请试用License，如何配置License服务器和安装GRID driver。

## 申请NVIDIA GRID License
1. 访问[NVIDIA Enterprise Account](http://www.nvidia.com/object/nvidia-enterprise-account.html) 注册账号且申请试用License，具体步骤可参考[注意事项](https://mp.weixin.qq.com/s/qKmUdAnG9WAg1WLZLLegkA)

2. 收到License申请成功的邮件后，登陆[NVIDIA Enterprise](https://nvid.nvidia.com/dashboard/)；在该网站下面的页面里激活邮件里收到的序列号。激活过程中需要填入相关信息，激活成功后会提示**“Product Activation Key was redeemed successfully”**
![](https://main.qcloudimg.com/raw/ad0b82aa0771fbd1f80ce31e3e0bd31f.png)

3. 按下图选择最新版本的GRID 6.3
![](https://main.qcloudimg.com/raw/ce7465dd96375c1184ae4587b0e07dfe.png)

	然后下载License Server安装程序（License Manager for Windows）和GRID Driver(NVIDIA vGPU for Windows)
![](https://main.qcloudimg.com/raw/67308d8f6d08221f4801560b7b51281e.png)

4. 创建一台普通CVM用作License服务器，操作系统建议选择Windows Server 2012 R2/Windows Server 2016

5.  获取License服务器的MAC地址后，回到License管理页面注册License，输入MAC地址，点击**Create**
	![](	https://main.qcloudimg.com/raw/5de341edfb96450e8fe5ed9527df83c8.png)
	
	配置License同时能授权用户的数量，在**Qty to Add**中填入数字，然后点击**Map Add-Ons**
	![](	https://main.qcloudimg.com/raw/16172658931dda3273b4d6fe591e1eab.png)
	
	下载License文件， 上传到创建的CVM License服务器上
	![](	https://main.qcloudimg.com/raw/b8726a29a15383fee194a67bd0bfe28d.png)

## 配置License服务器
1. 登陆到License服务器上，然后安装部署下载的License Manager for Windows，详细参考[NVIDIA官方文档](https://docs.nvidia.com/grid/6.0/grid-software-quick-start-guide/index.html#installing-grid-license-server-and-licences)

2. 用IE浏览器打开License的管理页面，上传之前下载的License文件；至此License服务器已配置完成。
   ![](https://main.qcloudimg.com/raw/0eb8fedc852592d0c204412a3fabc66e.png)

## 安装GRID Driver
1. 购买创建一台计算型GPU实例（GN6/GN6S/GN8/GN10/GN10/G10X）, 登陆机器，安装之前下载好的GRID Driver(NVIDIA vGPU for Windows)

2. 操作远程GPU实例的图形图像处理程序，需要安装VNC/Citrix HDX/PCoIP等第三方桌面协议

3. 通过远程桌面协议登陆GPU实例，打开NVIDIA Control Panel （鼠标右击桌面或点击桌面右下角图标），然后配置License服务器的地址；确保License服务器的地址是可以被访问的，例如是公网IP或者在同一个VPC内的内网地址；确保License服务器配置的端口是开放的
  ![](https://main.qcloudimg.com/raw/c9779eee64a02984901fd63e3cc7269b.png)
	
4. 至此NVIDIA GPU实例便可运行图形图像处理程序了
  ![](https://main.qcloudimg.com/raw/bc690d2fc2dd6f1828ed9ee1e8e5bf95.png)
