## 操作场景

文件上传 Windows 云服务器的常用方法是使用 MSTSC 远程桌面连接（Microsoft Terminal Services Client）。本文档指导您使用本地 Windows 计算机通过远程桌面连接，将文件上传至 Windows 云服务器。

## 前提条件

请确保 Windows 云服务器可以访问公网。

## 操作步骤
>? 以下操作步骤以 Windows 7 操作系统的本地计算机为例，根据操作系统的不同，详细操作步骤略有区别。
>
1. 在本地计算机，使用快捷键【Windows + R】，打开【运行】窗口。
2. 在弹出的【运行】窗口中，输入 **mstsc**，单击【确定】，打开【远程桌面连接】对话框。
3. 在【远程桌面连接】对话框中，输入云服务器公网 IP 地址，单击【选项】。如下图所示：
![](//mc.qcloudimg.com/static/img/80ab67bbac77365528e1e4ebd8fbb023/image.png)
2. 在【常规】页签中，输入云服务器公网 IP 地址和用户名 Administrator。如下图所示：
![](//mc.qcloudimg.com/static/img/b673c814747e0a3e8c934b5a84dfa89e/image.png)
3. 选择【本地资源】页签，单击【详细信息】。如下图所示：
![](//mccdn.qcloud.com/img56b1c57c38874.png)
4. 在弹出的【本地设备和资源】窗口中，选择【驱动器】模块，勾选需要上传到 Windows 云服务器的文件所在的本地硬盘，单击【确定】。如下图所示：
![](//mccdn.qcloud.com/img56b1c582c8471.png)
5. 本地配置完成后，单击【连接】，远程登录 Windows 云服务器。
6. 在 Windows 云服务器中，单击【开始】>【计算机】，即可以看到挂载到云服务器上的本地硬盘。如下图所示：
![](https://main.qcloudimg.com/raw/8e59dbca8d7cc7293669bf7adaf8985a.png)
6. 双击打开本地硬盘，将需要拷贝的本地文件复制到 Windows 云服务器中，即完成文件上传操作。 
