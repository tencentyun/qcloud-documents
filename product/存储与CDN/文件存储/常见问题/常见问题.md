### CFS 支持哪些平台？
支持 Linux 、 Unix、 Windows 等客户端。

### 文件存储怎么收费？
仅存储费用。按实际存储量计费（按每小时峰值存储量收取费用）。

### 文件存储支持哪些访问协议？
NFS v3.0/v4.0 及 CIFS/SMB 协议，其中 CIFS/SMB 协议公测中，可以提交申请试用。

其中由于 Windows 及 Linux 3.10 （例如 CentOS 6.\* ) 早期版本内核的操作系统客户端对 NFS 4.0 协议兼容问题，挂载后无法正常使用，此类客户端请使用 NFS 3.0 挂载。

由于协议兼容问题，若使用 Docker 或者 Kubernetes 等客户端挂载 CFS， 推荐使用 NFS v3 协议。（使用 NFS v4 协议可能会出现部分客户端无法正常挂载的问题） 

### 文件存储相关概念有哪些？
文件系统：文件系统是文件存储的实例，将文件系统挂载（ mount ）到 CVM 云服务器后，可以像使用本地文件系统一样使用文件存储。支持目录挂载。

挂载点：挂载点是计算节点访问文件存储的入口，定义了什么类型网络的计算节点、采用怎样的权限来访问文件存储。

### 每个用户可以创建多少个文件系统？
单用户每个地区上限 10 个，有特殊需求可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请扩容。

