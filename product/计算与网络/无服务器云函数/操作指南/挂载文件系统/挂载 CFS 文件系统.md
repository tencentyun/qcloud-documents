## 操作场景

[腾讯云 CFS 文件存储](https://cloud.tencent.com/product/cfs) 提供可扩展的共享文件存储服务，可与腾讯云服务器、容器服务或者批量处理等服务搭配使用。CFS 符合标准的 NFS 文件系统访问协议，为多个计算节点提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。

CFS 采用按量计费的计费模式，您只需为实际使用的存储空间付费，以小时为计费周期，按单位小时内实际使用存储空间的最大值（峰值）计算。

腾讯云 SCF 现在可以与 CSF 无缝集成。这使您的函数可以像访问本地文件系统一样编写访问存储在其中一个 CFS 文件系统上的文件。 您所要做的是配置 CFS，其中包括 CFS 文件系统，远端目录，本地目录，用户ID，用户组ID。 配置成功后，该函数就可以像访问本地文件系统一样访问指定的 CSF 文件系统。

## 使用 CFS 的好处
函数的执行空间不受大小限制。
多个函数可以共用一个 CFS，实现文件共享。

## 申请 CFS 文件存储资源
若您还未拥有文件系统，则请按照 [创建 CFS 文件系统](https://cloud.tencent.com/document/product/582/9132) 指引创建一个文件系统，创建时请注意 VPC 网络的选择需要与您的函数在相同的 VPC 下，以保障网络的互通。

## 配置挂载 CFS 文件系统
您需要先[创建 VPC 私有网络](https://cloud.tencent.com/document/product/215/30716)功能，才能配置 CFS， 这是因为 CFS 目前只能在用户私有的 VPC 环境才能添加挂载点，因此用户必须确保配置正确的 VPC 才能访问指定的 CFS 文件系统。

## 文件系统的 UserID and GroupID：
这两个值等同于文件系统中的用户和组的概念，SCF 会使用 UserID 10000 和 GroupID 10000 来操作您的 CFS 文件系统，请根据需求设置文件的拥有者和相应的组权限，确保您的 CFS 配置相应的权限，详见 [CFS 的权限设置](https://cloud.tencent.com/document/product/582/10951)。

## 远程目录：
远程目录描述了云函数需要访问的 CFS 文件系统的远端目录，由文件系统和远端目录两部分组成。

## 本地目录：
本地目录是指本地文件系统的挂载点。我们允许您使用 “mnt” 目录的子目录挂载 CFS 文件系统。

## 配置挂载 CFS 文件系统
1. 创建 VPC
    请参见 [网络配置](https://cloud.tencent.com/document/product/583/19702)
2. 创建 CFS
    请参见 [创建 CFS 文件系统](https://cloud.tencent.com/document/product/582/9132)
3. 配置文件系统
    勾选启用私有网络，并选择您 CFS 文件系统所在的 VPC 和子网。
    ![](https://main.qcloudimg.com/raw/f4d6ef21dcce9fd843a00eae47f5b5c5.png)
    填写本地目录和远程目录，并且选中您 CFS 文件系统的文件系统 ID 和挂载点 ID。
    ![](https://main.qcloudimg.com/raw/ccb6006ef802345c290e3f072c77f1fb.png)
4. 代码使用案例
    ![](https://main.qcloudimg.com/raw/cd399a711c79e0e791a13d72c692d104.png)
