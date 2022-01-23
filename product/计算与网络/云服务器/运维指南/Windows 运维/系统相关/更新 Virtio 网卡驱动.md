## 操作场景

腾讯云云服务器 Windows Server 2012 R2、Windows Server 2016和 Windows Server 2019通过安装 Virtio 网卡驱动程序来优化虚拟化硬件的网络性能。腾讯云会持续改进网卡驱动，用于提升性能和解决故障。本文档将指导您如何更新 Virtio 网卡驱动，以及查看驱动版本。

## 前提条件

已登录 Windows 云服务器，详情可参见 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。

## 操作步骤

### 查看系统版本信息

您的系统版本信息可通过以下方法进行查看：
1. 登录云服务器，右键单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/67b4c8b9bac6c8f0c8a60a5ed9c6b5dd.png" style="margin:-3px 0px">，并在弹出菜单中选择**运行**。
2. 在打开的“运行”窗口中，输入 **cmd** 并按 **Enter**。
3. 在打开的 “cmd” 窗口中，执行 `systeminfo` 命令即可查看系统信息。
本文系统版本以 “Windows Server 2016 数据中心版 64位中文版”为例，则获取信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5d7a63d9a3fe8b26507ecc55f353b464.png)

### 更新 Virtio 网卡驱动方法

<dx-alert infotype="notice" title="">
更新过程中网络会闪断，更新前请检查是否会影响业务，更新后需要重启计算机。
</dx-alert>


1. 通过云服务器中的浏览器下载适用于操作系统版本的 VirtIO 网卡驱动安装文件。 
VirtIO 网卡驱动下载地址如下，请对应实际网络环境进行下载：
 -  **公网下载地址**：`http://mirrors.tencent.com/install/windows/virtio_64_1.0.9.exe`
 -  **内网下载地址**：`http://mirrors.tencentyun.com/install/windows/virtio_64_1.0.9.exe`
2. 下载完成后，双击启动安装程序，单击 **Next**。
3. 保持默认勾选 “VirtioDrivers”，单击 **Next**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e77875fd9fdac5364188bc989bba0c05.png)
4. 选择安装位置，单击 **Install**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d38b32cba76dbb2cdfad95bae3de1f58.png)
5. 在弹出的安全提示中，勾选“始终信任来自 “Tencent Technology（Shenzhen）Company Limited” 的软件”，单击**安装**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/05d55414d0b8019fdaeb291084908041.png)
安装过程中，如果出现如下的弹出框，请选择**始终安装此驱动程序软件**。
![](https://main.qcloudimg.com/raw/fff5cd1b24bf3951742cc5a356c8d078.png)      
6. 根据提示，重新启动计算机，即可完成更新。


### 查看驱动版本

1. 右键单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/67b4c8b9bac6c8f0c8a60a5ed9c6b5dd.png" style="margin:-3px 0px">，并在弹出菜单中选择**运行**。
2. 在打开的“运行”窗口中，输入 **ncpa.cpl**，并按 **Enter**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8df948aa715e232924f2a943ea50e059.png)
2. 在打开的“网络连接”窗口中，右键单击“以太网”图标，选择**属性**。
3. 在弹出的“以太网 属性”窗口中，单击**配置**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f7a819e642167b4c87a911fe1b670ea0.png)
4. 在 “Tencent VirtIO Ethernet Adapter 属性”窗口中，选择**驱动程序**页签，即可查看当前驱动程序版本。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3ed38facb59230b4fcea0bac54c37b1d.png)

