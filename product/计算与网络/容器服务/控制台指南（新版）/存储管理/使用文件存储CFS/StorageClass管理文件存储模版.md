## 操作场景
集群管理员可使用 StorageClass 为容器服务集群定义不同的存储类型。容器服务已默认提供块存储类型的 StorageClass，您可通过 StorageClass 配合 PersistentVolumeClaim 动态创建需要的存储资源。

本文介绍通过控制台、Kubectl 两种方式创建文件存储 CFS 类型的 StorageClass，自定义文件存储使用所需的模板。

## 准备工作
#### 1. 安装文件存储扩展组件
 若您的集群已安装 CFS-CSI 的扩展组件，请跳过此步骤。若未安装，详细步骤请参见 [安装文件存储扩展组件](https://cloud.tencent.com/document/product/457/44234#.E5.AE.89.E8.A3.85.E6.96.87.E4.BB.B6.E5.AD.98.E5.82.A8.E6.89.A9.E5.B1.95.E7.BB.84.E4.BB.B6)。




#### 2. 创建子网
创建 StorageClass 过程中，需设置文件存储归属子网，为确保文件存储所处私有网络下每一个可用区均拥有合适子网，建议您提前进行子网创建。若无子网，详细步骤请参见 [创建子网](https://cloud.tencent.com/document/product/215/36517)。 

#### 3. 创建权限组并添加权限组规则
创建 StorageClass 过程中，需为文件系统配置权限组，为确保具备合适的权限组，建议您提前进行权限组创建。若无权限组，详细步骤请参见 [创建权限组和添加权限组规则](https://cloud.tencent.com/document/product/582/10951)。

#### 4. 获取文件系统 FSID
1. 在 [文件系统控制台](https://console.cloud.tencent.com/cfs/fs?rid=1)，单击需获取 FSID 的文件系统 ID，进入该文件系统详情页。
2. 选择**挂载点信息**页签，从 “Linux 下挂载” 获取该文件系统的 FSID。如下图所示， `a43qadkl`为该文件系统的 FSID。
![](https://qcloudimg.tencent-cloud.cn/raw/93f0d2dc442b708579b796403a42bd29.png)
>? 为了获取更好的稳定性，在通过 YAML 创建 PV 并使用 NFSV3 协议挂载时，需要指定待挂载文件系统对应的 FSID。


## 控制台操作指引

[](id:create)
### 创建 StorageClass
1. 登录 [ 容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**存储 > StorageClass**，进入 “StorageClass” 页面。
4. 单击**新建**，在“新建 StorageClass” 页面，配置 StorageClass 参数。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fc0fad0d5e843fcc8a6e29826ba0fd74.png)
<table>
<thead>
  <tr>
    <th>配置项</th>
    <th>描述</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>名称</td>
    <td>填写 StorageClass 的名称。本文以 cfs-storageclass 为例。</td>
  </tr>
	  <tr>   
    <td>地域</td>
    <td>默认为集群所在地域。  </td>
  </tr>
  <tr>   
    <td>Provisioner</td>
    <td>Provisioner 支持选择<b>云硬盘CBS(CSI)</b>或<b>文件存储CFS</b>。此处选择<b>文件存储CFS</b>。</td>
  </tr>
  <tr>
    <td>实例创建模式</td>
    <td>提供<b>创建新实例</b>和<b>共享实例</b>两种模式。<ul><li>创建新实例：挂载时每个 PVC 默认创建一个 CFS 实例。</li><li>共享实例：挂载时每个 PVC 将共享同一 CFS 实例的不同子目录，共享的 CFS 实例及子目录由系统自动创建。</li>
		<dx-alert infotype="explain" title="">CFS-CSI 组件自 v1.0.1 版本开始支持<b>共享存储实例</b>功能，请及时升级组件版本，使用说明如下：
<li>共享实例类型的 StorageClass 回收策略限制为“保留”。</li>
<li>通过该 StorageClass 初次动态创建 PVC 时会默认创建一个 CFS 实例，并在该实例下创建子目录实现 PVC 之间的挂载隔离。</li>
<li>每个共享实例类型 StorageClass 创建的 CFS 实例不同，建议您妥善控制数量。</li></ul>
</dx-alert></td>
  </tr>
  <tr>
    <td>可用区</td>
    <td>选择当前地域下支持使用文件存储的可用区。每个地域下不同可用区所适用的存储类型不完全一致，请参考 <a href="https://cloud.tencent.com/document/product/582/43623">可用地域</a><a href="https://cloud.tencent.com/document/product/582/43623"> </a>进行选择。</td>
  </tr>
  <tr>
    <td>CFS 归属子网</td>
    <td>设置当前可用区下文件系统的所属子网范围。</td>
  </tr>
  <tr>
    <td>存储类型</td>
    <td>文件存储提供<b>标准存储</b>和<b>性能存储</b>两种类型的文件系统，每个地域下不同可用区所适用的存储类型不完全一致，请结合控制台实际情况进行选择。 <ul><li>标准存储：低成本、大容量，适用于成本敏感及大容量的业务。例如数据备份、文件共享、日志存储等场景。 </li><li>性能存储：高吞吐、高 IOPS，适用于 IO 密集型工作负载。例如高性能计算、媒资渲染、机器学习、DevOps、办公 OA 等场景。</li></ul></td>
  </tr>
  <tr>
    <td>文件服务协议</td>
    <td>默认为 NFS 协议，允许透明访问服务器上的文件和文件系统。</td>
  </tr>
  <tr>
    <td>协议版本</td>
    <td>推荐使用 NFS v3 协议挂载获得更好的性能。如果您的应用依赖文件锁（即需要使用多台 CVM 同时编辑一个文件）请使用 NFS v4 协议挂载。</td>
  </tr>
  <tr>
    <td>权限组</td>
    <td>为文件系统配置权限组，便于进一步管理与文件系统处于同一网络下的来访客户端的访问权限及读写权限。请根据实际需求选择合适的权限组，如不具备，请前往 <a href="https://console.cloud.tencent.com/cfs/permission">权限组</a> 页面进行创建。</td>
  </tr>
  <tr>
    <td>回收策略</td>
    <td>提供<b>删除</b>和<b>保留</b>两种回收策略，出于数据安全考虑，推荐使用<b>保留</b>回收策略。 <ul><li>删除：通过 PVC 动态创建的 PV，在 PVC 销毁时，与其绑定的 PV 和存储实例也会自动销毁。</li><li>保留：通过 PVC 动态创建的 PV，在 PVC 销毁时，与其绑定的 PV 和存储实例会被保留。</li></ul></td>
  </tr>
  <tr>
    <td>标签</td>
    <td>选择 CFS 实例需要绑定的云标签。该标签将由 StorageClass 动态创建的 CFS 实例自动继承，StorageClass 创建后其绑定的标签参数不支持修改。如现有标签不符合您的要求，请前往 <a href="https://console.cloud.tencent.com/tag/taglist">标签控制台</a> 操作。</td>
  </tr>
</tbody>
</table>
5. 单击 **新建 StorageClass** 即可。
 

### 使用指定 StorageClass 创建 PVC[](id:createPVC)
1. 在“集群管理”页，选择需创建 PVC 的集群 ID。
2. 在集群详情页，选择左侧菜单栏中的**存储** > **PersistentVolumeClaim**，进入 “PersistentVolumeClaim” 信息页面。
3. 选择**新建**进入“新建 PersistentVolumeClaim” 页面，配置 PVC 关键参数。如下图所示：
![](https://main.qcloudimg.com/raw/17d188dba93ffa0c50818144d4a20378.png)
<table>
<thead>
  <tr>
    <th>配置项</th>
    <th>描述</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>名称</td>
    <td>填写 PersistentVolumeClaim 的名称。本文以 cfs-pvc 为例。</td>
  </tr>
  <tr>
    <td>命名空间</td>
    <td>命名空间用来划分集群资源。此处选择 <b>default</b>。</td>
  </tr>
  <tr>
    <td>Provisioner</td>
    <td>选择文件存储 CFS。</td>
  </tr>
  <tr>
    <td>读写权限</td>
    <td>文件存储仅支持多机读写。</td>
  </tr>
  <tr>
    <td>StorageClass</td>
    <td>按需指定 StorageClass。本文选择<b>指定 StorageClass</b>，以在 <a href="https://cloud.tencent.com/document/product/457/44235#.E5.88.9B.E5.BB.BA-storageclass">创建 StorageClass</a> 步骤中创建的 cfs-storageclass 为例。
		<dx-alert infotype="explain" title="">
<ul><li>PVC 和 PV 会绑定在同一个 StorageClass 下。</li>
<li><b>不指定 StorageClass</b> 意味着该 PVC 对应的 StorageClass 取值为空，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。</li></ul>
</dx-alert>
		</td>
  </tr>
  <tr>
    <td>PersistVolume</td>
    <td>按需指定 PersistentVolume。本文选择<b>不指定 PersistentVolume</b>。
		<dx-alert infotype="explain" title=""><ul>
<li>系统首先会筛选当前集群内是否存在符合绑定规则的 PV，若没有则根据 PVC 和所选 StorageClass 的参数动态创建 PV 与之绑定。</li>
<li>系统不允许在不指定 StorageClass 的情况下同时选择不指定 PersistVolume。</li>
<li>关于<b>不指定 PersistVolume</b> 的详细介绍，请参见 <a href="https://cloud.tencent.com/document/product/457/47014">查看 PV 和 PVC 的绑定规则</a>。</li></ul>
</dx-alert>
</td>
  </tr>
</tbody>
</table>
4. 单击**创建 PersistentVolumeClaim**。

### 创建 Workload 使用 PVC 数据卷
>? 该步骤以创建工作负载 Deployment 为例。
>
1. 在“集群管理”页面，选择目标集群 ID，进入待部署 Workload 的集群的 “Deployment” 页面。
2. 选择**新建**，进入“新建 Workload” 页面，参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 进行创建，并参考以下信息进行数据卷挂载。如下图所示：
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

## Kubectl 操作指引

### 创建 StorageClass
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cfs
parameters:
  # subdir-share: "true" 
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
|---------|---------|---------|
| zone | 否 |设置文件存储所在的地域。|
|pgroupid|否|设置文件存储所归属的权限组。|
|storagetype|否|默认为标准存储 SD，可取值及描述如下：<br>SD：标准型存储 <br>HP：性能存储|
|subdir-share|是|填写则代表 StorageClass 的实例创建模式为共享实例。|
|vpcid|是|创建的文件存储所在的私有网络 ID。|
|subnetid|是|创建的文件存储所在的子网 ID。|
|vers|是|插件连接文件系统时所使用的协议版本，动态生成的 PV 会继承该参数，目前支持的版本有 "3" 和 "4"。|
|resourcetags|是|文件系统云标签，生成的文件系统上会打上对应腾讯云标签，多个标签由英文逗号隔开，例如 "a:b,c:d"。|

### 创建 PVC
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
  volumeName: XXX  #动态创建无需填写，静态创建需要在该字段中指定 pv 实例 id 
```

| 参数 | 是否可选 | 描述 |
| -- | -- | -- |
|spec.accessModes|否|cfs 存储支持多读多写|
|spec.resources.requests.storage|是|无实际意义，具体存储大小只与文件系统种类有关。|
>? 
> 1. CFS 文件存储系统支持根据文件容量大小自动扩展文件系统存储容量，扩展过程不会中断请求和应用。默认创建的 CFS 实例容量大小为 10Gi，容量上限与产品类型相关，详情根据请参考 [系统限制](https://cloud.tencent.com/document/product/582/9135)。
> 2. 通过 PVC 动态创建的 PV 将自动继承 StorageClass 中设定的参数，该参数由存储插件自动生成。
   
