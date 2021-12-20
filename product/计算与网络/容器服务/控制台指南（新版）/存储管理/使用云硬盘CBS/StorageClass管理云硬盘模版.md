## 操作场景

集群管理员可使用 StorageClass 为容器服务集群定义不同的存储类型。容器服务已默认提供块存储类型的 StorageClass，您可通过 StorageClass 配合 PersistentVolumeClaim 动态创建需要的存储资源。

本文介绍通过控制台、Kubectl 两种方式创建云硬盘 CBS 类型的 StorageClass，自定义云硬盘使用所需的模板。

## 操作步骤
### 控制台操作指引

#### 创建 StorageClass[](id:create)
1. 登录[ 容器服务控制台 ](https://console.cloud.tencent.com/tke2)，选择左侧栏中的**集群**。
2. 在“集群管理”页中，单击需创建 StorageClass 的集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**存储** > **StorageClass**。如下图所示：
![](https://main.qcloudimg.com/raw/18a3d5587e381e73328839b9186e071b.png)
4. 单击**新建**进入“新建StorageClass” 页面，参考以下信息进行创建。如下图所示：
![](https://main.qcloudimg.com/raw/e3984211f83d506aa1116ffc39f47747.png)
主要参数信息如下：
	- **名称**：自定义，本文以 `cbs-test` 为例。
	- **Provisioner**：选择**云硬盘CBS**。
	- **地域**：当前集群所在地域。
	- **可用区**：表示当前地域下支持使用云硬盘的可用区，请按需选择。
	- **计费模式**：提供**按量计费**和**包年包月**两种计费模式，不同计费模式所支持的回收策略不同，请参考以下信息进行选择：  
		- **按量计费**：一种弹性计费模式，支持随时开通/销毁实例，按实例的实际使用量付费。支持删除和保留的回收策略。
		- **包年包月**：一种预付费模式，提前一次性支付一个月的存储费用，支持按月自动续费。仅支持保留的回收策略。
<dx-alert infotype="explain" title="">
- 如需购买包年包月云硬盘，则需前往 [角色](https://console.cloud.tencent.com/cam/role) 页面，为 `TKE_QCSRole` 角色添加策略  `QcloudCVMFinanceAccess` 配置支付权限，否则可能会因支付权限问题导致创建基于包年包月 StorageClass 的 PVC 失败。
- 仅计费模式为包年包月的云硬盘可执行续费操作，自动续费功能默认按月续费。用户可前往所创建的PVC详情页，打开/关闭自动续费功能。更多计费信息参见  [云硬盘计费问题](https://cloud.tencent.com/document/product/213/17281)。
</dx-alert>
	- **云盘类型**：通常提供**高性能云硬盘**、**SSD云硬盘**和**增强型SSD云硬盘**三种类型，不同可用区下提供情况有一定差异，详情请参见 [云硬盘类型说明 ](https://cloud.tencent.com/document/product/213/32811)并结合控制台提示进行选择。
	- **回收策略**：云盘的回收策略，通常提供**删除**和**保留**两种回收策略，具体选择情况与所选计费模式相关。出于数据安全考虑，推荐使用保留回收策略。
	- **卷绑定模式**：提供**立即绑定**和**等待调度**两种卷绑定模式，不同模式所支持的卷绑定策略不同，请参考以下信息进行选择：
		- **立即绑定**：通过该 storageclass 创建的 PVC 将直接进行 PV 的绑定和分配。
		- **等待调度**：通过该 storageclass 创建的 PVC 将延迟与 PV 的绑定和分配，直到使用该 PVC 的 Pod 被创建。
	- **定期备份**：设置定期备份可有效保护数据安全，备份数据将产生额外费用，详情请见 [快照概述](https://cloud.tencent.com/document/product/362/5754)。
>? 容器服务默认提供的 default-policy 备份策略的配置包括：执行备份的日期、执行备份的时间点和备份保留的时长。
>
5. 单击**新建StorageClass**即可完成创建。

#### 使用指定 StorageClass 创建 PVC[](id:createPVC)
1. 在“集群管理”页面，选择需创建 PVC 的集群 ID。
2. 在集群详情页面，选择左侧菜单栏中的**存储** > **PersistentVolumeClaim**，进入 “PersistentVolumeClaim” 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/e771b0d7e010605c3701de3f20831a96.png)
3. 单击**新建**进入“新建PersistentVolumeClaim” 页面，参考以下信息设置 PVC 关键参数。如下图所示：
![](https://main.qcloudimg.com/raw/c1099db788c2f8f284df7616d7273a77.png)
主要参数信息如下：
   - **名称**：自定义，本文以 `cbs-pvc` 为例。
   - **命名空间**：选择 “default”。
   - **Provisioner**：选择**云硬盘CBS**。
   - **读写权限**：云硬盘仅支持单机读写。
   - **StorageClass**：按需指定 StorageClass，本文选择已在 [创建 StorageClass](#create) 步骤中创建的 `cbs-test` 为例。
>?
>- PVC 和 PV 会绑定在同一个 StorageClass 下。
>- 不指定 StorageClass 意味着该 PVC 对应的 StorageClass 取值为空，对应 YAML 文件中的 `storageClassName` 字段取值为空字符串。
> 
   - **PersistVolume**：按需指定 PersistentVolume，本文以不指定 PersistentVolume 为例。
>? 
>- 系统首先会筛选当前集群内是否存在符合绑定规则的 PV，如果没有则根据 PVC 和所选 StorageClass 的参数动态创建 PV 与之绑定。
>- 系统不允许在不指定 StorageClass 的情况下同时选择不指定 PersistVolume。
>- 不指定 PersistentVolume。详情请参见 [查看 PV 和 PVC 的绑定规则](https://cloud.tencent.com/document/product/457/47014)。
> 
   - **云盘类型**：根据所选的 StorageClass 展示所选的云盘类型为**高性能云硬盘**、**SSD云硬盘**和**增强型SSD云硬盘**。
   - **容量**：在不指定 PersistentVolume 时，需提供期望的云硬盘容量。
   - **费用**：根据上述参数计算创建对应云盘的所需费用，详情参考 [计费模式](https://cloud.tencent.com/document/product/362/32361)。
4. 单击**创建PersistentVolumeClaim**，即可完成创建。

#### 创建 StatefulSet 挂载 PVC 类型数据卷
>?该步骤以创建工作负载 StatefulSet 为例。
>
1. 在目标集群详情页，选择左侧菜单栏中的**工作负载** > **StatefulSet**，进入 “StatefulSet” 页面。
2. 单击**新建**进入“新建Workload” 页面，参考[ 创建 StatefulSet ](https://cloud.tencent.com/document/product/457/31707#createStatefulSet)进行创建，并参考以下信息进行数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/f199ac6bdd9f926283916c4258502b55.png)
	- **数据卷（选填）**：
		- **挂载方式**：选择“使用已有PVC”。
		- **数据卷名称**：自定义，本文以 `cbs-vol` 为例。
		- **选择 PVC**：选择已有 PVC，本文以选择在 [使用指定 StorageClass 创建 PVC](#createPVC) 步骤中创建的 `cbs-pvc` 为例。
	- **实例内容器**：单击**添加挂载点**，进行挂载点设置。
		- **数据卷**：选择该步骤中已添加的数据卷 “cbs-vol”。
		- **目标路径**：填写目标路径，本文以 `/cache` 为例。
		- **挂载子路径**：仅挂载选中数据卷中的子路径或单一文件。例如，`/data` 或 `/test.txt`。
4. 单击**创建Workload**，即可完成创建。
>! 如使用 CBS 的 PVC 挂载模式，则数据卷只能挂载到一台 Node 主机上。

### Kubectl 操作指引
您可参考本文提供的示例模板，使用 Kubectl 进行 StorageClass 创建操作。


#### 创建 StorageClass
以下 YAML 文件示例为集群内默认存在 name 为 cbs 的 StorageClass：
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  # annotations:
  #   storageclass.beta.kubernetes.io/is-default-class: "true"
  #   如果有这一条，则会成为 default-class，创建 PVC 时不指定类型则自动使用此类型
   name: cloud-premium
provisioner: cloud.tencent.com/qcloud-cbs ## TKE 集群自带的 provisioner
parameters:
   type: CLOUD_PREMIUM
  # 支持 CLOUD_PREMIUM,CLOUD_SSD,CLOUD_HSSD 如果不识别则当做 CLOUD_PREMIUM
  # renewflag: NOTIFY_AND_AUTO_RENEW
  # renewflag为云硬盘的续费模式，NOTIFY_AND_AUTO_RENEW模式支持通知过期且按月自动续费，NOTIFY_AND_MANUAL_RENEW模式支持通知过期但不支持自动续费，DISABLE_NOTIFY_AND_MANUAL_RENEW模式支持不通知过期也不自动续费。不指定该字段则默认为NOTIFY_AND_MANUAL_RENEW模式。
  # paymode: PREPAID
  # paymode为云盘的计费模式，PREPAID模式（包年包月：仅支持Retain保留的回收策略），默认是 POSTPAID（按量计费：支持 Retain 保留和 Delete 删除策略，Retain 仅在高于1.8的集群版本生效）
  # aspid:asp-123
  # 支持指定快照策略，创建云盘后自动绑定此快照策略,绑定失败不影响创建
```
支持参数如下表：
<table>
<tr>
<th>参数</th> <th>描述</th>
</tr>
<tr>
<td>type</td> <td>包括 CLOUD_PREMIUM（高性能云硬盘）和 CLOUD_SSD（SSD 云硬盘）、CLOUD_HSSD（增强型 SSD 云硬盘）。</td>
</tr>
<tr>
<td>zone</td> <td>用于指定可用区。如果指定，则云硬盘将创建到此可用区。如果不指定，则拉取所有 Node 的可用区信息，进行随机选取。 腾讯云各地域标识符请参见 <a href="https://cloud.tencent.com/document/product/213/6091">地域和可用区</a>。</td>
</tr>
<tr>
<td>paymode</td> <td>云硬盘的计费模式，默认设置为 <code>POSTPAID</code> 模式，即按量计费，支持 Retain 保留和 Delete 删除策略，Retain 仅在高于1.8的集群版本生效。还可设置为 <code>PREPAID</code> 模式，即包年包月，仅支持 Retain 保留策略。</td>
</tr>
<tr>
<td>renewflag</td> <td>云硬盘的续费模式。默认为 <code>NOTIFY_AND_MANUAL_RENEW</code> 模式。<ul><li><code>NOTIFY_AND_AUTO_RENEW</code> 模式代表所创建的云硬盘支持通知过期且按月自动续费。</li><li><code>NOTIFY_AND_MANUAL_RENEW</code> 模式代表所创建的云硬盘支持通知过期但不自动续费。</li><li> <code>DISABLE_NOTIFY_AND_MANUAL_RENEW</code> 模式则代表所创建的云硬盘不通知过期也不自动续费。</li></ul></td>
</tr>
<tr>
<td>aspid</td> <td>指定快照 ID，创建云硬盘后自动绑定此快照策略，绑定失败不影响创建。</td>
</tr>
</table>


#### 创建多实例 StatefulSet

使用云硬盘创建多实例 StatefulSet，YAML 文件示例如下：
<dx-alert infotype="explain" title="">
资源对象的 apiVersion 可能因为您集群的 Kubernetes 版本不同而不同，您可通过 `kubectl api-versions` 命令查看当前资源对象的 apiVersion。
</dx-alert>
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:  # 自动创建pvc，进而自动创建pv
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: cloud-premium
      resources:
        requests:
          storage: 10Gi
```
