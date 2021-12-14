本文档主要介绍利用容器搭建 NFS 服务来共享 [CBS 云硬盘](https://cloud.tencent.com/document/product/362/2345) 的方法。

NFS 是 Network File System 的简写，即网络文件系统。 通过使用 NFS ，用户和程序可以像访问本地文件一样访问远端系统上的文件。

### 前提条件
如果您还未创建集群，您需要先创建集群。有关如何创建集群的详细信息，参见 [新建集群](https://cloud.tencent.com/document/product/457/9091)。
### 操作步骤
**第一步** ：新建服务
在 [容器服务控制台](https://console.cloud.tencent.com/ccs) 页面，单击 **服务**，在服务列表页单击**新建**。
![](//mc.qcloudimg.com/static/img/9770c91c39779859f75153b6709ff75b/image.gif)
**第二步**：添加数据卷
![](//mc.qcloudimg.com/static/img/ae63d74d7b78d2b74ad2590606c24cd7/image.gif)
>**注意**：
> -  如果提示“**无可用云盘**”，请跳转至 [云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs) 单击**新建**购买云硬盘。
> - 建议打开云硬盘的自动续费功能，防止存储在云硬盘中的数据因欠费造成不必要的损失。

**第三步**：在容器配置中设置挂载点
1. 单击运行容器下的 **显示高级设置**。
2. 设置挂载路径。

>**注意**：
>请务必按照下图所示将云盘挂载到 **/exports** 中。

![Alt text](https://mc.qcloudimg.com/static/img/a54be48bcbe8e24410361b5a2860c43f/image.png)
**第四步**：选择镜像
- **镜像**：在 TencentHub 镜像中选择 ccr.ccs.tencentyun.com/library/nfs-server。
- **版本**：选择 latest。

![Alt text](https://mc.qcloudimg.com/static/img/6238482728fbffc531c9b029bcf78eff/image.png)
**第五步**：设置服务访问方式为 **集群内访问**。
![](//mc.qcloudimg.com/static/img/b33610a809d2eb036b053a84a76203e0/image.gif)

**第六步**：添加端口映射
添加 111 , 2049 , 20048 三个端口映射。
![](//mc.qcloudimg.com/static/img/422f5cb9570b9674450cd8ea4d4a4a10/image.gif)
**第七步**：开启容器特权级功能
![Alt text](https://mc.qcloudimg.com/static/img/1a739ddd2e4933285af85954c4c59aea/image.png)
**第八步**：完成创建容器
服务创建完成后，可以在同一集群内创建一个挂载该 NFS 盘的测试服务。测试服务可以使用任意镜像，只需要在创建测试服务时选择挂载刚创建的 NFS 盘。
在创建测试服务的时候，NFS 盘挂载参数示例如下图：
**类型**：选择 NFS 盘。
**名称**：数据卷的名称。此处以 nnnfs 为例。
**路径**：请填写 **服务 IP:/exports**。
>**注意：**
>服务 IP 为刚创建成功的 NFS 盘服务的 IP。

![](https://mc.qcloudimg.com/static/img/9ce501057b5cad2a2271716725be0606/1212.png)
若测试服务启动成功，则说明 NFS 服务搭建完成。挂载 NFS 盘的细节请参见：[挂载详情](/doc/product/457/9112)。

>** 注意:**
>如果出现挂载 NFS 盘时候挂载失败，且提示事件 `mount: wrong fs type, bad option, bad superblock on ip:path, missing codepage or helper program, or other error (for several filesystems (e.g. nfs, cifs) `，可能是因为您正使用的较老集群里面不含有 NFS 的工具库（新建集群不会出现这种情况）。若出现这种情况，可以登录到集群节点上，按照系统的不同执行以下指令：

>- 对于 Ubuntu 16.04 系统：  
```shell
apt-get install nfs-kernel-server -y
``` 
- 对于 CentOS 7.2 系统：  
```shell
yum install nfs-utils -y
``` 
