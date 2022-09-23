## 简介

创建文件系统后，请在客户端上按照如下指引进行配置，挂载该文件系统并使用。NFS 文件网关支持 NFS v3.0 及 NFS v4.0 协议。

您可以在 "文件系统详情" 页面上查看挂载命令，如下图所示：
![](https://main.qcloudimg.com/raw/aa3a549b488ec20ed0c1e593a0c97d69.png)


## 在 Linux 上使用 NFS 文件系统

### 启动 NFS 客户端

挂载前，请确保系统中已经安装了 nfs-utils 或 nfs-common，安装方法如下：

- CentOS：
```plaintext
sudo yum install nfs-utils
```
- Ubuntu 或 Debian：
```plaintext
sudo apt-get install nfs-common
```

### NFS v4.0 挂载

使用下列命令实现 NFS v4.0 挂载 

```plaintext
sudo mount -t nfs -o vers=4 <挂载点IP>:/share/nfs/<文件系统名称即bucket名称> <待挂载目标目录>
```
>?
> - "<文件系统名称即 bucket 名称>" 与 "<待挂载目标目录>" 之间有一个空格。
> - 挂载点 IP：指网关的 IP 地址。 
> - 目前默认挂载的是文件系统目录（即文件系统名称）。 若在文件系统中创建子目录后，亦可挂载该子目录。
> - 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。
> 

#### 示例
- 挂载文件系统根目录：
```plaintext
sudo mount -t nfs -o vers=4 10.0.0.1:/share/nfs/bucketname /local/test
```
- 挂载文件系统子目录 subfolder：
```plaintext
sudo mount -t nfs -o vers=4 10.10.19.12:/share/nfs/bucketname/subfolder /local/test
```


### NFS v3.0 挂载

使用下列命令实现 NFS v3.0 挂载 
```plaintext
sudo mount -t nfs -o vers=3,nolock,proto=tcp <挂载点IP>:/share/nfs/<文件系统名称即 bucket 名称> <待挂载目标目录>
```

>?
> - "<文件系统名称即 bucket 名称>" 与 "<待挂载目标目录>" 之间有一个空格。
> - 挂载点 IP：指网关的 IP 地址。 
> - 目前默认挂载的是文件系统目录（即文件系统名称）。 若在文件系统中创建子目录后，亦可挂载该子目录。
> - 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。
> 


#### 示例
- 挂载文件系统根目录：
```plaintext
mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/share/nfs/bucketname /local/test
```
- 挂载文件系统子目录 subfolder：
```plaintext
mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/share/nfs/bucketname/subfolder /local/test
```

### 查看挂载点信息 

挂载完成后，请使用如下命令查看已挂载的文件系统：
```plaintext
mount -l
```

也可以使用如下命令查看该文件系统的容量信息：
```plaintext
df -h
```


### 卸载共享目录 

当某些情况下需要卸载共享目录，请使用如下命令。其中“目录名称”为根目录或者文件系统的完整路径。
```plaintext
umount <目录名称>
// 例如， umount /local/test
```

## 在 Windows 上使用 NFS 文件系统

### 开启 NFS 服务

挂载前，请确保系统已经启动 NFS 服务。此处以 Windows Server 2012 R2 为示例，启动方法如下：

1. 打开**控制面板 > 程序和功能 > 启用或关闭 Windows 功能**。
2. 系统将打开添加角色和功能向导页面，在**开始之前**步骤中，单击**下一步 > 基于角色或基于功能的安装 > 下一步 > 从服务器池中选择服务器**，进入**服务角色**配置项。
3. **服务器角色**中，展开**文件和存储服务 > 文件和 iSCSI 服务**，勾选 **NFS 服务器**。
![](https://main.qcloudimg.com/raw/cab72273d76a83e7361f44369a514515.jpg)
4. 在弹出的小窗口中，单击**添加功能**。
5. 单击**下一步**，在**功能**配置项中勾选 **NFS 客户端**，勾选 NFS 客户端即可开启 Windows NFS 客户端服务。
![](https://main.qcloudimg.com/raw/b0b33b3424b7d82f81ab24bfaadbf8d5.jpg)
6. 单击**下一步 > 安装**，等待系统安装 NFS 服务和客户端。
7. 安装完毕，单击**关闭**关闭窗口即可。



### 验证 NFS 服务是否启动

打开 Windows 下的命令行工具，在面板中敲入如下命令， 若返回 NFS 相关信息则表示 NFS 客户端正常运行中。
```plaintext
mount -l
```
![](https://main.qcloudimg.com/raw/eabca9ef64cdd23b6cbefc8b20d6ae6e.jpg)


### 添加匿名访问用户和用户组

#### 打开注册表
在命令行窗口中输入 regedit 命令，回车即可打开注册表窗口。

![](https://main.qcloudimg.com/raw/ece1a8b2acc23c2abb3c6068096d5abf.jpg)

#### 添加配置项 AnonymousUid 和 AnonymousGid
1. 在打开的注册表中找到如下路径并选中 
```plaintext
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```
2. 在右边空白处右键单击，弹出 "项"，在菜单中选择 "DWORD(32 位) 值"。
![](https://main.qcloudimg.com/raw/46c8b7898757cb82e228db0df7650c99.jpg)
3. 此时，在列表中会出现一条新的记录，把名称栏修改为 AnonymousUid 即可，数据值采用默认的0。使用同样方法继续添加一条名称为 AnonymousGid 的记录，数据也采用默认的0。
![](https://main.qcloudimg.com/raw/e1d244553bbd3a8d0b0084fe832278f3.jpg)



#### 重启使配置生效

关闭注册表并重启 Windows 系统，完成注册表修改。


#### 打开映射网络驱动器
1. 登录到需要挂载文件系统的 Windows 上。
2. 打开“我的电脑”，在菜单栏中单击**映射网络驱动器**。 
![](https://main.qcloudimg.com/raw/2500de31739754cb03f97b0d1f771c90.jpg)


#### 输入访问路径
在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 NFS 文件系统中看到的挂载目录）。
![](https://mc.qcloudimg.com/static/img/c7b07faf43812540d383b7767c52158b/image.png)


#### 验证读写
确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

>! 中文 Windows 系统的默认编码为 GBK，而网关依托于 Linux 环境，中文编码为 UTF-8，如果挂载后出现异常，请先确认是否存在中文文件，如果需要使用中文文件，需要将 Windows 系统的默认编码改为 UTF-8。

#### 断开文件系统
要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击**断开**选项，即可断开文件系统的连接。
![](https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png)


