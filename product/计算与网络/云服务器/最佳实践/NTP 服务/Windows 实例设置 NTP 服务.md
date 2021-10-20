## 操作场景

Windows 时间服务（Windows Time service，W32Time）用于本地系统与时钟源服务器之间的时间同步，使用网络时间协议（NTP）来同步网络上的计算机时钟。本文档以 Windows Server 2012 操作系统云服务器为例，介绍如何开启 NTP 服务和修改时钟源服务器地址。

## 操作步骤

1. 登录 Windows 云服务器。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;"></img> > **管理工具** > **服务**，打开服务窗口。
3. 在“服务”窗口中，双击打开 **Windows Time**。如下图所示：
![](https://main.qcloudimg.com/raw/f45a470caa8f09f5a12c4639db1a1ea6.png)
4. 在打开的 “Windows Time 的属性(本地计算机)” 窗口中，将“启动类型”设置为**自动**，将“服务状态”设置为**启动**，并单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/53af4acb5d03dbf623be5b3a44a412b3.png)
5. 在操作系统界面的任务栏中，单击右下角的时间 > **更改日期和时间设置**。如下图所示：
![](https://main.qcloudimg.com/raw/ff260db81f9db83d0358629b319990d6.png)
6. 在弹出的“日期和时间”窗口中，选择 **Internet 时间**页签，单击**更改设置**。如下图所示：
![](https://main.qcloudimg.com/raw/0e70f38a5b2a43c3cbdc093b79d96f8a.png)
7. 在弹出的 “Internet 时间设置” 窗口中，将“服务器”设置为目标时钟源服务器域名或者 IP 地址，单击**确定**，完成设置。如下图所示：
![](https://main.qcloudimg.com/raw/d27d42f7bb62118896f675d137d9f100.png)
