## 操作场景
文件存储（Cloud File Storage，CFS）提供了可扩展的共享文件存储服务，可与腾讯云云服务器 、容器、批量计算、轻量应用服务器等服务搭配使用。CFS 提供了标准的 NFS 及 CIFS/SMB 文件系统访问协议，可为计算服务提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。如需了解更多信息，请参见 [文件存储](https://cloud.tencent.com/document/product/582/9127) 产品文档。

您可通过挂载 CFS 文件系统实现轻量应用服务器实例存储容量扩展，或数据源共享等功能。本文介绍如何通过内网互联功能，给轻量应用服务器实例挂载 CFS 文件系统。


## 操作步骤

### 创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击【新建】。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
本文中“镜像”以选择“系统镜像 CentOS 7.6”为例，您可按需进行选择。其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。

### 创建文件系统
1. 登录文件存储控制台，选择左侧导航栏中的【[文件系统](https://console.cloud.tencent.com/cfs/fs)】。
2. 在“文件系统”页面上方，选择文件系统所在地域，并单击【新建】。
3. 进入“新建文件系统”页面：
 1. 在”选择文件系统类型“中，选择”通用标准型“，并单击【下一步：详细设置】。
 2. 在“详细设置”中，参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/7ac9f718737d57e49579790c663b3bae.png)
   主要配置信息如下：
    - **文件系统名称**：自定义设置。
    - **地域**及**可用区**：您可按需进行设置。本文选择与轻量应用服务器同一地域。
    - **文件协议**：若轻量应用服务器实例为 Linux 操作系统，则选择 “NFS”。若轻量应用服务器实例为 Windows 操作系统，则选择 “SMB”。
    - **选择网络**：选择文件系统所在私有网络 VPC。如需新建 VPC，请参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。
   如需了解其他配置项及更多信息，请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)。
 4. 单击【下一步：资源包】。
 3. 在“资源包”中单击【立即购买】，即可成功创建文件系统。

### 使用内网互联
1. 轻量应用服务器实例关联云联网
参考 [申请云联网关联](https://cloud.tencent.com/document/product/1207/56847#association)，将轻量应用服务实例关联云联网。
2. 文件系统 VPC 实例关联云联网
参考 [关联网络实例](https://cloud.tencent.com/document/product/877/18747)，将文件系统的 VPC 实例关联至云联网。

### 挂载文件系统
1. 参考 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642) 登录实例。
2. 执行以下命令，安装 `nfs-utils`。
```
sudo yum install nfs-utils
```
3. 执行以下命令，待挂载目标目录。
```
mkdir <待挂载目标目录>
```
例如，执行以下命令，创建目录 `local`。
```
mkdir /local/
```
4. 获取挂载命令：
 1. 在 “[文件系统](https://console.cloud.tencent.com/cfs/fs)” 页面中，单击文件系统名。
 2. 进入文件系统详情页，选择【挂载点信息】页签，即可从 “Linux下挂载” 获取命令。如下图所示：
![](https://main.qcloudimg.com/raw/6bd9984c4bf732dc3a7973afa9bbf50e.png)
5. 执行获取的挂载命令。本文以使用 NFS v4.0 挂载，且挂载 CFS 根目录为例，执行以下命令。
```
sudo mount -t nfs -o vers=4.0,noresvport xx.xx.x.xx:/ /local
``` 
如需了解 Linxu 操作系统挂载文件系统更多信息，请参见 [挂载 NFS 文件系统](https://cloud.tencent.com/document/product/582/11523#.E6.8C.82.E8.BD.BD-nfs-.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)。

### 查看挂载点信息
挂载完成后，可使用以下命令查看该文件系统的容量信息。
```
df -h
```
返回类似如下信息，则说明已成功挂载 CFS 文件系统。
![](https://main.qcloudimg.com/raw/e595bc1c0f92ab0fe9f2aebecabd3552.png)

## 相关操作

### 配置自动挂载文件系统
您还可参考 [自动挂载文件系统](https://cloud.tencent.com/document/product/582/13652) 进行配置，使轻量应用服务器重启后仍可自动挂载 CFS 文件系统。


## 相关文档
- [内网互联](https://cloud.tencent.com/document/product/1207/56847)
- [云联网](https://cloud.tencent.com/document/product/877/18675)
- [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)
- [在 Linux 客户端上使用 CFS 文件系统](https://cloud.tencent.com/document/product/582/11523)
