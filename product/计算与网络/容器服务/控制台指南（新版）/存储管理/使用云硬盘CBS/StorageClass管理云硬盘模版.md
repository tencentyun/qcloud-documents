## 操作场景

集群管理员可使用 StorageClass 为容器服务集群定义不同的存储类型。容器服务已默认提供块存储类型的 StorageClass，您可通过 StorageClass 配合 PersistentVolumeClaim 动态创建需要的存储资源。

本文介绍通过控制台、Kubectl 两种方式创建云硬盘 CBS 类型的 StorageClass，自定义云硬盘使用所需的模板。

## 操作步骤
### 控制台操作指引

#### 创建 StorageClass<span id="create"></span>
1. 登录[ 容器服务控制台 ](https://console.cloud.tencent.com/tke2)，选择左侧栏中的【集群】，进入“集群管理”界面。
2. 单击需创建 StorageClass 的集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的【存储】>【StorageClass】，进入 “StorageClass” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/9e4085b33612d7c234c9e868d941e561.png)
4. 单击【新建】进入“新建StorageClass” 页面，参考以下信息进行创建。如下图所示：
![](https://main.qcloudimg.com/raw/5c10dbeed3d6a7073ce38ead2223d38d.png)
主要参数信息如下：
	- **名称**：自定义，本文以 `cbs-test` 为例。
	- **Provisioner**：选择【云硬盘CBS】。
	- **可用区**：表示当前地域下支持使用云硬盘的可用区，请按需选择。
	- **计费模式**：提供【按量计费】和【包年包月】两种计费模式，不同计费模式所支持的回收策略不同，请参考以下信息进行选择：  
		- **按量计费**：一种弹性计费模式，支持随时开通/销毁实例，按实例的实际使用量付费。支持删除和保留的回收策略。
		- **包年包月**：一种预付费模式，提前一次性支付一个或多个月甚至多年的费用。仅支持保留的回收策略。
>? 如需购买包年包月云硬盘，则需前往 [角色](https://console.cloud.tencent.com/cam/role) 页面，为 `TKE_QCSRole` 角色添加策略  `QcloudCVMFinanceAccess` 配置支付权限，否则可能会因支付权限问题导致创建基于包年包月 StorageClass 的 PVC 失败。
>
	- **云盘类型**：通常提供【普通云硬盘】、【高性能云硬盘】、【SSD云硬盘】三种类型，不同可用区下提供情况有一定差异，详情请参见 [云硬盘类型说明 ](https://cloud.tencent.com/document/product/213/32811)并结合控制台提示进行选择。
	- **回收策略**：云盘的回收策略，通常提供【删除】和【保留】两种回收策略，具体选择情况与所选计费模式相关。出于数据安全考虑，推荐使用保留回收策略。
5. 单击【新建StorageClass 】即可完成创建。

#### 使用指定 StorageClass 创建 PVC<span id="createPVC"></span>
1. 在“集群管理”页面，选择需创建 PVC 的集群 ID。
2. 在集群详情页面，选择左侧菜单栏中的【存储】>【PersistentVolumeClaim】，进入 “PersistentVolumeClaim” 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/e771b0d7e010605c3701de3f20831a96.png)
3. 单击【新建】进入“新建PersistentVolumeClaim” 页面，参考以下信息设置 PVC 关键参数。如下图所示：
![](https://main.qcloudimg.com/raw/358edb5da97cd63030437b5628fa4d79.png)
主要参数信息如下：
   - **名称**：自定义，本文以 `cbs-pvc` 为例。
   - **命名空间**：选择 “default”。
   - **Provisioner**：选择【云硬盘CBS】。
   - **读写权限**：云硬盘仅支持单机读写。
   - **StorageClass**：按需选择 StorageClass，本文以选择在 [创建 StorageClass](#create) 步骤中创建的 `cbs-test` 为例。
5. 单击【创建PersistentVolumeClaim】，即可完成创建。

#### 创建 StatefulSet 挂载 PVC 类型数据卷
>?该步骤以创建工作负载 StatefulSet 为例。
>
1. 在目标集群详情页，选择左侧菜单栏中的【工作负载】>【StatefulSet】，进入 “StatefulSet” 页面。
2. 单击【新建】进入“新建Workload” 页面，参考[ 创建 StatefulSet ](https://cloud.tencent.com/document/product/457/31707#createStatefulSet)进行创建，并参考以下信息进行数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/f199ac6bdd9f926283916c4258502b55.png)
	- **数据卷（选填）**：
		- **挂载方式**：选择“使用已有PVC”。
		- **数据卷名称**：自定义，本文以 `cbs-vol` 为例。
		- **选择 PVC**：选择已有 PVC，本文以选择在 [使用指定 StorageClass 创建 PVC](#createPVC) 步骤中创建的 `cbs-pvc` 为例。
	- **实例内容器**：单击【添加挂载点】，进行挂载点设置。
		- **数据卷**：选择该步骤中已添加的数据卷 “cbs-vol”。
		- **目标路径**：填写目标路径，本文以 `/cache` 为例。
		- **挂载子路径**：仅挂载选中数据卷中的子路径或单一文件。例如，`/data` 或 `/test.txt`。
4. 单击【创建Workload】，即可完成创建。

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
  # 支持 CLOUD_BASIC,CLOUD_PREMIUM,CLOUD_SSD  如果不识别则当做 CLOUD_BASIC
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
<td>type</td> <td>StorageClass 的类型，包括 <code>CLOUD_BASIC</code>、<code>CLOUD_PREMIUM</code> 和 <code>CLOUD_SSD</code>。</td>
</tr>
<tr>
<td>zone</td> <td>用于指定可用区。如果指定，则云硬盘将创建到此可用区。如果不指定，则拉取所有 Node 的可用区信息，进行随机选取。 腾讯云各地域标识符请参见 <a href="https://cloud.tencent.com/document/product/213/6091">地域和可用区</a>。</td>
</tr>
<tr>
<td>paymode</td> <td>云硬盘的计费模式，默认设置为 <code>POSTPAID</code> 模式，即按量计费，支持 Retain 保留和 Delete 删除策略，Retain 仅在高于1.8的集群版本生效。还可设置为 <code>PREPAID</code> 模式，即包年包月，仅支持 Retain 保留策略。</td>
</tr>
<tr>
<td>aspid</td> <td>指定快照 ID，创建云硬盘后自动绑定此快照策略，绑定失败不影响创建。</td>
</tr>
</table>


#### 创建多实例 StatefulSet

使用云硬盘创建多实例 StatefulSet，YAML 文件示例如下：
``` yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: web
spec:
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
