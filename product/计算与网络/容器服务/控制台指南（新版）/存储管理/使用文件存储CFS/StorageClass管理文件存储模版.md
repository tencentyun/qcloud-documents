## 操作场景
集群管理员可使用 StorageClass 为容器服务集群定义不同的存储类型。容器服务已默认提供块存储类型的 StorageClass，您可通过 StorageClass 配合 PersistentVolumeClaim 动态创建需要的存储资源。

本文介绍通过控制台、Kubectl 两种方式创建文件存储 CFS 类型的 StorageClass，自定义文件存储使用所需的模板。

## 准备工作
### 安装文件存储扩展组件
>? 若您的集群已安装 CFS-CSI 的扩展组件，则请跳过此步骤。
>
1. 登录 [容器服务控制台 ](https://console.cloud.tencent.com/tke2)。
2. 单击左侧导航栏中的**集群**，进入**集群管理**页面。
3. 选择需新建组件的集群 ID，进入**集群详情**页面。
4. 在“集群详情页”，选择**组件管理** > **新建**，进入**新建组件**页面。
5. 在“新建组件”页面，勾选**CFS（腾讯云文件存储）**并单击**完成**即可。

### 创建子网
创建 StorageClass 过程中，需设置文件存储归属子网，为确保文件存储所处私有网络下每一个可用区均拥有合适子网，建议您提前进行子网创建。

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，单击左侧导航栏中的**子网**。
2. 在“子网”列表页面单击**+新建**，在弹出的“创建子网”窗口中设置子网名称、VPC 网段、CIDR、可用区和关联路由表等基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/6ca20ffe56545f924a1bb7e8a58b5110.png)
3. （可选）单击**+新增一行**，可以同时创建多个子网。
4. 单击**创建**即可。

### 创建权限组并添加权限组规则
创建 StorageClass 过程中，需为文件系统配置权限组，为确保具备合适的权限组，建议您提前进行权限组创建。

