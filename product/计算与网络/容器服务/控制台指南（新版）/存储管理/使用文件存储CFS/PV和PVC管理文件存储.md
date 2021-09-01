## 操作场景
腾讯云容器服务支持通过创建 PV/PVC，并在创建工作负载添加数据卷时使用已有 PVC，实现通过 PV 和 PVC 管理文件系统。

>!不同地域所支持的文件存储能力有一定差异，请按需选择。详情请参见[ 文件存储类型和性能规格](https://cloud.tencent.com/document/product/582/38112)。


## 准备工作
### 安装文件存储扩展组件
>? 若您的集群已安装 CFS-CSI 的扩展组件，则请跳过此步骤。
>
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 单击左侧导航栏中的**集群**，进入**集群管理**页面。
3. 选择需新建组件的集群 ID，进入**集群详情**页面。
4. 在“集群详情页”，选择**组件管理** > **新建**，进入**新建组件**页面。
5. 在“新建组件”页面，勾选**CFS（腾讯云文件存储）**并单击**完成**即可。

### 通过控制台创建 StorageClass[](id:createStorageClass)
由于静态创建文件存储类型的 PV 时，需要绑定同类型可用 StorageClass，请参考 [通过控制台创建 StorageClass](https://cloud.tencent.com/document/product/457/44235#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95) 完成创建。

### 创建文件存储[](id:createCFS)
1. 登录[ 文件存储控制台](https://console.cloud.tencent.com/cfs/fs?rid=1)，进入“文件系统”页面。
2. 单击**新建**，在弹出的“创建文件系统”窗口中，参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/27e35d96a2978626231f2f81743451e7.png)
	- **名称**：自定义，本文以 `cfs-test` 为例。
	- **地域**：选择所需要创建文件系统的地域，需确保与集群在同一地域。
	- **可用区**：选择所需要创建文件系统的可用区。
	- **存储类型**：提供**标准存储**和**性能存储**两种类型，不同可用区支持类型有一定差异，详情请参见[ 可用地域](https://cloud.tencent.com/document/product/582/43623)。
	- **文件服务协议**：选择文件系统的协议类型，**NFS**或**CIFS/SMB**。
		- NFS 协议：更适合于 Linux/Unix 客户端。
		- CIFS/SMB 协议：更适合于 Windows 客户端。
	- **客户端类型**：选择需要访问文件系统的客户端类型，云服务器（含容器、批量计算）或黑石服务器。 由于云服务器和黑石主机分别属于不同的网络，系统会根据您的客户端类型分配该文件系统到指定网络中。
	- **网络类型**：选择**私有网络**，以实现私有网络下云服务器对文件系统的共享。
	- **选择网络**：需确保与使用该文件系统的集群处于同一私有网络下。
	- **权限组**：每个文件系统必须绑定一个权限组，权限组规定了一组可来访白名单及读、写操作权限。
	- **标签**：
		- 若已拥有标签，可在此处为新建文件系统添加。
		- 若未拥有标签，则可前往 [标签控制台](https://console.cloud.tencent.com/tag/taglist) 创建所需要的标签，再为文件系统绑定标签。或可在文件系统创建完成后，再为文件系统添加标签。
3. 单击**新建**，等待创建成功即可。



### 获取文件系统子目录[](id:getPath)
1. 在“文件系统”页面，单击需获取子目标路径的文件系统 ID，进入该文件系统详情页。
2. 选择**挂载点信息**页签，从 “Linux下挂载” 获取该文件系统子目录路径 `/subfolder`。如下图所示：
![](https://main.qcloudimg.com/raw/78949f471b9b57b2ee10fc3652bad017.png)
	-  `localfolder`：指用户本地自己创建的目录。
	-  `subfolder`：指用户在文件存储的文件系统里创建的子目录，则该文件系统子目录路径即为 `/subfolder`。



## 操作步骤


### 静态创建 PV[](id:pv)
>? 静态创建 PV 适用于已有存量的文件存储，并在集群内使用的场景。
>
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建 PV 的集群 ID，进入待创建 PV 的集群管理页面。
3. 选择左侧菜单栏中的**存储** > **PersistentVolume**，进入 “PersistentVolume” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/d3d74b0bb94b8621904c3d8403937b3d.png)
4. 单击**新建**进入“新建PersistentVolume” 页面，参考以下信息设置 PV 参数。如下图所示：
![](https://main.qcloudimg.com/raw/3577b53114dc37ad63a4a2911a42e406.png)
	- **来源设置**：选择**静态创建**。
	- **名称**：自定义，本文以 `cfs-pv` 为例。
	- **Provisioner**：选择**文件存储CFS**。
	- **读写权限**：文件存储仅支持多机读写。
	- **StorageClass**：按需选择合适的 StorageClass。本文以选择在 [通过控制台创建 StorageClass](#createStorageClass) 步骤中创建的 `cfs-storageclass` 为例。
>? 
>- PVC 和 PV 会绑定在同一个 StorageClass 下。
>- 不指定 StorageClass 意味着该 PV 对应的 StorageClass 取值为空，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。
	- **选择CFS**：需确保文件存储与当前集群处于同一私有网络下，本文以选择在 [创建文件存储](#createCFS) 步骤中创建的 `cfs-test` 为例。
	- **CFS子目录**：填写已在步骤 [获取文件系统子目录](#getPath) 中获取的文件系统子路径，本文以 `/subfolder` 为例。
5. 单击**创建PersistentVolume**，即可完成创建。



### 创建 PVC[](id:createPVC2)
1.  在目标集群详情页，选择左侧菜单栏中的**存储** > **PersistentVolumeClaim**，进入 “PersistentVolumeClaim” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/1e33ff549656ade2836b91bb5d718201.png)
2. 选择**新建**进入“新建PersistentVolumeClaim” 页面，参考以下信息设置 PVC 关键参数。如下图所示：
![](https://main.qcloudimg.com/raw/a4dd41cd00d155fde6c1f7c9e6f5745a.png)
   - **名称**：自定义，本文以 `cfs-pvc` 为例。
   - **命名空间**：选择 “default”。
   - **Provisioner**：选择**文件存储CFS**。
   - **读写权限**：文件存储仅支持多机读写。
   - **StorageClass**：按需选择合适的 StorageClass。本文以选择在 [通过控制台创建 StorageClass](#createStorageClass) 步骤中创建的 `cfs-storageclass` 为例。
   >?
   >
   >- PVC 和 PV 会绑定在同一个 StorageClass 下。
>- 不指定意味着该 PVC 对应的 StorageClass 取值为空，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。
> 
   - **PersistVolume**：按需指定PersistentVolume，本文选择以在[ 静态创建 PV ](#pv) 步骤中创建的 `cfs-pv` 为例。
>? 
>- 只有与指定的 StorageClass 相同并且状态为 Available 和 Released 的 PV 为可选状态，如果当前集群内没有满足条件的 PV 可选，请选择“不指定”PersistVolume。
>- 如果选择的 PV 状态为 Released，还需手动删除该 PV 对应 YAML 配置文件中的 `claimRef` 字段，该 PV 才能顺利与 PVC 绑定。详情请参见 [查看 PV 和 PVC 的绑定规则](https://cloud.tencent.com/document/product/457/47014)。
3. 选择**创建PersistentVolumeClaim**，即可完成创建。


### 创建 Workload 使用 PVC 数据卷
>?该步骤以创建工作负载 Deployment 为例。
>
1. 在“集群管理”页面，选择目标集群 ID，进入待部署 Workload 的集群的 “Deployment” 页面。
2. 单击**新建**，进入“新建Workload” 页面，参考[ 创建 Deployment ](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)进行创建，并参考以下信息进行数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/813ba45a062ed57f8959121e484537d1.png)
	- **数据卷（选填）**：
		- **挂载方式**：选择“使用已有PVC”。
		- **数据卷名称**：自定义，本文以 `cfs-vol` 为例。
		- **选择 PVC**：选择在步骤 [创建 PVC](#createPVC2) 中已创建的 “cfs-pvc”。
	- **实例内容器**：单击**添加挂载点**，进行挂载点设置。
       - **数据卷**：选择该步骤中已添加的数据卷“cfs-vol”。
       - **目标路径**：填写目标路径，本文以 `/cache` 为例。
       - **挂载子路径**：仅挂载选中数据卷中的子路径或单一文件。例如， `/data` 或 `/test.txt`。
3. 单击**创建Workload**，完成创建。
 >! 如使用 CFS 的 PVC 挂载模式，数据卷支持挂载到多台 Node 主机上。

