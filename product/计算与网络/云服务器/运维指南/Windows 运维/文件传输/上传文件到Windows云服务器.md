## 操作场景

文件上传 Windows 云服务器的常用方法是使用 MSTSC 远程桌面连接（Microsoft Terminal Services Client）。本文档指导您使用本地 Windows 计算机通过远程桌面连接，将文件上传至 Windows 云服务器。

## 前提条件

请确保 Windows 云服务器可以访问公网。

## 操作步骤
>? 以下操作步骤以 Windows 7 操作系统的本地计算机为例，根据操作系统的不同，详细操作步骤略有区别。
>
### 获取公网 IP
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，在实例列表页面记录需上传文件云服务器的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/ea509a3a924e9cafc54af146acaa03d7.png)

### 上传文件
1. 在本地计算机，使用快捷键【Windows + R】，打开【运行】窗口。
2. 在弹出的【运行】窗口中，输入 **mstsc**，单击【确定】，打开【远程桌面连接】对话框。
3. 在【远程桌面连接】对话框中，输入云服务器公网 IP 地址，单击【选项】。如下图所示：
![](https://main.qcloudimg.com/raw/5b2a435c715317cf299bfbc07a09b802.png)
4. 在【常规】页签中，输入云服务器公网 IP 地址和用户名 Administrator。如下图所示：
![](https://main.qcloudimg.com/raw/09c2f84a3fa140c07b5a22a14b1f20cc.png)
5. 选择【本地资源】页签，单击【详细信息】。如下图所示：
![](https://main.qcloudimg.com/raw/0b33b2b83914f1a158bc174a2644d674.png)
6. 在弹出的【本地设备和资源】窗口中，选择【驱动器】模块，勾选所需上传到 Windows 云服务器文件所在的本地硬盘，单击【确定】。如下图所示：
例如，需上传到 Windows 云服务器的文件位于 E 盘，则需勾选 E 盘。
![](https://main.qcloudimg.com/raw/ed51f0181d2c964ff96323a9ff957203.png)
7. 本地配置完成后，单击【连接】，远程登录 Windows 云服务器。
8. 在 Windows 云服务器中，选择 <img src="https://main.qcloudimg.com/raw/ef8fb18be7880d8b48ce402b973f22dc.png" style="margin:-3px 0px">，在打开的窗口中单击【此电脑】，即可以看到挂载到云服务器上的本地硬盘。如下图所示：
>?该步骤 Windows 云服务器操作系统以 Windows Server 2016 为例，根据操作系统的不同，详细操作步骤略有区别。
>
![](https://main.qcloudimg.com/raw/bde1ac63a3a49e773d25e5df850897dd.png)
9. 双击打开已挂载的本地硬盘，并将需要拷贝的本地文件复制到 Windows 云服务器的其他硬盘中，即完成文件上传操作。
例如，将本地硬盘（F）中的 A 文件复制到 Windows 云服务器的 C: 盘中。

### 下载文件
如需将 Windows 云服务器中的文件下载至本地计算机，也可以参照上传文件的操作，将所需文件从 Windows 云服务器中复制到挂载的本地硬盘中，即可完成文件下载操作。


