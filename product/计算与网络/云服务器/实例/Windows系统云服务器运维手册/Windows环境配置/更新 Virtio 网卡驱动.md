腾讯云云服务器Window Server 2008 R2 企业版 SP1 和 Windows Server 2012 R2安装了 VirtIO 网卡驱动程序来优化虚拟化硬件的网络性能。腾讯云会持续改进网卡驱动，用于提升性能和解决故障。用户可以下载使用最新版本的网卡驱动。

> - 用户可以右键点击【计算机】-【属性】，在【查看有关计算机的基本信息】里可以查看系统的版本信息
> ![](//mccdn.qcloud.com/static/img/5cd57bbbd48668cca57efdaba7e5ae84/image.png)
> - 升级过程中网络会闪断，升级前请检查是否会影响业务， 升级后需要重启计算机。

腾讯云用户可通过以下内网地址下载适用于Window Server 2008 R2 和 Windows Server 2012 R2的 VirtIO 网卡驱动安装文件。内网下载地址：http://mirrors.tencentyun.com/install/windows/virtio_64_10003.msi

双击启动安装程序，选择【典型】安装模式，点击【安装】按钮：
![](//mccdn.qcloud.com/static/img/0d596e42ae299cfa295a0493dc68bc4d/image.png)

安装过程中出现安全提示，勾选【始终信任来自“Tencent Technology（Shenzhen）Company Limited”的软件】，点击【安装】按钮：
![](//mccdn.qcloud.com/static/img/f2f5aea8ed1aa8814e69fa9142254537/image.png)

如果出现如下的弹出框，选择【始终安装此驱动程序软件】：
![](//mccdn.qcloud.com/static/img/ca48d6e37f5deb2f4575bc608f5c49d6/image.png)

安装完成后，系统会提示重新启动计算机生效。此时重启计算机即可。