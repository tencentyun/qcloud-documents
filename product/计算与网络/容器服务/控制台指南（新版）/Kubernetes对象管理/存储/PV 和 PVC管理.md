## 简介

### 概述
PersistentVolume（PV）：集群内的存储资源，例如节点是集群的资源。PV 独立于 Pod 的生命周期，根据不同的 StorageClass 类型创建不同类型的 PV。
PersistentVolumeClaim（PVC）：集群内的存储请求。例如，PV 是 Pod 使用节点资源，PVC 则声明使用 PV 资源。当 PV 资源不足时，PVC 也可以动态创建 PV。



### 注意事项

- CBS 盘不支持跨可用区挂载。若挂载 CBS 类型 PV 的 Pod 迁移到其他可用区，将会导致挂载失败。
- TKE 控制台不支持 CBS 盘扩缩容，请自行前往 CBS 控制台执行操作。

## PV&PVC 控制台操作指引

### 静态创建 PV

静态创建 PV 适用于已有存量云盘,并在集群内使用的场景。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 PV 的集群 ID，进入待创建 PV 的集群管理页面。
4. 选择 “存储” > “PersistentVolume”，进入 PersistentVolume 信息页面。如下图所示：
   
   ![PersistentVolume](https://main.qcloudimg.com/raw/f18366db7dce49824e0d43dc4aeee516.png)
5. 单击【新建】，进入 “新建PersistentVolume” 页面。如下图所示：
   
   ![新建PersistentVolume](https://main.qcloudimg.com/raw/98cbf4ace819438faa51fa9add33330a.png)
6. 根据实际需求，设置 PV 参数。关键参数信息如下：
   - 来源设置：根据实际需求进行选择，默认为 “静态创建”。
   - 名称：自定义。
   - 选择云盘：根据实际需求进行选择。
   - StorageClass：根据实际需求进行选择。
7. 单击【创建PersistentVolume】，完成创建。

<span id="createPVC2"></span>

### 创建 PVC

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 PVC 的集群 ID，进入待创建 PVC 的集群管理页面。
4. 选择 “存储” > “PersistentVolumeClaim”，进入 PersistentVolumeClaim 信息页面。如下图所示：
   
   ![PersistentVolumeClaim](https://main.qcloudimg.com/raw/76cbf067c2f12c6e257c07d86300c818.png)
5. 单击【新建】，进入 “新建PersistentVolumeClaim” 页面。如下图所示：
   
   ![新建PersistentVolume](https://main.qcloudimg.com/raw/5b0c4d92f26e4c31d88a74435b52c6b5.png)
6. 根据实际需求，设置 PVC 参数。关键参数信息如下：
   - 名称：自定义。
   - 命名空间：根据实际需求进行选择命名空间类型。
   - StorageClass：根据实际需求进行选择。
   - 容量：根据实际需求进行设置。
7. 单击【创建PersistentVolumeClaim】，完成创建。
   
   > ? 若已有 PV 不足，系统将自动创建新的 PV。

### 创建 Workload 使用 PVC 数据卷

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择 “工作负载” > “DaemonSet”，进入 DaemonSet 信息页面。如下图所示：
   
   ![](https://main.qcloudimg.com/raw/73b214fcb0cf26e569310894dd44c512.png)
5. 单击【新建】，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击【添加数据卷】，添加数据卷。如下图所示：
   
   ![添加数据卷](https://main.qcloudimg.com/raw/110d1c5754b97df1388f39546263aaee.png)
7. 选择 “使用已有PVC” 方式，填写名称，选择已有的 PVC。如下图所示：
   
   ![使用已有PVC](https://main.qcloudimg.com/raw/aa1e843d3ea02d6af12298b6566e552b.png)
8. 单击【创建Workload】，完成创建。
   
   > !使用 PVC 挂载模式，数据卷只能挂载到一台 node 主机上

## Kubectl 操作 PV&PVC 指引

当前仅支持 CBS 类型的 PV&PVC。您可通过 [StorageClass 管理](https://cloud.tencent.com/document/product/457/31714) 指定 PV 绑定的云盘的类型。以下仅提供示例文件，您可直接通过 Kubectl 进行创建操作。

<span id="createPV"></span>

### （可选）创建 PV

通过已有 CBS 创建 PV。若未创建 PV，在 [创建 PVC](#createPVC) 时，系统将自动创建对应的 PV。

```Yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nginx-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  qcloudCbs:
      cbsDiskId: disk-xxxxxxx ## 指定已有的CBS id
      fsType: ext4
  storageClassName: cbs
```

<span id="createPVC"></span>

### 创建 PVC

若未 [创建 PV](#createPV)，在创建 PVC 时，系统将自动创建对应的 PV。YAML 示例如下：

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: nginx-pv-claim
spec:
  storageClassName: cbs
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

- 普通云盘大小必须是10的倍数，最小为10。
- 高效云盘最小为50GB。
- SSD 云硬盘最小为200GB，具体策略请参见 [云硬盘文档](https://cloud.tencent.com/document/product/362)。

### 使用 PVC

YAML 示例如下：

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      qcloud-app: nginx-deployment
  template:
    metadata:
      labels:
        qcloud-app: nginx-deployment
    spec:
      containers:
      - image: nginx
        imagePullPolicy: Always
        name: nginx
        volumeMounts:
        - mountPath: "/opt/"
          name: pvc-test
      volumes:
      - name: pvc-test
        persistentVolumeClaim:
          claimName: nginx-pv-claim # 已经创建好的 PVC
```
