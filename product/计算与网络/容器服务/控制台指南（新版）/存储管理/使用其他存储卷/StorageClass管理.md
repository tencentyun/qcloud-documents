## 简介

StorageClass 描述存储的类型，集群管理员可以为集群定义不同的存储类别。腾讯云 TKE 服务默认提供块存储类型的 StorageClass，通过 StorageClass 配合 PersistentVolumeClaim 可以动态创建需要的存储资源。

## StorageClass 控制台操作指引

### 创建 StorageClass

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击需要创建 StorageClass 的集群 ID，进入待创建 StorageClass 的集群管理页面。
4. 选择 “存储” > “StorageClass”，进入 StorageClass 信息页面。如下图所示：
![StorageClass](https://main.qcloudimg.com/raw/bdb7535c8b7d5b9a9b23239c8427357e.png)
5. 单击**新建**，进入 “新建StorageClass” 页面。如下图所示：
![新建StorageClass](https://main.qcloudimg.com/raw/dfbe33b52731d9b180dfb2ffc856adca.png)
6. 根据实际需求，设置 StorageClass 参数。关键参数信息如下：
 - 名称：自定义。
 - 计费模式：根据实际需求进行选择。
 - 可用区：根据实际需求进行设置，默认为 “随机可用区”。
 - 云盘类型：根据实际需求进行选择。
 - 回收策略：根据实际需求进行选择。
7. 单击**创建StorageClass**，完成创建。

### 创建 PVC 指定 StorageClass

参照 [PV 和 PVC 管理](https://cloud.tencent.com/document/product/457/31712) 中的 “[创建 PVC](https://cloud.tencent.com/document/product/457/31712#createPVC2)”，创建 PVC。并在设置 PVC 参数时，设置 StorageClass 参数。

### 创建 StatefulSet 挂载自动创建 PersistentVolumeClaim 类型

参照 [StatefulSet 管理](https://cloud.tencent.com/document/product/457/31707) 中的 “[创建 StatefulSet](https://cloud.tencent.com/document/product/457/31707#createStatefulSet)”，创建 StatefulSet。并在设置 StatefulSet 参数时，单击**添加数据卷**，选择 “使用新的 PVC” 方式，设置 PVC。如下图所示：
![](https://main.qcloudimg.com/raw/34f50be497c21d28423afe3bf68baba1.png)

## Kubectl 操作 StorageClass 指引

以下仅提供示例文件，您可直接通过 Kubectl 进行创建操作。

### 创建 StorageClass

如果不创建 StorageClass， 集群内将默认存在 name 为 CBS 的 StorageClass。
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
支持参数有：
- type：StorageClass 的类型，包括 CLOUD_BASIC、CLOUD_PREMIUM 和 CLOUD_SSD（注意全大写）。
- zone：指定 zone。如果指定，则云盘将创建到此 zone；如果不指定，则拉取所有 node 的 zone 信息，随机选取一个 zone。 腾讯云各地域标识符请参见 [地域和可用区](https://cloud.tencent.com/document/product/213/6091)。
- paymode：云盘的计费模式，默认设置为 POSTPAID 模式（即按量计费，支持 Retain 保留和 Delete 删除策略，Retain 仅在高于1.8的集群版本生效）。还可设置为 PREPAID 模式（即包年包月，仅支持 Retain 保留的回收策略）。
- aspid：指定快照 ID，创建云盘后自动绑定此快照策略，绑定失败不影响创建。

### 创建多实例 StatefulSet

使用云硬盘 CBS 创建多实例 StatefulSet，示例如下所示：
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