### 挂载点无法 mount，如何处理？
请参考以下方法进行排查：
- 查看错误消息。
- 检查是否安装了 nfs-utils 、 nfs-common 、cifs-utils 等。
- 本地挂载目录是否存在。
- 挂载点所在 VPC 网络是否和客户端主机所在 VPC 网络一致，地域是否相同。
- CFS 客户端所在的主机是否有做禁止访问外部端口的安全组策略，具体端口请参考 [文件系统端口问题](https://cloud.tencent.com/document/product/582/9551#.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E7.AB.AF.E5.8F.A3.E9.97.AE.E9.A2.98)。

### CFS 无法写入，如何处理？
请参考以下方法进行排查：
- 查看报错信息。
- 检查客户端所在主机网络是否正常，telnet 挂载点端口是否通，具体端口请参考 [文件系统端口问题](https://cloud.tencent.com/document/product/582/9551#.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E7.AB.AF.E5.8F.A3.E9.97.AE.E9.A2.98)。 
- 如果挂载的不是挂载点的根目录，请确认对应挂载的挂载点目录是否存在（这里常见的错误信息是“Stale file handle”，可以通过已经挂载根目录的设备查看其对应子目录是否存在）。

### 文件系统端口问题

文件系统协议 | 开放端口 | 确认网络联通性
------- | ------- | ---------
NFS 3.0 | 111，892，2049 |  telnet 文件系统 IP 2049
NFS 4.0 | 2049 |  telnet 文件系统 IP 2049
CIFS/SMB | 445 |  telnet 文件系统 IP 445 

> **注意：**
> CFS 暂不支持 ping。

### 权限生效问题
NFS 协议的文件系统，支持配置多条规则，并根据优先级生效。其中：
- 当同一个权限组内单条 IP 与网段中包含的 IP 的权限有冲突时，会生效优先级高的规则。若优先级相同则优先生效单条 IP 的权限。

- 若配置了两个有重叠的网段权限不同但优先级相同，则重叠网段的权限会随机生效，请尽量避免重叠网段的配置。 

> **注意：**
CIFS/SMB 文件系统不支持优先级，配置后不生效。

### 如何加速复制本地文件到 CFS？
Linux 可以使用下面 shell 脚本来加速复制本地文件到 CFS。下面代码中，"线程数量" 可以根据需要调整。
```
threads=<线程数量>; src=<源路径/>; dest=<目标路径/>; rsync -av -f"+ */" -f"- *" $src $dest && (cd $src && find . -type f | xargs -n1 -P$threads -I% rsync -av % $dest/% )

<!--例如，threads=24; src=/root/github/swift/; dest=/nfs/; rsync -av -f"+ */" -f"- *" $src $dest && (cd $src && find . -type f | xargs -n1 -P$threads -I% rsync -av % $dest/% )-->
```

### Windows 下修改文件名/目录名异常？
由于客户端对协议支持问题， Windows 客户端使用 NFS 协议挂载文件系统，会出现文件或者目录无法重命名的情况。此类情况，建议 Windows 用户使用 CIFS/SMB 协议来使用 CFS 文件系统。


### 使用 nfs 挂载后，Windows 下没有写入权限，如何处理？
请严格按照操作指引，在注册表中添加 AnonymousUid 和 AnonymousGid ，并重启系统后在重试。
文档：[挂载文件系统-在 Windows 上使用文件系统](https://cloud.tencent.com/document/product/582/9133#.E5.9C.A8-windows-.E4.B8.8A.E4.BD.BF.E7.94.A8.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)

### Windows IIS 无法使用 mapped driver，怎么办？
按照 [挂载文件系统-在 Windows 上使用文件系统](https://cloud.tencent.com/document/product/582/9133#.E5.9C.A8-windows-.E4.B8.8A.E4.BD.BF.E7.94.A8.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F) 中的步骤，配置正确的 NFS 客户端程序并修改注册（添加访问用户）表。
重启客户端后，打开 IIS 配置页面，增加站点并单击【高级设置】。
![](https://mc.qcloudimg.com/static/img/bdd15aa1ca694653b5595442cbc38737/IIS.png)
将高级设置中的 "物理路径" 为 CFS 挂载点。
![](https://main.qcloudimg.com/raw/54375f5bab346a95785bd26575a86fea.png)

### Docker 或 Kubernetes 部分挂载成功、部分失败问题

由于协议兼容问题，若使用 Docker 或者 Kubernetes 等客户端挂载 CFS， 推荐使用 NFS v3 协议。（使用 NFS v4 协议可能会出现部分客户端无法正常挂载的问题）


### 某可用区下 CFS 资源已售罄，如何继续使用？
以广州为例，若已经有广州一区的云服务器，此时需要用到 CFS 文件存储，但广州一区由于资源已售罄无法直接创建文件系统。
**VPC 网络下**
若云服务器在 VPC 的 "广州一区子网" 内， 您可以登录 [VPC 控制台](https://console.cloud.tencent.com/vpc) 为该私有网络创建创建一个可用区为 "广州二区" 的子网。
![](https://main.qcloudimg.com/raw/d25fc9283b76f114a772bebb1b703548.png)
![](https://main.qcloudimg.com/raw/5c0bb3dc41a7759bacf0c096dee4b413.png)

创建子网完成后，回到 CFS 控制台，创建广州二区的资源时选择该 VPC 及刚创建的子网。 此时原来在该 VPC 广州一区子网下的云服务器即可直接挂载 CFS 文件系统。
文件系统使用指引：
- [Linux](https://cloud.tencent.com/document/product/582/11523)
- [Windows](https://cloud.tencent.com/document/product/582/11524)

**基础网络下** 
若云服务器在基础网络内，可创建 VPC 及 广州二区子网并在该网络下创建文件系统。 通过 "基础网络互通" 方法，打通云服务器所在的基础网络及该 VPC 即可实现访问。[查看基础网络互通帮助>>](https://cloud.tencent.com/document/product/215/5002)

### 文件内容更新不同步，如何解决？
#### 问题现象
两台 Linux 云服务器挂载同一个 NFS 文件系统，在云服务器 A 上使用 append 方式写文件，在云服务器 B 上用`tail -f`观察文件内容的变化。在云服务器 A 上写完之后，10 ~ 30 秒的延时后在云服务器 B  上才能看到更新后的内容。但在相同的场景下，如果直接在云服务器 B 上打开文件（例如使用 vi 命令）则可立即看到更新的内容。

#### 问题出现原因
与 NFS 协议 mount 命令的选项以及`tail -f`的实现相关，用户使用此挂载命令：   
```
sudo mount -t nfs -o vers=4 <挂载点IP>:/ <待挂载目标目录>
```
 
当云服务器 B 以 NFS mount 命名挂载的文件系统，默认情况下 kernel 维护了一份文件和目录属性的 metadata 缓存。文件和目录属性包括许可权、大小、和时间戳记等，缓存的目的是减少 NFSPROC_GETATTR 远程过程调用（RPC）的次数。

`tail -f`的实现是通过 sleep+fstat 来观察文件属性（主要是文件大小）的变化，然后读入文件并输出。因此，fstat 的结果决定了 `tail -f`是否能实时输出文件内容。但是，由于文件及目录的 metadata 缓存的存在，fstat 轮询到的并不是实时的文件属性，因此， NFS 服务器端文件虽然已经更新，但`tail -f`却没法知道文件已经发生了变化，因此输出会有延时。

#### 解决办法
使用 mount 命令挂载文件系统时增加 noac 选项可以禁用文件和目录属性的缓存。挂载命令如下：
```
sudo mount -t nfs -o vers=4 noac <挂载点IP>:/ <待挂载目标目录>
sudo mount -t nfs -o vers=3 noac,nolock,proto=tcp <挂载点IP>:/<FSID或者子目录> <待挂载目标目录>
```

### Windows 7-based 或 Windows Server 2008 R2-based 操作系统使用 NFS 协议挂载时报错(0x800704C9)

#### 问题原因
由于这些版本机器缓存了 NFS 初始的端口地址，使用旧的地址与 nlockmgr 通信，详细原因参考 [微软官网说明](https://support.microsoft.com/en-us/help/2761774/0x800704c9-error-when-you-copy-files-to-an-nfs-server-from-a-windows-7)。

#### 解决办法
打开 Windows 的自动更新功能，将系统升级到官方最新版本后即可修复该问题。
