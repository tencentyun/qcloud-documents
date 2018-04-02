# 挂载文件系统

请按照以下指引挂载文件系统

## 在 Linux 上使用文件系统

### 在 CVM 上启动 NFS 客户端

挂载前，请确保系统中已经安装了 nfs-utils 或 nfs-common，安装方法如下：

> CentOS: sudo yum install nfs-utils
> Ubuntu 或 Debian: sudo apt-get install nfs-common


### NFS v4.0 挂载

使用下列命令实现 NFS v4.0 挂载，文件系统的挂载路径可以到 "控制台->文件系统详情->挂载点信息" 中获取。

> sudo mount -t nfs -o vers=4 <挂载点IP>:/ <待挂载目标目录>    
> //注意，"<挂载点IP>:/" 与 "<待挂载目标目录>" 之间有一个空格。


*说明*
* 		挂载点IP：指 创建文件系统时，自动的生成的挂载点IP。 
* 	 	目前默认挂载的是文件系统的根目录 "/"。 在文件系统中创建子目录后，可以挂载该子目录。
* 		待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

*示例*
* 		挂载 CFS 根目录：sudo mount -t nfs -o vers=4 10.0.0.1:/ /local/test。
* 	   挂载 CFS 子目录 subfolder：sudo mount -t nfs -o vers=4 10.10.19.12:/subfolder /local/test

![](https://mc.qcloudimg.com/static/img/03550214c0499438e86cfd64b3c377b8/image.png)

### NFS v3.0 挂载

使用下列命令实现 NFS v3.0 挂载，文件系统的挂载路径可以到 "控制台->文件系统详情->挂载点信息" 中获取。

> sudo mount -t nfs -o vers=3,nolock,proto=tcp <挂载点IP>:/<FSID或者子目录> <待挂载目标目录>   
> //注意，"<挂载点IP>:/<FSID或者子目录>" 与 "<待挂载目标目录>" 之间有一个空格。


*说明*

* 		挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。 
* 	 	NFS v3.0 仅支持子目录挂载，缺省文件系统子目录为 FSID 或者 "nfs" 。
* 		待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。


*示例*

* 	 挂载 CFS 子目录 subfolder：mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/z3r6k95r /local/test

* 	 挂载 CFS 子目录 subfolder：mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/nfs /local/test

![](https://mc.qcloudimg.com/static/img/03550214c0499438e86cfd64b3c377b8/image.png)

### 查看挂载点信息 

挂载完成后，请使用如下命令查看已挂载的文件系统，
> mount -l

也可以使用如下命令查看该文件系统的容量信息，
> df -h

### 卸载共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
> umount <目录名称>
> // 列如， umount /local/test



## 在 Windows 上使用文件系统

### 开启 NFS 服务

挂载前，请确保系统已经启动 NFS 服务。此处以 Windows Server 2012 R2 为示例，启动方法如下：

> 打开控制面板 -> 程序 -> 打开或关闭 windows 功能 -> 【服务器角色】页签中勾选 "NFS server" -> 【特性】中勾选 "NFS 客户端"，勾选 NFS 客户端即可开启 windows NFS 客户端服务.

下图以 Windows Server 2012 R2 为示例。
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

### 验证 NFS 服务是否启动

打开 windows 下的命令行工具，在面板中敲入如下命令， 若返回 NFS 相关信息则表示 NFS 客户端正常运行中。

> mount -h

![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

### 添加匿名访问用户和用户组

#### 打开注册表
在命令行窗口输入 regedit命令，回车即可打开注册表窗口。
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

#### 添加配置项 AnonymousUid 和 AnonymousGid
在打开的注册表中找到如下路径并选中 

> HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default

在右边空白处右键点击，弹出 "new", 在菜单中选择 "DWORD(32-bit) Value" 或者 "QWORD(64-bit) Value"（根据您的操作系统位数选择）。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的 0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的0。

![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)

![](https://mc.qcloudimg.com/static/img/80bb0cfbffbed939522459a830df3eac/image.png)

#### 重启使配置生效

关闭注册表并重启 windows 系统，完成注册表修改。


### 挂载文件系统
在 windows 的命令行工具中输入如下命令，挂载文件系统。其中，系统缺省子目录为 "nfs"。

> mount  <挂载点IP>:/<子目录> <共享目录名称>:
> //列如： mount 10.10.0.12:/nfs X:

若使用上述命令挂载，出现文件夹无法重命名的情况，请使用 FSID 进行挂载，挂载命令如下。
> mount <挂载点IP>:/FSID <共享目录名称>:
> //列如： mount 10.10.0.12:/z3r6k95r X:

**注，FSID 可以到 "控制台->文件系统详情->挂载点信息" 中获取。**

![](https://mc.qcloudimg.com/static/img/03550214c0499438e86cfd64b3c377b8/image.png)


### 卸载共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
> umount <目录名称>：
> // 列如， umount X：。 
> // 可以使用 umount -a 卸载所有网络挂载