1. 登录 [ 文件存储控制台 ](https://console.cloud.tencent.com/cfs)，选择左侧导航栏中的**权限组**。
2. 在“权限组”页面单击**新建**，在弹出的“创建权限组”窗口中配置权限组名称和备注。
3. 单击**确定**，完成创建即可在“权限组”页面进行查看。
4. 单击该权限组 ID，进入其详情页，可进行权限组规则的添加、编辑或删除操作。如果权限组中没有添加规则，则会允许全部。详情请参见 [ 添加权限组规则](https://cloud.tencent.com/document/product/582/10951#.E6.B7.BB.E5.8A.A0.E6.9D.83.E9.99.90.E7.BB.84.E8.A7.84.E5.88.99)。

### 获取文件系统 FSID
1. 在 [文件系统控制台](https://console.cloud.tencent.com/cfs/fs?rid=1)，单击需获取 FSID 的文件系统 ID，进入该文件系统详情页。
2. 选择**挂载点信息**页签，从 “Linux 下挂载” 获取该文件系统的 FSID。如下图所示， `a43qadkl`为该文件系统的 FSID。
![](https://qcloudimg.tencent-cloud.cn/raw/981aff01c8e414bcbf657d01fed1762d.png)
>? 为了获取更好的稳定性，在通过 YAML 创建 PV 并使用 NFSV3 协议挂载时，需要指定待挂载文件系统对应的 FSID。

## 操作步骤
### 控制台操作指引

[](id:create)
#### 通过控制台创建 StorageClass
1. 登录 [ 容器服务控制台  ](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**存储** > **StorageClass**，进入 “StorageClass” 页面。如下所示：
![](https://main.qcloudimg.com/raw/a630fa854ae6a45da2b24dcbabf50438.png)
4. 单击**新建**，进入“新建 StorageClass” 页面，参考以下信息进行创建。如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0de0875f38b2a77d584527294571352e.png)
主要参数信息如下：
   - **名称**：自定义，本文以 `cfs-storageclass` 为例。
   - **Provisioner**：选择**文件存储 CFS**。
   - **可用区**：表示当前地域下支持使用文件存储的可用区，每个地域下不同可用区所适用的存储类型不完全一致，请参考 [ 可用地域 ](https://cloud.tencent.com/document/product/582/43623) 进行选择。
   -  **CFS 归属子网**：设置当前可用区下文件系统的所属子网范围，请按需选择。
   - **存储类型**：文件存储提供**标准存储**和**性能存储**两种类型的文件系统，每个地域下不同可用区所适用的存储类型不完全一致，请结合控制台实际情况进行选择。
     - **标准存储**：低成本、大容量，适用于成本敏感及大容量的业务。例如数据备份、文件共享、日志存储等场景。
     - **性能存储**：高吞吐、高 IOPS，适用于 IO 密集型工作负载。例如高性能计算、媒资渲染、机器学习、DevOps、办公 OA 等场景。
   - **文件服务协议**：默认为 NFS 协议，允许透明访问服务器上的文件和文件系统。
   - **协议版本**：推荐使用 NFSV3 协议挂载获得更好的性能，如果您的应用依赖文件锁（即需要使用多台 CVM 同时编辑一个文件）请使用 NFSV4 协议挂载。
   - **权限组**：为文件系统配置权限组，便于进一步管理与文件系统处于同一网络下的来访客户端的访问权限及读写权限。请根据实际需求选择合适的权限组，如不具备，请前往 [权限组](https://console.cloud.tencent.com/cfs/permission) 页面进行创建。
   - **回收策略**：提供**删除**和**保留**两种回收策略，出于数据安全考虑，推荐使用保留回收策略。
      - **删除**：通过 PVC 动态创建的 PV，在 PVC 销毁时，与其绑定的 PV 和存储实例也会自动销毁。
      - **保留**：通过 PVC 动态创建的 PV，在 PVC 销毁时，与其绑定的 PV 和存储实例会被保留。
   - **标签**：选择 CFS 实例需要绑定的云标签。该标签将由 StorageClass 动态创建的 CFS 实例自动继承，StorageClass 创建后其绑定的标签参数不支持修改。如现有标签不符合您的要求，请前往 [标签控制台](https://console.cloud.tencent.com/tag/taglist) 操作。
5. 单击 **新建 StorageClass** 即可。

#### 使用指定 StorageClass 创建 PVC[](id:createPVC)
1. 在“集群管理”页，选择需创建 PVC 的集群 ID。
2. 在集群详情页，选择左侧菜单栏中的**存储** > **PersistentVolumeClaim**，进入 “PersistentVolumeClaim” 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/e771b0d7e010605c3701de3f20831a96.png)
3. 选择**新建**进入“新建 PersistentVolumeClaim” 页面，参考以下信息设置 PVC 关键参数。如下图所示：
![](https://main.qcloudimg.com/raw/17d188dba93ffa0c50818144d4a20378.png)
主要参数信息如下：
   - **名称**：自定义，本文以 `cfs-pvc` 为例。
   - **命名空间**：选择 “default ”。
   - **Provisioner**：选择**文件存储 CFS**。
   - **读写权限**：文件存储仅支持多机读写。
   - **StorageClass**：按需指定 StorageClass，本文选择以在 [创建 StorageClass](#create) 步骤中创建的 `cfs-storageclass` 为例。
>? 
>- PVC 和 PV 会绑定在同一个 StorageClass 下。
>- 不指定 StorageClass 意味着该 PVC 对应的 StorageClass 取值为空，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。
> 
   - **PersistVolume**：按需指定 PersistentVolume，本文以不指定 PersistentVolume 为例。
>? 
>- 系统首先会筛选当前集群内是否存在符合绑定规则的 PV，若没有则根据 PVC 和所选 StorageClass 的参数动态创建 PV 与之绑定。
>- 系统不允许在不指定 StorageClass 的情况下同时选择不指定 PersistVolume。
>- 不指定 PersistVolume。详情请参见 [查看 PV 和 PVC 的绑定规则](https://cloud.tencent.com/document/product/457/47014)。
> 
4. 单击**创建 PersistentVolumeClaim**，即可完成创建。

#### 创建 Workload 使用 PVC 数据卷
>? 该步骤以创建工作负载 Deployment 为例。
>
1. 在“集群管理”页面，选择目标集群 ID，进入待部署 Workload 的集群的 “Deployment” 页面。
2. 选择**新建**，进入“新建 Workload” 页面，参考 [ 创建 Deployment ](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 进行创建，并参考以下信息进行数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/813ba45a062ed57f8959121e484537d1.png)
  - **数据卷（选填）**：
    - **挂载方式**：选择“使用已有 PVC”。
    - **数据卷名称**：自定义，本文以 `cfs-vol` 为例。
    - **选择 PVC**：选择在步骤 [创建 PVC](#createPVC) 中已创建的 “cfs-pvc”。
  - **实例内容器**：单击**添加挂载点**，进行挂载点设置。
       - **数据卷**：选择该步骤中已添加的数据卷“cfs-vol”。
       - **目标路径**：填写目标路径，本文以 `/cache` 为例。
       - **挂载子路径**：仅挂载选中数据卷中的子路径或单一文件。例如， `/data` 或 `/test.txt`。
3. 单击**创建 Workload**，完成创建。
>! 如使用 CFS 的 PVC 挂载模式，数据卷支持挂载到多台 Node 主机上。

### Kubectl 操作指引

#### 创建 StorageClass
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cfs
parameters:
  vpcid: vpc-xxxxxxxx
  subnetid: subnet-xxxxxxxx
  vers: "3"
  resourcetags: ""
provisioner: com.tencent.cloud.csi.cfs
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

parameters 支持参数如下：
| 参数 | 是否可选 | 描述 |
| -- | -- | -- |
|zone|否|设置文件存储所在的地域。|
|pgroupid|否|设置文件存储所归属的权限组。|
|storagetype|否|默认为标准存储 SD，可取值及描述如下：SD：标准型存储 HP：性能存储|
|vpcid|是|创建的文件存储所在的私有网络 ID。|
|subnetid|是|创建的文件存储所在的子网 ID。|
|vers|是|插件连接文件系统时所使用的协议版本，动态生成的 PV 会继承该参数，目前支持的版本有 "3" 和 "4"。|
|resourcetags|是|文件系统云标签，生成的文件系统上会打上对应腾讯云标签，多个标签由英文逗号隔开，例如 "a:b,c:d"。|

#### 创建 PVC
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cfs
  namespace: default
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  storageClassName: cfs
  volumeMode: Filesystem
  volumeName: XXX
```

| 参数 | 是否可选 | 描述 |
| -- | -- | -- |
|spec.accessModes|否|cfs 存储支持多读多写|
|spec.resources.requests.storage|是|无实际意义，具体存储大小只与文件系统种类有关。|
>? 
> 1. CFS 文件存储系统支持根据文件容量大小自动扩展文件系统存储容量，扩展过程不会中断请求和应用。默认创建的 CFS 实例容量大小为 10Gi，容量上限与产品类型相关，详情根据请参考 [系统限制](https://cloud.tencent.com/document/product/582/9135)。
> 2. 通过 PVC 动态创建的 PV 将自动继承 StorageClass 中设定的参数，该参数由存储插件自动生成。
