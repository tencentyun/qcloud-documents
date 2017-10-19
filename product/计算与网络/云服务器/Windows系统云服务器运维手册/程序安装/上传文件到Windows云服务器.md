文件上传 Windows 云服务器的常用方法是使用 MSTSC 远程桌面连接 ( Microsoft Terminal Services Client )。本文档介绍本地 Windows 计算机通过远程桌面连接，上传文件至 Windows 云服务器的操作方法。请确保 Windows 云服务器能访问公网。

 1. 在本地计算机，快捷键【Windows + R】，在弹出窗口中输入【mstsc】，单击【确定】打开远程桌面连接对话框，输入云服务器公网 IP 地址，单击【选项】。
![](//mc.qcloudimg.com/static/img/80ab67bbac77365528e1e4ebd8fbb023/image.png)

 2. 在“常规”选项卡中，输入云服务器公网 IP 地址和用户名 Administrator 。
 ![](//mc.qcloudimg.com/static/img/b673c814747e0a3e8c934b5a84dfa89e/image.png)
 
 3. 进入“本地资源”选项卡，单击【详细信息】按钮。
![](//mccdn.qcloud.com/img56b1c57c38874.png)

 4. 在驱动器模块，勾选要上传到 Windows 云服务器的文件所在的本地硬盘，单击确定。
![](//mccdn.qcloud.com/img56b1c582c8471.png)

 5. 本地配置完成后，登录 Windows 云服务器，单击【开始】-【计算机】即可以看到挂载到云服务器上的本地硬盘。
![](//mccdn.qcloud.com/img56b1c58923383.png)

 6. 在云服务器中，双击进入本地硬盘，将需要拷贝的本地文件复制到 Windows 云服务器，即完成文件上传操作。 