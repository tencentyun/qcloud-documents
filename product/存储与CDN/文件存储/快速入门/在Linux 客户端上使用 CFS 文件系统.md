## 简介
本文为您详细介绍如何在 Linux 客户端上使用 CFS 文件系统。




## 步骤1: 创建文件系统及挂载点

详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132) 文档。


## 步骤2: 连接实例
本部分操作介绍登录 Linux 云服务器的常用方法，不同情况下可以使用不同的登录方式，此处介绍控制台登录，更多登录方式请见 [登录 Linux 实例](/doc/product/213/5436) 。

#### 前提条件
登录到云服务器时，需要使用管理员帐号和对应的密码。
 - 管理员账号：对于 Linux 类型的实例，管理员帐号统一为 root（Ubuntu 系统用户为 ubuntu）。
 - 密码：密码为购买云服务器时设置的密码。

#### 控制台登录云服务器
- 在 [云服务器](https://console.cloud.tencent.com/cvm/index) 列表的操作列，单击【登录】按钮即可通过 VNC 连接至 Linux 云服务器。
- 输入帐号和密码即可登录。

>?该终端为独享，即同一时间只有一个用户可以使用控制台登录。


#### 验证网络通信
挂载前，需要确认客户端与文件系统的网络可达性。您可以通过 telnet 命令验证，具体各个协议及客户端要求开放端口信息如下：

文件系统协议 | 客户端开放端口 | 确认网络联通性
------- | ------- | ---------
NFS 3.0 | 111，892，2049 |  telnet 111或者892或者2049
NFS 4.0 | 2049 |  telnet 2049
CIFS/SMB | 445 |  telnet 445 

>?CFS 暂不支持 ping。


## 步骤3: 挂载文件系统

### 挂载 NFS 文件系统

#### 1. 启动 NFS 客户端
挂载前，请确保系统中已经安装了`nfs-utils`或`nfs-common`，安装方法如下：
- CentOS：
```shell
sudo yum install nfs-utils
```
- Ubuntu 或 Debian：
```shell
sudo apt-get install nfs-common
```

#### 2. 创建待挂载目标目录
使用下列命令创建待挂载目标目录。
```shell
mkdir <待挂载目标目录>
```
示例：
```shell
mkdir /local/
mkdir /local/test
```

#### 3. 挂载文件系统
**NFS v4.0 挂载**
使用下列命令实现 NFS v4.0 挂载。
```shell
sudo mount -t nfs -o vers=4.0 <挂载点IP>:/ <待挂载目录>
```

- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- 目前默认挂载的是文件系统的根目录`/`。 在文件系统中创建子目录后，可以挂载该子目录。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

>!`<挂载点IP>:/`与`<待挂载目标目录>`之间有一个空格。


示例：
- 挂载 CFS 根目录：
```shell
sudo mount -t nfs -o vers=4.0 10.0.24.4:/ /localfolder
```
- 挂载 CFS 子目录：
```shell
sudo mount -t nfs -o vers=4.0 10.0.24.4:/subfolder /localfolder 
```

**NFS v3.0 挂载**
使用下列命令实现 NFS v3.0 挂载。
```shell
sudo mount -t nfs -o vers=3,nolock,proto=tcp <挂载点IP>:/<fsid> <待挂载目录>
```
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- NFS v3.0 仅支持子目录挂载，缺省文件系统子目录为 FSID。
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

>! `<挂载点IP>:/<FSID>` 与 `<待挂载目标目录>`之间有一个空格。

挂载 CFS 子目录示例如下：
```shell
sudo mount -t nfs -o vers=3,nolock,proto=tcp 10.0.24.4:/z3r6k95r /localfolder 
```

#### 4. 查看挂载点信息
挂载完成后，请使用如下命令查看已挂载的文件系统：
```shell
mount -l
```
也可以使用如下命令查看该文件系统的容量信息：
```shell
df -h
```


### 挂载 CIFS/SMB 文件系统
>!CIFS/SMB 协议文件系统公测中，更多信息请参见 [CIFS/SMB公测说明](https://cloud.tencent.com/document/product/582/9553#cifs.2Fsmb-.E5.85.AC.E6.B5.8B.E8.AF.B4.E6.98.8E)。

#### 1. 启动 CIFS 客户端
挂载前，请确保系统中已经安装了`cifs-utils`，安装方法如下：
CentOS：
```shell
sudo yum install cifs-utils.x86_64 –y
```

#### 2. 创建待挂载目标目录
使用下列命令创建待挂载目标目录。
```shell
mkdir <待挂载目标目录>
```
示例：
```shell
mkdir /local/
mkdir /local/test
```

#### 3. 挂载文件系统
使用下列命令实现 CIFS 挂载。
```shell
mount -t cifs -o guest //<挂载点IP>/<FSID> /<待挂载目标目录>
```
- 挂载点IP：指创建文件系统时，自动的生成的挂载点 IP。
- 目前默认挂载使用文件系统的 FSID。 
- 待挂载目标目录： 在当前服务器上，需要挂载的目标目录，需要用户事先创建。

>!`<FSID>`与`/<待挂载目标目录>`之间有一个空格。

示例：
```shell
mount -t cifs -o guest //10.66.168.75/vj3i1135  /local/test
```

#### 4. 查看挂载点信息
挂载完成后，请使用如下命令查看已挂载的文件系统：
```shell
mount -l
```
也可以使用如下命令查看该文件系统的容量信息：
```shell
df -h
```

## 步骤4: 卸载共享目录
当某些情况下需要卸载共享目录，请使用如下命令。其中 "目录名称" 为根目录或者文件系统的完整路径。
```shell
umount <目录名称>
```

示例： 
```shell
umount /local/test
```

>!强烈建议您在重启或关闭客户端前先执行卸载文件系统的操作，以避免引起系统异常。

## 步骤5: 终止资源

>!文件系统删除后，资源不可恢复，建议您删除文件系统之前，先备份资源。

您可以从腾讯云控制台终止文件系统。进入腾讯云 [文件存储控制台](https://console.cloud.tencent.com/cfs)，选中需要终止的文件系统，单击【删除】并【确认】，即可删除文件系统。


