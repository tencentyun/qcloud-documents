## 简介
PersistentVolume（PV）：集群内的存储资源。例如，节点是集群的资源。PV 独立于 Pod 的生命周期，根据不同的 StorageClass 类型创建不同类型的 PV。
PersistentVolumeClaim（PVC）：集群内的存储请求。例如，PV 是 Pod 使用节点资源，PVC 则声明使用 PV 资源。当 PV 资源不足时，PVC 也可以动态创建 PV。



## 注意事项

- CBS 盘不支持跨可用区挂载。若挂载 CBS 类型 PV 的 Pod 迁移到其他可用区，将会导致挂载失败。
- TKE 控制台不支持 CBS 盘扩缩容，请自行前往 [CBS 控制台](https://console.cloud.tencent.com/cvm/cbs/index) 执行操作。

## PV 及 PVC 控制台操作指引

### 静态创建 PV
>?静态创建 PV 适用于已有存量云盘，并在集群内使用的场景。
>
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需创建 PV 的集群 ID，进入待创建 PV 的集群管理页面。
3. 选择**存储** > **PersistentVolume**，进入 PersistentVolume 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/3a34484015631e655b62a346ef44a125.png)
4. 单击**新建**，进入 “新建PersistentVolume” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/7be60ba6a46605cc350f325fcdc203de.png)
5. 根据实际需求，设置 PV 参数。主要参数信息如下：
   - **来源设置**：参考以下信息按需选择，本文以选择**静态创建**为例。
   - **名称**：输入自定义名称。
   - **Provisioner**：按需选择 PV 类型，本文以选择**云硬盘CBS**为例。
   - **读写权限**：请按需选择，其中云硬盘只支持**单机读写**。
   - **选择云盘**：根据实际需求进行选择。
   - **StorageClass**：根据实际需求进行选择。
7. 单击**创建PersistentVolume**，完成创建。



### 创建 PVC[](id:createPVC2)
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需创建 PVC 的集群 ID，进入待创建 PVC 的集群管理页面。
3. 选择**存储** > **PersistentVolumeClaim**，进入 PersistentVolumeClaim 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/3c1f7fd04a9de9d3002a7bf53efe8477.png)
4. 单击**新建**，进入 “新建PersistentVolumeClaim” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/01754abcc90d606fc3c199d25f146779.png)
5. 根据实际需求，设置 PVC 参数。关键参数信息如下：
   - **名称**：输入自定义名称。
   - **命名空间**：根据实际需求进行选择命名空间类型。
   - **Provisioner**：按需选择 PVC 类型，本文以选择**云硬盘CBS**为例。
   - **读写权限**：请按需选择，其中云硬盘只支持**单机读写**。
   - **StorageClass**：根据实际需求进行选择。
   - **容量**：根据实际需求进行设置。云盘容量最小值由云硬盘产品规格决定，详情请参见 [云硬盘类型](https://cloud.tencent.com/product/cbs/types)。
6. 单击**创建PersistentVolumeClaim**，完成创建。
> ? 若已有 PV 不足，系统将自动创建新的 PV。

### 创建 Workload 使用 PVC 数据卷
1.  登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2.  单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
3. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。
![](https://main.qcloudimg.com/raw/087db7a85311be56aaf4b0bfbf60c886.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击**添加数据卷**，添加数据卷。如下图所示：
![](https://main.qcloudimg.com/raw/0101415b23de720a356aa43e4a910b1f.png)
6. 选择 “使用已有PVC” 方式，填写名称，选择已有的 PVC。如下图所示：
![](https://main.qcloudimg.com/raw/0d84058cd397d5001c4325d25576963d.png)
7. 单击**创建Workload**，完成创建。
 > !使用 PVC 挂载模式，数据卷只能挂载到一台 node 主机上

## Kubectl 操作 PV 及 PVC 指引

当前仅支持 CBS 及 CFS 类型的 PV 及 PVC。如选择 CBS 类型的 PV 及 PVC，您可通过 [StorageClass 管理](https://cloud.tencent.com/document/product/457/31714) 指定 PV 绑定的云盘的类型。以下仅提供示例文件，您可直接通过 Kubectl 进行创建操作。



### （可选）创建 PV[](id:createPV)

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



### 创建 PVC[](id:createPVC)

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

- 普通云盘大小必须是10的倍数，最小为10GB。
- 高性能云硬盘最小为50GB。
- SSD 云硬盘最小为100GB，详情请参见 [云硬盘类型](https://cloud.tencent.com/product/cbs/types)。

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
