创建文件系统后，请在其他服务器或客户端上按照如下指引进行配置，挂载该文件系统并使用。NFS 文件网关支持 NFS v3.0 及 NFS v4.0 协议。

>!若在 CVM 上使用网关，建议将网关部署在各来访客户端的 VPC 下；如果在不同 VPC 时，请使用 [对等连接](https://cloud.tencent.com/document/product/215/5000) 方法实现网络互通。

您可以在 "文件系统详情" 页面上查看挂载命令。如下图
![](https://mc.qcloudimg.com/static/img/427c850d61745f04d34e0e4f96f0a9b7/image.png)


## 在 Linux 上使用 NFS 文件系统

### 启动 NFS 客户端

挂载前，请确保系统中已经安装了 nfs-utils 或 nfs-common，安装方法如下：

- CentOS: sudo yum install nfs-utils
- Ubuntu 或 Debian: sudo apt-get install nfs-common


### NFS v4.0 挂载

使用下列命令实现 NFS v4.0 挂载 

```
sudo mount -t nfs -o vers=4 <挂载点IP>:/share/nfs/<文件系统名称即bucket名称> <待挂载目标目录>
```
>?
- "<文件系统名称即 bucket 名称>" 与 "<待挂载目标目录>" 之间有一个空格。
- 挂载点 IP：指网关的 IP 地址。 
- 目前默认挂载的是文件系统目录（即文件系统名称）。 若在文件系统中创建子目录后，亦可挂载该子目录。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

#### 示例
- 挂载文件系统根目录：sudo mount -t nfs -o vers=4 10.0.0.1:/share/nfs/bucketname /local/test。
- 挂载文件系统子目录 subfolder：sudo mount -t nfs -o vers=4 10.10.19.12:/share/nfs/bucketname/subfolder /local/test


### NFS v3.0 挂载

使用下列命令实现 NFS v3.0 挂载 
```
sudo mount -t nfs -o vers=3,nolock,proto=tcp <挂载点IP>:/share/nfs/<文件系统名称即 bucket 名称> <待挂载目标目录>
```

>?"
- <文件系统名称即 bucket 名称>" 与 "<待挂载目标目录>" 之间有一个空格。
- 挂载点 IP：指网关的 IP 地址。 
- 目前默认挂载的是文件系统目录（即文件系统名称）。 若在文件系统中创建子目录后，亦可挂载该子目录。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。


#### 示例
- 挂载文件系统根目录：mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/share/nfs/bucketname /local/test
- 挂载文件系统子目录 subfolder：mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/share/nfs/bucketname/subfolder /local/test


### 查看挂载点信息 

挂载完成后，请使用如下命令查看已挂载的文件系统，
`mount -l`

也可以使用如下命令查看该文件系统的容量信息，
`df -h`

### 卸载共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
```
umount <目录名称>
// 例如， umount /local/test
```

## 在 Windows 上使用 NFS 文件系统

### 开启 NFS 服务

挂载前，请确保系统已经启动 NFS 服务。此处以 Windows Server 2012 R2 为示例，启动方法如下：

打开控制面板 -> 程序 -> 打开或关闭 Windows 功能 -> 【服务器角色】页签中勾选 "NFS server" -> 【特性】中勾选 "NFS 客户端"，勾选 NFS 客户端即可开启 Windows NFS 客户端服务.

下图以 Windows Server 2012 R2 为示例。
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

### 验证 NFS 服务是否启动

打开 Windows 下的命令行工具，在面板中敲入如下命令， 若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
```
mount -l
```
![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

### 添加匿名访问用户和用户组

#### 打开注册表
在命令行窗口输入 regedit命令，回车即可打开注册表窗口。
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

#### 添加配置项 AnonymousUid 和 AnonymousGid
在打开的注册表中找到如下路径并选中 

``` HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```

在右边空白处右键单击，弹出 "new", 在菜单中选择 "DWORD(32-bit) Value"。此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的 0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的 0。

![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)

![](https://mc.qcloudimg.com/static/img/80bb0cfbffbed939522459a830df3eac/image.png)

#### 重启使配置生效

关闭注册表并重启 Windows 系统，完成注册表修改。


#### 打开 "映射网络驱动器"
登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网络驱动器"。 
![](https://mc.qcloudimg.com/static/img/5696d66a83d4e9b35196274f89e07dfc/image.png)
![](https://mc.qcloudimg.com/static/img/6eeb1c0838e6aab185ed8b76dc736912/image.png)

#### 输入访问路径
在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录）。
![](https://mc.qcloudimg.com/static/img/c7b07faf43812540d383b7767c52158b/image.png)


#### 验证读写
确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

#### 断开文件系统
要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击【断开】选项，即可断开文件系统的连接。
![](https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png)

